#!/usr/bin/env python3
"""Construct a clipped affine ORIGINAL negative cap; no integration or matrix solve."""
import argparse, hashlib, json, time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, acb, ctx
from validate_rpb108_si06_negative_band import PI, WEIGHTS, SHIFTS
from validate_rpb108_si08_multiband_rank import taylor_order

PIN = {'envelope_stop':'19af532b6bbd4a808854696b2a993e7ebd966e04da27fdd5f55e8b736668770b',
       'anchor':'264fd853ca006a578d76369ac5bd4588a2097145b829fbba7036693f29b04044',
       'negative':'a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f'}
B=F(11,10); K=F(1,1000); H=F(2145); D=10**12; ETA=F(2,D); SUB=16

def dy(x):
    n,e=x.man_exp();return F(int(n))*F(2)**int(e)

def bounds(x):
    l=dy(x.lower())*D;h=dy(x.upper())*D
    return [F(l.numerator//l.denominator,D),F(-(-h.numerator//h.denominator),D)]

def cap_mass(a,b,w,z0,z1):
    """Exact integral of min(w,max(0,linear(z0,z1))) on [a,b]."""
    knots={F(0),F(1)}
    if z0!=z1:
        for v in (F(0),w):
            s=(v-z0)/(z1-z0)
            if 0<s<1:knots.add(s)
    knots=sorted(knots);mass=F(0);nonzero=0
    def height(s):return min(w,max(F(0),z0+(z1-z0)*s))
    for l,r in zip(knots,knots[1:]):
        v0,v1=height(l),height(r)
        mass+=(b-a)*(r-l)*(v0+v1)/2
        nonzero+=v0>0 or v1>0
    return mass,len(knots)-1,nonzero

def main():
    p=argparse.ArgumentParser()
    for k in PIN:p.add_argument('--'+k.replace('_','-'),required=True)
    p.add_argument('--output',default='artifacts/original_affine_negative_cap.json')
    args=p.parse_args();start=time.monotonic();data={}
    for k,sha in PIN.items():
        raw=Path(getattr(args,k)).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
        data[k]=json.loads(raw)
    old=data['envelope_stop'];assert old['W_ODD_NEG']=='OPEN'
    assert flint.__version__=='0.8.0';ctx.prec=512
    cells=[tuple(map(F,row)) for row in old['original_SM40_cells']]
    assert len(cells)==3892 and sum((2*(b-a)*w for a,b,w in cells),F(0))==F(1073441879,64000000)
    prime2=8*PI[1]**2*sum((WEIGHTS[n][1]*SHIFTS[n][1]**2 for n in WEIGHTS),F(0))
    arch2=144*F(22,7)**2;assert arch2+prime2<H
    primes=[(arb(p).log()/arb(n).sqrt(),2*arb.pi()*arb(n).log()) for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]]
    records={}
    def endpoint(q):
        if q not in records:
            x=arb(str(q));m=acb(arb('1/4'),arb.pi()*x).digamma().real-arb.pi().log()
            for c,s in primes:m-=2*c*(s*x).cos()
            v=bounds(m);assert 0<=v[1]-v[0]<=ETA;records[q]=v
        return records[q]
    mass=F(0);pieces=0;nonzero=0;maxwidth=F(0)
    for index,(a,b,w) in enumerate(cells):
        for j in range(SUB):
            l=a+(b-a)*F(j,SUB);r=a+(b-a)*F(j+1,SUB);d=r-l
            lo0,hi0=endpoint(l);lo1,hi1=endpoint(r)
            err=H*d*d/8
            v,n,nz=cap_mass(l,r,w,K-lo0+err,K-lo1+err)
            mass+=2*v;pieces+=n;nonzero+=nz;maxwidth=max(maxwidth,d)
        if index%1000==0:print('Affine cap cell',index,'seconds',round(time.monotonic()-start,2),flush=True)
        assert time.monotonic()-start<90,'bounded 90-second cap construction guard'
    assert maxwidth==F(1,4096) and len(records)==62379
    oldmass=F(old['original_SM40_two_sided_mass']);assert 0<mass<oldmass
    delta=H*maxwidth**2/4+ETA
    # Retained physical anchor lower is a FULL-form Loewner lower; its
    # retained cross bound is not a bound for the omitted positive tail.
    z=data['anchor'];a=F(z['full_signed_A_diagonal_lower']);d=F(z['full_signed_D_diagonal_lower']);b=F(z['retained_signed_cross_abs_upper'])
    reserve=(a-F(1,8000))*(d-F(1,24))-b*b
    assert a>F(1,8000) and d>F(1,24) and reserve>0
    # Complete physical Gram in the SAME original near-null/complement basis.
    x=arb('11/10');omega=2*arb.pi()*arb('37/64');c=arb('4096/3013')
    ss=x-(2*omega*x).sin()/(2*omega);pp=x.sinh()-x
    sp=2*(arb('1/2')*(x/2).cosh()*(omega*x).sin()-omega*(x/2).sinh()*(omega*x).cos())/(arb('1/4')+omega**2)
    gram=[ss+2*c*sp+c*c*pp,ss+(c-1)*sp-c*pp,ss-2*sp+pp]
    gram_intervals=[bounds(v) for v in gram]
    trace=F(27,10);assert gram_intervals[0][1]+gram_intervals[2][1]<trace
    affine_margin=F(1,8000)-delta*trace;assert affine_margin>F(386,10**7)
    # SAME original 107 Taylor packets / 890 columns, different weight.
    assert sum(taylor_order(F(c['hi'])-F(c['lo']),24)[0] for c in data['negative']['cluster_witnesses'])==890
    e2=2*B*oldmass/F(2**48);eroot=F(363,10**9);M=F(old['envelope_global_operator_upper']);Mroot=F(353,100)
    assert e2<eroot**2 and M<Mroot**2
    tau=F(1,2**23)
    young=tau*M+2*(1+tau)*Mroot*eroot+(2+tau+1/tau)*e2
    finite_margin=F(1,8000)-(delta+young)*trace;assert finite_margin>F(248,10**7)
    out=dict(status='CONDITIONAL_ORIGINAL_AFFINE_CAP_ANCHOR_FEASIBILITY',input_sha256=PIN,
       original_SM40_cells=old['original_SM40_cells'],subdivisions_per_cell=SUB,frequency_cells=len(cells)*SUB,
       endpoint_multiplier_intervals=[[str(q),str(v[0]),str(v[1])] for q,v in sorted(records.items())],
       endpoint_count=len(records),working_precision_bits=512,flint_version=flint.__version__,endpoint_rounding_denominator=D,
       endpoint_uncertainty_upper=str(ETA),arch_curvature_upper=str(arch2),prime_curvature_upper=str(prime2),full_multiplier_curvature_upper=str(H),
       cap_formula='min(w40,max(0,kappa-linear_interpolant(endpoint_m_lower)+H*width^2/8))',
       maximum_cell_width=str(maxwidth),uniform_cap_minus_true_negative_upper=str(delta),
       original_cap_mass=str(oldmass),affine_cap_mass=str(mass),affine_piece_count=pieces,nonzero_affine_piece_count=nonzero,
       original_basis=z['original_basis'],physical_Gram_intervals=[[str(v) for v in row] for row in gram_intervals],physical_Gram_trace_upper=str(trace),
       inherited_signed_anchor_diagonal_lower=['1/8000','1/24'],inherited_anchor_Loewner_reserve=str(reserve),
       affine_cap_anchor_coefficient_lower=str(affine_margin),original_packet_count=107,unchanged_Taylor_columns=890,Taylor_bits=24,
       Taylor_analysis_squared_error_upper=str(e2),analysis_error_norm_upper=str(eroot),envelope_operator_norm_upper=str(M),envelope_operator_sqrt_upper=str(Mroot),
       Young_tau=str(tau),Young_cap_minus_affine_operator_upper=str(young),finite_rank_cap_anchor_coefficient_lower=str(finite_margin),
       full_operator_uniform_error_bound=True,original_signed_multiplier_used=True,both_reflected_frequencies_paid=True,
       actual_inverse_or_Galerkin_lift_computed=False,complete_470_source_gate_certified=False,full_890_moment_matrix_assembled=False,
       full_original_signed_schur_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print('AFFINE CAP FEASIBILITY PASS: full original 2D anchor, SAME 890-column Young cap; inverse/mixed gate OPEN; seconds',round(out['elapsed_seconds'],2))
    print('Uniform cap error',float(delta),'affine anchor lower',float(affine_margin),'finite cap anchor lower',float(finite_margin))
if __name__=='__main__':main()
