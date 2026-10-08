"""CC5 replay of actual native witness and exact cutoff-tail obstruction budgets.

The support-uncertainty and infinite Euler-tail lower bound are analytic proofs
in the companion note; this script audits their finite rational consequences.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import gzip,hashlib,json

ROOT=Path(__file__).resolve().parents[1]

def tail_floor(a,N):
    assert a>0 and N>=0
    return 1/(24*a*a*(F(N)+F(1,4))**2+6)

def run():
    path=ROOT/'notes/data/RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json'
    witness_raw=path.read_bytes();saved=json.loads(witness_raw)
    raw=gzip.decompress((ROOT/'notes/data/RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
    native_hash=hashlib.sha256(raw).hexdigest()
    assert native_hash==saved['input_sha256']['native']
    native=json.loads(raw)
    assert native['aperture']==saved['aperture']=='21/20'
    assert native['matrix_encoding']=='row-major lower triangle integer endpoints on grid 10^-80'
    v=list(map(F,saved['rational_coefficient_witness']))
    assert len(v)==112
    scale=10**40
    integers=[int(x*scale) for x in v]
    assert all(F(n,scale)==x for n,x in zip(integers,v))
    mass=sum((x*x for x in v),F(0))
    assert mass==F(saved['witness_mass_squared']) and mass>0
    lo=hi=0;index=0
    for i in range(112):
        for j in range(i+1):
            l,u=map(int,native['lower_triangle_row_major'][index]);index+=1
            assert l<=u
            coefficient=integers[i]*integers[j]*(1 if i==j else 2)
            lo+=coefficient*(l if coefficient>=0 else u)
            hi+=coefficient*(u if coefficient>=0 else l)
    assert index==6328
    qlo,qhi=F(lo,10**160),F(hi,10**160)
    savedlo,savedhi=map(F,saved['native_weil_witness_interval'])
    assert qlo==savedlo and qhi==savedhi and qlo>0
    a=F(21,20);rayleigh=qhi/mass
    N=32;floor=tail_floor(a,N)
    comparison_upper=qhi-floor*mass
    assert comparison_upper<0 and floor-rayleigh>F(36,10**6)
    # NF63's positive background: imported joint prime bound, audited scalar
    # harmonic lower budget, and conservative upper bound from |m0-w|<10.
    B=F(1063939,500000)
    harmonic=sum((F(4,4*j+1) for j in range(32)),F(0))
    background_lower=-F(27,5)+harmonic-B
    assert background_lower>F(157,1000) and harmonic<8 and B<3
    sinh=sum((a**(2*k+1)/factorial(2*k+1) for k in range(21)),F(0))
    remainder=a**43/factorial(43)/(1-a*a/F(44*45))
    pole_positive_upper=2*(a+sinh+remainder)
    assert pole_positive_upper<5
    # m0(0)<11, H32<8, B<3, positive pole <5 => F32<27 mass.
    background_upper=F(27)
    gain_lower=1+(floor-rayleigh)/background_upper
    assert gain_lower>1+F(1,10**6)
    excluded_N=14*10**14
    assert tail_floor(a,excluded_N)>rayleigh
    # Tail floor decreases with N: the endpoint check excludes all smaller N.
    controls=0
    for aperture in (F(1,4),F(1,2),F(1),F(21,20),F(3)):
        r=1/(6*aperture)
        assert 4*aperture*r==F(2,3)
        for n in range(129):
            q=F(n)+F(1,4);u=9*r*r
            integral_tail=F(1,2*q*q)
            lower=(1-4*aperture*r)*u*q*q/(q*q+u)*integral_tail
            assert lower==tail_floor(aperture,n)>0
            assert tail_floor(aperture,n+1)<lower
            # A positive-level shift retains its mass term: at Q=mu mass,
            # shifted cutoff is negative, not an original zero/negative value.
            mu=F(1,100);tail=lower
            shifted=(mu-tail)-mu
            assert shifted==-tail<0 and mu>0
            controls+=3
    result=dict(stage='CC5 actual cutoff relative-loss obstruction',aperture=str(a),
        native_sha256=native_hash,witness_sha256=hashlib.sha256(witness_raw).hexdigest(),
        native_lower_triangle_entries_audited=index,rational_witness_coordinates=112,
        witness_mass_squared=str(mass),native_witness_interval=[str(qlo),str(qhi)],
        native_witness_positive=True,original_rayleigh_upper=str(rayleigh),
        cutoff_N=32,analytic_tail_floor=str(floor),
        comparison_witness_upper=str(comparison_upper),
        comparison_rayleigh_upper=str(rayleigh-floor),
        original_prime_and_pole_terms_unchanged=True,
        cutoff_background_lower=str(background_lower),cutoff_background_upper=str(background_upper),
        cutoff_compact_gain_lower=str(gain_lower),cutoff_gain_above_one_certified=True,
        excluded_cutoff_indices_inclusive=[0,excluded_N],
        excluded_index_endpoint_floor=str(tail_floor(a,excluded_N)),
        scalar_controls=controls,all_finite_checks_passed=True,
        analytic_support_uncertainty_proof=True,analytic_euler_tail_proof=True,
        analytic_proofs_lean_certified=False,full_target_source_gram_replayed=False,
        original_negative_weil_vector=False,new_aperture_certified=False,
        arithmetic_nondivergence_bound=False,
        displays=dict(original_rayleigh_upper=float(rayleigh),tail_floor_32=float(floor),
            comparison_rayleigh_upper=float(rayleigh-floor),comparison_witness_upper=float(comparison_upper),
            compact_gain_lower=float(gain_lower),excluded_endpoint_floor=float(tail_floor(a,excluded_N))),
        constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    return result

if __name__=='__main__':
    result=run()
    (ROOT/'notes/data/RPB108_CUTOFF_LOSS_CC5_CERTIFICATE_20261008.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['displays'],indent=2))
    print(json.dumps({k:result[k] for k in ['scalar_controls','native_lower_triangle_entries_audited','excluded_cutoff_indices_inclusive']}))
