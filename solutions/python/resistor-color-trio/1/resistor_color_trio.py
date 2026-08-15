COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

PREFIXES = [
    (1_000_000_000, "gigaohms"),
    (1_000_000, "megaohms"),
    (1_000, "kiloohms"),
    (1, "ohms"),
]


def label(colors: list[str]) -> str:
    # 1. Map the first two colors to digits
    val1 = COLORS.index(colors[0])
    val2 = COLORS.index(colors[1])

    # 2. Get the exponent from the third color
    exponent = COLORS.index(colors[2])

    # 3. Calculate total resistance in ohms
    ohms = (val1 * 10 + val2) * (10**exponent)

    # 4. Format using the appropriate metric prefix
    for threshold, unit in PREFIXES:
        if ohms >= threshold and ohms % threshold == 0:
            return f"{ohms // threshold} {unit}"

    return f"{ohms} ohms"