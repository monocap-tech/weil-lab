#!/usr/bin/env python3
"""Bounded COMPLETE original raw signed mixed block: retained J242 x critical F4."""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from flint import arb,acb,acb_series,ctx
import flint
from verify_rpb108_original_signed_frequency_kernel import Kernel
import verify_rpb108_si29_full_J_L2_normalization as physical
import verify_rpb108_si29_original_prime_mixed as translated
RANK_SHA='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
CRITICAL_SHA='a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'
def dy(x):
    n,e=x.man_exp();return [str(n),int(e)]
def rat(v):return F(int(v[0]))*F(2)**int(v[1])
def ball(v):return [dy(v.mid()),dy(v.rad())]
def bounds(v,D=10**80):
    l=rat(dy(v.lower()))*D;h=rat(dy(v.upper()))*D
    return [str(F(l.numerator//l.denominator,D)),str(F(-(-h.numerator//h.denominator),D))]
def main():
    p=argparse.ArgumentParser();p.add_argument('--rank',required=True);p.add_argument('--critical',required=True);p.add_argument('--output',default='artifacts/original_signed_critical_mixed_block.json');args=p.parse_args();start=time.monotonic();data={}
    for name,sha in [('rank',RANK_SHA),('critical',CRITICAL_SHA)]:
        raw=Path(getattr(args,name)).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha;data[name]=json.loads(raw)
    rank,critical=data['rank'],data['critical'];assert rank['retained_physical_rank_upper']==242 and rank['retained_original_pole']
    assert flint.__version__=='0.8.0';ctx.prec=512;k=Kernel()
    spec=critical['exact_candidates'];probes=spec['probes'];assert len(probes)==4
    frequencies=list(map(F,spec['sine_frequencies']));aa=[list(map(F,p['sine_coefficients'])) for p in probes];bb=[F(p['sinh_coefficient']) for p in probes]
    basis=[]
    for c in frequencies:
        mu=acb(2*k.pi*arb(str(c)));Am,Im=k.point(mu);basis.append((mu,Am,Im))
    Ap,Ip=k.point(k.pole);basis.append((k.pole,Ap,Ip))
    coeffs=[[acb(str(a)) for a in av]+[-k.I*acb(str(b))] for av,b in zip(aa,bb)]
    grids=[[[acb(0) for _ in basis] for _ in basis] for _ in range(3)]
    for i,(v0,Av,Iv) in enumerate(basis):
        for j,(mu,Am,Im) in enumerate(basis[:i+1]):
            if i==j:values=k.diagonal(v0)
            else:
                ctx.cap=1;values=tuple(x[0] if isinstance(x,acb_series) else x for x in k.mixed(acb_series([v0]),acb_series([Av]),acb_series([Iv]),mu,Am,Im,v0==k.pole))
            for t in range(3):grids[t][i][j]=grids[t][j][i]=values[t]
    targetQ=[];targetComponents=[];firstparts=None
    for i in range(4):
        row=[];componentrow=[]
        for j in range(4):
            parts=[sum((coeffs[i][r]*coeffs[j][s]*G[r][s] for r in range(33) for s in range(33)),acb(0)) for G in grids]
            assert all(x.imag.contains(0) for x in parts)
            q=sum(parts,acb(0));lo,hi=map(F,critical['complete_signed_Gram_intervals'][i][j])
            assert arb(str(lo))<q.real<arb(str(hi))
            row.append(ball(q.real))
            componentrow.append({key:ball(value.real) for key,value in zip(['arch','prime','pole'],parts)})
            if i==j==0:firstparts=parts
        targetQ.append(row)
        targetComponents.append(componentrow)
    rows=[];offset=0;integrals=physical.Integrals();maxrad=F(0)
    def entry(values,t):
        nonlocal maxrad
        assert all(x.is_finite() and x.imag.contains(0) for x in values)
        total=sum(values,acb(0));maxrad=max(maxrad,rat(dy(total.real.rad())))
        return dict(target_index=t,components_native={key:ball(value.real) for key,value in zip(['arch','prime','pole'],values)},signed_native=ball(total.real),signed_interval=bounds(total.real))
    for cluster,((c,pmax),count) in enumerate(zip(rank['original_nodes'],rank['selected_multiplicities'])):
        c=F(c)
        if count:
            v0=acb(2*k.pi*arb(str(c)));v,A,I=k.functions(v0,count);ctx.cap=count
            parts=[[acb_series([0]) for _ in range(3)] for _ in range(4)]
            for s,(mu,Am,Im) in enumerate(basis):
                values=k.mixed(v,A,I,mu,Am,Im)
                for t in range(4):
                    for j in range(3):parts[t][j]+=coeffs[t][s]*values[j]
            for order in range(count):
                factor=(-1)**(order//2)*factorial(order);terms=physical.source_terms(c,order);norm=physical.gram(terms,terms,integrals);assert norm>0
                entries=[entry([part[order]*factor for part in parts[t]],t) for t in range(4)]
                rows.append(dict(original_source_index=offset+order,cluster=cluster,center=str(c),order=order,entries=entries,source_norm_squared_interval=bounds(norm),raw_coordinate='x^k sin(2*pi*c*x) for even k; x^k cos(2*pi*c*x) for odd k'))
        offset+=pmax
        assert time.monotonic()-start<90,'bounded 90-second COMPLETE mixed block guard'
    assert offset==469
    components=[[acb(0)]*3 for _ in range(4)]
    for s,(mu,Am,Im) in enumerate(basis):
        if mu==k.pole:values=k.diagonal(k.pole)
        else:
            ctx.cap=1;values=tuple(x[0] if isinstance(x,acb_series) else x for x in k.mixed(acb_series([k.pole]),acb_series([Ap]),acb_series([Ip]),mu,Am,Im,True))
        for t in range(4):
            for j in range(3):components[t][j]+=-k.I*coeffs[t][s]*values[j]
    rows.append(dict(original_source_index=469,cluster=None,center=None,order=None,entries=[entry(components[t],t) for t in range(4)],source_norm_squared_interval=bounds(k.pp),raw_coordinate='true sinh(x/2)'))
    assert len(rows)==242 and maxrad<F(1,10**70)
    targets=[]
    for av,b in zip(aa,bb):
        terms=[]
        for frequency,a in zip(frequencies,av):terms.extend((p,t,f,c*arb(str(a))) for p,t,f,c in physical.source_terms(frequency,0))
        terms.extend((p,t,f,c*arb(str(b))) for p,t,f,c in physical.pole_terms());targets.append(terms)
    clips=[]
    for power,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]:
        clip=translated.Clipped(arb(power).log());clips.append((2*arb(prime).log()/arb(power).sqrt(),clip,[translated.shifted(terms,clip) for terms in targets]))
    poles=[physical.gram(terms,physical.pole_terms(),integrals) for terms in targets]
    for row in rows:
        terms=physical.pole_terms() if row['original_source_index']==469 else physical.source_terms(F(row['center']),row['order'])
        sourcepole=physical.gram(terms,physical.pole_terms(),integrals)
        for t,e in enumerate(row['entries']):
            prime=-sum((weight*translated.clipped_gram(terms,shifted[t],clip) for weight,clip,shifted in clips),arb(0));pole=-2*poles[t]*sourcepole
            for key,value in [('prime',prime),('pole',pole)]:
                v=e['components_native'][key];mid=arb((int(v[0][0]),int(v[0][1])));rad=arb((int(v[1][0]),int(v[1][1])))
                assert (arb(mid,rad)-value).contains(0),(key,row['original_source_index'],t)
            e['independent_prime_native']=ball(prime);e['independent_pole_native']=ball(pole)
        assert time.monotonic()-start<90,'bounded 90-second independent translated-block guard'
    sums=[sum((max(abs(F(x)) for x in row['entries'][t]['signed_interval'])**2 for row in rows),F(0)) for t in range(4)]
    mu=F(1,1000)-F(rank['pruned_physical_complement_negative_upper']);assert mu>F(98,10**5)
    out=dict(status='CONDITIONAL_ORIGINAL_COMPLETE_RAW_SIGNED_CRITICAL_MIXED_BLOCK',rank_input_sha256=RANK_SHA,critical_input_sha256=CRITICAL_SHA,working_precision_bits=512,flint_version=flint.__version__,
      target_probe=probes[0],target_probes=probes,target_sine_frequencies=spec['sine_frequencies'],target_signed_kernel_Gram_native=targetQ,target_signed_kernel_Gram_components_native=targetComponents,target_signed_kernel_native=targetQ[0][0],
      target_signed_components_native={key:ball(value.real) for key,value in zip(['arch','prime','pole'],firstparts)},target_prior_signed_interval=critical['complete_scalar_witnesses'][0]['signed_energy_interval'],
      rows=rows,retained_source_count=242,critical_target_count=4,complete_mixed_entry_count=968,max_required_frequency_derivative_order=max(r['order'] or 0 for r in rows),maximum_native_block_radius=str(maxrad),raw_coordinate_column_squared_uppers=list(map(str,sums)),
      Laplace_terms=64,analytic_tail_strip_imaginary_bound='3/4',Cauchy_radius='1/4',Laplace_tail_Cauchy_base_upper=str(rat(dy(k.tail))),signed_physical_selected_complement_floor=str(mu),
      all_968_seven_prime_and_true_pole_cross_checks_passed=True,production_block_quadrature_used=False,global_source_monomial_expansion_used=False,full_physical_frame_transform_applied=False,
      raw_block_is_BS_mixed_block=False,raw_block_is_strong_residual=False,finite_BS_block_or_inverse_computed=False,critical_physical_projection_computed=False,augmented_frame_condition_certified=False,
      signed_Schur_or_global_sign_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
    path=Path(args.output);path.parent.mkdir(exist_ok=True,parents=True);path.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print('ORIGINAL COMPLETE RAW SIGNED CRITICAL BLOCK PASS: 242x4 entries; max derivative13; radius',float(maxrad),'seconds',round(out['elapsed_seconds'],2))
if __name__=='__main__':main()
