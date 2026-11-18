#!/usr/bin/env python3
"""Check sharded source schedule coverage, without trusting file names or counts.
This is a structural audit, not an independent numerical or Lean audit.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F
from verify_nf620_physical_key_tables import inventory

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--root",type=Path,required=True)
    p.add_argument("--shards",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    keys=inventory(args.root)
    expected={k:n+1 for k,n in keys.items() if k!=(0,0)}
    assert keys[(0,0)]==26
    seen={}
    manifests=[]
    maxrad=0
    for path in sorted(args.shards.rglob("nf621-shard*.json.gz")):
        with gzip.open(path,"rt") as f:
            d=json.load(f)
        assert d["scale"]=="10^2600" and d["exp_terms"]==1200 and d["atan_terms"]==2000
        count=0
        for t in d["tables"]:
            k=F(t["h"]),F(t["f"])
            assert k in expected and k not in seen
            assert len(t["rows"])==expected[k]
            for row in t["rows"]:
                assert len(row)==3
                x,y,r=map(int,row)
                assert r>=0
                maxrad=max(maxrad,r)
            seen[k]=len(t["rows"])
            count+=len(t["rows"])
        manifests.append({"file":path.name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                          "keys":len(d["tables"]),"rows":count})
    assert seen==expected
    assert len(seen)==7835 and sum(seen.values())==37994
    assert maxrad<10**30, "radius screening bound failed"
    out={"status":"source schedule coverage PASS","scale":"10^2600",
         "nonzero_keys":len(seen),"nonzero_rows":sum(seen.values()),"exact_zero_rows":27,
         "maximum_radius_integer":str(maxrad),
         "radius_screen":"all nonzero moment radii < 10^-2570",
         "shards":manifests,"evidence":"structural coverage of external integer replay; not analytic Lean attachment"}
    args.output.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
if __name__=="__main__":
    main()
