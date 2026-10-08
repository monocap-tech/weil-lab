"""Entire original odd56 no-lift gate and its complete positive leading block."""
import json,gzip,hashlib,sys
from pathlib import Path
from certify_native_rich_action_cc14 import I,F,compact
from certify_native_even_block_cc16 import interval_ldl
ROOT=Path(__file__).resolve().parents[1];sys.set_int_max_str_digits(0)
def compute():
 base=ROOT/'notes/data';names={'gram':'RPB108_PRIME8_GRAM112_105_CERTIFICATE_20261008.json.gz','native':'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz','source':'RPB108_PRIME8_SOURCE112_105_CERTIFICATE_20261008.json.gz'};raw={k:(base/v).read_bytes() for k,v in names.items()};decoded={k:gzip.decompress(x) for k,x in raw.items()};d={k:json.loads(x) for k,x in decoded.items()};g,n=d['gram'],d['native']
 assert hashlib.sha256(decoded['source']).hexdigest()==g['source_certificate_sha256'] and hashlib.sha256(decoded['native']).hexdigest()==g['native_certificate_sha256']
 Q=[[None]*112 for _ in range(112)];p=0
 for i in range(112):
  for j in range(i+1):Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in n['lower_triangle_row_major'][p]));p+=1
 odd=list(range(1,112,2));c=F(699,1000);delta=F(g['actual_gram_operator_error_upper'])
 S=[[Q[i][j]-I(*map(F,g['residual_gram_surrogate'][i][j]))/c-(delta/c if i==j else 0) for j in odd] for i in odd]
 grid=10**100;radius=max(sum(((x.hi-x.lo)/2 for x in row),F(0)) for row in S);radius=F((radius*grid).__ceil__()+56,grid)
 K=[[F((((S[i][j].lo+S[i][j].hi)/2)*grid).__floor__(),grid)-(radius if i==j else 0) for j in range(56)] for i in range(56)]
 ps,L,failed,bad=interval_ldl(K);size=len(ps)
 inv=[[I(0) for _ in range(size)] for _ in range(size)]
 for j in range(size):
  for i in range(j,size):inv[i][j]=I(int(i==j))-sum((L[i][k]*inv[k][j] for k in range(j,i)),I(0))
 trace=sum((max(abs(inv[i][j].lo),abs(inv[i][j].hi))**2/ps[i].lo for i in range(size) for j in range(i+1)),F(0));bound=1
 while bound<trace:bound*=10
 tau=F(1,bound);mu=min(tau/300,c/2)
 out={'stage':'CC16 entire original odd56 no-lift gate','aperture':'21/20','odd_native_degrees':odd,'all_original_panels':13,'all_prime_powers':[2,3,4,5,7,8],'both_signed_poles':True,'complete_source_operator_error_paid':str(delta),'full_odd56_passed':failed is None,'positive_leading_retained_dimension':size,'positive_leading_degrees':odd[:size],'remaining_odd_retained_dimension':56-size,'failed_pivot_index':failed,'failed_pivot_interval':None if bad is None else compact(bad),'positive_leading_ldl_pivots':list(map(compact,ps)),'positive_leading_deterministic_lower':[[str(K[i][j]) for j in range(size)] for i in range(size)],'leading_inverse_trace_upper':str(bound),'leading_retained_physical_margin_lower':str(tau),'infinite_odd_leading_slice_physical_margin_lower':str(mu),'infinite_odd_leading_slice_canonical_margin_lower':str(mu/(10*(mu+26))),'actual_odd_negative_direction_certified':False,'actual_inverse_evaluated':False,'nonstalling':False,'lean_certified':False,'input_sha256':{k:hashlib.sha256(x).hexdigest() for k,x in raw.items()}}
 b=(json.dumps(out,indent=2)+'\n').encode();(base/'RPB108_ODD_BLOCK_CC16_CERTIFICATE_20261008.json').write_bytes(b);(base/'RPB108_ODD_BLOCK_CC16_CERTIFICATE_20261008.json.gz').write_bytes(gzip.compress(b,mtime=0));print(json.dumps({'positive_leading_dimension':size,'remaining_odd_dimension':56-size,'failed_pivot_index':failed,'margin':float(mu)},indent=2));return out
if __name__=='__main__':compute()
