#!/usr/bin/env python3
"""Independent exact coupled min-max replay; native integration/domain standing retained."""
import hashlib,json,sys
from fractions import Fraction as Q
from pathlib import Path
PIN='2cd494b1558c43790f683d21926e1d1a83cc68a4edfdebd0d6074ac968f85919'
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):
    a=[u*v for u in x for v in y];return min(a),max(a)
def scale(x,c):return mul(x,(c,c))
def square(x):
    a,b=x;return (Q(0) if a<=0<=b else min(a*a,b*b),max(a*a,b*b))
def dy(v):return Q(int(v[0]))*Q(2)**int(v[1])
def ball(v):
    m,r=dy(v[0]),dy(v[1]);assert r>=0;return m-r,m+r
def subset(x,y):assert y[0]<=x[0]<=x[1]<=y[1]
def absup(v):return max(abs(v[0]),abs(v[1]))
def main():
    assert len(sys.argv)==4
    z=json.load(open(sys.argv[1]));raw=Path(sys.argv[2]).read_bytes();cr=Path(sys.argv[3]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==PIN==z['prior_native_sha256']
    assert hashlib.sha256(cr).hexdigest()==z['candidates_sha256'];prior=json.loads(raw);spec=json.loads(cr)
    assert z['exact_candidates']==spec and len(spec['probes'])==4 and spec['coefficient_denominator']==10**12
    assert spec['sine_frequencies']==prior['exact_probe']['sine_frequencies']==[str(Q(5*n,11)) for n in range(1,33)]
    assert spec['probes'][0]['sine_coefficients']==prior['exact_probe']['sine_coefficients'] and spec['probes'][0]['sinh_coefficient']==prior['exact_probe']['sinh_coefficient']
    for p in spec['probes']:
        assert len(p['sine_coefficients'])==32 and all((Q(v)*10**12).denominator==1 for v in p['sine_coefficients']+[p['sinh_coefficient']])
    assert z['status']=='CONDITIONAL_ORIGINAL_FOUR_NEAR_CRITICAL_BS_MODES' and z['working_precision_bits']==512 and z['flint_version']=='0.8.0'
    witnesses=z['complete_scalar_witnesses'];assert len(witnesses)==z['scalar_evaluations']==10
    expected=[[i,i] for i in range(4)]+[[i,j] for i in range(4) for j in range(i+1,4)]
    assert [v['label'] for v in witnesses]==expected
    data={}
    for witness in witnesses:
        v={k:ball(x) for k,x in witness['native_balls'].items()}
        N=tuple(map(Q,witness['physical_norm_interval']));q=tuple(map(Q,witness['signed_energy_interval']))
        assert N[0]>0 and all((x*10**40).denominator==1 for x in N+q)
        subset(v['norm'],N);subset(v['signed'],q)
        composed=add(add(mul(add(v['arch_constant'],v['arch_tail']),v['norm']),v['arch_integral']),add(v['prime'],scale(square(v['pole']),-2)))
        subset(composed,q);data[tuple(witness['label'])]=(N,q)
    assert list(map(str,data[(0,0)][1]))==prior['signed_energy_interval']
    G=[[None]*4 for _ in range(4)];T=[[None]*4 for _ in range(4)]
    for i in range(4):G[i][i],T[i][i]=data[(i,i)]
    for i in range(4):
        for j in range(i+1,4):
            ns,qs=data[(i,j)];ni,qi=data[(i,i)];nj,qj=data[(j,j)]
            G[i][j]=G[j][i]=((ns[0]-ni[1]-nj[1])/2,(ns[1]-ni[0]-nj[0])/2)
            T[i][j]=T[j][i]=((qs[0]-qi[1]-qj[1])/2,(qs[1]-qi[0]-qj[0])/2)
    decode=lambda m:[[tuple(map(Q,v)) for v in row] for row in m]
    assert G==decode(z['physical_Gram_intervals']) and T==decode(z['complete_signed_Gram_intervals'])
    # Independent diagonal-dominance physical lower, paying all mixed entries.
    rho=max(sum(absup((G[i][j][0]-int(i==j),G[i][j][1]-int(i==j))) for j in range(4)) for i in range(4))
    gersh=min(G[i][i][0]-sum(absup(G[i][j]) for j in range(4) if j!=i) for i in range(4))
    assert rho==Q(z['physical_Gram_identity_error_upper'])<Q(1,100)
    assert gersh>=Q(99,100)==Q(z['physical_Gram_lower'])
    rows=[sum((absup(v) for v in row),Q(0)) for row in T];sigma=max(rows)
    assert rows==list(map(Q,z['signed_Gram_absolute_row_uppers'])) and sigma==Q(z['signed_Gram_operator_absolute_upper'])
    kappa=Q(33621,10**9);assert kappa==Q(z['inherited_Astar_floor'])
    eta=sigma/(kappa*Q(99,100));assert eta==Q(z['fourth_BS_distance_from_one_upper'])<Q(3,10**12)
    assert Q(z['fourth_BS_eigenvalue_lower'])==Q(z['deflated_BS_norm_lower'])==1-eta
    assert z['near_critical_dimension_lower']==4 and z['arbitrary_orthogonal_deflation_rank_up_to']==3
    for k in ['exact_near_critical_multiplicity_certified','complement_spectral_floor_certified','full_signed_positivity_certified','global_true_BS_norm_upper_certified','original_J470_membership_claimed']:assert z[k] is False
    assert z['W_ODD_NEG']==z['original_domain_review']=='OPEN'
    # Diagonal-only energy entries cannot establish a coupled operator bound.
    d=Q(1,10**18);assert 2*(d+2*d)>d*2 and 3*d==max(d+abs(2*d),d+abs(2*d))
    # Physical metric matters even for a scalar energy upper.
    assert d/Q(1,2)==2*d>d
    print('INDEPENDENT FOUR-MODE MIN-MAX REPLAY PASS: all 10 complete scalar compositions, 6 signed mixed entries and physical metric; lambda4 >1-3e-12; every rank<=3 complement norm >1-3e-12; global upper OPEN')
if __name__=='__main__':main()
