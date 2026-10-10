"""RC50: endpoint-cancelled bounded archimedean remainder source Gram."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import psd
from validate_rpb108_rc35_enriched_residuals import transformed,reflect,polyadd,scalar,integrate
from validate_rpb108_rc38_thirty_two_residuals import build_forms,pairing
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc46_native_archimedean_head import regular_coefficients
from validate_rpb108_rc47_correlated_native_transport import root,upper,matrix,entries,intersect,serialize,rows
from validate_rpb108_rc49_prime_pole_covariance import relative_upper
from math import factorial

def source_forms(native,arch):
    V=matrix(native['native_trial_coefficients']);dforms,mom,R,metric_delta=build_forms(V)
    ntrial=32;N=192;H=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(260)]
    cmid=F(-3203794213-3203306050,2*10**9)
    reg=list(map(F,arch['regular_kernel_coefficients']))
    assert reg==regular_coefficients(N)
    fac=[factorial(k) for k in range(260)]
    forms=[];trials=[]
    for j in range(8):
        v=[F(0)]*32;tv=[F(0)]*32
        for n in range(32):
            for k,a in enumerate(transformed(legendre(n))):
                v[k]+=V[n][j]*a;tv[k]+=H[n]*V[n][j]*a
        target=transformed(legendre(j))
        # Remove q_j-T0 V-c_mid V+(-W V) from the inherited residual.
        # The remaining three coefficients are -K_metric V.
        A,BB,C=dforms[j]
        correction=[I(tv[k]+cmid*v[k]-(target[k] if k<len(target) else 0)) for k in range(32)]
        A=polyadd(A,correction)
        BB=polyadd(BB,[I(x/2) for x in v],-1)
        C=polyadd(C,[I(x/2) for x in v],-1)
        left=[F(0)]*225
        for p,rp in enumerate(reg):
            for m,vm in enumerate(v):
                left[p+m+1]+=R*rp*R**p*vm*F(fac[p]*fac[m],fac[p+m+1])
        regular=polyadd([I(x) for x in left],reflect([I(x) for x in left]),(-1)**j)
        A=polyadd(A,regular,-1)
        forms.append((A,BB,C));trials.append([I(x) for x in v])
        print('bounded archimedean source form',j,'constructed',file=sys.stderr,flush=True)
    return forms,trials,mom,R,metric_delta

def reflected_pairing(f,g,mom,R):
    # Same-parity reflection reduces nine logarithmic products to five.
    A,B,C=f;X,Y,Z=g
    return R*(integrate(A,X,mom[0])+2*integrate(A,Y,mom[1])+2*integrate(B,X,mom[1])+
              2*integrate(B,Y,mom[3])+2*integrate(B,Z,mom[5]))

def run(paths,replay=False,certificate=None):
    raw=[Path(p).read_bytes() for p in paths];metric,residual,native,transport,arch,joint=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert residual['metric_certificate_sha256']==native['metric_certificate_sha256']==hashes[0]
    assert [transport['input_sha256'][k] for k in [0,1,2,5]]==[hashes[k] for k in [0,1,2,4]]
    assert joint['input_sha256'][0]==hashes[2] and joint['input_sha256'][3]==hashes[3]
    forms,trials,mom,R,metric_delta=source_forms(native,arch)
    assert metric_delta==F(residual['source_operator_error_upper'])
    dc=F(488163,2*10**9);eps=metric_delta-2*dc;assert eps>0
    # The c_R uncertainty in the remaining regular metric kernel is
    # dc times the restricted Fourier projection onto [-e,e], norm <=dc.
    delta=upper(dc+eps+R*F(arch['regular_kernel_uniform_error_upper']),10**30)
    assert delta<F(49,200000)
    nominal={};trialhead={};center=[[F(0)]*8 for _ in range(8)];half=F(0)
    saved=entries(certificate['nominal_physical_archimedean_source_Gram_entry_enclosures']) if replay else None
    savedH=entries(certificate['nominal_trial_archimedean_remainder_head_entry_enclosures']) if replay else None
    for i in range(8):
        for j in range(i,8):
            key=(i,j)
            if (i-j)%2:nominal[key]=trialhead[key]=(F(0),F(0));continue
            q=reflected_pairing(forms[i],forms[j],mom,R) if replay else pairing(forms[i],forms[j],mom,R)
            A,B,C=forms[j]
            h=R*(integrate(trials[i],A,mom[0])+2*integrate(trials[i],B,mom[1])) if replay else R*(
                integrate(trials[i],A,mom[0])+integrate(trials[i],B,mom[1])+integrate(trials[i],C,mom[2]))
            if replay:
                a,bh=saved[key];assert I(a).h<=q.l<=q.h<=I(bh).l
                a,bh=savedH[key];assert I(a).h<=h.l<=h.h<=I(bh).l
                nominal[key]=saved[key];trialhead[key]=savedH[key]
            else:
                nominal[key]=outward(q,10**20);trialhead[key]=outward(h,10**25)
            lo,hi=nominal[key];assert hi-lo<F(1,10**18)
            center[i][j]=center[j][i]=(lo+hi)/2;half=max(half,(hi-lo)/2)
            print('archimedean source Gram entry',i,j,'replayed' if replay else 'enclosed',file=sys.stderr,flush=True)
    P=matrix(native['physical_native_Gram']);V=matrix(native['native_trial_coefficients'])
    mass=list(map(F,metric['physical_mass']))
    from validate_rpb108_rc31_trial_riesz import mm,tr
    T=mm(mm(tr(V),[[mass[i]*(i==j) for j in range(32)] for i in range(32)]),V)
    assert psd([[P[i][j]-F(1,8)*(i==j) for j in range(8)] for i in range(8)])
    Qup=[[center[i][j]+64*half*P[i][j] for j in range(8)] for i in range(8)];assert psd(Qup)
    snom=[root(nominal[(i,i)][1]) for i in range(8)];v=[root(T[i][i]) for i in range(8)]
    strial=[snom[i]+delta*v[i] for i in range(8)]
    ep=list(map(F,transport['physical_Riesz_error_column_norm_upper']))
    cost=[delta*v[i]+8*ep[i] for i in range(8)]
    oldrem=entries(arch['archimedean_trial_remainder_head_entry_enclosures'])
    oldarch=entries(transport['refined_actual_archimedean_head_entry_enclosures'])
    oldfull=entries(joint['actual_original_Weil_low_head_entry_enclosures'])
    pp=entries(joint['actual_joint_prime_pole_head_entry_enclosures'])
    M=entries(transport['refined_actual_native_Gram_entry_enclosures'])
    trialrem={};actualarch={};actualsource={};full={};ratios=[]
    for i in range(8):
        for j in range(i,8):
            key=(i,j)
            if (i-j)%2:trialrem[key]=actualarch[key]=actualsource[key]=full[key]=(F(0),F(0));continue
            a,bh=trialhead[key];rad=delta*root(T[i][i]*T[j][j])
            trialrem[key]=intersect((a-rad,bh+rad),oldrem[key])
            rad=ep[i]*strial[j]+ep[j]*strial[i]+8*ep[i]*ep[j]
            a,bh=trialrem[key]
            actualarch[key]=intersect((M[key][0]+a-rad,M[key][1]+bh+rad),oldarch[key])
            a,bh=nominal[key];sr=cost[i]*snom[j]+cost[j]*snom[i]+cost[i]*cost[j]
            actualsource[key]=(max(F(0),a-sr) if i==j else a-sr,bh+sr)
            a,bh=actualarch[key]
            full[key]=intersect((a+pp[key][0],bh+pp[key][1]),oldfull[key])
            ratios.append((oldarch[key][1]-oldarch[key][0])/(actualarch[key][1]-actualarch[key][0]))
    Berr=matrix(transport['actual_physical_Riesz_error_Gram_Loewner_upper']);rho=F(252,257)
    error=[[F(33,32)*64*Berr[i][j]+33*delta*delta*T[i][j] for j in range(8)] for i in range(8)]
    candidates=[]
    for t in [F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(1)]:
        A=[[rho*((1+t)*Qup[i][j]+(1+1/t)*error[i][j]) for j in range(8)] for i in range(8)]
        candidates.append((relative_upper(A,P),t,A))
    lam,t,A=min(candidates,key=lambda x:x[0]);alpha=F(native['canonical_native_Gram_physical_lower_factor'])
    bound=lam/alpha;old=F(arch['whole_actual_archimedean_remainder_source_Gram_relative_native_metric_upper'])
    assert bound<old and bound<F(12529,500) and min(ratios)>F(209,100)
    assert full[(6,7)]==M[(6,7)]==(F(0),F(0))
    assert all(full[(i,i)][0]>M[(i,i)][1]/25 for i in [6,7])
    return dict(milestone='RC50',status='PASS',input_sha256=hashes,native_features_certified=list(range(8)),
        source_bound_feature_scope='native features 0 through 7 only',
        endpoint_logarithms_cancelled_in_bounded_remainder=True,
        archimedean_remainder_source_approximation_operator_error_upper=str(delta),
        nominal_physical_archimedean_source_Gram_entry_enclosures=rows(nominal),
        nominal_trial_archimedean_remainder_head_entry_enclosures=rows(trialhead),
        nominal_physical_archimedean_source_Gram_Loewner_upper=serialize(Qup),
        true_trial_archimedean_source_column_norm_upper=list(map(str,strial)),
        actual_physical_archimedean_source_Gram_entry_enclosures=rows(actualsource),
        actual_native_archimedean_head_entry_enclosures=rows(actualarch),
        actual_original_Weil_low_head_entry_enclosures=rows(full),
        actual_canonical_archimedean_source_Gram_Loewner_upper=serialize(A),
        whole_actual_archimedean_remainder_source_Gram_relative_native_metric_upper=str(bound),
        previous_whole_actual_archimedean_remainder_source_Gram_relative_native_metric_upper=str(old),
        source_transport_Young_parameter=str(t),
        minimum_archimedean_head_width_improvement_factor_lower=str(min(ratios)),
        complete_head_diagonals_certified_positive=[i for (i,j),(a,bh) in full.items() if i==j and a>0],
        certified_positive_native_subspace_features=[6,7],
        original_Weil_floor_on_certified_two_feature_subspace_lower='1/25',
        original_Weil_head_floor_certified=False,
        complete_archimedean_prime_pole_covariance_evaluated=False,
        actual_canonical_archimedean_source_Gram_evaluated=False,
        full_1250_native_projection_constructed=False,aperture_extended=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc38_thirty_two_metric.json','rpb108_rc38_thirty_two_residuals.json',
        'rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc47_correlated_native_transport.json',
        'rpb108_rc46_native_archimedean_head.json','rpb108_rc49_prime_pole_covariance.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        cert=json.loads(Path(sys.argv[2]).read_text());result=run(sys.argv[3:] or defaults,True,cert)
        assert result==cert
        print('PASS: reflected logarithmic moment replay, source/head attachment, paid approximation error, all actual transports and whole-map PSD bounds')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
