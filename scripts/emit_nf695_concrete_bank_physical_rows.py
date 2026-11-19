#!/usr/bin/env python3
"""NF695 original bank H/V entry checks with exact NF631 row projections."""
import argparse
import gzip
import hashlib
import json
import zipfile
from fractions import Fraction as F
from pathlib import Path

from emit_nf675_original_literal_first_row import get_631, rat, vec, PINNED_NF631, N, Q
from emit_nf627_original_moment_bank import filetext

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def emit(archive, output):
    _, _, eh, ev, head, summary = get_631(archive)
    with zipfile.ZipFile(archive) as z:
        names = [n for n in z.namelist() if Path(n).name == "nf631-widened-entries.jsonl.gz"]
        assert len(names) == 1
        data = [json.loads(line) for line in gzip.decompress(z.read(names[0])).splitlines()][1:]
    output.mkdir(parents=True,exist_ok=True)
    records=[]
    for i in range(8):
        stem=f"nf695Row{i:03d}"
        h=[int(data[max(i,j)]["H_lower"][min(i,j)][0]) for j in range(N)]
        v=[int(x[0]) for x in data[i]["V"]]
        body="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
        body+=vec(stem+"H",h)+vec(stem+"V",v)
        body+=f"""def {stem}Payment : NF625PaymentData :=
  ⟨fun _ _ => 0,
   fun a b => if a.val = {i} then {stem}H[b.val]!
              else if b.val = {i} then {stem}H[a.val]!
              else 0,
   fun a b => if a.val = {i} then {stem}V[b.val]! else 0,
   fun _ => 0, {rat(F(eh,Q))}, {rat(F(ev,Q))}, 0⟩

theorem {stem}Fast : neutralNF674OriginalRowCheck
    nf691OriginalLookup {stem}Payment ({i} : Fin 242) = true := by
  decide +kernel

theorem {stem}ActualBank : neutralNF674OriginalRowCheck
    (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
    {stem}Payment ({i} : Fin 242) = true := by
  rw [nf691OriginalLookup_eq]
  exact {stem}Fast

theorem {stem}PaymentTransport (p : NF625PaymentData)
    (hrow : ∀ j : Fin 242, {stem}Payment.H0 ({i}:Fin 242) j = p.H0 ({i}:Fin 242) j)
    (hcol : ∀ j : Fin 242, {stem}Payment.H0 j ({i}:Fin 242) = p.H0 j ({i}:Fin 242))
    (hV : ∀ j : Fin 4, {stem}Payment.V0 ({i}:Fin 242) j = p.V0 ({i}:Fin 242) j)
    (heH : {stem}Payment.eH = p.eH) (heV : {stem}Payment.eV = p.eV) :
    neutralNF674OriginalRowCheck
      (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
      p ({i} : Fin 242) = true :=
  neutralNF675OriginalRow_true_of_projection _ _ _ _ hrow hcol hV heH heV
    {stem}ActualBank

#print axioms {stem}Fast
#print axioms {stem}ActualBank
#print axioms {stem}PaymentTransport
"""
        path=output/f"Row{i:03d}.lean"
        path.write_text(filetext(["WeilDefect.Generated.NF691.OriginalLookup",
            "WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLiteralRowProjection"],body))
        records.append({"row":i,"H":i+1,"V":4,"symmetry":N,"file":path.name,"sha256":sha(path),
             "theorems":[stem+s for s in ("Fast","ActualBank","PaymentTransport")]})
    assert sum(r["H"] for r in records)==36 and sum(r["V"] for r in records)==32
    (output/"manifest.json").write_text(json.dumps({
        "schema":"NF695-concrete-bank-original-entry-row-proposals-v1",
        "nf631_archive_sha256":PINNED_NF631,"widened_digest":summary["widened_entry_sha256"],
        "physical_eH":str(F(eh,Q)),"physical_eV":str(F(ev,Q)),
        "rows":records,"scope":"Concrete incumbent bank lookup, projected NF631 payment only; full payment attachment remains conditional."
    },indent=2)+"\n")
    print("NF695 exact source row projection proposals emitted; no Lean acceptance yet")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--archive",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path)
    a=p.parse_args()
    emit(a.archive,a.output)
