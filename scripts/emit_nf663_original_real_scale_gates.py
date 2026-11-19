#!/usr/bin/env python3
"""NF663: attach NF659's accepted 450 integer gates to actual real NF662 H.

All generated proofs refer to the existing exact NF659 theorems, not an
independent numerical computation. The source-real enclosure conclusion
also consumes NF662's all-225 actual integral membership theorem.
Compiler/axiom verification of this new attachment is separately required.
"""
import argparse
import hashlib
import json
from pathlib import Path

N=15
pref="WeilDefect.Generated.NF663."
def wrap(imports,body):
    return "".join(f"import {p}\n" for p in imports)+"""
namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0
noncomputable section

"""+body+"\nend\nend WeilDefect\n"

def main(out):
    out.mkdir(parents=True,exist_ok=True)
    files=[]
    def emit(name,imports,body):
        path=out/(name+".lean")
        path.write_text(wrap(imports,body))
        files.append({"file":path.name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    KI="(fun a b : Fin 15 => nf658Get nf658Kints a b)"
    CI="(fun a b : Fin 15 => nf658Get nf658Centers a b)"
    EI="(fun a b : Fin 15 => nf658Get nf658Radii a b)"
    for i in range(N):
        body=""
        for j in range(N):
            body+=f"""theorem nf663Center{i:02d}_{j:02d} :
    neutralNF663CenterInteger {KI} {CI}
      ({i} : Fin 15) ({j} : Fin 15) = nf659CenterAt {i} {j} := by
  change nf658TransformedCenter {i} {j} = nf659CenterAt {i} {j}
  exact nf659C{i:02d}_{j:02d}

theorem nf663Radius{i:02d}_{j:02d} :
    neutralNF663RadiusInteger {KI} {EI}
      ({i} : Fin 15) ({j} : Fin 15) = nf659RadiusAt {i} {j} := by
  change nf658TransformedRadius {i} {j} = nf659RadiusAt {i} {j}
  exact nf659R{i:02d}_{j:02d}

"""
        emit(f"Row{i:02d}",["WeilDefect.Generated.NF659.Complete",
            "WeilDefect.Generated.NF662.Complete",
            "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalGramIntegerRealScale"],body)
    body=f"""theorem nf663AllCenters (i j : Fin 15) :
    neutralNF663CenterInteger {KI} {CI} i j = nf659CenterAt i j := by
  fin_cases i <;> fin_cases j
"""
    for i in range(N):
        for j in range(N):body+=f"  · exact nf663Center{i:02d}_{j:02d}\n"
    body+=f"""
theorem nf663AllRadii (i j : Fin 15) :
    neutralNF663RadiusInteger {KI} {EI} i j = nf659RadiusAt i j := by
  fin_cases i <;> fin_cases j
"""
    for i in range(N):
        for j in range(N):body+=f"  · exact nf663Radius{i:02d}_{j:02d}\n"
    body+="""

/-- Every original 15-generator REAL physical H entry is contained in
the 64-digit rational center/radius array, not just its numerical center. -/
theorem nf663OriginalPhysical_sourceEnclosed (p q : Fin 15) :
    |neutralNF661PhysicalH p q -
      (nf658Get nf658Centers p q : ℝ)/(10 ^ 64 : ℝ)| ≤
      (nf658Get nf658Radii p q : ℝ)/(10 ^ 64 : ℝ) := by
  have hb := nf662AllOriginalPhysicalCompact p q
  simpa [nf662PhysicalCompactBall, NF591Ball.Contains] using hb

/-- Terminal NF663 physical-real statement. The two interval bounds are
the exact 225 integer values certified independently in NF659.
It neither assumes an eigenvalue bound nor proves global positivity. -/
theorem nf663ActualPhysical_transformedEnclosed (i j : Fin 15) :
    |neutralNF662Congruence nf662OriginalPreconditionerReal
        neutralNF661PhysicalH i j -
      (nf659CenterAt i j : ℝ)/(10 ^ 64 : ℝ)^3| ≤
      (nf659RadiusAt i j : ℝ)/(10 ^ 64 : ℝ)^3 := by
  have hb := neutralNF663ActualIntegerCongruence_enclosed
    neutralNF661PhysicalH
    (fun a b : Fin 15 => nf658Get nf658Kints a b)
    (fun a b : Fin 15 => nf658Get nf658Centers a b)
    (fun a b : Fin 15 => nf658Get nf658Radii a b)
    (10 ^ 64 : ℝ) (by positivity)
    nf663OriginalPhysical_sourceEnclosed i j
  change
    |neutralNF662Congruence nf662OriginalPreconditionerReal
        neutralNF661PhysicalH i j -
      (neutralNF663CenterInteger
        (fun a b : Fin 15 => nf658Get nf658Kints a b)
        (fun a b : Fin 15 => nf658Get nf658Centers a b) i j : ℝ) /
          (10 ^ 64 : ℝ)^3| ≤
      (neutralNF663RadiusInteger
        (fun a b : Fin 15 => nf658Get nf658Kints a b)
        (fun a b : Fin 15 => nf658Get nf658Radii a b) i j : ℝ) /
          (10 ^ 64 : ℝ)^3 at hb
  rw [nf663AllCenters i j, nf663AllRadii i j] at hb
  exact hb

#print axioms nf663OriginalPhysical_sourceEnclosed
#print axioms nf663AllCenters
#print axioms nf663AllRadii
#print axioms nf663ActualPhysical_transformedEnclosed
"""
    emit("Complete",[pref+f"Row{i:02d}" for i in range(N)],body)
    data={"schema":"NF663-original-physical-integer-to-real-v1",
          "center_gate_references":225,"radius_gate_references":225,
          "source":"NF658/NF659/NF662 proof artifacts",
          "scope":"emitted Lean theorem candidates until kernel audit passes",
          "files":files}
    (out/"manifest.json").write_text(json.dumps(data,indent=2)+"\n")
    print("NF663 generated 450 theorem references and a real physical transformed enclosure target")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("output",type=Path)
    main(p.parse_args().output)
