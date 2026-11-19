import random
import numpy as np 
from functools import partial
import matplotlib.pyplot as plt


def get_sma(prices: list[float], window: int) -> list[None | float]:
    out = []
    for t in range(len(prices)):
        if t + 1 < window:
            out.append(None)
        else:
            out.append(sum(prices[t - window + 1: t + 1]) / window)
            
    return out #type: ignore


_fast = partial(get_sma, window=3)
_slow = partial(get_sma, window=6)


def get_ema(prices: list[float], span: int):
    alpha = 2.0 / (span + 1)
    out, prev = [], None
    for p in prices:
        prev = p if prev is None else alpha * p + (1 - alpha) * prev #type: ignore
        out.append(prev)
    return out


def crossover(fast, slow):
    return [1 if f and s and f > s else 0 for f, s in zip(fast, slow)]


if __name__ == "__main__":
    span, interval = 100, 10
    prices = [random.random() * 100 for i in range(span)]
    fast_smas = [x if x else 0 for x in _fast(prices)]
    slow_smas = [x if x else 0 for x in _slow(prices, )]
    emas = get_ema(prices, 3)
    crossovers = crossover(get_sma(prices, 3), get_sma(prices, 10))

    print(crossovers)
    time = np.linspace(0, interval, span)
    plt.plot(time, prices)
    plt.plot(time, fast_smas, color="red")
    plt.plot(time, slow_smas, color="blue")
    plt.plot(time, emas, color="green")
    plt.show()