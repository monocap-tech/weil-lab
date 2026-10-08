"""Independent all-arithmetic edge-jump reconstruction on all thirteen panels."""
import json,hashlib
from pathlib import Path
from math import comb,isqrt
from certify_native_legendre_small_window import F,I
from certify_native_exact_logarithm import log_rational

def certificate():
 path=Path('notes/data/RPB108_PRIME8_SOURCE112_105_CERTIFICATE_20261008.json');raw=path.read_bytes();c=json.loads(raw)
 assert c['aperture']=='21/20' and c['prime_terms']==[2,3,4,5,7,8]
 old=I.grid;I.grid=10**500
 try:
  a=F(21,20);powers=[2,3,4,5,7,8];logs={n:log_rational(F(n),500) for n in powers}
  shifts={n:logs[n]/(2*a) for n in powers}
  cuts=[('0',I(0)),('1',I(1))]
  for n in powers:cuts.extend([(f'log({n})/(2a)',shifts[n]),(f'1-log({n})/(2a)',I(1)-shifts[n])])
  cuts.sort(key=lambda x:x[1].lo);assert c['panel_endpoints']==[x[0] for x in cuts]
  active=[]
  for left,right in zip(cuts,cuts[1:]):
   t=(left[1].hi+right[1].lo)/2;row=[]
   for j,n in enumerate(powers):
    for sign in [1,-1]:
     y=I(t)+sign*shifts[n]
     if 0<y.lo<=y.hi<1:row.append((j,sign))
     else:assert y.hi<0 or y.lo>1
   active.append(set(row))
  assert [set(map(tuple,r)) for r in c['panel_active_argument_shifts']]==active
  changes=[]
  for panel in range(12):
   gain=active[panel+1]-active[panel];loss=active[panel]-active[panel+1];assert len(gain)+len(loss)==1
   term=next(iter(gain or loss));changes.append((panel,term,1 if gain else -1))
  profiles=coeffchecks=controls=0
  for degree,row in enumerate(c['rows']):
   assert degree==row['degree'] and len(row['panels'])==13
   p=[(-1)**(degree-j)*comb(degree,j)*comb(degree+j,j) for j in range(degree+1)]
   for panel,(index,sign),gain in changes:
    n=powers[index];base=2 if n in [4,8] else n
    root=isqrt(n*I.grid**2);sqrt=I(F(root,I.grid),F(root+1,I.grid));amplitude=logs[base]/sqrt
    x=sign*shifts[n];xp=[I(1)]
    for _ in range(degree):xp.append(xp[-1]*x)
    expected=[-gain*amplitude*sum((p[j]*comb(j,k)*xp[j-k] for j in range(k,degree+1)),I(0)) for k in range(degree+1)]
    observed=[F(v-u,10**40) for u,v in zip(row['panels'][panel]['low_degree_numerators'],row['panels'][panel+1]['low_degree_numerators'])]
    allowance=F(row['panels'][panel]['coefficient_radius'])+F(row['panels'][panel+1]['coefficient_radius'])
    gap=sum((max(abs(v-e.lo),abs(v-e.hi)) for v,e in zip(observed,expected)),F(0));assert gap<=allowance
    assert abs(observed[-1])>allowance
    profiles+=1;coeffchecks+=degree+1;controls+=1
  assert profiles==controls==1344 and coeffchecks==75936
  return {'aperture':'21/20','source_sha256':hashlib.sha256(raw).hexdigest(),'independent_all_prime_power_profiles_checked':profiles,
   'coefficient_jump_checks':coeffchecks,'all_twelve_arithmetic_support_events_verified':True,'all_thirteen_panels_verified':True,
   'both_orientations_and_von_mangoldt_multiplicities_verified':True,'omitted_profile_controls_rejected':controls,
   'whole_domain_positivity':False,'lean_formalized':False}
 finally:I.grid=old
if __name__=='__main__':print(json.dumps(certificate(),indent=2))
