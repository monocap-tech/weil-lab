"""RC52: remaining archimedean-prime covariance and complete signed source."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc31_trial_riesz import psd
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import shift
from validate_rpb108_rc47_correlated_native_transport import root,matrix,entries,intersect,serialize,rows
from validate_rpb108_rc48_prime_source_covariance import polynomials,geometry
from validate_rpb108_rc49_prime_pole_covariance import relative_upper
from validate_rpb108_rc50_archimedean_source_covariance import source_forms

def primitives(x,degree,endpoint=None):
    """Three primitive families; endpoint logarithmic limits are exact."""
    if endpoint==0:return [[I(0)]*(degree+1) for _ in range(3)]
    if endpoint==1:
        H=F(0);out=[[],[],[]]
        for k in range(degree+1):
            a=k+1;H+=F(1,a)
            out[0].append(I(F(1,a)));out[1].append(I(-F(1,a*a)));out[2].append(I(-H/a))
        return out
    assert x.l>0 and x.h<1
    powers=[I(1)]
    for _ in range(degree+1):powers.append(powers[-1]*x)
    lx=x.log();lr=(1-x).log();sum_power=I(0);out=[[],[],[]]
    for k in range(degree+1):
        a=k+1;p=powers[a];sum_power=sum_power+p/a
        out[0].append(p/a)
        out[1].append(p*(lx/a-F(1,a*a)))
        out[2].append(((p-1)*lr-sum_power)/a)
    return out

def mixed(forms,native,prime,R,replay=False):
    terms,segments=geometry(prime);polys=polynomials(native)
    translated=[]
    for term in terms:
        translated.append([[a*2**k for k,a in enumerate(shift([I(x) for x in p],term['offset']-1))] for p in polys])
    ordered=[[I(0)]*8 for _ in range(8)]
    cache={}
    for ln,rn,left,right,active in segments:
        for name,t in [(ln,left),(rn,right)]:
            if name not in cache:
                cache[name]=primitives((t+1)/2,255,0 if name=='left' else 1 if name=='right' else None)
        moments=[[cache[rn][kind][k]-cache[ln][kind][k] for k in range(256)] for kind in range(3)]
        sources=[[sum((terms[h]['coefficient']*translated[h][j][l] for h in active),I(0)) for l in range(32)] for j in range(8)]
        for i,(A,B,C) in enumerate(forms):
            weighted=[]
            for l in range(32):
                value=sum((a*moments[0][k+l] for k,a in enumerate(A)),I(0))
                value=value+(2 if replay else 1)*sum((a*moments[1][k+l] for k,a in enumerate(B)),I(0))
                if not replay:value=value+sum((a*moments[2][k+l] for k,a in enumerate(C)),I(0))
                weighted.append(R*value)
            for j in range(8):
                if (i-j)%2:continue
                ordered[i][j]=ordered[i][j]+sum((weighted[l]*sources[j][l] for l in range(32)),I(0))
        print('archimedean-prime segment',ln,rn,'reflected' if replay else 'direct',file=sys.stderr,flush=True)
    cross={}
    for i in range(8):
        for j in range(i,8):
            cross[i,j]=I(0) if (i-j)%2 else ordered[i][j]+ordered[j][i]
    return cross

def run(paths,replay=False,certificate=None):
    raw=[Path(p).read_bytes() for p in paths]
    native,prime,pole,transport,arch,pcov,ppcov,acov,apcov=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert prime['native_certificate_sha256']==pole['source_certificate_sha256']==hashes[0]
    assert [transport['input_sha256'][k] for k in [2,3,4,5]]==[hashes[k] for k in [0,2,1,4]]
    assert pcov['input_sha256']==[hashes[k] for k in [0,1,3]]
    assert ppcov['input_sha256']==[hashes[k] for k in [0,1,2,3,5]]
    assert [acov['input_sha256'][k] for k in [2,3,4,5]]==[hashes[k] for k in [0,3,4,6]]
    assert apcov['input_sha256'][:7]==[hashes[k] for k in [0,2,3,4,6,7,5]]
    forms,trials,mom,R,metric_delta=source_forms(native,arch)
    delta=F(acov['archimedean_remainder_source_approximation_operator_error_upper'])
    assert delta==F(apcov['archimedean_source_approximation_operator_error_upper'])
    assert delta>=metric_delta-F(488163,2*10**9)+R*F(arch['regular_kernel_uniform_error_upper'])
    X=mixed(forms,native,prime,R,replay)
    cross={}
    saved=entries(certificate['nominal_symmetrized_archimedean_prime_source_cross_Gram_entry_enclosures']) if replay else None
    for key,value in X.items():
        if replay:
            a,b=saved[key];assert I(a).h<=value.l<=value.h<=I(b).l;cross[key]=(a,b)
        else:cross[key]=(F(0),F(0)) if (key[0]-key[1])%2 else outward(value,10**25)
    AP=entries(apcov['nominal_physical_joint_archimedean_pole_source_Gram_entry_enclosures'])
    PP=entries(ppcov['trial_symmetrized_prime_pole_source_cross_Gram_entry_enclosures'])
    Psource=entries(pcov['trial_physical_prime_source_Gram_entry_enclosures'])
    HAP=entries(apcov['nominal_joint_archimedean_pole_remainder_head_entry_enclosures'])
    HP=entries(pcov['trial_prime_head_entry_enclosures'])
    U={};H={};center=[[F(0)]*8 for _ in range(8)];half=F(0)
    for i in range(8):
        for j in range(i,8):
            key=i,j
            if (i-j)%2:U[key]=H[key]=(F(0),F(0));continue
            U[key]=outward(sum((rational_interval(*d[key]) for d in [AP,Psource,PP,cross]),I(0)),10**25)
            H[key]=(HAP[key][0]+HP[key][0],HAP[key][1]+HP[key][1])
            a,b=U[key];assert b-a<F(1,10**18)
            center[i][j]=center[j][i]=(a+b)/2;half=max(half,(b-a)/2)
    P=matrix(native['physical_native_Gram']);T=matrix(prime['physical_native_trial_Gram'])
    assert psd([[P[i][j]-F(1,8)*(i==j) for j in range(8)] for i in range(8)])
    Uup=[[center[i][j]+64*half*P[i][j] for j in range(8)] for i in range(8)];assert psd(Uup)
    kp=F(prime['full_paired_prime_physical_operator_norm_upper'])
    k=[8+kp+2*F(pole[name]) for name in ['cosh_physical_norm_squared_upper','sinh_physical_norm_squared_upper']]
    ep=list(map(F,transport['physical_Riesz_error_column_norm_upper']))
    n=[root(U[i,i][1]) for i in range(8)];v=[root(T[i][i]) for i in range(8)]
    s=[n[i]+delta*v[i] for i in range(8)];d=[delta*v[i]+k[i%2]*ep[i] for i in range(8)]
    M=entries(transport['refined_actual_native_Gram_entry_enclosures'])
    old=entries(apcov['actual_original_Weil_low_head_entry_enclosures'])
    full={};source={};ratios=[]
    for i in range(8):
        for j in range(i,8):
            key=i,j
            if (i-j)%2:full[key]=source[key]=(F(0),F(0));continue
            rad=delta*root(T[i][i]*T[j][j])+ep[i]*s[j]+ep[j]*s[i]+k[i%2]*ep[i]*ep[j]
            a,b=H[key];full[key]=intersect((M[key][0]+a-rad,M[key][1]+b+rad),old[key])
            ratios.append((old[key][1]-old[key][0])/(full[key][1]-full[key][0]))
            a,b=U[key];sr=d[i]*n[j]+d[j]*n[i]+d[i]*d[j]
            source[key]=(max(F(0),a-sr) if i==j else a-sr,b+sr)
    Berr=matrix(transport['actual_physical_Riesz_error_Gram_Loewner_upper']);rho=F(252,257)
    assert all(Berr[i][j]==0 for i in range(8) for j in range(8) if (i-j)%2)
    error=[[F(33,32)*k[i%2]*k[j%2]*Berr[i][j]+33*delta**2*T[i][j] for j in range(8)] for i in range(8)]
    candidates=[]
    for t in [F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(1)]:
        A=[[rho*((1+t)*Uup[i][j]+(1+1/t)*error[i][j]) for j in range(8)] for i in range(8)]
        candidates.append((relative_upper(A,P),t,A))
    lam,t,A=min(candidates,key=lambda x:x[0]);alpha=F(native['canonical_native_Gram_physical_lower_factor'])
    bound=lam/alpha
    previous=(root(F(apcov['whole_actual_joint_archimedean_pole_source_Gram_relative_native_metric_upper']))+
              root(F(pcov['whole_actual_prime_source_Gram_relative_native_metric_upper'])))**2
    assert bound<F(1887,500) and previous/bound>F(511,50)
    assert min(ratios)>F(59,50)
    assert [i for i in range(8) if full[i,i][0]>0]==[1,2,3,4,6,7]
    assert all(full[i,i][0]>M[i,i][1]/21 for i in [6,7])
    assert full[6,7]==M[6,7]==(F(0),F(0))
    return dict(milestone='RC52',status='PASS',input_sha256=hashes,native_features_certified=list(range(8)),
        source_bound_feature_scope='native features 0 through 7 only',
        physical_partition_segments=15,archimedean_source_approximation_operator_error_upper=str(delta),
        nominal_symmetrized_archimedean_prime_source_cross_Gram_entry_enclosures=rows(cross),
        nominal_complete_signed_physical_source_Gram_entry_enclosures=rows(U),
        nominal_complete_signed_remainder_head_entry_enclosures=rows(H),
        nominal_complete_signed_physical_source_Gram_Loewner_upper=serialize(Uup),
        true_trial_complete_signed_source_column_norm_upper=list(map(str,s)),
        actual_complete_signed_physical_source_Gram_entry_enclosures=rows(source),
        actual_original_Weil_low_head_entry_enclosures=rows(full),
        actual_complete_signed_canonical_source_Gram_Loewner_upper=serialize(A),
        whole_actual_complete_signed_source_Gram_relative_native_metric_upper=str(bound),
        previous_split_source_triangle_Gram_relative_native_metric_upper=str(previous),
        source_transport_Young_parameter=str(t),complete_physical_operator_parity_norm_upper=list(map(str,k)),
        minimum_complete_head_width_improvement_factor_lower=str(min(ratios)),
        complete_head_diagonals_certified_positive=[i for i in range(8) if full[i,i][0]>0],
        certified_positive_native_subspace_features=[6,7],original_Weil_floor_on_certified_two_feature_subspace_lower='1/21',
        complete_nominal_archimedean_prime_pole_trial_covariance_evaluated=True,
        actual_complete_canonical_source_Gram_evaluated=False,projected_source_residual_evaluated=False,
        original_Weil_head_floor_certified=False,full_1250_native_projection_constructed=False,aperture_extended=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc43_native_prime_head.json',
        'rpb108_rc42_native_signed_pole_head.json','rpb108_rc47_correlated_native_transport.json',
        'rpb108_rc46_native_archimedean_head.json','rpb108_rc48_prime_source_covariance.json',
        'rpb108_rc49_prime_pole_covariance.json','rpb108_rc50_archimedean_source_covariance.json',
        'rpb108_rc51_archimedean_pole_covariance.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        cert=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,cert)==cert
        print('PASS: reflected logarithmic mixed integration on all 15 prime segments, all signed source components, actual transport and rational PSD envelope')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
