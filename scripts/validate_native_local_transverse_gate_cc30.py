"""Exact CC30 premise controls; no actual zeta covariance is computed."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_critical_flux_limit_cc29 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]

def run():
    counts={k:0 for k in ('near_far_split','sparse_cluster','finite_prefix','genuine_crossing','full_mass')}
    def check(v,k):
        assert v,k
        counts[k]+=1
    betas=[F(k,64) for k in range(-24,25)]
    for eps in (F(1,64),F(1,32),F(1,16),F(1,8),F(1,4)):
        near=[b for b in betas if abs(b)<=eps]
        far=[b for b in betas if abs(b)>eps]
        mass=sum(b*b for b in betas)
        right=sum(1 for b in betas if b>eps)
        check(eps*eps*right<=mass,'near_far_split')
        check(len(far)==2*right,'near_far_split')
        check(mass<=eps*eps*len(betas)+F(1,4)*len(far),'near_far_split')
        check(sum(b*b for b in near)<=eps*eps*len(betas),'near_far_split')
    b=F(1,8);cumulative=0
    for j in range(4,13):
        m=2**j;T=2**m;cumulative+=m
        check(cumulative==2*m-16<2*m,'sparse_cluster')
        check(4*b*b*cumulative<F(8)*b*b*m,'sparse_cluster')
        check(4*b*b*cumulative<=F(T,m),'sparse_cluster')
        check(F(2)*b*b*m/F(m)==F(1,32),'sparse_cluster')
        check(F(2*m,m)==2,'sparse_cluster')
        check(T>m*m and T>2**(m//2),'sparse_cluster')
        check(all(T+1<2**(2**k) for k in range(j+1,14)),'sparse_cluster')
        # Finite prefix has zero local tail once its last height is passed.
        prefix=[2**(2**k) for k in range(4,j+1)]
        check(sum(1 for theta in prefix if T+2<=theta<T+3)==0,'finite_prefix')
    v=F(17,16)
    for j in (8,16,32,48,64):
        u=1-F(1,2**j);gap=1-u*u;leak=2*u*(v-u)
        check(leak>F(1,16),'genuine_crossing')
        check(leak/gap>F(2)**(j-6),'genuine_crossing')
        check(leak*leak/gap>F(2)**(j-10),'genuine_crossing')
        check(2*u*(1-u)/gap==2*u/(1+u)<1,'genuine_crossing')
    a,k,mu=F(9,25),F(12,25),F(16,25)
    lam=a*a+mu;gap=1-lam
    critical=a*a*k*k/(lam*gap)
    low=k*k+mu-a*a*k*k/lam
    check(k*k/(1-a*a)==F(9,34)<1,'full_mass')
    check(lam==F(481,625) and gap==F(144,625),'full_mass')
    check(critical+low==1 and low>0,'full_mass')
    inherited=inherited_run()
    assert inherited['all_passed'] and inherited['total_exact_checks']==24872
    paths=['scripts/validate_native_critical_flux_limit_cc29.py',
           'notes/REFLECTED_PACKET_BRIDGE_108_TRANSVERSE_DENSITY_SAMPLING_20261007.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_DENSITY_PHASE_CC22_20261008.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_CRITICAL_FLUX_LIMIT_CC29_20261008.md']
    return {'stage':'CC30 local transverse premise / Lindelof gate',
            'all_passed':True,'new_counts':counts,
            'new_exact_checks':sum(counts.values()),'inherited_cc29_checks':24872,
            'total_exact_checks':24872+sum(counts.values()),
            'analytic_result':'complete local second transverse mass o(log T) iff Lindelof, via imported Backlund criterion',
            'scope':'location premise audit; artificial cluster controls do not satisfy actual Weil EF',
            'local_transverse_vanishing_proved_unconditionally':False,
            'actual_critical_covariance_evaluated':False,'RH_proved':False,
            'new_aperture':False,'lean_certified':False,
            'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_LOCAL_TRANSVERSE_GATE_CC30_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
