 import pandas as pd

ticker = 'BP'
df = pd.read_csv(f'data/{ticker}.csv')
df

import talib

rsi = talib.RSI(df.c, 14)
sar = talib.SAR(df.h, df.l)

import numpy as np
bbands = np.array(talib.BBANDS(rsi, timeperiod=7, nbdevup=2, nbdevdn=2))
bbands[0]

dfp = pd.DataFrame(df['c'])
dfp['rsi'] = rsi
dfp['sar'] = sar.diff()
dfp['l'] = bbands[1]
dfp['h'] = bbands[0]
dfp['s_buy'] = (dfp.rsi<dfp.l).astype(int)
dfp['s_sell'] = (dfp.rsi>dfp.h).astype(int)

dfp.dropna()