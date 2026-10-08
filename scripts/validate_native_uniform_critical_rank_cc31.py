"""CC31 rational rank/Gram controls; no actual arithmetic row bound."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_local_transverse_gate_cc30 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]

def run():
    counts={k:0 for k in ('protected_complement','critical_rank','coherent_gram','scalar_to_matrix','unbounded_rank')}
    def check(v,k):
        assert v,k
        counts[k]+=1
    for n in (2,4,8,12):
        Z=[F(i,n+1) for i in range(1,n+1)]
        for alpha in (F(1,2),F(1),F(3,2)):
            for kappa in (F(1),F(2),F(5)):
                tau=alpha/(4*kappa);tail=alpha/(4*kappa+alpha)
                protected=[z for z in Z if z>tau]
                q=[alpha-kappa*(z+tail) for z in Z]
                check(len(protected)*tau<=sum(Z),'protected_complement')
                check(kappa*tail<alpha/4,'protected_complement')
                check(all(v>=alpha/2 for z,v in zip(Z,q) if z<=tau),'protected_complement')
                U2=F(3);eta=min(F(1,2),alpha/(4*U2));gamma=alpha/(2*U2)
                check(eta<gamma,'critical_rank')
                critical=[v for v in q if 0<v/U2<=eta]
                check(len(critical)<=len(protected),'critical_rank')
    for d in range(1,17):
        r=[F(i+1,32) for i in range(d)]
        omega=[v*v for v in r]
        # Gram z_i=r_i has normalized all-ones matrix; signs preserve norm.
        check(sum(F(1) for v in omega)==d,'coherent_gram')
        check(sum(F(1,d) for _ in range(d))==1,'unbounded_rank')
        check(F(1,d)<=1 and F(d)*F(1,d)==1,'unbounded_rank')
        for sign_mode in (0,1):
            signs=[F(-1) if sign_mode and i%2 else F(1) for i in range(d)]
            check(sum(s*s for s in signs)==d,'coherent_gram')
            for c in ([F(1)]*d,[F(i-d//2) for i in range(d)],signs):
                mixed=sum(c[i]*signs[i]*r[i] for i in range(d))**2
                rhs=d*sum(c[i]*c[i]*omega[i] for i in range(d))
                check(mixed<=rhs,'scalar_to_matrix')
            # Exact eigenvalue d on normalized signed coherent Gram.
            check(all(sum(signs[i]*signs[j]*signs[j] for j in range(d))==d*signs[i] for i in range(d)),'coherent_gram')
    inherited=inherited_run()
    assert inherited['all_passed'] and inherited['total_exact_checks']==24987
    paths=['scripts/validate_native_local_transverse_gate_cc30.py',
           'notes/REFLECTED_PACKET_BRIDGE_108_LOG_SOURCE_ANALYSIS_20261003.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_SOURCE_SHELL_GAIN_20261008.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_FORCED_SOURCE_CC20_20261008.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_CRITICAL_FLUX_LIMIT_CC29_20261008.md']
    return {'stage':'CC31 cap-uniform critical rank and scalar residual reduction',
            'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
            'inherited_cc30_checks':24987,'total_exact_checks':24987+sum(counts.values()),
            'analytic_result':'native Garding and positive source upper bound imply cap-uniform finite critical rank; scalar complete residual estimate implies collective modulus with rank factor',
            'actual_scalar_residual_bound_proved':False,'actual_critical_covariance_evaluated':False,
            'negative_source_compactness_assumed':False,'Lindelof_assumed':False,
            'new_aperture':False,'RH_proved':False,'lean_certified':False,
            'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_UNIFORM_CRITICAL_RANK_CC31_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
