#!/usr/bin/env python3
"""Read-only Weil-Lab PR #356 threshold-0.003 preflight.

Exactly bounds the Fourier sublevel projector ON THE INHERITED SM40 COVER
using pinned #350 and #346 archives. Does NOT prove positivity in gaps of
the SM40 cover or global original-domain acceptance.
"""
import hashlib
import json
import sys
import zipfile
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))

P350 = "3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09"
P346 = "c853b66001e3a36346ce1310df3b60ca694b3b458e8d658a3e6955cf5a14291e"
J350 = "9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2"
J346 = "8b58972bbdd2f9cb5d00275820ab6d6891feeff3bbd584a1c28231770368f514"
LAM = Q(3, 1000)
B = Q(11, 10)
OM = Q(44, 7) * B

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def read_zip(path, archive_hash, filename, json_hash):
    raw = Path(path).read_bytes()
    assert sha(raw) == archive_hash, "Unexpected archive SHA256"
    with zipfile.ZipFile(path) as z:
        obj = z.read(filename)
    assert sha(obj) == json_hash, "Unexpected retained JSON SHA256"
    return json.loads(obj)

def main(path350, path346):
    p = read_zip(path350, P350, "original_BS_pruned_rank_bound.json", J350)
    q = read_zip(path346, P346, "original_affine_negative_cap.json", J346)
    assert p["retained_physical_rank_upper"] == 242
    assert sum(p["selected_multiplicities"]) == 241
    assert p["zero_constraint_cluster_count"] == 40
    assert q["subdivisions_per_cell"] == 16
    H = Q(q["full_multiplier_curvature_upper"])
    assert H == 2145
    assert p["original_nodes"] == [
        [x[0], x[1]] for x in p["original_nodes"]
    ]
    old_cells = [tuple(map(Q, x)) for x in q["original_SM40_cells"]]
    assert old_cells == [tuple(map(Q, x)) for x in
                         json.loads(zipfile.ZipFile(path350).read(
                             "sm40_original_envelope_method_stop.json"))["original_SM40_cells"]]
    assert len(old_cells) == 3892
    endpoints = {Q(x): (Q(a), Q(b)) for x, a, b in q["endpoint_multiplier_intervals"]}
    assert len(endpoints) == 62379  # 3892*16 + 107 initial cluster endpoints
    group = 0
    kept = {}
    above = below = unresolved = 0
    old_width = Q(0)
    kept_width = Q(0)
    # Parse every individual certified endpoint; never interpolate over
    # uncovered frequency gaps between successive SM40 clusters.
    for lo, hi, weight in old_cells:
        while group < 106 and lo >= Q(p["cluster_witnesses"][group]["hi"]):
            group += 1
        row = p["cluster_witnesses"][group]
        assert Q(row["lo"]) <= lo < hi <= Q(row["hi"])
        step = (hi - lo) / 16
        old_width += hi-lo
        for k in range(16):
            a, b = lo + k * step, lo + (k + 1) * step
            la, ua = endpoints[a]
            lb, ub = endpoints[b]
            curvature = H * (b-a)**2 / 8
            # Rigorous complete-cell range from upper/lower endpoint balls
            # and the accepted original |m''| < 2145.
            if min(la,lb)-curvature >= LAM:
                above += 1
                continue
            below += (max(ua,ub)+curvature < LAM)
            unresolved += (max(ua,ub)+curvature >= LAM)
            kept_width += b-a
            if group not in kept:
                kept[group] = [a,b]
            else:
                kept[group][0] = min(kept[group][0],a)
                kept[group][1] = max(kept[group][1],b)
    assert above+below+unresolved == 62272
    assert old_width == Q(973,64)
    assert kept_width == Q(35127,4096)
    # These are precisely the candidate old-cover sublevel regions.
    # A cluster-wide interval is a conservative superset of its retained
    # disjoint fine cells. Exact existing derivative zeros give a bound
    # on every original odd supported f in J_242^perp simultaneously.
    entries = []
    total = Q(0)
    for i, (lo,hi) in sorted(kept.items()):
        row = p["cluster_witnesses"][i]
        n = row["retained_multiplicity"]
        c = Q(row["center"])
        distance = max(abs(lo-c),abs(hi-c))
        candidates = [
            2*(hi-lo)*2*B*OM**(2*r)*distance**(2*r) /
            ((2*r+1)*factorial(r)**2)
            for r in range(n+1)
        ]
        index = min(range(n+1),key=lambda j: candidates[j])
        cost = candidates[index]
        total += cost
        entries.append({
            "cluster":i,"retained_order":n,"chosen_order":index,
            "lo":str(lo),"hi":str(hi),
            "unweighted_projector_payment":str(cost)
        })
    assert all(p["cluster_witnesses"][i]["retained_multiplicity"] > 0 for i in kept)
    assert total < Q(11,50000)  # 0.00022, by exact fractions.
    report = {
        "scope":"ONLY original 3892-cell SM40 support, NOT all positive frequencies",
        "inputs":["#350 retained original J242 multiplicities",
                  "#346 native 62379 original multiplier endpoint enclosures"],
        "inherited_m_curvature_upper":str(H),
        "test_level":str(LAM),
        "intervals_checked":62272,
        "strictly_above_level":above,
        "strictly_below_level":below,
        "unresolved_included":unresolved,
        "potential_sublevel_positive_frequency_width":str(kept_width),
        "bounded_clusters":len(entries),
        "zero_constraint_clusters_excluded":40,
        "projector_on_old_support_upper_exact":str(total),
        "projector_on_old_support_upper_simple":"11/50000",
        "new_gap_and_collar_check":"OPEN",
        "global_Q_sublevel_upper_1_over_50":"NOT ESTABLISHED",
        "new_full_exterior_floor":"NOT CERTIFIED",
        "W_ODD_NEG":"OPEN",
        "per_cluster":entries
    }
    path = Path(str(CUSTODY_ROOT / 'nf356_old_cover_preflight.json'))
    path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k!="per_cluster"},indent=2))

if __name__ == "__main__":
    assert len(sys.argv)==3
    main(sys.argv[1],sys.argv[2])
