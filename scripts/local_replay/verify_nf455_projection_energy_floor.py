#!/usr/bin/env python3
"""NF455 original projection floor and precision audit; NF404 is not decided."""
from fractions import Fraction as F
from pathlib import Path
import json,runpy
root=Path(__file__).resolve().parents[2]
# Run the already source-pinned six-cell and NF404 exact verifier; re-use
# its actual rational values, not copied displayed decimal approximations.
v=runpy.run_path(str(root/"scripts/local_replay/verify_nf454_gate.py"))
a_lo,a_hi,C=v["al"],v["au"],v["C"]
j=json.loads((root/"notes/data/provisional/NF404_original_selected_pole_shear_exact.json").read_text())
Rlo=F(j["original_selected_after_pole_shear_power_lower_exact"])
Rhi=F(j["original_selected_after_pole_shear_power_upper_exact"])
budget=F(j["exact_source_original_full_complement_power_budget"])
assert j["original_dimension"]==242 and j["original_selected_pole_index"]==241
assert Rlo<=Rhi and C==Rlo+budget and budget>0
# Pythagoras on ORIGINAL physical projection: Efull >= Rlo.
# Efull = A + 2 E78 is the accepted NF454 ORIGINAL identity.
floor=(Rlo-a_hi)/2
gate_at_a_hi=(C-a_hi)/2
assert floor>F("2.59e-22")
assert F("2.5988e-22")<floor<F("2.5990e-22")
assert gate_at_a_hi-floor==budget/2
assert F("2.56e-26")<budget/2<F("2.57e-26")
# Current independent outward interval uncertainty is far bigger than
# the full NF404 orthogonal residual power budget.
width=a_hi-a_lo
assert width>50*budget
assert Rhi-Rlo<budget
# Exact decision, for the true (not yet measured) R in [Rlo,Rhi]:
# E78 = (R-A)/2 + ||Q_J(w-a*s)||^2/2.
# NF404 cap iff (R-Rlo)+||Q_J w||^2 <= budget.
# No upper on the latter is supplied by the six signed cells.
out={
 "pass":"NF455",
 "standing":"ACCEPTED original projection-derived E78 lower and independent-interval precision stop; NF404 undecided",
 "original_selected_rank":242,
 "true_full_J7_J8_E78_certified_lower_approx":format(float(floor),".17e"),
 "old_NF454_easy_pass_threshold":"2.59e-22",
 "original_projected_selected_mass_approx":format(float(Rlo),".17e"),
 "original_NF404_complement_power_budget_approx":format(float(budget),".17e"),
 "exact_gap_between_projection_floor_and_gate_at_fixed_A_approx":format(float(budget/2),".17e"),
 "current_A_interval_width_approx":format(float(width),".17e"),
 "A_width_over_complement_budget_gt":50,
 "proven_identity":"E78=(R-A)/2+||Q_J(w-a*s)||^2/2",
 "exact_NF404_condition":"(R-Rlo)+||Q_J(w-a*s)||^2<=budget",
 "complete_original_E78_upper":"OPEN",
 "complete_original_J242_complement_upper":"OPEN",
 "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
print(json.dumps(out,indent=2))
