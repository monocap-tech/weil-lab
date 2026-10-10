"""RC51: signed archimedean-pole covariance, with paid source approximation."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import json,hashlib,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc31_trial_riesz import psd,mm,tr
from validate_rpb108_rc35_enriched_residuals import integrate
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc47_correlated_native_transport import root,matrix,entries,intersect,serialize,rows
from validate_rpb108_rc49_prime_pole_covariance import relative_upper
from validate_rpb108_rc50_archimedean_source_covariance import source_forms

B=F(11,10);N=128

def exponential_moments(forms,mom,R,Q,replay=False):
    tail=2*B**(N+1)/factorial(N+1)
    assert B/F(N+2)<F(1,2)
    ep=[I(B**n/factorial(n)) for n in range(N+1)]
    em=[I((-B)**n/factorial(n)) for n in range(N+1)]
    values=[]
    for j,(A,C,D) in enumerate(forms):
        # Direct three-log integration versus a reflected two-log identity.
        a=integrate(A,ep,mom[0]);c=integrate(C,ep,mom[1])
        if replay:
            d=(-1)**j*I(B).exp()*integrate(C,em,mom[1])
        else:d=integrate(D,ep,mom[2])
        z=R*I(-B/2).exp()*(a+c+d)
        # The direct exponential tail uses Cauchy and the certified nominal norm.
        # Reflected replay has separate +/- tails and log-coefficient L1 bounds.
        if replay:
            def l1(p):return sum((max(abs(F(x.l)),abs(F(x.h))) for x in p),F(0))
            rad=I(R*tail)*(I(l1(A))+I(l1(C))*(1+I(B).exp()))
        else:rad=I(tail*root(R*Q[(j,j)][1]))
        values.append(z+I(rad.h.copy_negate(),rad.h))
        print('archimedean exponential moment',j,'reflected' if replay else 'direct',file=sys.stderr,flush=True)
    return values,tail

def run(paths,replay=False,certificate=None):
    raw=[Path(p).read_bytes() for p in paths]
    native,pole,transport,arch,joint,acov,pcov,metric=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert pole['source_certificate_sha256']==hashes[0]
    assert [transport['input_sha256'][k] for k in [0,2,3,5]]==[hashes[k] for k in [7,0,1,3]]
    assert [acov['input_sha256'][k] for k in [0,2,3,4,5]]==[hashes[k] for k in [7,0,2,3,4]]
    assert [joint['input_sha256'][k] for k in [0,2,3,4]]==[hashes[k] for k in [0,1,2,6]]
    assert pcov['input_sha256'][0]==hashes[0] and pcov['input_sha256'][2]==hashes[2]
    forms,trials,mom,R,metric_delta=source_forms(native,arch)
    delta=F(acov['archimedean_remainder_source_approximation_operator_error_upper'])
    assert delta>=metric_delta-F(488163,2*10**9)+R*F(arch['regular_kernel_uniform_error_upper'])
    Q=entries(acov['nominal_physical_archimedean_source_Gram_entry_enclosures'])
    H=entries(acov['nominal_trial_archimedean_remainder_head_entry_enclosures'])
    z,tail=exponential_moments(forms,mom,R,Q,replay)
    saved=[]
    for j,value in enumerate(z):
        if replay:
            row=certificate['nominal_archimedean_source_exponential_moment_enclosures'][j]
            a,b=F(row['lower']),F(row['upper'])
            assert I(a).h<=value.l<=value.h<=I(b).l
        else:a,b=outward(value,10**35)
        saved.append((a,b))
    m=[rational_interval(F(r['lower']),F(r['upper'])) for r in joint['trial_pole_moment_enclosures']]
    O=entries(joint['trial_physical_pole_source_Gram_entry_enclosures'])
    cross={};U={};J={};center=[[F(0)]*8 for _ in range(8)];half=F(0)
    for i in range(8):
        for j in range(i,8):
            key=i,j
            if (i-j)%2:cross[key]=U[key]=J[key]=(F(0),F(0));continue
            zi=rational_interval(*saved[i]);zj=rational_interval(*saved[j]);sign=(-1)**i
            x=2*sign*(m[j]*zi+m[i]*zj)
            cross[key]=outward(x,10**25)
            U[key]=outward(rational_interval(*Q[key])+x+rational_interval(*O[key]),10**25)
            J[key]=outward(rational_interval(*H[key])+2*sign*m[i]*m[j],10**25)
            a,b=U[key];assert b-a<F(1,10**18)
            center[i][j]=center[j][i]=(a+b)/2;half=max(half,(b-a)/2)
    P=matrix(native['physical_native_Gram']);V=matrix(native['native_trial_coefficients'])
    mass=list(map(F,metric['physical_mass']))
    T=mm(mm(tr(V),[[mass[i]*(i==j) for j in range(32)] for i in range(32)]),V)
    assert psd([[P[i][j]-F(1,8)*(i==j) for j in range(8)] for i in range(8)])
    Uup=[[center[i][j]+64*half*P[i][j] for j in range(8)] for i in range(8)];assert psd(Uup)
    k=[8+2*F(pole[name]) for name in ['cosh_physical_norm_squared_upper','sinh_physical_norm_squared_upper']]
    ep=list(map(F,transport['physical_Riesz_error_column_norm_upper']))
    snom=[root(U[(i,i)][1]) for i in range(8)];v=[root(T[i][i]) for i in range(8)]
    s=[snom[i]+delta*v[i] for i in range(8)]
    d=[delta*v[i]+k[i%2]*ep[i] for i in range(8)]
    M=entries(transport['refined_actual_native_Gram_entry_enclosures'])
    olda=entries(acov['actual_native_archimedean_head_entry_enclosures'])
    oldo=entries(transport['refined_actual_signed_pole_head_entry_enclosures'])
    prime=entries(pcov['actual_native_prime_head_entry_enclosures'])
    oldfull=entries(acov['actual_original_Weil_low_head_entry_enclosures'])
    actual={};source={};full={};ratios=[]
    for i in range(8):
        for j in range(i,8):
            key=i,j
            if (i-j)%2:actual[key]=source[key]=full[key]=(F(0),F(0));continue
            a,b=J[key]
            rad=delta*root(T[i][i]*T[j][j])+ep[i]*s[j]+ep[j]*s[i]+k[i%2]*ep[i]*ep[j]
            prior=(olda[key][0]+oldo[key][0],olda[key][1]+oldo[key][1])
            actual[key]=intersect((M[key][0]+a-rad,M[key][1]+b+rad),prior)
            ratios.append((prior[1]-prior[0])/(actual[key][1]-actual[key][0]))
            a,b=U[key];sr=d[i]*snom[j]+d[j]*snom[i]+d[i]*d[j]
            source[key]=(max(F(0),a-sr) if i==j else a-sr,b+sr)
            a,b=actual[key];full[key]=intersect((a+prime[key][0],b+prime[key][1]),oldfull[key])
    Berr=matrix(transport['actual_physical_Riesz_error_Gram_Loewner_upper']);rho=F(252,257)
    assert all(Berr[i][j]==0 for i in range(8) for j in range(8) if (i-j)%2)
    error=[[F(33,32)*k[i%2]*k[j%2]*Berr[i][j]+33*delta**2*T[i][j] for j in range(8)] for i in range(8)]
    candidates=[]
    for t in [F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(1)]:
        A=[[rho*((1+t)*Uup[i][j]+(1+1/t)*error[i][j]) for j in range(8)] for i in range(8)]
        candidates.append((relative_upper(A,P),t,A))
    lam,t,A=min(candidates,key=lambda x:x[0]);alpha=F(native['canonical_native_Gram_physical_lower_factor'])
    bound=lam/alpha
    separate=(root(F(acov['whole_actual_archimedean_remainder_source_Gram_relative_native_metric_upper']))+
              F(pole['canonical_signed_pole_operator_norm_upper']))**2
    assert bound<F(2797,250) and separate/bound>F(171,20)
    assert min(ratios)>F(1001,1000)
    assert all(cross[(i,i)][1]<0 if i%2==0 else cross[(i,i)][0]>0 for i in range(8))
    assert full[(6,7)]==M[(6,7)]==(F(0),F(0))
    assert all(full[(i,i)][0]>M[(i,i)][1]/25 for i in [6,7])
    return dict(milestone='RC51',status='PASS',input_sha256=hashes,native_features_certified=list(range(8)),
        source_bound_feature_scope='native features 0 through 7 only',
        exponential_degree=N,exponential_uniform_remainder_upper=str(tail),
        archimedean_source_approximation_operator_error_upper=str(delta),
        nominal_archimedean_source_exponential_moment_enclosures=[dict(j=j,lower=str(a),upper=str(b)) for j,(a,b) in enumerate(saved)],
        nominal_symmetrized_archimedean_pole_source_cross_Gram_entry_enclosures=rows(cross),
        nominal_physical_joint_archimedean_pole_source_Gram_entry_enclosures=rows(U),
        nominal_joint_archimedean_pole_remainder_head_entry_enclosures=rows(J),
        nominal_physical_joint_archimedean_pole_source_Gram_Loewner_upper=serialize(Uup),
        true_trial_joint_archimedean_pole_source_column_norm_upper=list(map(str,s)),
        actual_physical_joint_archimedean_pole_source_Gram_entry_enclosures=rows(source),
        actual_joint_archimedean_pole_head_entry_enclosures=rows(actual),
        joint_head_includes_canonical_native_Gram=True,
        actual_original_Weil_low_head_entry_enclosures=rows(full),
        actual_canonical_joint_archimedean_pole_source_Gram_Loewner_upper=serialize(A),
        whole_actual_joint_archimedean_pole_source_Gram_relative_native_metric_upper=str(bound),
        separate_component_triangle_source_Gram_relative_native_metric_upper=str(separate),
        source_transport_Young_parameter=str(t),joint_physical_operator_parity_norm_upper=list(map(str,k)),
        minimum_joint_head_width_improvement_factor_lower=str(min(ratios)),
        nominal_cross_diagonal_signs=['negative' if cross[(i,i)][1]<0 else 'positive' if cross[(i,i)][0]>0 else 'unresolved' for i in range(8)],
        complete_head_diagonals_certified_positive=[i for i in range(8) if full[(i,i)][0]>0],
        certified_positive_native_subspace_features=[6,7],original_Weil_floor_on_certified_two_feature_subspace_lower='1/25',
        complete_archimedean_prime_pole_covariance_evaluated=False,
        actual_canonical_joint_source_Gram_evaluated=False,original_Weil_head_floor_certified=False,
        full_1250_native_projection_constructed=False,aperture_extended=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc42_native_signed_pole_head.json',
        'rpb108_rc47_correlated_native_transport.json','rpb108_rc46_native_archimedean_head.json',
        'rpb108_rc49_prime_pole_covariance.json','rpb108_rc50_archimedean_source_covariance.json',
        'rpb108_rc48_prime_source_covariance.json','rpb108_rc38_thirty_two_metric.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        cert=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,cert)==cert
        print('PASS: independent reflected exponential/log moments, signed mixed covariance, paid approximation, actual transport and exact rational PSD bounds')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
