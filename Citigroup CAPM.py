# Package Import
import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['C', "^GSPC"]
data = pd.DataFrame()
for x in tickers:
    data[x] = wb.DataReader(x, data_source='yahoo',
                            start="2018-1-1")["Adj Close"]

sec_returns = np.log(data / data.shift(1))
cov = sec_returns.cov() * 250
cov_with_market = cov.iloc[0, 1]

market_var = sec_returns["^GSPC"].var() * 252

# Beta
C_beta = cov_with_market / market_var

# Expected return of Citigroup(CAPM)
rf = 1.31/100
equity_risk_prm = 5.5/100
C_er = rf + C_beta * equity_risk_prm

# Sharpe ratio
sharpe = (C_er - rf) / (sec_returns["C"].std() * 252 ** 0.05)
if sharpe > 1:
    print("Investable")
elif sharpe > 2:
    print("Great to invest")
elif sharpe > 3:
    print("Excellent to invest")
else:
    print("Sub-optimal")
