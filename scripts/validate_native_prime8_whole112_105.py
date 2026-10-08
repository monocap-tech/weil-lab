"""Independent widened corrected sign/conversion or scoped failure witness audit."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from certify_native_legendre_small_window import I,positive_pivots
ROOT=Path(__file__).resolve().parents[1]/'notes/data'
def certificate():
 raw=(ROOT/'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json').read_bytes();s=json.loads(raw)
 paths={'gram':'RPB108_PRIME8_GRAM112_105_CERTIFICATE_20261008.json','source':'RPB108_PRIME8_SOURCE112_105_CERTIFICATE_20261008.json',
 'native':'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json','complement':'RPB108_PRIME8_112_PREFLIGHT_105_CERTIFICATE_20261008.json','garding':'RPB108_PRIME8_GARDING_105_CERTIFICATE_20261008.json'}
 d={}
 for key,name in paths.items():
  b=(ROOT/name).read_bytes();assert hashlib.sha256(b).hexdigest()==s['input_sha256'][key];d[key]=json.loads(b)
 assert all(x['aperture']=='21/20' for x in d.values())
 c=F(d['complement']['physical_lower']);g=d['gram'];eta=F(d['source']['source_map_error_upper']);M=F(g['surrogate_residual_map_norm_upper'])
 trace=sum(F(g['residual_gram_surrogate'][i][i][1]) for i in range(112));assert M*M>=trace>0
 assert eta**2>=sum(F(x['normalized_uniform_error'])**2 for x in d['source']['rows'])
 delta=eta*(2*M+eta);assert delta==F(s['actual_gram_operator_error_upper'])==F(g['actual_gram_operator_error_upper'])
 saved=I.grid;I.grid=10**80
 try:
  Q=[[None]*112 for _ in range(112)];idx=0
  for i in range(112):
   for j in range(i+1):
    Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in d['native']['lower_triangle_row_major'][idx]));idx+=1
  R=[[I(*map(F,x)) for x in row] for row in g['residual_gram_surrogate']]
  S=[[Q[i][j]-R[i][j]/c-(I(delta/c) if i==j else I(0)) for j in range(112)] for i in range(112)]
  base={'aperture':'21/20','schur_certificate_sha256':hashlib.sha256(raw).hexdigest(),'independent_widened_grid_digits':80,
  'complete_actual_source_correction_recomputed':True,'whole_domain_positivity':False,'actual_negative_weil_vector_certified':False,'f4_entry_closed':False,'lean_formalized':False}
  if s['corrected_schur_status']=='PASS':
   tau=F(s['corrected_coercivity_lower_bound']);order=s['pivot_permutation'];assert sorted(order)==list(range(112));p=positive_pivots([[S[i][j]-(I(tau) if i==j else I(0)) for j in order] for i in order])
   L=s['lift_operator_norm_integer_upper'];assert L*L>=(trace+delta)/(c*c)
   mu=F(s['whole_domain_physical_coercivity_lower']);kap=F(s['logarithmic_coercivity_lower']);D=d['garding']['garding_constant']
   assert mu==tau*c/(tau+c*(1+L*L)) and kap==mu/(10*(mu+D))
   assert (tau-mu*(1+L*L))*(c-mu)-(mu*L)**2==mu*mu>0
   false=2*mu;assert (tau-false*(1+L*L))*(c-false)-(false*L)**2<0
   broken=[row[:] for row in S];broken[0][0]=I(-1)
   try:positive_pivots(broken)
   except ArithmeticError:pass
   else:raise AssertionError('Negative control accepted')
   base.update(corrected_schur_status='PASS',shifted_pivots_checked=112,exact_physical_and_logarithmic_conversions_verified=True,
   negative_diagonal_control_rejected=True,oversized_conversion_control_rejected=True,whole_domain_positivity=True,
   physical_lower=str(mu),logarithmic_lower=str(kap))
  elif s['corrected_schur_status']=='FAIL':
   v=list(map(F,s['rational_coefficient_witness']));assert len(v)==112;mass=sum(x*x for x in v);assert mass>0
   def value(A):return sum((A[i][j]*v[i]*v[j] for i in range(112) for j in range(112)),I(0))
   sv,qv,rv=map(value,[S,Q,R]);assert sv.hi<0
   noerror=qv-rv/c;needed=None
   if qv.lo>0:needed=(rv.lo+delta*mass)/qv.hi
   base.update(corrected_schur_status='FAIL',negative_sufficient_schur_interval=[str(sv.lo),str(sv.hi)],
   native_weil_interval=[str(qv.lo),str(qv.hi)],native_weil_interval_display=[float(qv.lo),float(qv.hi)],
   uncorrected_surrogate_schur_interval=[str(noerror.lo),str(noerror.hi)],
   uncorrected_surrogate_sign_also_negative=noerror.hi<0,
   required_scalar_complement_strict_lower=None if needed is None else str(needed),
   required_scalar_complement_lower_display=None if needed is None else float(needed),
   actual_negative_weil_vector_certified=qv.hi<0,
   failure_scope='complete corrected sufficient Schur form; actual Weil sign is independently reported')
  else:base.update(corrected_schur_status='INCOMPLETE',failure_scope='interval pivot failure without exact negative Schur witness')
  return base
 finally:I.grid=saved
if __name__=='__main__':print(json.dumps(certificate(),indent=2))
