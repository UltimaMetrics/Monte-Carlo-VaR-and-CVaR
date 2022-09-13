# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:56:35 2022

@author: sigma
"""


import pandas as pd
import numpy as np
from numpy.linalg import multi_dot

from scipy.stats import norm
from tabulate import tabulate

# Import matplotlib for visualization
import matplotlib
import matplotlib.pyplot as plt
import yfinance as yf


header = ['Confidence Level', 'Value At Risk']

asset=yf.Ticker("BITO")
BITO = asset.history(period="3y")
BITO['Close'].plot(title="BITO trend")

symbol=BITO

BITO_returns=BITO['Close'].pct_change()

mean=np.mean(BITO_returns)
             
stdev=np.std(BITO_returns)

asset=yf.Ticker("BITO")
BITO = asset.history(period="3y")
BITO['Close'].plot(title="BITO trend")
BITO['Close']

price=BITO['Close']

t=BITO['Close']

returns = price.pct_change().dropna()

#Historical VaR
# Use quantile function for Historical VaR
hVaR_90 = BITO_returns.quantile(0.10)
hVaR_95 = BITO_returns.quantile(0.05)
hVaR_99 = BITO_returns.quantile(0.01)

# Calculate CVar
CVaR_90 = (BITO_returns)[(BITO_returns)<=hVaR_90].mean()
CVaR_95 =(BITO_returns)[(BITO_returns)<=hVaR_95].mean()
CVaR_99 = (BITO_returns)[(BITO_returns)<=hVaR_99].mean()


ctable = [['90%', CVaR_90],['95%', CVaR_95],['99%', CVaR_99] ]
cheader = ['Confidence Level', 'Conditional Value At Risk']
print(tabulate(ctable,headers=cheader))