import yfinance as yf 
import math 

#scarica 5 anni di dati APPLE
dati= yf.download("AAPL", start="2020-01-01", end="2026-06-15")

print (dati.head())

rendimenti = dati["Close"]["AAPL"].pct_change()
print(rendimenti.head(1826))

print("rendimento giornaliero medio tra il 2020 e il 2025")
print(rendimenti.mean())

print("rendimento medio aritmetico di un'anno tra il 2020 e il 2025")
print(rendimenti.mean()*(252))

print("rendimento composto medio di un'anno tra il 2020 e il 2025")
print((1 + rendimenti.mean())**252 - 1)

print("volatilità (rischio) giornaliero medio tra il 2020 e il 2025")
print(rendimenti.std())

print("volatilità annualizzata")
print(rendimenti.std() * math.sqrt(252))

risk_free = 0.04
sharpe = ((1 + rendimenti.mean())**252 - 1 - risk_free) / (rendimenti.std() * math.sqrt(252))
print("Sharpe ratio Apple:", sharpe)
