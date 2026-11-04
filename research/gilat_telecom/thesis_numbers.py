"""Derived figures used in research/gilat_telecom/thesis_he.md that are not printed in output.txt or gate.md.

Every input is read from research/gilat_telecom/financials.json (each value there carries its document/page ref).
Run from the repository root: python3 -I research/gilat_telecom/thesis_numbers.py > research/gilat_telecom/thesis_numbers_output.txt
No valuation figure is computed here; output.txt (valuation.py) owns every value, margin and size.
Committed at the final edit (MF-15): the memo's header cites it, so it must reproduce from the repository.
"""
import json
import pathlib
import sys

FIN = pathlib.Path(__file__).resolve().parent / "financials.json"
d = json.load(open(FIN, encoding="utf-8"))
P = d["periods"]
FY = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]


def v(period: str, field: str):
    f = P[period].get(field)
    return None if f is None else f.get("v")


out = []
p = out.append

# 1. ROE = NI to owners / average equity to owners (FY2021 opening equity = 1.1.2021, restated); TTM on 30.6.2025 and 30.6.2026
eq_open = {"FY2021": v("FY2021", "equity_owners_opening")}
for a, b in zip(FY, FY[1:]):
    eq_open[b] = v(a, "equity_owners")
p("1. ROE = NI to owners / average equity (USD k; TTM ILS k)")
for y in FY:
    ni, e1, e0 = v(y, "net_income_owners"), v(y, "equity_owners"), eq_open[y]
    p(f"   {y}: NI {ni:,} / avg({e0:,}, {e1:,}) = {ni / ((e0 + e1) / 2):.1%}")
ni_t = v("TTM_2026-06-30", "net_income_owners")
e25, e26 = v("H1_2025", "equity_owners"), v("H1_2026", "equity_owners")
p(f"   TTM: NI {ni_t:,} / avg({e25:,}, {e26:,}) = {ni_t / ((e25 + e26) / 2):.1%}")

# 2. Segment shares of revenue and growth (USD k; gilat_fy2023 p.166-167, gilat_fy2025 p.181-182 via financials.json)
s = d["segments"]
p("2. Segment revenue shares")
for y in FY:
    tot = v(y, "revenue")
    g, gl, isp = (s[y][k]["revenue"] for k in ("government_defence", "global_business", "israel_comm_internet"))
    p(f"   {y}: revenue {tot:,}; government/defence {g:,} = {g / tot:.1%}; global (Africa) {gl:,} = {gl / tot:.1%}; Israel ISP {isp:,} = {isp / tot:.1%}")
g21, g25 = s["FY2021"]["government_defence"]["revenue"], s["FY2025"]["government_defence"]["revenue"]
a21, a25 = s["FY2021"]["global_business"]["revenue"], s["FY2025"]["global_business"]["revenue"]
p(f"   government/defence revenue FY2025 / FY2021 = {g25 / g21:.2f}x; global (Africa) FY2025 / FY2021 = {a25 / a21:.2f}x ({a25 / a21 - 1:+.0%})")
for y in FY:
    seg = s[y]["government_defence"]
    p(f"   {y}: government/defence segment margin {seg['result'] / seg['revenue']:.1%}")

# 3. Concentration, FY2025 (FS note gilat_fy2025 p.182: amounts in USD millions)
conc = [c for c in d["concentration"] if c.get("period") == "FY2025"]
tot25 = v("FY2025", "revenue")
two = sum(c["revenue_usd_k"] for c in conc)
p(f"3. FY2025 named customers: " + "; ".join(f"{c['customer'].split(':')[0]} {c['revenue_usd_k']:,} = {c['revenue_usd_k'] / tot25:.1%}" for c in conc)
  + f"; together {two:,} = {two / tot25:.1%}")

# 4. ISP KPIs (gilat_fy2025 p.94; gilat_h1_2026 p.8)
k = d["kpis"]
subs = k["isp_private_subscribers_end"]
p(f"4. ISP private subscribers 31.12.2024 {subs['2024-12-31']:,} -> 30.6.2026 {subs['2026-06-30']:,} = {subs['2026-06-30'] / subs['2024-12-31']:.1f}x;"
  f" ARPU FY2024 {k['isp_arpu_ils_monthly']['FY2024']} -> Q2 2026 {k['isp_arpu_ils_monthly']['Q2_2026']}")

# 5. Pay relative to profit (related-parties note, gilat_fy2025 p.176)
rp = d["related_parties_comp"]
p("5. CEO employment cost (related-parties note, USD k) and NI to owners")
for y in ("2023", "2024", "2025"):
    c = rp["interested_party_employed_salary"][y]
    ni = v("FY" + y, "net_income_owners")
    p(f"   {y}: CEO {c:,} = {c / ni:.0%} of NI {ni:,}; key management {rp['key_management_total'][y]:,}")

print("\n".join(out))
sys.exit(0)
