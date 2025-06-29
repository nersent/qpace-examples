import * as qp from "qpace/web";
// import * as pine from "qpace_example_lib_wasm";

window.onload = async () => {
  await qp.init();
  await qp.ta.init();
  // await pine.init();

  let { default: bars } = await import("../assets/btc.json");
  bars = bars.map((r) => qp.OhlcvBar.fromJSON(r));
  const ohlcv = qp.Ohlcv.fromBars(bars);
  ohlcv.timeframe = qp.Timeframe.Days(1);

  const ctx = new qp.Ctx(ohlcv, qp.Sym.BTC_USD());
  console.log(qp.ta.rsi(ctx.copy(), ctx.ohlcv.close, 14));
  // console.log(pine.script.customMa(ctx.copy(), ctx.ohlcv.close));
};
