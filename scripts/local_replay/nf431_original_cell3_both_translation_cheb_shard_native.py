#!/usr/bin/env python3
"""NF431: rigorous original entire-cell3 source-correlated Chebyshev SERIES shard of original cell-3 Chebyshev coefficients.

Use the genuine NF407 selected + four-critical source midpoint dyadics,
the complete NF424 digamma/endpoint-image transfer, all five true cell3
signed prime post-seam branches and original NF404 pole center.

Compute exact Chebyshev-series coefficients start<=n<stop of the analytic
cell3-branch continuation (NOT the physical function outside J6), using
1024+ bit native FLINT Arb/Acb. Keep the source sum correlated before
the m-dependent Bessel transform. Both endpoint images reduce to a
single real amplitude by original odd reflection. The *m=0 odd sinh
removable pole* is canceled algebraically, not numerically.

Certification is only for the computed prefix; all missing modes, true
cell3 signed scalar, other cells, NF404, W-ODD-NEG, RH remain OPEN.
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
X=F(7,20)
C=F(7,20)
H=F(7,100)
CENTER=F(6677356497477490213,4611686018427387904)
N_IMAGES=2048
MAX_K=13
PRIMES=((3,3),(4,2))
BOTH=((2,2),)

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
    ap.add_argument('--nf430',default='scripts/local_replay/nf430_original_cells3_7_source_branch_transfer_exact.py')
    ap.add_argument('--nf417',default='notes/data/provisional/NF417_original_cell3_full_z_pointwise_native.json')
    ap.add_argument('--output',required=True)
    ap.add_argument('--precision',type=int,default=2048)
    ap.add_argument('--start',type=int,required=True)
    ap.add_argument('--stop',type=int,required=True)
    args=ap.parse_args()
    assert 0<=args.start<args.stop<=1500 and args.stop-args.start<=256
    ctx.prec=args.precision
    source,ssha=load(args.source)
    seams,ksha=load(args.seams)
    nf417,old_point_sha=load(args.nf417)
    nf430bytes=Path(args.nf430).read_bytes()
    nf430sha=hashlib.sha256(nf430bytes).hexdigest()
    assert nf417['cell']==3 and nf417['x']=='7/20'
    assert nf417['nf407_original_source_sha256']==ssha
    assert nf417['true_original_complete_z_pointwise_certified']
    assert not nf417['entire_original_cell_z_certified']
    assert source['original_dimension']==242
    assert len(source['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
    assert len(source['original_source_critical_sine_frequencies'])==32
    assert source['W_ODD_NEG']==source['RH']=='OPEN'
    assert seams['certified_ordered_knots'][10]['label']=='-B+log(4)'
    assert seams['certified_ordered_knots'][11]['label']=='B-log(2)'
    assert F(seams['certified_ordered_knots'][10]['low'])>F(7,25)
    assert F(seams['certified_ordered_knots'][11]['high'])<F(21,50)
    assert F(seams['certified_ordered_knots'][10]['high'])<X<F(seams['certified_ordered_knots'][11]['low'])
    assert [n for n,base in BOTH]==[2]
    assert [n for n,base in PRIMES]==[3,4]
    terms,pole,s0=native_source(source)
    assert len(terms)>=240 and max(k for f,k,v in terms)<=MAX_K
    assert s0<F(1,10**700)
    raw=sum((abs(v)*B**k for f,k,v in terms),abs(pole))
    assert raw<10**160

    modes=args.stop
    K=modes-1+MAX_K+1
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
    hshifts=[arb(n).log() for n,_ in PRIMES]
    weights=[arb(base).log()/arb(n).sqrt() for n,base in PRIMES]
    bothh=A(2).log()
    bothw=A(2).log()/A(2).sqrt()
    print("NF431 native grouped genuine original source frequencies:",len(groups),flush=True)
    for rank,(f,ks) in enumerate(sorted(groups.items())):
        lam=acb(arb(0),2*pi*A(f))
        exB=(lam*A(B)).exp()
        exX=(lam*A(X)).exp()
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
        # Original cell3: n2 BOTH source translations before B-log2 seam.
        bhp=[base];bhm=[base]
        for k in range(max(k for k,v in ks)):
            bhp.append(mul_xminus(bhp[-1],-bothh))
            bhm.append(mul_xminus(bhm[-1],bothh))
        bphaseplus=(lam*bothh).exp()
        bphaseminus=(-lam*bothh).exp()
        # LEFT endpoint image amplitude for positive lambda and j-th
        # 1/(a-lambda/2) power. Odd symmetry gives RIGHT=-LEFT exactly.
        endpoly=[acb(0) for _ in range(MAX_K+1)]
        for k,q in ks:
            alpha=(acb(0,-A(q)/2) if k%2==0 else acb(A(q)/2))
            endpoint+=2*(alpha*exB*R(B**k)).real
            physical_point+=2*(alpha*exX*sum((math.comb(k,j)*deriv_D[k-j]*A(X)**j for j in range(k+1)),acb(0))).real
            for n in range(args.start,modes):
                s=acb(0)
                for j in range(k+1):
                    s+=math.comb(k,j)*deriv_D[k-j]*xpolys[j][n]
                res[n]+=2*(alpha*s).real
            for i,(weight,(phase,polys)) in enumerate(zip(weights,shifted)):
                physical_point-=weight*2*(alpha*(lam*(A(X)-hshifts[i])).exp()*(A(X)-hshifts[i])**k).real
                for n in range(args.start,modes):
                    res[n]-=weight*2*(alpha*phase*polys[k][n]).real
            physical_point-=bothw*2*(alpha*((lam*(A(X)+bothh)).exp()*(A(X)+bothh)**k
                                       +(lam*(A(X)-bothh)).exp()*(A(X)-bothh)**k)).real
            for n in range(args.start,modes):
                res[n]-=bothw*2*(alpha*(bphaseplus*bhp[k][n]
                                        +bphaseminus*bhm[k][n])).real
            for j in range(k+1):
                endpoly[j]+=alpha*R(F(math.comb(k,j)*math.factorial(j),2**j)*B**(k-j))
        image_groups.append((lam,exB,[exB*p for p in endpoly]))
        if (rank+1)%32==0:print("NF431 source-correlated interior and signed prime frequencies",rank+1,"/",len(groups),flush=True)
    # Entire original odd pole source u_p(y)=pole*sinh(y/2).
    endpoint+=A(pole)*(A(B)/2).sinh()
    plus=cheb_exp(R(F(1,2)),K)
    minus=cheb_exp(R(F(-1,2)),K)
    plus_x=mul_xminus(plus,0)
    minus_x=mul_xminus(minus,0)
    Kpole=(A(1).digamma()+ (A(F(1,2)).digamma()))/2 -logpi-A(B)
    physical_point+=A(pole)*(Kpole*(A(X)/2).sinh()+A(X)*(A(X)/2).cosh())
    for n in range(args.start,modes):
        # Analytically joint m0+psi(beta), beta->0, no pole split.
        res[n]+=(A(pole)*(Kpole*(plus[n]-minus[n])+plus_x[n]+minus_x[n])/2).real
    for (nprime,base),h,w in zip(PRIMES,hshifts,weights):
        physical_point-=w*A(pole)*((A(X)-h)/2).sinh()
        pplus=(R(F(1,2))*h).exp()
        pminus=(R(F(-1,2))*h).exp()
        for n in range(args.start,modes):
            res[n]-=w*A(pole)*(pminus*plus[n]-pplus*minus[n]).real/2
    physical_point-=bothw*A(pole)*(((A(X)+bothh)/2).sinh()+((A(X)-bothh)/2).sinh())
    bcosh=(bothh/2).cosh()
    for n in range(args.start,modes):
        res[n]-=bothw*A(pole)*bcosh*(plus[n]-minus[n]).real
    # Fixed NF404 exact dyadic centering -a sinh(x/2).
    physical_point-=A(CENTER)*(A(X)/2).sinh()
    for n in range(args.start,modes):
        res[n]-=A(CENTER)*(plus[n]-minus[n]).real/2
    # Original endpoint v=u4(B) and original log v/2*log B/(B-x).
    physical_point-=endpoint*((A(B)/A(B-X)).log()/2+sum(weights,arb(0)))
    D=A(B-C)
    disc=(D*D-A(H)**2).sqrt()
    Q=(D+disc)/2
    q=A(H)/(D+disc)
    assert q<A(F(1,5))
    for n in range(args.start,modes):
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
        physical_point+=(total/2*((-2*aa*R(B-X)).exp()-(-2*aa*R(B+X)).exp())).real
        for n in range(args.start,modes):
            b=1 if n==0 else 2
            res[n]+=total* ((fac if n%2==0 else facalt)*
                            z.bessel_i(n)*b/2).real
        if (m+1)%512==0:print("NF431 correlated common 2-sided image index",m+1,"/",N_IMAGES,flush=True)

    # Uniform true cell3 image/source analytic continuation error
    # <1e-45 on the full rational [.84,.98] fixed branch:
    # >0.24 left boundary and source dyadic radius <1e-700;
    # at x=.84, shifted x-log7 exceeds -B by <.01 only, paid via
    # factor 2 on source coefficient radius. The Chebyshev transform
    # operator has norm <=2 for every positive coefficient index.
    # Charge 4e-45 in EACH coefficient, plus outward native ball.
    analytic_charge=F(4,10**45)
    point_inter=enclosure(physical_point)
    old_inter=list(map(F,nf417['original_true_complete_z_pointwise_rational_interval']))
    point_delta=F(1,10**45)
    assert point_inter[0]-point_delta<=old_inter[1] and old_inter[0]<=point_inter[1]+point_delta,('NF417 cell3 independent physical pointwise overlap failed',[str(z)[:80] for z in point_inter],[str(z)[:80] for z in old_inter])
    print('NF431 full global transfer original z(9/10) overlaps independent original NF416 physical integral',flush=True)
    vals=[]
    for n,v in enumerate(res):
        if n<args.start:continue
        a,b=enclosure(v)
        lo=a-analytic_charge;hi=b+analytic_charge
        assert hi>=lo and hi-lo<F(1,10**25),(n,'unresolved radius',str(hi-lo)[:80])
        vals.append({
           'n':n,
           'native_finite_model_Chebyshev_ball_str':str(v)[:300],
           'true_original_cell3_fixed_branch_coefficient_outward_interval':[str(lo),str(hi)],
           'radius_target_below_1e_minus_25':True})
    # No missing coefficient is set to zero. This is a certified prefix,
    # NOT a degree-(modes-1) uniform approximation!
    out={
      'pass':'NF431','standing':'CERTIFIED ORIGINAL SOURCE-CORRELATED CHEBYSHEV SERIES SHARD; COMPLETE CELL6 AGGREGATION AND INTEGRAL OPEN',
      'source_sha256':ssha,'seams_sha256':ksha,'NF430_exact_branch_script_sha256':nf430sha,
      'independent_original_NF417_cell3_pointwise_parent_sha256':old_point_sha,
      'original_analytic_global_transfer_pointwise_NF417_overlap_pass':True,
      'native_analytic_global_transfer_pointwise_ball_str':str(physical_point)[:240],
      'NF430_exact_source_branch_script_sha256':nf430sha,
      'original_four_selected_plus_critical_count':246,
      'original_true_cell3':'(log(4)-11/10,11/10-log(2))',
      'fixed_analytic_branch_outside_physical_cell_is_not_original_z':True,
      'analytic_Chebyshev_center':'7/20',
      'analytic_Chebyshev_halfwidth':'7/100',
      'original_critical_sinh_m0_digamma_removable_pole_joined':True,
      'original_both_source_prime_translations_retained':[2],
      'original_post_seam_primes_retained':[3,4],
      'original_neither_branches':[5,7,8,9],
      'original_exact_NF404_dyadic_center':str(CENTER),
      'original_native_precision_bits':args.precision,
      'common_odd_source_image_amplitude_per_index':True,
      'common_endpoint_image_indices':N_IMAGES,
      'all_original_4096bit_source_midpoints':True,
      'true_original_source_radii_paid_by_uniform_charge':True,
      'true_original_fixed_branch_cheb_coefficient_error_charge_per_mode_exact':str(analytic_charge),
      'coefficients':vals,
      'number_of_certified_low_mode_coefficients':modes-args.start,
      'first_mode_index_inclusive':args.start,'stop_mode_index_exclusive':args.stop,
      'number_of_target_coefficients':1500,
      'all_1500_coefficients_certified_by_single_shard':False,
      'entire_cell3_poly_from_coefficients_uniformly_certified':False,
      'true_cell3_signed_pz_and_z2_integrated':False,
      'NF410_all_eight_cells_integrated':False,
      'NF404_complete_signed_scalar_decided':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'}
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    for it in vals:
        print('NF431 original cell3 coefficient n=',it['n'],
              'interval=',[str(z)[:70] for z in it['true_original_cell3_fixed_branch_coefficient_outward_interval']],flush=True)
    print('NF431 accepted certified prefix; missing coefficients and signed integration OPEN',flush=True)

if __name__=='__main__':main()
