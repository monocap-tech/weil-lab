"""CC7 exact target budgets and whole-resolvent finite controls.

Imports saved actual complement/source bounds and CC3 directional certificate.
Does not evaluate the whole shifted inverse or reconstruct blocked archives.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[1]

def bernoulli(n):
    b=[F(1)]
    for k in range(1,n+1):
        b.append(-sum((comb(k+1,j)*b[j] for j in range(k)),F(0))/F(k+1))
    return b

def run():
    source=ROOT/'notes/data/RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json'
    trial=ROOT/'notes/data/RPB108_COUPLED_TRIAL_CC3_CERTIFICATE_20261008.json'
    saved=json.loads(source.read_text());cc3=json.loads(trial.read_text())
    assert saved['aperture']==cc3['aperture']=='21/20'
    assert saved['input_sha256']['native']==cc3['native_sha256']
    c=F(saved['physical_complement_lower'])
    M=F(saved['surrogate_map_norm_upper']);eta=F(saved['complete_source_map_allowance'])
    gram_error=F(saved['actual_gram_operator_error_upper'])
    assert eta*(2*M+eta)==gram_error
    assert c==F(699,1000) and M+eta<8
    b=bernoulli(66)
    assert b[34]==F(2577687858367,6) and b[66]>0
    e=abs(b[66])/(33*F(129,4)**66)
    assert e<F(2,10**61)
    ce=c-e;Be=8+e
    assert ce>F(698,1000) and Be<F(81,10)
    inverse_error=e/(c*ce)
    graphmass=1+F(64)/(c*c)
    assert graphmass<133
    schur_error=e*c/ce*graphmass
    assert schur_error<F(3,10**59)
    mass=F(saved['witness_mass_squared'])
    direction_lower=F(cc3['trial_lower'][0])-schur_error*mass
    assert direction_lower>F(624,10**35)
    m=128;inverse_tail=1/(ce*2**(m+1))
    head_schur_budget=inverse_tail*Be*Be
    assert head_schur_budget<F(2,10**37)
    controls=0
    # Exact scalar spectral identities, not sampling used to prove the theorem.
    for cp in (F(1,3),ce,F(1),F(7)):
        for ratio in (F(1),F(2),F(7),F(100)):
            lam=cp*ratio;L=lam+cp
            for degree in (0,1,2,8,32,128):
                P=sum((cp**k/L**(k+1) for k in range(degree+1)),F(0))
                rem=1/lam-P
                assert rem==(cp/L)**(degree+1)/lam
                assert 0<=rem<=1/(cp*2**(degree+1))
                controls+=1
    # Cross-prime/mixed information is in L; powers do not diagonalize sources.
    matrix_controls=0
    for cp in (F(1,2),F(1),F(3)):
        for off in (F(-2),F(1),F(4)):
            # A genuine mixed complement C=cp I+vv*, with exact spectral projectors.
            v=(F(1),off);norm=1+off*off
            for Bvec in ((F(1),F(0)),(F(1),F(2)),(F(-3),F(1))):
                parallel=(Bvec[0]+off*Bvec[1])**2/norm
                total=Bvec[0]**2+Bvec[1]**2
                perpendicular=total-parallel
                assert perpendicular>=0
                exact=parallel/(cp+norm)+perpendicular/cp
                for degree in (0,2,8):
                    def p(lam):
                        return sum((cp**k/(lam+cp)**(k+1) for k in range(degree+1)),F(0))
                    head=parallel*p(cp+norm)+perpendicular*p(cp)
                    assert head<=exact<=head+total/(cp*2**(degree+1))
                    matrix_controls+=1
    # Forbidden finite-head sign inference: a positive Schur head may fail after tail.
    cp=F(1);degree=0;lam=cp;Bnorm2=F(1)
    inverse_head=F(1,2);A=F(3,4)
    assert A-Bnorm2*inverse_head>0 and A-Bnorm2/lam<0
    return {
        'stage':'CC7 actual protected complement and Schur transfer',
        'aperture':'21/20','N':32,'even_corrections':32,
        'signed_tail_error':str(e),'original_complement_lower':str(c),
        'comparison_complement_lower':str(ce),
        'actual_source_map_norm_strict_upper':'8',
        'comparison_source_map_norm_upper':str(Be),
        'whole_complement_inverse_error_upper':str(inverse_error),
        'whole_original_graph_mass_norm_squared_upper':str(graphmass),
        'whole_exact_schur_comparison_error_upper':str(schur_error),
        'actual_saved_completed_schur_direction_comparison_lower':str(direction_lower),
        'completed_direction_positive':True,
        'shifted_resolvent_head_degree':m,
        'whole_inverse_head_tail_upper':str(inverse_tail),
        'whole_schur_head_tail_upper':str(head_schur_budget),
        'scalar_resolvent_controls':controls,'mixed_complement_controls':matrix_controls,
        'positive_head_as_lower_bound_control_rejected':True,
        'whole_shifted_inverse_head_evaluated':False,
        'full_target_schur_sign_certified':False,
        'new_whole_aperture_certificate':False,
        'original_loss_nondivergence_bound':False,'lean_certified':False,
        'input_sha256':{'saved_target':hashlib.sha256(source.read_bytes()).hexdigest(),
                        'actual_trial':hashlib.sha256(trial.read_bytes()).hexdigest()},
        'displays':{'signed_tail_error':float(e),'inverse_error':float(inverse_error),
                    'whole_schur_comparison_error':float(schur_error),
                    'completed_direction_lower':float(direction_lower),
                    'whole_schur_head_tail':float(head_schur_budget)}
    }

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
