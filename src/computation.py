import math


def lux_to_ev(lux: float) -> float:
    if lux <= 0:
        return float("-inf")
    return math.log2(lux / 2.5)


def correct_lux(lux: float) -> float:
    return (
        6.0135e-13 * pow(lux, 4)
        - 9.3924e-9 * pow(lux, 3)
        + 8.1488e-5 * pow(lux, 2)
        + 1.0023 * lux
    )
