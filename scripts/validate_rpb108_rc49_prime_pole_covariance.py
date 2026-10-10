"""Prime-pole mixed physical source covariance on eight native trials."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib,json,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc31_trial_riesz import psd
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import shift,poly_value
from validate_rpb108_rc47_correlated_native_transport import root,matrix,entries,intersect,serialize,rows
from validate_rpb108_rc48_prime_source_covariance import polynomials,geometry

B=F(11,10);b=B/2;N=100

def exp_polynomial_integral(poly,left,right):
    # Taylor polynomial for exp(bt), with a separate uniform tail budget.
    coefficients=[I(0)]*(len(poly)+N)
    for k,a in enumerate(poly):
        for n in range(N+1):coefficients[k+n]=coefficients[k+n]+I(a*b**n/factorial(n))
    primitive=[I(0)]+[a/(k+1) for k,a in enumerate(coefficients)]
    return B*(poly_value(primitive,right)-poly_value(primitive,left))

def exact_exponential_integral(poly,left,right):
    # Independent closed primitive: q'+bq=p, integral p exp(bt)=q exp(bt).
    q=[I(0)]*len(poly)
    for k in range(len(poly)-1,-1,-1):
        q[k]=(poly[k]-(k+1)*q[k+1])/b if k+1<len(poly) else poly[k]/b
    return B*(poly_value(q,right)*(b*right).exp()-poly_value(q,left)*(b*left).exp())

def moments(native,prime,replay=False):
    polys=polynomials(native);V=matrix(native['native_trial_coefficients'])
    Aj=[sum((abs(V[n][j]) for n in range(32)),F(0)) for j in range(8)]
    tail=2*b**(N+1)/factorial(N+1)
    assert b/F(N+2)<F(1,2) and tail<F(1,10**180)
    m=[];z=[]
    if replay:
        m=[exact_exponential_integral([I(a) for a in poly],I(-1),I(1)) for poly in polys]
        terms,segments=geometry(prime)
        translated=[[shift([I(a) for a in poly],term['offset']) for poly in polys] for term in terms]
        z=[I(0)]*8
        for _,_,left,right,active in segments:
            for j in range(8):
                source=[sum((terms[k]['coefficient']*translated[k][j][n] for k in active),I(0)) for n in range(32)]
                z[j]=z[j]+exact_exponential_integral(source,left,right)
    else:
        for j,poly in enumerate(polys):
            raw=exp_polynomial_integral(poly,I(-1),I(1));rad=I(2*B*tail*Aj[j])
            m.append(raw+I(rad.h.copy_negate(),rad.h))
        z=[I(0)]*8;errors=[I(0)]*8
        for row in prime['active_prime_powers']:
            n,p=row['n'],row['base_prime'];ell=I(n).log();c=I(p).log()/I(n).sqrt()
            em=(-ell/2).exp();ep=(ell/2).exp()
            for j,poly in enumerate(polys):
                # Substitute y=x+/-ell before integrating the untranslated trial.
                plus=exp_polynomial_integral(poly,-1+ell/B,I(1))
                minus=exp_polynomial_integral(poly,I(-1),1-ell/B)
                z[j]=z[j]-c*(em*plus+ep*minus)
                errors[j]=errors[j]+c*(em+ep)*I(2*B*tail*Aj[j])
        z=[value+I(rad.h.copy_negate(),rad.h) for value,rad in zip(z,errors)]
    return m,z,tail

def relative_upper(A,P):
    def accepted(t):return psd([[t*P[i][j]-A[i][j] for j in range(8)] for i in range(8)])
    low=F(0);high=F(1)
    while not accepted(high):high*=2
    for _ in range(32):
        mid=(low+high)/2
        if accepted(mid):high=mid
        else:low=mid
    assert accepted(high);return high

def run(paths):
    raw=[Path(p).read_bytes() for p in paths];native,prime,pole,transport,pcov=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert native['native_features_certified']==list(range(8))
    assert prime['native_certificate_sha256']==pole['source_certificate_sha256']==hashes[0]
    assert transport['input_sha256'][2]==hashes[0] and transport['input_sha256'][3]==hashes[2] and transport['input_sha256'][4]==hashes[1]
    assert pcov['input_sha256']==[hashes[0],hashes[1],hashes[3]]
    m,z,tail=moments(native,prime)
    saved_m=[];saved_z=[]
    for i in range(8):
        ml,mh=outward(m[i],10**35);zl,zh=outward(z[i],10**35)
        prior=pole['actual_native_pole_moment_enclosures'][i]
        assert F(prior['trial_m_plus_lower'])<=ml<=mh<=F(prior['trial_m_plus_upper'])
        saved_m.append((ml,mh));saved_z.append((zl,zh))
    sinh=(I(B).exp()-I(-B).exp())/2
    norm=[I(B)+sinh,sinh-I(B)]
    polek=[2*F(pole['cosh_physical_norm_squared_upper']),2*F(pole['sinh_physical_norm_squared_upper'])]
    for k in range(2):assert norm[k].h<=I(polek[k]/2).l
    Uprime=entries(pcov['trial_physical_prime_source_Gram_entry_enclosures'])
    Hprime=entries(pcov['trial_prime_head_entry_enclosures'])
    cross={};Upole={};Ujoint={};Hjoint={};half=F(0);center=[[F(0)]*8 for _ in range(8)]
    for i in range(8):
        for j in range(i,8):
            key=(i,j)
            if (i-j)%2:cross[key]=Upole[key]=Ujoint[key]=Hjoint[key]=(F(0),F(0));continue
            sign=(-1)**i
            mi=rational_interval(*saved_m[i]);mj=rational_interval(*saved_m[j])
            zi=rational_interval(*saved_z[i]);zj=rational_interval(*saved_z[j])
            # Symmetrized cross covariance, not a sum of component squares.
            x=2*sign*(mj*zi+mi*zj);o=4*mi*mj*norm[i%2]
            cross[key]=outward(x,10**25);Upole[key]=outward(o,10**25)
            joint=rational_interval(*Uprime[key])+x+o
            lo,hi=outward(joint,10**25);Ujoint[key]=(lo,hi)
            Hjoint[key]=outward(rational_interval(*Hprime[key])+2*sign*mi*mj,10**25)
            assert hi-lo<F(1,10**22)
            center[i][j]=center[j][i]=(lo+hi)/2;half=max(half,(hi-lo)/2)
    P=matrix(native['physical_native_Gram']);assert psd([[P[i][j]-F(1,8)*(i==j) for j in range(8)] for i in range(8)])
    Uup=[[center[i][j]+64*half*P[i][j] for j in range(8)] for i in range(8)];assert psd(Uup)
    s=[root(Ujoint[(i,i)][1]) for i in range(8)]
    ep=list(map(F,transport['physical_Riesz_error_column_norm_upper']))
    kp=F(prime['full_paired_prime_physical_operator_norm_upper']);k=[kp+polek[0],kp+polek[1]]
    actualjoint={};actualsource={};full={}
    oldprime=entries(pcov['actual_native_prime_head_entry_enclosures'])
    oldpole=entries(transport['refined_actual_signed_pole_head_entry_enclosures'])
    arch=entries(transport['refined_actual_archimedean_head_entry_enclosures'])
    oldfull=entries(pcov['actual_original_Weil_low_head_entry_enclosures']);ratios=[]
    for i in range(8):
        for j in range(i,8):
            key=(i,j)
            if (i-j)%2:actualjoint[key]=actualsource[key]=full[key]=(F(0),F(0));continue
            ki=k[i%2];linear=ep[i]*s[j]+ep[j]*s[i]
            rad=linear+ki*ep[i]*ep[j]
            a,bh=Hjoint[key]
            prior=(oldprime[key][0]+oldpole[key][0],oldprime[key][1]+oldpole[key][1])
            actualjoint[key]=intersect((a-rad,bh+rad),prior)
            a,bh=Ujoint[key];sr=ki*linear+ki*ki*ep[i]*ep[j]
            actualsource[key]=(max(F(0),a-sr) if i==j else a-sr,bh+sr)
            a,bh=actualjoint[key]
            full[key]=intersect((a+arch[key][0],bh+arch[key][1]),oldfull[key])
            ratios.append((prior[1]-prior[0])/(actualjoint[key][1]-actualjoint[key][0]))
    Berr=matrix(transport['actual_physical_Riesz_error_Gram_Loewner_upper']);rho=F(252,257)
    error=[[k[i%2]*k[j%2]*Berr[i][j] for j in range(8)] for i in range(8)]
    assert all(Berr[i][j]==0 for i in range(8) for j in range(8) if (i-j)%2)
    candidates=[]
    for t in [F(1,32),F(1,16),F(1,8),F(1,4),F(1,2),F(1)]:
        A=[[rho*((1+t)*Uup[i][j]+(1+1/t)*error[i][j]) for j in range(8)] for i in range(8)]
        candidates.append((relative_upper(A,P),t,A))
    lam,t,A=min(candidates,key=lambda x:x[0]);alpha=F(native['canonical_native_Gram_physical_lower_factor'])
    bound=lam/alpha
    separate=(root(F(pcov['whole_actual_prime_source_Gram_relative_native_metric_upper']))+
              F(pole['canonical_signed_pole_operator_norm_upper']))**2
    assert bound<separate and bound<F(667,50)
    assert separate/bound>F(437,100) and min(ratios)>F(21,20)
    assert all(hi<0 for (i,j),(lo,hi) in cross.items() if i==j)
    return dict(milestone='RC49',status='PASS',input_sha256=hashes,native_features_certified=list(range(8)),
        source_bound_feature_scope='native features 0 through 7 only',
        exponential_degree=N,exponential_uniform_remainder_upper=str(tail),
        trial_pole_moment_enclosures=[dict(j=i,lower=str(a),upper=str(bh)) for i,(a,bh) in enumerate(saved_m)],
        trial_prime_source_exponential_moment_enclosures=[dict(j=i,lower=str(a),upper=str(bh)) for i,(a,bh) in enumerate(saved_z)],
        trial_symmetrized_prime_pole_source_cross_Gram_entry_enclosures=rows(cross),
        trial_physical_pole_source_Gram_entry_enclosures=rows(Upole),
        trial_physical_joint_prime_pole_source_Gram_entry_enclosures=rows(Ujoint),
        trial_physical_joint_prime_pole_source_Gram_Loewner_upper=serialize(Uup),
        trial_joint_prime_pole_source_column_norm_upper=list(map(str,s)),
        actual_physical_joint_prime_pole_source_Gram_entry_enclosures=rows(actualsource),
        actual_joint_prime_pole_head_entry_enclosures=rows(actualjoint),
        actual_original_Weil_low_head_entry_enclosures=rows(full),
        actual_canonical_joint_prime_pole_source_Gram_Loewner_upper=serialize(A),
        actual_canonical_joint_prime_pole_source_Gram_relative_physical_native_Gram_upper=str(lam),
        whole_actual_joint_prime_pole_source_Gram_relative_native_metric_upper=str(bound),
        separate_component_triangle_source_Gram_relative_native_metric_upper=str(separate),
        source_transport_Young_parameter=str(t),
        joint_prime_pole_physical_operator_parity_norm_upper=list(map(str,k)),
        minimum_joint_head_width_improvement_factor_lower=str(min(ratios)),
        all_trial_prime_pole_cross_diagonals_strictly_negative=True,
        all_complete_head_diagonal_intervals_contain_zero=all(a<0<bh for (i,j),(a,bh) in full.items() if i==j),
        all_trial_prime_pole_source_correlations_evaluated=True,
        actual_canonical_joint_prime_pole_source_Gram_evaluated=False,
        complete_archimedean_prime_pole_covariance_evaluated=False,
        original_Weil_head_floor_certified=False,full_1250_native_projection_constructed=False,aperture_extended=False)

def replay(path,paths):
    cert=json.loads(Path(path).read_text());native,prime,pole,transport,pcov=[json.loads(Path(p).read_text()) for p in paths]
    assert cert['input_sha256']==[hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in paths]
    m,z,_=moments(native,prime,replay=True)
    for name,values in [('trial_pole_moment_enclosures',m),('trial_prime_source_exponential_moment_enclosures',z)]:
        for row,value in zip(cert[name],values):
            assert I(F(row['lower'])).h<=value.l<=value.h<=I(F(row['upper'])).l
    assert run(paths)==cert
    print('PASS: independent exponential primitives on all translated support segments, pole moments, signed mixed covariance, actual joint transport and whole-map PSD bounds')

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc43_native_prime_head.json',
        'rpb108_rc42_native_signed_pole_head.json','rpb108_rc47_correlated_native_transport.json',
        'rpb108_rc48_prime_source_covariance.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':replay(sys.argv[2],sys.argv[3:] or defaults)
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
