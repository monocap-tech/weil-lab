#!/usr/bin/env python3
"""Generate a bounded one-key Lean trial from an untrusted integer receipt."""
import argparse
import gzip
import json
from pathlib import Path
from fractions import Fraction

def qlit(s):
    q=Fraction(s)
    return f"({q.numerator}/{q.denominator}:ℚ)"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("receipt",type=Path)
    ap.add_argument("output",type=Path)
    ap.add_argument("--h",default="0")
    ap.add_argument("--f",default="37/32")
    ap.add_argument("--count",type=int,default=1)
    args=ap.parse_args()
    with gzip.open(args.receipt,"rt") as f:
        data=json.load(f)
    assert data["scale"]=="10^2600" and data["exp_terms"]==1200 and data["atan_terms"]==2000
    h,f=Fraction(args.h),Fraction(args.f)
    t=next(t for t in data["tables"] if Fraction(t["h"])==h and Fraction(t["f"])==f)
    assert 0<args.count<=len(t["rows"])
    def scaled(s):
        return f"({int(s)}:ℚ)/(neutralNF616Q:ℚ)"
    entries=",\n  ".join("⟨"+",".join(map(scaled,row))+"⟩" for row in t["rows"][:args.count])
    count=args.count
    args.output.write_text(f"""import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFastMomentTable

namespace WeilDefect
noncomputable section

def nf621TrialKey : NF616Frequency := ⟨{qlit(h)},{qlit(f)}⟩

def nf621TrialRows : Array NF617MomentRow := #[
  {entries}
]

set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem nf621TrialCheck :
    neutralNF621FastTableCheck
      (neutralNF592PiBall neutralNF616Q neutralNF616AtanN)
      nf621TrialKey neutralNF616Q neutralNF616ExpN nf621TrialRows = true := by
  decide +kernel

theorem nf621TrialSound (n : ℕ) (hn : n < nf621TrialRows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) nf621TrialKey.value n-
      (neutralNF617MomentRead nf621TrialRows n).value‖ ≤
        (neutralNF617MomentRead nf621TrialRows n).rad :=
  neutralNF621FastHighPrecision_sound nf621TrialKey nf621TrialRows nf621TrialCheck n hn

#print axioms nf621TrialCheck
#print axioms nf621TrialSound

end
end WeilDefect
""")
    print(f"emitted {count} untrusted row proposals; no proof asserted")
if __name__=="__main__":
    main()
