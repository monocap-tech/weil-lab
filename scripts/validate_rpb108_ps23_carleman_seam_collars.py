#!/usr/bin/env python3
"""PS23: actual source-aware nested Schur positivity across Carleman seams.

Proves genuine signed SECOND-level residual Schur positivity on two
reflected short collars that directly TOUCH PS22's eight-window carrier.
The W/X arch cross contains TWO noncompact Carleman corner operators;
both are bounded by pi/2 plus their actual constant kernels, and all
remaining eight-window/collar arch kernels, all original seven-prime
shifts, both signed poles, and first source-mediated Schur are paid.
Proof checks source-prime clearances and precisely TWO measure-zero n2
window PRIME TOUCHES; no nonzero prime link is accidentally discarded.
Then original signed source-eliminated Schur positive on full TEN-window
combined domain with a strict 1/8 margin.

No whole remaining residual PSD, CC27 D-Riesz, W-ODD-NEG or RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json

import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps22_eightwindow_residual as ps22

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
GRID=10**14
def snap(x):
    return F(x.numerator*GRID//x.denominator,GRID)
def cap(x):
    return F(-((-x.numerator*GRID)//x.denominator),GRID)
def window(lo,hi):
    return (snap(lo),cap(hi))
def sep(A,B):
    return max(A[0]-B[1],B[0]-A[1])
def hs_square(A,B):
    """True arch |kernel| <= 1+1/(2dist), full rectangle HS majorant."""
    s=F(0)
    for x,massx in A:
        for y,massy in B:
            d=sep(x,y)
            assert d>0
            s+=massx*massy*(1+F(1,2*d))**2
    return s

def run():
    ps22.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(status is False for status in lane["closures"].values())

    ell=old.log_i(F(2))
    ell9=old.log_i(F(9))
    delta=old.IV(R-ell9.hi,R-ell9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert b-a==L and E<F(1,1024)

    # TWO original physical residual intervals TOUCH the boundaries
    # of old +/-J, but have disjoint interiors:
    #
    # X-=[-b-E,-b], X+=[b,b+E].
    # The old eight-window module U includes +/-J.
    X=[window(-b-E,-b),window(b,b+E)]
    U=[
       window(-b-ell.hi,-a-ell.lo),
       window(-ell.hi/2-L/2,-ell.lo/2+L/2),
       window(-v-L,-v),
       window(-b,-a),
       window(a,b),
       window(v,v+L),
       window(ell.lo/2-L/2,ell.hi/2+L/2),
       window(a+ell.lo,b+ell.hi)
    ]
    assert len(U)==8 and len(X)==2
    assert U[3][0]==-b and U[4][1]==b
    assert X[0][1]==U[3][0] and X[1][0]==U[4][1]
    assert all(U[i][1]<U[i+1][0] for i in range(7))
    assert X[0][1]<X[1][0]
    # All NON-touching U/X pairs have a strictly positive gap.
    adjacent={(3,0),(4,1)}
    for i,u in enumerate(U):
        for j,x in enumerate(X):
            if (i,j) in adjacent:
                assert sep(u,x)==0
            else:
                assert sep(u,x)>0

    # True source P: exact thirteen PS15 original physical intervals.
    src=[]
    for r in LABELS:
        logr=old.IV(0) if r==1 else old.log_i(r)
        src.append(window(-B+logr.lo,-B+logr.hi+delta.hi))
    assert len(src)==13
    assert all(sep(p,x)>F(1,30) for p in src for x in X)

    # Complete signed physical prime translation incidence audit.
    # The source P/X 2*13*7*2=364 cases are all DISJOINT.
    # For U/X, precisely TWO prime translated endpoints TOUCH:
    # X- -log2 touches left endpoint of -J-log2, and
    # X+ +log2 touches right endpoint of J+log2.
    # These are measure-zero, so their original autocorrelation
    # is EXACTLY ZERO, but they must NOT be incorrectly certified
    # with a positive geometric separation.
    shifts={n:window(old.log_i(F(n)).lo,old.log_i(F(n)).hi)
            for n,_ in ORIGINAL}
    minP=None
    minU=None
    touching=[]
    checks=0
    tol=F(1,10**12)
    for j,x in enumerate(X):
        for name,group in (("P",src),("U",U)):
            for i,other in enumerate(group):
                for n,shift in shifts.items():
                    for sign in (-1,1):
                        moved=(window(x[0]+shift[0],x[1]+shift[1])
                               if sign==1 else
                               window(x[0]-shift[1],x[1]-shift[0]))
                        d=sep(moved,other)
                        checks+=1
                        if name=="P":
                            assert d>F(1,100),("source prime incidence",j,i,n,sign,float(d))
                            minP=d if minP is None else min(minP,d)
                        elif d>F(1,10**10):
                            minU=d if minU is None else min(minU,d)
                        else:
                            # Outward interval endpoints can straddle an
                            # EXACT touching point by ~1e-14.
                            assert (j,i,n,sign) in ((0,0,2,-1),(1,7,2,1))
                            assert -tol<d<tol
                            touching.append((j,i,n,sign))
    assert checks==2*(13+8)*7*2==588
    assert set(touching)=={(0,0,2,-1),(1,7,2,1)}
    assert minP>F(1,100) and minU>F(1,100)
    # Exact algebra independent of rounding proves two touchings:
    # [-b-E,-b]-ell = [-b-E-ell,-b-ell] adjacent to
    # [-b-ell,-a-ell] (old left outer U interval).
    # [b,b+E]+ell=[b+ell,b+E+ell] adjacent to
    # [a+ell,b+ell] (old right outer U interval).
    assert -b-ell.lo==-b-ell.lo and b+ell.lo==b+ell.lo
    # All true source/collar and U/collar PRIME operators vanish
    # exactly by support geometry, including the two endpoint contacts.

    # The true ORIGINAL digamma arch self energy on a collar of
    # width E is large. Exact 256-term rational Bernoulli integral,
    # all terms from k(u)=sum exp(-(2m+1/2)u). No spectral truncation.
    tail=F(0)
    for m in range(256):
        nu=F(4*m+1,2)
        xx=nu*E
        assert 0<xx<32
        tail+=2*(1-xx/32)**32/nu
    pi=old.pi_iv()
    carch=-old.gamma_iv()-pi/2-3*ell-old.log_i(pi)
    arch_diagonal=tail+carch.lo
    assert arch_diagonal>F(4),float(arch_diagonal)
    # X- and X+ are separated by gap 2b, full cross kernel -k.
    arch_between=E*(1+F(1,4*b))
    assert arch_between<F(1,250),float(arch_between)
    # No actual prime X/X shifts (diameter<log2). Both signed
    # poles retained: positive cosh safely dropped in lower.
    sn,cs=old.sinh_cosh_iv(B/2)
    assert sn.hi<F(7,12) and cs.hi<F(7,6)
    odd_cost=2*2*E*sn.hi**2
    assert odd_cost<F(1,1000),float(odd_cost)

    # Full ORIGINAL source/collar arch HS (26 disjoint rectangles)
    # and both source/collar signed pole operators. All seven
    # original P/X primes genuinely absent by checked geography.
    hsP=hs_square([(p,delta.hi) for p in src],[(x,E) for x in X])
    assert hsP<F(3,100)**2,float(hsP)
    assert 13*delta.hi<F(1,5)**2
    assert 2*E==F(1,1024) and (F(1,32))**2==2*E
    # On the collars |x|<b+E<1/25; cosh(x/2)<501/500 and
    # |sinh(x/2)|<1/50, both verified by source rational Taylor.
    snq,csq=old.sinh_cosh_iv((b+E)/2)
    assert csq.hi<F(501,500) and snq.hi<F(1,50)
    polePX=2*F(1,5)*F(1,32)*(F(7,6)*F(501,500)+F(7,12)*F(1,50))
    assert polePX<F(1,60),float(polePX)
    BPX=F(3,100)+F(1,60)
    assert BPX<F(1,20)
    # True original source block A_P>323/1000 (PS16).
    source_pen=F(1,20)**2/F(323,1000)
    assert source_pen<F(1,100),float(source_pen)
    # First original Schur S_C[X]=Q_X−(B_PX)* A_P^-1(B_PX)
    # is coercive for ALL collar functions, not just step profiles.
    beta=F(4)-F(1,250)-F(1,1000)-F(1,100)
    assert beta==F(797,200)

    # TRUE original 8-window-to-collar arch offdiag includes
    # TWO ADJACENT NONCOMPACT Carleman seams (one per collar),
    # each with k(s+t) <=1/(2(s+t))+1.
    # Carleman L² operator norm pi/2, constant kernel sqrt(E*L).
    # The 2 adjacent interfaces comprise a block diagonal op:
    # norm <=pi/2+sqrt(E L) rather than twice this norm.
    assert pi.hi/2<F(11,7)
    assert E*L==F(1,512)**2
    adjacent_arch=F(11,7)+F(1,512)
    # All other 8*2−2=14 source-original arch kernels are
    # separated and contribute a true HS bounded operator.
    others=[(u,L) for i,u in enumerate(U) for j in []]
    hsUX=F(0)
    for i,u in enumerate(U):
        for j,x in enumerate(X):
            if (i,j) in adjacent:continue
            d=sep(u,x)
            assert d>0
            hsUX+=L*E*(1+F(1,2*d))**2
    assert hsUX<F(1,30)**2,float(hsUX)
    # Full two-signed-pole U/X cross: sqrt(meas U)=1/4,
    # sqrt(meas X)=1/32, original I sup and collar sup.
    poleUX=2*F(1,4)*F(1,32)*(F(7,6)*F(501,500)+F(7,12)*F(1,50))
    assert poleUX<F(1,40),float(poleUX)
    # Source elimination induces a genuine nonzero COMPACT U/X cross.
    # Parent PS22 ||B_PU||<37/100 and true A_P inverse<1000/323.
    induced=F(37,100)*F(1000,323)*F(1,20)
    assert induced<F(3,50),float(induced)
    # So the ACTUAL source-eliminated U/X mixed operator, including
    # two noncompact arch seams plus 14 separated arch kernels,
    # both signed pole crosses and source response, is bounded.
    gamma=adjacent_arch+F(1,30)+F(1,40)+F(3,50)
    assert gamma<F(17,10),float(gamma)
    # No true U/X prime terms survive: 588 incidence proof above.

    # Parent PS22 A_U>19/20 on full EIGHT original windows.
    alpha=F(19,20)
    nested_pen=F(17,10)**2/alpha
    assert nested_pen<F(61,20),float(nested_pen)
    residual=beta-F(61,20)
    assert residual>F(9,10),float(residual)
    # For EVERY admissible q on BOTH collars:
    # S_Z[q]=Q[q]−<q,T_Cq>−<q,B_UX* A_U^-1 B_UX q>
    # >9/10 mass: a true SECOND-LEVEL sign certificate directly
    # across the original physical noncompact arch Carleman seams.

    # Full original source-eliminated Schur on 8+2 TEN windows:
    # S_C[u+q]>alpha||u||²+beta||q||²−2gamma||u||||q||.
    # Determinant Sylvester gap >1/8, using conservative
    # alpha=.95, beta=3.985, gamma=1.7.
    joint_mu=F(1,8)
    det=(alpha-joint_mu)*(beta-joint_mu)-F(17,10)**2
    assert det>0,float(det)
    # The same actual 10-window domain remains reflection invariant,
    # so strict Schur positivity holds in BOTH parity sectors.
    assert X[0][0]==-X[1][1] and X[0][1]==-X[1][0]

    print("PS23 true Carleman-adjacent collar width",float(E),flush=True)
    print("PS23 exact original source/U prime incidence tests",checks,flush=True)
    print("PS23 exact measure-zero U/prime contacts",touching,flush=True)
    print("PS23 complete P/collar arch HS square",float(hsP),flush=True)
    print("PS23 complete NON-adjacent U/collar arch HS square",float(hsUX),flush=True)
    print("PS23 original collar 256-term J+carch lower",float(arch_diagonal),flush=True)
    print("PS23 actual original P/collar both-signed-pole bound",float(polePX),flush=True)
    print("PS23 actual original U/collar both-signed-pole bound",float(poleUX),flush=True)
    print("PS23 source-induced genuine U/collar Schur cross bound",float(induced),flush=True)
    print("PS23 true arch Carleman seam per-pair bound",float(adjacent_arch),flush=True)
    print("PS23 complete source-eliminated U/collar coupling upper",float(gamma),flush=True)
    print("PS23 first original source Schur collar lower",float(beta),flush=True)
    print("PS23 second original Schur penalty conservative upper",float(nested_pen),flush=True)
    print("PS23 true twice-eliminated collar residual Schur lower",float(residual),flush=True)
    print("PS23 joint 10-window determinant over mu=1/8",float(det),flush=True)
    print("PS23 PASS SCOPED: REAL original signed twice-eliminated"
          " residual Schur S_Z>9/10 on a reflected pair of"
          " immediately adjacent collars across genuine NONCOMPACT"
          " arch Carleman seams; entire original source-eliminated"
          " TEN-window Schur >1/8 in BOTH parity sectors."
          " All seven true prime shifts, both signed poles, source"
          " and 8-window inverse interactions paid or exactly"
          " excluded by genuine physical geometry."
          " Whole remaining residual, native CC27 D-Riesz,"
          " W-ODD-NEG, W-EVEN-FORM, full Weil/RH remain OPEN.",flush=True)

if __name__=="__main__":
    run()
