#!/usr/bin/env python3
"""CP009 exact rational sufficient *precision policy* for all remaining RS zeros.

Not a zeta root generator, interval arithmetic sign prover, or signed Weil
matrix certificate. CP008's first-52 small intervals remain kernel candidates.
Actual RS data must be SHA-checked and separately kernel-certified as zeros.
"""
import argparse
import hashlib
import itertools
import json
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

from cp005_formal_zero_roster_adapter import (
    H, RADII, CENTERS, E_tail, E_QUAD_ALLOWANCE, EPS_MAX
)
from cp006_dyadic_zero_bracket_budget import band_caps, dyadic_band, localization
from cp008_real_first52_refinement_preflight import parse_candidate

N_RS = 1_747_950
HALFWIDTH_BASE = F(2,10**9)
MAX_HALFWIDTH = F(1,1000)
BANDS = range(7,20)   # 128 <= original RS ordinates < 2^20
SOURCE_COMMIT = "c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
PIN = Path(__file__).with_name("cp007_upstream_store_source_manifest.json")


def row_weight(radius, band):
    """Height-band maximal sum of the 3x3 normalized cosine-moment Lipschitz row."""
    hs=(H,H,radius)
    caps=[band_caps(h,band) for h in hs]
    return max(sum(F(25,24)*(hs[i]+hs[k]) *
                   (caps[i][1]*caps[k][0]+caps[i][0]*caps[k][1]
                    +abs(CENTERS[i]-CENTERS[k])*caps[i][0]*caps[k][0])
                   for k in range(3)) for i in range(3))


def halfwidth_cap(band):
    """Single rational policy simultaneously valid for both frozen radii."""
    if band not in BANDS:
        raise ValueError("Dyadic band outside original 149.5..1,000,450 RS domain")
    return min(MAX_HALFWIDTH,
               HALFWIDTH_BASE * min(row_weight(r,0)/row_weight(r,band) for r in RADII))


def original_first52_error(radius):
    bins=defaultdict(lambda:F(0))
    for a,b in parse_candidate():
        bins[dyadic_band(a)] += (b-a)/2
    return localization(radius,dict(bins))


def uniform_rs_upper(radius):
    return N_RS*HALFWIDTH_BASE*row_weight(radius,0)


def total_conditional_bound(radius):
    """Conditional on real 52/RS interval proof & independent E_quad receipt."""
    return (E_tail(radius)+E_QUAD_ALLOWANCE+
            original_first52_error(radius)+uniform_rs_upper(radius))


def schedule_selftest():
    assert N_RS+52==1_748_002
    assert BANDS.start==7 and BANDS.stop==20
    for band in BANDS:
        half=halfwidth_cap(band)
        assert 0 < half <= MAX_HALFWIDTH
        for radius in RADII:
            assert half*row_weight(radius,band) <= HALFWIDTH_BASE*row_weight(radius,0)
    assert halfwidth_cap(7)==HALFWIDTH_BASE
    assert halfwidth_cap(18)==MAX_HALFWIDTH
    assert halfwidth_cap(14)>HALFWIDTH_BASE*100
    assert F(1,10**8)>halfwidth_cap(7)  # negative control; fails early-bin policy
    assert F(1,10**6)<halfwidth_cap(18) # high-bin permissive proof
    assert F(25,4)/(F(150)*4)==F(1,96)
    assert F(25,4)/(F(10**6)*32)==F(25,128000000)
    # The original Riemann-Siegel named analytic error bound includes
    # 25/(4 t^(5/4)) + 1/(32 t^(15/4)). Since 150^(1/4)<4
    # and (10^6)^(1/4)<32, the TWO rational lower bounds above hold.
    for radius in RADII:
        first=original_first52_error(radius)
        rs=uniform_rs_upper(radius)
        total=total_conditional_bound(radius)
        assert total<EPS_MAX
        print(f"radius={radius}, first52 candidate error={first} ({float(first):.12g})")
        print(f"  remaining RS {N_RS} uniform-budget upper={rs} ({float(rs):.12g})")
        print(f"  conditional total upper={total} ({float(total):.12g}); "
              f"target {EPS_MAX}; positive headroom {float(EPS_MAX-total):.12g}")
    for j in BANDS:
        print(f"dyadic [2^{j},2^{j+1}): allowable half-width "
              f"{halfwidth_cap(j)} ({float(halfwidth_cap(j)):.12g})")
    print("ORIGINAL RS ANALYTIC ERROR FLOOR: t=150 >1/96; t=10^6 >25/128000000")
    print("CP009 EXACT RATIONAL CONDITIONAL SCHEDULE PASS — NO CERTIFIED RS ROOTS OR LEAN PASS")


def git_blob_sha(path):
    size=path.stat().st_size
    h=hashlib.sha1(b"blob "+str(size).encode()+b"\0")
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()


def verify_shards(original_root, candidate_root, report_path):
    """STREAMING strict source row and planned-precision check, NOT sign proof."""
    pin=json.loads(PIN.read_text(encoding="utf-8"))
    if pin["pinned_commit"]!=SOURCE_COMMIT:
        raise ValueError("Pinned source commit mismatch")
    sources=pin["riemann_siegel"]["files"]
    manifest_path=candidate_root/"manifest.json"
    metadata=json.loads(manifest_path.read_text(encoding="utf-8"))
    if metadata.get("upstream_commit")!=SOURCE_COMMIT or metadata.get("rows")!=N_RS:
        raise ValueError("Candidate RS manifest must pin source commit and exact count")
    incoming=metadata.get("files")
    if not isinstance(incoming,list) or len(incoming)!=len(sources):
        raise ValueError("Seven certified candidate file records required")
    bands=defaultdict(lambda:F(0))
    count=0
    previous_right=None
    report=[]
    for file_index,(name,original_sha,expected_count,source_last) in enumerate(sources):
        orig=original_root/name
        candidate=candidate_root/name
        if git_blob_sha(orig)!=original_sha:
            raise ValueError(f"Original RS store Git SHA mismatch at {name}")
        if incoming[file_index].get("file")!=name or incoming[file_index].get("rows")!=expected_count:
            raise ValueError(f"Candidate manifest shard name/count mismatch at {name}")
        digest=hashlib.sha256(candidate.read_bytes()).hexdigest()
        if incoming[file_index].get("sha256")!=digest:
            raise ValueError(f"Candidate shard not digest-pinned at {name}")
        observed=0
        with orig.open("r",encoding="ascii") as old, candidate.open("r",encoding="ascii") as new:
            for orig_line,refined_line in itertools.zip_longest(old,new):
                if orig_line is None or refined_line is None:
                    raise ValueError(f"Original/candidate count mismatch in {name}")
                o=[s.strip() for s in orig_line.split(",")]
                q=[s.strip() for s in refined_line.split(",")]
                if len(o)!=3 or len(q)!=3:
                    raise ValueError(f"Invalid 3-column source row in {name}")
                observed+=1
                if int(o[0])!=count+1 or int(q[0])!=count+1:
                    raise ValueError(f"Original local RS root index mismatch at {name} row {observed}")
                olda,oldb=F(o[1]),F(o[2])
                a,b=F(q[1]),F(q[2])
                if not (olda<=a<b<=oldb and F(1495,10)<=a):
                    raise ValueError(f"Candidate RS zero is not inside original source at {name}:{observed}")
                if previous_right is not None and previous_right>=a:
                    raise ValueError(f"Candidate RS rows overlap at {name}:{observed}")
                previous_right=b
                band=dyadic_band(a)
                half=(b-a)/2
                if half>halfwidth_cap(band):
                    raise ValueError(f"RS root {count+1} in band 2^{band} exceeds exact CP009 halfwidth cap")
                bands[band]+=half
                count+=1
        if observed!=expected_count:
            raise ValueError(f"Original shard {name} count mismatch")
        if F(source_last)!=oldb:
            raise ValueError(f"Original {name} endpoint mismatch")
        report.append({"file":name,"rows":observed,"source_git_blob":original_sha,
                       "refined_sha256":digest})
    if count!=N_RS:
        raise ValueError("Incomplete RS root roster")
    first52={r:original_first52_error(r) for r in RADII}
    condition={}
    for radius in RADII:
        loc=localization(radius,dict(bands))
        total=E_tail(radius)+E_QUAD_ALLOWANCE+first52[radius]+loc
        if not total < EPS_MAX:
            raise ValueError("Actual candidate band's total error exceeds CP009 threshold")
        condition[str(radius)]={"rs_localization":str(loc),
                                "total_conditional_upper":str(total)}
    result={"status":"STRUCTURAL_PRECISION_POLICY_PASS_NOT_LEAN",
            "source_commit":SOURCE_COMMIT,"total_root_rows":count,
            "source_provenance":report,
            "by_band_halfwidth":{str(j):str(x) for j,x in sorted(bands.items())},
            "conditional_bounds":condition,
            "missing":"Actual RS endpoint sign/error kernel certificates, full original EF and quadrature"}
    report_path.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(result["status"],"rows",count,"bands",len(bands))
    print("Input manifests and exact ratios are NOT proof that each refined row has a zeta zero.")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--source-rs-dir",type=Path)
    p.add_argument("--candidate-rs-dir",type=Path)
    p.add_argument("--report",type=Path,default=Path("cp009-rs-precision-audit.json"))
    a=p.parse_args()
    if a.self_test:
        schedule_selftest()
    if a.source_rs_dir or a.candidate_rs_dir:
        if not a.source_rs_dir or not a.candidate_rs_dir:
            raise SystemExit("NOT_READY: must supply both RS source and candidate directories")
        try:
            verify_shards(a.source_rs_dir,a.candidate_rs_dir,a.report)
        except (OSError,ValueError,KeyError,IndexError,AssertionError) as exc:
            raise SystemExit(f"NOT_READY: {exc}")
    if not a.self_test and not a.source_rs_dir:
        p.print_help()


if __name__=="__main__":
    main()
