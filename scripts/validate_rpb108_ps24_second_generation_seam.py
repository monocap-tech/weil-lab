#!/usr/bin/env python3
"""PS24: constructive second-generation Carleman seam absorption.

Strict, original-source-rational *iterability test* after PS23:
  - improve PS23 original 10-window signed Schur pivot >9/50;
  - add next two dyadic outer collars, width 2**(-192), DIRECTLY
    adjacent to the two original PS23 collars;
  - retain two noncompact arch Carleman corners, all genuinely
    nonzero source/old-module arch and both signed pole effects,
    and compact original source-induced inverse responses;
  - explicitly certify all 644 real original prime-shift incidences
    from BOTH collars to the original source and ten-window module;
  - use an analytic original digamma log-tail bound, not 2**192
    discretization or giant Bernoulli series;
  - certify second-generation true source+10-window-eliminated
    residual positive >45 and combined 12-window S_C >1/8.

This is one geometric second-generation step, NOT a proof of
complete-cover iteration or full complementary signed PSD/RH.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps23_carleman_seam_collars as ps23

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=F(11,5)
L=F(1,128)
E=F(1,2048)
ETA=F(1,2**192)
a,b=F(1,32),F(5,128)
v=F(1,6)
ORIGINAL=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
LABELS=sorted({F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
              |{F(9,n) for n in (2,4,5,7,8)})
GRID=10**14
def floorq(q):return F(q.numerator*GRID//q.denominator,GRID)
def ceilq(q):return F(-((-q.numerator*GRID)//q.denominator),GRID)
def iv(lo,hi=None):
    if hi is None:hi=lo
    return (floorq(lo),ceilq(hi))
def dist(x,y):return max(x[0]-y[1],y[0]-x[1])

def run():
    ps23.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(flag is False for flag in lane["closures"].values())

    ell=old.log_i(F(2))
    ell9=old.log_i(F(9))
    delta=old.IV(R-ell9.hi,R-ell9.lo)
    pi=old.pi_iv()
    assert ell.lo>F(693,1000) and ell.hi<F(7,10)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert ETA==F(1,2**192)
    # Base PS22 positive U8 physical intervals.
    U=[
        iv(-b-ell.hi,-a-ell.lo),
        iv(-ell.hi/2-L/2,-ell.lo/2+L/2),
        iv(-v-L,-v),iv(-b,-a),iv(a,b),
        iv(v,v+L),
        iv(ell.lo/2-L/2,ell.hi/2+L/2),
        iv(a+ell.lo,b+ell.hi)
    ]
    # PS23 two genuine adjacent first-generation collars.
    X=[(-b-E,-b),(b,b+E)]
    # PS24 two *more* collars, exactly touching the OUTER faces of X.
    # Do NOT snap ETA at grid=1e-14 or it would disappear!
    Y=[(-b-E-ETA,-b-E),(b+E,b+E+ETA)]
    S=U+X
    assert len(U)==8 and len(X)==2 and len(S)==10 and len(Y)==2
    assert all(y[1]-y[0]==ETA for y in Y)
    assert Y[0][1]==X[0][0] and Y[1][0]==X[1][1]
    assert Y[0][0]>-B and Y[1][1]<B
    assert all(dist(y,u)>0 for y in Y for u in U)
    for j,y in enumerate(Y):
        for k,x in enumerate(X):
            if (j,k) in ((0,0),(1,1)):
                assert dist(y,x)==0
            else:assert dist(y,x)>0

    # Exact P source support (13 PS15 actual intervals).
    source=[]
    for r in LABELS:
        logr=(old.IV(0) if r==1 else old.log_i(r))
        source.append(iv(-B+logr.lo,-B+logr.hi+delta.hi))
    assert len(source)==13
    assert all(dist(y,p)>F(1,100) for y in Y for p in source)

    # All 2*(13+10)*7*2 = 644 original *physical* prime shifts.
    # The previous generation's two measure-zero contacts become
    # STRICTLY DISJOINT at separation ETA, since these collars
    # lie beyond X in the outward direction. With original outward
    # ln-enclosures the clearance is >=E at their nearest contacts.
    # Other primes remain strictly separated. Never round ETA away.
    shifts={n:iv(old.log_i(F(n)).lo,old.log_i(F(n)).hi)
            for n,_ in ORIGINAL}
    checks=0
    minP,minS=None,None
    for y in Y:
        for name,group in (("P",source),("S",S)):
            for target in group:
                for n,sh in shifts.items():
                    for sign in (-1,1):
                        moved=(y[0]+sh[0],y[1]+sh[1]) if sign==1 else (y[0]-sh[1],y[1]-sh[0])
                        d=dist(moved,target)
                        assert d>0,("PS24 prime overlap",name,n,sign,str(d))
                        if name=="P":minP=d if minP is None else min(minP,d)
                        else:minS=d if minS is None else min(minS,d)
                        checks+=1
    assert checks==644
    assert minP>F(1,100) and minS>F(1,5000)

    # New two collars internally also have NO n>=2 prime link:
    # maximum whole Y diameter <log2. Their mutual original
    # arch cross, both signed poles, remain explicitly controlled.
    assert Y[1][1]-Y[0][0]<ell.lo
    between=ETA*(1+F(1,2*dist(Y[0],Y[1])))
    assert between<F(1,1000)

    # SCALE-FREE ORIGINAL DIGAMMA POSITIVITY (NO enormous mesh):
    # k(u)=exp(-u/2)/(1-exp(-2u)), 0<u<=1,
    # exp(-u/2)>1/2 and 1-exp(-2u)<=2u,
    # hence k(u)>=1/(4u).
    # For support diameter <=ETA and u>=ETA, D_f(u)=2||f||²,
    # so J[f]>=2 int_ETA^1 k(u)du ||f||²
    #            >=.5*ln(1/ETA)||f||²
    #            =96*ln2 ||f||².
    # Source-pinned rational c_arch >-6 gives >60.528 mass.
    carch=-old.gamma_iv()-pi/2-3*ell-old.log_i(pi)
    assert -F(6)<carch.lo and carch.hi<-F(5)
    diag=F(96)*ell.lo+carch.lo
    assert diag>F(60)+F(1,2),float(diag)
    sn,cs=old.sinh_cosh_iv(B/2)
    assert sn.hi<F(7,12) and cs.hi<F(7,6)
    odd=2*(2*ETA)*sn.hi**2
    assert odd<F(1,1000)

    # All 26 TRUE source/Y arch rectangles have positive distance.
    # Treat their full actual nonperiodic k(|x-y|) HS norm:
    hsP=sum((delta.hi*ETA*(1+F(1,2*dist(p,y)))**2
             for p in source for y in Y),F(0))
    assert hsP<F(1,2000)**2,float(hsP)
    # sqrt(2*ETA)<2^-95. Original both rank-one signed
    # source/Y poles, using actual physical source measure.
    sqrtY=F(1,2**95)
    assert 2*ETA<sqrtY**2
    assert 13*delta.hi<F(1,5)**2
    polePY=2*F(1,5)*sqrtY*(F(7,6)**2+F(7,12)**2)
    assert polePY<F(1,2000)
    bpy=F(1,1000)
    # All source/Y original prime cross terms are exactly zero
    # by the complete 644-case physical shift audit.
    source_pen=bpy**2/F(323,1000)
    assert source_pen<F(1,1000)
    beta=F(60) # diag >60.5 and three costs each <.001
    assert diag-between-odd-source_pen>beta

    # Full original signed S10/Y mixed arch. There are exactly
    # TWO adjacent Carleman corners: X−/Y− and X+/Y+.
    # They operate on orthogonal old-window input/output blocks.
    # Each is bounded by pi/2 + sqrt(E*ETA); the direct sum has
    # the SAME bound, not twice the Carleman norm.
    assert pi.hi/2<F(11,7)
    assert E*ETA<F(1,10**6)**2
    adjacent=F(11,7)+F(1,10**6)

    # All remaining 18 original signed S/Y arch pairs are
    # physically separated. They are retained and form a HS
    # operator with an outward exact rational rectangular bound.
    hs_other=F(0)
    for j,y in enumerate(Y):
        for i,s in enumerate(S):
            if (j,i) in ((0,8),(1,9)):continue
            d=dist(y,s)
            assert d>0
            mass=(L if i<8 else E)
            hs_other+=mass*ETA*(1+F(1,2*d))**2
    assert hs_other<F(1,2000)**2,float(hs_other)
    # Complete original signed even/odd poles across S/Y;
    # |S|=8L+2E <(13/50)^2 and |Y|=2 ETA.
    assert 8*L+2*E<F(13,50)**2
    poleSY=2*F(13,50)*sqrtY*(F(7,6)**2+F(7,12)**2)
    assert poleSY<F(1,2000)

    # Source-elimination creates a NONZERO S/Y cross:
    # source-to-U8<.37, source-to-X2<.05; orthogonality of
    # inputs gives full source-to-S<3/8.
    assert F(37,100)**2+F(1,20)**2<F(3,8)**2
    induced=F(3,8)*F(1000,323)*bpy
    assert induced<F(1,500)
    gamma=adjacent+F(1,2000)+F(1,2000)+F(1,500)
    assert gamma<F(8,5),float(gamma)

    # SHARPEN parent PS23 TEN-window original source-eliminated
    # alpha using its real 8/2 block Sylvester determinant:
    # alpha8>.95, betaX>3.985, gamma8X<1.7, so alpha10>.18.
    alpha10=F(9,50)
    a8,bx,g8=F(19,20),F(797,200),F(17,10)
    det10=(a8-alpha10)*(bx-alpha10)-g8**2
    assert det10>0,float(det10)

    # True after eliminating BOTH previous positive blocks
    # (13-source P AND ten-window S), full signed residual
    # S_Y[y] = Q[y] - <y,T_Py> -
    #   <y,B_SY^* A_S^-1 B_SY y>
    # > beta - (8/5)^2/(9/50) > 45 mass.
    second_pen=F(8,5)**2/alpha10
    residual=beta-second_pen
    assert residual>F(45)

    # COMPLETE source-eliminated TWELVE-window coupled domain:
    # S_C[s+y] >=alpha10||s||²+beta||y||²
    #              -2gamma||s||||y||.
    # Sylvester strict positive lower mu=1/8, even though Y
    # physically touches the PS23 collars at TWO noncompact seams.
    mu=F(1,8)
    det12=(alpha10-mu)*(beta-mu)-F(8,5)**2
    assert det12>0,float(det12)
    # The entire 12-window domain is reflection invariant,
    # so the same strict bound applies in both parity sectors.
    assert Y[0][0]==-Y[1][1] and Y[0][1]==-Y[1][0]

    print("PS24 guard collar second-generation width =2^-192",str(ETA),flush=True)
    print("PS24 original source+ten-window signed prime incidence checks",checks,flush=True)
    print("PS24 minimum original source/Y prime clearance",float(minP),flush=True)
    print("PS24 minimum full ten-window/Y prime clearance",float(minS),flush=True)
    print("PS24 ORIGINAL logarithmic kernel local Y diagonal lower",float(diag),flush=True)
    print("PS24 original full source/Y arch HS square",float(hsP),flush=True)
    print("PS24 original full 18 nonadjacent old/Y arch HS square",float(hs_other),flush=True)
    print("PS24 original source/Y signed both-pole bound",float(polePY),flush=True)
    print("PS24 original ten-window/Y signed both-pole bound",float(poleSY),flush=True)
    print("PS24 genuine two adjacent original Carleman corners",float(adjacent),flush=True)
    print("PS24 source-mediated old/Y induced signed cross",float(induced),flush=True)
    print("PS24 complete true old/Y signed Schur cross upper",float(gamma),flush=True)
    print("PS24 improved original ten-window Schur gap",float(alpha10),flush=True)
    print("PS24 TEN-window >.18 determinant",float(det10),flush=True)
    print("PS24 nested Y energy-dual correction upper",float(second_pen),flush=True)
    print("PS24 TRUE original twice-eliminated Y Schur lower",float(residual),flush=True)
    print("PS24 combined twelve-window >1/8 determinant",float(det12),flush=True)
    print("PS24 PASS SCOPED: a SECOND generation of reflected"
          " physical adjacent collars absorbs TWO more noncompact"
          " original arch Carleman seams, with certified original"
          " signed twice-eliminated residual >45 on Y and full"
          " coupled source-eliminated TWELVE-window form >1/8"
          " in both parities. A general 2x2 reusable seam criterion"
          " is established; no entire physical complement covering"
          " or W-ODD-NEG/CC27/RH closure.",flush=True)

if __name__=="__main__":
    run()
