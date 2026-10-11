"""RC69: actual rank-22 complementary source lower witnesses on enriched trials.

Exact supported Legendre tests are canonically orthogonal to native Riesz
features of lower degree. Replay uses reflected and affine integrations.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from validate_rpb108_rc30_interval_metric import I
from validate_rpb108_rc29_atom_reduction import legendre
from validate_rpb108_rc35_enriched_residuals import transformed,integrate
from validate_rpb108_rc42_native_signed_pole_head import outward
from validate_rpb108_rc43_native_prime_head import shift
from validate_rpb108_rc47_correlated_native_transport import matrix,root
from validate_rpb108_rc48_prime_source_covariance import geometry,integrate_product
from validate_rpb108_rc49_prime_pole_covariance import exact_exponential_integral,exp_polynomial_integral,N as EXP_N,b as EXP_B
from validate_rpb108_rc68_enriched_original_source_covariance import source_forms
from math import factorial
R=F(11,5)
def quad(v,A):return sum((v[i]*v[j]*A[i][j] for i in range(len(v)) for j in range(len(v))),F(0))
def prime_pair(z,translated,terms,segments,B,replay):
    total=I(0)
    for _,_,left,right,active in segments:
        source=[sum((terms[k]['coefficient']*translated[k][j] for k in active),I(0)) for j in range(64)]
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
 enriched,native,precision,prime,arch,source,transport,floor,weak=[json.loads(x) for x in raw]
 hashes=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [source['input_sha256'][k] for k in [0,1,2,3,5,6]]==[hashes[k] for k in [0,1,2,3,4,6]]
 assert floor['input_sha256'][6]==hashes[2]
 assert weak['input_sha256'][4]==hashes[7]
 forms,mom,trials,targets=source_forms(enriched,native,arch,precision)
 V=matrix(enriched['enriched_native_trial_coefficients']);G=matrix(enriched['recentered_nominal_metric_center'])
 mass=list(map(F,enriched['physical_mass']));P=matrix(native['physical_native_Gram'])
 T=[[sum((mass[a]*V[a][i]*V[a][j] for a in range(64)),F(0)) for j in range(22)] for i in range(22)]
 Ep=matrix(enriched['enriched_actual_physical_Riesz_error_Gram_Loewner_upper'])
 M8up=matrix(floor['actual_canonical_native_Gram_Loewner_upper']);rho=F(252,257)
 delta=F(source['actual_source_approximation_operator_error_upper']);deltaG=F(enriched['actual_recentered_metric_mass_error_upper'])
 gamma=F(weak['scalar_Schur_source_budget_strict_ceiling_using_inherited_complement_floor']);oldgamma=F(weak['old_conditional_squared_source_budget'])
 k=list(map(F,transport['complete_physical_operator_parity_norm_upper']));terms,segments=geometry(prime)
 detectors=[];combined=[];errors={};inputup={}
 for parity,direction in enumerate(precision['weak_direction_actual_quadratic_enclosures']):
  v=list(map(F,direction['coefficients']))+[F(0)]*14;assert len(v)==22
  pn=quad(v,P);tt=quad(v,T);ee=quad(v,Ep);assert min(pn,tt,ee)>0
  err=k[parity]*root(ee,10**30)+delta*root(tt,10**30)
  mup=min(rho*pn,quad(v[:8],M8up));assert mup>0
  label='even' if parity==0 else 'odd';errors[label]=err;inputup[label]=mup
  combo=[[sum((I(v[j])*forms[j][part][a] for j in range(22)),I(0)) for a in range(len(forms[0][part]))] for part in range(3)]
  coeff=[sum((V[a][j]*v[j] for j in range(22)),F(0)) for a in range(64)]
  LP=[legendre(a) for a in range(64)]
  poly=[sum((coeff[a]*(LP[a][b] if b<=a else 0) for a in range(64)),F(0)) for b in range(64)]
  translated=[shift([I(x) for x in poly],term['offset']) for term in terms]
  trialmoment=exp_moment(poly,sum(map(abs,coeff),F(0)),replay)
  for n in range(22+parity,64,2):
   zp=[I(x) for x in legendre(n)];zy=[I(x) for x in transformed(legendre(n))];A,B,C=combo
   archpair=R*(integrate(zy,A,mom[0])+2*integrate(zy,B,mom[1])) if replay else R*(integrate(zy,A,mom[0])+integrate(zy,B,mom[1])+integrate(zy,C,mom[2]))
   pp=prime_pair(zp,translated,terms,segments,R/2,replay)
   pole=2*(-1)**parity*trialmoment*exp_moment(legendre(n),F(1),replay)
   value=archpair+pp+pole
   if saved is None:a,b=outward(value,10**30)
   else:
    row=saved['individual_complementary_source_detectors'][len(detectors)];a,b=map(F,row['nominal_source_pairing_enclosure']);assert I(a).h<=value.l<=value.h<=I(b).l
   dm=mass[n];zup=G[n][n]+deltaG*dm;rad=root(dm,10**30)*err;lo,hi=a-rad,b+rad
   distance=min(abs(lo),abs(hi)) if lo*hi>0 else F(0);lower=distance**2/(zup*mup)
   # Exact physical monomial orthogonality implies canonical orthogonality
   # against actual native Riesz representatives, independent of trials.
   for degree in range(n):
    pairing=sum((x*R/2*F(2,degree+j+1) for j,x in enumerate(legendre(n)) if (degree+j)%2==0),F(0));assert pairing==0
   if replay:assert root(dm,10**30)**2>=dm and root(ee,10**30)**2>=ee
   detectors.append(dict(parity=label,source_coefficients=list(map(str,v)),test_degree=n,
    physical_test_squared_norm=str(dm),actual_canonical_test_squared_norm_upper=str(zup),
    actual_source_input_squared_norm_upper=str(mup),enriched_source_physical_error_norm_upper=str(err),
    nominal_source_pairing_enclosure=[str(a),str(b)],actual_source_pairing_enclosure=[str(lo),str(hi)],
    actual_source_pairing_transfer_allowance=str(rad),actual_projected_source_relative_Gram_lower=str(lower),
    applies_to_consecutive_native_head_counts=list(range(22,n+1)),scalar_Schur_budget_ceiling_exceeded=lower>gamma,
    old_fixed_source_budget_exceeded=lower>oldgamma))
   print('individual detector',label,n,float(lower),file=sys.stderr,flush=True)
 for label in ['even','odd']:
  components=[x for x in detectors if x['parity']==label]
  for first in components:
   degree=first['test_degree'];selected=[x for x in components if x['test_degree']>=degree]
   weights=[sum(map(F,x['nominal_source_pairing_enclosure']))/2/F(x['physical_test_squared_norm']) for x in selected];support=[x['test_degree'] for x in selected]
   dm=sum((w*w*mass[n] for w,n in zip(weights,support)),F(0));assert dm>0
   zup=sum((weights[i]*G[n][m]*weights[j] for i,n in enumerate(support) for j,m in enumerate(support)),F(0))+deltaG*dm;assert zup>0
   a=b=F(0)
   for w,x in zip(weights,selected):
    ends=[w*F(y) for y in x['nominal_source_pairing_enclosure']];a+=min(ends);b+=max(ends)
   rad=root(dm,10**30)*errors[label];lo,hi=a-rad,b+rad
   distance=min(abs(lo),abs(hi)) if lo*hi>0 else F(0);lower=distance**2/(zup*inputup[label])
   if replay:assert root(dm,10**30)**2>=dm and lower*zup*inputup[label]==distance**2
   combined.append(dict(parity=label,minimum_test_degree=degree,test_degrees=support,exact_test_coefficients=list(map(str,weights)),
    physical_test_squared_norm=str(dm),actual_canonical_test_squared_norm_upper=str(zup),
    actual_source_input_squared_norm_upper=str(inputup[label]),nominal_source_pairing_enclosure=[str(a),str(b)],
    actual_source_pairing_enclosure=[str(lo),str(hi)],actual_source_pairing_transfer_allowance=str(rad),
    actual_projected_source_relative_Gram_lower=str(lower),applies_to_consecutive_native_head_counts=list(range(22,degree+1)),
    scalar_Schur_budget_ceiling_exceeded=lower>gamma,old_fixed_source_budget_exceeded=lower>oldgamma,
    ratio_to_scalar_Schur_budget_ceiling=str(lower/gamma)))
   print('combined detector',label,degree,float(lower),'ceiling ratio',float(lower/gamma),file=sys.stderr,flush=True)
 accepted=[x for x in combined if x['scalar_Schur_budget_ceiling_exceeded']]
 largest=max((x['minimum_test_degree'] for x in accepted),default=None)
 best=max(combined,key=lambda x:F(x['actual_projected_source_relative_Gram_lower']))
 return dict(milestone='RC69',status='PASS',input_sha256=hashes,trial_dimension=64,
  source_input_scope='two exact low-eight native directions, padded into the actual 22-feature head',
  actual_test_degree_scope=list(range(22,64)),individual_complementary_source_detectors=detectors,
  combined_complementary_source_detectors=combined,strict_scalar_Schur_source_budget_ceiling=str(gamma),old_fixed_source_budget=str(oldgamma),
  largest_consecutive_native_head_count_ruled_out_for_scalar_Schur_budget=largest,
  necessary_consecutive_native_head_count_for_this_budget_lower=largest+1 if largest is not None else None,
  actual_rank_22_scalar_Schur_source_budget_failure_proved=largest is not None and largest>=22,
  strongest_detector=dict(parity=best['parity'],minimum_test_degree=best['minimum_test_degree'],actual_projected_source_relative_Gram_lower=best['actual_projected_source_relative_Gram_lower']),
  lower_bound_scope='directional canonical Cauchy-Schwarz witness, not a Loewner lower bound',
  actual_1250_source_budget_failure_proved=False,whole_aperture_positivity_obstructed=False,
  negative_Weil_direction_proved=False,whole_aperture_positivity_extended=False,RH=False,F4=False)
if __name__=='__main__':
 base=Path(__file__).parent.parent/'certificates'
 defaults=[base/n for n in ['rpb108_rc67_sixty_four_riesz_enrichment.json','rpb108_rc59_twenty_two_native_projection.json','rpb108_rc56_precision_attached_head.json','rpb108_rc43_native_prime_head.json','rpb108_rc46_native_archimedean_head.json','rpb108_rc68_enriched_original_source_covariance.json','rpb108_rc66_arch_multiplier_transport.json','rpb108_rc57_uniform_low_head_floor.json','rpb108_rc63_twenty_two_weak_floor_obstruction.json']]
 if len(sys.argv)>1 and sys.argv[1]=='--replay':
  saved=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,saved)==saved
  print('PASS: independent reflected archimedean, affine prime and closed pole integrations; exact complementary orthogonality and actual canonical leakage lower witnesses')
 else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
