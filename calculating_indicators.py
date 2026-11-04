import numpy as np


def get_momentum(prices: list[float], lookback) -> list[None | float]:
    out: list[None | float] = [None] * len(prices)
    for t in range(lookback, len(prices)):
        out[t] = prices[t] / prices[t - lookback] - 1.0
    return out


def get_rsi(prices: list[float], window):
    out: list[None | float] = [None] * len(prices)
    for t in range(window, len(prices)):
        gains = losses = 0
        for k in range(t - window + 1, t + 1):
            change = prices[k] - prices[k - 1]
            if change >= 0: gains += change
            else: losses += -change

        avg_gain, avg_loss = gains/window, losses/window
        out[t] = 100.0 if avg_loss == 0 else 100.0 - 100 / (1.0 + avg_gain / avg_loss)
    return out


def get_volatility(prices: list[float], window):
    out = [None] * len(prices)
    for t in range(len(prices)):
        if t + 1 >= window:
            w = prices[t - window + 1: t + 1]
            mean = sum(w)/ window
            out[t] = (sum((x - mean) ** 2 for x in w) / window) ** 0.5
            
    return out

def simulate_gbm(
    s0: float = 100.0,     # starting price
    mu: float = 0.08,      # annual drift (expected return)
    sigma: float = 0.20,   # annual volatility
    n_steps: int = 252,    # number of steps (252 trading days)
    dt: float = 1 / 252,   # time step in years
    seed: int | None = None,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(n_steps)
    log_returns = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
    return s0 * np.exp(np.cumsum(log_returns))


if __name__ == "__main__":
    num = 100
    window = 20
    prices = simulate_gbm(mu=-0.80, n_steps=num, seed=42)
    print("Prices: ", prices)

    momentum = get_momentum(list(prices), window)
    print("Momentum: ", momentum)
    print("")
    rsi = get_rsi(list(prices), window)
    print("RSI Value: ", rsi)
    print("")
    volatility = get_volatility(list(prices), window)
    print("Volatility: ", volatility)

    import matplotlib.pyplot as plt

    plt.plot(range(num), prices, label="Price")
    plt.plot(range(num), [0 if not x else x for x in momentum], color="red", label="Momentum")
    plt.plot(range(num), [0 if not x else x for x in rsi], color="blue", label="RSI")
    plt.plot(range(num), [0 if not x else x for x in volatility], color="green", label="Volatility")
    plt.legend()
    plt.show()