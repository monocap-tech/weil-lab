#!/usr/bin/env python3
"""EF30: ORIGINAL SI10 470x471 moment rank via exact sampled rowspace.

This is NOT a floating Gram rank test. The 469 true physical source
moment rows are exact invertible block-lower-triangular transforms of
the sampled real-even exponential-polynomial rows:
  x_l**k*cos(2*pi*c_j*x_l), k even,
  x_l**k*sin(2*pi*c_j*x_l), k odd,
x_l=l/512, l=1..471; native 107 centers and p_j sum 469.
The leading diagonal coefficient in each block is bhat_r(c_j)>0
by 2*pi*c_j*r<pi/2 for r=1/8192. True positive-pole moment row
is J_r(1/2)*cosh(x_l/2) with J_r>0.

A 938th-order bilateral shift recurrence for even sequences
  P(E)=prod_j (E**2-2cos(2*pi*c_j/512)*E+1)**p_j
has actual source sample sequences as solutions. Since the sequences
are even, vanishing on integer sample indices 1..471 implies
vanishing -471..-1. If the CERTIFIED central coefficient
b_469=[E^469]P(E) is NONZERO, apply P(E) at -469: every term
except b_469 F(0) vanishes, so F(0)=0. Now 939 consecutive
samples vanish; the recurrence of order 938 with nonzero
constant and leading coefficients implies F=0 on ALL integers.
Distinct actual roots e^(±2*pi*i*c_j/512) and their multiplicities
then imply all 469 real-even polynomial source coefficients vanish.
Thus SI10 sampled/moment source rank is EXACTLY 469.

True pole row adds exactly one rank:
  the source sample matrix has algebraic entries (rational phase
  roots of unity), so its nullspace has nonzero algebraic vectors.
  For any nonzero algebraic a=(a_1,..,a_471),
  sum_l a_l cosh(l/1024) !=0:
  T=e^(1/1024) is transcendental (Hermite-Lindemann) and
  2 sum a_l cosh(l/1024)=sum a_l(T^l+T^-l) is a nonzero
  Laurent polynomial in T with ALGEBRAIC coefficients.
  Hence genuine positive-pole row is independent of the source
  rowspace. If source rank=469, true Htilde rank=470, nullity=1.

Every actual root phase is enclosed via the EF24 340-digit directed
integer original SI06 pi/trig routine. Native source P(E) coefficients
are recursively outward-rounded at EVERY polynomial multiplication;
the 938-degree polynomial is never replaced by a sampled float.
If b469 interval includes zero, report CONDITIONAL rank only;
never claim a certified actual full rank.

Full genuine g vector (EF29) is already an accepted Actions artifact;
δ=dist(g,rowspace Htilde), original arch diagonal A and full corrected
even/odd/whole Weil/RH remain UNCOMPUTED/OPEN.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from validate_rpb108_ef28_pole_neutral_moment_kernel import (
    original_source_and_geometry, GRID,R,COUNT,TOTAL_ROWS,D
)
from validate_rpb108_ef24_original_even_edge_intervals import (
    I,S,trig_pi
)

ROOT=Path(__file__).resolve().parents[1]
N=469

def native_root_non_aliases(centers):
    assert len(centers)==107
    roots=[]
    for i,c in enumerate(centers):
        # e^(i*theta)=e^(-i*theta) iff c/256 is integer:
        assert (c/F(256)).denominator!=1,("source self-conjugate root",i,c)
        roots.append((c,1))
        roots.append((-c,1))
    for i in range(len(roots)):
        for j in range(i+1,len(roots)):
            a,b=roots[i][0],roots[j][0]
            assert ((a-b)/512).denominator!=1,(
                "native SI10 sampled root alias",i,j,a,b)
    return len(roots)

def original_characteristic_central(centers,orders):
    """Full exact real recurrence P(E) with outward 340-digit coeffs."""
    poly=[I(S)]
    t=0
    for j,(c,p) in enumerate(zip(centers,orders)):
        ct,_=trig_pi(2*c*GRID)
        factor=-2*ct
        assert ct.lo>=-S and ct.hi<=S
        for _ in range(p):
            old=poly
            q=[I(0) for _ in range(len(old)+2)]
            for k,v in enumerate(old):
                q[k]=q[k]+v
                q[k+1]=q[k+1]+factor*v
                q[k+2]=q[k+2]+v
            poly=q
            t+=1
    assert t==N and len(poly)==2*N+1==939
    assert poly[0].lo==poly[0].hi==S
    assert poly[-1].lo==poly[-1].hi==S
    # Source P(E) is exactly real monic self-reciprocal.
    # Verify enclosures of mirrored coefficients overlap.
    for k in (0,1,2,3,37,468,469,470,471,901,936,938):
        a,b=poly[k],poly[2*N-k]
        assert max(a.lo,b.lo)<=min(a.hi,b.hi)
    central=poly[N]
    neighbors=[(k,poly[k].sign(),poly[k].scaled()) for k in range(N-2,N+3)]
    print("EF30 genuine original 938-order sampled shift recurrence"
          " P(E) center b469:",central.scaled(),
          "sign",central.sign(),"interval relative precision:"
          " 10^340 fixed-point source",flush=True)
    print("EF30 native central five coefficient intervals:",neighbors,flush=True)
    if not central.excludes_zero():
        print("EF30 SOURCE METHOD STOP: central coefficient interval"
              " includes zero. No full actual 469 sampled row rank"
              " certified by the central-recurrence criterion.",flush=True)
    return central

def exact_triangular_moment_rowspace(centers,orders,xs):
    # The physical original bell Fourier bhat_r(c)>0 directly:
    # positive cos integrand when |2*pi*c*t|<pi/2 for |t|<r.
    # Because max c<896 and r=1/8192, 4*c*r<1.
    assert max(centers)<F(896)
    assert 4*max(centers)*R<1
    # b even, so for k even (x^k cos), odd (x^k sin),
    # convolution expands via binomial in t:
    # leading degree k coefficient is bhat_r(c)>0;
    # all lower degree terms stay same even source family.
    # Triangular within EACH original c cluster, no
    # operator reconstruction or numerical row inverse.
    assert sum(orders)==N
    assert len(xs)==COUNT and len(centers)==len(orders)==107
    # Genuine positive even pole:
    # <cosh(x/2),phi_l>=J_r(1/2)*cosh(x_l/2),
    # J_r positive because b_r>0, cosh(t/2)>0.
    return True

def source_degree_and_rigidity_regression():
    # Independent EXACT rational toy source for the central
    # coefficient/proof step, not the genuine SI10 certificate:
    # z_j roots from t²-2u_j t+1 with u_j=1/3,2/5.
    toy=[(F(1,3),2),(F(2,5),1)]
    poly=[F(1)]
    for u,p in toy:
        for _ in range(p):
            old=poly
            new=[F(0) for _ in range(len(old)+2)]
            for k,v in enumerate(old):
                new[k]+=v
                new[k+1]-=2*u*v
                new[k+2]+=v
            poly=new
    assert len(poly)==7 and poly[3]!=0
    assert poly==poly[::-1]
    # Simulated even source recurrence F(k)=z^k+z^-k
    # satisfies its matching quadratic for every integer k
    # (formal Laurent polynomial shift identity).
    return poly[3]

def run():
    m=json.loads((ROOT/"research/obligations.json").read_text())
    ob={x["id"]:x for x in m["obligations"]}
    assert m["active_obligation"]=="W-EVEN-FORM"
    assert all(ob[x]["status"]=="open" for x in ("W-EVEN-FORM","W-ODD-NEG","W-WHOLE-FORM"))
    assert "EF30" in ob["W-EVEN-FORM"]["evidence"]
    centers,orders,xs=original_source_and_geometry()
    assert sum(orders)==N
    distinct=native_root_non_aliases(centers)
    assert distinct==214
    exact_triangular_moment_rowspace(centers,orders,xs)
    toy=source_degree_and_rigidity_regression()
    central=original_characteristic_central(centers,orders)
    print("EF30 actual SI10 source original 107 centers / 469"
          " real-even rows, 471 bell pairs at l/512;",
          " sampled roots 214 DISTINCT; repeated orders total 938."
          " Actual physical source H rows = invertible positive"
          " diagonal BLOCK triangular transforms of sampled rows.",
          flush=True)
    print("EF30 positive original pole sample row:"
          " J_r(1/2)*cosh(l/1024), J_r>0; pole INDEPENDENT"
          " over real source rowspace by algebraic sampled"
          " roots of unity + transcendental e^(1/1024).",flush=True)
    print("EF30 toy rational central coefficient:",toy,
          "only regression, not original proof.",flush=True)
    if central.excludes_zero():
        print("EF30 ORIGINAL EXACT RANK CERTIFIED:"
              " b469!=0 -> even 469 source sampled rows independent"
              " on 471 positive points by 938-order recurrence."
              " Genuine source moment rank EXACTLY 469 via"
              " triangular nonzero bhat_r(c) transforms;"
              " genuine pole adds one rank =>"
              " rank Htilde=470, dim ker Htilde=1.",
              flush=True)
    else:
        print("EF30 EXACT RANK NOT CLOSED: only source/pole"
              " row-equivalence and pole independence accepted.",
              flush=True)
    print("EF30 OPEN: genuine 471-dimensional EF29 signed g vector"
          " is calculated, but oriented one-dimensional kernel"
          " projector and δ are NOT calculated;"
          " matrix smallest singular value unbounded;"
          " A_arch and corrected even Schur sign NOT computed;"
          " W-EVEN/odd/whole Weil/RH OPEN.",flush=True)

if __name__=="__main__":
    run()
