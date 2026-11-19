#!/usr/bin/env python3
"""NF694: source-exact bounded original H/V row certificates (not bank attachment)."""
import argparse
import gzip
import hashlib
import json
import zipfile
from fractions import Fraction as F
from pathlib import Path

from emit_nf675_original_literal_first_row import get_631, rat, vec, PINNED_NF631, N, Q
from emit_nf627_original_moment_bank import emit_bank, filetext
from emit_nf629_original_entry_row_pilot import required_keys
from verify_nf622_physical_entry_reassembly import selected, critical, read_shards, entry

def emit(root, shards, archive, coverage, output, i):
    assert 1 <= i <= 3
    _, _, eH, eV, head, summary = get_631(archive)
    with zipfile.ZipFile(archive) as z:
        names = [n for n in z.namelist() if Path(n).name == "nf631-widened-entries.jsonl.gz"]
        assert len(names) == 1
        data = [json.loads(line) for line in gzip.decompress(z.read(names[0])).splitlines()][1:]
    h = [int(data[max(i,j)]["H_lower"][min(i,j)][0]) for j in range(N)]
    v = [int(x[0]) for x in data[i]["V"]]
    S,C = selected(root),critical(root)
    assert len(S)==N and len(C)==4
    original = read_shards(root,shards)
    assert len(original)==7835 and sum(map(len,original.values()))==37994
    hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in shards.rglob("nf621-shard*.json.gz")}
    assert len(hashes)==8 and hashes=={s["file"]:s["sha256"] for s in json.loads(coverage.read_text())["shards"]}
    need=required_keys(S[i],[*S[:i+1],*C])
    subset={k:original[k][:d+1] for k,d in need.items()}
    assert all(len(subset[k])==d+1 for k,d in need.items())
    for j in range(i+1):
        mid,rad=entry(subset,S[i],S[j])
        assert abs(mid-h[j])+rad<=eH,("H",i,j)
    for j in range(4):
        mid,rad=entry(subset,S[i],C[j])
        assert abs(mid-v[j])+rad<=eV,("V",i,j)
    m=emit_bank(subset,output,16,hashes)
    for p in output.glob("*.lean"):
        p.write_text(p.read_text().replace("WeilDefect.Generated.NF627.","WeilDefect.Generated.NF694."))
    for rec in m["files"]:
        p=output/rec["file"]
        rec["bytes"]=p.stat().st_size
        rec["sha256"]=hashlib.sha256(p.read_bytes()).hexdigest()
    (output/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    body="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
    body+=vec("nf694HCenters",h)+vec("nf694VCenters",v)
    body+=f"""def nf694Payment : NF625PaymentData :=
  ⟨fun _ _ => 0,
   fun a b => if a.val = {i} then nf694HCenters[b.val]!
              else if b.val = {i} then nf694HCenters[a.val]!
              else 0,
   fun a b => if a.val = {i} then nf694VCenters[b.val]! else 0,
   fun _ => 0, {rat(F(eH,Q))}, {rat(F(eV,Q))}, 0⟩

def nf694Moments : NF622Moments :=
  neutralNF624Lookup nf627Bank (neutralNF624Index nf627Bank)

theorem nf694OriginalRow{i} : neutralNF674OriginalRowCheck
    nf694Moments nf694Payment ({i} : Fin 242) = true := by
  decide +kernel

#print axioms nf694OriginalRow{i}
"""
    (output/"RowGate.lean").write_text(filetext([
        "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalExecutableEntryChecks",
        "WeilDefect.Generated.NF694.Bank"],body))
    info={"schema":"NF694-original-local-row-v1","row":i,"H":i+1,"V":4,"symmetry":N,
          "original_archive":PINNED_NF631,"original_widened_digest":summary["widened_entry_sha256"],
          "source_hashes":hashes,"keys":m["keys"],"rows":m["rows"],
          "physical_eH":str(F(eH,Q)),"physical_eV":str(F(eV,Q)),
          "files":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in output.glob("*.lean")},
          "scope":"Exact external reassembly and local Lean candidates only; full original moment and payment projection attachment remains separate."}
    (output/"row-manifest.json").write_text(json.dumps(info,indent=2)+"\n")
    print("NF694 exact external row preflight PASS",i,"H",i+1,"V",4,"keys",m["keys"])

if __name__=="__main__":
    p=argparse.ArgumentParser()
    for arg in ("root","shards","archive","coverage","output"):
        p.add_argument("--"+arg,required=True,type=Path)
    p.add_argument("--row",required=True,type=int)
    a=p.parse_args()
    emit(a.root,a.shards,a.archive,a.coverage,a.output,a.row)
