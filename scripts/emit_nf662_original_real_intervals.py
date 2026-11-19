#!/usr/bin/env python3
"""NF662: proof candidates attaching all 225 real original physical H entries.

Consumes the established NF658 source/compact-ball theorems and exact original
NF661 source enumeration. Does not assume a new interval or numeric fact.
Generated modules are candidates until Lean and axiom audits pass.
"""
import argparse
import hashlib
import json
from pathlib import Path

N = 15
INDICES = [*range(14), 241]


def hname(i, j):
    a, b = sorted((INDICES[i], INDICES[j]), reverse=True)
    return f"nf658H{a:03d}_{b:03d}"


def theorem_name(i, j):
    return f"nf662RealH{i:02d}_{j:02d}"


def produce(out: Path):
    out.mkdir(parents=True, exist_ok=True)
    files = []

    def write(name, imports, body):
        s = "\n".join("import " + p for p in imports)
        s += "\n\nnamespace WeilDefect\nset_option maxRecDepth 100000\n"
        s += "set_option maxHeartbeats 0\n\n" + body + "\nend WeilDefect\n"
        path = out / (name + ".lean")
        path.write_text(s)
        files.append({"file": path.name,
                      "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})

    for i in range(N):
        body = []
        for j in range(N):
            a, b = max(i, j), min(i, j)
            name = theorem_name(i, j)
            old = hname(i, j)
            stmt = f"""theorem {name} :
    (nf662PhysicalCompactBall ({i} : Fin 15) ({j} : Fin 15)).Contains
      (neutralNF661PhysicalH ({i} : Fin 15) ({j} : Fin 15)) := by"""
            lines = [stmt]
            if i < j:
                lines.extend([
                    f"  rw [nf662CompactBalls_symm ({i} : Fin 15) ({j} : Fin 15),",
                    f"    neutralNF661PhysicalH_symm ({i} : Fin 15) ({j} : Fin 15)]",
                ])
            lines.extend([
                "  have heq :",
                f"      nf662PhysicalCompactBall ({a} : Fin 15) ({b} : Fin 15) =",
                f"        {old}Ball := by",
                "    apply nf662Ball_ext <;> decide +kernel",
                "  rw [heq]",
                "  simpa [neutralNF661PhysicalH, neutralNF661Source] using",
                f"    {old}Contains",
            ])
            body.append("\n".join(lines))
        allrow = [
            f"theorem nf662AllRow{i:02d} (j : Fin 15) :",
            f"    (nf662PhysicalCompactBall ({i} : Fin 15) j).Contains",
            f"      (neutralNF661PhysicalH ({i} : Fin 15) j) := by",
            "  fin_cases j",
        ]
        for j in range(N):
            allrow.append(f"  · exact {theorem_name(i,j)}")
        body.append("\n".join(allrow))
        body.append(f"#print axioms {theorem_name(i,0)}")
        body.append(f"#print axioms {theorem_name(i,14)}")
        write(f"Row{i:02d}", ["WeilDefect.Generated.NF662.PhysicalPilots"],
              "\n\n".join(body))

    complete = [
        "theorem nf662AllOriginalPhysicalCompact :",
        "    ∀ i j : Fin 15,",
        "      (nf662PhysicalCompactBall i j).Contains",
        "        (neutralNF661PhysicalH i j) := by",
        "  intro i j",
        "  fin_cases i",
    ]
    for i in range(N):
        complete.append(f"  · exact nf662AllRow{i:02d} j")
    complete.append("""
noncomputable def nf662OriginalCenterReal (i j : Fin 15) : ℝ :=
  ((nf662PhysicalCompactBall i j).mid : ℝ)

noncomputable def nf662OriginalRadiusReal (i j : Fin 15) : ℝ :=
  ((nf662PhysicalCompactBall i j).rad : ℝ)

noncomputable def nf662OriginalPreconditionerReal (i j : Fin 15) : ℝ :=
  (nf658Get nf658Kints i j : ℝ) / (10 ^ 64 : ℝ)

/-- All 225 real transformed physical H entries are enclosed in
the exact 64-digit source interval propagation; numeric identification
with the NF659 integer transformed arrays is a separate final gate. -/
theorem nf662AllOriginalTransformedRealEnclosed (i j : Fin 15) :
    |neutralNF662Congruence nf662OriginalPreconditionerReal
        neutralNF661PhysicalH i j -
      neutralNF662Center nf662OriginalPreconditionerReal
        nf662OriginalCenterReal i j| ≤
      neutralNF662Radius nf662OriginalPreconditionerReal
        nf662OriginalRadiusReal i j := by
  apply neutralNF662ActualCongruence_enclosed
    neutralNF661PhysicalH nf662OriginalCenterReal
    nf662OriginalRadiusReal nf662OriginalPreconditionerReal
  intro p q
  exact nf662AllOriginalPhysicalCompact p q

#print axioms nf662AllOriginalPhysicalCompact
#print axioms nf662AllOriginalTransformedRealEnclosed
""")
    write("Complete", [f"WeilDefect.Generated.NF662.Row{i:02d}" for i in range(N)],
          "\n".join(complete))
    manifest = {
        "schema": "NF662-original-physical-real-compact-attachment-v1",
        "source_indices": INDICES,
        "physical_source_entry_theorems": N*N,
        "lower_triangular_original_NF658_inputs": N*(N+1)//2,
        "upper_triangular_from_symmetry": N*(N-1)//2,
        "scope": "generated proof candidates; kernel acceptance pending",
        "files": files,
    }
    (out/"manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")
    print("NF662 generated all 225 original physical real compact entry proofs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    produce(parser.parse_args().output)
