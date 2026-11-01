"""Thor Explorations (TSXV/AIM: THX, OTC: THXPF) - Rev 4 valuation, 1.11.2026. USD millions.

Gold miners are a commodity business: the constitution puts them in the "cheap" track
(grade C), valued on assets at a through-cycle price, never on peak prices. Each scenario
therefore uses its own long-term gold deck from 2027, below today's ~$4,100 spot; only
Q4 2026 is priced at spot. NAV = net cash + mine-by-mine DCF at the 10% hurdle.

DATA WARNING: company, SEDAR and news sites were blocked in the research environment;
inputs come from search-engine summaries (see sources.md). UNVERIFIED.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
from rev4_value import Valuation, Scenario, hurdle

r = hurdle(0.0503)                 # USD project, US 10y 5.03% -> 10%
shares = 666.573                   # million
usdcad = 1.42
price_cad = 0.90                   # TSXV, 25.10.2026
price = price_cad / usdcad         # USD
net_cash = 236.4                   # 30.9.2026, incl. 2,825 oz bullion
spot = 4100.0                      # late Oct 2026 (~$4,074-4,118, 20-22.10)

NIGERIA_ROYALTY = 0.15             # Nigeria Tax Act 2025, from 3%
NIGERIA_TAX = 0.30                 # Pioneer status (tax holiday) through 2027
SENEGAL_ROYALTY = 0.065            # 5% state royalty + 1.5% IMC NSR (capped $60M)
SENEGAL_TAX = 0.30                 # statutory; PFS excluded incentives
SENEGAL_STATE = 0.10               # free-carried state interest (2016 code)


def pv(flows):                     # flows: {year: cash}, discounted to end-2026
    return sum(cf / (1 + r) ** (y - 2026) for y, cf in flows.items())


def segilola_pit(gold):
    """Q4 2026 pit at spot, then ~30 koz/yr from stockpiles in 2027-28, closure 2029."""
    flows = {2026.9: 17.0 * (spot - 1300) / 1000}
    for y in (2027, 2028):
        aisc = 1000 + NIGERIA_ROYALTY * gold
        pre_tax = 30.0 * (gold - aisc) / 1000
        flows[y] = pre_tax * (1 - (0 if y <= 2027 else NIGERIA_TAX))
    flows[2029] = -15.0
    return pv(flows)


def segilola_underground(gold):
    """Unreserved option: $60M capex 2027-28, 50 koz/yr 2029-33."""
    flows = {2027: -25.0, 2028: -35.0}
    for y in range(2029, 2034):
        aisc = 1400 + NIGERIA_ROYALTY * gold
        flows[y] = 50.0 * (gold - aisc) / 1000 * (1 - NIGERIA_TAX)
    return pv(flows)


def douta(gold, start=2027):
    """PFS: $254M capex over two years, 82 koz/yr for 12.6 years, AISC $1,478 at $3,500."""
    flows = {start: -254 * 0.4, start + 1: -254 * 0.6}
    for i in range(13):
        oz = 82.0 * (0.6 if i == 12 else 1.0)
        aisc = 1250 + SENEGAL_ROYALTY * gold
        flows[start + 2 + i] = oz * (gold - aisc) / 1000 * (1 - SENEGAL_TAX)
    flows[start + 15] = -20.0
    return pv(flows) * (1 - SENEGAL_STATE)


G_AND_A = -45.0                    # PV of corporate costs outside AISC

def nav(gold, p_douta, p_ug, exploration):
    return (net_cash + segilola_pit(gold) + p_ug * segilola_underground(gold)
            + p_douta * douta(gold) + exploration + G_AND_A)

SCEN = {  # gold deck, P(Douta built from 2027), P(underground), exploration
    "bear": (2800.0, 0.40, 0.00, 10.0),
    "base": (3500.0, 0.65, 0.40, 20.0),
    "bull": (4500.0, 0.85, 0.70, 40.0),
}

v = Valuation("Thor Explorations (USD per share)", "USD", price, shares, grade="C", extra_margin=0.05)
v.methods = {f"NAV at ${g:,.0f} gold ({k})": nav(g, pd, pu, ex) / shares for k, (g, pd, pu, ex) in SCEN.items()}
v.methods["NAV at $4,100 spot, base risking"] = nav(spot, 0.65, 0.40, 20.0) / shares
v.scenarios = [Scenario(k, p, nav(*SCEN[k]) / shares) for k, p in (("bear", 0.25), ("base", 0.50), ("bull", 0.25))]

def implied_gold():
    lo, hi = 1000.0, 8000.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if nav(mid, 0.65, 0.40, 20.0) < price * shares:
            lo = mid
        else:
            hi = mid
    return mid

if __name__ == "__main__":
    print(f"price C${price_cad} = US${price:.3f}; mcap US${price * shares:.0f}M; EV US${price * shares - net_cash:.0f}M")
    for k, (g, pd, pu, ex) in SCEN.items():
        print(f"{k:>5} gold ${g:,.0f}: pit {segilola_pit(g):6.1f}  UG(100%) {segilola_underground(g):6.1f}  "
              f"Douta(attrib, unrisked) {douta(g):6.1f}  NAV {nav(g, pd, pu, ex):6.1f}")
    print(f"Douta unrisked at spot: {douta(spot):.0f}; one-year delay at base: {douta(3500, 2028):.0f}")
    print(v.report())
    print(f"buy line in CAD: C${v.buy_line() * usdcad:.2f}; base value C${v.base_value() * usdcad:.2f}")
    print(f"price implies a long-term gold price of ${implied_gold():,.0f}/oz (base risking)")
    print(f"cash per share US${net_cash / shares:.3f} = {net_cash / (price * shares):.0%} of market cap")
    print(f"dividend C$0.05/yr = {0.05 / price_cad:.1%} yield")
