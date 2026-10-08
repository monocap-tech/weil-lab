"""NF70: actual CC9 weak-channel inverse budget and complete absolute-row audit.
Consumes pinned CC9, compact native and old whole-source bound certificates.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib,json,sys
from certify_native_legendre_small_window import I
I.grid=10**100

def sqrt_upper(x):
 assert x>=0
 g=10**100
 z=(x*g*g).__ceil__();n=isqrt(z)
 if n*n<z:n+=1
 return F(n,g)
def sqrt_interval(x):
 hi=sqrt_upper(x);lo=hi-F(1,10**100)
 return I(max(F(0),lo),hi)
def pair(x): return [str(x.lo),str(x.hi)]
def run(native_path,cc9_path,schur_path):
 raw=Path(native_path).read_bytes();craw=Path(cc9_path).read_bytes()
 n=json.loads(raw);cc=json.loads(craw);oraw=Path(schur_path).read_bytes();old=json.loads(oraw)
 assert hashlib.sha256(raw).hexdigest()==cc['input_sha256']['native']
 assert hashlib.sha256(oraw).hexdigest()==cc['input_sha256']['saved_target']
 assert hashlib.sha256(raw).hexdigest()==old['input_sha256']['native']
 assert n['aperture']==cc['aperture']==old['aperture']=='21/20'
 assert cc['two_retained_plane_positive'] and not cc['whole_domain_positivity']
 intervals=[[I(*map(F,p)) for p in row] for row in cc['original_completed_schur_lower_block']]
 # Symmetric midpoint minus complete row-radius norm is a deterministic lower matrix.
 mid=[[(x.lo+x.hi)/2 for x in row] for row in intervals]
 rad=[[(x.hi-x.lo)/2 for x in row] for row in intervals]
 pad=max(sum(row) for row in rad)
 a=mid[0][0]-pad;b=mid[0][1];d=mid[1][1]-pad
 assert mid[0][1]==mid[1][0] and a>0 and d>0
 ell=a-b*b/d;rho=b/d
 assert ell>F(136,10**34)
 assert d>F(36,1000)
 # Exact weak/strong inverse decomposition, including mixed sign.
 inv=[[1/ell,-rho/ell],[-rho/ell,1/d+rho*rho/ell]]
 assert inv[0][0]*a+inv[0][1]*b==1
 assert inv[0][0]*b+inv[0][1]*d==0
 for x,y in [(F(1),F(0)),(F(0),F(1)),(F(1,7),F(2,9))]:
  assert inv[0][0]*x*x+2*inv[0][1]*x*y+inv[1][1]*y*y==(x-rho*y)**2/ell+y*y/d
 Q=[[None]*112 for _ in range(112)];k=0
 for i in range(112):
  for j in range(i+1):
   l,h=n['lower_triangle_row_major'][k];k+=1
   Q[i][j]=Q[j][i]=I(F(int(l),10**80),F(int(h),10**80))
 v=list(map(F,old['rational_coefficient_witness']))
 # u is the same rational physical constant as CC9; normalized coordinate is nu sqrt(2a).
 u=F(cc['constant_rational_scale'])*sqrt_interval(F(21,10))
 coeff=[I(x) for x in v];coeff[0]=coeff[0]-rho*u
 native_rows=[sum((Q[i][j]*coeff[j] for j in range(112)),I(0)) for i in range(112)]
 row_squared=sum((max(abs(x.lo),abs(x.hi))**2 for x in native_rows),F(0))
 row_upper=sqrt_upper(row_squared)
 # Independent overlaps: actual native witness energy and native constant coupling.
 qh=sum((Q[i][j]*v[i]*v[j] for i in range(112) for j in range(112)),I(0))
 cross=u*sum((Q[0][j]*v[j] for j in range(112)),I(0))
 for got,saved in [(qh,cc['retained_native_block'][0][0]),(cross,cc['retained_native_block'][0][1]),(u*u*Q[0][0],cc['retained_native_block'][1][1])]:
  lo,hi=map(F,saved)
  assert max(got.lo,lo)<=min(got.hi,hi)
 GR=[[I(*map(F,p)) for p in row] for row in cc['actual_retained_source_gram']]
 source_sq=GR[0][0]-2*rho*GR[0][1]+rho*rho*GR[1][1]
 assert source_sq.hi>0
 source_upper=sqrt_upper(source_sq.hi)
 M=F(old['surrogate_map_norm_upper'])+F(old['complete_source_map_allowance'])
 assert M<8
 c=F(cc['complement_lower']);assert c==F(699,1000)
 absolute_mixed_upper=row_upper+M*source_upper/c
 weak_reaction_budget=absolute_mixed_upper**2/ell
 constant_rows=[Q[i][0]*u for i in range(112)]
 constant_native_upper=sqrt_upper(sum((max(abs(x.lo),abs(x.hi))**2 for x in constant_rows),F(0)))
 constant_source_upper=sqrt_upper(GR[1][1].hi)
 constant_mixed_upper=constant_native_upper+M*constant_source_upper/c
 strong_reaction_budget=constant_mixed_upper**2/d
 # Illustrative sufficient requirement for a hypothetical known remainder margin kappa.
 # This is not an evaluated remainder margin or the actual Schur mixed row.
 examples=[]
 for kap in [F(1),F(1,100),F(1,10**32)]:
  threshold=sqrt_upper(ell*kap/2)-F(1,10**100)
  assert threshold*threshold<ell*kap/2
  examples.append({'hypothetical_remainder_margin':str(kap),
   'weak_row_sufficient_budget_lower':str(threshold),
   'display':float(threshold),'actual_remainder_margin_known':False})
 assert weak_reaction_budget>1
 return {'passed':True,'aperture':'21/20','cc9_json_sha256':hashlib.sha256(craw).hexdigest(),
  'compact_native_sha256':hashlib.sha256(raw).hexdigest(),
  'saved_schur_certificate_sha256':hashlib.sha256(oraw).hexdigest(),
  'deterministic_lower_plane':[[str(a),str(b)],[str(b),str(d)]],
  'row_radius_padding':str(pad),'weak_margin':str(ell),'shear_ratio':str(rho),
  'inverse_lower_plane_upper_for_actual_inverse':[[str(x) for x in row] for row in inv],
  'weak_native_row_norm_upper':str(row_upper),
  'weak_complete_projected_source_norm_squared':pair(source_sq),
  'complete_source_operator_norm_upper':str(M),
  'weak_absolute_completed_mixed_row_upper':str(absolute_mixed_upper),
  'weak_inverse_reaction_absolute_budget_upper':str(weak_reaction_budget),
  'strong_absolute_completed_mixed_row_upper':str(constant_mixed_upper),
  'strong_inverse_reaction_absolute_budget_upper':str(strong_reaction_budget),
  'whole_plane_absolute_reaction_budget_upper':str(weak_reaction_budget+strong_reaction_budget),
  'hypothetical_remainder_budget_examples':examples,
  'native_overlap_checks':3,
  'displays':{'weak_margin':float(ell),'shear_ratio':float(rho),
   'inverse_weak_coefficient':float(1/ell),'strong_coefficient':float(1/d),
   'weak_native_row_norm_upper':float(row_upper),'weak_source_norm_upper':float(source_upper),
   'absolute_mixed_row_upper':float(absolute_mixed_upper),
   'absolute_weak_reaction_budget_upper':float(weak_reaction_budget),
   'strong_absolute_mixed_row_upper':float(constant_mixed_upper),
   'whole_plane_absolute_reaction_budget_upper':float(weak_reaction_budget+strong_reaction_budget)},
  'full_binary_gram_replayed':False,'whole_source_gram_bound_imported':True,
  'actual_remaining_completed_mixed_row_evaluated':False,
  'remaining_110_matrix_sign':False,'new_aperture':False,'arithmetic_nondivergence':False,
  'lean_certified':False}
if __name__=='__main__':
 result=run(*sys.argv[1:4]);Path(sys.argv[4]).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'passed':result['passed'],'displays':result['displays'],'native_overlaps':3},indent=2))
