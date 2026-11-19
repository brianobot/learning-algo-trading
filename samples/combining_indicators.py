from calculating_indicators import get_volatility, get_momentum
from calculating_ma import get_ema, get_sma


def signal(prices: list[float], fast, slow, vol_cap):
    trend, vol = get_sma(prices, slow), get_volatility(prices, fast)
    out: list[None | float] = [None] * len(prices)
    for t in range(len(prices)):
        if trend[t] is None or vol[t] is None:
            out[t] = 0
        elif prices[t] > trend[t] and vol[t] <= vol_cap: #type: ignore
            out[t] = 1
        else:
            out[t] = 0
    return out


def feature_matrix(prices, window):
    s, m, v = get_sma(prices, window), get_momentum(prices, window-1), get_volatility(prices, window)
    return [{"sma": s[t], "mom": m[t], "vol": v[t]} for t in range(len(prices))]


def ready_rows(matrix: list[dict[str, float]]):
    return [i for i, row in enumerate(matrix) if all(v is not None for v in row.values())]

if __name__ == "__main__":
    pass