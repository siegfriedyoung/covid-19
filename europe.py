#!/usr/bin/env python
# encoding: utf-8`
import pandas as pd
import numpy as np
import sys
from os.path import exists
# # import statsmodels.tsa.tsatools as stm
import datetime as dt
import matplotlib.dates as mdates
# import statsmodels.api as sm
from matplotlib import pyplot as plt

icudata = pd.read_csv('data.csv', index_col=0, header=0)
testdata = pd.read_csv('test.csv', index_col=0, header=0)

for country in set(icudata.index):
    cdata = icudata.loc[country, :].pivot_table(index='date', columns='indicator', values='value')
    cdata.index = pd.to_datetime(cdata.index)
    if cdata.empty:
        cdata = icudata.loc[country, :].pivot_table(index='date', columns='year_week', values='value')
    if not(cdata.empty):
        plt.figure(country)
        plt.plot(cdata.index, cdata.values)
        plt.title(country)
        plt.legend(cdata.columns)

for country in set(testdata.index):
    cdata = testdata.loc[country, ['year_week', 'testing_rate', 'positivity_rate']]
    cdata.index = cdata['year_week']

    if not(cdata.empty):
        fig1 = plt.figure(country)
        ax1_1 = fig1.add_subplot(1, 1, 1)
        ax1_1.plot(cdata.index, cdata['testing_rate'])
        ax1_1.legend(['testing_rate'], loc=3)
        ax1_2 = ax1_1.twinx()
        ax1_2.plot(cdata.index, cdata['positivity_rate'], color='red')
        ax1_2.legend(['positivity_rate'], loc=1)
        plt.title(country)

plt.show()
