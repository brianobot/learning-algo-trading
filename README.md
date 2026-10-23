# Learning Algo Trading with Python and Rust

## Market Model
market data comes in ticks, ticks are very noisy, aggregate ticks into bars, which represent key attributes for the span of the bar, 
Open price, High price, Low Price, Close Price and the Volume of trade taken in that interval

When building the aggregation, avoid the looking ahead, and ever tick should belong to exactly one bar, to ensure this 
every bar must only contain ticks start from start to one value less than each interval

valid range => start of interval <= t < end of interval, this ensures that boundary ticks belong to exactly one bar 
and there is no look ahead bug.

A key indicator that this rule is met is in the ability of a series of bar to support decision making without needing the next bar, such 
that given a series of bars, a trade decision can be made for all of them including the very last one.

This also ensures that there is no gap, no overlaps and no future leakage.


## Rate of Returns
### Simple Return
This is the fractional change of the price at time t from previous bar's close price; give by the formula

$$\text{Return}[t] = \frac{\text{Prices}[t]}{\text{Prices}[t -1]} - 1$$

### Logarithm Return 
$$\text{lr}[t] = ln(\frac{\text{Prices}[t]}{\text[Prices[t - 1]]}})$$


## Maintainer
Brian Obot <brianobot9@gmail.com>