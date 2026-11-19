#!/usr/bin/env python3
"""Emit original-frame mass / Dy checks tied to the NF677 scalar literals.

H,V are deliberately absent: the projected input retains exactly D,y,w
and the original scalar parameters. Full-cache attachment still requires
the exact original D,y,w projection equality and remaining A/b/Ay gates.
"""
import argparse,hashlib,json,re,sys
from pathlib import Path
from fractions import Fraction as F
from emit_nf630_original_literal_payments import historical,array,filetext,sha
from verify_nf623_uniform_physical_payments import N,Q
sys.set_int_max_str_digits(0)
MODULE="WeilDefect.Generated.NF678"
CORE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMassProjection"
SCALAR="WeilDefect.Generated.NF639"
OPTIONS="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def emit(a):
    d,S,y,U,w,T,mid,rad,frame=historical(a.root,a.historical)
    assert N==242
    p=a.scalar
    manifest=json.loads((p/"manifest.json").read_text())
    assert hashlib.sha256((p/"manifest.json").read_bytes()).hexdigest()=="efcb46ca6eabeae80d0beb21f8627773d23b71002c26fed82f68f47e56bbf896"
    assert sha(a.historical)==manifest["historical_sha256"]
    for rec in manifest["files"]:
        if rec["file"]!="Params.lean":
            assert sha(p/rec["file"])==rec["sha256"]
    params=(p/"Params.lean").read_text()
    scales={k:int(v) for k,v in re.findall(r"def nf639([SQTU]) : ℕ := (\d+)",params)}
    assert scales==dict(S=S,Q=Q,T=T,U=U)
    cols=[sum(abs(d[k][i]) for k in range(N)) for i in range(N)]
    rows=[sum(map(abs,row)) for row in d]
    total=sum(cols); wm=sum(map(abs,w)); ym=sum(abs(v)*c for v,c in zip(y,cols))
    dy=[sum(x*z for x,z in zip(row,y)) for row in d]
    for i in range(N):
        vals=list(map(int,re.findall(r"\((-?\d+):ℤ\)",(p/f"Row{i:03d}.lean").read_text())))
        assert len(vals)==9
        de,co,to,wm0,ym0,ma,b,ay,dy0=vals
        assert (co,to,wm0,ym0,ma,dy0)==(cols[i],total,wm,ym,rows[i],dy[i]),i
    a.output.mkdir(parents=True,exist_ok=True)
    files=[]
    def write(name,imports,body):
        f=a.output/(name+".lean")
        f.write_text(filetext(imports,OPTIONS+body))
        files.append(dict(file=f.name,sha256=sha(f)))
    blocks=[]
    for start in range(0,N,4):
        name=f"Frame{start:03d}"
        blocks.append(MODULE+"."+name)
        body=""
        for i in range(start,min(N,start+4)):
            body+=f"def nf678D{i:03d} : Array ℤ := {array(d[i])}\n\n"
        write(name,["Mathlib"],body)
    body="def nf678D : Array (Array ℤ) := #["+", ".join(f"nf678D{i:03d}" for i in range(N))+"]\n\n"
    for name,values in [("Y",y),("W",w),("Cols",cols)]:
        body+=f"def nf678{name} : Array ℤ := {array(values)}\n\n"
    body+="""def nf678OriginalFrame : NF626ScaledInputs :=
  ⟨fun i j => (nf678D[i.val]!)[j.val]!,
   fun _ _ => 0, fun _ _ => 0,
   fun i => nf678Y[i.val]!, fun j => nf678W[j.val]!,
   nf639S, nf639Q, nf639U, nf639T, nf639EH, nf639EV, nf639R⟩

def nf678ProposedCols (i : Fin 242) : ℤ := nf678Cols[i.val]!
"""
    write("Data",[CORE,SCALAR+".Params",*blocks],body)
    body=f"""theorem nf678TotalLiteral :
    ({total}:ℤ) = ∑ j, nf678ProposedCols j := by
  decide +kernel

theorem nf678YMassLiteral :
    ({ym}:ℤ) = neutralNF626Dot (fun j => |nf678OriginalFrame.y j|) nf678ProposedCols := by
  decide +kernel

theorem nf678WMassLiteral :
    ({wm}:ℤ) = nf678OriginalFrame.wMass := by
  decide +kernel

theorem nf678OriginalWGate : nf678OriginalFrame.wCheck = true := by
  decide +kernel

#print axioms nf678TotalLiteral
#print axioms nf678YMassLiteral
#print axioms nf678WMassLiteral
#print axioms nf678OriginalWGate
"""
    write("Totals",[MODULE+".Data"],body)
    for i in range(N):
        v=f"nf639Row{i:03d}"
        z=f"nf678Row{i:03d}"
        body=f"""/-- Six exact scalar identities for source {i}. -/
theorem {z}Col : nf678ProposedCols ({i}:Fin 242) =
    nf678OriginalFrame.col ({i}:Fin 242) := by
  decide +kernel

theorem {z}ColBind : {v}.col = nf678ProposedCols ({i}:Fin 242) := by
  decide +kernel

theorem {z}Mass : {v}.rowMass =
    nf678OriginalFrame.rowMass ({i}:Fin 242) := by
  decide +kernel

theorem {z}Dy : {v}.Dy =
    neutralNF626Dot (nf678OriginalFrame.D ({i}:Fin 242)) nf678OriginalFrame.y := by
  decide +kernel

theorem {z}Shared : {v}.total = ({total}:ℤ) ∧
    {v}.wMass = ({wm}:ℤ) ∧ {v}.yMass = ({ym}:ℤ) := by
  decide +kernel

#print axioms {z}Col
#print axioms {z}ColBind
#print axioms {z}Mass
#print axioms {z}Dy
#print axioms {z}Shared
"""
        write(f"Mass{i:03d}",[MODULE+".Data",SCALAR+f".Row{i:03d}"],body)
    body="theorem nf678AllOriginalColumns : ∀ i : Fin 242, nf678ProposedCols i = nf678OriginalFrame.col i := by\n  intro i\n  fin_cases i\n"
    for i in range(N):
        body+=f"  · exact nf678Row{i:03d}Col\n"
    body+=f"""
theorem nf678GlobalMasses :
    ({total}:ℤ) = nf678OriginalFrame.total ∧
    ({ym}:ℤ) = nf678OriginalFrame.yMass :=
  neutralNF678Totals_of_columns nf678OriginalFrame nf678ProposedCols
    nf678AllOriginalColumns ({total}:ℤ) ({ym}:ℤ)
    nf678TotalLiteral nf678YMassLiteral

#print axioms nf678AllOriginalColumns
#print axioms nf678GlobalMasses
"""
    write("AllColumns",[MODULE+".Totals",*[MODULE+f".Mass{i:03d}" for i in range(N)]],body)
    (a.output/"manifest.json").write_text(json.dumps(dict(schema="NF678-original-frame-mass-proposals-v1",historical_sha256=sha(a.historical),scalar_manifest_sha256=sha(p/"manifest.json"),frame_sha256=frame,rows=N,exact_external_mass_and_Dy_rows=N,files=files,scope="Projected original frame D,y,w and scalar numerator checks; H,V,HD,A,b,Ay and complete cache validity not certified."),indent=2)+"\n")
    print("NF678 external all 242 original D row/column mass and Dy identities replayed; literal Lean proposals emitted.")
def main():
    p=argparse.ArgumentParser()
    for key in ("root","historical","scalar","output"):
        p.add_argument("--"+key,type=Path,required=True)
    emit(p.parse_args())
if __name__=="__main__":main()
