#!/usr/bin/env python3
"""NF465 exact rational resolution audit: no source-integral certification claimed."""
from fractions import Fraction as F
import json, argparse
from pathlib import Path
M=F(30000)
zlow=F(65,10**12)  # 6.5e-11, inherited conservative original J7 anchor
zhigh=F(9,10**11)  # 9e-11
x0=F(26,25)
# Source-independent logical consequence of the inherited source-certified
# anchor and global Lipschitz bound only: positivity persists for r=zlow/M.
r=zlow/M
assert r==F(13,6*10**15)
# Beyond r, the function zlow-M*abs(x-x0) is an admissible
# Lipschitz-compatible alternative (not the original Weil source).
assert zlow-M*r==0
assert F(1,100)>r
# Largest certified nonnegative symmetric interval is 2*r.
# A 1/100 macroscopic step cannot be decided from this data alone.
ratio=F(1,100)/r
assert ratio>10**12
# Entire genuine J7 is >0.11 in length (original exact rational
# artanh bound inherited in NF464; here only conservative comparison).
assert F(11,100)/(2*r)>10**13
out={"pass":"NF465","standing":"METHOD STOP: anchor-plus-Lipschitz-only propagation, not original signed integral",
     "original_nf417_418_anchor_x":"26/25","original_z_anchor_lower":"6.5e-11",
     "original_z_anchor_upper":"9e-11","original_derivative_absolute_bound":"30000",
     "positivity_radius_at_anchor_exact":str(r),
     "positivity_radius_decimal":float(r),
     "one_hundredth_unit_step_to_radius_ratio_strict_gt":"1e12",
     "J7_length_0_11_over_two_r_strict_gt":"1e13",
     "counterexample_is_abstract_lipschitz_function_not_original_source":True,
     "original_macroscopic_signed_J7_integral":"OPEN",
     "next":"NF466 actual original-source compact-kernel correlated interval evaluator; do not attempt derivative-only tiling"}
print(json.dumps(out,indent=2))
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--output");a=p.parse_args()
 if a.output:Path(a.output).write_text(json.dumps(out,indent=2)+"\n")
