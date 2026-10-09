#!/usr/bin/env python3
"""NF16: improve genuine original physical F112 complement from 17/100
to 207/1000 at a=53/50, *without* inheriting old aperture certificates.

Uses only NF10's two strict rational bounds from the same target:
  arch - 13/5 - poles > raw_lower
  complete weighted-prime Schur norm < prime_upper_6000.
Thus Q|F112 > raw_lower + 13/5 - prime_upper_6000.
No improved full E112 native or corrected whole-domain Schur is inferred.
"""
import json
from fractions import Fraction as F
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"notes/data/RPB108_NF10_COMPLEMENT106_CERTIFICATE_20261008.json"
data=json.loads(p.read_text())
assert data["aperture"]=="53/50"
assert data["certified_joint_prime_norm_upper"]=="13/5"
assert data["physical_complement_certified_lower"]=="17/100"
raw=F(data["physical_complement_raw_lower_rounded"])
prime=F(data["prime_operator_enclosure_6000"]["upper"])
target=raw+F(13,5)-prime
assert prime<F(257,100)
assert target>F(207,1000)
assert F(207,1000)>F(17,100)
print(json.dumps(dict(
   status="PASS",aperture="53/50",retained_modes=112,
   strict_new_derived_raw_lower=str(target),
   original_F112_physical_lower="207/1000",
   original_complete_prime_operator_bound=str(prime),
   inverse_factor_upper="1000/207",
   derivation="old NF10 raw minus old prime allowance 13/5 plus independently enclosed full six-prime operator",
   source_rebuilt=False,native_E112_complete=False,
   corrected_full_Schur=False,whole_aperture_positive=False),indent=2))
