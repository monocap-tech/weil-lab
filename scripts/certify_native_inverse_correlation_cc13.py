"""CC13: actual even quotient calibration and sharp inverse-interval limit.

This audits an estimator, not the original whole Schur matrix. Synthetic
controls are identified separately and do not replace arithmetic data.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import gzip, hashlib, json, sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
GRID=10**100
class I:
 def __init__(self,a,b=None):
  a=F(a);b=a if b is None else F(b)
  assert a<=b
  self.lo=F((a*GRID).__floor__(),GRID);self.hi=F((b*GRID).__ceil__(),GRID)
 def __add__(self,o):
  o=o if isinstance(o,I) else I(o);return I(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,o):return self+-asI(o)
 def __rsub__(self,o):return asI(o)+-self
 def __mul__(self,o):
  o=asI(o);v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)];return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=asI(o);assert not o.lo<=0<=o.hi;return self*I(1/o.hi,1/o.lo)
def asI(o):return o if isinstance(o,I) else I(o)
def read(x):return I(*map(F,x))
def bounds(x):return [str(x.lo),str(x.hi)]
def sqrt_bounds(x):
 x=F(x);assert x>=0;k=isqrt((x*GRID**2).__floor__());return I(F(k,GRID),F(k+1,GRID))
def quad(A,v):return sum((v[i]*A[i][j]*v[j] for i in range(len(v)) for j in range(len(v))),I(0))
def solve(A,b):
 n=len(b);m=[list(map(F,row))+[F(b[i])] for i,row in enumerate(A)]
 for i in range(n):
  assert m[i][i]!=0;p=m[i][i];m[i]=[x/p for x in m[i]]
  for j in range(n):
   if j!=i:
    t=m[j][i];m[j]=[x-t*y for x,y in zip(m[j],m[i])]
 return [row[-1] for row in m]
def pivots(A):
 A=[list(map(F,row)) for row in A];out=[]
 for k in range(len(A)):
  p=A[k][k];assert p>0;out.append(p)
  for i in range(k+1,len(A)):
   for j in range(i,len(A)):
    A[i][j]-=A[i][k]*A[k][j]/p;A[j][i]=A[i][j]
 return out
def compute():
 names={'nf71':'RPB108_CORRELATED_WEAK_ROW_NF71_CERTIFICATE_20261008.json',
 'cc9':'RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json',
 'cc11':'RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json',
 'cc12':'RPB108_QUANTITATIVE_BRIDGE_CC12_CERTIFICATE_20261008.json',
 'saved':'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json'}
 raws={k:(ROOT/'notes/data'/p).read_bytes() for k,p in names.items()}
 d={k:json.loads(v) for k,v in raws.items()};nf,old,odd,saved=d['nf71'],d['cc9'],d['cc11'],d['saved']
 for key in ('cc9','cc11','saved'):
  assert hashlib.sha256(raws[key]).hexdigest()==d['cc12']['input_sha256'][key]
 assert hashlib.sha256(raws['cc9']).hexdigest()==nf['input_sha256']['cc9']
 assert hashlib.sha256(raws['saved']).hexdigest()==nf['input_sha256']['old_schur']
 G5=[[F(x) for x in row] for row in odd['deterministic_scaled_lower_matrix']]
 pp=pivots(G5);assert list(map(str,pp))==odd['exact_ldl_pivots']
 assert odd['protected_slice_codimension']==107 and odd['five_retained_plane_positive']
 raw=gzip.decompress((ROOT/'notes/data/RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
 assert hashlib.sha256(raw).hexdigest()==saved['input_sha256']['native']==old['input_sha256']['native']
 n=json.loads(raw);Q=[[None]*112 for _ in range(112)];index=0
 assert hashlib.sha256(raw).hexdigest()==nf['input_sha256']['native']==d['cc12']['input_sha256']['native']
 for i in range(112):
  for j in range(i+1):
   Q[i][j]=Q[j][i]=I(*(F(int(x),10**80) for x in n['lower_triangle_row_major'][index]));index+=1
 v=list(map(F,saved['rational_coefficient_witness']))
 hm=sum((v[j]**2 for j in range(2,112,2)),F(0));assert hm>v[2]**2
 r=[F(j==2)-v[2]*v[j]/hm if j>=2 and j%2==0 else F(0) for j in range(112)]
 mass=sum((x*x for x in r),F(0));assert mass>0
 assert sum((r[j]*v[j] for j in range(112)),F(0))==0
 assert r[0]==0 and all(r[j]==0 for j in range(1,112,2))
 qr=quad(Q,r);ray=qr/mass;assert 0<ray.lo<=ray.hi<F(241,1000)
 a=sum((read(nf['correlated_projected_native_row'][j])*r[j] for j in range(112)),I(0))
 ell=F(nf['even_weak_margin']);c=F(699,1000)
 plane=[[F(x) for x in row] for row in nf['even_plane_deterministic_lower']]
 rho=plane[0][1]/plane[1][1];assert plane[0][0]-plane[0][1]*rho==ell
 GR=[[read(x) for x in row] for row in old['actual_retained_source_gram']]
 GZ=[[read(x) for x in row] for row in old['trial_action_gram']]
 V=[read(row[0])-rho*read(row[1]) for row in old['mixed_trial_action']]
 weak=quad(GR,[F(1),-rho])
 # Historical odd source is retained in GR. Pay its complete upper norm
 # when converting a LOWER residual endpoint to the exactly even source.
 oddmass=sum((v[j]**2 for j in range(1,112,2)),F(0));oddsource=64*oddmass
 det=GZ[0][0]*GZ[1][1]-GZ[0][1]*GZ[1][0];assert det.lo>0
 credit=(GZ[1][1]*V[0]*V[0]-2*GZ[0][1]*V[0]*V[1]+GZ[0][0]*V[1]*V[1])/det
 minimum=weak-credit-I(0,oddsource);assert minimum.lo>F(24,10**33)
 M=F(saved['surrogate_map_norm_upper'])+F(saved['complete_source_map_allowance']);assert 7<M<8
 # Sharp scalar inverse interval with granted ZERO unweighted correlation:
 # radius = ||E|| ||B_r||/(2c). This is an allowance, not actual reaction.
 floor=M*M*minimum.lo/(4*c*c*ell);assert floor>48 and floor>ray.hi
 # If a compatible positive J_R existed, the best necessary row scale on
 # this normalized r is at most sqrt(ell*ray.hi). No lower J is inferred.
 ceiling=sqrt_bounds(ell*ray.hi)
 headnorm=a/sqrt_bounds(mass)
 # EXACT summary countercontrol. E and B_r are orthogonal and their complete
 # ordinary 2-source Gram is identical. Native head/diagonal are inside the
 # actual tested intervals. This does NOT match every arithmetic custody blob.
 s=F(155,10**18);b=F(17,50);k=5/(8*c);mix=3/(8*c)
 aa=(a.lo+a.hi)/2;qq=(qr.lo+qr.hi)/2;J=qq-k*b*b;assert J>0
 A=[[ell+k*s*s,aa],[aa,qq]]
 # H0=k I; H1=[[k,-mix],[-mix,k]], all 0<H<=1/c.
 C0=[[1/k,F(0)],[F(0),1/k]]
 C1=[[5*c/2,3*c/2],[3*c/2,5*c/2]]
 assert pivots([[C0[i][j]-(c if i==j else 0) for j in range(2)] for i in range(2)])
 assert C1[0][0]-c==abs(C1[0][1]) and C1[1][1]-c==abs(C1[1][0])
 gooddet=ell*J-aa*aa;badcross=aa+mix*s*b;baddet=ell*J-badcross*badcross
 assert gooddet>0 and baddet<0 and s*s<minimum.lo
 # Complete ORIGINAL source identity is unchanged. Synthetic controls have
 # their own full covariance identity; no prime/pole slot is relabeled.
 return {'stage':'CC13 sharp inverse-correlation information limit','classification':'C',
 'method_stopped':'ordinary residual correlation plus scalar protected inverse interval',
 'actual_arithmetic_new_suppression':False,'aperture':'21/20',
 'current_whole_domain_aperture':'1','protected_codimension':107,
 'cc11_five_scaled_ldl_pivots_recomputed':list(map(str,pp)),
 'exact_even_quotient_dimension':54,'remaining_odd_quotient_dimension':53,
 'even_test_vector_orthogonal_to_all_cc11_five':list(map(str,r)),
 'test_mass':str(mass),'native_test_energy':bounds(qr),'native_rayleigh_upper_for_completed_remainder':bounds(ray),
 'actual_correlated_trial_native_head_on_test':bounds(a),'normalized_head':bounds(headnorm),
 'even_weak_margin':str(ell),'exact_even_minimum_two_trial_residual_squared':bounds(minimum),
 'historical_odd_source_lower_endpoint_payment':str(oddsource),
 'entire_source_map_upper':str(M),'complement_lower':str(c),
 'granted_zero_ordinary_correlation_uniform_allowance_floor':str(floor),
 'best_possible_test_row_ceiling_if_remainder_positive':bounds(ceiling),
 'summary_countercontrol':{'scope':'matches tested scalar intervals and granted ordinary correlation only; not all original arithmetic data',
 'residual_scale':str(s),'test_source_scale':str(b),'source_gram':[[str(s*s),'0'],['0',str(b*b)]],
 'native_residual_chart':[[str(x) for x in row] for row in A],
 'C_good':[[str(x) for x in row] for row in C0],'C_bad':[[str(x) for x in row] for row in C1],
 'same_inverse_diagonals':str(k),'remaining_lower_form_in_both':str(J),
 'positive_completed_determinant':str(gooddet),'negative_completed_determinant':str(baddet),
 'inverse_correlation_good':'0','inverse_correlation_bad':str(-mix*s*b)},
 'whole_even_sign':False,'whole_odd_sign':False,'cc12_obstruction_overcome':False,
 'global_nonstalling':False,'full_binary_source_gram_replayed':False,'lean_certified':False,
 'input_sha256':{**{k:hashlib.sha256(x).hexdigest() for k,x in raws.items()},'native':hashlib.sha256(raw).hexdigest()},
 'displays':{'test_rayleigh_upper':float(ray.hi),'normalized_native_head':float(headnorm.hi),
 'even_residual_floor':float(minimum.lo),'best_ordinary_orthogonality_allowance_floor':float(floor),
 'test_row_ceiling':float(ceiling.hi),'compatible_countercontrol_remainder':float(J),
 'good_determinant':float(gooddet),'bad_determinant':float(baddet)}}
if __name__=='__main__':
 out=compute();(ROOT/'notes/data/RPB108_INVERSE_CORRELATION_CC13_CERTIFICATE_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out['displays'],indent=2))
