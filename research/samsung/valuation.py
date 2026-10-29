"""Samsung Electronics (005930 / 005935) - Rev 4 valuation after Q3 2026 (29.10.2026). KRW trillions.

The constitution puts cyclicals in the "cheap" track only: no net debt, valued on
trough or mid-cycle earnings, never on peak. Memory is at a super-cycle peak
(Q3 OP margin 55%), so the base case capitalises through-cycle earnings and adds
the present value of the boom years separately.

DATA WARNING: Samsung IR, DART and news sites were blocked in the research
environment; inputs come from search-engine summaries (see sources.md). UNVERIFIED.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
from rev4_value import Valuation, Scenario, hurdle

r = hurdle(0.0407)                         # Korea 10y 4.07% -> 10%
tax = 0.20
price_common = 232_000                     # close 29.10.2026 (-4.13%)
price_pref = 166_300                       # 26.10.2026, latest found
shares = (5_919.6 + 816.0 - 136.7) / 1000  # bn shares outstanding, common + pref, ex-treasury
net_cash = 197.6
after_tax_interest = net_cash * 0.03 * (1 - tax)

op_history = {2016: 29.24, 2017: 53.65, 2018: 58.89, 2019: 27.77, 2020: 35.99,
              2021: 51.63, 2022: 43.38, 2023: 6.57, 2024: 32.73, 2025: 43.60}
op_2026e = 254.1 + 120.0                   # 9M actual + Q4 inside the 107-126 consensus band
avg_10y_pre_boom = sum(op_history.values()) / 10
avg_10y_incl_2026 = (sum(op_history.values()) - op_history[2016] + op_2026e) / 10

def value_per_share(normal_op, boom):
    """Capitalised normal earnings + PV of after-tax excess profit in the boom years."""
    epv_equity = (normal_op * (1 - tax) + after_tax_interest) / r + net_cash
    excess = sum((op - normal_op) * (1 - tax) / (1 + r) ** (i + 1) for i, op in enumerate(boom))
    return (epv_equity + excess) * 1e12 / (shares * 1e9)

bear = value_per_share(50.0, [350.0, 150.0])     # prices roll over in 2027-28
base = value_per_share(avg_10y_incl_2026, [450.0, 300.0])
bull = value_per_share(120.0, [550.0, 400.0])    # AI lifts mid-cycle earnings structurally

v = Valuation("Samsung Electronics (per common-equivalent share)", "KRW", price_common, shares, grade="C")
v.methods = {
    "10x pre-tax, 2016-25 average OP": (10 * avg_10y_pre_boom + net_cash) * 1e3 / shares,
    "10x pre-tax, 2017-26E average OP": (10 * avg_10y_incl_2026 + net_cash) * 1e3 / shares,
    "EPV on 2017-26E average OP": ((avg_10y_incl_2026 * (1 - tax) + after_tax_interest) / r + net_cash) * 1e3 / shares,
    "base: EPV + PV of 2027-28 boom": base,
}
v.scenarios = [Scenario("bear", 0.30, bear), Scenario("base", 0.45, base), Scenario("bull", 0.25, bull)]

def implied_normal_op(price, boom):
    lo, hi = 0.0, 500.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if value_per_share(mid, boom) < price:
            lo = mid
        else:
            hi = mid
    return mid

if __name__ == "__main__":
    mcap = (5_919.6 * price_common + 816.0 * price_pref) / 1e6
    print(f"r={r:.0%} shares={shares:.3f}bn mcap~{mcap:,.0f}T net cash {net_cash}T")
    print(f"avg OP 2016-25 {avg_10y_pre_boom:.1f}T; 2017-26E {avg_10y_incl_2026:.1f}T; 2026E {op_2026e:.0f}T")
    print(v.report())
    print(f"price implies normal OP of {implied_normal_op(price_common, [450.0, 300.0]):.0f}T after a 450/300 boom")
    print(f"preferred at {price_pref:,}: discount {1 - price_pref / price_common:.0%}, "
          f"price/base {price_pref / base:.2f}, price/buy line {price_pref / v.buy_line():.2f}")
    print(f"Q3 DPS 4,601: {4601 / price_common:.1%} on common, {4601 / price_pref:.1%} on pref (one quarter)")
    print(f"2026 returns 90-110T = {90 / mcap:.1%}-{110 / mcap:.1%} of market cap")
