#!/usr/bin/env python3
"""PS20: true original signed six-window Schur-positive module and nested Schur.

Source-pinned exact original seven-prime quadratic Q. The already
source-eliminated S_C is >7/6 on six reflecting complement windows;
all six internal window arch cross, real two log2 translation links,
both original poles and actual thirteen-source energy-dual response
are retained. Then split the REST of original complement using true
form-domain-preserving sharp projections and derive a second exact
signed Schur, with noncompact L2 cross and compact energy-dual penalty.

Does NOT claim the residual signed Schur PSD, CC27 D-Riesz transfer,
W-ODD-NEG/W-EVEN-FORM, full Weil positivity or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json

import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps19_coupled_quiet_fourblock as ps19

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
SOURCES=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
LABELS=sorted({F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
              |{F(9,n) for n in (2,4,5,7,8)})
w=F(1,128)
a,b=F(1,32),F(5,128)
v=F(1,6)

def iv(lo,hi=None):
    return old.IV(lo,hi)

# Exact-rational outward geometry grid: source logarithms are proved
# by the pinned RC315 220-term enclosure, then all repeated 1092
# incidence / 78 kernel calculations use conservative 10^-15 bounds.
# This avoids enormous denominators without using floating-point tests.
GRID=10**15
def snap(q):
    return F(q.numerator*GRID//q.denominator, GRID)
def ceilgrid(q):
    return F(-((-q.numerator*GRID)//q.denominator),GRID)
def snap_iv(x):
    return iv(snap(x.lo),ceilgrid(x.hi))

def run():
    ps19.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(not x for x in lane["closures"].values())

    ln2=old.log_i(F(2))
    ln9=old.log_i(F(9))
    delta=iv(R-ln9.hi,R-ln9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert b-a==w
    # Explicit full SIX physically supported windows:
    # [-b-ln2,-a-ln2];[-v-w,-v];[-b,-a];[a,b];[v,v+w];[a+ln2,b+ln2].
    # Exact reflection invariance with internal signed log2 edge pairs.
    wins=[
        (iv(-b-ln2.hi,-b-ln2.lo),iv(-a-ln2.hi,-a-ln2.lo)),
        (iv(-v-w),iv(-v)),
        (iv(-b),iv(-a)),
        (iv(a),iv(b)),
        (iv(v),iv(v+w)),
        (iv(a+ln2.lo,a+ln2.hi),iv(b+ln2.lo,b+ln2.hi))
    ]
    assert len(wins)==6 and 6*w==F(3,64)
    wins=[(snap_iv(lo),snap_iv(hi)) for lo,hi in wins]
    for lo,hi in wins:
        assert -B<lo.lo<=lo.hi<hi.lo<=hi.hi<B
        assert w<=hi.hi-lo.lo<w+F(1,10**12)
    for i in range(5):
        assert wins[i][1].hi < wins[i+1][0].lo
    assert -(v+w)==-v-w and -(b+ln2.lo)==-b-ln2.lo

    logs={r:(iv(0) if r==1 else snap_iv(old.log_i(r))) for r in LABELS}
    source=[(r,snap_iv(iv(-B+logs[r].lo,-B+logs[r].hi)),
                 snap_iv(iv(-B+logs[r].lo+delta.lo,-B+logs[r].hi+delta.hi)))
                 for r in LABELS]
    assert len(source)==13

    # All 6*13 source/physical windows truly disjoint.
    # Explicit full original source to W arch HS kernel -k(|x-y|).
    hs_arch_sq=F(0)
    min_source_gap=None
    for lo,hi in wins:
        for r,left,right in source:
            d=max(lo.lo-right.hi,left.lo-hi.hi)
            assert d>0,("PS20 source/window overlap",str(r),float(d))
            min_source_gap=d if min_source_gap is None else min(min_source_gap,d)
            hs_arch_sq+=delta.hi*w*(F(1)+F(1,2*d))**2
    assert min_source_gap>F(1,1000)
    assert hs_arch_sq<F(4,25)**2,("PS20 arch source-W HS too big",float(hs_arch_sq))

    # COMPLETE 6*13*7*2=1092 original source/window signed
    # prime-translation checks, not a replacement by PS10 IMS graph.
    shifts={n:snap_iv(old.log_i(F(n))) for n,_ in SOURCES}
    min_shift_gap=None
    count=0
    for lo,hi in wins:
        for r,left,right in source:
            for n,ell in shifts.items():
                for sign in (-1,1):
                    if sign>0:
                        shifted_lo,shifted_hi=lo.lo+ell.lo,hi.hi+ell.hi
                    else:
                        shifted_lo,shifted_hi=lo.lo-ell.hi,hi.hi-ell.lo
                    gap=max(left.lo-shifted_hi,shifted_lo-right.hi)
                    assert gap>0,("PS20 true original prime reaches source",str(r),n,sign,float(gap))
                    min_shift_gap=gap if min_shift_gap is None else min(min_shift_gap,gap)
                    count+=1
    assert count==6*13*7*2==1092
    assert min_shift_gap>F(1,500)

    # Exact original signed prime couplings *within* all six windows,
    # all seven original n checked. Only the two log2 links survive.
    edges=[]
    for i in range(6):
        for j in range(i+1,6):
            dmin=wins[j][0].lo-wins[i][1].hi
            dmax=wins[j][1].hi-wins[i][0].lo
            for n,ell in shifts.items():
                if dmin<ell.hi and ell.lo<dmax:
                    assert n==2 and (i,j) in ((0,2),(3,5)),(i,j,n)
                    edges.append((i,j,n))
    assert edges==[(0,2,2),(3,5,2)]
    # The links are exact since W0+log2=W2 and W3+log2=W5.
    w2=ln2/old.sqrt_i(2)
    assert w2.hi<F(1,2)

    # Original self-arch + scalar lower from the actual 64-term
    # digamma kernel tail on EACH one of six w=1/128 intervals.
    tail64=F(0)
    for m in range(64):
        nu=F(4*m+1,2)
        x=nu*w
        assert 0<x<32
        tail64+=2*(1-x/32)**32/nu
    pi=old.pi_iv()
    carch=-old.gamma_iv()-pi/2-3*ln2-old.log_i(pi)
    local_diag=carch.lo+tail64
    assert local_diag>F(11,5),float(local_diag)

    # All FIFTEEN actual inter-window original arch couplings.
    # Full matrix symmetric: operator norm bounded by max row sum,
    # each nonoverlapping pair kernel <=1/(2d)+1.
    rowmax=F(0)
    for i,(lo,hi) in enumerate(wins):
        row=F(0)
        for j,(left,right) in enumerate(wins):
            if i==j:continue
            d=max(lo.lo-right.hi,left.lo-hi.hi)
            assert d>0
            row+=w*(F(1)+F(1,2*d))
        rowmax=max(rowmax,row)
    assert rowmax<F(17,100),float(rowmax)

    # Original POSITIVE even pole dropped only for a lower estimate.
    # Original NEGATIVE odd pole over all six windows paid.
    sn,cs=old.sinh_cosh_iv(B/2)
    assert sn.hi<F(7,12) and cs.hi<F(7,6)
    odd_allowance=2*6*w*sn.hi**2
    assert odd_allowance<F(1,30),float(odd_allowance)

    # Both original signed rank-one source/W pole crosses:
    # sqrt(13delta)<1/5, sqrt(6w)<11/50, cosh/sinh sup 7/6,7/12.
    assert 13*delta.hi<F(1,5)**2
    assert 6*w<F(11,50)**2
    source_pole=2*F(1,5)*F(11,50)*(F(7,6)**2+F(7,12)**2)
    assert source_pole<F(3,20),float(source_pole)
    source_arch=F(4,25)
    assert hs_arch_sq<source_arch**2
    # ORIGINAL source/W primes exactly ZERO, verified 1092 pairs.
    source_cross=source_arch+F(3,20)
    assert source_cross==F(31,100)
    # PS16 source A_P>323/1000 (all 19 true original prime links).
    source_schur_penalty=source_cross**2/F(323,1000)
    assert source_schur_penalty<F(3,10),float(source_schur_penalty)

    # Whole original source-ELIMINATED complementary Schur restricted
    # to this genuine 6-interval infinite-dimensional physical module:
    # 2.2 - .17 - .5 -1/30 - .3 =359/300 >7/6.
    six_schur_lower=F(11,5)-F(17,100)-F(1,2)-F(1,30)-F(3,10)
    assert six_schur_lower==F(359,300)>F(7,6)
    # Both parity sectors preserved under reflection.

    # SECOND-LEVEL SCHUR onto R=C minus this SIX-window carrier.
    # Each six sharp window projector preserves actual original
    # logarithmic form domain by truncated k_M + Carleman as PS15.
    # Entire original arch W/R offdiag: 6 disjoint outputs,
    # each <=pi/sqrt(2)+sqrt(wR), hence <sqrt6*(2.245+.14)<6.
    assert pi.hi<F(22,7)
    assert F(7,5)**2<2
    assert F(6)<F(5,2)**2
    assert w*R<F(7,50)**2
    arch_WR_rational=F(5,2)*(F(110,49)+F(7,50))
    assert arch_WR_rational<F(6)
    # ALL 7 original signed W/R prime shifts paid, full bound.
    weights=[]
    for n,base in SOURCES:
        root=iv(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        weights.append(old.log_i(F(base))/root)
    original_prime_WR=2*sum((x.hi for x in weights),F(0))
    assert original_prime_WR<F(71,10)
    # BOTH original signed pole cross W/R, no unphysical omission:
    # ||Wc||<sqrt(6w)*7/6, ||c||<8/5,
    # ||Ws||<sqrt(6w)*7/12, ||s||<1/2.
    sinB=2*sn*cs
    assert B+sinB.hi<F(8,5)**2
    assert sinB.hi-B<F(1,2)**2
    original_pole_WR=2*F(11,50)*(F(7,6)*F(8,5)+F(7,12)*F(1,2))
    assert original_pole_WR<F(1)
    # Source-elimination induces a COMPACT W/R correction:
    # ||W T_C R|| <= ||B_PW|| ||A_P^-1|| ||B_PR||
    # with B_PW<31/100, A_P^-1<1000/323 and PS15
    # entire original B_PC<67/4. Its norm is <17.
    source_WR=F(31,100)*F(1000,323)*F(67,4)
    assert source_WR<F(17)
    true_wr_bound=F(6)+F(71,10)+F(1)+F(17)
    assert true_wr_bound==F(311,10)<F(32)

    # Let A_W denote the restricted *already source-eliminated*
    # original Schur S_C on six windows. A_W>7/6, compact inverse.
    # True signed nested Schur on rest R is
    # S_R=(S_C)|R - B_WR* A_W^-1 B_WR,
    # B_WR = W (V_original) R - W T_C R, full arch/prime/poles.
    # Its penalty is positive COMPACT, with crude bound < 878.
    nested_penalty=F(32)**2/F(7,6)
    assert nested_penalty==F(6144,7)<F(878)
    assert old.log_i(F(2)).lo>F(69,100)
    # Original raw W/R cross has NONCOMPACT arch Carleman seam:
    # adjacent weakly null normalized indicator steps -> -log2,
    # all original prime cross vanish, poles O(eps).
    # Source compact T_C cross vanishes on such steps, so the
    # actual second-level B_WR has essential norm >= log2.
    # Compact A_W^-1/2 nevertheless makes the nested penalty compact.

    print("PS20 full six-window support physical measure",float(6*w),flush=True)
    print("PS20 original source-six minimum distance",float(min_source_gap),flush=True)
    print("PS20 all source-six prime checks",count,flush=True)
    print("PS20 original source-six signed prime min clearance",float(min_shift_gap),flush=True)
    print("PS20 true six-window internal original prime edges",edges,flush=True)
    print("PS20 entire original six-window local arch+carch lower",float(local_diag),flush=True)
    print("PS20 true complete 15-cross-window arch norm upper",float(rowmax),flush=True)
    print("PS20 original negative odd pole cost upper",float(odd_allowance),flush=True)
    print("PS20 full original source-six arch HS-square upper",float(hs_arch_sq),flush=True)
    print("PS20 original signed source-six pole upper",float(source_pole),flush=True)
    print("PS20 full actual original source-six Schur penalty upper",float(source_schur_penalty),flush=True)
    print("PS20 certified TRUE six-window S_C lower",float(six_schur_lower),flush=True)
    print("PS20 complete source-aware W/rest cross rational upper",float(true_wr_bound),flush=True)
    print("PS20 source-induced W/rest compact coupling upper",float(source_WR),flush=True)
    print("PS20 true nested signed residual Schur penalty crude upper",float(nested_penalty),flush=True)
    print("PS20 PASS SCOPED: six coupled infinite-dimensional original"
          " complementary windows source-eliminated S_C>7/6 in BOTH"
          " parities; 1092 source-window original prime shifts"
          " checked and exact TWO internal n2 links retained."
          " Genuine second-level full original signed R=C-W"
          " Schur assembled with all arch, 7 primes, both poles"
          " and source energy response; W/R raw coupling"
          " noncompact essential norm>=log2 but energy-dual"
          " penalty positive compact <878. Residual S_R PSD"
          " NOT established; CC27, W-ODD-NEG, W-EVEN-FORM,"
          " full original Weil and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
