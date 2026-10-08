"""Independent full even56 consumer, pair overlaps and source-error checks."""
import json,gzip,hashlib,sys
from math import isqrt
from pathlib import Path
from fractions import Fraction as F
from certify_native_inverse_correlation_cc13 import I,read,bounds,quad,pivots
from validate_native_defect_envelope_cc15 import controls
ROOT=Path(__file__).resolve().parents[1]
sys.set_int_max_str_digits(0)
def matrix(d):return [[read(x) for x in row] for row in d]
def ldl(A):
 n=len(A);a=[[I(x) if not isinstance(x,I) else x for x in row] for row in A];L=[[I(int(i==j)) for j in range(n)] for i in range(n)];ps=[]
 for k in range(n):
  p=a[k][k]
  if p.lo<=0:return ps,L,k
  ps.append(p)
  for i in range(k+1,n):L[i][k]=a[i][k]/p
  for i in range(k+1,n):
   for j in range(i,n):a[i][j]=a[j][i]=a[i][j]-a[i][k]*a[k][j]/p
 return ps,L,None
def run():
 base=ROOT/'notes/data';p=base/'RPB108_EVEN_BLOCK_CC16_CERTIFICATE_20261008.json';raw=p.read_bytes() if p.exists() else gzip.decompress(p.with_suffix('.json.gz').read_bytes());d=json.loads(raw);c=F(699,1000);checks=controls()
 prior_raw=(base/'RPB108_DEFECT_ENVELOPE_CC15_CERTIFICATE_20261008.json.gz').read_bytes();assert hashlib.sha256(prior_raw).hexdigest()==d['input_sha256']['cc15'];checks+=1;prior=json.loads(gzip.decompress(prior_raw))
 J=matrix(prior['whole_defect_matrix']);A=matrix(d['whole_even_native_matrix']);G=matrix(d['whole_even_source_gram_surrogate']);H=matrix(d['whole_defect_source_cross']);cross=matrix(d['whole_action_retained_source_cross']);L=[[F(x) for x in row] for row in d['rational_complete_matrix_lift']];chart=[[F(x) for x in row] for row in d['original_even_coordinate_chart']];delta=F(d['complete_source_operator_error_paid'])
 gram_raw=(base/'RPB108_PRIME8_GRAM112_105_CERTIFICATE_20261008.json.gz').read_bytes();assert hashlib.sha256(gram_raw).hexdigest()==d['input_sha256']['gram'];checks+=1;gram=json.loads(gzip.decompress(gram_raw))
 source_raw=(base/'RPB108_PRIME8_SOURCE112_105_CERTIFICATE_20261008.json.gz').read_bytes();assert hashlib.sha256(source_raw).hexdigest()==d['input_sha256']['source'];checks+=1
 assert hashlib.sha256(gzip.decompress(source_raw)).hexdigest()==gram['source_certificate_sha256'];checks+=1
 assert delta==F(gram['actual_gram_operator_error_upper'])>0;checks+=1
 even=list(range(0,112,2));assert d['retained_even_degrees']==even and d['mixed_cross_count']==896;checks+=1
 # Every even source Gram entry comes from the pinned complete112 archive.
 for i,n in enumerate(even):
  for j,m in enumerate(even):
   expected=read(gram['residual_gram_surrogate'][n][m]);actual=G[i][j]
   assert max(expected.lo,actual.lo)<=min(expected.hi,actual.hi);checks+=1
 zraw=(base/'RPB108_RICH_ACTION_CC14_CERTIFICATE_20261008.json.gz').read_bytes();assert hashlib.sha256(zraw).hexdigest()==d['input_sha256']['cc14'];checks+=1;z=json.loads(gzip.decompress(zraw));rows=matrix(z['complete_trial_native_rows'])
 # Independent integer-square-root reconstruction of every paid mixed
 # source error, using full physical source norms rather than10^12.
 source=json.loads(gzip.decompress(source_raw));GZ=matrix(z['complete_action_gram'])
 def root800(x):
  grid=10**800;k=isqrt((F(x)*grid*grid).__floor__());return F(k+1,grid)
 proxy=[root800(G[j][j].hi)+root800(sum((max(abs(A[k][j].lo),abs(A[k][j].hi))**2 for k in range(56)),F(0)))+F(source['rows'][even[j]]['normalized_uniform_error']) for j in range(56)]
 for i in range(16):
  full=root800(GZ[i][i].hi+sum((max(abs(x.lo),abs(x.hi))**2 for x in rows[i]),F(0)))
  for j,k in enumerate(even):
   e=F(source['rows'][k]['normalized_uniform_error'])*full+F(z['source_errors'][i+2])*proxy[j]
   paid=F(d['actual_cross_source_error_payments'][i][j]);assert e<=paid and paid-e<F(1,10**100);checks+=1
 for i in range(16):
  for j,k in enumerate(even):
   expected=cross[i][j]/c-rows[i][k];assert max(expected.lo,H[i][j].lo)<=min(expected.hi,H[i][j].hi);checks+=1
 # Pair overlap audits ensure the new complete cross encloses BOTH original
 # CC15 sources, not merely their individual coordinate/source norms.
 saved=json.loads((base/'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json').read_bytes());nf=json.loads((base/'RPB108_CORRELATED_WEAK_ROW_NF71_CERTIFICATE_20261008.json').read_bytes());v=list(map(F,saved['rational_coefficient_witness']));plane=[[F(x) for x in row] for row in nf['even_plane_deterministic_lower']];rho=plane[0][1]/plane[1][1];w=[v[k] for k in even];w[0]-=rho
 r=json.loads((base/'RPB108_INVERSE_CORRELATION_CC13_CERTIFICATE_20261008.json').read_bytes())['even_test_vector_orthogonal_to_all_cc11_five'];r=[F(r[k]) for k in even]
 ac=matrix(prior['whole_mixed_action_source_cross']);nc=matrix(prior['whole_mixed_native_source_cross'])
 for i in range(16):
  for j,x in enumerate((w,r)):
   actual=sum((H[i][k]*x[k] for k in range(56)),I(0));expected=ac[i][j]/c-nc[i][j]
   assert max(actual.lo,expected.lo)<=min(actual.hi,expected.hi);checks+=1
 assert chart[0]==[10**16*x for x in w] and w[1]!=0;checks+=1
 assert chart[1:]==[[F(j==0) for j in range(56)]]+[[F(j==k) for j in range(56)] for k in range(2,56)];checks+=1
 # Independent source-first congruence. The source delta becomes the FULL
 # physical chart Gram, including its off-diagonal entries.
 basis=[0]+list(range(2,56));wv=chart[0]
 def congr(M):
  out=[[I(0) for _ in range(56)] for _ in range(56)];out[0][0]=quad(M,wv)
  for i,k in enumerate(basis,1):
   out[0][i]=out[i][0]=sum((wv[j]*M[j][k] for j in range(56)),I(0))
   for j,l in enumerate(basis,1):out[i][j]=M[k][l]
  return out
 AC=congr(A);GC=congr(G)
 HC=[[sum((H[i][j]*wv[j] for j in range(56)),I(0))]+[H[i][k] for k in basis] for i in range(16)]
 for i in range(16):
  exact=(ac[i][0]/c-nc[i][0])*10**16;a=HC[i][0]
  HC[i][0]=I(max(a.lo,exact.lo),min(a.hi,exact.hi));checks+=1
 LC=[[sum((L[i][j]*wv[j] for j in range(56)),F(0))]+[L[i][k] for k in basis] for i in range(16)]
 JL=[[sum((J[i][k]*LC[k][j] for k in range(16)),I(0)) for j in range(56)] for i in range(16)]
 S=[[AC[i][j]-GC[i][j]/c+sum((HC[k][i]*LC[k][j]+LC[k][i]*HC[k][j]-LC[k][i]*JL[k][j] for k in range(16)),I(0))-delta/c*sum((chart[i][k]*chart[j][k] for k in range(56)),F(0)) for j in range(56)] for i in range(56)]
 for i in range(56):
  for j in range(i+1,56):
   a,b=S[i][j],S[j][i];S[i][j]=S[j][i]=I(min(a.lo,b.lo),max(a.hi,b.hi))
 published=matrix(d['whole_chart_schur_lower'])
 for i in range(56):
  for j in range(56):assert max(S[i][j].lo,published[i][j].lo)<=min(S[i][j].hi,published[i][j].hi);checks+=1
 weights=list(map(F,d['interval_row_weights']));assert weights==[F(1,10**20)]+[F(1)]*55;checks+=1
 payments=[sum(((S[i][j].hi-S[i][j].lo)/2*weights[j]/weights[i] for j in range(56)),F(0)) for i in range(56)];radius=max(payments)
 K=[[(S[i][j].lo+S[i][j].hi)/2-(payments[i] if i==j else 0) for j in range(56)] for i in range(56)];ps,lower,failed=ldl(K)
 out={'passed':True,'exact_checks':checks,'full_original_even_dimension':56,'complete_mixed_action_source_crosses':896,'cc15_both_original_source_cross_overlaps':32,'source_operator_payment_retained':True,'independent_full_ldl_positive_pivots':len(ps),'failed_pivot_index':failed,'whole_even56_lower_passed':failed is None,'independent_chart_row_radius':str(radius),'full_archives_decoded_and_authenticated':True,'full_source_gram_constructors_replayed':False,'actual_inverse_evaluated':False,'whole_odd_sign':False,'nonstalling':False,'lean_certified':False}
 if failed is None:
  # Trace inverse upper from the independently enclosed unit triangular LDL.
  invL=[[I(0) for _ in range(56)] for _ in range(56)]
  for j in range(56):
   for i in range(j,56):invL[i][j]=I(int(i==j))-sum((lower[i][k]*invL[k][j] for k in range(j,i)),I(0))
  trace=sum((max(abs(invL[i][j].lo),abs(invL[i][j].hi))**2/ps[i].lo for i in range(56) for j in range(i+1)),F(0))
  mass=sum((x*x for row in chart for x in row),F(0));tb=1;mb=1
  while tb<trace:tb*=10
  while mb<mass:mb*=10
  tau=F(1,tb*mb);mu=min(tau/300,c/2);kap=mu/(10*(mu+26))
  cc11=json.loads((base/'RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json').read_bytes());oldmu=F(cc11['whole_infinite_slice_physical_margin']);joined=min(mu,oldmu)
  assert list(map(str,pivots(cc11['deterministic_scaled_lower_matrix'])))==cc11['exact_ldl_pivots'];checks+=1
  out.update({'whole_even_retained_physical_margin_lower':str(tau),'whole_infinite_even_physical_margin_lower':str(mu),'whole_infinite_even_canonical_margin_lower':str(kap),'independent_chart_inverse_trace_upper':str(tb),'physical_chart_mass_trace_upper':str(mb),'historical_cc11_physical_margin_preserved':str(oldmu),'joined_even_full_plus_odd3_physical_margin_lower':str(joined),'joined_even_full_plus_odd3_canonical_margin_lower':str(joined/(10*(joined+26))),'new_positive_slice_codimension':53,'original_nonpositive_spectral_dimension_upper':53})
 # Independent whole odd56 gate, retaining ALL mixed entries and delta.
 oddcert=json.loads(gzip.decompress((base/'RPB108_ODD_BLOCK_CC16_CERTIFICATE_20261008.json.gz').read_bytes()));native=json.loads(gzip.decompress((base/'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes()));Q=[[None]*112 for _ in range(112)];pos=0
 for i in range(112):
  for j in range(i+1):Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in native['lower_triangle_row_major'][pos]));pos+=1
 odd=list(range(1,112,2));OS=[[Q[i][j]-read(gram['residual_gram_surrogate'][i][j])/c-(delta/c if i==j else 0) for j in odd] for i in odd]
 oradius=max(sum(((x.hi-x.lo)/2 for x in row),F(0)) for row in OS);OK=[[(OS[i][j].lo+OS[i][j].hi)/2-(oradius if i==j else 0) for j in range(56)] for i in range(56)];op,ol,of=ldl(OK)
 assert len(op)==oddcert['positive_leading_retained_dimension']==55 and of==oddcert['failed_pivot_index']==55;checks+=1
 # Check the entire leading55 matrix supplied by the independent producer.
 published_odd=[[F(x) for x in row] for row in oddcert['positive_leading_deterministic_lower']];opp,oll,opf=ldl(published_odd);assert opf is None and len(opp)==55;checks+=1
 oi=[[I(0) for _ in range(55)] for _ in range(55)]
 for j in range(55):
  for i in range(j,55):oi[i][j]=I(int(i==j))-sum((ol[i][k]*oi[k][j] for k in range(j,i)),I(0))
 ot=sum((max(abs(oi[i][j].lo),abs(oi[i][j].hi))**2/op[i].lo for i in range(55) for j in range(i+1)),F(0));ob=1
 while ob<ot:ob*=10
 omu=min(F(1,ob)/300,c/2)
 out.update({'independent_odd_leading_positive_pivots':55,'whole_odd56_passed':False,'remaining_odd_retained_dimension':1,'independent_odd_leading_inverse_trace_upper':str(ob),'infinite_odd_leading55_physical_margin_lower':str(omu),'actual_odd_negative_direction_certified':False})
 if failed is None:
  joined=min(mu,omu);out.update({'new_positive_slice_codimension':1,'original_nonpositive_spectral_dimension_upper':1,'joined_even_full_plus_odd55_physical_margin_lower':str(joined),'joined_even_full_plus_odd55_canonical_margin_lower':str(joined/(10*(joined+26))),'remaining_even_retained_dimension':0})
 from validate_native_inverse_correlation_cc13 import run as prior_controls
 old=prior_controls();assert old['passed'];out['cc13_controls_replayed']=old['exact_checks'];checks+=1;out['exact_checks']=checks
 (base/'RPB108_EVEN_BLOCK_CC16_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n');return out
if __name__=='__main__':
 d=run();print(json.dumps({k:v for k,v in d.items() if len(str(v))<180},indent=2))
