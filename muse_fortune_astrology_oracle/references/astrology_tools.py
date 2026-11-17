#!/usr/bin/env python3
"""Helpers for the muse_fortune_astrology_oracle skill.

Commands:
  selftest                      Verify the chart calculation against known anchors
                                (sun signs, and Einstein's published natal chart)
                                and check the oracle deck.
  chart YYYY-MM-DD [HH:MM] [PLACE]
                                Print the sun sign, moon sign (needs the birth
                                time) and ascendant (needs time and place), plus
                                today's Jupiter and Saturn signs.
                                PLACE is a Japanese prefectural capital from the
                                built-in table (e.g. 大阪), or "lat,lon" or
                                "lat,lon,utc_offset_hours". Default offset +9.
  draw [n]                      Draw n oracle cards by random lot (default 3).
                                Oracle cards have no reversed position. Never
                                draw twice for the same question.

Requires the pyswisseph library (pip install pyswisseph), using its built-in
Moshier ephemeris (no data files; accuracy is more than enough to determine
signs). If it is missing, this script exits with an error instead of guessing:
the chart must never be hand-computed.
"""
import sys
import random
from datetime import date

try:
    import swisseph as swe
except ImportError:
    print("ERROR: pyswisseph is not installed. Run: pip install pyswisseph", file=sys.stderr)
    sys.exit(2)

FLAGS = swe.FLG_MOSEPH | swe.FLG_SPEED

SIGNS = ["牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座",
         "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座"]
ELEMENTS = ["火", "地", "風", "水"] * 3

# Japanese prefectural capitals: name -> (latitude, longitude). UTC offset +9.
PLACES = {
    "札幌": (43.06, 141.35), "青森": (40.82, 140.74), "盛岡": (39.70, 141.15),
    "仙台": (38.27, 140.87), "秋田": (39.72, 140.10), "山形": (38.24, 140.36),
    "福島": (37.75, 140.47), "水戸": (36.34, 140.45), "宇都宮": (36.56, 139.88),
    "前橋": (36.39, 139.06), "さいたま": (35.86, 139.65), "千葉": (35.61, 140.12),
    "東京": (35.68, 139.69), "横浜": (35.44, 139.64), "新潟": (37.92, 139.06),
    "富山": (36.70, 137.21), "金沢": (36.56, 136.66), "福井": (36.07, 136.22),
    "甲府": (35.66, 138.57), "長野": (36.65, 138.18), "岐阜": (35.42, 136.76),
    "静岡": (34.98, 138.38), "名古屋": (35.18, 136.91), "津": (34.73, 136.51),
    "大津": (35.00, 135.87), "京都": (35.01, 135.77), "大阪": (34.69, 135.50),
    "神戸": (34.69, 135.20), "奈良": (34.69, 135.83), "和歌山": (34.23, 135.17),
    "鳥取": (35.50, 134.24), "松江": (35.47, 133.05), "岡山": (34.66, 133.92),
    "広島": (34.39, 132.46), "山口": (34.19, 131.47), "徳島": (34.07, 134.56),
    "高松": (34.34, 134.04), "松山": (33.84, 132.77), "高知": (33.55, 133.53),
    "福岡": (33.59, 130.40), "佐賀": (33.26, 130.30), "長崎": (32.75, 129.87),
    "熊本": (32.79, 130.74), "大分": (33.24, 131.61), "宮崎": (31.91, 131.42),
    "鹿児島": (31.56, 130.56), "那覇": (26.21, 127.68),
}


def sign_of(lon):
    idx = int(lon // 30) % 12
    return SIGNS[idx], ELEMENTS[idx], lon % 30


def planet_lon(jd, planet):
    return swe.calc_ut(jd, planet, FLAGS)[0][0]


def jd_from_local(y, m, d, hh, mm, offset_hours):
    utc_hour = hh + mm / 60.0 - offset_hours
    return swe.julday(y, m, d, utc_hour)


def ascendant(jd, lat, lon):
    cusps, ascmc = swe.houses_ex(jd, lat, lon, b"P")
    return ascmc[0]


def parse_place(place):
    """Return (lat, lon, utc_offset) or None if the place is unknown."""
    if place is None:
        return None
    key = place.strip()
    for suffix in ("都", "府", "県"):
        if key.endswith(suffix) and len(key) > 1:
            key = key[: -len(suffix)]
            break
    if key in PLACES:
        lat, lon = PLACES[key]
        return lat, lon, 9.0
    parts = key.split(",")
    if len(parts) in (2, 3):
        try:
            lat = float(parts[0])
            lon = float(parts[1])
            offset = float(parts[2]) if len(parts) == 3 else 9.0
            return lat, lon, offset
        except ValueError:
            return None
    return None


def selftest():
    ok = True

    def check(label, got, exp):
        nonlocal ok
        good = got == exp
        ok = ok and good
        print(f"{'OK' if good else 'NG'}: {label} = {got} (expected {exp})")

    # Sun-sign anchors (textbook date ranges), computed at noon JST.
    for (y, m, d), exp in [
        ((1970, 9, 25), "天秤座"),
        ((2000, 1, 1), "山羊座"),
        ((1990, 8, 15), "獅子座"),
        ((1985, 4, 10), "牡羊座"),
    ]:
        jd = jd_from_local(y, m, d, 12, 0, 9.0)
        check(f"太陽星座 {y}-{m:02d}-{d:02d}", sign_of(planet_lon(jd, swe.SUN))[0], exp)

    # Full-chart anchor: Albert Einstein, born 1879-03-14 11:30 local time in
    # Ulm, Germany (48.40N, 10.00E; local mean time = UTC +0:40). His published
    # chart: Sun in Pisces, Moon in Sagittarius, Ascendant in Cancer.
    jd = jd_from_local(1879, 3, 14, 11, 30, 40 / 60.0)
    check("アインシュタイン 太陽星座", sign_of(planet_lon(jd, swe.SUN))[0], "魚座")
    check("アインシュタイン 月星座", sign_of(planet_lon(jd, swe.MOON))[0], "射手座")
    check("アインシュタイン 上昇宮", sign_of(ascendant(jd, 48.40, 10.00))[0], "蟹座")

    # Built-in place table.
    check("出生地テーブルの件数", len(PLACES), 47)
    check("出生地 大阪の解決", parse_place("大阪府") is not None, True)
    check("出生地 不明な地名", parse_place("どこか"), None)

    # Oracle deck integrity.
    check("オラクル総数", len(CARDS), 36)
    check("オラクル重複なし", len({c[0] for c in CARDS}), 36)

    print("SELFTEST:", "ALL OK" if ok else "FAILED")
    return 0 if ok else 1


def chart(y, m, d, hh=None, mm=0, place=None):
    parsed = parse_place(place) if place else None
    if place and parsed is None:
        print(f"ERROR: 出生地「{place}」が分かりません。都道府県庁所在地の名前か、lat,lon で指定してください", file=sys.stderr)
        return 2
    offset = parsed[2] if parsed else 9.0
    if hh is None:
        jd = jd_from_local(y, m, d, 12, 0, offset)
        sun = sign_of(planet_lon(jd, swe.SUN))
        print(f"太陽星座: {sun[0]}（{sun[1]}）")
        print("※出生時刻が不明のため、太陽星座のみの簡易鑑定です（月星座・上昇宮は出しません）")
    else:
        jd = jd_from_local(y, m, d, hh, mm, offset)
        sun = sign_of(planet_lon(jd, swe.SUN))
        moon = sign_of(planet_lon(jd, swe.MOON))
        print(f"太陽星座: {sun[0]}（{sun[1]}）")
        print(f"月星座: {moon[0]}（{moon[1]}）")
        if parsed:
            asc = sign_of(ascendant(jd, parsed[0], parsed[1]))
            print(f"上昇宮（アセンダント）: {asc[0]}（{asc[1]}）")
        else:
            print("※出生地が不明のため、上昇宮は出しません")
    today = date.today()
    jd_now = jd_from_local(today.year, today.month, today.day, 12, 0, 9.0)
    jup = sign_of(planet_lon(jd_now, swe.JUPITER))
    sat = sign_of(planet_lon(jd_now, swe.SATURN))
    print(f"現在の木星: {jup[0]}（{jup[1]}）／ 現在の土星: {sat[0]}（{sat[1]}）")
    return 0


# An original 36-card oracle deck: (name, keyword). No reversed positions.
CARDS = [
    ("夜明け", "新しい始まり"),
    ("夕暮れ", "区切り・休息"),
    ("太陽", "活力・成功"),
    ("月", "直感・周期"),
    ("星", "希望・導き"),
    ("雲", "一時的な不透明さ"),
    ("雨", "浄化・感情"),
    ("虹", "雨のちの希望"),
    ("風", "変化・知らせ"),
    ("炎", "情熱・行動"),
    ("川", "流れに乗る"),
    ("海", "深さ・無意識"),
    ("山", "安定・努力"),
    ("森", "回復・静けさ"),
    ("種", "可能性・芽生え"),
    ("木", "成長・根を張る"),
    ("花", "開花・喜び"),
    ("実り", "収穫・成果"),
    ("羽", "軽やかさ・自由"),
    ("鳥", "視点・伝達"),
    ("扉", "選択・開く"),
    ("鍵", "解決の糸口"),
    ("橋", "つながり・移行"),
    ("道", "進む方向"),
    ("灯", "導き・安心"),
    ("鏡", "映す・気づき"),
    ("貝", "内に秘めたもの"),
    ("蝶", "変容"),
    ("泉", "湧き出る力・潤い"),
    ("砂時計", "時間・待つこと"),
    ("手紙", "連絡・言葉"),
    ("輪", "循環・めぐり"),
    ("剣", "決断・切り分ける"),
    ("盾", "守る・境界線"),
    ("王冠", "自信・達成"),
    ("空", "広がり・可能性"),
]


def draw(n=3):
    rng = random.SystemRandom()
    picked = rng.sample(CARDS, n)
    positions = ["現状", "課題", "助言"]
    for i, (name, kw) in enumerate(picked):
        label = positions[i] if n == 3 else f"{i + 1}枚目"
        print(f"{label}: {name} ― {kw}")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "selftest":
        sys.exit(selftest())
    elif cmd == "chart":
        y, m, d = map(int, sys.argv[2].split("-"))
        hh = None
        mm = 0
        place = None
        rest = sys.argv[3:]
        if rest and ":" in rest[0]:
            hh, mm = map(int, rest[0].split(":"))
            rest = rest[1:]
        if rest:
            place = rest[0]
        sys.exit(chart(y, m, d, hh, mm, place))
    elif cmd == "draw":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        sys.exit(draw(n))
    else:
        print(__doc__)
        sys.exit(1)
