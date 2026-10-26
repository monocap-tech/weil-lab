#!/usr/bin/env python3
"""Construct exact SI29 Hermite-residual coordinates and certified series tails.

This constructs an analytic candidate basis, NOT the full-J470 projected
energy matrix T, its lower bound, or the normalized response.
"""
import argparse,ast,hashlib,json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

N=106
POWERS=tuple(range(107,134,2))
B=F(11,10)
PI_LO=F(333,106)
PI_UP=F(22,7)

def constants(path):
    def value(n):
        if isinstance(n,ast.Constant) and isinstance(n.value,int):return n.value
        if isinstance(n,(ast.Tuple,ast.List)):return tuple(value(x) for x in n.elts)
        assert isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='F'
        assert not n.keywords
        return F(*(value(x) for x in n.args))
    out={}
    for n in ast.parse(Path(path).read_text()).body:
        if isinstance(n,ast.Assign):
            for t in n.targets:
                if isinstance(t,ast.Name) and t.id in ('EXPECTED_CLUSTERS','EXPECTED_FEATURES'):
                    out[t.id]=value(n.value)
    assert len(out['EXPECTED_CLUSTERS'])==15 and sum(p for c,p in out['EXPECTED_CLUSTERS'])==N
    assert len(out['EXPECTED_FEATURES'])==14
    return out['EXPECTED_CLUSTERS'],out['EXPECTED_FEATURES']

def polynomial(nodes):
    w=[F(1)]
    for c,p in nodes:
        for _ in range(p):
            z=[F(0)]*(len(w)+1)
            for i,v in enumerate(w):z[i]-=c*v;z[i+1]+=v
            w=z
    assert len(w)==N+1 and w[-1]==1
    return w

def band_moments(feature,degree):
    c,r,d=feature
    assert r>0 and d in (0,1)
    lo,hi=c-r,c+r
    lp=[F(1)];hp=[F(1)]
    for _ in range(degree+2):lp.append(lp[-1]*lo);hp.append(hp[-1]*hi)
    mean=[(hp[k+1]-lp[k+1])/(2*r*(k+1)) for k in range(degree+1)]
    if d==0:
        assert mean[0]==1 and mean[1]==c
        return mean
    moments=[3*((hp[k+2]-lp[k+2])/F(k+2)-c*(hp[k+1]-lp[k+1])/F(k+1))/(2*r*r)
            for k in range(degree+1)]
    assert moments[0]==0 and moments[1]==r
    return moments

def residual_jets(nodes,features,max_degree):
    # General generator for coefficients of the EXACT entire residual.
    # For odd k, eta^k-Hermite(eta^k) = eta^k-(eta^k mod W).
    assert max_degree>=107
    w=polynomial(nodes)
    mu=[band_moments(f,max_degree) for f in features]
    rem=[F(1)]+[F(0)]*(N-1)
    out={}
    for k in range(max_degree+1):
        if k>=107 and k%2:
            if k==107:
                # Independent first-remainder identity: eta^107-I eta^107
                # equals W(eta)*(eta+sum multiplicity*node).
                total=sum((c*p for c,p in nodes),F(0))
                first=[-v for v in rem]+[F(0),F(1)]
                expected=[F(0)]*108
                for i,v in enumerate(w):
                    expected[i]+=total*v;expected[i+1]+=v
                assert first==expected
            out[k]=[m[k]-sum((v*m[i] for i,v in enumerate(rem)),F(0)) for m in mu]
        lead=rem[-1];rem=[F(0)]+rem[:-1]
        for i in range(N):rem[i]-=lead*w[i]
    return w,out

def inverse(a):
    n=len(a)
    w=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        p=next(i for i in range(k,n) if w[i][k])
        w[k],w[p]=w[p],w[k]
        d=w[k][k];w[k]=[x/d for x in w[k]]
        for i in range(n):
            if i!=k and w[i][k]:
                d=w[i][k];w[i]=[a-d*b for a,b in zip(w[i],w[k])]
    return [row[n:] for row in w]

def rank_mod(a,p=1000000007):
    m=[[v.numerator%p*pow(v.denominator%p,-1,p)%p for v in row] for row in a]
    rank=0
    for k in range(len(m[0])):
        row=next((i for i in range(rank,len(m)) if m[i][k]),None)
        if row is None:continue
        m[rank],m[row]=m[row],m[rank]
        d=pow(m[rank][k],-1,p);m[rank]=[v*d%p for v in m[rank]]
        for i in range(rank+1,len(m)):
            d=m[i][k];m[i]=[(a-d*b)%p for a,b in zip(m[i],m[rank])]
        rank+=1
    return rank

def serialized(a):return [[str(v) for v in row] for row in a]

def run(source,certificate):
    raw=Path(source).read_bytes()
    z=json.loads(Path(certificate).read_text())
    assert z['original_source_count']==470 and z['Hermite_original_generator_count']==106
    assert z['true_continuous_SI29_feature_count']==14
    assert max(map(F,z['exact_feature_uniform_pointwise_errors']))<F(1,10**21)
    assert z['actual_original_weighted_Schur_T']=='OPEN'
    nodes,features=constants(source)
    assert max(c for c,p in nodes)<15 and max(c+r for c,r,d in features)<15
    W,jets=residual_jets(nodes,features,133)
    M=[jets[k] for k in POWERS]
    assert all(M[0])
    leading=M[0]
    normalized=[[v/leading[j] for j,v in enumerate(row)] for row in M]
    assert rank_mod(normalized)==14
    C=inverse(normalized)
    scales=[F((-1)**((k-1)//2)*factorial(k))/(2*PI_UP)**k for k in POWERS]
    U=[[C[i][j]*scales[j]/leading[i] for j in range(14)] for i in range(14)]
    # Physical coefficient is (-1)^((k-1)/2)*(2*pi)^k/k!*(M U)_kj.
    # Thus transformed jets are diagonal with positive (pi/pi_up)^k.
    assert all(sum((M[i][k]*U[k][j] for k in range(14)),F(0))==
               (scales[i] if i==j else 0) for i in range(14) for j in range(14))
    assert (PI_LO/PI_UP)**133>F(9,10)
    # Let P_K be the exact degree-K Taylor polynomial defined by the
    # generator above and the transform U. Hermite remainder of eta^k:
    # <= binom(k,N)*W_band*15^(k-N).
    # Hence after K, |G-P_K| <= weight*sum_(n>=K+1-N) lambda^n/n!.
    # The derivative gains (N+n)/B. Ratios below bound both tails.
    K=639;n=K+1-N
    lam=2*PI_UP*B*15
    rho=lam/F(n+1)
    rho1=lam*F(N+n+1,(n+1)*(N+n))
    assert 0<rho<1 and 0<rho1<1
    base=lam**n/factorial(n)
    error=[]
    for j in range(14):
        # Finite upward integer compaction of the transformation norm;
        # use the independently certified uniform 1e-21 residual ceiling.
        weight=F(sum(abs(U[i][j]).__ceil__() for i in range(14)),10**21)
        e=weight*base/(1-rho)
        de=weight*F(N+n,B)*base/(1-rho1)
        variation=2*e+2*B*de
        energy=36*2*B*e*e+variation*variation
        Ao_strong2=36**2*2*B*e*e+F(325,18)*variation*variation
        # ||s||^2<1; Astar=Ao-2|s><s|.
        Astar_strong2=2*Ao_strong2+8*2*B*e*e
        assert e<F(1,10**95)
        assert energy<F(1,10**180) and Astar_strong2<F(1,10**180)
        error.append(dict(column=j,weighted_uniform_residual_ceiling=str(weight),
                          uniform_function_tail=str(e),uniform_derivative_tail=str(de),
                          original_Astar_form_error_upper=str(energy),
                          original_Astar_strong_error_squared_upper=str(Astar_strong2)))
    # Actual original pole norm=sinh(11/10)-11/10<1.
    # Original Hermite source's positive-series helper supplies that check
    # in the workflow; all Fourier/domain identifications remain inherited.
    return dict(status='CERTIFIED_CONDITIONAL_ACTUAL_SI29_RESIDUAL_JET_COORDINATES',
        hermite_source_sha256=hashlib.sha256(raw).hexdigest(),
        original_J_source_count=470,hermite_interpolating_source_count=106,feature_count=14,
        interpolation_nodes=[[str(c),p] for c,p in nodes],
        feature_definitions=[[str(c),str(r),d] for c,r,d in features],
        first_nonzero_candidate_powers=list(POWERS),
        frequency_residual_moment_matrix=serialized(M),
        rational_feature_transform=serialized(U),
        exact_transformed_jet_scales=list(map(str,scales)),
        normalized_physical_leading_coefficients_in_interval=['9/10','1'],
        exact_modular_jet_rank=14,modulus=1000000007,
        certified_series_truncation_degree=K,series_tail_errors=error,
        full_degree639_polynomial_coefficients_materialized=False,
        coefficient_generator='residual_jets(nodes,features,max_degree)',
        original_auxiliary_features_changed=False,
        physical_residual_basis_independence_certified=True,
        independence_modulo_full_J470_certified=False,
        Astar_energy_condition_number_certified=False,
        actual_full_J470_energy_Schur_T_computed=False,
        normalized_forcing_computed=False,normalized_inverse_response_certified=False,
        inherited_original_analytic_domain_review='OPEN',odd_even_CC27_Weil_RH='OPEN')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--source',required=True)
    p.add_argument('--certificate',required=True)
    p.add_argument('--output',default='artifacts/si29_normalized_residual_coordinates.json')
    args=p.parse_args()
    r=run(args.source,args.certificate)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(r,indent=2)+'\n')
    print('ACTUAL SI29 RESIDUAL COORDINATES PASS: exact jet rank 14; powers 107..133')
    print('Degree639 uniform error <1e-95; Astar strong squared error <1e-180')
    print('Full-J energy T, matched forcing, response and global signed operator OPEN')
