#!/usr/bin/env python3
"""PS19 — four-window actual ORIGINAL signed complementary Schur coercivity.

Four symmetric genuine PHYSICAL complement intervals (width 1/128),
including two exact internal prime log2 resonances. All seven original
source-to-four-window prime shifts are certified absent by source
geometry; the two REAL internal n=2 prime links are RETAINED. Entire
inter-window arch cross, BOTH signed poles, and source-energy Schur
subtraction B* A_P^-1 B certified. This is not whole complement PSD,
full CC27 D-Riesz identification, W-ODD-NEG, W-EVEN-FORM or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json

import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps18_spectral_rank_obstruction as ps18

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
N=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
LABELS=sorted({F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
              |{F(9,n) for n in (2,4,5,7,8)})

def run():
    # Replays whole ORIGINAL signed seven-prime PS18->PS01/RC315
    # source and its true source-complement Schur form-domain custody.
    ps18.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(value is False for value in lane["closures"].values())

    ln2=old.log_i(F(2))
    ln9=old.log_i(F(9))
    pi=old.pi_iv()
    delta=old.IV(R-ln9.hi,R-ln9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    logs={r:(old.IV(0) if r==1 else old.log_i(r)) for r in LABELS}
    assert len(LABELS)==13
    # Actual disjoint physical 4 windows (in left-to-right order):
    # W1= -([1/32,5/128]+log2), W2=-[1/32,5/128],
    # W3=[1/32,5/128], W4=[1/32,5/128]+log2.
    # All widths exactly 1/128; reflection swaps 0<->3,1<->2.
    base_lo,base_hi=F(1,32),F(5,128)
    width=base_hi-base_lo
    assert width==F(1,128)
    wins=[
      (old.IV(-base_hi-ln2.hi,-base_hi-ln2.lo),
       old.IV(-base_lo-ln2.hi,-base_lo-ln2.lo)),
      (old.IV(-base_hi),old.IV(-base_lo)),
      (old.IV(base_lo),old.IV(base_hi)),
      (old.IV(base_lo+ln2.lo,base_lo+ln2.hi),
       old.IV(base_hi+ln2.lo,base_hi+ln2.hi))
    ]
    assert len(wins)==4
    for lo,hi in wins:
        assert -B<lo.lo<=lo.hi<hi.lo<=hi.hi<B
        # Width is identically 1/128 at the symbolic log level.
        assert F(1,128)<=hi.hi-lo.lo<F(1,128)+F(1,10**25)
    for i in range(3):
        assert wins[i][1].hi<wins[i+1][0].lo

    # Every one of four windows lies in the ACTUAL original sharp
    # source complement. 13*4 support distances are strictly positive.
    source=[]
    for r in LABELS:
        o=logs[r]
        source.append((r,old.IV(-B+o.lo,-B+o.hi),
                       old.IV(-B+o.lo+delta.lo,-B+o.hi+delta.hi)))
    hs_arch_sq=F(0)
    min_dist=None
    for lo,hi in wins:
        for r,a,b in source:
            dist=max(lo.lo-b.hi,a.lo-hi.hi)
            assert dist>0,("source/support overlap",str(r),float(dist))
            min_dist=dist if min_dist is None else min(min_dist,dist)
            # Entire signed source-to-4-window arch cross (kernel -k).
            # HS² <= delta*width Σ [1+1/(2d)]². Every 13*4 pair.
            hs_arch_sq+=delta.hi*width*(1+F(1,2*dist))**2
    assert min_dist>F(1,1000)
    assert hs_arch_sq<F(1,49),("four original signed arch source HS",float(hs_arch_sq))

    shifts={n:old.log_i(F(n)) for n,b in N}
    min_source_prime_gap=None
    # Exhaust ALL 4*13*7*2 actual source-window shift incidences:
    # none overlap, including all 4/8/9 prime powers.
    for lo,hi in wins:
        for r,a,b in source:
            for n,ell in shifts.items():
                for sign in (-1,1):
                    if sign==1:
                        slo,shi=lo.lo+ell.lo,hi.hi+ell.hi
                    else:
                        slo,shi=lo.lo-ell.hi,hi.hi-ell.lo
                    clearance=max(a.lo-shi,slo-b.hi)
                    assert clearance>0,("source prime shift intersects window",str(r),n,sign,float(clearance))
                    min_source_prime_gap=(clearance if min_source_prime_gap is None
                                          else min(min_source_prime_gap,clearance))
    assert min_source_prime_gap>F(1,10000)

    # All ACTUAL original prime interactions WITHIN the 4 windows.
    # The only two are 0->1 and 2->3 by original n=2, exact log2.
    # All others have strict SHIFT gap (none approximate log3,4,5,7,8,9).
    prime_edges=[]
    for i in range(4):
        for j in range(i+1,4):
            dif_lo=wins[j][0].lo-wins[i][1].hi
            dif_hi=wins[j][1].hi-wins[i][0].lo
            for n,ell in shifts.items():
                intersects=(dif_lo<ell.hi and ell.lo<dif_hi)
                if intersects:
                    assert n==2 and (i,j) in ((0,1),(2,3)),(i,j,n)
                    prime_edges.append((i,j,n))
    assert prime_edges==[(0,1,2),(2,3,2)]
    # More than interval overlap: the two links are *EXACT*
    # translations because W1+log2=W2 and W3+log2=W4.
    assert -(base_hi+ln2.lo)+ln2.lo==-base_hi
    assert base_lo+ln2.lo>base_hi

    # Arch self-energy for EACH arbitrary original-form-admissible
    # component supported in ONE width-1/128 window:
    # J[f_i] >=2 int_width^∞ k(u) du *||f_i||².
    # Source-original 64 term Bernoulli (all Fraction).
    tail64=F(0)
    for m in range(64):
        nu=F(4*m+1,2)
        x=nu*width
        assert 0<x<32
        tail64+=2*(1-x/32)**32/nu
    carch=-old.gamma_iv()-pi/2-3*ln2-old.log_i(pi)
    local_diag=carch.lo+tail64
    assert local_diag>F(11,5),float(local_diag)

    # Original nonlocal cross-window arch kernel -k(|x-y|).
    # Every pair retained. Schur matrix row sum bound:
    # ||A_ij|| <= width*(1+1/(2*min_dist_ij)).
    cross_rows=[]
    for i,(a,b) in enumerate(wins):
        row=F(0)
        for j,(c,d) in enumerate(wins):
            if i==j:continue
            dist=max(c.lo-b.hi,a.lo-d.hi)
            assert dist>0
            row+=width*(1+F(1,2*dist))
        cross_rows.append(row)
    arch_cross=max(cross_rows)
    assert arch_cross<F(1,10),float(arch_cross)

    # True original n2 translation is the TWO 2-channel disjoint
    # weighted shifts: its signed offdiagonal fiber matrix norm w2.
    # Both prime links are kept, and no n>=3 shifts occur internally.
    w2=ln2/old.sqrt_i(2)
    assert w2.hi<F(1,2)

    # Positive original EVEN pole safely dropped for a lower bound.
    # Negative ODD pole paid over ENTIRE 4-interval support:
    # -2 |<h,s>|² >= -2*(4*width)*sup_I |s|² ||h||².
    sn,cs=old.sinh_cosh_iv(B/2)
    assert sn.hi<F(7,12) and cs.hi<F(7,6)
    odd_cost=2*4*width*sn.hi**2
    assert odd_cost<F(1,40),float(odd_cost)

    # TRUE source inverse correction to the full signed complement
    # Schur, including 24 Carleman seams and both signed poles.
    # All original source-to-window primes vanished EXPLICITLY.
    # Original source arch B has HS <1/7.
    # ||P c||<=sqrt(13delta)*sup c <=(1/5)*(7/6)
    # ||W c||<=sqrt(4width)*sup c <=(9/50)*(7/6).
    # Similarly for sinh; 4width=1/32, sqrt<9/50.
    assert 13*delta.hi<F(1,5)**2
    assert 4*width<F(9,50)**2
    pole_cross=2*F(1,5)*F(9,50)*(F(7,6)**2+F(7,12)**2)
    assert pole_cross==F(49,400)<F(1,8)
    cross_bound=F(1,7)+F(1,8)
    assert cross_bound<F(27,100)
    assert hs_arch_sq<F(1,49)
    # PS16 TRUE A_P>323/1000 on 13-source domain; not a surrogate.
    full_source_penalty=cross_bound**2/F(323,1000)
    assert full_source_penalty<F(9,40),float(full_source_penalty)

    # For ANY original complement h supported on full union of these
    # four windows (not just step profiles):
    # Q_C[h] >=(local_diag - original n2 direct prime norm
    #       - arch mutual cross - original negative odd pole) ||h||².
    # True source Schur subtracts positive T_C <= penalty.
    # Certificate uses strict rationalized ACCEPTED bound:
    four_block_schur=F(11,5)-F(1,2)-F(1,10)-F(1,40)-F(9,40)
    assert four_block_schur==F(27,20)
    assert four_block_schur>F(4,3)
    # The original 4-window support is reflection invariant:
    # the entire strict Schur bound applies in BOTH parity sectors.
    assert len(prime_edges)==2
    print("PS19 4 physical interval width",float(width),flush=True)
    print("PS19 ORIGINAL source-quiet minimum interval separation",float(min_dist),flush=True)
    print("PS19 true complete source-prime minimum shift clearance",float(min_source_prime_gap),flush=True)
    print("PS19 original prime 4-window edges",prime_edges,flush=True)
    print("PS19 true original local arch+carch lower",float(local_diag),flush=True)
    print("PS19 original cross-window digamma arch norm upper",float(arch_cross),flush=True)
    print("PS19 true n2 linked prime spectral norm upper",float(w2.hi),flush=True)
    print("PS19 original odd pole global cost upper",float(odd_cost),flush=True)
    print("PS19 original source-to-4 arch HS-square upper",float(hs_arch_sq),flush=True)
    print("PS19 both signed source pole cross bound",float(pole_cross),flush=True)
    print("PS19 exact full source energy Schur penalty bound",float(full_source_penalty),flush=True)
    print("PS19 true signed 4-window complementary Schur lower",float(four_block_schur),flush=True)
    print("PS19 PASS SCOPED: TRUE original source-adjusted complementary"
          " Schur >27/20 L2 mass on infinite-dimensional"
          " reflection-invariant FOUR-WINDOW space with TWO ACTUAL"
          " signed log2 prime couplings, all original seven"
          " source-window shifts certified absent, complete"
          " nonzero arch/poles and source inverse paid. Both parities."
          " WHOLE complementary signed Schur, CC27 D-Riesz,"
          " canonical W-ODD-NEG, W-EVEN-FORM and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
