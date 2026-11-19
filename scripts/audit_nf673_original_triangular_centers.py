#!/usr/bin/env python3
"""Verify pinned NF631 original 242-source H/V archived CENTER layout.

Only immutable source archive, integer parsing, shape and center symmetry
are checked here. This does NOT prove its analytic moment containments or
the Lean boolean checks. The genuine H symmetry is the NF606 integral theorem.
"""
import argparse
import gzip
import hashlib
import json
import sys
import zipfile
from pathlib import Path

sys.set_int_max_str_digits(0)

PINNED_ARCHIVE = "e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9"
N = 242
V_COLS = 4


def parse_archive(path):
    archive_bytes = path.read_bytes()
    checksum = hashlib.sha256(archive_bytes).hexdigest()
    if checksum != PINNED_ARCHIVE:
        raise ValueError("immutable NF631 source archive SHA256 mismatch")
    with zipfile.ZipFile(path) as zf:
        files = zf.namelist()
        def load(base):
            found = [p for p in files if Path(p).name == base]
            if len(found) != 1:
                raise ValueError(f"expected exactly one {base}, got {found}")
            return zf.read(found[0])
        raw = load("nf631-widened-entries.jsonl.gz")
        summary = json.loads(load("nf631-widening.json"))
    if summary["widened_entry_sha256"] != hashlib.sha256(raw).hexdigest():
        raise ValueError("widened-entry manifest digest mismatch")
    rows = [json.loads(line) for line in gzip.decompress(raw).splitlines()]
    if len(rows) != N + 1:
        raise ValueError("original 242 rows missing or duplicated")
    header, *data = rows
    if header["schema"] != "NF622-original-physical-entry-balls-v1":
        raise ValueError("wrong original physical-entry schema")
    if header["scale"] != "10^2600":
        raise ValueError("unexpected physical moment scale")
    centers = [[0] * N for _ in range(N)]
    count_h = count_v = 0
    max_h = max_v = 0
    for i, row in enumerate(data):
        if row["row"] != i or len(row["H_lower"]) != i + 1:
            raise ValueError(f"lower triangle row {i} mismatch")
        if len(row["V"]) != V_COLS:
            raise ValueError(f"mixed source row {i} mismatch")
        for j, item in enumerate(row["H_lower"]):
            if len(item) != 2:
                raise ValueError(f"bad H ball at {(i,j)}")
            mid, rad = map(int, item)
            if rad < 0:
                raise ValueError("negative H radius")
            centers[i][j] = centers[j][i] = mid
            count_h += 1
            max_h = max(max_h, rad)
        for item in row["V"]:
            if len(item) != 2:
                raise ValueError("bad V ball")
            mid, rad = map(int, item)
            if rad < 0:
                raise ValueError("negative V radius")
            count_v += 1
            max_v = max(max_v, rad)
    if count_h != N * (N + 1) // 2 or count_v != N * V_COLS:
        raise ValueError("missing physical source entries")
    if (summary["H_entries"], summary["V_entries"]) != (count_h, count_v):
        raise ValueError("original NF631 manifest count mismatch")
    if any(centers[i][j] != centers[j][i] for i in range(N) for j in range(N)):
        raise ValueError("original rational H center symmetry mismatch")
    return {
        "schema": "NF673-original-symmetric-center-source-audit-v1",
        "archive_sha256": checksum,
        "original_entry_sha256": header.get("original_entry_sha256"),
        "full_source_rank": N,
        "H_lower_count": count_h,
        "H_upper_recovered_by_symmetry": N * (N - 1) // 2,
        "H_center_symmetry_comparisons": N * N,
        "V_entry_count": count_v,
        "H_max_radius_units": str(max_h),
        "V_max_radius_units": str(max_v),
        "scope": "external serialized-center source custody only; Lean H and V interval-check truth still open",
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--archive", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    report = parse_archive(args.archive)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print("NF673 pinned original physical source layout PASS", report["H_lower_count"],
          "H lower entries,", report["V_entry_count"], "mixed V entries")
    print("This does NOT certify Lean moment-entry or payment gates.")


if __name__ == "__main__":
    main()
