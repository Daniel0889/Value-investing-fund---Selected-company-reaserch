"""Alphabet (GOOGL) - Rev 4 valuation after the Q3 2026 report (28.10.2026). USD billions.

DATA WARNING: the research environment blocked SEC, abc.xyz and news sites; inputs come
from search-engine summaries of the Q3 release, call and coverage (see sources.md).
They are UNVERIFIED until checked against the 10-Q.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
from rev4_value import Valuation, Scenario, epv, ten_x_pretax, reverse_dcf, explicit_dcf, hurdle

r = hurdle(0.0503)                     # US 10y 5.03% -> 10%
price = 292.0                          # after-hours 28.10.2026 (close 324.89, -10%)
shares = 12.368 + 19.25 / 355.0        # diluted + mandatory convertible preferred
net_cash = 265.1 - 125.1 - 19.25       # cash+securities - LT debt - preferred
mcap = price * shares

# Earning power today
ebit_q3_ann = 40.58 * 4                # 162.3
ebit_ttm = 155.0                       # estimate: Q4'25 + 9M'26 (see sources.md)
tax = 0.18
nopat_run = ebit_q3_ann * (1 - tax)    # maintenance capex ~ D&A in a no-growth world
nopat_ttm = ebit_ttm * (1 - tax)

capex_hist = [25.1, 23.5, 22.3, 24.6, 31.5, 32.3, 52.5, 91.4]   # 2018-2025
capex_2026 = 200.0
revenue_2026 = 500.0

def scenario(growth, margin, capex):
    pv, rows = explicit_dcf(revenue_2026, growth, margin, capex,
                            capex_hist[1:] + [capex_2026], r, tax)
    return (pv + net_cash) / shares, rows

def capex_path(first3, intensity):
    return first3 + [None] * 7, intensity

def build_capex(first3, intensity, growth):
    rev, out = revenue_2026, []
    for i in range(10):
        rev *= 1 + growth[i]
        out.append(first3[i] if i < 3 else rev * intensity[i - 3])
    return out

g_base = [0.20, 0.12, 0.10, 0.09, 0.08, 0.07, 0.06, 0.06, 0.05, 0.05]
m_base = [0.42, 0.44, 0.45, 0.46, 0.46, 0.46, 0.46, 0.46, 0.46, 0.46]
c_base = build_capex([280, 270, 250], [0.22, 0.22, 0.20, 0.19, 0.18, 0.18, 0.18], g_base)

g_bear = [0.14, 0.07, 0.05, 0.05, 0.05, 0.04, 0.04, 0.04, 0.04, 0.04]
m_bear = [0.40, 0.39, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38]
c_bear = build_capex([260, 220, 180], [0.20, 0.20, 0.19, 0.18, 0.18, 0.18, 0.18], g_bear)

g_bull = [0.25, 0.15, 0.13, 0.11, 0.10, 0.09, 0.08, 0.07, 0.06, 0.06]
m_bull = [0.44, 0.46, 0.48, 0.49, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50]
c_bull = build_capex([300, 300, 280], [0.20, 0.19, 0.18, 0.17, 0.17, 0.17, 0.17], g_bull)

bear, rows_bear = scenario(g_bear, m_bear, c_bear)
base, rows_base = scenario(g_base, m_base, c_base)
bull, rows_bull = scenario(g_bull, m_bull, c_bull)

v = Valuation("Alphabet", "USD", price, shares, grade="A")
v.methods = {
    "EPV, run-rate EBIT (no growth)": epv(nopat_run, r, net_cash) / shares,
    "EPV, TTM EBIT (no growth)": epv(nopat_ttm, r, net_cash) / shares,
    "10x pre-tax, run-rate EBIT": ten_x_pretax(ebit_q3_ann, net_cash) / shares,
    "explicit 10y DCF, base": base,
}
v.scenarios = [Scenario("bear", 0.25, bear), Scenario("base", 0.50, base), Scenario("bull", 0.25, bull)]

if __name__ == "__main__":
    print(f"r={r:.0%} shares={shares:.3f}B mcap={mcap:,.0f} net cash={net_cash:.1f}")
    implied = reverse_dcf(mcap, nopat_run, r, net_cash=net_cash)
    print(f"reverse DCF: price implies {implied:.1%} a year for 10 years on NOPAT {nopat_run:.0f} (FCF = NOPAT)")
    print(v.report())
    for name, rows in (("bear", rows_bear), ("base", rows_base), ("bull", rows_bull)):
        print(f"\n{name}: year  revenue  EBIT%   D&A   capex   FCF")
        for i, row in enumerate(rows):
            print(f"      {2027 + i}  {row['revenue']:7.0f}  {row['ebit_margin']:5.1%}  {row['d_and_a']:5.0f}  {row['capex']:5.0f}  {row['fcf']:5.0f}")
