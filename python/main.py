import os
from time import perf_counter
import qpace as qp
from tqdm import tqdm
import numpy as np
import pandas as pd

# from qpace.ta import accdist

# print(qp.ta.accdist)
# print(accdist)
ohlcv_path = os.path.join(os.path.dirname(__file__), "../assets/btc.csv")
ohlcv = qp.Ohlcv.read_csv(ohlcv_path)
ohlcv.timeframe = qp.Timeframe.Days(1)
ctx = qp.Ctx(ohlcv, qp.Sym.BTC_USD())

bt = qp.Backtest(ctx.copy())
for bar_index in bt:
    if bar_index == 10:
        bt.signal(qp.Signal.Long())
    elif bar_index == 20:
        bt.signal(qp.Signal.Short())
    elif bar_index == 30:
        bt.signal(qp.Signal.Close_all())

bt_summary = bt.summary()
print(bt_summary.to_dict())
bt_summary.display()
