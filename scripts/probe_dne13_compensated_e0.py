#!/usr/bin/env python3
"""NON-CERTIFYING original Weil compensated e0 source diagnostic.

Gauss rules are convergence controls, not outward interval certificates.
Retains original endpoint logs, all six prime powers and both signed poles.
"""
import json, math
import numpy as np
from scipy.special import roots_legendre, eval_legendre

A=53/50
ACTIVE=(2,3,4,5,7,8)
C=-np.euler_gamma-math.log(2*math.pi)

def basis(n,x):
    return math.sqrt((2*n+1)/(2*A))*eval_legendre(n,np.asarray(x)/A)

def regular(t):
    t=np.asarray(t)
    # Stable local expansion of e^(t/2)/(2 sinh(t))-1/(2t).
    small=t<1e-3
    out=np.empty_like(t)
    z=t[small]
    out[small]=.25-z/48-z*z/32+7*z**3/11520+5*z**4/1536
    z=t[~small]
    out[~small]=np.exp(-z/2)/(-np.expm1(-2*z))-1/(2*z)
    return out

def run(order):
    z,g=roots_legendre(order)
    cuts=sorted(set([-A,0.,A]+[x for n in ACTIVE for x in (A-math.log(n),-A+math.log(n)) if -A<x<A]))
    xs=[];ws=[]
    # Square substitution in both boundary panels resolves integrable logs.
    for l,r in zip(cuts[:-1],cuts[1:]):
        if l==-A or r==A:
            length=math.sqrt(r-l);t=(z+1)*length/2
            xs.append(-A+t*t if l==-A else A-t*t)
            ws.append(g*length*t)
        else:
            xs.append((r+l)/2+(r-l)*z/2);ws.append(g*(r-l)/2)
    x=np.concatenate(xs);weight=np.concatenate(ws)
    deg=[0,112,114]
    p=np.array([basis(n,x) for n in deg])
    H=np.array([sum(1/k for k in range(1,n+1)) for n in deg])
    arch=(C+H[:,None]-.5*np.log((A-x)*(A+x)))*p
    # Split convolution at y=x: each regular kernel is analytic on its side.
    for side in (-1,1):
        length=(x+A) if side==-1 else (A-x)
        t=length[:,None]*(z+1)/2
        y=x[:,None]+side*t
        rw=regular(t)*g[None,:]*length[:,None]/2
        for i,n in enumerate(deg):arch[i]-=np.sum(rw*basis(n,y),axis=1)
    source=arch.copy()
    for n in ACTIVE:
        ell=math.log(n);c=math.log(2 if n in (4,8) else n)/math.sqrt(n)
        for sign in (-1,1):
            y=x+sign*ell;mask=np.abs(y)<A
            for i,k in enumerate(deg):source[i,mask]-=c*basis(k,y[mask])
    # Independent smooth full-interval Gauss rule for actual even pole moments.
    for i,n in enumerate(deg):
        moment=A*np.dot(g,basis(n,A*z)*np.cosh(A*z/2))
        source[i]+=2*moment*np.cosh(x/2)
    gram=(source*weight)@p.T
    asym=np.max(np.abs(gram-gram.T))
    gram=(gram+gram.T)/2
    coeff=np.linalg.solve(gram[1:,1:],gram[1:,0])
    w=p[0]-coeff@p[1:]
    s=source[0]-coeff@source[1:]
    retained=np.array([np.dot(weight*s,basis(n,x)) for n in range(0,112,2)])
    full=np.dot(weight,s*s)
    projected=full-np.dot(retained,retained)
    direct=s.copy()
    for value,n in zip(retained,range(0,112,2)):
        direct-=value*basis(n,x)
    direct_square=np.dot(weight,direct*direct)
    assert abs(direct_square-projected)<1e-9
    energy=gram[0,0]-np.dot(gram[0,1:],coeff)
    high=np.array([np.dot(weight*s,p[i]) for i in (1,2)])
    return dict(order=order,native_block=gram.tolist(),symmetry_error=float(asym),
        correction_coefficients=coeff.tolist(),compensated_source_square=float(full),
        retained_projection_square=float(np.dot(retained,retained)),
        full_F112_source_residual_square=float(projected),
        direct_projected_source_square=float(direct_square),
        two_high_pairings=high.tolist(),corrected_energy=float(energy),
        physical_gate_budget=float(.207*energy),
        physical_gate_ratio=float(projected/(.207*energy)),
        constant_pairing_error=float(gram[0,0]-.0401520842754207446870744),
        source_norm_uncompensated=float(np.dot(weight,source[0]**2)),
        corrected_vector_mass=float(np.dot(weight,w*w)),certified=False)

if __name__=='__main__':
    out=dict(stage='DNE13 compensated e0 diagnostic',aperture='53/50',
        method='native complete source + split Gauss rules + endpoint square substitution',
        runs=[run(n) for n in (160,240,360)],
        interval_certificate=False,actual_null_exclusion=False,RH=False)
    print(json.dumps(out,indent=2))
