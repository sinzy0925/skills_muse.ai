#!/usr/bin/env python3
"""Helpers for the muse_fortune_kyusei_shichusuimei_daily skill.

Commands:
  selftest                      Verify the calculations against known anchors
                                (Four Pillars charts, Kyusei stars, the month
                                board, and the element-relation table).
  daily YYYY-MM-DD [HH:MM] [TARGET]
                                Print everything a daily reading needs: the
                                natal chart (pillars, day master, element
                                balance), the Kyusei stars (honmeisei,
                                getsumeisei), and for the target date (default
                                today) its pillars, the year's and month's
                                Kyusei board stars, and how today's elements
                                relate to the day master.

Requires the sxtwl library (pip install sxtwl). If it is missing, this script
exits with an error instead of guessing: nothing here is hand-computed.
There is no draw in this skill — both methods are calculations.
"""
import sys
from datetime import date

try:
    import sxtwl
except ImportError:
    print("ERROR: sxtwl is not installed. Run: pip install sxtwl", file=sys.stderr)
    sys.exit(2)

TG = "甲乙丙丁戊己庚辛壬癸"
DZ = "子丑寅卯辰巳午未申酉戌亥"
TG_ELEM = ["木", "木", "火", "火", "土", "土", "金", "金", "水", "水"]
DZ_ELEM = ["水", "土", "木", "木", "土", "火", "火", "土", "金", "金", "土", "水"]
TG_YINYANG = ["陽", "陰"] * 5

STAR_NAMES = {
    1: "一白水星", 2: "二黒土星", 3: "三碧木星", 4: "四緑木星", 5: "五黄土星",
    6: "六白金星", 7: "七赤金星", 8: "八白土星", 9: "九紫火星",
}
STAR_ELEM = {1: "水", 2: "土", 3: "木", 4: "木", 5: "土", 6: "金", 7: "金", 8: "土", 9: "火"}

# Generating cycle: key generates value （木生火， 火生土， 土生金， 金生水， 水生木）.
GEN = {"木": "火", "火": "土", "土": "金", "金": "水", "水": "木"}
# Controlling cycle: key controls value （木剋土， 土剋水， 水剋火， 火剋金， 金剋木）.
CTL = {"木": "土", "土": "水", "水": "火", "火": "金", "金": "木"}


def relation(me, other):
    """How `other`'s element relates to `me` (the day master)."""
    if other == me:
        return "比和（同じ気。自分のペースで進める日）"
    if GEN[other] == me:
        return "相生（相手が自分を生む。追い風・助けが来やすい日）"
    if GEN[me] == other:
        return "漏気（自分が相手を生む。出す・与える・消耗しやすい日）"
    if CTL[other] == me:
        return "相剋（相手が自分を剋す。圧や負担を感じやすい日）"
    return "制気（自分が相手を剋す。主導権を取りやすい日）"


def gz_str(g):
    return TG[g.tg] + DZ[g.dz]


def pillars(y, m, d, hh=None):
    day = sxtwl.fromSolar(y, m, d)
    out = {"年柱": day.getYearGZ(), "月柱": day.getMonthGZ(), "日柱": day.getDayGZ()}
    if hh is not None:
        out["時柱"] = day.getHourGZ(hh)
    return out


def effective_year(y, m, d):
    day = sxtwl.fromSolar(y, m, d)
    mid = sxtwl.fromSolar(y, 6, 1)
    gz_day = (day.getYearGZ().tg, day.getYearGZ().dz)
    gz_mid = (mid.getYearGZ().tg, mid.getYearGZ().dz)
    return y if gz_day == gz_mid else y - 1


def star_for_year(year):
    s = sum(int(c) for c in str(year))
    while s > 9:
        s = sum(int(c) for c in str(s))
    return ((10 - s) % 9) + 1


def month_star(base_star, y, m, d):
    """The month board's center star （月盤中宮）, given the year's star as the
    base. The same table also yields a person's 月命星 when the base is their
    本命星."""
    day = sxtwl.fromSolar(y, m, d)
    dz = day.getMonthGZ().dz
    idx = (dz - 2) % 12  # 寅 = 2 in DZ order
    if base_star in (1, 4, 7):
        start = 8
    elif base_star in (2, 5, 8):
        start = 5
    else:
        start = 2
    return ((start - 1 - idx) % 9) + 1


def selftest():
    ok = True

    def check(label, got, exp):
        nonlocal ok
        good = got == exp
        ok = ok and good
        print(f"{'OK' if good else 'NG'}: {label} = {got} (expected {exp})")

    # Four Pillars anchors (subset of the sibling skill's published anchors).
    for (y, m, d), which, exp in [
        ((2000, 1, 1), "日柱", "戊午"),
        ((1984, 2, 2), "年柱", "癸亥"),   # before 立春
        ((1984, 2, 5), "年柱", "甲子"),   # after 立春
        ((1970, 9, 25), "日柱", "戊申"),
        ((2024, 2, 5), "月柱", "丙寅"),
    ]:
        check(f"四柱推命 {y}-{m:02d}-{d:02d} {which}", gz_str(pillars(y, m, d)[which]), exp)

    # Kyusei anchors.
    check("本命星 1970-09-25", STAR_NAMES[star_for_year(effective_year(1970, 9, 25))], "三碧木星")
    check("本命星 1984-02-02", STAR_NAMES[star_for_year(effective_year(1984, 2, 2))], "八白土星")
    h = star_for_year(effective_year(1970, 9, 25))
    check("月命星 1970-09-25", STAR_NAMES[month_star(h, 1970, 9, 25)], "四緑木星")

    # Month board anchors: the board center of 1970-09 equals that month's
    # 月命星 (same table); and 2026-11 （亥月， year star 一白） is 八白.
    y1970 = star_for_year(effective_year(1970, 9, 25))
    check("月盤中宮 1970-09", STAR_NAMES[month_star(y1970, 1970, 9, 25)], "四緑木星")
    y2026 = star_for_year(effective_year(2026, 11, 17))
    check("月盤中宮 2026-11", STAR_NAMES[month_star(y2026, 2026, 11, 17)], "八白土星")

    # Element-relation table (day master 土 as the example).
    check("関係 土×火", relation("土", "火").split("（")[0], "相生")
    check("関係 土×木", relation("土", "木").split("（")[0], "相剋")
    check("関係 土×土", relation("土", "土").split("（")[0], "比和")
    check("関係 土×金", relation("土", "金").split("（")[0], "漏気")
    check("関係 土×水", relation("土", "水").split("（")[0], "制気")

    print("SELFTEST:", "ALL OK" if ok else "FAILED")
    return 0 if ok else 1


def daily(y, m, d, hh=None, target=None):
    ps = pillars(y, m, d, hh)
    counts = {"木": 0, "火": 0, "土": 0, "金": 0, "水": 0}
    parts = []
    for name, g in ps.items():
        counts[TG_ELEM[g.tg]] += 1
        counts[DZ_ELEM[g.dz]] += 1
        parts.append(f"{name} {gz_str(g)}")
    day_gz = ps["日柱"]
    dm_elem = TG_ELEM[day_gz.tg]
    day_master = f"{TG[day_gz.tg]}（{dm_elem}の{TG_YINYANG[day_gz.tg]}）"
    honmei = star_for_year(effective_year(y, m, d))
    getsumei = month_star(honmei, y, m, d)

    t = target or date.today()
    tp = pillars(t.year, t.month, t.day)
    t_year_star = star_for_year(effective_year(t.year, t.month, t.day))
    t_month_star = month_star(t_year_star, t.year, t.month, t.day)
    t_day_gz = tp["日柱"]
    t_stem_elem = TG_ELEM[t_day_gz.tg]
    t_branch_elem = DZ_ELEM[t_day_gz.dz]

    print("【本人の土台】")
    print("命式: " + " / ".join(parts))
    print(f"日主: {day_master}")
    print("五行バランス（天干＋地支の本気）: " + "・".join(f"{k} {v}" for k, v in counts.items()))
    print(f"本命星: {STAR_NAMES[honmei]}（{STAR_ELEM[honmei]}）／ 月命星: {STAR_NAMES[getsumei]}（{STAR_ELEM[getsumei]}）")
    if hh is None:
        print("※出生時刻が不明のため、時柱なしの簡易計算です")
    print(f"【{t.year}年{t.month}月{t.day}日 の運気材料】")
    print(f"その日の干支: 年柱 {gz_str(tp['年柱'])} / 月柱 {gz_str(tp['月柱'])} / 日柱 {gz_str(tp['日柱'])}")
    print(f"今年の九星: {STAR_NAMES[t_year_star]}（{STAR_ELEM[t_year_star]}）／ 今月の九星（月盤中宮）: {STAR_NAMES[t_month_star]}（{STAR_ELEM[t_month_star]}）")
    print(f"日主（{dm_elem}）と今日の天干（{t_stem_elem}）の関係: {relation(dm_elem, t_stem_elem)}")
    print(f"日主（{dm_elem}）と今日の地支の本気（{t_branch_elem}）の関係: {relation(dm_elem, t_branch_elem)}")
    print(f"本命星（{STAR_ELEM[honmei]}）と今月の九星（{STAR_ELEM[t_month_star]}）の関係: {relation(STAR_ELEM[honmei], STAR_ELEM[t_month_star])}")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "selftest":
        sys.exit(selftest())
    elif cmd == "daily":
        y, m, d = map(int, sys.argv[2].split("-"))
        hh = None
        target = None
        for a in sys.argv[3:]:
            if ":" in a:
                hh = int(a.split(":")[0])
            elif len(a.split("-")) == 3:
                ty, tm, td = map(int, a.split("-"))
                target = date(ty, tm, td)
        sys.exit(daily(y, m, d, hh, target))
    else:
        print(__doc__)
        sys.exit(1)
