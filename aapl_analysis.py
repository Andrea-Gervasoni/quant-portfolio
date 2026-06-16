import yfinance as yf
import math

# download AAPL data from 2020 to 2026
data = yf.download("AAPL", start="2020-01-01", end="2026-06-15")

print(data.head())

returns = data["Close"]["AAPL"].pct_change()
print(returns.head(1826))

print("average daily return between 2020 and 2026")
print(returns.mean())

print("arithmetic average return of one year between 2020 and 2026")
print(returns.mean() * 252)

print("one-year average compound return between 2020 and 2026")
print((1 + returns.mean())**252 - 1)

print("average daily volatility (risk) between 2020 and 2026")
print(returns.std())

print("annualized volatility")
print(returns.std() * math.sqrt(252))

risk_free = 0.04
sharpe = ((1 + returns.mean())**252 - 1 - risk_free) / (returns.std() * math.sqrt(252))
print("Sharpe ratio AAPL:", sharpe)
