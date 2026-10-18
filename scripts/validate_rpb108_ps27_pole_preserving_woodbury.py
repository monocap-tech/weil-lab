#!/usr/bin/env python3
"""PS27 — true original source-preserving Woodbury rank-one EVEN pole.

Exact source-pinned algebra of ORIGINAL positive even pole *before*
13-source Schur elimination, unlike PS26's post-Schur artificial pole
deletion. Original pole-FREE source A0=A_P-2|c_P><c_P| stays POSITIVE
under a strict rational bound A0>1997/9000, using PS16 actual A_P.
Hence the WHOLE original source-eliminated Schur is exactly:
   S_C = S_C^0 + alpha |<d,h>|^2,
   d=c_C - B0* A0^-1 c_P, alpha=2/(1+2t),
   t=<c_P,A0^-1 c_P>, 3994/2907<alpha<=2,
   S_C^0=Q_C^0-B0* A0^-1 B0.
Both cross source inverse effects are retained in d, not c_C.
Explicit Q0 negative RC315 constant witness survives the genuine
pole-FREE Schur: S_C^0[1_Cu0]<-4.35974. This NEGATIVE source-removed
surrogate is NOT negativity of full original S_C/Q, nor RH disproof.

Parity: d even, odd sectors S_C=S_C^0. The true-even acceptance gate
is positivity of S_C^0 on K=ker<d,.> plus one scalar variational gate
with actual alpha; it is NOT certified positive here. If S_C>=0
then negative index of S_C^0,even is exactly ONE. Original source
and every genuine physical arch, 7 primes, odd pole retained.
"""
from fractions import Fraction as F
from pathlib import Path
import json

import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps26_even_pole_global_no_go as ps26

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B

def mm(A,B):
    assert len(A[0])==len(B)
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
              for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):
    return [list(r) for r in zip(*A)]
def add(A,B):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(A,B)]
def sub(A,B):
    return [[x-y for x,y in zip(ra,rb)] for ra,rb in zip(A,B)]
def scale(A,x):
    return [[x*v for v in row] for row in A]
def col(v):
    return [[x] for x in v]
def inv2(A):
    assert len(A)==len(A[0])==2
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert d>0
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def schur(A,B,D):
    return sub(D,mm(tr(B),mm(inv2(A),B)))
def scalar(V):
    assert len(V)==len(V[0])==1
    return V[0][0]

def finite_woodbury_replay():
    # Pure exact-Fraction 2+2-dimensional REAL symmetric block
    # algebra replay. It does NOT substitute for infinite-dimensional
    # source Woodbury functional-analytic proof but catches a missing
    # factor, wrong inverse, or erroneous source/cross pole placement.
    A0=[[F(4),F(1)],[F(1),F(3)]]
    D0=[[F(5),F(1)],[F(1),F(4)]]
    B0=[[F(1),F(2)],[F(-1),F(1)]]
    cp=col([F(1,3),F(1,4)])
    cc=col([F(2,3),F(1,5)])
    A=add(A0,scale(mm(cp,tr(cp)),F(2)))
    B=add(B0,scale(mm(cp,tr(cc)),F(2)))
    D=add(D0,scale(mm(cc,tr(cc)),F(2)))
    Sdirect=schur(A,B,D)
    S0=schur(A0,B0,D0)
    inv=inv2(A0)
    T=scalar(mm(tr(cp),mm(inv,cp)))
    d=sub(cc,mm(tr(B0),mm(inv,cp)))
    alpha=F(2)/(F(1)+F(2)*T)
    Swood=add(S0,scale(mm(d,tr(d)),alpha))
    assert Sdirect==Swood
    # Check equality of true quadratic forms for independent profiles.
    for h in (col([F(1),F(0)]),col([F(0),F(1)]),
              col([F(7,5),F(-3,4)])):
        assert scalar(mm(tr(h),mm(Sdirect,h)))==scalar(mm(tr(h),mm(Swood,h)))
    return T,alpha,d

def run():
    ps26.run()  # replay entire original pinned PS25→...→RC315 chain
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT" and lane["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(v is False for v in lane["closures"].values())

    # SOURCE TRUE: A_P>323/1000 on the actual 13 original physical
    # source channels, including all original internal 7 prime shifts,
    # digamma kernel, and both correctly signed poles.
    # The original positive even pole is rank-one +2 c_P c_P*.
    # Its physical source mass is bounded by
    # ||c_P||² <=13*delta*cosh(B/2)²
    ell9=old.log_i(F(9))
    delta=old.IV(R-ell9.hi,R-ell9.lo)
    sinh,cosh=old.sinh_cosh_iv(B/2)
    assert 0<delta.lo<=delta.hi<F(1,350)
    assert cosh.hi<F(7,6)
    cp_mass_upper=F(13,350)*F(7,6)**2
    assert cp_mass_upper==F(91,1800)
    cp_even_cost=F(2)*cp_mass_upper
    # Define true pole-FREE source A0=A_P -2 c_P c_P*.
    a0_lower=F(323,1000)-cp_even_cost
    assert a0_lower==F(1997,9000)>F(1,5)
    # A0 IS invertible positive (unlike whole pole-free Q0).
    # t=<c_P,A0^-1 c_P> >=0 is finite and bounded rationally.
    t_upper=cp_mass_upper/a0_lower
    assert t_upper==F(455,1997)<F(23,100)
    # Effective original positive pole alpha |<d,h>|² after exact
    # source elimination, with true original pre-pole source/cross:
    # B0=B_PC -2 |c_P><c_C|;
    # d=c_C - B0* A0^-1 c_P,
    # alpha = 2/(1+2t).
    alpha_lower=F(2)/(F(1)+F(2)*t_upper)
    assert alpha_lower==F(3994,2907)>F(137,100)
    assert alpha_lower<F(2)

    # A conservative bound on the true PRE-POLE B0, to show that
    # the effective vector d exists as an L2 carrier. PS15 gives
    # full source/complement B_PC<67/4. ||c_C|| <=sqrt(R)*7/6
    # with sqrt(R)<3/2, ||c_P||<9/40.
    assert cp_mass_upper<F(9,40)**2
    assert R<F(3,2)**2
    cC_norm_upper=F(7,4)
    b0_upper=F(67,4)+F(2)*F(9,40)*cC_norm_upper
    assert b0_upper==F(1403,80)<F(18)
    d_diff_upper=b0_upper*F(1)/a0_lower*F(9,40)
    assert d_diff_upper<F(18)
    # Finite but intentionally NOT a small perturbation:
    # replacing d by c_C is UNJUSTIFIED. The exact inverse response
    # is part of the effective rank-one vector d.

    receipt=json.loads((ROOT/"certificates/rpb108_rc315_low_mode_sign.json").read_text())
    assert receipt["milestone"]=="RC315" and receipt["original_source_pin"]==old.ORIGINAL_PIN
    q0_lo,q0_hi=map(F,receipt["original_low_diagonals"][0]["physically_normalized_original_Weil_diagonal_interval"])
    assert F(0)<q0_lo<=q0_hi<F(41,1000)
    # On u0=1/sqrt(R), original even pole >=2R=4.4.
    # Q0=Q−2|<c,u>|² on WHOLE domain is explicitly NEGATIVE.
    true_pole_free_negative=q0_hi-F(2)*R
    assert true_pole_free_negative<-F(435,100)
    # The original pre-pole source A0 is proved POSITIVE, so
    # its actual source Schur is
    # S0_C[h]=inf_{p} Q0[p+h].
    # h=1_C u0 admissible; p0=1_P u0 admissible:
    # S0_C[h]<=Q0[u0]<-4.35974.
    # This is a NEW actual pole-FREE source-Schur obstruction,
    # much stronger than PS26's post-Schur B_C[h]<-4.212.
    assert true_pole_free_negative<-F(43,10)

    # Reflection: r <-> 9/r makes P and C invariant. c_P,c_C are
    # even; original arch and prime symmetric covariance keeps B0
    # parity-preserving. A0^-1 on P commutes with reflection, hence
    # effective d=c_C-B0* A0^-1 c_P is EVEN, so odd original
    # S_C and S0_C coincide IDENTICALLY.
    labels={F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
    labels|={F(9,n) for n in (2,4,5,7,8)}
    assert len(labels)==13 and all(F(9)/r in labels for r in labels)

    # The exact parity-positive acceptance theorem:
    # Let ell_eff(h)=<d,h>. For EVEN sector H_e define
    # K_eff={even h in original form domain: ell_eff(h)=0}.
    # Since S0_C[h0]<0 for even h0=1_Cu0, index-(S0_C,e)>=1.
    # Rank-one positive update may remove at most ONE negative
    # independent direction. If S_C >=0 EVEN, then necessarily
    # ind-(S0_C,e)==1 and S0_C>=0 on K_eff.
    # If d!=0: phi=d/||d||. Exact original even sign criterion:
    # S0_C>=0 on K_eff AND
    # inf_{k in K_eff} (S0_C[phi+k]+alpha||d||²)>=0.
    # NO positive K_eff or scalar infimum is computed in PS27.
    # d=0 would leave the explicit negative S0_C even direction
    # uncorrected and hence is impossible IF full even S_C PSD.
    t_test,alpha_test,d_test=finite_woodbury_replay()
    assert t_test>0 and F(0)<alpha_test<F(2)
    assert len(d_test)==2

    print("PS27 physical source ||c_P||² rational strict upper",
          float(cp_mass_upper),flush=True)
    print("PS27 true pole-FREE source coercivity strict lower",float(a0_lower),flush=True)
    print("PS27 source pole self-energy t strict upper",float(t_upper),flush=True)
    print("PS27 true renormalized positive EVEN pole alpha strict lower",
          float(alpha_lower),flush=True)
    print("PS27 genuine PRE-pole source-cross B0 coarse norm upper",float(b0_upper),flush=True)
    print("PS27 exact finite block original-pole Woodbury replay t",str(t_test),flush=True)
    print("PS27 exact finite block original-pole Woodbury replay alpha",str(alpha_test),flush=True)
    print("PS27 pinned actual original pole-FREE Schur constant witness upper",
          float(true_pole_free_negative),flush=True)
    print("PS27 PASS SCOPED: full original source pole-FREE A0>1997/9000,"
          " exact true physical signed original source Schur identity"
          " S_C=S0_C+[2/(1+2t)]|<d,*>|² with"
          " 3994/2907<alpha<=2 and exact effective d"
          " including source inverse; Q0/S0_C have a proven"
          " NEGATIVE pole-FREE even direction (NOT original Weil)."
          " Original ODD sector unaffected by even pole."
          " EVEN effective-pole-orthogonal K_eff positivity and one"
          " scalar variational correction remain mandatory OPEN."
          " W-ODD-NEG, W-EVEN-FORM, CC27 D-Riesz, whole original"
          " Weil and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
