#!/usr/bin/env python3
"""Helpers for the muse_fortune_kyusei_runes skill.

Commands:
  selftest                      Verify the Kyusei calculation against known anchors
                                and check the rune deck.
  chart YYYY-MM-DD              Print the 本命星 (honmeisei), 月命星 (getsumeisei)
                                and the current year's star.
  draw [n]                      Draw n runes by random lot (default 3), each with
                                upright / reversed. Symmetric runes have no
                                reversed position. Never draw twice for the same
                                question.

Requires the sxtwl library (pip install sxtwl), used only for the solar-term
boundaries （立春 for the year, 節入り for the month). If it is missing, this
script exits with an error instead of guessing: the stars must never be
hand-computed.
"""
import sys
import random
from datetime import date

try:
    import sxtwl
except ImportError:
    print("ERROR: sxtwl is not installed. Run: pip install sxtwl", file=sys.stderr)
    sys.exit(2)

STAR_NAMES = {
    1: "一白水星", 2: "二黒土星", 3: "三碧木星", 4: "四緑木星", 5: "五黄土星",
    6: "六白金星", 7: "七赤金星", 8: "八白土星", 9: "九紫火星",
}
STAR_ELEM = {1: "水", 2: "土", 3: "木", 4: "木", 5: "土", 6: "金", 7: "金", 8: "土", 9: "火"}

DZ = "子丑寅卯辰巳午未申酉戌亥"


def effective_year(y, m, d):
    """The Kyusei year: if the date is before 立春， it belongs to the previous year.
    Detected by comparing the sxtwl year pillar with mid-year (always after 立春）."""
    day = sxtwl.fromSolar(y, m, d)
    mid = sxtwl.fromSolar(y, 6, 1)
    gz_day = (day.getYearGZ().tg, day.getYearGZ().dz)
    gz_mid = (mid.getYearGZ().tg, mid.getYearGZ().dz)
    return y if gz_day == gz_mid else y - 1


def star_for_year(year):
    """本命星 number for a (Kyusei) year: digit-sum the year, subtract from 11."""
    s = sum(int(c) for c in str(year))
    while s > 9:
        s = sum(int(c) for c in str(s))
    return ((10 - s) % 9) + 1


def honmeisei(y, m, d):
    return star_for_year(effective_year(y, m, d))


def getsumeisei(y, m, d, honmei):
    """月命星： the 節月 index comes from the sxtwl month pillar's branch
    （寅月 = 0 ... 丑月 = 11). The 寅月 star depends on the 本命星 group and
    decreases by one each month."""
    day = sxtwl.fromSolar(y, m, d)
    dz = day.getMonthGZ().dz
    idx = (dz - 2) % 12  # 寅 = 2 in DZ order
    if honmei in (1, 4, 7):
        start = 8
    elif honmei in (2, 5, 8):
        start = 5
    else:  # 3, 6, 9
        start = 2
    return ((start - 1 - idx) % 9) + 1


def selftest():
    ok = True

    def check(label, got, exp):
        nonlocal ok
        good = got == exp
        ok = ok and good
        print(f"{'OK' if good else 'NG'}: {label} = {got} (expected {exp})")

    # 本命星 anchors (widely published), including the 立春 boundary.
    for (y, m, d), exp in [
        ((1970, 9, 25), 3),   # 三碧木星
        ((1984, 2, 5), 7),    # after 立春 -> 七赤金星
        ((1984, 2, 2), 8),    # before 立春 -> counts as 1983, 八白土星
        ((1990, 6, 15), 1),   # 一白水星
        ((2000, 6, 15), 9),   # 九紫火星
        ((2024, 6, 15), 3),   # 三碧木星
        ((1975, 6, 15), 7),   # 七赤金星
    ]:
        check(f"本命星 {y}-{m:02d}-{d:02d}", STAR_NAMES[honmeisei(y, m, d)], STAR_NAMES[exp])

    # 月命星 anchors from the published group table.
    for (y, m, d), exp in [
        ((1970, 9, 25), 4),   # 三碧・酉月 -> 四緑木星
        ((1990, 2, 10), 8),   # 一白・寅月 -> 八白土星
        ((1971, 2, 10), 5),   # 二黒・寅月 -> 五黄土星
        ((1984, 2, 5), 8),    # 七赤・寅月 -> 八白土星
    ]:
        h = honmeisei(y, m, d)
        check(f"月命星 {y}-{m:02d}-{d:02d}", STAR_NAMES[getsumeisei(y, m, d, h)], STAR_NAMES[exp])

    # Rune deck integrity.
    check("ルーン総数", len(RUNES), 24)
    check("ルーン重複なし", len({r[0] for r in RUNES}), 24)
    check("対称ルーン（逆位置なし）の数", sum(1 for r in RUNES if r[3]), 8)

    print("SELFTEST:", "ALL OK" if ok else "FAILED")
    return 0 if ok else 1


def chart(y, m, d):
    ey = effective_year(y, m, d)
    h = star_for_year(ey)
    g = getsumeisei(y, m, d, h)
    today = date.today()
    ynow = star_for_year(effective_year(today.year, today.month, today.day))
    print(f"九星の年（立春基準）: {ey}年")
    print(f"本命星: {STAR_NAMES[h]}（{STAR_ELEM[h]}）")
    print(f"月命星: {STAR_NAMES[g]}（{STAR_ELEM[g]}）")
    print(f"今年の九星: {STAR_NAMES[ynow]}（{STAR_ELEM[ynow]}）")
    return 0


# Elder Futhark, 24 runes: (name, rune char, keyword, symmetric = no reversed)
RUNES = [
    ("フェフ", "ᚠ", "豊かさ・お金の流れ", False),
    ("ウルズ", "ᚢ", "生命力・回復", False),
    ("スリサズ", "ᚦ", "守り・試練", False),
    ("アンスズ", "ᚨ", "言葉・知恵・知らせ", False),
    ("ライド", "ᚱ", "移動・リズム", False),
    ("ケナズ", "ᚲ", "ひらめき・学び", False),
    ("ゲボ", "ᚷ", "贈り物・交換", True),
    ("ウンヨ", "ᚹ", "喜び・調和", False),
    ("ハガラズ", "ᚺ", "嵐・リセット", True),
    ("ナウシズ", "ᚾ", "必要・忍耐", True),
    ("イサ", "ᛁ", "静止・待つ", True),
    ("ジェラ", "ᛃ", "収穫・周期", True),
    ("エイワズ", "ᛇ", "忍耐・軸", True),
    ("ペルスロ", "ᛈ", "運・秘密", False),
    ("アルジズ", "ᛉ", "守護・直感", False),
    ("ソウィロ", "ᛊ", "太陽・成功", True),
    ("ティワズ", "ᛏ", "勝利・正義", False),
    ("ベルカナ", "ᛒ", "成長・新しい始まり", False),
    ("エワズ", "ᛖ", "協力・前進", False),
    ("マンナズ", "ᛗ", "人・つながり", False),
    ("ラグズ", "ᛚ", "水・直感・流れ", False),
    ("イングワズ", "ᛜ", "内なる成長・種", False),
    ("ダガズ", "ᛞ", "夜明け・転機", True),
    ("オサラ", "ᛟ", "家・受け継ぐもの", False),
]


def draw(n=3):
    rng = random.SystemRandom()
    picked = rng.sample(RUNES, n)
    positions = ["現状", "課題", "助言"]
    for i, (name, char, kw, sym) in enumerate(picked):
        if sym:
            orient = "正位置（このルーンに逆位置はありません）"
        else:
            orient = "正位置" if rng.random() < 0.5 else "逆位置"
        label = positions[i] if n == 3 else f"{i + 1}つ目"
        print(f"{label}: {name} {char}（{orient}）― {kw}")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "selftest":
        sys.exit(selftest())
    elif cmd == "chart":
        y, m, d = map(int, sys.argv[2].split("-"))
        sys.exit(chart(y, m, d))
    elif cmd == "draw":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        sys.exit(draw(n))
    else:
        print(__doc__)
        sys.exit(1)
