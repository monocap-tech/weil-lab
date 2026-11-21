#!/usr/bin/env python3
"""CP018 real Lean kernel + standard axiom custody; fail-closed.

The original upstream v4.35 source is imported and new local CP013-017
Lean source modules plus BOTH CP018 modules require actual compiled
.olean. This does NOT mark a genuine source derivative formula or
numerical 8-cell intervals as certified: those remain explicit premises.
"""
import hashlib
import json
import re
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]/"cp011_zeta_v435"
SRC=("CP018EightCell","CP018HardyJet")
DEPENDENCIES=(
 "CP013RSOnly","CP013Seam","CP014FiniteCut","CP014ZetaCut",
 "CP014HardyRank","CP015SourceWitnesses","CP016FirstRSRank",
 "CP016MonotoneAttach","CP017CurvatureBudget",
)
TARGETS=(
 "CP018EightCell.center_mem_interval",
 "CP018EightCell.eight_center_cover",
 "CP018EightCell.exact_eight_cell_curvature_margin",
 "CP018EightCell.eight_midpoints_and_third_derivative_imply_curvature",
 "CP018EightCell.original_hardyZ_strictMono_of_eight_midpoint_certificate",
 "CP018HardyJet.uniform_curvature_of_eight_source_jet_boxes",
 "CP018HardyJet.genuine_anchor_of_first_jet_certificate",
)
ALLOWED={"propext","Classical.choice","Quot.sound"}
OLEAN_DIR=BASE/".lake/build/lib/lean"
LOG=BASE/"cp018-original-hardy-eight-cell-actual-axioms.log"
OUTPUT=BASE/"cp018-original-hardy-8-cell-conditional-kernel-receipt.json"

def sha(path):
 return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
 sources={m:BASE/(m+".lean") for m in SRC}
 all_oleans={m:OLEAN_DIR/(m+".olean") for m in SRC+DEPENDENCIES}
 required=[*sources.values(),*all_oleans.values(),LOG,BASE/"lean-toolchain"]
 absent=[str(p) for p in required if not p.is_file()]
 if absent: raise SystemExit("NOT_READY: real original external source .olean or actual axiom log absent: "+repr(absent))
 if (BASE/"lean-toolchain").read_text("utf-8").strip()!="leanprover/lean4:v4.35.0":
  raise SystemExit("NOT_READY: original v4.35 toolchain changed")
 for name,f in sources.items():
  text=f.read_text("utf-8")
  if re.search(r"(?m)^\s*(axiom|sorry)\b",text):
   raise SystemExit("NOT_READY: hidden declared axiom or sorry in new "+name)
 eight=sources["CP018EightCell"].read_text("utf-8")
 jet=sources["CP018HardyJet"].read_text("utf-8")
 for text in ["(hD2diff :","(hD3 :","(hcenters :",
              "(hD1diff :","(hanchor :"]:
  if text not in eight:
   raise SystemExit("NOT_READY: source eight-center numerical/smoothness hypothesis omitted: "+text)
 for text in ["(hidentity :", "(hboxes :",
              "deriv (deriv Zeta.hardyZ) t = sourceSecondJet t",
              "deriv Zeta.hardyZ a = sourceFirstJet a"]:
  if text not in jet:
   raise SystemExit("NOT_READY: source derivative jet exactness or whole-cell interval box hypothesis omitted: "+text)
 log=LOG.read_text("utf-8")
 if "sorryAx" in log or "error:" in log or "unsolved goals" in log:
  raise SystemExit("NOT_READY: genuine Lean error/admission in compiled axiom output")
 axioms={}
 for name in TARGETS:
  rx=re.compile(re.escape("'"+name+"'")+r"\s+depends on axioms:\s*\[([^\]]*)\]")
  found=rx.findall(log)
  if len(found)!=1:
   raise SystemExit("NOT_READY: no unique real Lean #print axioms "+name)
  deps={x.strip() for x in found[0].split(",") if x.strip()}
  if not deps<=ALLOWED:
   raise SystemExit("NOT_READY: nonstandard Lean axioms: "+name+": "+repr(deps-ALLOWED))
  axioms[name]=sorted(deps)
 out={
  "status":"CP018_ORIGINAL_HARDY_8CELL_AND_COMPLEX_JET_CONDITIONAL_KERNEL_PASS_ONLY",
  "scope":"Seven formal logical/real-analysis sufficiency implications with explicit UNSOLVED original analytic jet, center derivative, third derivative, and root sign inputs.",
  "external_pinned_original_Zeta":"c06b4e13d9c847e50a32c3d738271cbad62ae9f3",
  "external_original_Lean":"leanprover/lean4:v4.35.0",
  "source_sha256":{m:sha(p) for m,p in sources.items()},
  "actual_new_olean_sha256":{m:sha(all_oleans[m]) for m in SRC},
  "dependency_olean_sha256":{m:sha(all_oleans[m]) for m in DEPENDENCIES},
  "real_standard_axioms":axioms,
  "actual_axiom_log_sha256":sha(LOG),
  "rational_curvature_upper":"1566059/400000",
  "rational_curvature_slack":"33941/400000",
  "genuine_original_theta_prime_and_double_prime_identity_proved":False,
  "genuine_original_zeta_first_and_second_derivatives_enclosed":False,
  "original_Z_double_prime_eight_interval_boxes_proved":False,
  "original_Z_third_prime_uniform_enclosure_proved":False,
  "original_Z_prime_anchor_proved":False,
  "genuine_new_refined_zero_sign_proved":False,
  "original_signed_Weil_spectral_matrix_equality_proved":False,
  "RH_or_global_Weil_positivity":False
 }
 OUTPUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 print(out["status"])
 print("A conditional kernel proof is NOT a validated analytic derivative enclosure or numerical root53 proof.")

if __name__=="__main__":
 main()
