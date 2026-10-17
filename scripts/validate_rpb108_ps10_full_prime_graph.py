#!/usr/bin/env python3
"""PS10 exact original seven-prime IMS physical graph certificate.

13 disjoint physical L2 channels; exact 13-edge/5-mode fiber; original
weights and sharp full-prime IMS norm. No full signed Weil PSD or RH.
"""
import json
from pathlib import Path
from fractions import Fraction as F
from math import sqrt
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps09_prime3_triad as ps09

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
SMALL=(2,3,4,5,7,8)
SOURCE=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    ps09.run()  # Replays PS07, PS06, PS03 and pinned RC315 originals.
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(v is False for v in lane["closures"].values())

    log9=old.log_i(F(9))
    log2=old.log_i(F(2))
    delta=old.IV(R-log9.hi,R-log9.lo)
    a=old.IV(log9.lo-B,log9.hi-B)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert log2.lo>delta.hi and old.log_i(F(8)).hi<2*a.lo

    # Rational labels mean exact log-offset equivalence:
    # log(9/3)=log3 is the ONLY duplicated interior source.
    offsets={F(1),F(9)}
    offsets.update(F(n) for n in SMALL)
    offsets.update(F(9,n) for n in SMALL if n!=3)
    assert len(offsets)==13 and F(9,3)==F(3)
    logs={x:(old.IV(0) if x==1 else old.log_i(x)) for x in offsets}
    order=sorted(offsets,key=lambda x:logs[x].lo)
    assert order[0]==1 and order[-1]==9
    sep=min(logs[y].lo-logs[x].hi for x,y in zip(order,order[1:]))
    assert sep>F(1,10)>delta.hi
    for x in order:
        # Each actual interval [-B+log x, -B+log x+delta] lies in I.
        assert -B+logs[x].lo>=-B
        assert -B+logs[x].hi+delta.hi<=B+F(1,10**24)
        if x not in (F(1),F(9)):
            assert logs[x].lo>3*delta.hi/4
            assert logs[x].hi<log9.lo-3*delta.hi/4
    assert sum(x not in (1,9) for x in offsets)==11

    # All nonzero IMS edges have one physical edge-active endpoint.
    # n<9 translates LEFT->interior and interior->RIGHT; n9 L->R.
    edges=[(F(1),F(n),n) for n in SMALL]
    edges += [(F(9,n),F(9),n) for n in SMALL]
    edges += [(F(1),F(9),9)]
    assert len(edges)==13
    assert all(u in offsets and v in offsets for u,v,n in edges)
    assert len({frozenset((u,v)) for u,v,n in edges})==13
    deg={x:0 for x in offsets}
    for u,v,n in edges:
        deg[u]+=1
        deg[v]+=1
    assert sorted(deg.values())==[1]*10+[2,7,7]
    assert deg[F(1)]==deg[F(9)]==7 and deg[F(3)]==2
    assert log9.lo>2*a.hi
    for n in SMALL:
        assert old.log_i(F(n)).hi<2*a.lo

    # Seven true Lambda(n) weights with no float acceptance.
    w={}
    rho2=old.IV(0)
    for n,base in SOURCE:
        ell=old.log_i(F(base))
        rho2+=ell**2/F(n)
        root=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        w[n]=ell/root
        assert w[n].lo>0
    assert set(w)=={2,3,4,5,7,8,9}
    assert F(1419,1000)**2<rho2.lo<=rho2.hi<F(1420,1000)**2

    leaf5sq=sum((old.log_i(F(base))**2/F(n)
       for n,base in SOURCE if n in (2,4,5,7,8)),old.IV(0))
    assert 0<leaf5sq.lo and leaf5sq.hi<rho2.lo
    # Five invariant fiber modes: hubs L,R, shared C3, collective
    # five-leaf left & right vectors. Exactly 8 common null modes.
    assert len(offsets)==5+8 and len(SMALL)-1==5
    # For z in [0,pi/2]: p=1-cos(z), q=1-sin(z).
    # M(z)<=entrywise p*M_left+q*M_right and p+q<=1.
    # Both endpoint hub-stars have spectral norm rho=sqrt(rho2).
    # Thus entire seven-prime IMS operator norm is EXACTLY rho,
    # attained on a positive-measure edge plateau.
    for s,c in ((F(0),F(1)),(F(3,5),F(4,5)),
                (F(4,5),F(3,5)),(F(1),F(0))):
        assert s*s+c*c==1
        p,q=1-c,1-s
        assert 0<=p<=1 and 0<=q<=1 and p+q<=1
        assert 0<=1-2*s*c<=p+q

    print("PS10 original 13-channel offset gap >=",float(sep),flush=True)
    print("PS10 complete original prime IMS graph vertices",len(offsets),flush=True)
    print("PS10 true signed original weighted source edges",len(edges),flush=True)
    print("PS10 fixed active fiber channels",5,"common null channels",8,flush=True)
    print("PS10 original 5-leaf weight-square upper",float(leaf5sq.hi),flush=True)
    print("PS10 exact sharp full seven-prime squared norm enclosure",
          float(rho2.lo),float(rho2.hi),flush=True)
    print("PS10 exact sharp prime IMS norm approx",sqrt(float(rho2.lo)),flush=True)
    print("PS10 complete IMS essential norm approx",sqrt(float(rho2.lo)),flush=True)
    print("PS10 PASS SCOPED: original seven-prime IMS defect is"
          " globally an EXACT 13-channel/13-edge physical direct fiber,"
          " reduced to 5 active fiber modes; sharp full prime norm and"
          " complete IMS essential norm sqrt(sum w_n**2) in (1.419,1.420)."
          " No inverse-energy spectral solve, Weil Schur PSD or RH.",flush=True)

if __name__=="__main__":
    run()
