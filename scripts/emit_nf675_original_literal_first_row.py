#!/usr/bin/env python3
"""Emit a REAL original NF631-pinned H[0,0]+V[0,*] Lean Boolean trial.

The bank is a SOURCE-EXACT subset of the original eight NF621 moment
shards. The row 0 reference centers and GLOBAL physical eH/eV
allowances come from the SHA-pinned original NF631 widened archive.
The emitted Lean decide +kernel statement must pass independently:
generation never asserts a proof or admits an arbitrary widened radius.

The payment is explicitly only a row-0 projection; a separate Lean
projection theorem states exactly what is needed to transfer its
Boolean result to complete original NF626 payment data.
"""
import argparse
import gzip
import hashlib
import json
import sys
import zipfile
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
PINNED_NF631="e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9"
N=242
Q=10**2600

from emit_nf627_original_moment_bank import emit_bank,filetext
from emit_nf629_original_entry_row_pilot import required_keys
from verify_nf622_physical_entry_reassembly import selected, critical, read_shards

def get_631(archive):
    b=archive.read_bytes()
    assert hashlib.sha256(b).hexdigest()==PINNED_NF631, "untrusted original NF631 archive"
    with zipfile.ZipFile(archive) as z:
        def read(base):
            names=[n for n in z.namelist() if Path(n).name==base]
            assert len(names)==1,(base,names)
            return z.read(names[0])
        raw=read("nf631-widened-entries.jsonl.gz")
        summary=json.loads(read("nf631-widening.json"))
    assert hashlib.sha256(raw).hexdigest()==summary["widened_entry_sha256"]
    rows=[json.loads(line) for line in gzip.decompress(raw).splitlines()]
    assert len(rows)==N+1
    head,*data=rows
    assert head["schema"]=="NF622-original-physical-entry-balls-v1"
    assert head["scale"]=="10^2600"
    assert [r["row"] for r in data]==list(range(N))
    assert all(len(r["H_lower"])==i+1 and len(r["V"])==4
               for i,r in enumerate(data))
    eH=eV=0
    h0=[0]*N
    for i,row in enumerate(data):
        for j,(mid,rad) in enumerate(row["H_lower"]):
            mid,rad=int(mid),int(rad)
            assert rad>=0
            eH=max(eH,rad)
            if j==0:
                h0[i]=mid
        for mid,rad in row["V"]:
            assert int(rad)>=0
            eV=max(eV,int(rad))
    v0=[int(x[0]) for x in data[0]["V"]]
    assert summary["H_entries"]==N*(N+1)//2
    assert summary["V_entries"]==4*N
    return h0,v0,eH,eV,head,summary

def rat(x):
    x=F(x)
    return f"({x.numerator}:ℚ)/{x.denominator}"

def vec(name,xs):
    return f"def {name} : Array ℚ := #[\n  "+",\n  ".join(f"({v}:ℚ)/(neutralNF616Q:ℚ)" for v in xs)+"\n]\n\n"

def emit(root,shards,archive,output):
    h0,v0,eH,eV,head,summary=get_631(archive)
    original=read_shards(root,shards)
    S,C=selected(root),critical(root)
    assert len(S)==N and len(C)==4
    need=required_keys(S[0],[S[0],*C])
    subset={k:original[k][:degree+1] for k,degree in need.items()}
    assert all(len(subset[k])==degree+1 for k,degree in need.items())
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
            for p in shards.rglob("nf621-shard*.json.gz")}
    assert len(hashes)==8
    m=emit_bank(subset,output,32,hashes)
    # NF627's emitter writes imports under its original module prefix.
    # The row pilot is intentionally isolated in NF675; rewrite module
    # paths only, never the original rational row literals.
    for p in output.glob("*.lean"):
        p.write_text(p.read_text().replace(
            "WeilDefect.Generated.NF627.", "WeilDefect.Generated.NF675."))
    for rec in m["files"]:
        p=output/rec["file"]
        rec["bytes"]=p.stat().st_size
        rec["sha256"]=hashlib.sha256(p.read_bytes()).hexdigest()
    (output/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    body="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
    body+=vec("nf675PhysicalH0Centers",h0)
    body+=vec("nf675PhysicalV0Centers",v0)
    body+=f"""def nf675OriginalRow0Payment : NF625PaymentData :=
  ⟨fun _ _ => 0,
   fun i j => if i.val = 0 then nf675PhysicalH0Centers[j.val]!
              else if j.val = 0 then nf675PhysicalH0Centers[i.val]!
              else 0,
   fun i j => if i.val = 0 then nf675PhysicalV0Centers[j.val]!
              else 0,
   fun _ => 0,
   {rat(F(eH,Q))},
   {rat(F(eV,Q))},
   0⟩

def nf675OriginalRow0Moments : NF622Moments :=
  neutralNF624Lookup nf627Bank (neutralNF624Index nf627Bank)

/-- Original H[0,0] and V[0,0..3], under *actual full physical*
NF631-referenced eH/eV and genuine NF621 source moment bank.
No result is claimed by the source generator. -/
theorem nf675OriginalRow0_actualEntryCheck :
    neutralNF674OriginalRowCheck nf675OriginalRow0Moments
      nf675OriginalRow0Payment (0 : Fin 242) = true := by
  decide +kernel

#print axioms nf675OriginalRow0_actualEntryCheck
"""
    (output/"OriginalRow0Gate.lean").write_text(filetext([
        "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLiteralRowProjection",
        "WeilDefect.Generated.NF675.Bank",
    ],body))
    info={
      "schema":"NF675-source-exact-original-row-0-candidate-v1",
      "archive_sha256":PINNED_NF631,
      "source_original_entry_sha256":head.get("original_entry_sha256"),
      "original_nf631_widened_digest":summary["widened_entry_sha256"],
      "nf621_source_hashes":hashes,
      "original_source_count":N,
      "original_covered_source_index":0,
      "genuine_H_widening_checks":1,
      "genuine_V_widening_checks":4,
      "exact_center_symmetry_comparisons":N,
      "physical_eH":str(F(eH,Q)),
      "physical_eV":str(F(eV,Q)),
      "partial_bank_keys":m["keys"],
      "partial_bank_rows":m["rows"],
      "files":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in output.glob("*.lean")},
      "scope":"actual source-data gate proposal: Lean kernel PASS needed; partial bank is NOT a complete original global moment proof",
    }
    (output/"row0-manifest.json").write_text(json.dumps(info,indent=2)+"\n")
    return info

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--root",type=Path,required=True)
    p.add_argument("--shards",type=Path,required=True)
    p.add_argument("--archive",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    info=emit(a.root,a.shards,a.archive,a.output)
    print("NF675 prepared ACTUAL original row 0 H and V Boolean Lean check;",
          info["partial_bank_keys"],"source moment keys;",
          "Lean certificate not yet accepted")

if __name__=="__main__":
    main()
