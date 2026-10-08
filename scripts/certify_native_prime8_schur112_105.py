"""Complete actual-error-corrected Schur decision at 21/20; failures are scoped."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots
from certify_native_prime8_gram112_105 import negative_candidate

ROOT=Path(__file__).resolve().parents[1]/'notes/data'
def read(label):
 p=ROOT/f'RPB108_PRIME8_{label}_105_CERTIFICATE_20261008.json'
 return p.read_bytes(),json.loads(p.read_bytes())
def matrix(n):
 Q=[[None]*112 for _ in range(112)];index=0
 for i in range(112):
  for j in range(i+1):
   Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in n['lower_triangle_row_major'][index]));index+=1
 return Q
def quadratic(A,v):
 return sum((A[i][j]*v[i]*v[j] for i in range(112) for j in range(112)),I(0))
def certificate():
 old=I.grid;I.grid=10**160
 try:
  gr,g=read('GRAM112');sr,s=read('SOURCE112')
  nr=(ROOT/'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json').read_bytes();n=json.loads(nr)
  cr,cdata=read('112_PREFLIGHT');dr,d=read('GARDING')
  assert g['aperture']==s['aperture']==n['aperture']==cdata['aperture']==d['aperture']=='21/20'
  assert g['source_certificate_sha256']==hashlib.sha256(sr).hexdigest() and g['native_certificate_sha256']==hashlib.sha256(nr).hexdigest()
  assert g['panel_count']==13 and g['integration_degree']==942 and g['all_mixed_terms_retained']
  assert g['native_source_pairing_count']==12544 and g['physical_degrees']==list(range(112))
  Q=matrix(n);R=[[I(*map(F,x)) for x in row] for row in g['residual_gram_surrogate']]
  trace=sum((F(g['residual_gram_surrogate'][i][i][1]) for i in range(112)),F(0))
  eta=F(s['source_map_error_upper']);M=F(g['surrogate_residual_map_norm_upper']);assert M*M>=trace>0
  delta=eta*(2*M+eta);assert delta==F(g['actual_gram_operator_error_upper'])
  c=F(cdata['physical_lower']);assert c==F(699,1000)<F(cdata['physical_unrounded_lower']);beta=1/c
  S=[[Q[i][j]-beta*R[i][j]-(I(beta*delta) if i==j else I(0)) for j in range(112)] for i in range(112)]
  base={'aperture':'21/20','physical_degrees':list(range(112)),'interval_grid_digits':160,
   'input_sha256':{'gram':hashlib.sha256(gr).hexdigest(),'source':hashlib.sha256(sr).hexdigest(),'native':hashlib.sha256(nr).hexdigest(),'complement':hashlib.sha256(cr).hexdigest(),'garding':hashlib.sha256(dr).hexdigest()},
   'physical_complement_lower':str(c),'complement_inverse_factor':str(beta),'actual_gram_operator_error_upper':str(delta),
   'complete_source_map_allowance':str(eta),'surrogate_map_norm_upper':str(M),'garding_constant':d['garding_constant'],
   'whole_domain_positivity':False,'actual_negative_weil_vector_certified':False,'f4_entry_closed':False,'lean_formalized':False}
  ordering=None
  for candidate in [list(range(112)),list(range(110,-1,-2))+list(range(111,0,-2)),sorted(range(112),key=lambda i:S[i][i].lo,reverse=True)]:
   try:positive_pivots([[S[i][j]for j in candidate]for i in candidate]);ordering=candidate;break
   except ArithmeticError:pass
  if ordering is None:
   v=negative_candidate(S)
   if v is not None:
    value=quadratic(S,v);q=quadratic(Q,v)
    mass=sum(x*x for x in v)
    base.update(corrected_schur_status='FAIL' if value.hi<0 else 'INCOMPLETE',
     witness_kind='negative corrected sufficient Schur form; not an actual negative Weil vector',
     rational_coefficient_witness=list(map(str,v)),witness_mass_squared=str(mass),
     corrected_witness_interval=[str(value.lo),str(value.hi)],native_weil_witness_interval=[str(q.lo),str(q.hi)],
     corrected_witness_display=[float(value.lo),float(value.hi)],native_weil_witness_display=[float(q.lo),float(q.hi)],
     actual_negative_weil_vector_certified=q.hi<0)
   else:base.update(corrected_schur_status='INCOMPLETE',witness_kind='interval pivot failure without a negative interval witness')
   return base
  tau=F(n['raw_physical_coercivity_lower_bound'])
  if tau<=0:tau=F(1,10**28)
  while True:
   lower=[[S[i][j]-(I(tau) if i==j else I(0)) for j in range(112)] for i in range(112)]
   try:pivots=positive_pivots([[lower[i][j]for j in ordering]for i in ordering]);break
   except ArithmeticError:
    if tau<F(1,10**60):raise
    tau/=2
  lift2=beta*beta*(trace+delta);L=1
  while L*L<=lift2:L+=1
  mu=tau*c/(tau+c*(1+L*L));kap=mu/(10*(mu+d['garding_constant']))
  determinant=(tau-mu*(1+L*L))*(c-mu)-(mu*L)**2;assert determinant==mu*mu>0
  false=2*mu;assert (tau-false*(1+L*L))*(c-false)-(false*L)**2<0
  broken=[row[:] for row in lower];broken[0][0]=I(-1)
  try:positive_pivots(broken)
  except ArithmeticError:pass
  else:raise AssertionError('Negative diagonal accepted')
  base.update(corrected_schur_status='PASS',corrected_coercivity_lower_bound=str(tau),
   pivot_permutation=ordering,shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],lift_norm_squared_upper=str(lift2),lift_operator_norm_integer_upper=L,
   whole_domain_physical_coercivity_lower=str(mu),logarithmic_coercivity_lower=str(kap),
   physical_coercivity_display=float(mu),logarithmic_coercivity_display=float(kap),
   exact_conversion_determinant=str(determinant),oversized_conversion_control_rejected=True,
   negative_diagonal_control_rejected=True,whole_domain_positivity=True,global_endpoint_excluded=False,full_transport_closed=False)
  return base
 finally:I.grid=old
if __name__=='__main__':print(json.dumps(certificate(),indent=2))
