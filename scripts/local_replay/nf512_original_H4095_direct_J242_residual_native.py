#!/usr/bin/env python3
"""NF512 staged authentic original H4095 direct J242 residual calculation.

Instead of computing 242 local mixed moments and 242**2 local Gram entries,
form the SAME original exterior-optimal J242 selected fit as a single
source-correlated physical function in its historic D frame. Recenter
this function and complete original W at the ACTUAL symmetric H4095 cell,
and rigorously integrate their signed difference squared.

A second source-native physical Gram endpoint contraction computes the
complete local selected leverage tau_H. The script fails closed if its
original-source intervals cannot decide a strict cell-specific gate.

The old original NF404 criterion and actual NF407/NF406 complete source
are not changed. No Weil image/domain or RH inference is permitted.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,arb_mat,ctx
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import verify_nf504_original_J8_support_saturated_exterior_native as source
import verify_rpb108_si29_full_J_L2_normalization as phys
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf380_original_archived_signed_dual import interval
from verify_nf374_original_matched_curvature import load,RANK_SHA

B=F(11,10);BO=F(549,500);M=4096
J=4095;H=BO/M;HALF=H/2;X0=BO-HALF
D0=B-X0;D_MAX=D0+HALF
RADIUS=F(1,25)
K=240
NF505_SHA='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF494_SHA='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'

def A(x):return source.native.A(x)
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def matcol(xs):return arb_mat([[x] for x in xs])
def bound(x):return source.absmax(x)
def out_pair(x):return interval(x)
def source_nodes():
    rank=load('notes/data/provisional/parents/pr350_original_BS_pruned_rank_bound.json',RANK_SHA)
    nodes=[]
    for (freq,kmax),number in zip(rank['original_nodes'],rank['selected_multiplicities']):
        assert 0<=number<=kmax
        for k in range(number):nodes.append((F(freq),k))
    assert len(nodes)==241 and rank['retained_original_pole']
    nodes.append((None,None))
    return nodes
def complete_gram(nodes,b):
    G=arb_mat(242,242)
    ker=phys.Integrals()
    ker.b=A(b)
    cols=[phys.pole_terms() if f is None else phys.source_terms(f,k) for f,k in nodes]
    for i in range(242):
        for j in range(i+1):
            G[i,j]=G[j,i]=phys.gram(cols[i],cols[j],ker)
    return G
def shifted_poly(coeff):
    # Exact polynomial Taylor shift in interval Arb (not midpoint
    # evaluation), retaining all ORIGINAL 400 NF494 source coefficients.
    assert len(coeff)==400
    out=[arb(0) for _ in range(K+1)]
    d0=A(D0)
    for c in reversed(coeff):
        nxt=[arb(0) for _ in range(K+1)]
        nxt[0]=out[0]*d0+c
        for j in range(1,K+1):
            nxt[j]=out[j]*d0+out[j-1]
        out=nxt
    # All high-order original 400-polynomial terms omitted after the
    # midpoint shift are bounded BEFORE any selected-frame transport.
    # binom(n,j)<=binom(n,K+1)binom(n-K-1,j-K-1)
    # and |t|<=HALF; the original variable d0+t <=D_MAX.
    tail=arb(0)
    half=A(HALF);dmax=A(D_MAX)
    for n in range(K+1,400):
        tail+=bound(coeff[n])*A(math.comb(n,K+1))*half**(K+1)*dmax**(n-K-1)
    assert tail.lower()>=0
    return out,tail
def actual_W_taylor(receipt):
    H400=[source.ball(pair) for pair in receipt['original_H_400_native_outward']]
    U400=[source.ball(pair) for pair in receipt['original_U_400_native_outward']]
    hp,htail=shifted_poly(H400)
    up,utail=shifted_poly(U400)
    # Original NF494 physical d=B-x, but local polynomial coordinate
    # t=x-X0 hence d=D0-t: alternate signs of all shifted jets.
    hp=[(-1 if j%2 else 1)*z for j,z in enumerate(hp)]
    up=[(-1 if j%2 else 1)*z for j,z in enumerate(up)]

    # Same seven ORIGINAL Lambda(n)/sqrt(n) arithmetic, source-certified
    # against the unchanged NF411 intervals, not old coarse widths.
    nf411,sha=read('notes/data/provisional/NF411_original_source_boundary_jet.json')
    assert nf411['nf407_source_sha256']==source.SRC
    prime_base={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
    C8=arb(0);seen=set()
    for row in nf411['all_seven_original_prime_seam_derivative_identities']:
        n=row['prime_power']
        assert n in prime_base and n not in seen
        z=A(prime_base[n]).log()/A(n).sqrt()
        assert source.cmpoverlap(z,row['c_n_positive_outward'])
        C8+=z;seen.add(n)
    assert seen==set(prime_base)

    # Physical all-source W(B-d)=H(d)+U(B)C8+
    #                  U(B-d)/2*log(B/d). Prime term is U(B), CONSTANT.
    ll=[arb(0) for _ in range(K+1)]
    ll[0]=(A(B)/A(D0)).log()
    for j in range(1,K+1):
        ll[j]=A(F(1,j))/A(D0)**j
    poly=[hp[j] for j in range(K+1)]
    poly[0]+=U400[0]*C8
    for j in range(K+1):
        poly[j]+=sum((up[a]*ll[j-a] for a in range(j+1)),arb(0))/2

    rho=F(HALF,D0)
    assert 0<rho<F(1,10)
    logtail=A(rho**(K+1)/((K+1)*(1-rho)))
    Lmax=(A(B)/A(D0-HALF)).log()
    Uweighted=[bound(u)*A(HALF)**j for j,u in enumerate(up)]
    Lweighted=[bound(l)*A(HALF)**j for j,l in enumerate(ll)]
    lost=arb(0)
    for j in range(1,K+1):
        lost+=Uweighted[j]*sum((Lweighted[k] for k in range(K-j+1,K+1)),arb(0))
    # Above lost includes exactly i+j>K but i=0 omitted; for i=0,
    # the sole omitted log tail is U0*logtail charged below.
    source_tail_H=A(F(10)**420*(D_MAX/RADIUS)**400/(1-D_MAX/RADIUS))
    source_tail_U=A(F(10)**400*(D_MAX/RADIUS)**400/(1-D_MAX/RADIUS))
    error=htail+(utail+source_tail_U)*Lmax/2+source_tail_H
    error+=(lost+sum(Uweighted,arb(0))*logtail)/2
    assert error.upper()<A(F(1,10**50)), ('METHOD STOP genuine W local remainder too wide',error)
    return poly,error

def fitted_J_taylor(nodes,raw):
    pi=arb.pi()
    out=[arb(0) for _ in range(K+1)]
    x0=A(X0)
    for i,(f,k) in enumerate(nodes):
        c=raw[i,0]
        if f is None:
            ep=(x0/2).exp()/2
            em=-( -x0/2).exp()/2
            s=arb(1)
            for m in range(K+1):
                if m: s/=m
                out[m]+=c*(ep*(A(F(1,2))**m)+em*((-A(F(1,2)))**m))*s
        else:
            omega=2*pi*A(f)
            iw=acb(arb(0),omega)
            phase=(iw*x0).exp()
            ex=[phase]
            for m in range(1,K+1):ex.append(ex[-1]*iw/m)
            xp=[x0**j for j in range(k+1)]
            for m in range(K+1):
                z=acb(0)
                for l in range(min(k,m)+1):
                    z+=math.comb(k,l)*xp[k-l]*ex[m-l]
                v=z.imag if k%2==0 else z.real
                out[m]+=c*v
    # On H4095, |2*pi*f*HALF|<1 for every genuine original selected
    # frequency. The omitted Taylor remainder of x^k sin/cos is
    # bounded by 3*B^13/(K-13+1)! uniformly for all 241 generators.
    # Apply this bound to the fully correlated TRUE raw D*a vector;
    # it is a separate analytic remainder, not per-moment overcharge.
    fmax=max(f for f,k in nodes if f is not None)
    assert (2*A(arb.pi())*A(fmax)*A(HALF)).upper()<1
    amp=sum((bound(raw[i,0]) for i in range(241)),arb(0))
    remainder=amp*A(F(3)*(B**13)/math.factorial(K-13+1))
    remainder+=bound(raw[241,0])*A(F(2)*(B/2)**(K+1)/math.factorial(K+1))
    assert remainder.upper()<A(F(1,10**40)), (
        'METHOD STOP original selected fit analytic tail too wide',remainder)
    return out,remainder

def box(poly,tlo,thi,fee):
    t=arb(A((tlo+thi)/2),A((thi-tlo)/2))
    v=arb(0)
    for c in reversed(poly):v=v*t+c
    return v+arb(0,fee.upper())

def square_bounds(a):
    lo,hi=a.lower(),a.upper()
    low=arb(0) if lo<=0<=hi else min(lo*lo,hi*hi)
    high=max(lo*lo,hi*hi)
    return low,high

def integrate(poly,fee,steps):
    dx=H/steps
    low=arb(0);high=arb(0)
    for j in range(steps):
        xlo=X0-HALF+j*dx
        xhi=xlo+dx
        z=box(poly,xlo-X0,xhi-X0,fee)
        l,u=square_bounds(z)
        low+=2*A(dx)*l
        high+=2*A(dx)*u
    return low,high

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--nf494',required=True)
    p.add_argument('--nf505',required=True)
    p.add_argument('--nf511',required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--steps',type=int,default=128)
    p.add_argument('--bits',type=int,default=4096)
    o=p.parse_args()
    assert o.bits==4096 and 32<=o.steps<=2048 and o.steps&(o.steps-1)==0
    ctx.prec=4096
    Hjet,hsha=read(o.nf494)
    old,osha=read(o.nf505)
    receipt,_=read(o.nf511)
    assert hsha==NF494_SHA and osha==NF505_SHA
    assert Hjet['pass']=='NF494-native' and old['pass']=='NF504-native'
    assert receipt['pass']=='NF511-original-source-exact-local-W-pole-panel'
    assert Hjet['original_nf407_source_sha256']==old['source_original_NF407_sha256']==source.SRC
    assert Hjet['original_nf406_seams_sha256']==old['source_original_NF406_sha256']==source.SEAM
    assert old['original_selected_J_dimension']==242
    assert old['original_original_D_frame_SHA256']==FRAME
    assert receipt['mirrored_cell_index']==J
    assert receipt['original_nf505_raw_SHA256']==NF505_SHA
    assert receipt['original_nf494_raw_SHA256']==NF494_SHA
    assert old['original_support_saturated_physical_Hilbert_gate']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    nodes=source_nodes()
    assert [['pole',None] if f is None else [str(f),k] for f,k in nodes]==old['original_source_basis_nodes']

    Gfull=complete_gram(nodes,B)
    D=candidate(Gfull)
    N,frameerr=source.source_norm_check(Gfull,D)
    print('NF512 original full selected D frame SOURCE SHA accepted',flush=True)
    Gout=complete_gram(nodes,BO)
    Nout=D.transpose()*Gout*D
    Nout=(Nout+Nout.transpose())/2
    for i,j in ((0,0),(1,0),(40,7),(100,99),(241,241)):
        prior=old['original_actual_exterior_J242_D_Gram_rows_outward'][i][j]
        (m,e),(r,v)=prior
        cen=F(int(m))*F(2)**int(e);rad=F(int(r))*F(2)**int(v)
        assert Nout[i,j].lower()<=A(cen+rad) and Nout[i,j].upper()>=A(cen-rad)

    dO=matcol([source.ball(v) for v in old['original_actual_exterior_W_moments_D_outward']])
    aO=Nout.solve(dO,algorithm='lu')
    assert max((bound((Nout*aO-dO)[i,0]) for i in range(242)),arb(0)).upper()<A(F(1,10**50))
    raw=D*aO
    # Reconstruction in physical source space is done BEFORE evaluating
    # cell energy and before paying the remainder; never multiply
    # independently rounded 242 local mixed moments by huge D columns.
    W,feeW=actual_W_taylor(Hjet)
    fit,feeJ=fitted_J_taylor(nodes,raw)
    residual=[w-v for w,v in zip(W,fit)]
    sqR=integrate(residual,feeW+feeJ,o.steps)
    sqW=integrate(W,feeW,o.steps)
    assert source.cmpoverlap(arb(sqW[0],(sqW[1]-sqW[0])/2) if False else
                             (sqW[0]+sqW[1])/2+arb(0,(sqW[1]-sqW[0])/2),
                             receipt['local_E_H_original_full_W_squared']), (
                             'METHOD STOP source J8 local W² inconsistent with accepted NF511')
    assert sqR[0]>=0
    oldR=source.ball(old['original_original_saturated_exterior_residual_outward'])
    assert sqR[0]<=oldR.upper()
    # A genuine full local 242D leverage measurement using original
    # physical source Gram, not old aggregate rank accounting.
    Gleft=complete_gram(nodes,BO-H)
    Nleft=D.transpose()*Gleft*D
    C=(Nout-Nleft+Nout.transpose()-Nleft.transpose())/2
    trace_source=Nout.solve(C,algorithm='lu')
    tau=sum((trace_source[i,i] for i in range(242)),arb(0))
    assert tau.lower()>0 and tau.upper()<A(242), (
        'METHOD STOP full original local leverage interval indeterminate',tau)
    gamma=A(F(old['original_original_gamma_squared']))
    named='METHOD_STOP_LEVERAGE_GE_ONE_OR_INDETERMINATE'
    conservative=None
    if tau.upper()<1:
        lower=oldR.lower()-sqR[1]/(1-tau.upper())
        conservative=interval(lower)
        named=('CERTIFIED_ORIGINAL_NF404_SINGLE_PAIR_PHYSICAL_NO_GO'
               if lower>gamma else 'LOCAL_NECESSARY_GATE_INDETERMINATE')
    result={
      'pass':'NF512-original-local-direct-residual-native',
      'standing':'ORIGINAL source 4096bit H4095 true globally fitted 242D local residual and selected leverage; fixed NF404 gate scoped only',
      'original_NF505_SHA256':NF505_SHA,'original_NF494_SHA256':NF494_SHA,
      'source_original_NF407_SHA256':source.SRC,'source_original_NF406_SHA256':source.SEAM,
      'original_source_D_SHA256':FRAME,'original_selected_dimension':242,
      'true_original_microcell_index':J,'source_original_pair_width':str(2*H),
      'selected_jet_order':K,'physical_subslabs':o.steps,
      'original_source_W_taylor_global_error_upper':interval(feeW),
      'original_source_selected_fit_taylor_error_upper':interval(feeJ),
      'original_full_W_H4095_energy_native': [str(sqW[0].lower()),str(sqW[1].upper())],
      'original_complete_242D_exterior_fitted_residual_eH_native':
           [str(sqR[0].lower()),str(sqR[1].upper())],
      'original_complete_242D_selected_local_leverage_native':interval(tau),
      'original_R_O_outward':old['original_original_saturated_exterior_residual_outward'],
      'original_unchanged_NF404_gamma_squared':old['original_original_gamma_squared'],
      'original_single_pair_NF404_gate':named,
      'original_single_pair_no_go_lower_if_tau_lt_one':conservative,
      'physical_W_local_source_integral_complete':True,
      'original_full_local_residual_direct_integral_complete':True,
      'original_full_local_242x242_Mixed_moments_reintegrated_separately':False,
      'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(o.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF512 ORIGINAL source H4095 local actual J242 e_H',
          sqR[0].str(18),sqR[1].str(18),flush=True)
    print('NF512 ORIGINAL source H4095 full selected leverage',tau.str(18),flush=True)
    print('NF512 unchanged NF404 named cell physical gate:',named,flush=True)
    print('Original Weil test-source eligibility, signed form and RH OPEN',flush=True)

if __name__=='__main__':
    main()
