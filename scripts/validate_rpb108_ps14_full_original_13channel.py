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

    # All 19 original signed prime-translation edges, rather than the
    # 13 edges of the IMS localization defect, occur as exact channel
    # multipliers with entries -w_n on the entire L2[0,delta] fiber.
    w={}
    for n,base in SRC:
        root=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        w[n]=old.log_i(F(base))/root
        assert w[n].lo>0
    W=[[F(0) for j in range(13)] for i in range(13)]
    for i,j,n in edges:
        W[i][j]=W[j][i]=w[n].hi
    # W is symmetric entrywise nonnegative. Its spectral radius
    # squared is <=max row sum of W^2. Every entry is Fraction.
    squared=[[sum((W[i][k]*W[k][j] for k in range(13)),F(0))
              for j in range(13)] for i in range(13)]
    rowmax=max(sum(row,F(0)) for row in squared)
    assert rowmax<F(11,5)**2,float(rowmax)

    # True short-interval J local lower from original nonnegative
    # digamma kernel, with physical channel length delta.
    # 64 original terms, exact rational Bernoulli exponential enclosure:
    # exp(-x)>=(1-x/32)^32 for x<32.
    T64=F(0)
    for m in range(64):
        lam=F(4*m+1,2)
        x=lam*delta.hi
        assert F(0)<x<F(32)
        T64+=2*(1-x/32)**32/lam
    assert carch.lo+T64>F(8,3),float(carch.lo+T64)

    # Off-channel original arch kernel -k(|x-y|), x in one source
    # interval and y in another. All distances >=g=0.1-delta.
    # Exact k(u)<=1/(2u)+1, Schur row integral <=12delta*k(g).
    g=F(1,10)-delta.hi
    assert g>F(17,175)
    arch_cross=12*delta.hi*(1+F(1)/(2*g))
    assert arch_cross<F(1,4),float(arch_cross)

    # The original positive even pole is retained safely by
    # dropping it only in this Q LOWER bound. Original odd pole
    # costs at most 2*measure(union)*sinh(B/2)^2.
    sn,cs=old.sinh_cosh_iv(B/2)
    odd_cost=26*delta.hi*sn.hi**2
    assert odd_cost<F(1,30),float(odd_cost)

    original_gap=carch.lo+T64
    # Strict SOURCE margin on the entire infinite-dimensional
    # supported thirteen-channel ORIGINAL signed form.
    lower_cert=F(8,3)-F(11,5)-F(1,4)-F(1,30)
    assert lower_cert==F(11,60)>F(1,6)
    assert original_gap-F(11,5)-arch_cross-odd_cost>F(1,6)

    print("PS14 thirteen original physical intervals",len(offsets),flush=True)
    print("PS14 exact min offset gap",float(sep),flush=True)
    print("PS14 full original 19 prime edges",len(edges),flush=True)
    print("PS14 full original 19-edge signed prime W-square row bound",
          float(rowmax),flush=True)
    print("PS14 true original arch 64-term integrated tail",float(T64),flush=True)
    print("PS14 true original arch diagonal+carch lower",float(original_gap),flush=True)
    print("PS14 true off-channel original arch norm bound",float(arch_cross),flush=True)
    print("PS14 true signed odd pole bound",float(odd_cost),flush=True)
    print("PS14 certified entire-source original unshifted Q gap",
          float(original_gap-F(11,5)-arch_cross-odd_cost),flush=True)
    print("PS14 PASS SCOPED: Q>1/6 L2 mass on complete 13-channel"
          " PS10 source carrier with separately admissible pieces,"
          " including all 19 actual original signed prime edges."
          " Whole interior complement/cross-Schur, CC27 D-Riesz"
          " attachment, W-ODD-NEG and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
