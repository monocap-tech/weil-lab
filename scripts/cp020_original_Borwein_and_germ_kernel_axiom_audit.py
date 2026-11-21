#!/usr/bin/env python3
"""CP020 FAIL-CLOSED genuine original Zeta v4.35 source .olean custody.

A true PASS requires actual original pinned Zeta-v1-1e6 original Lean
4.35, 18 real .olean files (15 CP013–19 prerequisites, three CP020
modules) and SEVENTEEN standard-only #print axioms receipts.

No SHA, source-only preflight, Fraction test or mathematically
plausible uncompiled proof can promote a theorem. Even a true kernel
pass would NOT prove Hardy-Z global curvature, CP010 narrowed root
sign, original signed Weil ↔ spectral comparison, or global RH.
"""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
NEW=("CP020Pochhammer","CP020BorweinCircle","CP020DerivativeTransport")
DEPENDENCIES=(
 "CP013RSOnly","CP013Seam",
 "CP014FiniteCut","CP014ZetaCut","CP014HardyRank",
 "CP015SourceWitnesses",
 "CP016FirstRSRank","CP016MonotoneAttach",
 "CP017CurvatureBudget",
 "CP018EightCell","CP018HardyJet",
 "CP019OriginalFirstJet","CP019ThetaSecond",
 "CP019HolomorphicRemainder","CP019CauchyRemainder",
)
TARGETS=(
 "CP020Pochhammer.norm_ascPochhammer_eval_le_product",
 "CP020Pochhammer.original_bernoulli_fourteen",
 "CP020Pochhammer.source_B14_coefficient_norm",
 "CP020Pochhammer.majorant_product_nonneg",
 "CP020BorweinCircle.source_circle_geometry",
 "CP020BorweinCircle.original_Borwein_prefactor_le",
 "CP020BorweinCircle.original_complex_cpow_bound",
 "CP020BorweinCircle.original_Borwein_omitted_term_le",
 "CP020BorweinCircle.exact_original_Borwein_real_envelope",
 "CP020BorweinCircle.original_Borwein_all_circles",
 "CP020BorweinCircle.original_EM_Cauchy_all_heights",
 "CP020BorweinCircle.original_EM_third_derivative_all_heights",
 "CP020DerivativeTransport.original_zeta_EM_germs_equal",
 "CP020DerivativeTransport.original_zeta_EM_derivative_error_identity",
 "CP020DerivativeTransport.original_center_valid",
 "CP020DerivativeTransport.original_zeta_approximant_derivative_error_all_heights",
 "CP020DerivativeTransport.original_zeta_approximant_third_derivative_error_all_heights",
)
ALLOWED={"propext","Classical.choice","Quot.sound"}
OUTPUT=BASE/"cp020-original-Borwein-circle-and-transport-kernel-receipt.json"
LOG=BASE/"cp020-original-source-genuine-axioms.log"

def sha(p):
 return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
 sources={n:BASE/(n+".lean") for n in NEW}
 oleans={n:BASE/".lake/build/lib/lean"/(n+".olean") for n in NEW+DEPENDENCIES}
 need=[*sources.values(),*oleans.values(),LOG,BASE/"lean-toolchain"]
 absent=[str(x) for x in need if not x.is_file()]
 if absent:
  raise SystemExit("NOT_READY: missing actual original external v4.35 compiled source/oleans/axiom logs "+repr(absent))
 if (BASE/"lean-toolchain").read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
  raise SystemExit("NOT_READY: original external v4.35 compiler mismatch")
 for n,path in sources.items():
  body=path.read_text("utf-8")
  if re.search(r"(?m)^\s*(axiom|sorry)\b",body):
   raise SystemExit("NOT_READY: actual sorry/new axiom in "+n)
 for target in TARGETS:
  name,decl=target.split(".",1)
  body=sources[name].read_text("utf-8")
  if "theorem "+decl not in body or "#print axioms "+target not in body:
   raise SystemExit("NOT_READY: unlisted/missing source Lean theorem or axiom target "+target)
 cir=sources["CP020BorweinCircle"].read_text("utf-8")
 if "theorem original_Borwein_all_circles" not in cir:
  raise SystemExit("NOT_READY: circular original source Borwein premise not discharged")
 if "(hBorweinOnCircle :" in cir:
  raise SystemExit("NOT_READY: new CP020 source still takes fake all-circle Borwein premise")
 trans=sources["CP020DerivativeTransport"].read_text("utf-8")
 if "Filter.EventuallyEq.iteratedDeriv_eq" not in trans or "riemannZeta_eq_approximant_add_remainder" not in trans:
  raise SystemExit("NOT_READY: actual original source germ-to-derivative transport omitted")
 log=LOG.read_text("utf-8")
 if "sorryAx" in log or "error:" in log or "unsolved goals" in log:
  raise SystemExit("NOT_READY: actual Lean elaboration/admission failure in original source")
 axioms={}
 for target in TARGETS:
  pat=re.compile(re.escape("'"+target+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
  found=pat.findall(log)
  if len(found)!=1:
   raise SystemExit("NOT_READY: missing or duplicate original #print axioms output "+target)
  ds={d.strip() for d in found[0].split(",") if d.strip()}
  if not ds<=ALLOWED:
   raise SystemExit("NOT_READY: nonstandard original Lean axioms "+target+": "+repr(ds-ALLOWED))
  axioms[target]=sorted(ds)
 result={
  "status":"CP020_ORIGINAL_ZETA_M6N256_BORWEIN_COMPLEX_CIRCLE_AND_DERIV_TRANSPORT_KERNEL_PASS",
  "scope":"Actual unassumed source Borwein cap on every moving complex circle; genuine Cauchy remainder k=0..3, original zeta approximant derivative equality of germs and error <= 1.152e-10 at third order.",
  "original_zeta_commit":"c06b4e13d9c847e50a32c3d738271cbad62ae9f3",
  "genuine_original_toolchain":"leanprover/lean4:v4.35.0",
  "new_source_sha256":{n:sha(p) for n,p in sources.items()},
  "new_actual_olean_sha256":{n:sha(oleans[n]) for n in NEW},
  "prereq_actual_olean_sha256":{n:sha(oleans[n]) for n in DEPENDENCIES},
  "actual_axiom_receipts":axioms,
  "axiom_log_sha256":sha(LOG),
  "source_derived_M":6,"source_derived_N":256,
  "circle_radius":"1/4","original_height_window":["299/2","15005353/100000"],
  "uniform_complex_Borwein_remainder_cap":"3/10^13",
  "uniform_third_derivative_zeta_approx_error":"1152/10^13",
  "proved_actual_hardyZ_first_derivative_anchor_12_div5":False,
  "proved_actual_uniform_hardyZ_curvature_le_4":False,
  "proved_genuine_original_narrow_root_53_sign":False,
  "proved_signed_Weil_to_normalized_full_spectral_matrix":False,
  "proved_global_Weil_positivity_or_RH":False
 }
 OUTPUT.write_text(json.dumps(result,indent=2)+"\n","utf-8")
 print(result["status"])
 print("This is COMPLEX Euler-Maclaurin remainder custody, not entire Hardy-Z curvature.")
if __name__=="__main__":
 main()
