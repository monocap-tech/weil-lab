#!/usr/bin/env python3
"""CP007 complete original upstream zero-store dyadic-band REAL-DATA audit.

Consumes all 1,748,002 source-store interval rows, verifies original Git blob
SHAs and both store manifests, then evaluates CP006's exact-Fraction upper
localization error. Byte-identical published candidate rows are not proof that
an exported file has been linked to each Lean kernel certificate; this
receipt must never say LEAN PASS or spectral compatibility established.
"""
import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

from cp006_dyadic_zero_bracket_budget import dyadic_band, budget_report
from cp007_original_first52_precision_obstruction import (
    SOURCE_ROWS, SOURCE_BLOB, parse_original52, assess,
)

PIN = Path(__file__).with_name("cp007_upstream_store_source_manifest.json")


def gitblob_sha_of_path(path):
    size=path.stat().st_size
    hashobj=hashlib.sha1(b"blob "+str(size).encode()+b"\0")
    with path.open("rb") as stream:
        for block in iter(lambda:stream.read(1024*1024),b""):
            hashobj.update(block)
    return hashobj.hexdigest()


def verify_blob(path,sha):
    got=gitblob_sha_of_path(path)
    if got!=sha:
        raise ValueError(f"Refusing original-store SHA drift for {path}: {got} != {sha}")


def load_manifest(root,external,expected_columns,expected_rows,sha):
    f=root/external
    verify_blob(f,sha)
    j=json.loads(f.read_text(encoding="utf-8"))
    if j.get("rows")!=expected_rows or j.get("cols")!=expected_columns:
        raise ValueError(f"Source store declared row count or column schema mismatch: {external}")
    return j


def iter_rows(path,cols,start_index):
    with path.open("r",encoding="ascii") as reader:
        for index,line in enumerate(reader,start_index):
            fields=[x.strip() for x in line.strip().split(",")]
            if len(fields)!=len(cols) or int(fields[0])!=index:
                raise ValueError(f"Exact original store row index/column mismatch at {path}:{index}")
            try:
                left,right=F(fields[1]),F(fields[2])
            except Exception as e:
                raise ValueError(f"Non-rational source store entry at {path}:{index}") from e
            if not 0<left<right:
                raise ValueError(f"Not a positive interval at {path}:{index}")
            if any(not z.isdigit() for z in fields[3:]):
                raise ValueError(f"Method-specific cert source data invalid at {path}:{index}")
            yield left,right


def source_audit(root,output):
    pin=json.loads(PIN.read_text(encoding="utf-8"))
    assert pin["pinned_commit"]=="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
    em=pin["euler_maclaurin"]
    rs=pin["riemann_siegel"]
    jm=load_manifest(root,em["manifest_path"],em["columns"],em["rows"],em["manifest_git_sha"])
    jr=load_manifest(root,rs["manifest_path"],rs["columns"],rs["rows"],rs["manifest_git_sha"])
    original_lean_batch=root/em["compiler_batch_path"]
    verify_blob(original_lean_batch,em["compiler_batch_git_sha"])
    if em["compiler_batch_statement"] not in original_lean_batch.read_text(encoding="utf-8"):
        raise ValueError("True generated Lean original first-52 batch statement not found")

    if len(jm.get("files",[]))!=1 or jm["files"][0]["file"]!="zeros_00001.txt":
        raise ValueError("Unexpected original Euler Maclaurin source store layout")
    if len(jr.get("files",[]))!=7:
        raise ValueError("Expected seven actual original Riemann Siegel store shards")

    bands=defaultdict(lambda:F(0))
    previous=None
    total=0
    report=[]
    sources=[("euler_maclaurin",em,[(jm["files"][0]["file"],em["store_git_sha"],52,em["last_right"])],jm),
             ("riemann_siegel",rs,rs["files"],jr)]
    for method,info,files,external_manifest in sources:
        local_index=1
        method_total=0
        for idx,(name,sha,expected_count,final_height) in enumerate(files):
            actual_manifest_file=external_manifest["files"][idx]
            if not (actual_manifest_file["file"]==name
                    and actual_manifest_file["rows"]==expected_count
                    and F(str(actual_manifest_file["height"]))==F(str(final_height))):
                raise ValueError(f"Manifest per-file expected row count or height mismatch: {name}")
            path=root/"python"/"out"/method/"zeros"/name
            verify_blob(path,sha)
            count=0
            for left,right in iter_rows(path,info["columns"],local_index):
                if previous is not None and left<previous:
                    raise ValueError(f"Overlapping original zero source intervals at {name}:{local_index+count}")
                previous=right
                bands[dyadic_band(left)]+=(right-left)/2
                count+=1
            if count!=expected_count:
                raise ValueError(f"Actual number of source rows doesn't match manifest: {name}")
            if previous!=F(str(final_height)):
                raise ValueError(f"True last zero interval endpoint incorrect in {name}")
            report.append({"source":method,"file":name,"git_blob_sha":sha,
                           "rows":count,"last_right":str(previous)})
            local_index+=count
            method_total+=count
            total+=count
        if method_total!=info["rows"]:
            raise ValueError(f"Method total source count mismatch: {method}")
    if total!=pin["total"] or total!=1_748_002:
        raise ValueError("Source full count mismatches upstream Lean proof count")
    bounds=budget_report(dict(bands))
    status="SOURCE_DATA_ERROR_BUDGET_EXCEEDED" if not all(x["within_budget"] for x in bounds.values()) else "SOURCE_DATA_BUDGET_BELOW_THRESHOLD"
    receipt={
       "status":status,
       "trust":"Source SHA matches only; real Lean/olean-to-each-zero proof lineage and original full Weil dictionary are OPEN",
       "pinned_commit":pin["pinned_commit"],
       "total_rows":total,
       "individual_source_files":report,
       "dyadic_bins":{str(j):str(v) for j,v in sorted(bands.items())},
       "original_cp006_bound_by_radius":bounds,
    }
    output.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(status)
    print(f"Exact source verified 8 bracket files / {total} rows; {len(bands)} rational dyadic bins")
    for radius,values in bounds.items():
        print(f"r={radius}: normalized CP006 bound ~{float(F(values['total_conditional_upper'])):.9f}, "
              f"threshold=0.002, within={values['within_budget']}")
    print("This measures adequacy of RAW widened source brackets; does NOT falsify actual Weil spectral compatibility.")


def self_test():
    arr=parse_original52()
    stats=assess(arr)
    assert len(arr)==52
    assert all(x["first_bracket_exceeds_total_target"] for x in stats.values())
    pin=json.loads(PIN.read_text(encoding="utf-8"))
    assert sum(x[2] for x in pin["riemann_siegel"]["files"])==1_747_950
    assert pin["total"]==pin["euler_maclaurin"]["rows"]+pin["riemann_siegel"]["rows"]
    print("CP007 SHA-pinned source manifest and real first-52 exact rational negative control: PASS")
    print("All 1,748,002 data rows not yet read in this self-test.")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--self-test",action="store_true")
    parser.add_argument("--upstream-source-root",type=Path)
    parser.add_argument("--out",type=Path,default=Path("cp007-original-full-store-interval-error-report.json"))
    args=parser.parse_args()
    if args.self_test:
        self_test()
    if args.upstream_source_root:
        try:
            source_audit(args.upstream_source_root,args.out)
        except (OSError,UnicodeError,ValueError,KeyError,IndexError,AssertionError) as e:
            print("NOT_READY: ORIGINAL PINNED SOURCE CHECK FAILED:",e)
            raise SystemExit(2)
    if not args.self_test and not args.upstream_source_root:
        parser.print_help()


if __name__=="__main__":
    main()
