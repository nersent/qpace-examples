import { resolve } from "path";
import * as qp from "qpace/node";

const ohlcvPath = resolve(import.meta.dirname, "../assets/btc.csv");
const ohlcv = qp.Ohlcv.readCsv(ohlcvPath);
ohlcv.timeframe = qp.Timeframe.Days(1);

const sym = qp.Sym.BTC_USD();
const ctx = new qp.Ctx(ohlcv, sym);

console.log(qp.ta.rsi(ctx.copy(), ctx.ohlcv.close, 14));

// Compiler example:
// import * as pine from "qpace_example_lib_node";
// console.log(pine.script.customMa(ctx.copy(), ctx.ohlcv.close));
