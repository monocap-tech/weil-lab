"""RC54: add the physical feature source before the canonical lift."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib,json,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import psd,mm,tr
from validate_rpb108_rc35_enriched_residuals import transformed,integrate
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import shift
from validate_rpb108_rc47_correlated_native_transport import matrix,entries,serialize,rows,root,intersect
from validate_rpb108_rc48_prime_source_covariance import polynomials,geometry,integrate_product
from validate_rpb108_rc49_prime_pole_covariance import exp_polynomial_integral,exact_exponential_integral,relative_upper
from validate_rpb108_rc50_archimedean_source_covariance import source_forms

def features(native,replay):
    C=matrix(native['chebyshev_to_legendre']);qt=[];qy=[]
    for j in range(8):
        p=[F(0)]*8;y=[F(0)]*8
        for n in range(8):
            for k,a in enumerate(legendre(n)):p[k]+=C[n][j]*a
            for k,a in enumerate(transformed(legendre(n))):y[k]+=C[n][j]*a
        qt.append(p);qy.append(y)
    if replay:
        cheb=[[F(1)],[F(0),F(1)]]
        for n in range(1,7):
            p=[F(0)]*(n+2)
            for k,a in enumerate(cheb[n]):p[k+1]+=2*a
            for k,a in enumerate(cheb[n-1]):p[k]-=a
            cheb.append(p)
        assert all(qt[j]==cheb[j]+[F(0)]*(8-len(cheb[j])) for j in range(8))
    return qt,qy

def pairings(native,prime,arch,joint,replay=False):
    forms,trials,mom,R,_=source_forms(native,arch);qt,qy=features(native,replay)
    archH=[[I(0)]*8 for _ in range(8)]
    for i in range(8):
        for j,(A,B,C) in enumerate(forms):
            if (i-j)%2:continue
            p=[I(a) for a in qy[i]]
            h=integrate(p,A,mom[0])+(2 if replay else 1)*integrate(p,B,mom[1])
            if not replay:h=h+integrate(p,C,mom[2])
            archH[i][j]=R*h
    terms,segments=geometry(prime);vp=polynomials(native)
    translated=[[shift([I(a) for a in p],term['offset']) for p in vp] for term in terms]
    primeH=[[I(0)]*8 for _ in range(8)]
    for ln,rn,left,right,active in segments:
        sources=[[sum((terms[k]['coefficient']*translated[k][j][m] for k in active),I(0)) for m in range(32)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                if (i-j)%2:continue
                p=[I(a) for a in qt[i]];s=sources[j]
                if replay:
                    length=right-left
                    powers=[I(1)]
                    for _ in range(31):powers.append(powers[-1]*length)
                    p=[a*powers[k] for k,a in enumerate(shift(p,left))]
                    s=[a*powers[k] for k,a in enumerate(shift(s,left))]
                    h=F(11,10)*length*sum((a*b/F(k+l+1) for k,a in enumerate(p) for l,b in enumerate(s)),I(0))
                else:h=integrate_product(p,s,left,right,F(11,10))
                primeH[i][j]=primeH[i][j]+h
        print('feature-prime source segment',ln,rn,'affine' if replay else 'direct',file=sys.stderr,flush=True)
    mv=[rational_interval(F(r['lower']),F(r['upper'])) for r in joint['trial_pole_moment_enclosures']]
    mq=[];b=F(11,20);tail=2*b**101/factorial(101)
    for p in qt:
        if replay:value=exact_exponential_integral([I(a) for a in p],I(-1),I(1))
        else:
            value=exp_polynomial_integral(p,I(-1),I(1))
            rad=I(F(11,5)*tail*sum(map(abs,p),F(0)));value=value+I(rad.h.copy_negate(),rad.h)
        mq.append(value)
    out={}
    for i in range(8):
        for j in range(8):
            out[i,j]=I(0) if (i-j)%2 else archH[i][j]+primeH[i][j]+2*(-1)**i*mq[i]*mv[j]
    return out

def run(paths,replay=False,certificate=None):
    raw=[Path(p).read_bytes() for p in paths]
    native,prime,arch,transport,joint,complete,projected,metric=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert [complete['input_sha256'][k] for k in [0,1,3,4,6]]==[hashes[k] for k in [0,1,3,2,4]]
    assert [projected['input_sha256'][k] for k in [0,2,3,5]]==[hashes[k] for k in [0,3,1,5]]
    assert prime['native_certificate_sha256']==hashes[0] and arch['native_certificate_sha256']==hashes[0]
    assert projected['input_sha256'][4]==native['metric_certificate_sha256']==hashes[7]
    values=pairings(native,prime,arch,joint,replay);saved={}
    prior=entries(certificate['nominal_physical_feature_remainder_source_pairing_enclosures']) if replay else None
    for key,value in values.items():
        if replay:
            a,b=prior[key];assert I(a).h<=value.l<=value.h<=I(b).l;saved[key]=(a,b)
        else:saved[key]=(F(0),F(0)) if (key[0]-key[1])%2 else outward(value,10**25)
    P=matrix(native['physical_native_Gram'])
    Q=entries(complete['nominal_complete_signed_physical_source_Gram_entry_enclosures'])
    full={};center=[[F(0)]*8 for _ in range(8)];half=F(0)
    for i in range(8):
        for j in range(i,8):
            key=i,j
            if (i-j)%2:full[key]=(F(0),F(0));continue
            value=I(P[i][j])+rational_interval(*Q[key])+rational_interval(*saved[i,j])+rational_interval(*saved[j,i])
            a,b=outward(value,10**25);full[key]=(a,b)
            center[i][j]=center[j][i]=(a+b)/2;half=max(half,(b-a)/2)
            assert b-a<F(1,10**18)
    assert psd([[P[i][j]-F(1,8)*(i==j) for j in range(8)] for i in range(8)])
    Uup=[[center[i][j]+64*half*P[i][j] for j in range(8)] for i in range(8)];assert psd(Uup)
    # R=i^*q exactly. Pi8 R=R, hence projecting the original source
    # equals projecting the bounded remainder source.
    error=matrix(projected['source_approximation_and_actual_physical_transfer_Gram_Loewner_upper'])
    rho=F(252,257);alpha=F(native['canonical_native_Gram_physical_lower_factor'])
    candidates=[]
    for t in [F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(1),F(2),F(4)]:
        A=[[rho*((1+t)*Uup[i][j]+(1+1/t)*error[i][j]) for j in range(8)] for i in range(8)]
        candidates.append((relative_upper(A,P),t,A))
    lam,t,A=min(candidates,key=lambda x:x[0]);bound=lam/alpha
    old=F(projected['whole_actual_canonical_orthogonal_source_residual_Gram_relative_native_metric_upper'])
    print('original source coarse lift bound',float(bound),'prior residual',float(old),file=sys.stderr,flush=True)
    V=matrix(native['native_trial_coefficients']);G=matrix(metric['metric_center'])
    Gtrial=mm(mm(tr(V),G),V);T=matrix(prime['physical_native_trial_Gram'])
    Em=F(metric['mass_metric_error_upper']);delta=F(complete['archimedean_source_approximation_operator_error_upper'])
    s=[root(full[i,i][1])+delta*root(T[i][i]) for i in range(8)]
    ep=list(map(F,transport['physical_Riesz_error_column_norm_upper']))
    ec=list(map(F,transport['canonical_Riesz_error_column_norm_upper']))
    k=list(map(F,complete['complete_physical_operator_parity_norm_upper']))
    H=entries(complete['nominal_complete_signed_remainder_head_entry_enclosures'])
    priorhead=entries(complete['actual_original_Weil_low_head_entry_enclosures']);head={}
    for i in range(8):
        for j in range(i,8):
            key=i,j
            if (i-j)%2:head[key]=(F(0),F(0));continue
            a,b=H[key];rad=(Em+delta)*root(T[i][i]*T[j][j])+ep[i]*s[j]+ep[j]*s[i]+k[i%2]*ep[i]*ep[j]
            lo=Gtrial[i][j]+a-rad-ec[i]*ec[j]
            hi=Gtrial[i][j]+b+rad+(ec[i]*ec[j] if i!=j else 0)
            head[key]=intersect((lo,hi),priorhead[key])
    print('new head diagonals',[(i,float(head[i,i][0]),float(head[i,i][1])) for i in range(8)],file=sys.stderr,flush=True)
    assert [i for i in range(8) if head[i,i][0]>0]==list(range(8))
    M=entries(transport['refined_actual_native_Gram_entry_enclosures'])
    assert head[6,7]==M[6,7]==(F(0),F(0))
    assert all(head[i,i][0]>M[i,i][1]/17 for i in [6,7])
    sub=[0,1,6,7];theta=F(1,200);robust=[]
    for i in sub:
        row=[];radius=F(0)
        for j in sub:
            key=tuple(sorted((i,j)));a,b=head[key];c,d=M[key]
            lo=a-theta*d;hi=b-theta*c
            row.append((lo+hi)/2);radius+=(hi-lo)/2
        row[sub.index(i)]-=radius;robust.append(row)
    assert psd(robust)
    # The global original-source lift does not beat RC53 here. Retain
    # its tighter orthogonal-residual envelope rather than replacing it.
    assert old<bound<F(4223,1000)
    residualA=matrix(projected['actual_canonical_orthogonal_source_residual_Gram_Loewner_upper'])
    return dict(milestone='RC54',status='PASS',input_sha256=hashes,native_features_certified=list(range(8)),
        source_and_residual_feature_scope='native source columns 0 through 7 only',
        nominal_physical_feature_remainder_source_pairing_enclosures=rows(saved),
        nominal_physical_original_source_Gram_entry_enclosures=rows(full),
        nominal_physical_original_source_Gram_Loewner_upper=serialize(Uup),
        actual_canonical_original_source_Gram_Loewner_upper=serialize(A),
        actual_canonical_orthogonal_source_residual_Gram_Loewner_upper=serialize(residualA),
        actual_canonical_original_source_Gram_relative_native_metric_upper=str(bound),
        whole_actual_canonical_orthogonal_source_residual_Gram_relative_native_metric_upper=str(old),
        previous_projected_source_residual_Gram_relative_native_metric_upper=str(old),
        actual_original_Weil_low_head_entry_enclosures=rows(head),
        identity_source_head_transfer_evaluated=True,
        complete_head_diagonals_certified_positive=[i for i in range(8) if head[i,i][0]>0],
        certified_positive_native_subspace_features=sub,
        original_Weil_floor_on_certified_four_feature_subspace_lower=str(theta),
        robust_four_feature_Weil_minus_floor_metric_Loewner_lower=serialize(robust),
        stronger_two_feature_subspace_features=[6,7],
        original_Weil_floor_on_certified_two_feature_subspace_lower='1/17',
        original_source_global_lift_improves_prior_residual_allowance=False,
        source_transport_Young_parameter=str(t),identity_source_lift_exact_native_Riesz_map=True,
        original_and_remainder_projected_source_residuals_equal=True,
        canonical_orthogonal_residual_upper_bound_certified=True,actual_original_canonical_source_Gram_evaluated=False,
        exact_actual_projection_coefficients_evaluated=False,final_1250_projected_residual_gate_met=False,
        original_Weil_head_floor_certified=False,full_1250_native_projection_constructed=False,aperture_extended=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc43_native_prime_head.json',
        'rpb108_rc46_native_archimedean_head.json','rpb108_rc47_correlated_native_transport.json',
        'rpb108_rc49_prime_pole_covariance.json','rpb108_rc52_complete_source_covariance.json',
        'rpb108_rc53_projected_source_residual.json','rpb108_rc38_thirty_two_metric.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        cert=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,cert)==cert
        print('PASS: reflected archimedean integration, affine prime segments, exact exponential primitives, identity-source cancellation and actual orthogonal residual PSD bound')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
