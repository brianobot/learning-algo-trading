from calculating_ma import get_ema, get_sma
from signals_and_crossovers import crossover_state as make_signal


def strategy_returns(prices: list[float], signals: list[int], fraction: float):
    return [signals[t] * fraction * (prices[t+1]/(prices[t] - 1.0)) for t in range(len(prices) - 1)]


def equity_curve(strat_ret: list[float], start: float):
    eq = [start]
    for r in strat_ret:
        eq.append(eq[-1] * (1 + r))
    return eq


def run_strategy(prices: list[float], fast: list[float], slow: list[float], fraction: float, start: float):
    sig, eq, trades, prev = make_signal(fast, slow), start, 0, 0
    for t in range(len(prices) - 1):
        if sig[t] != prev: 
            trades += 1

        prev = sig[t]
        eq *= (1 + sig[t] * fraction * (prices[t+1]/prices[t] - 1.0))
    return {"final_equity": eq, "trades": trades, "signal": sig}
    

if __name__ == "__main__":
    prices = [10, 12, 12, 11, 10, 9, 8, 10, 13, 15]
    signals = make_signal(get_sma(prices, 3), get_sma(prices, 4)) #type: ignore
    strat_ret = strategy_returns(prices, signals, 0.20) #type: ignore
    print("strat ret: ", strat_ret)

    import matplotlib.pyplot as plt

    plt.plot(range(len(prices) - 1), strat_ret)
    plt.show()