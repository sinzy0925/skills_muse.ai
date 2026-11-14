#!/usr/bin/env python3
"""Helpers for the muse_fortune_shichusuimei_tarot skill.

Commands:
  selftest                      Verify the pillar calculation against known anchor charts.
  meishiki YYYY-MM-DD [HH:MM]   Print the four pillars, the day master, the five-element
                                balance, and the current year's pillar.
  draw [n]                      Draw n tarot cards by random lot (default 3), each with
                                upright / reversed. Never draw twice for the same question.

Requires the sxtwl library (pip install sxtwl). If it is missing, this script
exits with an error instead of guessing: the pillars must never be hand-computed.
"""
import sys
import random
from datetime import date

try:
    import sxtwl
except ImportError:
    print("ERROR: sxtwl is not installed. Run: pip install sxtwl", file=sys.stderr)
    sys.exit(2)

TG = "甲乙丙丁戊己庚辛壬癸"
DZ = "子丑寅卯辰巳午未申酉戌亥"
TG_ELEM = ["木", "木", "火", "火", "土", "土", "金", "金", "水", "水"]
# 本気 (the main element of each earthly branch)
DZ_ELEM = ["水", "土", "木", "木", "土", "火", "火", "土", "金", "金", "土", "水"]
TG_YINYANG = ["陽", "陰"] * 5


def gz_str(g):
    return TG[g.tg] + DZ[g.dz]


def pillars(y, m, d, hh=None):
    day = sxtwl.fromSolar(y, m, d)
    out = {"年柱": day.getYearGZ(), "月柱": day.getMonthGZ(), "日柱": day.getDayGZ()}
    if hh is not None:
        out["時柱"] = day.getHourGZ(hh)
    return out


def selftest():
    # Well-known published anchors, including solar-term boundaries （立春）.
    cases = [
        ((1900, 1, 31), "日柱", "甲辰"),
        ((2000, 1, 1), "日柱", "戊午"),
        ((2000, 1, 1), "年柱", "己卯"),   # before 立春
        ((1984, 2, 2), "年柱", "癸亥"),   # before 立春
        ((1984, 2, 5), "年柱", "甲子"),   # after 立春
        ((1984, 2, 5), "月柱", "丙寅"),
        ((1893, 12, 26), "年柱", "癸巳"),
        ((1893, 12, 26), "月柱", "甲子"),
        ((1893, 12, 26), "日柱", "丁酉"),
        ((2024, 2, 3), "月柱", "乙丑"),   # before 立春
        ((2024, 2, 5), "年柱", "甲辰"),
        ((2024, 2, 5), "月柱", "丙寅"),
    ]
    ok = True
    for (y, m, d), which, exp in cases:
        got = gz_str(pillars(y, m, d)[which])
        if got != exp:
            ok = False
        print(f"{'OK' if got == exp else 'NG'}: {y}-{m:02d}-{d:02d} {which} = {got} (expected {exp})")
    print("SELFTEST:", "ALL OK" if ok else "FAILED")
    return 0 if ok else 1


def meishiki(y, m, d, hh=None):
    ps = pillars(y, m, d, hh)
    counts = {"木": 0, "火": 0, "土": 0, "金": 0, "水": 0}
    parts = []
    for name, g in ps.items():
        counts[TG_ELEM[g.tg]] += 1
        counts[DZ_ELEM[g.dz]] += 1
        parts.append(f"{name} {gz_str(g)}")
    day_gz = ps["日柱"]
    day_master = f"{TG[day_gz.tg]}（{TG_ELEM[day_gz.tg]}の{TG_YINYANG[day_gz.tg]}）"
    today = date.today()
    year_now = gz_str(sxtwl.fromSolar(today.year, today.month, today.day).getYearGZ())
    print("命式: " + " / ".join(parts))
    print(f"日主: {day_master}")
    print("五行バランス（天干＋地支の本気で数える）: " + "・".join(f"{k} {v}" for k, v in counts.items()))
    print(f"今年の干支: {year_now}（立春基準）")
    if hh is None:
        print("※出生時刻が不明のため、時柱なしの簡易鑑定です")
    return 0


MAJOR = ["愚者", "魔術師", "女教皇", "女帝", "皇帝", "教皇", "恋人", "戦車", "力", "隠者",
         "運命の輪", "正義", "吊るされた男", "死神", "節制", "悪魔", "塔", "星", "月",
         "太陽", "審判", "世界"]
SUITS = ["ワンド", "カップ", "ソード", "ペンタクル"]
RANKS = ["エース", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "ペイジ", "ナイト", "クイーン", "キング"]


def deck():
    cards = list(MAJOR)
    for s in SUITS:
        for r in RANKS:
            cards.append(f"{s}の{r}")
    return cards


def draw(n=3):
    rng = random.SystemRandom()
    picked = rng.sample(deck(), n)
    positions = ["現状", "課題", "助言"]
    for i, c in enumerate(picked):
        orient = "正位置" if rng.random() < 0.5 else "逆位置"
        label = positions[i] if n == 3 else f"{i + 1}枚目"
        print(f"{label}: {c}（{orient}）")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "selftest":
        sys.exit(selftest())
    elif cmd == "meishiki":
        y, m, d = map(int, sys.argv[2].split("-"))
        hh = None
        if len(sys.argv) > 3:
            hh = int(sys.argv[3].split(":")[0])
        sys.exit(meishiki(y, m, d, hh))
    elif cmd == "draw":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        sys.exit(draw(n))
    else:
        print(__doc__)
        sys.exit(1)
