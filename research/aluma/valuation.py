"""Aluma Infrastructure Fund (TASE 1181643) - Rev 4 valuation, ILS millions.

DATA WARNING: Israeli sites (Maya, Globes, Bizportal...) were blocked in the research
environment. Every input below comes from search-engine summaries of the cited
articles and is UNVERIFIED until checked against the Maya filings.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "lib"))
from rev4_value import Valuation, Scenario

equity_30jun26 = 455.5          # Maya company page / Bizportal 20045210
dividend_oct26 = 61.3           # paid 12.10.2026, 20.17 agorot/share
dc_placement = 12.0             # Discount Capital, ILS 1.13/share pre-dividend
shares_record = dividend_oct26 / 0.2017            # ~303.9M at record date
shares = shares_record + dc_placement / 1.13       # ~314.5M after placement
price = 0.80                    # ILS, ~19.10.2026 close (80 agorot)

nav = equity_30jun26 - dividend_oct26 + dc_placement          # pro-forma book NAV
nav_ps = nav / shares

# Non-binding MOU: ILS 150M for 20% of Alumenergy at ILS 750M post-money.
# Aluma's ~84% stake: implied ~413M at the Discount Capital price, ~504M at the MOU price.
mou_uplift = 0.84 * 600 - 0.84 * (411 + 81)
# External manager: ~1-1.5% of ~655M assets a year, about 2.2% of NAV.
# Value to the owner after fees, at the 10% hurdle: NAV * r / (r + fee drag) ~ 0.82.
fee_factor = 0.10 / (0.10 + 0.015 * 655.1 / equity_30jun26)
level3_haircut = 0.25           # bear case: unlisted marks 25% too high

bear = nav * (1 - level3_haircut) * fee_factor / shares
base = nav * fee_factor / shares
bull = (nav + mou_uplift) * fee_factor / shares

v = Valuation("Aluma Infrastructure Fund", "ILS", price, shares, grade="C", extra_margin=0.05)
v.methods = {
    "pro-forma book NAV": nav_ps,
    "NAV incl. MOU mark": (nav + mou_uplift) / shares,
    "owner value after fees (base)": base,
}
v.scenarios = [Scenario("bear", 0.30, bear), Scenario("base", 0.50, base), Scenario("bull", 0.20, bull)]

if __name__ == "__main__":
    print(f"shares {shares:.1f}M  NAV {nav:.1f}M  NAV/share {nav_ps:.3f}  P/NAV {price / nav_ps:.2f}")
    print(f"market cap {price * shares:.1f}M  MOU uplift {mou_uplift:.1f}M  fee factor {fee_factor:.3f}")
    print(v.report())
