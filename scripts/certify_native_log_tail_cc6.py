"""Exact finite controls for CC6's analytic retained-tail comparison theorem.

Euler--Maclaurin and its whole-frequency remainder are proved in the note;
finite controls do not substitute for that proof. Only stdlib is required.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parents[1]

def bernoulli(n):
    values=[F(1)]
    for m in range(1,n+1):
        values.append(-sum((comb(m+1,j)*values[j] for j in range(m)),F(0))/F(m+1))
    return values

def epsilon(N,K):
    return 8*F(factorial(2*K-1))/(6*(F(N)+F(1,4)))**(2*K)

def logarithm(v):
    assert v>=1
    shifts=0
    while v>=2:
        v/=2;shifts+=1
    def small(t):
        z=(t-1)/(t+1)
        total=sum((2*z**(2*j+1)/F(2*j+1) for j in range(200)),F(0))
        tail=2*z**401/F(401)/(1-z*z)
        return total,total+tail
    a,b=small(v);c,d=small(F(2))
    return a+shifts*c,b+shifts*d

def tail_model(N,K,x,B):
    q=F(N)+F(1,4)
    l,u=logarithm(1+x*x/(q*q))
    correction=x*x/(2*q*(q*q+x*x))
    real,imag=q/(q*q+x*x),-x/(q*q+x*x)
    power=(F(1),F(0))
    for degree in range(1,2*K+1):
        power=(power[0]*real-power[1]*imag,power[0]*imag+power[1]*real)
        if degree%2==0:
            correction+=B[degree]/degree*(q**(-degree)-power[0])
    return l/2+correction,u/2+correction

def run():
    B=bernoulli(64)
    assert B[1]==-F(1,2) and B[2]==F(1,6) and B[4]==-F(1,30)
    assert B[6]==F(1,42) and B[8]==-F(1,30) and B[10]==F(5,66)
    assert all(B[j]==0 for j in range(3,64,2))
    eps=epsilon(32,32);delta=2*eps
    assert eps<F(8,10**59) and delta<F(16,10**59)
    geometric_controls=0
    for n in range(1,65):
        assert epsilon(n,n)<=F(8,9**n)
        geometric_controls+=1
    controls=0
    # Two exact tail decompositions must enclose a common exact tail.
    # The shifted model has a MUCH smaller analytic remainder.
    for x in map(F,[0,1,3,10,32,100,1000,1000000]):
        l,u=tail_model(32,32,x,B)
        ll,uu=tail_model(96,32,x,B)
        partial=sum((x*x/((F(j)+F(1,4))*((F(j)+F(1,4))**2+x*x)) for j in range(32,96)),F(0))
        small_eps=epsilon(96,32)
        assert max(l-eps,partial+ll-small_eps)<=min(u+eps,partial+uu+small_eps)
        if x==0:
            assert l==u==ll==uu==partial==0
        controls+=1
    source=ROOT/'notes/data/RPB108_CUTOFF_LOSS_CC5_CERTIFICATE_20261008.json'
    imported=json.loads(source.read_text())
    mass=F(imported['witness_mass_squared'])
    qlo,qhi=map(F,imported['native_witness_interval'])
    witness_lower=qlo-delta*mass
    assert witness_lower>0 and witness_lower/mass>F(187,10**34)
    anchor_mass=F(4,10**32)-delta
    anchor_canonical=F(2,10**34)-delta
    assert anchor_mass>F(399,10**34) and anchor_canonical>F(199,10**36)
    # Genuine coupled completions, with all matrix blocks perturbed together.
    schur_controls=0
    for c in (F(1,2),F(1),F(3)):
        for d in (c/100,c/10,c/2):
            for k in (F(-3),F(0),F(2)):
                for s in (F(0),F(1,10**32),F(1,10)):
                    for v in ((F(1),F(0)),(F(0),F(1)),(F(1),F(2)),(F(-2),F(3))):
                        norm=v[0]**2+v[1]**2
                        r00=d*v[0]**2/norm;r01=d*v[0]*v[1]/norm;r11=d*v[1]**2/norm
                        a=s+k*k/c-r00;b=k-r01;cc=c-r11
                        assert cc>0
                        sm=a-b*b/cc
                        graphmass=1+k*k/(c*c)
                        lossbudget=d*c/(c-d)*graphmass
                        assert s-lossbudget<=sm<=s
                        schur_controls+=1
    # The lower comparison can touch earlier than an original positive level.
    mu=delta/2
    assert mu>0 and mu-delta<0
    result={
        'stage':'CC6 retained logarithmic Euler-tail comparison',
        'N':32,'K':32,'epsilon_uniform':str(eps),'mass_defect_delta':str(delta),
        'uniform_real_frequency_bound_analytic':True,
        'radius_free_log_principal_part_retained':True,
        'tail_decomposition_finite_controls':controls,
        'geometric_accuracy_finite_controls':geometric_controls,
        'exact_coupled_schur_controls':schur_controls,
        'saved_native_positive_witness_lower_comparison':str(witness_lower),
        'saved_native_positive_witness_rayleigh_lower_comparison':str(witness_lower/mass),
        'anchor_lower_comparison_physical_margin':str(anchor_mass),
        'anchor_lower_comparison_canonical_margin':str(anchor_canonical),
        'cc5_certificate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'cc5_native_replay_imported_not_rerun':True,
        'complete_original_prime_pole_source_identity_preserved':True,
        'comparison_gain_identified_with_nf63_gain':False,
        'new_aperture_certificate':False,
        'arithmetic_relative_loss_nondivergence_bound':False,
        'lean_certified':False,
        'displays':{'epsilon_uniform':float(eps),'witness_rayleigh_lower_comparison':float(witness_lower/mass)}
    }
    return result

if __name__=='__main__':
    result=run()
    print(json.dumps(result,indent=2))
