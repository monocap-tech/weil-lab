#!/usr/bin/env python3
"""SM36 numerical FEASIBILITY PILOT using genuine original source functions.

Exploratory (NOT proof / NOT an interval certificate):
 * original SI10 signed seven-prime 107 clusters and parity generators,
 * sampled original pole-free A_o multiplier using the digamma/prime formula,
 * source physical Gram and pole-only Sherman--Morrison restoration,
 * all original SM10 107 moment blocks / 890 Taylor synthesis columns,
 * physical source-to-negative-cap overlap matrices and finite trial Ncap,
 * grid/padding convergence and conditioning.

The entire true high-Fourier archimedean tail, exact A_o resolvent
strong residual, all 470 sources, rigorous interval matrices, and
actual full odd O1/O2 ARE NOT VERIFIED by this pilot. High-frequency
cutoff in FFT is NOT legitimate in a proof, and FFT periodic/window
aliasing is not automatically eliminated by merely increasing N.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy import linalg, special

from validate_rpb108_si06_negative_band import ACTIVE, B
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_sm10_explicit_odd_cap_moments import (
    full_upper_leaves, BITS as CAP_BITS, TAU
)
from validate_rpb108_sm17_compact_spectral_gate import (
    KAPPA, KAPPA_STAR, ETA_UP
)

B_FLOAT=float(B)
KAPPA_FLOAT=float(KAPPA)
THETA=51.0/56.0
ROOT=Path(__file__).resolve().parents[1]


def original_multiplier(xi):
    """Exploratory double evaluation of CC27/SI06 ORIGINAL seven-prime m.

    Re psi(1/4+i*pi*xi)-log(pi) minus 2 sum_n
       log(p(n))/sqrt(n)*cos(2*pi*xi*log(n)), n=2,3,4,5,7,8,9.
    Roundoff and digamma library evaluations are NOT rigorously enclosed.
    """
    x=np.asarray(xi,dtype=float)
    arch=np.real(special.digamma(0.25+1j*np.pi*x))-np.log(np.pi)
    prime=np.zeros_like(x)
    for n,p in ACTIVE.items():
        # SI06 ACTIVE[n] is p(n); prime coefficient log(p(n))/sqrt(n).
        prime-=2*np.log(p)/np.sqrt(n)*np.cos(2*np.pi*x*np.log(n))
    return arch+prime


def geometry():
    clusters,w,m,nleaf,npositive=protected_inner_cover()
    assert len(clusters)==107 and nleaf==973 and npositive==9261
    cap,W,Mneg,total=full_upper_leaves()
    assert len(cap)==107 and W==w and Mneg==m
    assert abs(float(Mneg)-37.59565259375)<1e-9
    infos=[]
    for a,b,mj in clusters:
        c=(a+b)/2
        p,_=taylor_order(b-a,9)
        infos.append((float(c),int(p)))
    assert sum(p for c,p in infos)==469
    assert all(infos[i][0]<infos[i+1][0] for i in range(106))
    orders=[taylor_order(cl[-1][1]-cl[0][0],CAP_BITS)[0] for cl in cap]
    assert sum(orders)==890
    return infos,cap,orders,float(m),float(w),float(total)


def select_sources(infos):
    # 14 spread-out ORIGINAL cluster centers, plus critical original
    # witness neighborhoods: near 14.42, 389.56, 882.91.
    ix={int(round(i)) for i in np.linspace(0,len(infos)-1,14)}
    ix.update(min(range(len(infos)), key=lambda j:abs(infos[j][0]-a))
              for a in (14.42,389.56,882.91))
    ix=sorted(ix)
    sources=[("cluster",j,0) for j in ix]
    # Include selected higher polynomial degrees without silently
    # deleting or declaring any ORIGINAL source directions.
    for j in ix[::2]:
        if infos[j][1]>=2:
            sources.append(("cluster",j,1))
    sources.append(("pole",-1,-1))
    assert 16<=len(sources)<=32 and sources[-1][0]=="pole"
    return sources


def physical_columns(n,infos,sources):
    dx=2*B_FLOAT/n
    x=-B_FLOAT+dx*np.arange(n)
    v=np.empty((n,len(sources)),dtype=float)
    for k,(typ,j,degree) in enumerate(sources):
        if typ=="pole":
            v[:,k]=np.sinh(x/2)
        else:
            c=infos[j][0]
            if degree%2==0:
                v[:,k]=x**degree*np.sin(2*np.pi*c*x)
            else:
                v[:,k]=x**degree*np.cos(2*np.pi*c*x)
    return x,dx,v


def fourier_form(v,dx,pad):
    n=len(v)
    N=n*pad
    freq=np.fft.fftfreq(N,d=dx)
    spec=dx*np.fft.fft(v,n=N,axis=0)
    m=original_multiplier(freq)
    plus=KAPPA_FLOAT+np.maximum(m-KAPPA_FLOAT,0.)
    minus=np.maximum(KAPPA_FLOAT-m,0.)
    df=1/(N*dx)
    def form(weights):
        a=spec.conj().T@(spec*weights[:,None])*df
        return np.real((a+a.conj().T)/2)
    return form(plus),form(minus),form(np.ones_like(freq)),{
        "nyquist":1/(2*dx),
        "freq_step":df,
        "min_multiplier":float(np.min(m)),
        "max_multiplier":float(np.max(m)),
        "negative_frequency_bins":int(np.count_nonzero(minus>0))
    }


def all_source_negative_cap(v,x,dx,cap,orders,coefficient,H,mass,total):
    """Actual original 890 U source overlaps, block moment matrices.

    All computations HERE use float64 physical quadrature, including
    107 cluster monomial moments; they are NOT outward-enclosed.
    """
    d=v.shape[1]
    out=np.zeros((d,d))
    ncol=0
    max_abs_overlap=0.
    # Positive (h+kappa) on every ORIGINAL SI10 unresolved leaf.
    # Original SM10 C_j=2 integral w (xi-c)^(k+l) dxi.
    for cluster,p in zip(cap,orders):
        a=cluster[0][0];b=cluster[-1][1]
        c=float((a+b)/2)
        phase=2*np.pi*c*x
        sx=np.sin(phase);cx=np.cos(phase)
        base=2*np.pi*x
        u=np.empty((len(x),p))
        poly=np.ones(len(x))
        for k in range(p):
            u[:,k]=poly*(sx if k%4==0 else
                         cx if k%4==1 else -sx if k%4==2 else -cx)
            poly=poly*base/(k+1)
        # TRUE physical overlap U*Z, without treating Fourier
        # disjointness as physical orthogonality.
        l=(u.T@v)*dx@coefficient
        max_abs_overlap=max(max_abs_overlap,float(np.max(np.abs(l))))
        ncol+=p

        # Positive quadrature factorization, every original leaf.
        # nquad>=p integrates a polynomial degree <=2p-2 exactly
        # in exact arithmetic; float64 is only a pilot estimate.
        nodes,weights=np.polynomial.legendre.leggauss(max(12,p))
        cm=np.zeros((p,p))
        powers=np.arange(p)
        for aa,bb,h in cluster:
            aa=float(aa);bb=float(bb); h=float(h)
            width=(bb-aa)/2
            xx=(aa+bb)/2+width*nodes-c
            mon=xx[:,None]**powers[None,:]
            cm+=2*(h+KAPPA_FLOAT)*width*(
                mon.T@(mon*weights[:,None]))
        out+=(1+float(TAU))*(l.T@cm@l)
    assert ncol==890
    eta=(1+1/float(TAU))*2*B_FLOAT*total*2**(-2*CAP_BITS)
    assert 0<eta<float(ETA_UP)
    ztz=coefficient.T@H@coefficient
    out+=eta*ztz
    return (out+out.T)/2,{"columns":ncol,"blocks":len(cap),
                          "eta":eta,"max_abs_overlap":max_abs_overlap}


def one_run(n,pad,infos,sources,cap,orders,mass,total):
    x,dx,v=physical_columns(n,infos,sources)
    H=(v.T@v)*dx
    H=(H+H.T)/2
    a0,kfreq,gramfft,finfo=fourier_form(v,dx,pad)
    b=(v.T@np.sinh(x/2))*dx
    astar=(a0-2*np.outer(b,b))
    astar=(astar+astar.T)/2
    H_cond=float(np.linalg.cond(H))
    A_cond=float(np.linalg.cond(a0))
    parseval=float(np.linalg.norm(gramfft-H)/max(np.linalg.norm(H),1e-16))
    # Numerical sources can be EXTREMELY ill-conditioned. Never
    # delete singular directions or claim this is a rigorous inverse.
    try:
        t0=linalg.solve(a0,H,assume_a="pos")
        z=linalg.solve(a0,b,assume_a="pos")
        tau=float(1-2*b@z)
        c=linalg.solve(astar,H,assume_a="pos")
        c_sm=t0+(2/tau)*np.outer(z,b@t0)
        relative_pole=float(np.linalg.norm(c-c_sm)/max(np.linalg.norm(c),1e-30))
        G0=(c.T@astar@c)
        G0=(G0+G0.T)/2
        eigen_astar=linalg.eigh(astar,H,eigvals_only=True,
                                check_finite=True)
        ncap,ci=all_source_negative_cap(v,x,dx,cap,orders,c,H,mass,total)
        eigen_cap=linalg.eigh(ncap,G0,eigvals_only=True,
                              check_finite=True)
        # Direct sampled original K integral is diagnostic only.
        nsampled=c.T@kfreq@c
        nsampled=(nsampled+nsampled.T)/2
        ratio=float(np.linalg.norm(ncap-nsampled)/
                    max(np.linalg.norm(nsampled),1e-30))
        resolved={"pole_trial_tau":tau,
             "pole_sherman_morrison_relative_diff":relative_pole,
             "min_generalized_Astar_eigenvalue":float(eigen_astar[0]),
             "max_generalized_cap_trial_eigenvalue":float(eigen_cap[-1]),
             "cap_vs_sample_negative_relative":ratio,
             "cap":ci}
    except (linalg.LinAlgError,ValueError,ZeroDivisionError) as e:
        resolved={"pilot_solve_failed":str(e),
                  "not_certified":True}
    return {"nphysical":n,"pad":pad,"pilot_sources":len(sources),
            "gram_condition":H_cond,"polefree_stiffness_condition":A_cond,
            "sampled_parseval_relative":parseval,**finfo,**resolved}


def main():
    pa=argparse.ArgumentParser()
    pa.add_argument("--output",default="artifacts/sm36_original_numerical_pilot.json")
    pa.add_argument("--quick",action="store_true")
    args=pa.parse_args()
    # Important original signed multiplier normalization checks.
    anchors=np.array([0.3,389.38,389.56,389.75,882.91])
    mm=original_multiplier(anchors)
    assert mm[0]>1.4 and mm[1]>2 and mm[2]<-0.4
    assert mm[3]>2 and mm[4]<-0.08
    infos,cap,orders,mass,width,total=geometry()
    sources=select_sources(infos)
    runs=[(4096,4),(8192,4)] if args.quick else [
        (4096,4),(8192,4),(8192,8)]
    metrics=[]
    for n,pad in runs:
        result=one_run(n,pad,infos,sources,cap,orders,mass,total)
        metrics.append(result)
        print("SM36 PILOT",json.dumps(result,sort_keys=True),flush=True)
    # ALL numerical values are exploratory. No FFT grid comparison can
    # certify the ORIGINAL high log-frequency tail or a strong residual.
    output={
      "status":"NUMERICAL_EXPLORATION_ONLY_NOT_WHOLE_OPERATOR_CERTIFICATE",
      "canonical_odd_O1_O2":"open",
      "source_count_entire":470,
      "pilot_source_descriptors":[
          {"kind":t,"center":None if j<0 else infos[j][0],"degree":k}
          for t,j,k in sources],
      "original_negative_clusters":len(cap),
      "original_negative_cap_columns":sum(orders),
      "original_negative_mass":mass,
      "multiplier_anchor_values":dict(zip(
          [str(y) for y in anchors],[float(z) for z in mm])),
      "cases":metrics,
      "missing_certificate":[
          "true whole-frequency positive pole-free A_o stiffness",
          "whole positive archimedean logarithmic Fourier tail",
          "rigorous Fourier/quadrature and physical Gram intervals",
          "positive resolvent whole strong residual R*R",
          "470-source complete Galerkin solve and conditioning",
          "full 470-source 890 negative-cap certified Loewner sign"
      ]
    }
    path=ROOT/args.output
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(output,indent=2,allow_nan=False)+"\n")
    print("SM36 PASS NUMERICAL FEASIBILITY ONLY:"
          " original physical source/whole sampled Fourier A0,"
          " original pole restoration and original complete"
          " 107-block 890-source finite trial coupling computed;"
          " full original odd sign, even, Weil, RH OPEN",flush=True)


if __name__=="__main__":
    main()
