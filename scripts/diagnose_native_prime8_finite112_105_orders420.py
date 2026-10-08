"""Diagnose native interval sign failure without equating it to actual negativity."""
import gzip,json,hashlib
from pathlib import Path
from math import isqrt
from certify_native_legendre_small_window import F,I
from certify_native_matrix112_checkpoint import load
from certify_native_prime8_gram112_105 import negative_candidate

def run():
 root=Path('notes/data');path=root/'RPB108_PRIME8_RAW112_105_ORDERS420_CHECKPOINT_20261008.json.gz'
 raw=path.read_bytes();st=json.loads(gzip.decompress(raw));assert st['completed_rows']==112 and st['bindings']['aperture']=='21/20'
 I.grid=10**400;done,rawQ=load(path,st['bindings']);assert done==112
 def sqrt(x):
  n=isqrt(x*I.grid**2);return I(F(n,I.grid),F(n+1,I.grid))
 Q=[[sqrt((2*i+1)*(2*j+1))*rawQ[i][j]/F(21,10) for j in range(112)] for i in range(112)]
 width=max(x.hi-x.lo for row in Q for x in row)
 out={'aperture':'21/20','raw_checkpoint_sha256':hashlib.sha256(raw).hexdigest(),'completed_rows':112,'maximum_entry_width':str(width),'maximum_entry_width_display':float(width),'physical_degrees':list(range(112)),'prime_terms':[2,3,4,5,7,8],'whole_domain_positivity':False,'finite_sign_certified':False,'actual_negative_weil_vector_certified':False,'f4_entry_closed':False}
 failures=[]
 for parity in [0,1]:
  deg=list(range(parity,112,2));m=[[x for x in row] for row in [[Q[i][j] for j in deg] for i in deg]]
  for k in range(len(m)):
   p=m[k][k]
   if p.lo<=0:
    failures.append({'parity':parity,'pivot_index_in_parity_block':k,'degree':deg[k],'pivot_interval':[str(p.lo),str(p.hi)],'display':[float(p.lo),float(p.hi)],'previous_positive_pivots':k});break
   for i in range(k+1,len(m)):
    for j in range(i,len(m)):
     m[i][j]=m[i][j]-m[i][k]*m[k][j]/p;m[j][i]=m[i][j]
  else:failures.append({'parity':parity,'all_pivots_positive':True})
 out['interval_parity_audits']=failures
 v=negative_candidate(Q)
 if v is not None:
  q=sum((Q[i][j]*v[i]*v[j] for i in range(112) for j in range(112)),I(0));mass=sum(x*x for x in v)
  out.update(rational_trial=list(map(str,v)),trial_mass=str(mass),trial_weil_interval=[str(q.lo),str(q.hi)],trial_weil_interval_display=[float(q.lo),float(q.hi)],actual_negative_weil_vector_certified=q.hi<0)
 else:out.update(midpoint_negative_trial_found=False)
 # Export exact physical raw intervals for independent normalization/pairing diagnosis.
 payload={'aperture':'21/20','physical_degrees':list(range(112)),'prime_terms':[2,3,4,5,7,8],
  'matrix_intervals':[[[str(x.lo),str(x.hi)] for x in row] for row in Q],'maximum_entry_width':str(width),'raw_checkpoint_sha256':hashlib.sha256(raw).hexdigest(),'finite_sign_certified':False,'whole_domain_positivity':False}
 (root/'RPB108_PRIME8_MATRIX112_105_ORDERS420_UNDECIDED_20261008.json').write_text(json.dumps(payload,indent=2)+'\n')
 (root/'RPB108_PRIME8_FINITE112_105_ORDERS420_DIAGNOSIS_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['rational_trial','maximum_entry_width','raw_checkpoint_sha256','physical_degrees','interval_parity_audits','trial_weil_interval']},indent=2))
 print(json.dumps([{k:v for k,v in x.items() if k!='pivot_interval'} for x in failures]))
if __name__=='__main__':run()
