#!/usr/bin/env python3
"""SM41: actual original odd pole-free positive Fourier TAIL (rigorous),
with source-analytic low-frequency NUMERICAL pilot kept separate.

WHOLE-REAL exact mathematical upper, conditional on inherited
original Fourier/closed-domain identification:
  For xi>=1, a_o(xi)=max(kappa,m(xi)) <=17+log(xi),
  with m original Re psi(1/4+i*pi*xi)-log pi and all genuine
  seven signed prime-power cosine terms. A direct digamma
  positive-term expansion, split at N=ceil(pi*xi), proves
  this from TWOC<70751/10000 and rational ln21<4.
  On the actual 25 SI10 physically supported odd pilot
  sine/degree-1 xcos/pole sources, if xi>=Lambda>=2*max c,
  analytically |T_j(xi)|<=u_j/xi with EXACT rational
  u(sin)=1/2, u(xcos)=7/10, u(sinh(x/2))=2/5.
  Therefore on ALL real coefficient vectors z:
    0<= Qtail_Ao(z)<= [2*sum u_j^2*(18+ln Lambda)/Lambda] ||z||^2
    ||a_o \hat z||^2_(|xi|>Lambda)
      <= [2*sum u_j^2*((17+lnLambda)^2
           +2*(17+lnLambda)+2)/Lambda] ||z||^2.
  Upper log(Lambda) via exact SI06 ln2 upper for powers of 2.

Crucially these are complete WHOLE-REAL positive high-frequency
bounds on the ORIGINAL physically supported selected pilot sources,
not finite FFT cutoff assumptions or claims about the full 470
resolvent. An explicit whole-470 generator-derivative IBP majorant
is also derived but extremely loose and not used for sign proof.

Numerical-only low band 0<=xi<=Lambda Gauss 8/16 uses actual
analytic odd source Fourier transforms and original digamma +
seven prime multiplier; no interval Gauss error. Samples do NOT
certify original complete positive Astar matrix, strong residual,
470-source Loewner gate, signed Wodd positivity or RH.
"""
import argparse
import json
from fractions import Fraction as F
from math import factorial

import numpy as np
from scipy import linalg

from validate_rpb108_si06_negative_band import (
    B, PI, LN, TWOC
)
from validate_rpb108_si10_complement_positivity import (
    protected_inner_cover, KAPPA
)
from validate_rpb108_si08_multiband_rank import taylor_order
from sm36_original_odd_numerical_pilot import (
    ROOT, B_FLOAT, geometry, select_sources, physical_columns,
    fourier_form, original_multiplier
)
from sm38_leafwise_original_odd_fourier_audit import (
    supported_odd_sine_transform, generalized_max
)

ARCH_PLUS_C=17  # Exact global original a_o(xi) <= 17+ln xi for xi>=1.
SIN_BOUND=F(1,2)
XCOS_BOUND=F(7,10)
POLE_BOUND=F(2,5)


def mathematical_global_original_positive_multiplier_majorant():
    """Integer/rational prerequisites of original true analytic lemma.

    psi(a+it) real-part expansion at a=1/4:
      arch(xi) = psi(a)-log pi
        +sum_{k>=0} t²/((k+a)((k+a)²+t²)), t=pi xi.
    psi(1/4)-log pi<0. For t>=1, N=ceil(t):
      sum[k<N] <=4+ln(4N+1)
      sum[k>=N]<=t²((N+a)^-3 +[2(N+a)^2]^-1)
                  <=1/t+1/2<=3/2.
    pi<4, xi>=1 => 4N+1<=4(t+1)+1<=21xi.
    log21<4 (e^4>21 by first 4 positive rational terms).
    arch(xi)<19/2 +ln xi; |original signed prime|<=TWOC.
    19/2+TWOC<17, so max(kappa,m)<17+ln xi.
    """
    assert PI[0]>3 and PI[1]<4
    assert LN[2][0]>F(69,100)
    assert TWOC<F(70751,10000)
    assert F(19,2)+TWOC<ARCH_PLUS_C
    assert KAPPA<1
    # Rigorous e^4>21 follows finite positive exponential terms.
    assert sum((F(4)**k/F(factorial(k)) for k in range(5)),F(0))>21
    # Universal source analytic transform constants below.
    # sine <=3/(2*pi*xi) <=1/(2xi)
    assert F(3,2)/3<=SIN_BOUND
    # xcos <= [3B/(2*pi)+5/(4*pi²*xi)] /xi
    # <= [B/2+5/36]/xi <7/(10xi).
    assert B/2+F(5,36)<XCOS_BOUND
    # sinh pole <= [1/(3xi)+1/(18xi²)] <2/(5xi)
    assert F(1,3)+F(1,18)<POLE_BOUND
    # sinh(11/20)<1 and cosh(11/20)<2:
    # ln2>69/100>11/20, hence e^(11/20)<2,
    # and e^(-11/20)<1. (Use elementary ordering.)
    assert LN[2][0]>F(11,20)
    return True


def odd_pilot_tail_enclosure(infos,sources,cutoff):
    """CERTIFIED original 25 source Ao FORM & strong multiplier tail.

    Exact rational inequalities, no FFT quadrature or floating
    resolution assumption. Powers of two cutoff to bound lnLambda.
    """
    cutoff=int(cutoff)
    assert cutoff>=2048 and cutoff&(cutoff-1)==0
    cmax=max(infos[j][0] for kind,j,k in sources if kind=="cluster")
    # Original cluster center is rational in SI10; float only used
    # for this redundant quick precheck, exact center below.
    clusters,_,_,_,_=protected_inner_cover()
    center_exact=max((a+b)/2 for a,b,_ in clusters)
    assert F(cutoff)>=2*center_exact
    assert cutoff>=1
    u=[]
    degree_counts={"sin":0,"xcos":0,"pole":0}
    for kind,j,k in sources:
        if kind=="pole":
            u.append(POLE_BOUND); degree_counts["pole"]+=1
        elif k==0:
            u.append(SIN_BOUND);degree_counts["sin"]+=1
        elif k==1:
            u.append(XCOS_BOUND);degree_counts["xcos"]+=1
        else:
            raise AssertionError("SM41 only selected k=0 or1; do not silently apply bound to remaining original 470.")
    assert len(u)==25 and sum(degree_counts.values())==25
    assert degree_counts["pole"]==1
    energy=sum((x*x for x in u),F(0))
    # Exact SI06 infinite series ln2 rational upper, no float:
    power=cutoff.bit_length()-1
    # Exact outward RATIONAL cap already proved by SI06:
    # ln2 < 347/500. Avoid transporting the enormous exact
    # 128-term LN denominator through every source bound.
    assert LN[2][1]<F(347,500)
    log_up=power*F(347,500)
    assert F(0)<log_up and F(2)**power==cutoff
    form=2*energy*(ARCH_PLUS_C+1+log_up)/cutoff
    v=ARCH_PLUS_C+log_up
    strong=2*energy*(v*v+2*v+2)/cutoff
    assert 0<form<strong
    # An actual source-form tail, for all x in R^25:
    # 0<= T_pos,Ao(x) <= form * ||x||^2.
    # Whole-line strong Fourier multiplier tail <=strong*||x||^2.
    return {
        "cutoff":cutoff,
        "actual_original_max_cluster_center_exact":str(center_exact),
        "certified_original_positive_multiplier_upper":
            "a_o(xi)<=17+log(xi) for all real xi>=1",
        "exact_rational_log_cutoff_upper":str(log_up),
        "source_dims":len(u),"source_type_count":degree_counts,
        "sum_source_transform_bound_squares_exact":str(energy),
        "exact_form_tail_operator_norm_upper":str(form),
        "exact_strong_multiplier_tail_squared_norm_upper":str(strong),
        "form_tail_upper_float":float(form),
        "strong_tail_squared_upper_float":float(strong),
        "proves_original_positive_tail_for_selected_25":True,
        "proves_actual_original_470_resolvent":False
    }


def full_470_supported_IBP_tail(cutoff):
    """RIGOROUS original all 470 source tail via elementary IBP,
    deliberately loose to expose unresolved conditioning.

    For original w_j(x)=x^k sin/cos(2*pi*c*x), |w_j(B)|<=B^k,
    and integral abs(w_j') <=2*k*B^k +4*pi_up*c*B^(k+1).
    T_j's sine transform <= [2(1+k)B^k +
        4*pi_up*c*B^(k+1)]/(2*pi*xi)
       <= that rational expression / (6 xi) as pi>3.
    Pole true M<=2+2B and u<=M/6.
    This holds regardless of resonance or order, but is much
    weaker than selected-source exact sine transforms.
    """
    clusters,_,_,_,_=protected_inner_cover()
    assert len(clusters)==107
    l2=F(0);num=0
    for a,b,_ in clusters:
        c=(a+b)/2
        kmax,_=taylor_order(b-a,9)
        for k in range(kmax):
            endpoint_and_variation=(
               2*(1+k)*B**k+4*PI[1]*c*B**(k+1))
            u=endpoint_and_variation/6
            l2+=u*u
            num+=1
    pole_var=(2+2*B)/6
    l2+=pole_var*pole_var
    num+=1
    assert num==470
    logup=(cutoff.bit_length()-1)*F(347,500)
    form=2*l2*(ARCH_PLUS_C+1+logup)/cutoff
    # Large value is not a proof that no better matrix-weighted
    # bound exists: it exposes the insufficiency of one scalar
    # all-470 integration-by-parts majorant.
    return {"original_complete_source_count":num,
            "general_original_source_tail_method":
                "zero-extension integration by parts, full k=0..p_j-1",
            "source_bound_sum_of_squares_float":float(l2),
            "all_470_scalar_form_tail_upper_float":float(form),
            "whole_470_operator_sign_certified":False}


def low_band_original_positive_form(infos,sources,cutoff,order,subcells=8):
    """Numerical-only original analytic-source low frequency stiffness.

    Divide EVERY original unit frequency interval into 8 finer
    subcells. One-cell Gauss8 failed honest convergence (2.35%
    drift against Gauss16), due to rapid original signed prime
    phases and source transforms. Keep hard 8-vs-16 gate, don't
    hide coarse quadrature error or infer a rigorous interval.
    """
    assert subcells>=8 and cutoff%1==0
    nodes,weights=np.polynomial.legendre.leggauss(order)
    width=1./subcells
    cells=np.arange(cutoff*subcells,dtype=float)*width
    xi=(cells[:,None]+0.5*width*(nodes[None,:]+1)).ravel()
    dw=np.broadcast_to((width/2)*weights[None,:],
                       (cutoff*subcells,order)).ravel()
    m=original_multiplier(xi)
    ap=np.maximum(float(KAPPA),m)
    T=supported_odd_sine_transform(xi,infos,sources)
    A=T.T@(T*(2*dw*ap)[:,None])
    return (A+A.T)/2


def numerical_selected_25_pilot(infos,sources,cutoff,tail):
    """Measured low band and optional old FFT diagnostic. NONPROOF."""
    matrices=[]
    for q in (8,16):
        A=low_band_original_positive_form(infos,sources,cutoff,q)
        eig=linalg.eigvalsh(A)
        matrices.append((q,A,{
          "gauss_order":q,
          "source_count":25,
          "original_low_frequency_band":[0,cutoff],
          "quadrature_subcells_per_unit_frequency":8,
          "minimum_eigenvalue_raw_basis":float(eig[0]),
          "maximum_eigenvalue_raw_basis":float(eig[-1]),
          "source_tridiagonal_or_disjoint_band_proxy":False,
          "rigorous_quadrature":False
        }))
    A8=matrices[0][1]
    A16=matrices[1][1]
    drift=float(np.linalg.norm(A8-A16)/max(np.linalg.norm(A16),1e-30))
    # Valid only as numerical convergence sanity; actual continuous
    # low-band quadrature still lacks a proven remainder.
    assert drift<1e-3,("SM41 inadequate low frequency Gauss convergence",drift)
    # Original source pole correction computed by physical sample
    # only, not actual certified original infinite resolvent tau.
    x,dx,v=physical_columns(8192,infos,sources)
    b=(v.T@np.sinh(x/2))*dx
    H=(v.T@v)*dx
    pole_trial=A16-2*np.outer(b,b)
    pole_trial=(pole_trial+pole_trial.T)/2
    minp=float(linalg.eigvalsh(pole_trial)[0])
    result={
      "cutoff":cutoff,
      "gauss8_vs16_relative_Frobenius_drift":drift,
      "positive_tail_certified_scalar_Ao_form_upper":
          tail["form_tail_upper_float"],
      "positive_tail_certified_scalar_strong_squared_upper":
          tail["strong_tail_squared_upper_float"],
      "raw_basis_pole_conditioned_low_band_min_eig":minp,
      "low_gauss_cases":[d for _,_,d in matrices],
      "numerical_only":True,
      "full_original_positive_stiffness_certified":False
    }
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--quick",action="store_true")
    p.add_argument("--output",default="artifacts/sm41_original_arch_log_tail.json")
    args=p.parse_args()
    o=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in o["obligations"] if x["id"]=="W-ODD-NEG")
    assert o["active_obligation"]=="W-ODD-NEG"
    assert o["objective"]["status"]=="open" and odd["status"]=="open"
    assert o["governance"]["no_automatic_promotion"] is True
    assert all(k in odd["evidence"] and k in o["evidence"]
               for k in ("SM39","SM40","SM41"))
    assert "sm41_original_positive_arch_tail" in o["governance"]
    mathematical_global_original_positive_multiplier_majorant()
    infos,cap,orders,mass,width,total=geometry()
    sources=select_sources(infos)
    exact=[]
    for cutoff in (2048,4096,8192):
        t=odd_pilot_tail_enclosure(infos,sources,cutoff)
        exact.append(t)
        print("SM41 ORIGINAL EXACT WHOLE POSITIVE HIGH LOG TAIL",
              json.dumps(t,sort_keys=True),flush=True)
    assert all(exact[i]["form_tail_upper_float"]>
               exact[i+1]["form_tail_upper_float"]
               for i in range(2))
    full=full_470_supported_IBP_tail(4096)
    print("SM41 original ALL 470-source coarse IBP tail",
          json.dumps(full,sort_keys=True),flush=True)
    numerics=[]
    for cutoff in ([2048] if args.quick else [2048,4096]):
        t=next(t for t in exact if t["cutoff"]==cutoff)
        q=numerical_selected_25_pilot(infos,sources,cutoff,t)
        numerics.append(q)
        print("SM41 ORIGINAL POSITIVE LOW BAND NUMERICAL ONLY",
              json.dumps(q,sort_keys=True),flush=True)
    result={
      "status":"CERTIFIED_ACTUAL_ORIGINAL_POSITIVE_LOG_HIGH_TAIL_SELECTED_SOURCES_ONLY",
      "canonical_W_ODD_NEG":"OPEN",
      "rigorous_original_multiplier_tail":{
        "frequency_region":"|xi|>=1",
        "original_full_digamma_and_all_seven_primes":True,
        "pointwise_upper":"a_o(xi)<=17+ln|xi|",
        "exact_analytic_derivation_required":True,
        "correct_zero_extension_fourier_parity":True
      },
      "actual_original_supported_25_source_tail":exact,
      "original_complete_470_source_coarse_IBP_upper":full,
      "same_original_selected_25_numerical_low_band":numerics,
      "incomplete_acceptance":[
        "interval enclosure of original low frequency digamma/prime Gauss source Gram",
        "all original 470 source sharp high-frequency positive tail",
        "exact full original positive pole-conditioned Astar stiffness and inverse",
        "full strong residual low+high (SM41 certifies ONLY multiplier high tail)",
        "original all 470 G,N generalized <=51/56 or corrected Schur",
        "independent original Fourier zero-extension analytic audit",
        "complete original odd/even Weil positivity, CC27 and RH"
      ]
    }
    dest=ROOT/args.output
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,indent=2)+"\n")
    print("SM41 SCOPED PASS: exact rigorous original positive"
          " digamma+seven-prime logarithmic HIGH Fourier tail,"
          " selected actual odd physical source 25-dimensional"
          " complete form AND strong multiplier high tail;"
          " numerical original 2048/4096 low band NONCERTIFYING."
          " TRUE original 470 inverse/residual, odd O1/O2,"
          " even E1-E4 full Weil CC27 RH OPEN.",flush=True)


if __name__=="__main__":
    main()
