#!/usr/bin/env python3
"""PS29 -- exact-rational replay of the original even pole-angle spectral gate.

ANALYTIC (not independently machine certified here):
 * the original even pole-FREE source Schur L has compact resolvent;
 * strict modulus improvement for sign-changing even h shows that
   its negative lowest eigenvalue is simple with phi0 >= 0;
 * PS28 d >= c_C >= 1 implies a=<d,phi0> > 0.
These require functional-analytic review. No original eigenvalues are
calculated by this regression.

EXACT ALGEBRA (tested with Fraction toy spectra):
 assuming lambda1>=0 and d perpendicular to ker(L), let
 a=<d,phi0>, beta=<b,L_plus^-1 b>, Delta=a*a-abs(lambda0)*beta.
 The ORIGINAL positive rank-one restored form L+alpha*d*d*
 is PSD iff Delta>0 and alpha*Delta>=abs(lambda0).
 K_eff nonnegativity alone permits Delta=0; no finite alpha
 makes that equality case PSD.
Original odd W-ODD-NEG, even W-EVEN-FORM, CC27 D-Riesz, RH OPEN.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_ps28_positive_source_resolvent as ps28

ROOT=Path(__file__).resolve().parents[1]
REPO_LANE="research/parallel_investigations/w_physical_shift.json"


def beta_value(b, pos_lambdas):
    assert len(b)==len(pos_lambdas)
    assert all(x>0 for x in pos_lambdas)
    return sum((x*x/mu for x,mu in zip(b,pos_lambdas)),F(0))


def ground_block_reduction(lam_abs,a,b,pos_lambdas,alpha):
    """Exact finite spectral Schur: positive block eliminated FIRST."""
    assert lam_abs>0 and a>0 and alpha>0
    beta=beta_value(b,pos_lambdas)
    delta=a*a-lam_abs*beta
    schur_scalar=-lam_abs+alpha*a*a/(1+alpha*beta)
    assert (schur_scalar>=0)==(delta>0 and alpha*delta>=lam_abs)
    return beta,delta,schur_scalar


def run():
    ps28.run()
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/REPO_LANE).read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(v is False for v in lane["closures"].values())
    assert lane["checkpoints"][-1]["id"]=="PS29"

    # All exact bounds below are inherited from the ORIGINAL PS28
    # source-resolvent trial. Neither alpha nor d is numerically
    # evaluated for the true infinite-dimensional original operator.
    alpha_lower=F(3994,2907)
    alpha_upper=F(240000,120169)
    sufficient_margin=F(1)/alpha_lower
    impossible_margin=F(1)/alpha_upper
    assert sufficient_margin==F(2907,3994)
    assert impossible_margin==F(120169,240000)
    assert 0<impossible_margin<sufficient_margin<1

    # True spectral sign is NOT inferred from a>0.
    # A rank-one update cannot fix two negative eigenvectors.
    # L_test=diag(-2,-1,3), d_test=(2,1,1):
    # k=(1,-2,0) is pole orthogonal; L[k]=-2-4=-6.
    d_two=(F(2),F(1),F(1))
    k_two=(F(1),F(-2),F(0))
    assert sum((x*y for x,y in zip(d_two,k_two)),F(0))==0
    assert -2*k_two[0]**2-k_two[1]**2+3*k_two[2]**2==-6

    # Ground-pole overlap a=1>0 is insufficient: choose
    # L=diag(-2,1), d=(1,2), k=(2,-1) in K.
    a=F(1)
    b=(F(2),)
    beta=beta_value(b,(F(1),))
    delta=a*a-F(2)*beta
    assert beta==4 and delta==-7
    assert F(-2)*F(2)**2+F(1)*F(-1)**2==-7

    # In the boundary case Delta=0, even K is nonnegative but
    # no finite alpha can restore positivity.
    # L=diag(-1,1), d=(1,1).
    for alpha in (F(1,10),F(1),F(2),F(1000000)):
        beta,delta,s=ground_block_reduction(
            F(1),F(1),(F(1),),(F(1),),alpha)
        assert beta==1 and delta==0 and s<0

    # NONZERO Delta finite-rank test with three original-STYLE
    # orthogonal spectral directions (not actual original eigenpairs):
    # L=diag(-2,3,5), d=(2,1,1/2).
    beta=F(23,60)
    delta=F(97,30)
    threshold=F(60,97)
    assert beta_value((F(1),F(1,2)),(F(3),F(5)))==beta
    assert F(2)**2-F(2)*beta==delta
    for alpha,expect_nonnegative in (
        (F(1,2),False),
        (threshold,True),
        (F(1),True),
    ):
        b,d,s=ground_block_reduction(
            F(2),F(2),(F(1),F(1,2)),(F(3),F(5)),alpha)
        assert b==beta and d==delta
        assert (s>=0)==expect_nonnegative
        assert (alpha*delta>=2)==expect_nonnegative

    # Lambda1 = 0 case: nonzero coupling to a null vector
    # cannot be repaired by any alpha. Here d=(1,1) and
    # L=diag(-1,0); k=(1,-1) has pole zero and L[k]=-1.
    assert F(1)*F(1)+F(1)*F(-1)==0
    assert -F(1)**2==-1
    # If d annihilates the nullspace, it remains a harmless
    # nullspace. On its orthogonal positive complement use
    # the same strictly positive inverse and Delta gate:
    # L=diag(-1,0,2), d=(2,0,1).
    beta,delta,s=ground_block_reduction(
        F(1),F(2),(F(1),),(F(2),),F(2,7))
    assert beta==F(1,2) and delta==F(7,2) and s==0

    # Source-derived condition corridor, conditional on:
    # lambda1>=0; d kills ker(L); computed m=Delta/|lambda0|.
    # If m >= sufficient_margin, original alpha>alpha_lower
    # makes original even Schur PSD. If m <= impossible_margin,
    # original alpha<alpha_upper proves it indefinite.
    for m in (sufficient_margin,sufficient_margin+F(1,100)):
        assert alpha_lower*m>=1
    for m in (impossible_margin,impossible_margin-F(1,100)):
        assert alpha_upper*m<=1

    print("PS29 original even pole-FREE Schur ground mode: "
          "compactness/strict modulus/simplicity ANALYTIC, "
          "independent review pending",flush=True)
    print("PS29 pole ground-state overlap a>0 from PS28 d>=1: "
          "ANALYTIC, not a quantitative eigenpair solve",flush=True)
    print("PS29 finite exact spectral test beta",str(beta),flush=True)
    print("PS29 finite exact spectral test Delta",str(delta),flush=True)
    print("PS29 finite exact spectral alpha threshold",
          str(threshold),flush=True)
    print("PS29 exact sufficient true source-alpha margin",
          str(sufficient_margin),flush=True)
    print("PS29 exact impossible true source-alpha margin",
          str(impossible_margin),flush=True)
    print("PS29 PASS SCOPED: exact rank-one spectral Schur algebra, "
          "zero-mode and two-negative-mode obstructions, genuine "
          "PS28 source-derived coefficient corridor replayed. "
          "No original lambda1/a/beta/Delta computed, no actual "
          "K_eff or scalar positivity established. W-ODD-NEG, "
          "W-EVEN-FORM, native CC27 D-Riesz, whole signed Weil "
          "and RH OPEN.",flush=True)


if __name__=="__main__":
    run()
