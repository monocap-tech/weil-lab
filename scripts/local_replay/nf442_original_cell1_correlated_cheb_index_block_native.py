#!/usr/bin/env python3
"""NF442: original-source correlated high 256..511 original-source Chebyshev series block for cell 4.

Use the genuine NF407 selected + four-critical source midpoint dyadics,
the complete NF424 digamma/endpoint-image transfer, n2 and n3 both-sided true original cell1 prime translates and original NF404 pole center.

Compute exact Chebyshev-series coefficient balls on [start,stop) of the analytic
cell1-branch continuation (NOT the physical function outside J1), using
1024+ bit native FLINT Arb/Acb. Keep the source sum correlated before
the m-dependent Bessel transform. Both endpoint images reduce to a
single real amplitude by original odd reflection. The *m=0 odd sinh
removable pole* is canceled algebraically, not numerically.

Certification is only for the computed prefix; all missing modes, true
cell1 signed scalar, other cells, NF404, W-ODD-NEG, RH remain OPEN.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb, acb, ctx
from nf415_original_cell6_I1_validated_acb import native_source

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
B=F(11,10)
X=F(7,10000)
C=F(7,10000)
H=F(8,10000)
CENTER=F(6677356497477490213,4611686018427387904)
N_IMAGES=2048
MAX_K=13
TRANSLATES=((2,2,1),(2,2,-1),(3,3,1),(3,3,-1)) # shift=sign*logn, + for u(x-log n)

def A(z):
    return arb(str(z))
def R(z):
    return acb(A(z))
def load(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def enclosure(z,digits=75):
    m,rad,e=z.mid_rad_10exp(digits)
    fac=F(10)**int(e)
    return [F(int(m)-int(rad))*fac,F(int(m)+int(rad))*fac]
def cheb_exp(lam,K):
    z=lam*A(H)
    v=(lam*A(C)).exp()
    return [v*z.bessel_i(k)*(1 if k==0 else 2) for k in range(K+1)]
def mul_xminus(v,shift):
    """Chebyshev coefficient multiplication by x-shift, padded degree K."""
    N=len(v)-1
    out=[acb(0) for _ in range(N+1)]
    t=A(C)-A(shift);h=A(H)
    for k,b in enumerate(v):
        out[k]+=t*b
        if k==0:
            if N:out[1]+=h*b
        else:
            out[k-1]+=h*b/2
            if k<N:out[k+1]+=h*b/2
    return out
def polygamma_D(lam):
    aa=R(F(1,4))
    lo=aa-lam/2;hi=aa+lam/2
    res=[]
    for r in range(MAX_K+1):
        dr=(lo.polygamma(r)*((-1)**r)+hi.polygamma(r))/(2**(r+1))
        if r==0:dr-=acb.pi().log()
        res.append(dr)
    return res

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
    ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
    ap.add_argument('--nf441-router',default='scripts/local_replay/nf441_original_cells1_2_8_typed_geometry_exact.py')
    ap.add_argument('--output',required=True)
    ap.add_argument('--precision',type=int,default=2048)
    ap.add_argument('--start',type=int,default=64)
    ap.add_argument('--stop',type=int,default=320)
    ap.add_argument('--nf441',default='scripts/local_replay/nf441_original_cell1_source_native_cheb64.py')
    args=ap.parse_args()
    assert 0<=args.start<args.stop<=512 and args.stop-args.start<=256
    ctx.prec=args.precision
    source,ssha=load(args.source)
    seams,ksha=load(args.seams)
    router_sha=hashlib.sha256(Path(args.nf441_router).read_bytes()).hexdigest()
    assert seams['original_signed_prime_powers_all_retained'] and seams['number_of_open_physical_support_cells']==16
    assert source['original_dimension']==242
    assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
    assert len(source['original_source_critical_sine_frequencies'])==32
    assert source['W_ODD_NEG']==source['RH']=='OPEN'
    knots=seams['certified_ordered_knots']
    assert knots[8]['label']=='0' and knots[9]['label']=='B-log(3)'
    assert C-H<F(knots[8]['low'])<=F(knots[8]['high'])<C
    assert C<F(knots[9]['low'])<=F(knots[9]['high'])<C+H
    assert B-(C+H)==F(2197,2000)>F(1,2)
    assert F(36,2000)*10**160*F(1,3)**2048<F(1,10**50)
    terms,pole,s0=native_source(source)
    assert len(terms)>=240 and max(k for f,k,v in terms)<=MAX_K
    assert s0<F(1,10**700)
    raw=sum((abs(v)*B**k for f,k,v in terms),abs(pole))
    assert raw<10**160

    start=args.start;stop=args.stop;modes=stop-start
    K=stop-1+MAX_K+1
    parent_script_sha=hashlib.sha256(Path(args.nf441).read_bytes()).hexdigest()
    digamma=arb(1).digamma()
    logpi=arb.pi().log()
    pi=arb.pi()
    res=[arb(0) for _ in range(modes)]
    physical_point=arb(0)
    image_groups=[]
    endpoint=arb(0)
    groups={}
    for f,k,q in terms:groups.setdefault(f,[]).append((k,q))
    assert all(f>0 for f in groups)
    hshifts=[arb(n).log()*sign for n,base,sign in TRANSLATES]
    weights=[arb(base).log()/arb(n).sqrt() for n,base,sign in TRANSLATES]
    assert [t[0] for t in TRANSLATES]==[2,2,3,3] and [t[2] for t in TRANSLATES]==[1,-1,1,-1]
    physical_prime=arb(0)
    print("NF442 native grouped genuine original source frequencies:",len(groups),flush=True)
    for rank,(f,ks) in enumerate(sorted(groups.items())):
        lam=acb(arb(0),2*pi*A(f))
        exB=(lam*A(B)).exp()
        exX=(lam*A(X)).exp()
        base=cheb_exp(lam,K)
        deriv_D=polygamma_D(lam)
        xpolys=[base]
        for k in range(MAX_K):xpolys.append(mul_xminus(xpolys[-1],0))
        # Cache four actual physical prime shifted source polynomials.
        shifted=[]
        for h in hshifts:
            sh=[base]
            for k in range(max(k for k,v in ks)):
                sh.append(mul_xminus(sh[-1],h))
            shifted.append(((-lam*h).exp(),sh))
        # LEFT endpoint image amplitude for positive lambda and j-th
        # 1/(a-lambda/2) power. Odd symmetry gives RIGHT=-LEFT exactly.
        endpoly=[acb(0) for _ in range(MAX_K+1)]
        for k,q in ks:
            alpha=(acb(0,-A(q)/2) if k%2==0 else acb(A(q)/2))
            endpoint+=2*(alpha*exB*R(B**k)).real
            physical_point+=2*(alpha*exX*sum((math.comb(k,j)*deriv_D[k-j]*A(X)**j for j in range(k+1)),acb(0))).real
            for n in range(start,stop):
                s=acb(0)
                for j in range(k+1):
                    s+=math.comb(k,j)*deriv_D[k-j]*xpolys[j][n]
                res[n-start]+=2*(alpha*s).real
            for i,(weight,(phase,polys)) in enumerate(zip(weights,shifted)):
                signed_term=weight*2*(alpha*(lam*(A(X)-hshifts[i])).exp()*(A(X)-hshifts[i])**k).real
                physical_point-=signed_term
                physical_prime-=signed_term
                for n in range(start,stop):
                    res[n-start]-=weight*2*(alpha*phase*polys[k][n]).real
            for j in range(k+1):
                endpoly[j]+=alpha*R(F(math.comb(k,j)*math.factorial(j),2**j)*B**(k-j))
        image_groups.append((lam,exB,[exB*p for p in endpoly]))
        if (rank+1)%32==0:print("NF442 source-correlated interior and signed prime frequencies",rank+1,"/",len(groups),flush=True)
    # Entire original odd pole source u_p(y)=pole*sinh(y/2).
    endpoint+=A(pole)*(A(B)/2).sinh()
    plus=cheb_exp(R(F(1,2)),K)
    minus=cheb_exp(R(F(-1,2)),K)
    plus_x=mul_xminus(plus,0)
    minus_x=mul_xminus(minus,0)
    Kpole=(A(1).digamma()+ (A(F(1,2)).digamma()))/2 -logpi-A(B)
    physical_point+=A(pole)*(Kpole*(A(X)/2).sinh()+A(X)*(A(X)/2).cosh())
    for n in range(start,stop):
        # Analytically joint m0+psi(beta), beta->0, no pole split.
        res[n-start]+=(A(pole)*(Kpole*(plus[n]-minus[n])+plus_x[n]+minus_x[n])/2).real
    for (nprime,base,sign),h,w in zip(TRANSLATES,hshifts,weights):
        pole_signed=w*A(pole)*((A(X)-h)/2).sinh()
        physical_point-=pole_signed
        physical_prime-=pole_signed
        pplus=(R(F(1,2))*h).exp()
        pminus=(R(F(-1,2))*h).exp()
        for n in range(start,stop):
            res[n-start]-=w*A(pole)*(pminus*plus[n]-pplus*minus[n]).real/2
    # Fixed NF404 exact dyadic centering -a sinh(x/2).
    physical_point-=A(CENTER)*(A(X)/2).sinh()
    for n in range(start,stop):
        res[n-start]-=A(CENTER)*(plus[n]-minus[n]).real/2
    # Original endpoint v=u4(B) and original log v/2*log B/(B-x).
    physical_point-=endpoint*((A(B)/A(B-X)).log()/2+sum(weights,arb(0)))
    D=A(B-C)
    disc=(D*D-A(H)**2).sqrt()
    Q=(D+disc)/2
    q=A(H)/(D+disc)
    assert q<A(F(1,5))
    for n in range(start,stop):
        ell=(A(B)/Q).log() if n==0 else 2*q**n/n
        res[n-start]-=endpoint*ell/2
        # All four true original signed two-sided branches add -w*u(B).
        if n==0:res[n-start]-=sum(weights,arb(0))*endpoint

    # Absolute n=start..stop-1 exact Chebyshev coefficients of BOTH actual
    # endpoint families, factored after full source amplitude summation.
    for m in range(N_IMAGES):
        aa=R(F(4*m+1,4))
        total=arb(0)
        for lam,exB,polys in image_groups:
            inv=1/(aa-lam/2)
            powers=inv
            v=acb(0)
            for t in polys:
                v+=t*powers
                powers*=inv
            total+=2*v.real
        # The genuine odd sinh m0 pole is removable; NEVER divide
        # by aa-1/4 at m=0. Its regular -lambda/2 component survives.
        if m==0:
            total-=A(pole)*(-A(B)/2).exp()  # -pole*e^-B/2
        else:
            total+=A(pole)*((A(B)/2).exp()/A(F(m))-
                           (-A(B)/2).exp()/A(F(m)+F(1,2)))/2
        z=aa*2*A(H)
        # Factor exp(-2aB)*[exp(2a(C+Ht))-exp(-2a(C+Ht))]
        # BEFORE any high-precision Bessel multiplication.
        fac=( (-2*aa*R(B-C)).exp() - (-2*aa*R(B+C)).exp() )
        facalt=( (-2*aa*R(B-C)).exp() + (-2*aa*R(B+C)).exp() )
        # I_n(-s)=(-1)^n I_n(s): even n subtract right, odd add.
        physical_point+=(total/2*((-2*aa*R(B-X)).exp()-(-2*aa*R(B+X)).exp())).real
        for n in range(start,stop):
            b=1 if n==0 else 2
            res[n-start]+=total* ((fac if n%2==0 else facalt)*
                            z.bessel_i(n)*b/2).real
        if (m+1)%512==0:print("NF442 correlated common 2-sided image index",m+1,"/",N_IMAGES,flush=True)

    # Original J1 real x in [0,B-log3], B-x>1.0985:
    # 2048 matched image/source radius below 1e-50, source 4096bits.
    # Fixed-branch analytic continuation outside J1 does not represent
    # the actual switched original response there.
    analytic_charge=F(4,10**45)
    from nf415_original_cell6_I1_validated_acb import U
    ucheck=U(source)
    direct_prime=arb(0)
    for h,w in zip(hshifts,weights):
        direct_prime-=w*ucheck.at(R(X)-R(h)).real
    pp=enclosure(physical_prime);dp=enclosure(direct_prime)
    assert pp[0]<=dp[1] and dp[0]<=pp[1],('J1 both n2 n3 sided original source prime mismatch',str(pp)[:80],str(dp)[:80])
    ep=enclosure(endpoint);ud=enclosure(ucheck.at(R(B)).real)
    assert ep[0]<=ud[1] and ud[0]<=ep[1],('independent original source endpoint mismatch',str(ep)[:80],str(ud)[:80])
    print('NF442 independent original J1 both n2 n3 sides plus u(B) source PASS',flush=True)
    vals=[]
    for i,v in enumerate(res):
        n=start+i
        a,b=enclosure(v)
        lo=a-analytic_charge;hi=b+analytic_charge
        assert hi>=lo and hi-lo<F(1,10**25),(n,'unresolved radius',str(hi-lo)[:80])
        vals.append({
           'n':n,
           'native_finite_model_Chebyshev_ball_str':str(v)[:300],
           'true_original_cell1_fixed_branch_coefficient_outward_interval':[str(lo),str(hi)],
           'radius_target_below_1e_minus_25':True})
    # No missing coefficient is set to zero. This is a certified original CELL1 index block,
    # NOT a degree-(stop-1) uniform approximation!
    out={
      'pass':'NF442','standing':'CERTIFIED ORIGINAL SOURCE-CORRELATED CELL1 CHEBYSHEV INDEX BLOCK INCLUDING n2 and n3 BOTH SIDES; FULL CELL1 SIGNED INTEGRAL OPEN',
      'source_sha256':ssha,'seams_sha256':ksha,'NF441_cells1_2_8_router_sha256':router_sha,
      'NF441_accepted_cell1_native64_script_sha256':parent_script_sha,
      'original_independent_direct_source_both_n2_and_n3_prime_overlap_pass':True,
      'original_independent_direct_source_endpoint_overlap_pass':True,
      'native_analytic_global_transfer_pointwise_ball_str':str(physical_point)[:240],
      'original_four_selected_plus_critical_count':246,
      'original_true_cell1':'(0,11/10-log(3))',
      'fixed_analytic_branch_outside_physical_cell_is_not_original_z':True,
      'analytic_Chebyshev_center':'7/10000',
      'analytic_Chebyshev_halfwidth':'1/1250',
      'original_critical_sinh_m0_digamma_removable_pole_joined':True,
      'original_minus_translate_primes':[2,3],
      'original_plus_translate_primes':[2,3],
      'original_neither_prime_branches':[4,5,7,8,9],
      'original_signed_prime_translate_terms':4,
      'original_exact_NF404_dyadic_center':str(CENTER),
      'original_native_precision_bits':args.precision,
      'common_odd_source_image_amplitude_per_index':True,
      'common_endpoint_image_indices':N_IMAGES,
      'all_original_4096bit_source_midpoints':True,
      'true_original_source_radii_paid_by_uniform_charge':True,
      'true_original_fixed_branch_cheb_coefficient_error_charge_per_mode_exact':str(analytic_charge),
      'coefficients':vals,
      'mode_start_inclusive':start,
      'mode_stop_exclusive':stop,
      'number_of_certified_new_index_block_coefficients':modes,
      'number_of_target_coefficients':512,
      'previous_original_cell1_modes_0to63_certified':64,
      'true_cell1_full_uniform_tail_n512_onward_certified':False,
      'all_cell1_coefficients_certified':False,
      'entire_cell1_poly_from_coefficients_uniformly_certified':False,
      'true_cell1_signed_pz_and_z2_integrated':False,
      'NF410_all_eight_cells_integrated':False,
      'NF404_complete_signed_scalar_decided':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'}
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    for it in vals:
        print('NF442 original cell1 coefficient n=',it['n'],
              'interval=',[str(z)[:70] for z in it['true_original_cell1_fixed_branch_coefficient_outward_interval']],flush=True)
    assert [v['n'] for v in vals]==list(range(start,stop))
    print('NF442 original cell1 source-native index block',start,stop-1,'PASS; true cell1 signed integral OPEN',flush=True)

if __name__=='__main__':main()
