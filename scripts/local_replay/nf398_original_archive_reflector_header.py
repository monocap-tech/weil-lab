#!/usr/bin/env python3
"""NF398 authenticated original archived Householder COUNT/shape preflight.

Checks real historical ZIP SHA and original WJJ JSON SHA; never infers
the number of stored reflectors from ambient selected rank. No Weil sign,
signed selected moment or candidate acceptance is asserted.
"""
import argparse,hashlib,json,zipfile
from pathlib import Path
ZIP_SHA="f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0"
M_SHA="33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa"
N=242

def main(zip_path,out_path):
    raw=Path(zip_path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==ZIP_SHA
    with zipfile.ZipFile(zip_path) as archive:
        matrix_raw=archive.read("original_selected_signed_matrix.json")
    assert hashlib.sha256(matrix_raw).hexdigest()==M_SHA
    j=json.loads(matrix_raw)
    assert j["selected_rank"]==N
    rows=j["householder_vectors"]
    count=len(rows)
    assert 0<count<=N
    for k,r in enumerate(rows):
        assert r["start"]==k,("invalid original reflector start",k,r.get("start"))
        assert len(r["vector"])==N-k,("invalid original reflected suffix",k)
    assert len(j["finite_transformed_signed_matrix_upper_native"])==N
    record={
      "pass":"NF398",
      "status":"AUTHENTIC ORIGINAL REFLECTOR HEADER VERIFIED; NATIVE SIGNED RESULT STILL OPEN",
      "original_signed_archive_sha256":ZIP_SHA,
      "original_signed_matrix_sha256":M_SHA,
      "selected_rank":N,
      "actual_archived_householder_reflector_count":count,
      "all_archived_reflector_starts_and_suffix_shapes_checked":True,
      "missing_trailing_reflectors_treated_as_identity":N-count,
      "old_nf397_count_equals_242_assumption_was_valid":count==N,
      "actual_original_signed_scalar_computed":False,
      "j387":"UNDECIDED","W_ODD_NEG":"OPEN","RH":"OPEN"
    }
    if out_path:
        out=Path(out_path);out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(record,indent=2)+"\n")
    print("NF398 authentic archive reflector count:",count,"in ambient",N)
    print("NF398 full source authentic; native original signed scalar still OPEN")
    return record

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--archive",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    main(a.archive,a.output)
