#!/usr/bin/env python3
"""Reuse the exact NF684 endpoint leaves for every other compatible NF621 key.

No additional Taylor chain is generated. The five prerequisite local
tables are not imported as proofs. Each new table checks its own four
exact parameter bindings and its original residual gate.
"""
import argparse,gzip,json,sys
from pathlib import Path
from fractions import Fraction as F
from emit_nf684_second_oscillator_moments import CASES,sha,validate
from emit_nf627_original_moment_bank import filetext,qlit,keylit,rowlit
from verify_nf620_physical_key_tables import reduced,table
from verify_nf622_physical_entry_reassembly import read_shards
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF685"
LEAF="WeilDefect.Generated.NF684"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
def main():
    p=argparse.ArgumentParser()
    for k in ("root","shards","bank","pi","leaves","output"):
        p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args()
    a.output.mkdir(parents=True,exist_ok=True)
    bm,pm,lm=validate(a.bank),validate(a.pi),validate(a.leaves)
    hashes={q.name:sha(q) for q in a.shards.rglob("nf621-shard*.json.gz")}
    assert len(hashes)==8 and hashes==bm["input_sha256"]==lm["input_sha256"]
    assert lm["pi_manifest_sha256"]==sha(a.pi/"manifest.json")
    assert lm["bank_manifest_sha256"]==sha(a.bank/"manifest.json")
    assert lm["schema"]=="NF684-second-oscillator-local-moment-proposals-v1"
    assert (lm["rows"],lm["leaf_count"],lm["prefix_checks"])==(79,11,418)
    rows=read_shards(a.root,a.shards)
    assert len(rows)==7835 and sum(map(len,rows.values()))==37994
    with gzip.open(a.bank/"endpoints.json.gz","rt") as f: b=json.load(f)
    assert b["schema"]=="NF635-original-shared-endpoints-v1" and b["scale"]=="10^2600"
    R,P=({F(q):i for i,(q,v) in enumerate(b[k])} for k in ("real","phase"))
    old={k for _,k,_ in CASES}
    real={s*h for h,f in old for s in (-1,1)}
    phase={reduced(s*f) for h,f in old for s in (-1,1)}
    assert len(real)==3 and len(phase)==8
    family=sorted({abs(q) for q in phase})
    assert len(family)==4
    accepted=dict((r["file"],r["sha256"]) for r in lm["files"])
    def leaf(kind,q):
        i=(R if kind=="Real" else P)[q]
        name=f"{kind}{i:04d}"
        assert name+".lean" in accepted and sha(a.leaves/(name+".lean"))==accepted[name+".lean"]
        return name,"nf684"+name,i
    compatible=[(k,v) for k,v in sorted(rows.items()) if
                k[0] in real and -k[0] in real and
                reduced(k[1]) in phase and reduced(-k[1]) in phase]
    assert len(compatible)==92 and sum(len(v) for k,v in compatible)==601
    targets=[(k,v) for k,v in compatible if k not in old]
    assert len(targets)==87 and sum(len(v) for k,v in targets)==522
    files=[]; records=[]
    for i,(k,data) in enumerate(targets):
        h,f=k
        assert table(h,f,len(data)-1)==data,k
        rr=[(q,leaf("Real",q)) for q in (h,-h)]
        pp=[(reduced(q),leaf("Phase",reduced(q))) for q in (f,-f)]
        label=f"Key{i:03d}"; z="nf685"+label
        def lookup(s,ps):
            out=f"def {z}{s} (q : ℚ) : NF591Rect :=\n"
            for q,l in dict(ps).items(): out+=f"  if q={qlit(q)} then {l[1]}Value else\n"
            return out+"  NF591Rect.zero\n\n"
        body=lookup("R",rr)+lookup("P",pp)
        body+=f"def {z}Table : NF624KeyTable := ⟨{keylit(k)}, #[\n    "+",\n    ".join(map(rowlit,data))+"\n  ]⟩\n\n"
        proofs=[]
        for kind,ps,exprs in [
            ("R",rr,[z+"Table.key.h","(-"+z+"Table.key.h)"]),
            ("P",pp,["neutralNF592Reduced "+z+"Table.key.f",
                    "neutralNF592Reduced (-"+z+"Table.key.f)"])]:
            for j,((q,l),expr) in enumerate(zip(ps,exprs)):
                n=z+kind+str(j); proofs.append(n+"Eq")
                body+=f"theorem {n}Param : {expr}={qlit(q)} := by\n  decide +kernel\n"
                body+=f"theorem {n}Check : neutralNF633RectEq ({z}{kind} {qlit(q)}) {l[1]}Value=true := by\n  decide +kernel\n"
                ref=(f"neutralNF621RealEndpoint ({expr}) neutralNF616Q neutralNF616ExpN" if kind=="R" else
                     f"neutralNF634PhaseReduced nf632Pi ({expr}) neutralNF616Q neutralNF616ExpN")
                body+=f"theorem {n}Eq : {z}{kind} ({expr})={ref} := by\n  rw [{n}Param]\n  exact (neutralNF633RectEq_sound _ _ {n}Check).trans {l[1]}Eq.symm\n\n"
        body+=f"theorem {z}Check : neutralNF634SharedKeyCheck nf632Pi {z}R {z}P {z}Table=true := by\n  decide +kernel\n\n"
        body+=f"""theorem {z}Moment (n : ℕ) (hn : n < {z}Table.rows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) {z}Table.key.value n-
      (neutralNF617MomentRead {z}Table.rows n).value‖ ≤
      (neutralNF617MomentRead {z}Table.rows n).rad :=
  neutralNF648Moment_of_local nf632Pi {z}R {z}P {z}Table nf632PiEq
    {' '.join(proofs)} {z}Check n hn

#print axioms {z}Moment
"""
        imports=sorted({LEAF+"."+l[0] for q,l in rr+pp})
        path=a.output/(label+".lean")
        path.write_text(filetext(imports,OPT+body),encoding="utf8")
        digest=sha(path)
        files.append({"file":path.name,"sha256":digest})
        records.append({"module":label,"key":[str(h),str(f)],"rows":len(data),
                        "family":family.index(abs(reduced(f))),
                        "real":[l[2] for q,l in rr],"phase":[l[2] for q,l in pp],
                        "sha256":digest})
    m={"schema":"NF685-shared-phase-table-proposals-v1",
       "input_sha256":hashes,"leaf_manifest_sha256":sha(a.leaves/"manifest.json"),
       "bank_manifest_sha256":sha(a.bank/"manifest.json"),
       "pi_manifest_sha256":sha(a.pi/"manifest.json"),
       "prior_tables":5,"prior_rows":79,"new_tables":len(records),"new_rows":sum(r["rows"] for r in records),
       "new_endpoint_leaves":0,"new_prefix_transitions":0,
       "families":[{"index":i,"abs_phase":str(q),"tables":sum(r["family"]==i for r in records),"rows":sum(r["rows"] for r in records if r["family"]==i)} for i,q in enumerate(family)],
       "tables":records,"files":files,
       "scope":"Original local analytic table proposals using existing NF684 endpoint sources; no global bank truth; NF684 and NF685 proofs require kernel acceptance."}
    (a.output/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    print("NF685 external reconstruction: 87 additional tables / 522 rows; no additional Taylor chains;",m["families"],flush=True)
if __name__=="__main__": main()
