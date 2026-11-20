#!/usr/bin/env python3
"""NF727: authenticate *accepted* NF726 original two-half finite cover witnesses.

The NF726 full master build failed, but BOTH individual half jobs succeeded.
This check only licenses the separately accepted half theorems. Its JSON must
not describe the failed NF726 full master or original numerical row as proven.
"""
import hashlib
import json
from pathlib import Path

RECEIPTS=Path("nf727-accepted-nf726")
SOURCE=Path("WeilDefect/Arithmetic")
EXPECTED={
    0:("nf726-source-bound-half-000","nf726-half-000.json",
       "ActualZetaOriginalPhysicalPackedFinHalf000.olean"),
    16:("nf726-source-bound-half-016","nf726-half-016.json",
        "ActualZetaOriginalPhysicalPackedFinHalf016.olean"),
}
ALLOWED={"propext","Classical.choice","Quot.sound"}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def unique(root,name):
    files=list(root.rglob(name))
    assert len(files)==1,(root,name,files)
    return files[0]


def main():
    seen=[]
    for i,(folder,mname,oname) in EXPECTED.items():
        root=RECEIPTS/folder
        path=unique(root,mname)
        m=json.loads(path.read_text())
        assert m["schema"]=="NF726-source-bound-pinned-half-olean-v1"
        assert m["half_block"]==i
        assert m["first_coordinate"]==i*8
        assert m["end_coordinate"]==min((i+16)*8,242)
        assert m["theorem"]==f"neutralNF726Half{i:03d}"
        assert set(m["axioms"]) <= ALLOWED
        assert m["source_type"]=="Fin 242 pure arithmetic"
        assert m["numerical_products_asserted"] is False
        source=SOURCE/f"ActualZetaOriginalPhysicalPackedFinHalf{i:03d}.lean"
        assert m["source_sha256"]==digest(source)
        obj=unique(root,oname)
        assert obj.stat().st_size>1024
        assert m["olean_sha256"]==digest(obj)
        old=m["accepted_original_four_chunk_fingerprints"]
        assert [x["block_start"] for x in old]==[0,8,16,24]
        assert len({x["source_sha256"] for x in old})==4
        for x in old:
            src=SOURCE/f"ActualZetaOriginalPhysicalPackedFinChunk{x['block_start']:03d}.lean"
            assert x["source_sha256"]==digest(src)
        seen.append({
            "half":i,
            "source_sha256":m["source_sha256"],
            "olean_sha256":m["olean_sha256"],
            "audit_sha256":digest(path),
            "compiler":m["compiler"],
            "four_accepted_original_chunks":old,
            "prior_four_chunk_reconstruction_sha256":
                m["accepted_original_four_chunk_receipt_sha256"],
            "theorem":m["theorem"],
        })
    assert len(seen)==2 and seen[0]["half"]==0 and seen[1]["half"]==16
    assert seen[0]["four_accepted_original_chunks"]==seen[1]["four_accepted_original_chunks"]
    assert seen[0]["compiler"]==seen[1]["compiler"]
    assert (seen[0]["prior_four_chunk_reconstruction_sha256"]==
            seen[1]["prior_four_chunk_reconstruction_sha256"])
    result={
       "schema":"NF727-two-accepted-NF726-finite-halves-source-custody-v1",
       "upstream_run_id":44699835930,
       "upstream_accepted_jobs":[136165238061,136165238542],
       "upstream_accepted_artifact_ids":[14613196175,14613037846],
       "source_bound_halves":seen,
       "complete_fin242_master_kernel_accepted":False,
       "full_original_numeric_HD_A_row_kernel_accepted":False,
       "scope":"Both NF726 original-position bounded half theorems accepted and .olean source-bound. Neither the failed full original Fin master nor actual global numerical row universal theorem is accepted."
    }
    Path("nf727-half-provenance.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("NF727 prior NF726 left and right original Fin242 half source, axiom, compiled SHA, compiler and original 4-chunk receipts VALID; global numerical universal proof not yet accepted")


if __name__=="__main__":
    main()
