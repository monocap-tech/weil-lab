"""RC58: actual projected-source lower witnesses in canonical complements.

Legendre_n is orthogonal, in the canonical pairing, to native Riesz
representatives of all physical polynomials of degree < n. A source pairing
therefore lower-bounds every nested projected residual with 8<=N<=n.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib,json,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc31_trial_riesz import mm,tr
from validate_rpb108_rc35_enriched_residuals import transformed,integrate
from validate_rpb108_rc42_native_signed_pole_head import outward,rational_interval
from validate_rpb108_rc43_native_prime_head import shift
from validate_rpb108_rc47_correlated_native_transport import matrix,root
from validate_rpb108_rc48_prime_source_covariance import polynomials,geometry,integrate_product
from validate_rpb108_rc49_prime_pole_covariance import exact_exponential_integral,exp_polynomial_integral,N as EXP_N,b as EXP_B
from validate_rpb108_rc50_archimedean_source_covariance import source_forms
from validate_rpb108_rc55_weak_head_schur import quad
from validate_rpb108_rc56_precision_attached_head import DC0

def prime_pair(z,translated,terms,segments,B,replay):
    total=I(0)
    for _,_,left,right,active in segments:
        source=[sum((terms[k]['coefficient']*translated[k][j] for k in active),I(0)) for j in range(32)]
        if replay:
            # Independent integration after x/B=left+(right-left)u.
            length=right-left;zp=shift(z,left);fp=shift(source,left)
            za=[];fa=[];power=I(1)
            for x in zp:za.append(x*power);power=power*length
            power=I(1)
            for x in fp:fa.append(x*power);power=power*length
            total=total+B*length*sum((x*y/F(i+j+1) for i,x in enumerate(za) for j,y in enumerate(fa)),I(0))
        else:total=total+integrate_product(z,source,left,right,B)
    return total

def exp_moment(poly,sup,replay):
    if replay:return exact_exponential_integral([I(x) for x in poly],I(-1),I(1))
    value=exp_polynomial_integral(poly,I(-1),I(1))
    tail=2*EXP_B**(EXP_N+1)/factorial(EXP_N+1)
    radius=I(F(11,5)*tail*sup).h
    return value+I(radius.copy_negate(),radius)

def run(paths,replay=False,saved=None):
    raw=[Path(p).read_bytes() for p in paths]
    native,metric,prime,arch,complete,precision,floor=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert [precision['input_sha256'][k] for k in [0,1,4,5,6]]==hashes[:5]
    assert [floor['input_sha256'][k] for k in [0,1,3,4,6]]==[hashes[k] for k in [0,1,2,4,5]]
    assert floor['full_low_eight_original_Weil_head_floor_certified']
    forms,_,mom,R,_=source_forms(native,arch)
    polys=polynomials(native);V=matrix(native['native_trial_coefficients'])
    terms,segments=geometry(prime);P=matrix(native['physical_native_Gram'])
    T=matrix(prime['physical_native_trial_Gram']);G=matrix(metric['metric_center'])
    Mup=matrix(floor['actual_canonical_native_Gram_Loewner_upper'])
    rho=F(252,257);deltaS=F(precision['source_error_from_old_nominal_forms_upper'])
    deltaG=2*(abs(F(precision['constant_center_shift']))+F(precision['constant_radius']))+F(metric['mass_metric_error_upper'])-2*DC0
    gamma=F(floor['conditional_1250_gate']['required_actual_canonical_source_residual_relative_Gram_upper'])
    detectors=[];source_errors={};input_uppers={}
    for parity,direction in enumerate(precision['weak_direction_actual_quadratic_enclosures']):
        v=list(map(F,direction['coefficients']));pn=quad(v,P);tt=quad(v,T)
        e=F(direction['actual_physical_Riesz_error_squared_upper'])
        assert pn==F(direction['physical_native_squared_norm'])>0
        k=F(complete['complete_physical_operator_parity_norm_upper'][parity])
        source_error=k*root(e)+deltaS*root(tt)
        source_errors['even' if parity==0 else 'odd']=source_error
        input_up=min(rho*pn,quad(v,Mup));assert input_up>0
        input_uppers['even' if parity==0 else 'odd']=input_up
        combo=[[sum((I(v[j])*forms[j][part][a] for j in range(8)),I(0))
            for a in range(len(forms[0][part]))] for part in range(3)]
        poly=[sum((v[j]*polys[j][a] for j in range(8)),F(0)) for a in range(32)]
        translated=[shift([I(x) for x in poly],term['offset']) for term in terms]
        sup=sum((abs(sum((V[a][j]*v[j] for j in range(8)),F(0))) for a in range(32)),F(0))
        trial_m=exp_moment(poly,sup,replay)
        for n in range(8+parity,32,2):
            zp=[I(x) for x in legendre(n)];zy=[I(x) for x in transformed(legendre(n))]
            A,BB,C=combo
            if replay:pa=R*(integrate(zy,A,mom[0])+2*integrate(zy,BB,mom[1]))
            else:pa=R*(integrate(zy,A,mom[0])+integrate(zy,BB,mom[1])+integrate(zy,C,mom[2]))
            pp=prime_pair(zp,translated,terms,segments,R/2,replay)
            pole=2*((-1)**parity)*trial_m*exp_moment(legendre(n),F(1),replay)
            value=pa+pp+pole
            if replay:
                row=saved['complementary_source_detectors'][len(detectors)]
                a,b=map(F,row['nominal_trial_source_pairing_enclosure'])
                assert I(a).h<=value.l<=value.h<=I(b).l
            else:a,b=outward(value,10**30)
            mass=R/F(2*n+1);zup=G[n][n]+deltaG*mass;assert zup>mass>0
            # Physical pairing transport: actual K iR-F_nom is at most
            # k sqrt(e_phys)+deltaS sqrt(t). No canonical/physical conflation.
            rad=root(mass)*source_error;lo,hi=a-rad,b+rad
            distance=min(abs(lo),abs(hi)) if lo*hi>0 else F(0)
            lower=distance**2/(zup*input_up)
            # Exact physical moment orthogonality against every polynomial
            # of degree <n, hence canonical orthogonality to Riesz features.
            for degree in range(n):
                pairing=sum((x*R/2*F(2,degree+j+1) for j,x in enumerate(legendre(n)) if (degree+j)%2==0),F(0))
                assert pairing==0
            if replay:
                assert root(mass)**2>=mass and root(e)**2>=e and root(tt)**2>=tt
                assert lower*zup*input_up==distance**2
            detectors.append(dict(source_parity='even' if parity==0 else 'odd',source_coefficients=list(map(str,v)),
                complementary_Legendre_test_degree=n,physical_test_squared_norm=str(mass),
                canonical_test_squared_norm_upper=str(zup),source_physical_native_squared_norm=str(pn),
                source_input_canonical_squared_norm_upper=str(input_up),
                nominal_trial_source_pairing_enclosure=[str(a),str(b)],actual_source_pairing_enclosure=[str(lo),str(hi)],
                actual_source_pairing_transfer_allowance=str(rad),
                projected_source_residual_relative_canonical_native_Gram_lower=str(lower),
                applies_to_nested_native_head_feature_counts=list(range(8,n+1)),
                revised_source_gate_ruled_out_for_these_heads=lower>gamma,
                ratio_to_revised_source_gate=str(lower/gamma)))
            print('source detector',parity,n,'lower',float(lower),'gate ratio',float(lower/gamma),file=sys.stderr,flush=True)
    combined=[]
    for parity in ['even','odd']:
        component=[x for x in detectors if x['source_parity']==parity]
        for first in component:
            degree=first['complementary_Legendre_test_degree']
            selected=[x for x in component if x['complementary_Legendre_test_degree']>=degree]
            # Explicit exact test, selected using the nominal physical
            # mass geometry only. No numerical eigenvector is certified.
            weights=[sum(map(F,x['nominal_trial_source_pairing_enclosure']))/2/F(x['physical_test_squared_norm']) for x in selected]
            support=[x['complementary_Legendre_test_degree'] for x in selected]
            mass=sum((w*w*F(x['physical_test_squared_norm']) for w,x in zip(weights,selected)),F(0))
            zup=sum((weights[i]*G[n][m]*weights[j] for i,n in enumerate(support)
                for j,m in enumerate(support)),F(0))+deltaG*mass
            a=b=F(0)
            for w,x in zip(weights,selected):
                ends=[w*F(y) for y in x['nominal_trial_source_pairing_enclosure']]
                a+=min(ends);b+=max(ends)
            rad=root(mass)*source_errors[parity];lo,hi=a-rad,b+rad
            distance=min(abs(lo),abs(hi)) if lo*hi>0 else F(0)
            input_up=input_uppers[parity]
            lower=distance**2/(zup*input_up)
            if replay:
                assert root(mass)**2>=mass and lower*zup*input_up==distance**2
                assert min(support)>=degree and all(n%2==support[0]%2 for n in support)
            combined.append(dict(source_parity=parity,minimum_test_degree=degree,
                Legendre_test_degrees=support,exact_Legendre_test_coefficients=list(map(str,weights)),
                physical_test_squared_norm=str(mass),canonical_test_squared_norm_upper=str(zup),
                nominal_trial_source_pairing_enclosure=[str(a),str(b)],actual_source_pairing_enclosure=[str(lo),str(hi)],
                actual_source_pairing_transfer_allowance=str(rad),
                source_input_canonical_squared_norm_upper=str(input_up),
                projected_source_residual_relative_canonical_native_Gram_lower=str(lower),
                applies_to_nested_native_head_feature_counts=list(range(8,degree+1)),
                revised_source_gate_ruled_out_for_these_heads=lower>gamma,ratio_to_revised_source_gate=str(lower/gamma)))
            print('combined source detector',parity,degree,'lower',float(lower),'gate ratio',float(lower/gamma),file=sys.stderr,flush=True)
    accepted=[x for x in combined if x['revised_source_gate_ruled_out_for_these_heads']]
    assert accepted
    largest=max(x['minimum_test_degree'] for x in accepted)
    strongest=max(accepted,key=lambda x:F(x['projected_source_residual_relative_canonical_native_Gram_lower']))
    return dict(milestone='RC58',status='PASS',input_sha256=hashes,cap='11/10',
        source_feature_scope='two exact low-eight native source combinations from RC56',
        residual_lower_bound_scope='one exact source input direction per detector, not a Loewner lower bound',
        projection_family='actual canonical orthogonal projections onto consecutive native Riesz features 0 through N-1',
        detector_degrees_evaluated=list(range(8,32)),complementary_source_detectors=detectors,
        combined_complementary_source_detectors=combined,
        required_projected_source_relative_Gram_upper=str(gamma),
        largest_consecutive_native_head_count_ruled_out_for_revised_source_gate=largest,
        necessary_consecutive_native_head_count_for_revised_source_gate_lower=largest+1,
        strongest_detector_minimum_degree=strongest['minimum_test_degree'],
        strongest_actual_projected_source_relative_Gram_lower=strongest['projected_source_residual_relative_canonical_native_Gram_lower'],
        projection_lower_bound_follows_from_actual_test_pairing_and_canonical_Cauchy_Schwarz=True,
        actual_1250_source_gate_ruled_out=False,full_1250_native_projection_constructed=False,
        retained_actual_low_eight_Weil_floor=floor['original_Weil_uniform_low_eight_canonical_floor_lower'],
        whole_aperture_positivity_extended=False,RH=False,F4=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/n for n in ['rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc38_thirty_two_metric.json',
        'rpb108_rc43_native_prime_head.json','rpb108_rc46_native_archimedean_head.json',
        'rpb108_rc52_complete_source_covariance.json','rpb108_rc56_precision_attached_head.json',
        'rpb108_rc57_uniform_low_head_floor.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
        print('PASS: reflected archimedean moments, affine prime segments, closed exponential pole moments, exact complement orthogonality and actual projected-source lower bounds')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
