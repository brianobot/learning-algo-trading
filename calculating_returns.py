import math
import random


def simple_returns(prices: list[int]):
    out: list[None | float] = [None]
    for t in range(1, len(prices)):
        out.append((prices[t] / prices[t - 1]) - 1.0)
    return out


def log_returns(prices: list[int]):
    out: list[None | float] = [None]
    for t in range(1, len(prices)):
        out.append(math.log(prices[t]/ prices[t -1]))
    return out


def simple_return_wealth_aggregation(prices: list[int]):
    wealth = 1.0
    for r in simple_returns(prices)[1:]:
        wealth *= (1 + r) #type: ignore
    return wealth


def log_returns_wealth_aggregation(prices: list[int]) -> float:
    total_log = sum(x for x in log_returns(prices)[1:]) # type: ignore
    return math.exp(total_log)


if __name__ == "__main__":
    prices = [random.randint(80, 120) for i in range(10)]
    log1 = simple_returns(prices)
    log2 = log_returns(prices)

    print(f"Simple Returns: {log1}")
    print(f"Log Returns: {log2}")
