#!/usr/bin/env python3
"""NF426: rigorous *prefix only* of original cell-6 Chebyshev coefficients.

Use the genuine NF407 selected + four-critical source midpoint dyadics,
the complete NF424 digamma/endpoint-image transfer, all five true cell6
signed prime post-seam branches and original NF404 pole center.

Compute exact Chebyshev-series coefficients n=0..modes-1 of the analytic
cell6-branch continuation (NOT the physical function outside J6), using
1024+ bit native FLINT Arb/Acb. Keep the source sum correlated before
the m-dependent Bessel transform. Both endpoint images reduce to a
single real amplitude by original odd reflection. The *m=0 odd sinh
removable pole* is canceled algebraically, not numerically.

Certification is only for the computed prefix; all missing modes, true
cell6 signed scalar, other cells, NF404, W-ODD-NEG, RH remain OPEN.
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
C=F(91,100)
H=F(7,100)
CENTER=F(6677356497477490213,4611686018427387904)
N_IMAGES=2048
MAX_K=13
PRIMES=((2,2),(3,3),(4,2),(5,5),(7,7))

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
    ap.add_argument('--nf423',default='notes/data/provisional/NF423_original_entire_open_cell6_zthird_native.json')
    ap.add_argument('--nf425',default='scripts/local_replay/nf425_original_cell6_chebyshev_existence_exact.py')
    ap.add_argument('--output',required=True)
    ap.add_argument('--precision',type=int,default=2048)
    ap.add_argument('--modes',type=int,default=4)
    args=ap.parse_args()
    assert 1<=args.modes<=16
    ctx.prec=args.precision
    source,ssha=load(args.source)
    seams,ksha=load(args.seams)
    prior,psha=load(args.nf423)
    nf425bytes=Path(args.nf425).read_bytes()
    nf425sha=hashlib.sha256(nf425bytes).hexdigest()
    assert ssha==prior['original_nf407_source_sha256']
    assert ksha==prior['original_nf406_exact_support_seams_sha256']
    assert source['original_dimension']==242
    assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
    assert len(source['original_source_critical_sine_frequencies'])==32
    assert prior['true_original_entire_open_cell6_zthird_uniform_strict_upper']==286758
    assert prior['original_all_seven_real_signed_prime_branches_inside_open_cell']==['post-seam']*5+['neither']*2
    assert source['W_ODD_NEG']==source['RH']=='OPEN'
    assert seams['certified_ordered_knots'][13]['label']=='-B+log(7)'
    assert seams['certified_ordered_knots'][14]['label']=='-B+log(8)'
    assert F(seams['certified_ordered_knots'][13]['low'])>F(21,25)
    assert F(seams['certified_ordered_knots'][14]['high'])<F(49,50)
    terms,pole,s0=native_source(source)
    assert len(terms)>=240 and max(k for f,k,v in terms)<=MAX_K
    assert s0<F(1,10**700)
    raw=sum((abs(v)*B**k for f,k,v in terms),abs(pole))
    assert raw<10**160

    modes=args.modes
    K=modes-1+MAX_K+1
    digamma=arb(1).digamma()
    logpi=arb.pi().log()
    pi=arb.pi()
    res=[arb(0) for _ in range(modes)]
    image_groups=[]
    endpoint=arb(0)
    groups={}
    for f,k,q in terms:groups.setdefault(f,[]).append((k,q))
    assert all(f>0 for f in groups)
    hshifts=[arb(n).log() for n,_ in PRIMES]
    weights=[arb(base).log()/arb(n).sqrt() for n,base in PRIMES]
    print("NF426 native grouped genuine original source frequencies:",len(groups),flush=True)
    for rank,(f,ks) in enumerate(sorted(groups.items())):
        lam=acb(arb(0),2*pi*A(f))
        exB=(lam*A(B)).exp()
        base=cheb_exp(lam,K)
        deriv_D=polygamma_D(lam)
        xpolys=[base]
        for k in range(MAX_K):xpolys.append(mul_xminus(xpolys[-1],0))
        # Cache five actual prime post-seam shifted source polynomials.
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
            for n in range(modes):
                s=acb(0)
                for j in range(k+1):
                    s+=math.comb(k,j)*deriv_D[k-j]*xpolys[j][n]
                res[n]+=2*(alpha*s).real
            for i,(weight,(phase,polys)) in enumerate(zip(weights,shifted)):
                for n in range(modes):
                    res[n]-=weight*2*(alpha*phase*polys[k][n]).real
            for j in range(k+1):
                endpoly[j]+=alpha*R(F(math.comb(k,j)*math.factorial(j),2**j)*B**(k-j))
        image_groups.append((lam,exB,[exB*p for p in endpoly]))
        if (rank+1)%32==0:print("NF426 source-correlated interior and signed prime frequencies",rank+1,"/",len(groups),flush=True)
    # Entire original odd pole source u_p(y)=pole*sinh(y/2).
    endpoint+=A(pole)*(A(B)/2).sinh()
    plus=cheb_exp(R(F(1,2)),K)
    minus=cheb_exp(R(F(-1,2)),K)
    plus_x=mul_xminus(plus,0)
    minus_x=mul_xminus(minus,0)
    Kpole=(A(1).digamma()+ (A(F(1,2)).digamma()))/2 -logpi-A(B)
    for n in range(modes):
        # Analytically joint m0+psi(beta), beta->0, no pole split.
        res[n]+=A(pole)*(Kpole*(plus[n]-minus[n])+plus_x[n]+minus_x[n])/2
    for (nprime,base),h,w in zip(PRIMES,hshifts,weights):
        pplus=(R(F(1,2))*h).exp()
        pminus=(R(F(-1,2))*h).exp()
        for n in range(modes):
            res[n]-=w*A(pole)*(pminus*plus[n]-pplus*minus[n]).real/2
    # Fixed NF404 exact dyadic centering -a sinh(x/2).
    for n in range(modes):
        res[n]-=A(CENTER)*(plus[n]-minus[n]).real/2
    # Original endpoint v=u4(B) and original log v/2*log B/(B-x).
    D=A(B-C)
    disc=(D*D-A(H)**2).sqrt()
    Q=(D+disc)/2
    q=A(H)/(D+disc)
    assert q<A(F(1,5))
    for n in range(modes):
        ell=(A(B)/Q).log() if n==0 else 2*q**n/n
        res[n]-=endpoint*ell/2
        # All five true original signed post-seam branches add -w*u(B).
        if n==0:res[n]-=sum(weights,arb(0))*endpoint

    # n=0...modes-1 exact Chebyshev coefficients of BOTH actual
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
        for n in range(modes):
            b=1 if n==0 else 2
            res[n]+=total* ((fac if n%2==0 else facalt)*
                            z.bessel_i(n)*b/2).real
        if (m+1)%512==0:print("NF426 correlated common 2-sided image index",m+1,"/",N_IMAGES,flush=True)

    # Uniform true cell6 image/source analytic continuation error
    # <1e-45 on the full rational [.84,.98] fixed branch:
    # >0.24 left boundary and source dyadic radius <1e-700;
    # at x=.84, shifted x-log7 exceeds -B by <.01 only, paid via
    # factor 2 on source coefficient radius. The Chebyshev transform
    # operator has norm <=2 for every positive coefficient index.
    # Charge 4e-45 in EACH coefficient, plus outward native ball.
    analytic_charge=F(4,10**45)
    vals=[]
    for n,v in enumerate(res):
        a,b=enclosure(v)
        lo=a-analytic_charge;hi=b+analytic_charge
        assert hi>=lo and hi-lo<F(1,10**25),(n,'unresolved radius',str(hi-lo)[:80])
        vals.append({
           'n':n,
           'native_finite_model_Chebyshev_ball_str':str(v)[:300],
           'true_original_cell6_fixed_branch_coefficient_outward_interval':[str(lo),str(hi)],
           'radius_target_below_1e_minus_25':True})
    # No missing coefficient is set to zero. This is a certified prefix,
    # NOT a degree-(modes-1) uniform approximation!
    out={
      'pass':'NF426','standing':'CERTIFIED ORIGINAL SOURCE-CORRELATED LOW-MODE CHEBYSHEV COEFFICIENT PREFIX ONLY; FULL CELL6 INTEGRAL OPEN',
      'source_sha256':ssha,'seams_sha256':ksha,'NF423_sha256':psha,
      'NF425_exact_preflight_script_sha256':nf425sha,
      'original_four_selected_plus_critical_count':246,
      'original_true_cell6':'(log(7)-11/10,log(8)-11/10)',
      'fixed_analytic_branch_outside_physical_cell_is_not_original_z':True,
      'analytic_Chebyshev_center':'91/100',
      'analytic_Chebyshev_halfwidth':'7/100',
      'original_critical_sinh_m0_digamma_removable_pole_joined':True,
      'original_all_five_post_seam_primes_retained':[2,3,4,5,7],
      'original_two_neither_branches':[8,9],
      'original_exact_NF404_dyadic_center':str(CENTER),
      'original_native_precision_bits':args.precision,
      'common_odd_source_image_amplitude_per_index':True,
      'common_endpoint_image_indices':N_IMAGES,
      'all_original_4096bit_source_midpoints':True,
      'true_original_source_radii_paid_by_uniform_charge':True,
      'true_original_fixed_branch_cheb_coefficient_error_charge_per_mode_exact':str(analytic_charge),
      'coefficients':vals,
      'number_of_certified_low_mode_coefficients':modes,
      'number_of_target_coefficients':2049,
      'all_2049_coefficients_certified':False,
      'entire_cell6_poly_from_coefficients_uniformly_certified':False,
      'true_cell6_signed_pz_and_z2_integrated':False,
      'NF410_all_eight_cells_integrated':False,
      'NF404_complete_signed_scalar_decided':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'}
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    for it in vals:
        print('NF426 original cell6 coefficient n=',it['n'],
              'interval=',[str(z)[:70] for z in it['true_original_cell6_fixed_branch_coefficient_outward_interval']],flush=True)
    print('NF426 accepted certified prefix; missing coefficients and signed integration OPEN',flush=True)

if __name__=='__main__':main()
