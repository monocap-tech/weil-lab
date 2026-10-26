#!/usr/bin/env python3
"""Complete original signed mixed terms from the physical 2D anchor to xcos.

Compute only Q(f,r), Q(g,r), Q(r,r), with r=xcos+alpha*sinh.
All low-frequency cells and both signs of the infinite tail are paid.
A failed sufficient Schur lower is explicitly inconclusive.
"""
import argparse
from functools import lru_cache
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import validate_rpb108_mg07_signed_sine_pole_2d as C
from validate_rpb108_sm42_original_physical_gram_and_low_gate import (
    I,F1,F2,pole_sin,pole_xcos)
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si06_negative_band import LN
from validate_rpb108_mg07_global_negative_sup import exact_bound
from validate_rpb108_sm41_original_positive_log_tail import (
    mathematical_global_original_positive_multiplier_majorant)

import validate_rpb108_sm42_original_physical_gram_and_low_gate as P
# Identical exact phase intervals recur in F0/F1/F2 within each cell.
P.sin_cos_period=lru_cache(maxsize=64)(P.sin_cos_period)
ROOT=Path(__file__).resolve().parents[1]
ANCHOR_SHA='3a86fee52200c586b07b04f49ea50585be2e570ac172762206dda1bafe811db4'
L=F(12)
LOG_L_UP=4*F(347,500)

def absmax(x):
    return max(abs(x[0]),abs(x[1]))

def bounds(v):
    return v.l,v.h

def tail_integral(p):
    # Integral_L^infinity (17+ln xi)/xi^p, with exact upward ln L.
    assert p>=2
    n=F(p-1)
    return L**(1-p)*((17+LOG_L_UP)/n+1/(n*n))

def tail_product(a,b):
    return 2*sum((x*y*tail_integral(i+j+2)
                  for i,x in enumerate(a) for j,y in enumerate(b)),F(0))

def evaluate(anchor_path):
    raw=Path(anchor_path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==ANCHOR_SHA
    cap=json.loads(raw)
    assert cap['status']=='CERTIFIED_CONDITIONAL_PHYSICAL_2D_ANCHOR_INVERSE_CAP'
    assert cap['complete_physical_anchor_inverse_diagonal_upper']==['8000','24']
    assert cap['input_source_sha']=='8844685d3e72a3d38f943b084b6e5bc70ef3d09c'
    assert C.B==F(11,10) and C.CENTER==F(37,64)
    assert C.D2+C.LOWARCH<C.CURVE==2300
    assert L<16 and LN[2][1]<F(347,500)
    assert mathematical_global_original_positive_multiplier_majorant()
    assert F(exact_bound()['original_negative_norm_upper'])<17
    # Therefore |m(xi)| <= 17+ln|xi| for |xi|>=12, including
    # negative m: (-m)+ <= (kappa-m)+ <= Hsup < 17.
    clusters,_,mass,leaves,_=C.protected_inner_cover()
    assert len(clusters)==107 and leaves==973 and mass<F(38)
    assert clusters[0][:2]==(F(0),F(37,32))
    assert taylor_order(clusters[0][1]-clusters[0][0],9)[0]>=2
    assert all(not(a<L<b) for a,b,m in clusters)
    M2=sum((m/a**2 for a,b,m in clusters if a>=L),F(0))
    assert 0<M2<F(423,25000)
    sinB,cosB=C.cos_sin_pi_multiple(2*C.B*C.CENTER)
    sh=C.hyperbolic_interval(C.B/2,'sinh')
    ch=C.hyperbolic_interval(C.B/2,'cosh')
    # Rational endpoint-aligned basis change inside span(xcos,sinh).
    alpha_exact=-C.B*((cosB[0]+cosB[1])/2)/sh.mid()
    alpha=F((alpha_exact*10**6+F(1,2)).__floor__(),10**6)
    pi=I(C.PI[0],C.PI[1])
    omega=(2*C.PI[0]*C.CENTER,2*C.PI[1]*C.CENTER)
    wup=omega[1]
    pi_lo=C.PI_LO
    correction=1-(wup/(2*pi_lo*L))**2
    assert correction>0
    packet_tails=[]
    for a,b,name in C.BASIS:
        ep=C.above(C.abs_upper(C.add(C.scl(a,sinB),C.scl(b,bounds(sh)))),10**12)
        dv=C.above(C.abs_upper(C.add(C.scl(a,C.mul(omega,cosB)),C.scl(b/2,bounds(ch)))),10**12)
        n1=abs(a)*C.abs_upper(sinB)*wup*wup+abs(b)*sh.h/4
        n2=abs(a)*wup**3*C.abs_upper(cosB)+abs(b)*ch.h/8
        # The original exact closed sine/sinh Fourier majorant:
        # |T| <= (ep+dv/k+n1/(k^2-w^2)+n2/(k*(k^2-w^2)))/(pi*xi).
        # k>=2*pi_lo*xi, k^2-w^2 >= correction*(2*pi_lo*xi)^2.
        coeff=[ep/pi_lo,dv/(2*pi_lo**2),
               n1/(4*pi_lo**3*correction),n2/(8*pi_lo**4*correction)]
        coeff=[C.above(v,10**12) for v in coeff]
        assert all(v>=0 for v in coeff)
        packet_tails.append(coeff)
    endpoint=C.add(C.scl(C.B,cosB),C.scl(alpha,bounds(sh)))
    deriv=C.add(C.add(cosB,C.scl(-C.B,C.mul(omega,sinB))),
                C.scl(alpha/2,bounds(ch)))
    # Integral |(xcos(wx)+alpha*sinh(x/2))''|
    # <=4 B w + w^2 B^2 + |alpha|*(cosh(B/2)-1).
    second_l1=4*C.B*wup+wup*wup*C.B**2+abs(alpha)*(ch.h-1)
    rtail=[C.abs_upper(endpoint)/pi_lo,
           (2*C.abs_upper(deriv)+second_l1)/(4*pi_lo**2)]
    rtail=[C.above(v,10**12) for v in rtail]
    assert all(v>=0 for v in rtail)
    beta_r=rtail[0]+rtail[1]/L
    high_cross=[C.above(tail_product(t,rtail),10**12) for t in packet_tails]
    high_rnegative=C.above(M2*beta_r**2,10**12)
    phys=C.physical_anchor()
    q=tuple(map(F,phys['physical_sine_sinh_cross_Gram_interval']))
    S=tuple(map(F,phys['physical_sinh_self_Gram_interval']))
    overlaps=[C.sum_i(C.scalar_i(a,q),C.scalar_i(b,S)) for a,b,_ in C.BASIS]
    r_raw=pole_xcos(C.CENTER,sh,ch)+alpha*I(*S)
    r_overlap=(C.below(r_raw.l,10**12),C.above(r_raw.h,10**12))
    overlaps.append(r_overlap)
    pairs=((0,2),(1,2),(2,2))
    poles=[C.scalar_i(2,C.mul_i(overlaps[i],overlaps[j])) for i,j in pairs]
    d2=[C.above(4*C.PI[1]**2*(abs(a)*2*C.B**3/3+
                            abs(b)*2*C.B**3/3*sh.h)) for a,b,_ in C.BASIS]
    d2.append(C.above(2*C.PI[1]**2*C.B**4+
                     abs(alpha)*4*C.PI[1]**2*2*C.B**3/3*sh.h))
    sums=[[F(0),F(0)] for _ in pairs]
    count=0
    for left,right,h in C.REGIONS:
        for j in range(int((right-left)/h)):
            l=left+j*h;mid=l+h/2;r=l+h
            li=C.signed_m_at(l);ri=C.signed_m_at(r)
            lo=sum(li)/2;hi=sum(ri)/2
            m0=(lo+hi)/2;m1=(hi-lo)/h
            eps=C.above(max((li[1]-li[0])/2,(ri[1]-ri[0])/2)+C.CURVE*h*h/8)
            wabs=abs(m0)+abs(m1)*h/2+eps
            base=C.qbasis(mid,sh,ch)
            interval=[C.qinterval(base,a,b) for a,b,_ in C.BASIS]
            rv=(F1(mid+C.CENTER)+F1(mid-C.CENTER))/2+alpha*pole_sin(mid,sh,ch)
            rd=pi*(F2(mid+C.CENTER)+F2(mid-C.CENTER))+alpha*base[3]
            # Match the anchor's outward endpoint compaction before products.
            # Raw F1/F2/pole Fractions otherwise carry huge denominators.
            interval.append(((C.below(rv.l,10**12),C.above(rv.h,10**12)),
                             (C.below(rd.l,10**12),C.above(rd.h,10**12))))
            vals=[];ders=[];errs=[];mx=[]
            for k,(tv,dt) in enumerate(interval):
                v=sum(tv)/2;d=sum(dt)/2
                E=C.above((tv[1]-tv[0])/2+(dt[1]-dt[0])*h/4+d2[k]*h*h/8)
                vals.append(v);ders.append(d);errs.append(E)
                mx.append(abs(v)+abs(d)*h/2)
            for k,(i,jj) in enumerate(pairs):
                v,d=vals[i],ders[i];w,e=vals[jj],ders[jj]
                baseline=2*(h*m0*v*w+h**3/F(12)*(m0*d*e+m1*(v*e+d*w)))
                error=2*h*(eps*mx[i]*mx[jj]+
                     wabs*(errs[i]*mx[jj]+errs[jj]*mx[i]+errs[i]*errs[jj]))
                # Both endpoints rounded OUTWARD independently.
                sums[k][0]+=C.below(baseline-error,10**12)
                sums[k][1]+=C.above(baseline+error,10**12)
            count+=1
        print('mixed cells',count,flush=True)
    assert count==7168
    signed=[(s[0]-p[1],s[1]-p[0]) for s,p in zip(sums,poles)]
    complete_cross=[(signed[i][0]-high_cross[i],signed[i][1]+high_cross[i]) for i in range(2)]
    bmax=list(map(absmax,complete_cross))
    rlower=signed[2][0]-high_rnegative
    anisotropic=8000*bmax[0]**2+24*bmax[1]**2
    isotropic=7100*(bmax[0]**2+bmax[1]**2)
    penalty=min(anisotropic,isotropic)
    schur_lower=rlower-penalty
    return dict(status='CERTIFIED_COMPLETE_ORIGINAL_MIXED_INTERVALS_AND_SUFFICIENT_SCHUR_LOWER',
        source_center=str(C.CENTER),xcos_degree=1,original_cluster_index=0,
        rational_sinh_alignment=str(alpha),original_lowband_cells=count,
        accepted_anchor_run_id=40263282082,accepted_anchor_artifact_id=12625472360,
        anchor_json_sha256=ANCHOR_SHA,
        complete_cross_intervals=[[str(x) for x in row] for row in complete_cross],
        high12_complete_cross_absolute_payments=list(map(str,high_cross)),
        high12_abs_multiplier_majorant='|m(xi)| <= 17+ln|xi|',
        anchor_packet_tail_coefficients=[[str(x) for x in row] for row in packet_tails],
        new_source_packet_tail_coefficients=list(map(str,rtail)),
        new_source_full_signed_diagonal_lower=str(rlower),
        high12_negative_diagonal_payment=str(high_rnegative),
        high12_weighted_negative_mass=str(M2),
        high12_new_source_beta=str(beta_r),
        lowband_signed_plus_pole_intervals=[[str(x) for x in row] for row in signed],
        anisotropic_schur_penalty_upper=str(anisotropic),
        isotropic_schur_penalty_upper=str(isotropic),
        selected_schur_penalty_upper=str(penalty),
        complete_signed_scalar_schur_lower=str(schur_lower),
        strict_scalar_schur_positive_certified=schur_lower>0,
        nonpositive_lower_is_not_actual_negative_witness=True,
        full_remaining_468_source_and_infinite_schur='OPEN',
        SM34_energy_dual_transport='OPEN',
        inherited_analytic_domain_review='OPEN',whole_original_odd_even_CC27_Weil_RH='OPEN')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--anchor',required=True)
    p.add_argument('--output',default='artifacts/mg07_original_complete_xcos_coupling.json')
    args=p.parse_args()
    z=evaluate(args.anchor)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(z,indent=2)+'\n')
    print('COMPLETE MIXED COUPLING',*[float(F(x)) for x in z['high12_complete_cross_absolute_payments']],
          'Schur lower',float(F(z['complete_signed_scalar_schur_lower'])),
          'strict pass',z['strict_scalar_schur_positive_certified'],flush=True)
