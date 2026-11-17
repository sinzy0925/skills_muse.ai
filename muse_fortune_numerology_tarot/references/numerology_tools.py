#!/usr/bin/env python3
"""Helpers for the muse_fortune_numerology_tarot skill.

Commands:
  selftest                      Verify the numerology calculation against known
                                anchors and check the tarot deck.
  numbers YYYY-MM-DD            Print the ライフパス (life path), バースデー
                                (birthday) and パーソナルイヤー (personal year)
                                numbers for a birth date.
  draw [n]                      Draw n tarot cards by random lot (default 3), each
                                with upright / reversed. Never draw twice for the
                                same question.

Reduction rule (the v1 convention of this skill): add the digits repeatedly
until the result is 1-9, except that 11 and 22 are kept as master numbers.
The personal year is calendar-based (January to December). Pure arithmetic —
no external library is needed, and the numbers must still never be computed
by hand in the reading: always use this helper's output verbatim.
"""
import sys
import random
from datetime import date

MASTER = (11, 22)

MEANINGS = {
    1: "始まり・自立・リーダーシップ",
    2: "調和・感受性・支える",
    3: "表現・楽しさ・創造",
    4: "安定・基盤・コツコツ",
    5: "変化・自由・体験",
    6: "愛情・責任・育てる",
    7: "探求・内省・専門性",
    8: "実り・力・現実化",
    9: "完成・手放し・博愛",
    11: "直感・ひらめき（マスターナンバー）",
    22: "大きな実現・築く（マスターナンバー）",
}


def reduce_num(n):
    while n > 9 and n not in MASTER:
        n = sum(int(c) for c in str(n))
    return n


def digit_sum_of_date(y, m, d):
    return sum(int(c) for c in f"{y:04d}{m:02d}{d:02d}")


def lifepath(y, m, d):
    return reduce_num(digit_sum_of_date(y, m, d))


def birthday(d):
    return reduce_num(d)


def personal_year(m, d, year):
    return reduce_num(reduce_num(m) + reduce_num(d) + reduce_num(sum(int(c) for c in str(year))))


def fmt(n):
    return f"{n}（{MEANINGS[n]}）"


def selftest():
    ok = True

    def check(label, got, exp):
        nonlocal ok
        good = got == exp
        ok = ok and good
        print(f"{'OK' if good else 'NG'}: {label} = {got} (expected {exp})")

    # ライフパス anchors, including both master numbers.
    for (y, m, d), exp in [
        ((1970, 9, 25), 6),
        ((1990, 1, 1), 3),
        ((2000, 8, 1), 11),   # digit sum is exactly 11
        ((1983, 6, 2), 11),   # 29 -> 11
        ((2001, 9, 19), 22),  # digit sum is exactly 22
    ]:
        check(f"ライフパス {y}-{m:02d}-{d:02d}", lifepath(y, m, d), exp)

    # バースデー anchors.
    for d, exp in [(25, 7), (11, 11), (29, 11), (22, 22), (31, 4), (9, 9)]:
        check(f"バースデー {d}日", birthday(d), exp)

    # パーソナルイヤー anchors (calendar-year convention).
    for (m, d, year), exp in [
        ((9, 25, 2026), 8),
        ((1, 1, 2026), 3),
        ((12, 31, 2025), 7),
    ]:
        check(f"パーソナルイヤー {m}/{d} in {year}", personal_year(m, d, year), exp)

    # Tarot deck integrity.
    check("タロット総数", len(deck()), 78)
    check("タロット重複なし", len(set(deck())), 78)

    print("SELFTEST:", "ALL OK" if ok else "FAILED")
    return 0 if ok else 1


def numbers(y, m, d):
    today = date.today()
    lp = lifepath(y, m, d)
    bd = birthday(d)
    py = personal_year(m, d, today.year)
    print(f"ライフパスナンバー: {fmt(lp)}")
    print(f"バースデーナンバー: {fmt(bd)}")
    print(f"パーソナルイヤー（{today.year}年）: {fmt(py)}")
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
    elif cmd == "numbers":
        y, m, d = map(int, sys.argv[2].split("-"))
        sys.exit(numbers(y, m, d))
    elif cmd == "draw":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        sys.exit(draw(n))
    else:
        print(__doc__)
        sys.exit(1)
