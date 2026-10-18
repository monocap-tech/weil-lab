#!/usr/bin/env python3
"""PS21 original signed nested residual TWO-window coercivity + eight-window coupling.

Replay full pinned PS20 original physical SI10/CC27 signed seven-prime source.
Two reflected width-1/128 windows centered at +/- log(2)/2 lie in the true
PS20 uncovered complement. They have one REAL original log2 prime link.
All source-to-new and six-window-to-new prime shifts vanish by exact
interval arithmetic; all original arch + signed pole + source inverse
+ six-window inverse corrections remain paid. Source-eliminated true
six-plus-two coupled Schur is coercive in BOTH parity sectors.

No whole residual PSD, D-Riesz transfer, W-ODD-NEG/W-EVEN-FORM or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps20_sixwindow_nested_schur as ps20

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
L=F(1,128)
a,b=F(1,32),F(5,128)
v=F(1,6)
ORIGINAL=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
LABELS=sorted({F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
              |{F(9,n) for n in (2,4,5,7,8)})
GRID=10**15

def floorq(q):
    return F((q.numerator*GRID)//q.denominator,GRID)
def ceilq(q):
    return F(-((-q.numerator*GRID)//q.denominator),GRID)
def enc(lo,hi=None):
    if hi is None:hi=lo
    return (floorq(lo),ceilq(hi))
def sep(x,y):
    return max(x[0]-y[1],y[0]-x[1])
def arch_hsq(A,Z):
    # Full k(u)<=1+1/(2u), disjoint rectangles,
    # exact outward rational source-support envelope.
    return sum((lenA*lenZ*(1+F(1)/(2*sep(x,y)))**2
       for x,lenA in A for y,lenZ in Z),F(0))

def run():
    ps20.run()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT" and lane["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(v is False for v in lane["closures"].values())

    log2=old.log_i(F(2))
    log9=old.log_i(F(9))
    delta=old.IV(F(11,5)-log9.hi,F(11,5)-log9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    # Q+= [ell2/2-L/2,ell2/2+L/2], Q-=-Q+.
    # In the exact physical model Q- +ell2 = Q+;
    # this is a REAL nonzero signed n2 translation.
    Q=[
      enc(-log2.hi/2-L/2,-log2.lo/2+L/2),
      enc(log2.lo/2-L/2,log2.hi/2+L/2)
    ]
    assert Q[0][1]<0<Q[1][0]
    assert Q[0][0]>-B and Q[1][1]<B

    W=[
      enc(-b-log2.hi,-a-log2.lo),
      enc(-v-L,-v),
      enc(-b,-a),enc(a,b),
      enc(v,v+L),
      enc(a+log2.lo,b+log2.hi)
    ]
    assert len(W)==6
    assert all(W[i][1]<W[i+1][0] for i in range(5))
    assert all(sep(q,x)>F(1,8) for q in Q for x in W)
    source=[]
    for r in LABELS:
        ell=(old.IV(0) if r==1 else old.log_i(r))
        source.append(enc(-B+ell.lo,-B+ell.hi+delta.hi))
    assert len(source)==13
    assert all(sep(q,x)>F(1,20) for q in Q for x in source)

    # Every 2*13*7*2 original source-to-Q prime possibility,
    # plus every 2*6*7*2 existing-module-to-Q prime possibility,
    # is checked with outward interval bounds. No invented zero
    # correlation where physical shifted supports overlap.
    logs={n:enc(old.log_i(F(n)).lo,old.log_i(F(n)).hi)
          for n,_ in ORIGINAL}
    shift_checks=0
    minP,minW=None,None
    for qs in Q:
        for grp,which in ((source,"P"),(W,"W")):
            for orig in grp:
                for n,ell in logs.items():
                    for sign in (-1,1):
                        moved=(enc(qs[0]+ell[0],qs[1]+ell[1])
                              if sign>0 else
                              enc(qs[0]-ell[1],qs[1]-ell[0]))
                        d=sep(moved,orig)
                        assert d>0,(which,"prime overlap",n,sign,str(d))
                        if which=="P":
                            minP=d if minP is None else min(minP,d)
                        else:
                            minW=d if minW is None else min(minW,d)
                        shift_checks+=1
    assert shift_checks==2*(13+6)*7*2==532
    assert minP>F(1,20) and minW>F(1,100)

    # Exact n2 signed link between the reflected new windows:
    # left+log2=right, while n=3,4,5,7,8,9 have no internal links.
    assert 2*(log2.lo/2-L/2)<log2.lo
    assert Q[1][0]-Q[0][1]<log2.hi
    assert Q[1][1]-Q[0][0]>log2.lo
    for n,ell in logs.items():
        if n==2:continue
        assert sep(enc(Q[0][0]+ell[0],Q[0][1]+ell[1]),Q[1])>0
    w2=log2/old.sqrt_i(2)
    assert w2.hi<F(1,2)

    # Actual original 64-term digamma tail (not a model kernel)
    # is uniform on any admissible width L short-support piece.
    arch64=F(0)
    for j in range(64):
        nu=F(4*j+1,2)
        x=nu*L
        assert 0<x<32
        arch64+=2*(1-x/32)**32/nu
    pi=old.pi_iv()
    carch=-old.gamma_iv()-pi/2-3*log2-old.log_i(pi)
    actual_local=arch64+carch.lo
    assert actual_local>F(11,5),float(actual_local)

    # True original inter-Q arch interaction (one separated pair).
    arch_internal=L*(1+F(1)/(2*sep(Q[0],Q[1])))
    assert arch_internal<F(1,70),float(arch_internal)
    sn,cs=old.sinh_cosh_iv(B/2)
    assert sn.hi<F(7,12) and cs.hi<F(7,6)
    odd_allow=2*(2*L)*sn.hi**2
    assert odd_allow<F(1,80),float(odd_allow)

    # Full 26 source/Q arch kernel distance-summed HS and both
    # original signed pole source crosses. Exact true 13-source
    # Schur positive A_P > 323/1000 (PS16), not a surrogate.
    P=[(x,delta.hi) for x in source]
    T=[(x,L) for x in Q]
    hsP=arch_hsq(P,T)
    assert hsP<F(11,100)**2,float(hsP)
    assert 13*delta.hi<F(1,5)**2
    # sqrt support(Q)=sqrt(2L)=1/8
    source_pole=2*F(1,5)*F(1,8)*(F(7,6)**2+F(7,12)**2)
    assert source_pole<F(9,100)
    pqcross=F(11,100)+F(9,100)
    assert pqcross==F(1,5)
    p_pen=pqcross**2/F(323,1000)
    assert p_pen<F(1,8),float(p_pen)

    # Full 12 W/Q arch kernels and two signed original pole
    # W/Q crosses; W/Q true PRIME cross verified identically 0.
    hsW=arch_hsq([(x,L) for x in W],T)
    assert hsW<F(1,14)**2,float(hsW)
    assert 6*L<F(11,50)**2
    w_pole=2*F(11,50)*F(1,8)*(F(7,6)**2+F(7,12)**2)
    assert w_pole<F(1,10),float(w_pole)

    # Source elimination creates NONZERO signed W/Q cross:
    # ||W T_C Q||< ||B_PW|| ||A_P^-1|| ||B_PQ||.
    # No false prime cross and no false omission of source inverse.
    source_induced=F(31,100)*F(1000,323)*pqcross
    wrbound=F(1,14)+F(1,10)+source_induced
    assert wrbound<F(3,8),float(wrbound)
    # True already-source-eliminated A_W >7/6 from PS20.
    nested_pen=F(3,8)**2/F(7,6)
    assert nested_pen==F(27,224)<F(121,1000)

    # Whole original signed second-level Schur on Q after
    # eliminating both POSITIVE source P and POSITIVE old W:
    actual_second_margin=(F(11,5)-F(1,2)-F(1,70)-F(1,80)
                          -F(1,8)-nested_pen)
    assert actual_second_margin>F(7,5),float(actual_second_margin)

    # The full source-ELIMINATED signed Schur on W+Q includes
    # ALL nonzero W/Q arch/pole/source-mediated cross, NOT
    # direct prime (geometrically absent). Completing square gives
    # S_C[w+q] = ||A_W^1/2(w+A_W^-1 Bq)||²+S_R[q].
    # ||A_W^-1 B|| <(6/7)*(3/8)=9/28.
    # Invertible triangular map norm <1+9/28=37/28.
    # With A_W>7/6 and S_R|Q>7/5, uniform eight-window
    # source-eliminated margin > (7/6)*(28/37)^2 >2/3.
    eight_lower=F(7,6)*(F(28,37))**2
    assert eight_lower>F(2,3),float(eight_lower)

    print("PS21 physical new reflected Q interval width",float(L),flush=True)
    print("PS21 source/W original prime shift checks",shift_checks,flush=True)
    print("PS21 source prime minimum clearance",float(minP),flush=True)
    print("PS21 W prime minimum clearance",float(minW),flush=True)
    print("PS21 true internal n2 signed prime upper",float(w2.hi),flush=True)
    print("PS21 original two-window arch+carch local lower",float(actual_local),flush=True)
    print("PS21 original two-window mutual arch upper",float(arch_internal),flush=True)
    print("PS21 source/Q arch HS square upper",float(hsP),flush=True)
    print("PS21 six-window/Q arch HS square upper",float(hsW),flush=True)
    print("PS21 source/Q all signed pole upper",float(source_pole),flush=True)
    print("PS21 six-window/Q all signed pole upper",float(w_pole),flush=True)
    print("PS21 true source Schur two-window subtraction upper",float(p_pen),flush=True)
    print("PS21 true W/Q source-mediated cross upper",float(source_induced),flush=True)
    print("PS21 source-adjusted W/Q cross norm upper",float(wrbound),flush=True)
    print("PS21 full nested six-window Schur penalty upper",float(nested_pen),flush=True)
    print("PS21 true second-level ORIGINAL signed residual Q lower",float(actual_second_margin),flush=True)
    print("PS21 eight-window coupled original source Schur uniform lower",float(eight_lower),flush=True)
    print("PS21 PASS SCOPED: source-eliminated original signed"
          " eight-window S_C>2/3 on INFINITE DIMENSIONAL"
          " reflection-symmetric carrier with THREE true n2 links,"
          " nested residual S_R>7/5 on a real two-window"
          " prime-linked subspace after two genuine positive"
          " eliminations and full arch/poles/source response."
          " Whole residual PSD, native CC27 D-Riesz bridge,"
          " W-ODD-NEG, W-EVEN-FORM and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
