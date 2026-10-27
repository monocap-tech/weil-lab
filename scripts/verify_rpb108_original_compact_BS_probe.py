#!/usr/bin/env python3
"""Native scalar original BS near-critical witness and GLOBAL affine-cap stop.

The exact rational candidate is independently verified; pilot eigenvalues
and quadrature are not inputs to acceptance.
"""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
import flint
from flint import arb,acb,ctx
from validate_rpb108_si06_negative_band import PI,WEIGHTS,SHIFTS
CAP_SHA='8b58972bbdd2f9cb5d00275820ab6d6891feeff3bbd584a1c28231770368f514'
B=F(11,10);H=F(2145);HLOCAL=F(786)
def dy(x):
    n,e=x.man_exp();return [str(n),int(e)]
def rat(v):return F(int(v[0]))*F(2)**int(v[1])
def ball(v):return [dy(v.mid()),dy(v.rad())]
def bounds(v,D):
    l=rat(dy(v.lower()))*D;h=rat(dy(v.upper()))*D
    return F(l.numerator//l.denominator,D),F(-(-h.numerator//h.denominator),D)
def main():
    p=argparse.ArgumentParser();p.add_argument('--cap',required=True);p.add_argument('--probe',required=True);p.add_argument('--output',default='artifacts/original_compact_BS_native_probe.json');args=p.parse_args();start=time.monotonic()
    raw=Path(args.cap).read_bytes();assert hashlib.sha256(raw).hexdigest()==CAP_SHA;cap=json.loads(raw)
    praw=Path(args.probe).read_bytes();spec=json.loads(praw);assert spec['dirichlet_modes']==32
    assert spec['sine_frequencies']==[str(F(5*n,11)) for n in range(1,33)]
    a=list(map(F,spec['sine_coefficients']));b=F(spec['sinh_coefficient']);assert len(a)==32
    assert all((x*10**12).denominator==1 for x in a+[b])
    assert flint.__version__=='0.8.0';ctx.prec=512
    pi=arb.pi();bb=arb(str(B));L=2*bb;I=acb(0,1)
    rates=[];co=[]
    for n,c in enumerate(a,1):
        nu=2*pi*arb(str(F(5*n,11)));rates.extend([acb(0,nu),acb(0,-nu)]);co.extend([acb(0,-arb(str(c))/2),acb(0,arb(str(c))/2)])
    rates.extend([acb('1/2'),acb('-1/2')]);co.extend([acb(arb(str(b))/2),acb(-arb(str(b))/2)])
    size=len(rates);d=[acb(0) for _ in rates];t=[acb(0) for _ in rates]
    # Group the exact translated correlation into O(size) exponentials.
    for j in range(size):
        for k in range(size):
            c=co[j]*co[k]
            if k==(j^1):d[k]+=L*c;t[k]-=c
            else:
                rho=rates[j]+rates[k]
                d[j^1]+=c*(rho*bb).exp()/rho;d[k]-=c*(-rho*bb).exp()/rho
    norm=sum(d,acb(0))
    def overlap(s):return sum(((d[j]+t[j]*s)*(rates[j]*s).exp() for j in range(size)),acb(0))
    def exprel(z):return (z/2).exp()*(I*z/2).sinc()
    def D(s):return -sum((d[j]*rates[j]*exprel(rates[j]*s)+t[j]*(rates[j]*s).exp() for j in range(size)),acb(0))
    endpoint=sum((co[j]*(rates[j]*bb).exp() for j in range(size)),acb(0))
    assert (D(acb(0))-endpoint*endpoint).contains(0)
    # Independent norm/pole formulas use sine orthogonality and explicit overlaps.
    pp=bb.sinh()-bb;sp=[]
    for n in range(1,33):
        nu=2*pi*arb(str(F(5*n,11)))
        sp.append(-2*nu*(bb/2).sinh()*((-1)**n)/(arb('1/4')+nu**2))
    pole=sum((arb(str(c))*s for c,s in zip(a,sp)),arb(0))+arb(str(b))*pp
    norm2=bb*sum((arb(str(c))**2 for c in a),arb(0))+2*arb(str(b))*sum((arb(str(c))*s for c,s in zip(a,sp)),arb(0))+arb(str(b))**2*pp
    assert (norm.real-norm2).contains(0) and norm.imag.contains(0)
    def direct_overlap(s):
        out=acb(0)
        for j in range(size):
            for k in range(size):
                c=co[j]*co[k];rho=rates[j]+rates[k]
                out+=c*((L-s)*(rates[k]*s).exp() if k==(j^1) else ((rho*bb-rates[j]*s).exp()-(-rho*bb+rates[k]*s).exp())/rho)
        return out
    for s in [acb(0),acb('1/7'),acb(L)]:
        assert (overlap(s)-direct_overlap(s)).contains(0)
        if s!=0:assert (D(s)-(norm-overlap(s))/s).contains(0)
    integ=acb.integral(lambda s,_:(s/2).exp()/(I*s).sinc()*D(s),0,L,rel_tol=arb(2)**-160,abs_tol=arb(2)**-160,eval_limit=100000,depth_limit=24)
    assert integ.is_finite() and integ.imag.contains(0)
    tail=arb(0)
    for n in range(64):
        lam=arb(2*n)+arb('1/2');tail+=2*(-lam*L).exp()/lam
    rem=2*(-arb('257/2')*L).exp()/(arb('257/2')*(1-(-2*L).exp()));tail+=arb(0,rem.upper())
    c0=-arb.const_euler()-pi/2-3*arb(2).log()-pi.log();assert (c0-(acb('1/4').digamma().real-pi.log())).contains(0)
    prime=acb(0)
    for n,pn in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]:
        s=arb(n).log();v=overlap(acb(s));assert (v-direct_overlap(acb(s))).contains(0)
        prime-=2*arb(pn).log()/arb(n).sqrt()*v
    Q=(c0+tail)*norm+integ+prime-2*pole*pole
    assert Q.is_finite() and Q.imag.contains(0)
    qlo,qhi=bounds(Q.real,10**40);nlo,nhi=bounds(norm.real,10**40)
    assert 0<qlo<qhi<F(1,10**10) and F(99,100)<nlo<nhi<F(101,100)
    # One exact original fine cell supplies BOTH negative mass and cap defect.
    l,r,w=map(F,[spec['defect_cell'][k] for k in ('lo','hi','parent_SM40_height')]);width=r-l;mid=(l+r)/2
    assert l>=F(1,4) and width==F(1,4096)
    parents=[tuple(map(F,x)) for x in cap['original_SM40_cells']]
    assert any(a<=l<r<=b and ww==w and (l-a)/(b-a)*16 in range(16) and r-l==(b-a)/16 for a,b,ww in parents)
    records={F(q):(F(lo),F(hi)) for q,lo,hi in cap['endpoint_multiplier_intervals']}
    z0=F(1,1000)-records[l][0]+H*width**2/8;z1=F(1,1000)-records[r][0]+H*width**2/8
    assert 0<min(z0,z1)<=max(z0,z1)<w
    fmid=arb(0);x=arb(str(mid));theta=2*pi*x
    for n,c in enumerate(a,1):
        freq=arb(str(F(5*n,11)));fmid+=arb(str(c))*bb*((2*pi*bb*(freq-x)).sinc()-(2*pi*bb*(freq+x)).sinc())
    fmid+=arb(str(b))*2*(arb('1/2')*(bb/2).cosh()*(theta*bb).sin()-theta*(bb/2).sinh()*(theta*bb).cos())/(arb('1/4')+theta**2)
    ref=acb(0)
    for rate,c in zip(rates,co):
        for sign in (-1,1):
            rho=rate+sign*I*theta
            ref+=c*sign/(2*I)*((rho*bb).exp()-(-rho*bb).exp())/rho
    assert (ref.real-fmid).contains(0) and ref.imag.contains(0)
    flo,fhi=bounds(fmid,10**24);assert flo*fhi>0
    assert (F(44,7)*B)**2*2*B*nhi<11**2
    Fourierlower=min(abs(flo),abs(fhi))-11*width/2;assert Fourierlower>0
    m=acb(arb('1/4'),pi*x).digamma().real-pi.log()
    for n,pn in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]:m-=2*arb(pn).log()/arb(n).sqrt()*(2*pi*x*arb(n).log()).cos()
    mlo,mhi=bounds(m,10**24);rlower=F(1,1000)-mhi-132*width/2;assert rlower>0
    klower=2*width*rlower*Fourierlower**2
    archlocal=2*F(22,7)**2*(F(64,27)+F(104,125))
    prime2=8*PI[1]**2*sum((WEIGHTS[n][1]*SHIFTS[n][1]**2 for n in WEIGHTS),F(0));assert archlocal+prime2<HLOCAL
    defect=(H-HLOCAL)*width**2/8
    gap=2*width*defect*Fourierlower**2-qhi;assert gap>0
    upperA=F(cap['envelope_operator_norm_upper'])*nhi+qhi
    true_lower=klower/(klower+qhi);cap_lower=1+gap/upperA
    assert true_lower>1-F(6,10**12) and cap_lower>1+F(3,10**10)
    assert time.monotonic()-start<120,'bounded 120-second native scalar guard'
    out=dict(status='CONDITIONAL_ORIGINAL_COMPACT_BS_NEAR_CRITICAL_AND_GLOBAL_AFFINE_CAP_STOP',cap_input_sha256=CAP_SHA,probe_sha256=hashlib.sha256(praw).hexdigest(),exact_probe=spec,
      working_precision_bits=512,flint_version=flint.__version__,native_balls={k:ball(v.real if isinstance(v,acb) else v) for k,v in dict(norm=norm,arch_constant=c0,arch_integral=integ,arch_tail=tail,prime=prime,pole=pole,signed=Q).items()},
      physical_norm_interval=list(map(str,[nlo,nhi])),signed_energy_interval=list(map(str,[qlo,qhi])),
      mid_Fourier_interval=list(map(str,[flo,fhi])),mid_multiplier_interval=list(map(str,[mlo,mhi])),Fourier_derivative_upper='11',multiplier_derivative_upper='132',
      Fourier_on_cell_abs_lower=str(Fourierlower),negative_multiplier_on_cell_lower=str(rlower),true_negative_action_lower=str(klower),
      local_arch_curvature_upper=str(archlocal),prime_curvature_upper=str(prime2),local_full_curvature_upper=str(HLOCAL),cap_pointwise_overpayment_on_cell_lower=str(defect),
      affine_cap_minus_Astar_action_lower=str(gap),Astar_action_upper=str(upperA),original_true_BS_norm_lower=str(true_lower),affine_cap_BS_norm_lower=str(cap_lower),
      sufficient_coercivity_residual_squared_budget_ceiling=str(F(33621,10**9)*(1-true_lower)),residual_budget_scope='ONLY the scalar kappa_star^-1 norm-residual certificate for Galerkin trials containing this exact probe; residual itself UNCOMPUTED',
      whole_odd_affine_cap_comparison_stopped=True,all_Young_caps_dominating_same_affine_envelope_stopped=True,
      original_J470_membership_claimed=False,exact_J470_energy_dual_gate_stopped=False,original_signed_negative_direction_proved=False,
      original_true_BS_global_upper_certified=False,infinite_operator_remainder_certified=False,W_ODD_NEG='OPEN',original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print('NATIVE ORIGINAL BS / AFFINE CAP STOP PASS seconds',round(out['elapsed_seconds'],2),'Q interval',float(qlo),float(qhi),'cap gap',float(gap),'true BS distance upper',float(1-true_lower))
if __name__=='__main__':main()
