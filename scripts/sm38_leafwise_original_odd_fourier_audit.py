#!/usr/bin/env python3
"""SM38: source-ANALYTIC original odd Fourier amplitudes and leafwise Kneg.

NONCERTIFYING float64 experiment on SAME original SI10 25 source space:
 * all 973 unresolved negative leaves / 3892 genuine SM37 real subcells;
 * at Gauss orders 4,8,16 integrate actual original signed seven-prime
   Kneg=(kappa-m(xi))_+, SM37 envelope, SM10 old envelope;
 * evaluate Fourier sine amplitudes of actual selected original odd
   x^0 sin(2pi c x), x cos(2pi c x), and sinh(x/2) analytically,
   with exact finite B=11/10 support (NO FFT frequency sampling);
 * use SAME sampled pole-conditioned source Galerkin solves as SM36/37,
   compare complete 25x25 generalized spectral maxima with SM37
   890-column cap and prior FFT direct Kneg;
 * return cap decomposition into multiplier envelope vs moment/Taylor/
   Young and residual; original Fourier normalization checked by an
   independent discrete physical integral on selected anchor points.

Gauss orders, finite-digit trig/special.digamma, approximate pole-free
positive Astar trial and uncertified whole high-frequency arch/log tail
are NOT interval proof. Complete 470 source W_odd O1/O2/Weil/RH OPEN.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy import linalg

from sm36_original_odd_numerical_pilot import (
    B_FLOAT,KAPPA_FLOAT,THETA,ROOT,geometry,select_sources,
    physical_columns,fourier_form,all_source_negative_cap,
    original_multiplier
)
from validate_rpb108_sm37_refined_original_negative_cap import (
    refined_signed_original_cap
)
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves,BITS,TAU
)

def sincprime(u):
    """Derivative of sin(pi*u)/(pi*u), stable at removable zero."""
    u=np.asarray(u,dtype=float)
    o=np.empty_like(u)
    small=np.abs(u)<1e-3
    q=u[small]
    pi=np.pi
    o[small]=q*(-pi*pi/3+q*q*(pi**4/30+q*q*(
        -pi**6/840+q*q*pi**8/45360)))
    q=u[~small]
    o[~small]=np.cos(pi*q)/q-np.sin(pi*q)/(pi*q*q)
    return o


def supported_odd_sine_transform(xi,infos,sources):
    """T_g(xi)=integral_-B^B g(x) sin(2pi*xi*x) dx, closed formula.

    Genuinely *supported* on [-B,B], not disjoint Fourier packet model.
    Each original selected basis has k=0 sine, k=1 x*cos, or pole.
    """
    freq=np.asarray(xi,dtype=float).reshape(-1)
    ans=np.empty((len(freq),len(sources)),dtype=float)
    for j,(typ,index,degree) in enumerate(sources):
        if typ=="pole":
            a=0.5;b=2*np.pi*freq
            ans[:,j]=2*(a*np.cosh(a*B_FLOAT)*np.sin(b*B_FLOAT)
                       -b*np.sinh(a*B_FLOAT)*np.cos(b*B_FLOAT))/(a*a+b*b)
        else:
            c=infos[index][0]
            minus=2*B_FLOAT*(c-freq)
            plus=2*B_FLOAT*(c+freq)
            if degree==0:
                ans[:,j]=B_FLOAT*(np.sinc(minus)-np.sinc(plus))
            elif degree==1:
                ans[:,j]=B_FLOAT**2/np.pi*(
                    sincprime(minus)-sincprime(plus))
            else:
                raise AssertionError("The SM38 pilot selects only degree 0/1")
    assert np.all(np.isfinite(ans))
    return ans


def check_independent_physical_transform(infos,sources):
    # Independent trapezoidal spatial integration, used ONLY to
    # catch wrong physical factor/sign in analytic closed formula.
    # Subdivide true physical support strongly enough that both
    # high-frequency source and sine test products are resolved.
    xi=np.array([0.2,14.42,389.56,882.91],dtype=float)
    from sm36_original_odd_numerical_pilot import physical_columns
    x,dx,v=physical_columns(32768,infos,sources)
    quad=dx*(v.T@np.sin(2*np.pi*x[:,None]*xi[None,:]))
    closed=supported_odd_sine_transform(xi,infos,sources).T
    err=np.max(np.abs(quad-closed))
    assert err<3e-3,("analytic-vs-spatial original sine Fourier mismatch",err)
    # Exact parity: T_odd(0)=0, including the original sinh pole.
    assert np.max(np.abs(supported_odd_sine_transform(
        np.array([0.]),infos,sources)))<1e-14
    return float(err)


def prepare_real_subcells(refined,old):
    assert len(refined)==len(old)==107
    centers=[];halfwidth=[];newweight=[];oldweight=[]
    allpositive=0
    for j,(cnew,cold) in enumerate(zip(refined,old)):
        assert len(cnew)==4*len(cold)
        for k,(aa,bb,hh) in enumerate(cold):
            assert bb>aa
            parent=float(hh)+KAPPA_FLOAT
            for l in range(4):
                a,b,hnew=cnew[4*k+l]
                assert a>=aa and b<=bb
                centers.append(float((a+b)/2))
                halfwidth.append(float((b-a)/2))
                new=float(hnew)+KAPPA_FLOAT
                assert new>=0 and new<=parent+1e-14
                newweight.append(new)
                oldweight.append(parent)
                if new<=1.0000001e-6:allpositive+=1
    assert len(centers)==3892
    return (np.asarray(centers),np.asarray(halfwidth),
            np.asarray(newweight),np.asarray(oldweight),allpositive)


def gauss_frequency_integrals(
    original_sources,infos,c,centers,halfwidth,wnew,wold,order):
    """Full physical original sine Fourier matrix via per-subcell Gauss.

    Each column in original_sources is exact-formula odd sine, odd
    x*cos or sinh. The trial solution is a linear combination
    of these original functions with c from SM36 sampled Astar.
    """
    nodes,weights=np.polynomial.legendre.leggauss(order)
    xi=(centers[:,None]+halfwidth[:,None]*nodes[None,:]).ravel()
    q=(halfwidth[:,None]*np.broadcast_to(weights,(
        len(centers),order))).ravel()
    assert len(xi)==3892*order
    # All 3892 original certified frequency cells are integrated.
    # We only integrate the ORIGINAL negative-frequency support.
    truew=np.maximum(KAPPA_FLOAT-original_multiplier(xi),0.)
    envnew=np.repeat(wnew,order)
    envold=np.repeat(wold,order)
    # Narrow cells and outward certified envelopes should dominate
    # the actual numerical signed multiplier at quadrature nodes.
    env_mismatch=float(np.max(truew-envnew))
    if env_mismatch>2e-5:
        raise RuntimeError(
            "SM38 sign-envelope appears violated on original real"
            " quadrature samples; do not infer an operator cap "
            f"(violation={env_mismatch})")
    T=supported_odd_sine_transform(xi,infos,original_sources)
    F=T@c
    assert F.shape==(len(xi),len(original_sources))
    def kernel(w):
        # Full original odd Fourier |Z fhat|² has +/- symmetry
        # factor 2; T is integral_-B^B f(x)sin(2pi*xi*x) dx.
        z=2*q*w
        a=F.T@(F*z[:,None])
        return (a+a.T)/2
    direct=kernel(truew)
    env=kernel(envnew)
    oldenv=kernel(envold)
    # Each envelope is a PSD operator cap *before* source Taylor/
    # Young approximation; all cross interactions retained here.
    return direct,env,oldenv,{
        "frequency_gauss_order":order,
        "original_signed_subcells":len(centers),
        "original_original_leaves":973,
        "real_frequency_points":len(xi),
        "max_new_envelope_minus_true_violation":env_mismatch,
        "true_kneg_sampled_positive_frequency_mass":
            float(2*np.sum(q*truew)),
        "refined_envelope_positive_frequency_mass":
            float(2*np.sum(q*envnew)),
        "original_envelope_positive_frequency_mass":
            float(2*np.sum(q*envold)),
        "sampled_original_negative_frequency_nodes":
            int(np.count_nonzero(truew)),
    }


def generalized_max(A,G):
    A=(A+A.T)/2
    G=(G+G.T)/2
    return float(linalg.eigh(A,G,eigvals_only=True,check_finite=True)[-1])


def one_case(n,pad,orders=(4,8,16)):
    infos,old,oldorders,mass,width,oldtotal=geometry()
    sources=select_sources(infos)
    assert len(sources)==25 and sources[-1][0]=="pole"
    refined,reforders,stats=refined_signed_original_cap(4)
    assert reforders==oldorders and stats["source_columns"]==890
    centers,halfwidth,wnew,wold,nfloor=prepare_real_subcells(refined,old)
    x,dx,v=physical_columns(n,infos,sources)
    H=v.T@v*dx
    A0,negfft,_,fmeta=fourier_form(v,dx,pad)
    b=v.T@np.sinh(x/2)*dx
    Astar=(A0-2*np.outer(b,b))
    Astar=(Astar+Astar.T)/2
    c=linalg.solve(Astar,H,assume_a="pos")
    G=(c.T@Astar@c)
    G=(G+G.T)/2
    oldcap,_=all_source_negative_cap(
        v,x,dx,old,oldorders,c,H,mass,oldtotal)
    newcap,_=all_source_negative_cap(
        v,x,dx,refined,reforders,c,H,mass,
        float(stats["new_total_cap_mass"]))
    sampledfft=c.T@negfft@c
    fft_max=generalized_max(sampledfft,G)
    oldcapmax=generalized_max(oldcap,G)
    newcapmax=generalized_max(newcap,G)
    transform_err=check_independent_physical_transform(infos,sources)
    quad=[]
    for order in orders:
        true,env,oldenv,meta=gauss_frequency_integrals(
            sources,infos,c,centers,halfwidth,wnew,wold,order)
        tru_max=generalized_max(true,G)
        env_max=generalized_max(env,G)
        oldenv_max=generalized_max(oldenv,G)
        # Numerical diagnostics of complete coupled Loewner
        # orientation, never substituted for interval certificates.
        scale=max(float(np.linalg.norm(oldcap)),1e-25)
        eig={
          "true_to_new_envelope":float(np.linalg.eigvalsh(
              (env-true+env.T-true.T)/2)[0]),
          "new_envelope_to_old":float(np.linalg.eigvalsh(
              (oldenv-env+oldenv.T-env.T)/2)[0]),
          "new_envelope_to_new_moment_cap":float(np.linalg.eigvalsh(
              (newcap-env+newcap.T-env.T)/2)[0])
        }
        meta.update({
           "direct_leafwise_true_negative_generalized_max":tru_max,
           "new_envelope_leafwise_generalized_max":env_max,
           "old_envelope_leafwise_generalized_max":oldenv_max,
           "moment_cap_SM37_generalized_max":newcapmax,
           "moment_cap_SM10_generalized_max":oldcapmax,
           "moment_synthesis_inflation":newcapmax/max(env_max,1e-30),
           "signed_envelope_inflation":env_max/max(tru_max,1e-30),
           "old_envelope_inflation":oldenv_max/max(tru_max,1e-30),
           "fft_direct_negative_generalized_max":fft_max,
           "fft_to_leafwise_true_ratio":fft_max/max(tru_max,1e-30),
           "moment_minus_envelope_loewner_min_eigenvalues":eig,
           "all_eigen_checks_diagnostic":True,
           "true_operator_sign_certified":False
        })
        quad.append(meta)
        print("SM38 ANALYTIC-SOURCE LEAFWISE QUADRATURE"
              " NONCERTIFYING",json.dumps(meta,sort_keys=True),flush=True)
        if eig["new_envelope_to_new_moment_cap"] < -1e-5*scale:
            # This indicates either physical source quadrature/FFT
            # aliasing or a genuine source cap normalization error.
            # The scoped envelope proof is inherited independently,
            # so label the pilot inconsistent and inspect it.
            print("SM38 WARNING sampled moment-vs-envelope"
                  " complete matrix numerically inconsistent;"
                  " investigate original physical grid aliasing"
                  " before using any sampled ratio.",flush=True)
    # Numerical-only engineering diagnosis; not an interval
    # source Fourier integral or original spectral certificate.
    q8,q16=quad[1],quad[2]
    a=q8["direct_leafwise_true_negative_generalized_max"]
    bmax=q16["direct_leafwise_true_negative_generalized_max"]
    relative_gauss_drift=abs(a-bmax)/max(abs(bmax),1e-30)
    assert relative_gauss_drift<1e-3,(
        "SM38 inadequate leafwise Gauss convergence",relative_gauss_drift)
    assert q16["signed_envelope_inflation"]>5
    assert q16["moment_synthesis_inflation"]<1.05
    assert q16["direct_leafwise_true_negative_generalized_max"]>THETA
    print("SM38 DIAGNOSIS NUMERICAL ONLY: Gauss8/16"
          " original leafwise relative change",relative_gauss_drift,
          "signed-envelope-only spectral inflation",
          q16["signed_envelope_inflation"],
          "moment/Young additional ratio",
          q16["moment_synthesis_inflation"],
          "FFT direct/leafwise direct",
          q16["fft_to_leafwise_true_ratio"],
          "=> MULTIPLIER ENVELOPE dominates selected-source"
          " original signed-negative cap excess; no O1/O2.",
          flush=True)
    return {
      "gauss8_to_16_relative_direct_change":relative_gauss_drift,
      "numerical_bottleneck":"ORIGINAL_REAL_FREQUENCY_MULTIPLIER_ENVELOPE",
      "original_pilot_source_count":len(sources),
      "physical_grid":n,"positive_fourier_fft_padding":pad,
      "original_negative_clusters":107,
      "original_negative_moment_columns":890,
      "max_fft_direct_negative":fft_max,
      "max_SM10_moment_cap":oldcapmax,
      "max_SM37_moment_cap":newcapmax,
      "analytic_transform_vs_independent_spatial_max_abs":
          transform_err,
      "old_973_leaves_refined_into":len(centers),
      "cells_at_spd_floor":nfloor,
      "quadrature_orders":quad,
      "pole_denominator_selected_trial":
          float(1-2*b@linalg.solve(A0,b,assume_a="pos")),
      "numerical_only":True,
    }


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/sm38_leafwise_original_odd_fourier.json")
    p.add_argument("--quick",action="store_true")
    args=p.parse_args()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open" and odd["status"]=="open"
    assert m["governance"]["no_automatic_promotion"] is True
    assert "O1/O2" in odd["acceptance"]
    assert all(x in odd["evidence"] and x in m["evidence"]
               for x in ("SM36","SM37","SM38"))
    assert "sm38_leafwise_original_fourier_diagnostic" in m["governance"]
    configs=[(4096,4)] if args.quick else [(4096,4),(8192,8)]
    cases=[one_case(n,pad) for n,pad in configs]
    data={
      "status":"ORIGINAL_ANALYTIC_SOURCE_LEAFWISE_NUMERICAL_DIAGNOSTIC_ONLY",
      "canonical_odd_O1_O2":"open",
      "quadrature_status":"NONCERTIFYING_FLOAT64_NOT_INTERVAL_PROOF",
      "original_source_carrier":470,"pilot_source_count":25,
      "negative_original_signed_leaves":973,
      "certified_SM37_original_subcells":3892,
      "original_complete_negative_moment_columns":890,
      "cases":cases,
      "outstanding":[
         "rigorous interval derivative/gauss quadrature remainder",
         "certified full archimedean positive log Fourier tail",
         "genuine 470-original-source Astar inverse and strong residual",
         "entire true original 470-source generalized Loewner gate",
         "independent original signed Fourier physical-domain audit"
      ]
    }
    out=ROOT/args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(data,indent=2,allow_nan=False)+"\n")
    print("SM38 scoped numerical feasibility COMPLETE:"
          " entire ORIGINAL signed negative support integrated"
          " with source-ANALYTIC sine Fourier on each of 3892 cells,"
          " original signed multiplier, old/new envelope and same"
          " 890 original physical source moments separated."
          " No true original odd spectral closure, Weil or RH.",
          flush=True)


if __name__=="__main__":
    main()
