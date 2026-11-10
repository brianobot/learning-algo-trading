import math

from calculating_indicators import simulate_gbm, get_volatility, get_momentum, get_rsi
import matplotlib.pyplot as plt

def threshold_signal(indicator, lo, hi):
    out = []
    for v in indicator:
        if v is None:   out.append(0)
        elif v > hi:    out.append(1)
        elif v < lo:    out.append(-1)
        else:           out.append(0)
    return out


def _missing(x):
    return x is None or (isinstance(x, float) and math.isnan(x))


def crossover_state(fast, slow):
    out, state = [], 0
    for f, s in zip(fast, slow):
        if _missing(f) or _missing(s):
            state = 0
            out.append(state)
        elif f > s:  
            state = 1 
            out.append(1)
        elif f < s:  
            state = -1    
            out.append(-1)
        else:                       
            out.append(state)                 # tie -> hold
    return out


if __name__ == "__main__":
    num = 100
    window = 10
    prices = simulate_gbm(mu=0.80, n_steps=num, seed=42)
    risk, trend = get_volatility(list(prices), window), get_momentum(list(prices), window)

    max_risk, min_risk = max(x for x in risk if x is not None), min(x for x in risk if x is not None)
    max_trend, min_trend = max(x for x in trend if x is not None), min(x for x in trend if x is not None)
    print(f"Max Risk: {max_risk}, Min Risk: {min_risk}")
    print(f"Max Trend: {max_trend}, Min Trend: {min_trend}")

    risk_threshold = threshold_signal(risk, min_risk * 1.3, max_risk * 0.7)
    trend_threshold = threshold_signal(trend, min_trend * 1.3, max_trend * 0.7)

    print("Risk threshold: ", risk_threshold)
    print("Trend Threshold: ", trend_threshold)

    plt.plot(range(100), prices)
    plt.plot(range(100), [0 if x is None else x for x in risk])
    plt.plot(range(100), [0 if x is None else x for x in trend])
    plt.show()
    