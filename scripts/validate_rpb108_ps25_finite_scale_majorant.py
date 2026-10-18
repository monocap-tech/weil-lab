#!/usr/bin/env python3
"""PS25 — FINITE-SCALE source-true 12-window signed Schur via exact 12x12 Z majorant.

Unlike PS24's 2**-192 second-generation collars, the two new
reflected outer collars have the SAME width 1/2048 as the first.
All twelve physical windows are included SIMULTANEOUSLY, not with
a too-small nested 10-window scalar pivot. Source response is
bounded by a true componentwise rank-one Schur majorant and all
original noncompact adjacent arch Carleman seams are included.

Exact outward rational scalar matrix M with offdiagonal <=0:
  Q_C[f] >= t^T M t, t_i=||f_i||.
Verify M-1/4 I >0 with a strictly positive INTEGER weighted
diagonal-dominance vector. This proves S_C>1/4 mass on all 12
infinite-dimensional physical windows in BOTH parity sectors.
Original full residual PSD, CC27 D-Riesz, W-ODD-NEG and RH OPEN.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps24_second_generation_seam as ps24

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
L=F(1,128)
E=F(1,2048)
a,b=F(1,32),F(5,128)
v=F(1,6)
ORIGINAL=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
LABELS=sorted({F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
              |{F(9,n) for n in (2,4,5,7,8)})
GRID=10**12
SQGRID=10**8
MGRID=10**7

def down(q,grid=GRID):
    return F(q.numerator*grid//q.denominator,grid)
def up(q,grid=GRID):
    return F(-((-q.numerator*grid)//q.denominator),grid)
def endpoint(lo,hi=None):
    if hi is None:hi=lo
    return (down(lo),up(hi))
def interval(start,end,width,label):
    assert width>0
    return (start,end,width,label)
def gap_lo(p,q):
    return max(q[0][0]-p[1][1],p[0][0]-q[1][1])
def sqrt_up(q,grid=SQGRID):
    assert q>=0
    n=q.numerator*grid*grid
    d=q.denominator
    k=isqrt(n//d)
    if k*k*d<n:k+=1
    return F(k,grid)
def norm_round(q):
    return up(q,MGRID)

def run():
    ps24.run() # original 13-source and all PS01–PS24 source obligations
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(x is False for x in lane["closures"].values())

    ell=old.log_i(F(2))
    ell9=old.log_i(F(9))
    delta=old.IV(R-ell9.hi,R-ell9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    # Original eight windows plus two *first-generation* collars X
    # and a NEW pair Y with THE SAME fixed width E=1/2048.
    # Indices sorted left to right:
    # 0 -J-ln2, 1 -ln2/2, 2 -V, 3 Y-,4 X-,5 -J,
    # 6 J,7 X+,8 Y+,9 V,10 ln2/2,11 J+ln2.
    wins=[
      interval(endpoint(-b-ell.hi), endpoint(-a-ell.lo),L,"U-left-outer"),
      interval(endpoint(-ell.hi/2-L/2),endpoint(-ell.lo/2+L/2),L,"U-left-mid"),
      interval(endpoint(-v-L),endpoint(-v),L,"U-left-V"),
      interval(endpoint(-b-2*E),endpoint(-b-E),E,"Y-left-finite"),
      interval(endpoint(-b-E),endpoint(-b),E,"X-left"),
      interval(endpoint(-b),endpoint(-a),L,"U-left-inner"),
      interval(endpoint(a),endpoint(b),L,"U-right-inner"),
      interval(endpoint(b),endpoint(b+E),E,"X-right"),
      interval(endpoint(b+E),endpoint(b+2*E),E,"Y-right-finite"),
      interval(endpoint(v),endpoint(v+L),L,"U-right-V"),
      interval(endpoint(ell.lo/2-L/2),endpoint(ell.hi/2+L/2),L,"U-right-mid"),
      interval(endpoint(a+ell.lo),endpoint(b+ell.hi),L,"U-right-outer")
    ]
    n=len(wins)
    assert n==12
    for i,p in enumerate(wins):
        assert p[0][0]<p[0][1]+p[2] and p[0][1]<p[1][0]
        assert p[0][0]>-B and p[1][1]<B
        if i>0:assert p[0][0]>=wins[i-1][1][0]
    assert 8*L+4*E==F(33,512) # nonshrinking positive physical coverage
    # Four REAL adjacent noncompact corner interfaces across the
    # two three-interval chains: Y-X-U and U-X-Y.
    touches={(3,4),(4,5),(6,7),(7,8)}
    for i in range(n):
        for j in range(i+1,n):
            if (i,j) in touches:
                # Exact rational symbolic endpoints; no rounding of
                # a tiny physical width to zero.
                assert j==i+1 and gap_lo(wins[i],wins[j])>=-F(1,10**10)
            else:assert gap_lo(wins[i],wins[j])>0,(i,j)

    # True original thirteen-source sharp physical intervals.
    src=[]
    for r in LABELS:
        lr=(old.IV(0) if r==1 else old.log_i(r))
        src.append(interval(endpoint(-B+lr.lo,-B+lr.hi),
                            endpoint(-B+lr.lo+delta.lo,-B+lr.hi+delta.hi),
                            delta.hi,str(r)))
    assert len(src)==13

    # All 12*13*7*2 = 2184 TRUE original source-to-new-module
    # prime shift configurations have STRICT physical clearance.
    # No source-prime cross may be removed without this test.
    shifts={p:old.log_i(F(p)) for p,_ in ORIGINAL}
    all_checks=0
    min_source_clearance=None
    for w in wins:
        for p in src:
            assert gap_lo(w,p)>0
            for number,shift in shifts.items():
                for sign in (-1,1):
                    moved=(endpoint(w[0][0]+shift.lo,w[0][1]+shift.hi),
                           endpoint(w[1][0]+shift.lo,w[1][1]+shift.hi)
                           ) if sign==1 else (
                           endpoint(w[0][0]-shift.hi,w[0][1]-shift.lo),
                           endpoint(w[1][0]-shift.hi,w[1][1]-shift.lo))
                    d=gap_lo((moved[0],moved[1],w[2],"shift"),p)
                    assert d>0,("PS25 source prime collision",w[3],p[3],number,sign,float(d))
                    min_source_clearance=(d if min_source_clearance is None else
                                          min(min_source_clearance,d))
                    all_checks+=1
    assert all_checks==2184
    assert min_source_clearance>F(1,200)

    # All seven TRUE original internal prime powers checked for every
    # pair, including 2 measure-zero n2 contacts, and exactly
    # 3 genuine positive-measure original n2 translations.
    exact_links={(0,5,2),(1,10,2),(6,11,2)}
    exact_touches={(0,4,2),(7,11,2)}
    overlap_links=[]
    endpoint_contacts=[]
    for i in range(n):
        for j in range(i+1,n):
            for number,shift in shifts.items():
                sh_lo=endpoint(wins[i][0][0]+shift.lo,wins[i][0][1]+shift.hi)
                sh_hi=endpoint(wins[i][1][0]+shift.lo,wins[i][1][1]+shift.hi)
                d=gap_lo((sh_lo,sh_hi,wins[i][2],"shift"),wins[j])
                if (i,j,number) in exact_links:
                    assert d<-F(1,1000)
                    overlap_links.append((i,j,number))
                elif (i,j,number) in exact_touches:
                    assert -F(1,10**10)<d<F(1,10**10)
                    endpoint_contacts.append((i,j,number))
                else:
                    assert d>0,("unexpected prime overlap",i,j,number,float(d))
    assert set(overlap_links)==exact_links
    assert set(endpoint_contacts)==exact_touches

    pi=old.pi_iv()
    assert pi.hi/2<F(11,7)
    w2=ell/old.sqrt_i(2)
    assert w2.lo>0 and w2.hi<F(1,2)

    # Actual original 64-term digamma diagonal tail on U width L,
    # and the 256-term original bound on all FOUR width E collars.
    carch=-old.gamma_iv()-pi/2-3*ell-old.log_i(pi)
    def arch_tail(width,num_terms):
        result=F(0)
        for k in range(num_terms):
            nu=F(4*k+1,2)
            x=nu*width
            assert 0<x<32
            result+=2*(1-x/32)**32/nu
        return result+carch.lo
    assert arch_tail(L,64)>F(11,5)
    assert arch_tail(E,256)>F(4)
    diagonal=[F(11,5) if w[2]==L else F(4) for w in wins]

    # ACTUAL all-pair arch integral bound:
    # touching: Carleman norm pi/2 + sqrt(width_i*width_j);
    # separated distance d>0:
    # ||kernel||_HS <= sqrt(A*C)
    #    +.5 sqrt(A*C/[d(d+A+C)]).
    # Proof: k<=1+1/(2u), Minkowski HS, and
    # int int (d+s+t)^-2 ds dt
    # =log(1+AC/[d(d+A+C)]) <=AC/[d(d+A+C)].
    def arch_pair(i,j):
        A,C=wins[i][2],wins[j][2]
        if (i,j) in touches:
            return norm_round(F(11,7)+sqrt_up(A*C))
        d=gap_lo(wins[i],wins[j])
        assert d>0
        return norm_round(sqrt_up(A*C)+F(1,2)*sqrt_up(A*C/(d*(d+A+C))))

    # Entire original P / individual window ARCH kernel rectangles,
    # as bounded HS; unlike a GLOBAL source response bound, this
    # retains source-response geometry channel by channel.
    # The source-P pole vector is paid with BOTH real original signs.
    def local_t(i):
        p=wins[i]
        return max((abs(q) for end in (p[0],p[1]) for q in end))/2
    def cbound(t):return F(1)/(1-t*t/2)
    def sbound(t):return t/(1-t*t/6)
    assert all(local_t(i)<F(3,5) for i in range(n))
    bvec=[]
    oddvec=[]
    for i,w in enumerate(wins):
        width=w[2]
        hs=F(0)
        for s in src:
            d=gap_lo(w,s)
            assert d>0
            hs+=delta.hi*width*(1+F(1,2*d))**2
        barch=sqrt_up(hs)
        sqrtwidth=sqrt_up(width)
        t=local_t(i)
        # ||Pc||<=sqrt(13delta)*7/6 <(1/5)(7/6).
        # ||Ps||<1/5*7/12. Both real signed poles retained.
        bpole=2*F(1,5)*sqrtwidth*(F(7,6)*cbound(t)+F(7,12)*sbound(t))
        bvec.append(norm_round(barch+bpole))
        oddvec.append(norm_round(sqrtwidth*sbound(t)))
    assert len(bvec)==len(oddvec)==n

    # Symmetric exact rational Z-matrix lower of the ORIGINAL
    # signed source-ELIMINATED Q_C on entire 12-window space.
    # Drop original positive even pole safely; pay original odd pole
    # as rank-one 2*oddvec*oddvec^T. Pay full positive true source
    # energy-dual subtraction by bvec bvec^T/(323/1000),
    # using PS16's original 13-source A_P>323/1000.
    M=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i]=diagonal[i]-2*oddvec[i]**2-bvec[i]**2/F(323,1000)
        for j in range(i+1,n):
            val=arch_pair(i,j)
            if (i,j,2) in exact_links:val+=w2.hi
            val+=2*oddvec[i]*oddvec[j]+bvec[i]*bvec[j]/F(323,1000)
            M[i][j]=M[j][i]=-val
            assert val>0
    assert all(M[i][j]<0 for i in range(n) for j in range(n) if i!=j)

    # EXACT POSITIVE INTEGER WEIGHTED Z-MATRIX DIAGONAL DOMINANCE:
    # M-1/4 I has negative offdiagonals. If v>0 and (M-.25I)v>0
    # coordinatewise, congruence by diag(v) yields a symmetric
    # positive strictly row-diagonally dominant matrix, hence SPD.
    # This certifies an unshifted original signed Schur lower gap
    # on ALL arbitrary 12 physical-component functions, not just
    # one test vector or a truncated operator matrix.
    weights=[301,197,140,327,472,703,703,472,327,140,197,301]
    assert len(weights)==n and all(x>0 for x in weights)
    mu=F(1,4)
    margins=[sum((M[i][j]*weights[j] for j in range(n)),F(0))
             -mu*weights[i] for i in range(n)]
    assert all(z>F(0) for z in margins),[
       (i,float(z)) for i,z in enumerate(margins)]
    # The source-adjusted Z-majorant is reflection-symmetric.
    assert all(abs(M[i][j]-M[n-1-i][n-1-j])<F(1,100)
               for i in range(n) for j in range(n))

    # This certificate covers a fixed useful physical width
    # 8*(1/128)+4*(1/2048)=33/512, compared with PS24
    # 8L+2E+2**(-191), *without* any 2**(-192) new subintervals.
    # It remains only a small fraction of original I length 11/5.
    physical_coverage=8*L+4*E
    covered_with_source=physical_coverage+13*delta.hi
    assert physical_coverage==F(33,512)
    assert covered_with_source<R/F(20) # <5% of original whole interval
    uncovered_lower=R-covered_with_source
    assert uncovered_lower>F(2)
    print("PS25 finite-scale 12-window physical measure",float(physical_coverage),flush=True)
    print("PS25 2nd collar width NONSHRINKING",float(E),flush=True)
    print("PS25 source-to-12-window original prime shift checks",all_checks,flush=True)
    print("PS25 strict source prime minimum clearance",float(min_source_clearance),flush=True)
    print("PS25 real original prime links",overlap_links,flush=True)
    print("PS25 exact measure-zero n2 contacts",endpoint_contacts,flush=True)
    print("PS25 original 64+256 arch tail lower gates",float(arch_tail(L,64)),float(arch_tail(E,256)),flush=True)
    print("PS25 maximum componentwise full original source cross",float(max(bvec)),flush=True)
    print("PS25 exact weighted positive diagonal-dominance min slack",float(min(margins)),flush=True)
    print("PS25 original signed source Schur TWELVE-channel positive margin >",float(mu),flush=True)
    print("PS25 original physical support uncovered length lower",float(uncovered_lower),flush=True)
    print("PS25 PASS SCOPED: full unchanged original source-adjusted"
          " signed Weil Schur strictly >1/4 L2 on the ENTIRE"
          " reflection-symmetric 12-window INFINITE-DIMENSIONAL"
          " carrier with FOUR TRUE NONCOMPACT arch Carleman seams,"
          " THREE original signed n2 links, all inter-channel"
          " arch cross (including CLOSE but separated U/Y), BOTH"
          " original signed pole contributions and FULL source"
          " inverse paid by a verified EXACT rational 12x12"
          " Z-majorant and integer diagonal-dominance witness."
          " SECOND GENERATION WIDTH E=1/2048 (nonshrinking)."
          " Less than 5% of physical domain is covered including"
          " source; remaining signed complementary Schur, native"
          " CC27 D-Riesz, W-ODD-NEG, W-EVEN-FORM, whole Weil and"
          " RH remain OPEN.",flush=True)

if __name__=="__main__":
    run()
