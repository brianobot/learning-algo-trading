import time


def backward_window(series, current, window):
    out = [None] * len(series)
    out[max(current - window + 1, 0): current + 1] = series[max(current - window + 1, 0): current + 1]
    return out


def fixed_fraction_sizing(signal, equity, fraction, price):
    if signal == 0 or price <= 0:
        return 0.0
    return signal * (fraction * equity) / price


def vol_target_weight(signal, target_vol, asset_vol, max_leverage):
    if signal == 0 or asset_vol <= 0:
        return 0.0

    w = target_vol / asset_vol
    if w > max_leverage:
        w = max_leverage

    return signal * w


def run_positions(prices, signals, fraction):
    total = 0.0
    for t in range(len(prices) -  1):
        weight = signals[t] * fraction
        r_next = prices[t + 1] / prices[t] - 1.0
        total += weight * r_next
    return total


if __name__ == "__main__":
    series = list(range(11))
    for i in range(13):
        window = backward_window(series, i, 3)
        print(window)
        time.sleep(1)