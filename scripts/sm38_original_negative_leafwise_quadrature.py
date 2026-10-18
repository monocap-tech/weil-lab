#!/usr/bin/env python3
"""SM38 genuinely original odd negative Fourier leafwise integration pilot.

NEW NUMERICAL (not interval certification):
 * analytically exact closed formulas for physically supported odd SI10
   pilot generators' sine Fourier transforms, including pole sinh(x/2);
 * Gauss-Legendre directly on ALL 973 original signed-negative leaves,
   with independent orders 8, 16, 32, 48 and no FFT frequency bins;
 * separate original signed direct K-, original SM10 piecewise upper
   multiplier envelope, and SM37 new 3,892-subcell *upper envelope*
   against the SAME actual 25-source Galerkin trial;
 * compare full actual SM37 890-column Taylor/Young/eta cap on SAME
   Galerkin coefficients to integral of its ORIGINAL upper envelope
   with the true supported analytic sine Fourier amplitudes;
 * compare coarse FFT K- approximation to independent leafwise answer
   (the positive-pole-conditioned *trial* still uses FFT and remains
   noncertifying).

The EXACT original original-real-frequency envelope upper and SM37
890 strict SPD moment cap are inherited proven source statements.
ALL new quadrature integrations, sin/cos/pole analytic amplitude in
float64, generalized eigenvalues and trial inverse are NONCERTIFYING:
they lack outward interval quadrature, positive-frequency digamma
logarithmic tail, full strong Galerkin residual, and all 470 sources.
A same-selected-source unfavorable Ritz result is NOT an original
full odd negative spectral direction or a counterexample to RH.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import integrate, linalg

from sm36_original_odd_numerical_pilot import (
    B_FLOAT,KAPPA_FLOAT,THETA,geometry,select_sources,physical_columns,
    fourier_form,all_source_negative_cap,original_multiplier,
)
from validate_rpb108_sm37_refined_original_negative_cap import (
    refined_signed_original_cap
)
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves
)

ROOT=Path(__file__).resolve().parents[1]
B=B_FLOAT


def base_sine_overlap(y):
    # ∫_-B^B sin(2πc x) sin(2πxi x) dx
    # = B*sinc[2B(c-xi)] - B*sinc[2B(c+xi)].
    return B*np.sinc(2*B*y)


def derivative_base_overlap(y):
    # d/dy [ B sin(t)/t ], t=2πBy; stable near resonance.
    yy=np.asarray(y,dtype=float)
    t=2*np.pi*B*yy
    v=np.empty_like(t)
    small=np.abs(t)<0.02
    z=t[small]
    v[small]=B*(2*np.pi*B)*(
        -z/3+z**3/30-z**5/840+z**7/45360
    )
    u=t[~small]
    v[~small]=B*(2*np.pi*B)*(u*np.cos(u)-np.sin(u))/u**2
    return v


def exact_formula_physical_sine_amplitudes(freq,infos,sources):
    """Nonperiodic exact physical ∫_-B^B f(x)sin(2πxi x) dx.

    Formulas mathematically exact; numerical double evaluation not
    interval-certified. The selected SM36 original generators contain
    degrees 0 and 1 only, plus genuine odd pole sinh(x/2).
    """
    xi=np.atleast_1d(np.asarray(freq,dtype=float))
    result=np.empty((len(xi),len(sources)))
    for j,(typ,source_id,degree) in enumerate(sources):
        if typ=="pole":
            a=0.5; w=2*np.pi*xi
            result[:,j]=2*(a*np.cosh(a*B)*np.sin(w*B)
                -w*np.sinh(a*B)*np.cos(w*B))/(a*a+w*w)
        else:
            c=infos[source_id][0]
            if degree==0:
                result[:,j]=(base_sine_overlap(c-xi)
                             -base_sine_overlap(c+xi))
            elif degree==1:
                result[:,j]=(derivative_base_overlap(c-xi)
                             -derivative_base_overlap(c+xi))/(2*np.pi)
            else:
                raise ValueError("SM38 pilot only supports original k=0,1; "
                    "higher real original k need exact derivative recurrence")
    assert np.isfinite(result).all()
    return result


def validate_physical_transforms(infos,sources):
    centers=(0.0,0.27,14.42,14.423,389.56,389.565,882.91)
    choices=[0, len(sources)//2, len(sources)-1]
    for j in choices:
        typ,source_id,k=sources[j]
        for xi in centers:
            a=float(exact_formula_physical_sine_amplitudes(
                [xi],infos,[sources[j]])[0,0])
            def f(x):
                if typ=="pole":return np.sinh(x/2)
                c=infos[source_id][0]
                return (x**k)*(np.sin(2*np.pi*c*x) if k%2==0
                              else np.cos(2*np.pi*c*x))
            # INDEPENDENT physical-space high-resolution composite
            # Simpson cross-validation. The old QUADPACK check
            # reached subdivision/roundoff failure for near-resonant
            # high-frequency SOURCE and test sine products: such a
            # failure must not be mistaken for a bad analytic formula.
            # The fixed dense real-space grid is entirely independent
            # of the leafwise frequency Gauss nodes and FFT padding.
            xx=np.linspace(0.,B,131073)
            val=float(integrate.simpson(
                2*f(xx)*np.sin(2*np.pi*xi*xx),x=xx))
            assert abs(a-val)<2e-5,(typ,k,xi,a,val,abs(a-val))
    # Odd sine Fourier convention normalized by Parseval; DO NOT
    # drop the 2 for negative mirrored frequency in all integrals.
    return True


def nodes_for_cells(cells,order):
    u,w=np.polynomial.legendre.leggauss(order)
    bounds=np.array([(float(a),float(b))
                     for a,b,*rest in cells],dtype=float)
    lo=bounds[:,0];hi=bounds[:,1]
    centers=(lo+hi)/2;half=(hi-lo)/2
    return ((centers[:,None]+half[:,None]*u[None,:]).reshape(-1),
            (half[:,None]*np.broadcast_to(w,(len(lo),order))).reshape(-1))


def matrix_from_nodes(nodes,weights,infos,sources,source_coeff):
    # Full cross coupling between ALL selected true physical
    # pilot source combinations, not source-by-source diagonals.
    amp=exact_formula_physical_sine_amplitudes(nodes,infos,sources)
    physical=amp@source_coeff
    value=2*(physical.T@(physical*weights[:,None]))
    return (value+value.T)/2


def original_fourier_integral(clusters,infos,sources,c,order,
                              method):
    assert method in ("direct","sm10-envelope","sm37-envelope")
    if method=="sm37-envelope":
        cells=[(a,b,float(h)+KAPPA_FLOAT)
               for cluster in clusters for a,b,h in cluster]
    elif method=="sm10-envelope":
        cells=[(a,b,float(h)+KAPPA_FLOAT)
               for cluster in clusters for a,b,h in cluster]
    else:
        cells=[(a,b,0.0) for cluster in clusters for a,b,h in cluster]
    nodes,weights=nodes_for_cells(cells,order)
    if method=="direct":
        signed=original_multiplier(nodes)
        response=np.maximum(KAPPA_FLOAT-signed,0.)
    else:
        heights=np.array([z[2] for z in cells])
        response=np.repeat(heights,order)
    signed_weight=weights*response
    m=matrix_from_nodes(nodes,signed_weight,infos,sources,c)
    return m,{
        "cell_count":len(cells),"nodes":len(nodes),
        "quadrature_order":order,
        "nonzero_negative_nodes":int(np.count_nonzero(response>0)),
        "numeric_signed_negative_mass":float(2*np.sum(signed_weight)),
        "quadrature_kind":method,
    }


def generalized_max(m,g):
    return float(linalg.eigh(
        (m+m.T)/2,(g+g.T)/2,eigvals_only=True,
        check_finite=True)[-1])


def one_case(n,pad,original,refined,orders,infos,sources,mass,total,
             newtotal,orders_gauss):
    x,dx,v=physical_columns(n,infos,sources)
    H=(v.T@v)*dx;H=(H+H.T)/2
    a0,kfft,_,sample=fourier_form(v,dx,pad)
    b=(v.T@np.sinh(x/2))*dx
    astar=a0-2*np.outer(b,b)
    astar=(astar+astar.T)/2
    c=linalg.solve(astar,H,assume_a="pos")
    g=c.T@astar@c
    g=(g+g.T)/2
    sampled=c.T@kfft@c
    sampled=(sampled+sampled.T)/2
    oldcap,_=all_source_negative_cap(
        v,x,dx,original,orders,c,H,mass,total)
    newcap,_=all_source_negative_cap(
        v,x,dx,refined,orders,c,H,mass,float(newtotal))
    direct_list=[]
    sm10_env_list=[]
    sm37_env_list=[]
    for q in orders_gauss:
        direct,dd=original_fourier_integral(
            original,infos,sources,c,q,"direct")
        oldenv,oo=original_fourier_integral(
            original,infos,sources,c,q,"sm10-envelope")
        newenv,nn=original_fourier_integral(
            refined,infos,sources,c,q,"sm37-envelope")
        dmax=generalized_max(direct,g)
        oldmax=generalized_max(oldenv,g)
        newmax=generalized_max(newenv,g)
        direct_list.append({"order":q,"maximum":dmax,
                            "signed_negative_mass":dd["numeric_signed_negative_mass"]})
        sm10_env_list.append({"order":q,"maximum":oldmax})
        sm37_env_list.append({"order":q,"maximum":newmax})
        # Whole-real original signed envelope ensures actual
        # direct<=new envelope<=old envelope in mathematical
        # operator order; compare only numerically with tolerances.
        eig_new_minus_direct=np.linalg.eigvalsh(newenv-direct)[0]
        eig_old_minus_new=np.linalg.eigvalsh(oldenv-newenv)[0]
        scale=max(1.,float(np.linalg.norm(oldenv)))
        assert eig_new_minus_direct>-1e-6*scale,(
            "negative quadrature/formula inconsistency",eig_new_minus_direct)
        assert eig_old_minus_new>-1e-6*scale,(
            "upper envelope nested ordering inconsistent",eig_old_minus_new)
        assert dmax<=newmax+1e-6*max(1,newmax)
        assert newmax<=oldmax+1e-6*max(1,oldmax)
    q0,q1=direct_list[-2:]
    n0,n1=sm37_env_list[-2:]
    direct_change=abs(q1["maximum"]-q0["maximum"])
    newenv_change=abs(n1["maximum"]-n0["maximum"])
    last_d=q1["maximum"];last_new=n1["maximum"]
    capmax=generalized_max(newcap,g)
    oldcapmax=generalized_max(oldcap,g)
    sampledmax=generalized_max(sampled,g)
    assert capmax>=last_new-1e-5*max(1,capmax),(
        "Original SM10 full Taylor cap should dominate original envelope",
        capmax,last_new)
    return {
      "status":"NONCERTIFYING_NUMERICAL_SELECTED_25_SOURCE_PILOT",
      "physical_grid":n,"fft_padding":pad,
      "sampled_fft_frequency_step":sample["freq_step"],
      "actual_selected_sources":len(sources),
      "original_full_negative_leaf_count":973,
      "refined_exact_original_subcell_count":3892,
      "original_negative_cap_blocks":107,
      "original_negative_cap_source_columns":890,
      "direct_true_formula_negative_gauss":direct_list,
      "old_envelope_analytic_transform_gauss":sm10_env_list,
      "new_envelope_analytic_transform_gauss":sm37_env_list,
      "highest_order_direct_gauss_change":direct_change,
      "highest_order_refined_envelope_gauss_change":newenv_change,
      "coarse_fft_direct_sample_generalized_max":sampledmax,
      "leafwise_direct_gauss_generalized_max":last_d,
      "sm10_envelope_exact_formula_gauss_generalized_max":
          sm10_env_list[-1]["maximum"],
      "sm37_envelope_exact_formula_gauss_generalized_max":last_new,
      "sm10_taylor_cap_generalized_max":oldcapmax,
      "sm37_taylor_cap_generalized_max":capmax,
      "sample_to_leafwise_ratio":sampledmax/max(last_d,1e-30),
      "refined_envelope_to_direct_ratio":last_new/max(last_d,1e-30),
      "sm37_taylor_cap_to_refined_envelope_ratio":
          capmax/max(last_new,1e-30),
      "sm37_taylor_cap_to_direct_ratio":capmax/max(last_d,1e-30),
      "original_theta_51_over_56":THETA,
      "math_certificate":False,
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",
        default="artifacts/sm38_original_negative_leafwise_pilot.json")
    parser.add_argument("--quick",action="store_true")
    args=parser.parse_args()
    governance=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(o for o in governance["obligations"] if o["id"]=="W-ODD-NEG")
    assert governance["active_obligation"]=="W-ODD-NEG"
    assert governance["objective"]["status"]=="open"
    assert governance["governance"]["no_automatic_promotion"] is True
    assert odd["status"]=="open" and "O1/O2" in odd["acceptance"]
    assert "SM38" in governance["evidence"] and "SM38" in odd["evidence"]
    assert "sm38_leafwise_negative_fourier_pilot" in governance["governance"]
    infos,original,oldorders,mass,w,total=geometry()
    refined,orders,stats=refined_signed_original_cap()
    assert oldorders==orders and len(original)==len(refined)==107
    assert stats["new_subcells"]==3892 and stats["source_columns"]==890
    sources=select_sources(infos)
    assert len(sources)==25 and sources[-1][0]=="pole"
    assert validate_physical_transforms(infos,sources)
    cases=[]
    settings=([(4096,4)] if args.quick else [
        (4096,4),(8192,4),(8192,8)])
    orders_gauss=[8,16] if args.quick else [8,16,32]
    for n,pad in settings:
        result=one_case(n,pad,original,refined,orders,infos,
                        sources,mass,total,stats["new_total_cap_mass"],
                        orders_gauss)
        cases.append(result)
        print("SM38 LEAFWISE NUMERICAL DIAGNOSTIC",
              json.dumps(result,sort_keys=True),flush=True)
    print("SM38 scoped original analytic sine-amplitude formulas"
          " verified against separate spatial scipy quadrature"
          " (NOT interval proof). All 973 original negative"
          " leaves integrated independently at Gauss orders",
          orders_gauss,flush=True)
    print("SM38 PASS NUMERICAL ONLY: source-level negative"
          " Fourier reference resolved without coarse FFT bins;"
          " old/refined original whole REAL envelope upper"
          " and Taylor cap compared on SAME 25-source trial."
          " No positive arch full Fourier tail or 470 original"
          " source inverse/residual; complete original odd"
          " O1/O2, even E1-E4, signed whole Weil, CC27, RH OPEN.",
          flush=True)
    obj={
      "status":"NONCERTIFYING_ANALYTIC_TRANSFORM_LEAFWISE_FOURIER_QUADRATURE",
      "canonical_odd_O1_O2":"open",
      "true_original_signed_negative_frequency_leaves":973,
      "true_original_refined_envelope_subcells":3892,
      "original_negative_moment_blocks":107,
      "original_negative_cap_physical_columns":890,
      "quadrature_orders":orders_gauss,
      "analytic_supported_odd_sine_transform_tested_against_spatial_quad":
          True,
      "cases":cases,
      "missing_complete_operator_certificates":[
          "Outward interval original m(xi) and amplitude integral quadrature",
          "Certifiable original pole-free positive/logarithmic Fourier tail",
          "Exact original 470 source positive inverse/strong Galerkin residual",
          "All 470 original generalized eigenvalues and orthogonal residual",
          "Independent analytic audit of SI06/SM10 physical operator identification"
      ]
    }
    path=ROOT/args.output
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,indent=2,allow_nan=False)+"\n")


if __name__=="__main__":
    main()
