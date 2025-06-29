import os
from time import perf_counter
import qpace as qp
from tqdm import tqdm
import numpy as np
import pandas as pd

ohlcv_path = os.path.join(os.path.dirname(__file__), "../assets/btc.csv")
ohlcv = qp.Ohlcv.read_csv(ohlcv_path)
ohlcv.timeframe = qp.Timeframe.Days(1)
ctx = qp.Ctx(ohlcv, qp.Sym.BTC_USD())

rsi = qp.ta.rsi(ctx.copy(), ctx.ohlcv.close, 14)
print(rsi[0:30])
