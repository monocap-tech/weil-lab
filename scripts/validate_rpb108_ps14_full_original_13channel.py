#!/usr/bin/env python3
"""PS14 full original signed Q thirteen-channel rational certificate."""

from fractions import Fraction as F
import json
from pathlib import Path
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps13_interior_morse_local as ps13

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
SRC=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
N={n for n,b in SRC}

def run():
    ps13.run()  # Original RC315 and entire signed PS01-PS13 replay.
    m=json.loads((ROOT/"research/obligations.json").read_text())
    p=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert p["id"]=="W-PHYSICAL-SHIFT" and p["status"]=="open"
    assert p["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(not x for x in p["closures"].values())

    pi=old.pi_iv()
    ln9=old.log_i(F(9))
    ln2=old.log_i(F(2))
    delta=old.IV(R-ln9.hi,R-ln9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    carch=-old.gamma_iv()-pi/2-3*ln2-old.log_i(pi)

    # Original thirteen PS10 source channels, exact RATIONAL offset labels.
    offsets=sorted({F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
                   |{F(9,n) for n in (2,4,5,7,8)})
    assert len(offsets)==13 and offsets[0]==1 and offsets[-1]==9
    logs={q:(old.IV(0) if q==1 else old.log_i(q)) for q in offsets}
    sep=min(logs[v].lo-logs[u].hi for u,v in zip(offsets,offsets[1:]))
    assert sep>F(1,10)>delta.hi
    # Verify all nonresonant original prime translations MISS the
    # entire thin channel interval, using exact rational ratio margins.
    assert old.log_i(F(101,100)).lo>delta.hi
    edges=[]
    for i,u in enumerate(offsets):
        for j in range(i+1,len(offsets)):
            v=offsets[j]
            for n,base in SRC:
                ratio=v/(u*n)
                if ratio==1:
                    edges.append((i,j,n))
                else:
                    assert ratio>=F(101,100) or ratio<=F(100,101)
    assert len(edges)==19
    assert len({(i,j) for i,j,n in edges})==19
