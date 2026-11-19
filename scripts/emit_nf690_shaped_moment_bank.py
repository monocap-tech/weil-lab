#!/usr/bin/env python3
"""Build the original numerical bank payload in locally readable literal chunks.
The shape is structural; analytic validity is separate. A genuine NF684 table
is attached in a bounded pilot. No synthetic payload is claimed as the bank.
"""
import argparse,hashlib,json,re,sys
from fractions import Fraction as F
from pathlib import Path
from emit_nf627_original_moment_bank import filetext,rowlit
from verify_nf622_physical_entry_reassembly import read_shards
sys.set_int_max_str_digits(0)
MOD="WeilDefect.Generated.NF690"
CORE="WeilDefect.Arithmetic.ActualZetaOriginalPhysicalShapedBank"
COMPACT="WeilDefect.Generated.NF687.Compact"
OPT="set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n"
WIDTH=16
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(d):
    m=json.loads((d/"manifest.json").read_text())
    for r in m["files"]:
        if d.name=="NF679" and r["file"]!="Metadata.lean":continue
        assert sha(d/r["file"])==r["sha256"]
    return m
def main():
    p=argparse.ArgumentParser()
    for k in ("root","shards","metadata","compact","local","output"):
        p.add_argument("--"+k,type=Path,required=True)
    a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    md,cm,lm=validate(a.metadata),validate(a.compact),validate(a.local)
    assert cm["metadata_sha256"]==sha(a.metadata/"Metadata.lean")
    assert (md["keys"],md["moment_rows"])==(7835,37994)
    hashes={p.name:sha(p) for p in a.shards.rglob("nf621-shard*.json.gz")}
    assert len(hashes)==8 and hashes==md["input_sha256"]==lm["input_sha256"]
    data=read_shards(a.root,a.shards);ordered=sorted(data.items())
    pattern=r"⟨⟨\((-?\d+/\d+):ℚ\),\((-?\d+/\d+):ℚ\)⟩, Array\.replicate (\d+) ⟨0,0,0⟩⟩"
    meta=[((F(h),F(f)),int(n)) for h,f,n in re.findall(pattern,(a.metadata/"Metadata.lean").read_text())]
    assert meta==[(k,len(v)) for k,v in ordered]
    # Verify every compact-block literal matches the original metadata.
    blockpat=r"\(⟨\((-?\d+/\d+):ℚ\),\((-?\d+/\d+):ℚ\)⟩,(\d+)\)"
    compact=[]
    for path in sorted(a.compact.glob("Block*.lean")):
        compact.extend(((F(h),F(f)),int(n)) for h,f,n in re.findall(blockpat,path.read_text()))
    assert meta==compact
    key=(F(0),F(285,128))
    slot=next(i for i,(k,v) in enumerate(ordered) if k==key)
    assert len(data[key])==22
    # The independently reconstructed row literal really is identical to
    # the original previously audited NF684 CrossSum moment source.
    local=(a.local/"CrossSum.lean").read_text()
    literal=",\n    ".join(map(rowlit,data[key]))
    assert literal in local
    files=[];blocks=[];records=[]
    def write(name,imports,body):
        path=a.output/(name+".lean")
        path.write_text(filetext(imports,OPT+body),encoding="utf8")
        files.append({"file":path.name,"sha256":sha(path),"bytes":path.stat().st_size})
    for start in range(0,len(ordered),WIDTH):
        name=f"Chunk{start//WIDTH:03d}";v="nf690"+name;blocks.append(name)
        items=[]
        for i,(k,rows) in enumerate(ordered[start:start+WIDTH],start):
            items.append("#[\n    "+",\n    ".join(map(rowlit,rows))+"\n  ]")
            records.append({"index":i,"key":list(map(str,k)),"rows":len(rows),"chunk":name,"offset":i-start})
        write(name,[CORE],f"def {v} : Array (Array NF617MomentRow) := #[\n  "+",\n  ".join(items)+"\n]")
    body="def nf690Parts : Array (Unit → Array (Array NF617MomentRow)) := #[\n  "+",\n  ".join("fun _ => nf690"+x for x in blocks)+"\n]\n\n"
    body+="""
def nf690Payload (i : ℕ) : Array NF617MomentRow :=
  let p := (nf690Parts[i / 16]?).getD (fun _ => #[])
  ((p ())[i % 16]?).getD #[]

def nf690OriginalBank : Array NF624KeyTable :=
  neutralNF690Bank nf687Read nf687Size nf690Payload

theorem nf690OriginalBank_size : nf690OriginalBank.size=nf687Size :=
  neutralNF690Bank_size nf687Read nf687Size nf690Payload

theorem nf690OriginalBank_shape (i : ℕ) (hi : i<nf687Size) :
    neutralNF627ShapeAt nf690OriginalBank i=nf687Read i :=
  neutralNF690Bank_shape nf687Read nf687Size nf690Payload i hi

theorem nf690OriginalBank_index :
    neutralNF624Index nf690OriginalBank=nf687Index :=
  neutralNF690Bank_index nf687Read nf687Size nf690Payload

#print axioms nf690OriginalBank_size
#print axioms nf690OriginalBank_shape
#print axioms nf690OriginalBank_index
"""
    write("Bank",[COMPACT]+[MOD+"."+x for x in blocks],body)
    write("Coverage",[MOD+".Bank","WeilDefect.Generated.NF687.AllGroups"],"""
theorem nf690OriginalCoverage :
    neutralNF624CoverageCheck nf690OriginalBank (neutralNF624Index nf690OriginalBank)=true :=
  nf687CoverageOnBank nf690OriginalBank nf690OriginalBank_size nf690OriginalBank_shape

#print axioms nf690OriginalCoverage
""")
    block=f"Chunk{slot//WIDTH:03d}"
    body=f"""-- This function is a LOCAL pilot only, not the full bank payload.
def nf690PilotRows (_ : ℕ) : Array NF617MomentRow :=
  (nf690{block}[{slot%WIDTH}]?).getD #[]

theorem nf690CrossSumKey : (nf687Read {slot}).1 = nf684CrossSumTable.key := by
  decide +kernel

theorem nf690CrossSumLength : (nf687Read {slot}).2 = nf684CrossSumTable.rows.size := by
  decide +kernel

theorem nf690CrossSumRows : nf690PilotRows {slot} = nf684CrossSumTable.rows := by
  rfl

theorem nf690CrossSumTableEq :
    neutralNF690Table nf687Read nf690PilotRows {slot} = nf684CrossSumTable :=
  neutralNF690Table_eq nf687Read nf690PilotRows {slot} nf684CrossSumTable
    nf690CrossSumKey nf690CrossSumRows nf690CrossSumLength

theorem nf690CrossSumSound :
    neutralNF690TableSound (neutralNF690Table nf687Read nf690PilotRows {slot}) := by
  rw [nf690CrossSumTableEq]
  exact nf684CrossSumMoment

#print axioms nf690CrossSumKey
#print axioms nf690CrossSumLength
#print axioms nf690CrossSumRows
#print axioms nf690CrossSumTableEq
#print axioms nf690CrossSumSound
"""
    write("Pilot",[COMPACT,MOD+"."+block,"WeilDefect.Generated.NF684.CrossSum"],body)
    m={"schema":"NF690-shaped-original-bank-proposals-v1","keys":len(ordered),"rows":sum(len(v) for k,v in ordered),
       "chunk_width":WIDTH,"chunks":len(blocks),"input_sha256":hashes,
       "metadata_sha256":sha(a.metadata/"Metadata.lean"),"compact_manifest_sha256":sha(a.compact/"manifest.json"),
       "local_manifest_sha256":sha(a.local/"manifest.json"),"pilot_index":slot,"pilot_chunk":block,
       "pilot_key":list(map(str,key)),"pilot_rows":22,"slots":records,"files":files,
       "scope":"Full original numerical payload source proposals; generic structural attachment and single local analytic receipt pilot only. Full Bank/Coverage modules are emitted, not built in this pilot."}
    (a.output/"manifest.json").write_text(json.dumps(m,indent=2)+"\n")
    print("NF690 all 7835 original payload tables / 37994 rows emitted in",len(blocks),"chunks; pilot slot",slot,"; kernel pending",flush=True)
if __name__=="__main__":main()
