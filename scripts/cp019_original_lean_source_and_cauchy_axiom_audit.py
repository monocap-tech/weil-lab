#!/usr/bin/env python3
"""CP019 original Zeta Lean v4.35 actual 17-new-theorem kernel custody.

Only REAL source compiled .olean files from actual pinned external
Zeta Lean v4.35 and genuine standard-only #print axioms lines may be
promoted. Numeric original Borwein circle inequality remains a NEW
explicit premise even after successful source conditional compilation.

Crucially: a file SHA, raw Lean source or exact Fraction preflight
is NOT a kernel theorem receipt; a source theorem with an explicit
hBorweinOnCircle cannot imply the universal circle bound alone.
"""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
NEW=(
 "CP019OriginalFirstJet",
 "CP019ThetaSecond",
 "CP019HolomorphicRemainder",
 "CP019CauchyRemainder",
)
PREREQ=(
 "CP013RSOnly","CP013Seam","CP014FiniteCut","CP014ZetaCut",
 "CP014HardyRank","CP015SourceWitnesses",
 "CP016FirstRSRank","CP016MonotoneAttach",
 "CP017CurvatureBudget","CP018EightCell","CP018HardyJet",
)
TARGETS=(
 "CP019OriginalFirstJet.original_theta_deriv_eq_digamma",
 "CP019OriginalFirstJet.original_hardyZ_hasDerivAt_first_source_jet",
 "CP019OriginalFirstJet.original_hardyZ_deriv_eq_first_source_jet",
 "CP019ThetaSecond.hasDerivAt_re_digamma_quarter_vertical",
 "CP019ThetaSecond.original_riemannSiegelTheta_second_deriv",
 "CP019ThetaSecond.original_phase_second_jet_matches_source",
 "CP019HolomorphicRemainder.original_remainder_differentiableOn",
 "CP019HolomorphicRemainder.closed_disk_real_part_ge_quarter",
 "CP019HolomorphicRemainder.original_zeta_remainder_diffContOnCl_ball",
 "CP019CauchyRemainder.sphere_re_quarter_le",
 "CP019CauchyRemainder.original_source_zeta_remainder_bound_on_circle",
 "CP019CauchyRemainder.exact_rational_Borwein_majorant",
 "CP019CauchyRemainder.exact_Borwein_majorant_lt_three_1e13",
 "CP019CauchyRemainder.original_zeta_EM_remainder_cauchy_budget",
 "CP019CauchyRemainder.third_derivative_original_zeta_EM_remainder_budget",
 "CP019CauchyRemainder.original_zeta_EM_cauchy_of_Borwein_circle_only",
 "CP019CauchyRemainder.original_EM_third_deriv_of_Borwein_circle_only",
)
ALLOWED={"propext","Classical.choice","Quot.sound"}
LOG=BASE/"cp019-original-source-actual-axioms.log"
RECEIPT=BASE/"cp019-original-first-jet-and-conditional-Cauchy-kernel-receipt.json"
OLEAN_DIR=BASE/".lake/build/lib/lean"

def sha(path):
 return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
 source={x:BASE/(x+".lean") for x in NEW}
 oleans={x:OLEAN_DIR/(x+".olean") for x in NEW+PREREQ}
 required=[*source.values(),*oleans.values(),LOG,BASE/"lean-toolchain"]
 missing=[str(x) for x in required if not x.is_file()]
 if missing:
  raise SystemExit("NOT_READY: real original Zeta v4.35 .olean/source/axiom outputs missing: "+repr(missing))
 if (BASE/"lean-toolchain").read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
  raise SystemExit("NOT_READY: original toolchain must be Zeta v4.35")
 for name,path in source.items():
  s=path.read_text("utf-8")
  if re.search(r"(?m)^\s*(sorry|axiom)\b",s):
   raise SystemExit("NOT_READY: added axiom/sorry in new "+name)
 for name in TARGETS:
  module,target=name.split(".",1)
  body=source[module].read_text("utf-8")
  if ("#print axioms "+name) not in body:
   raise SystemExit("NOT_READY: missing actual source #print axioms "+name)
  if ("theorem "+target) not in body:
   raise SystemExit("NOT_READY: missing genuine Lean theorem "+name)
 cauchy=source["CP019CauchyRemainder"].read_text("utf-8")
 if "hBorweinOnCircle" not in cauchy or "original_zeta_EM_cauchy_of_Borwein_circle_only" not in cauchy:
  raise SystemExit("NOT_READY: removed explicit remaining original Borwein-circle source hypothesis")
 holo=source["CP019HolomorphicRemainder"].read_text("utf-8")
 if "differentiableOn_eulerMaclaurinRemainderIoi_cpow" not in holo:
  raise SystemExit("NOT_READY: original actual holomorphic remainder proof source link missing")
 log=LOG.read_text("utf-8")
 if "sorryAx" in log or "error:" in log or "unsolved goals" in log:
  raise SystemExit("NOT_READY: real Lean error or admitted source")
 axioms={}
 for target in TARGETS:
  rx=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
  found=rx.findall(log)
  if len(found)!=1:
   raise SystemExit("NOT_READY: missing/nonunique real Lean #print axioms "+target)
  d={x.strip() for x in found[0].split(",") if x.strip()}
  if not d<=ALLOWED:
   raise SystemExit("NOT_READY: source theorem uses disallowed axioms "+target+": "+repr(d-ALLOWED))
  axioms[target]=sorted(d)
 result={
   "status":"CP019_ORIGINAL_HARDYZ_FIRST_THETA_SECOND_JET_AND_CAUCHY_CONDITIONAL_KERNEL_PASS_ONLY",
   "meaning":"Actual first HardyZ derivative, theta second derivative, exact original EM remainder holomorphy, conditional Cauchy derivative budget. Whole original Borwein bound over circles remains a source obligation.",
   "pinned_original_zeta_commit":"c06b4e13d9c847e50a32c3d738271cbad62ae9f3",
   "toolchain":"leanprover/lean4:v4.35.0",
   "new_actual_source_sha256":{n:sha(p) for n,p in source.items()},
   "new_actual_olean_sha256":{n:sha(oleans[n]) for n in NEW},
   "prerequisite_actual_olean_sha256":{n:sha(oleans[n]) for n in PREREQ},
   "actual_axiom_log_sha256":sha(LOG),
   "standard_axioms":axioms,
   "exact_Borwein_rational_bound":"181596617021805363/633825300114114700748351602688",
   "Cauchy_uniform_source_circle_cap":"3/10^13",
   "actual_all_circle_Borwein_inequality_proved":False,
   "actual_analytical_hardyZ_second_jet_identity_proved":False,
   "actual_HardyZ_Zprime_anchor_enclosed":False,
   "actual_HardyZ_Zdoubleprime_uniformly_enclosed":False,
   "new_refined_first_RS_zero_sign_accepted":False,
   "original_signed_Weil_spectral_3x3_equivalence":False,
   "RH_or_global_Weil_positivity":False
 }
 RECEIPT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(result["status"])
 print("No numeric source Z'(149.5) or uniform HardyZ curvature or RH promoted.")

if __name__=="__main__":
 main()
