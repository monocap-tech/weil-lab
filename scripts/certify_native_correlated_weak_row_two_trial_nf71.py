"""NF71: correlated whole even-remainder row with original degree112/114 lift."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys
from certify_native_legendre_small_window import I
from certify_native_weak_reaction_budget_nf70 import sqrt_upper,sqrt_interval
I.grid=10**100
def interval(p):return I(*map(F,p))
def bounds(x):return [str(x.lo),str(x.hi)]
def mid(x):return (x.lo+x.hi)/2
def norm_upper(row):return sqrt_upper(sum((max(abs(x.lo),abs(x.hi))**2 for x in row),F(0)))
def run(native_path,cc9_path,old_path,cc3_path,oldbudget_path,fresh114_path):
 raws=[Path(p).read_bytes() for p in (native_path,cc9_path,old_path,cc3_path,oldbudget_path,fresh114_path)]
 n,cc,old,t3,oldb,fresh=map(json.loads,raws)
 assert fresh['passed'] and fresh['degree']==114 and fresh['aperture']=='21/20'
 assert fresh['prime_powers']==[2,3,4,5,7,8] and fresh['both_signed_poles_retained']
 assert hashlib.sha256(raws[0]).hexdigest()==t3['native_sha256']==old['input_sha256']['native']==cc['input_sha256']['native']
 assert hashlib.sha256(raws[2]).hexdigest()==cc['input_sha256']['saved_target']==t3['witness_sha256']
 v=list(map(F,old['rational_coefficient_witness']));rho=F(oldb['shear_ratio'])
 a=F(oldb['deterministic_lower_plane'][0][0]);b=F(oldb['deterministic_lower_plane'][0][1]);d=F(oldb['deterministic_lower_plane'][1][1])
 assert b/d==rho
 Q=[[None]*112 for _ in range(112)];index=0
 for i in range(112):
  for j in range(i+1):
   l,h=n['lower_triangle_row_major'][index];index+=1
   Q[i][j]=Q[j][i]=I(F(int(l),10**80),F(int(h),10**80))
 odd=[F(0) if i%2==0 else x for i,x in enumerate(v)]
 oddmass=sum((x*x for x in odd),F(0))
 qodd=sum((Q[i][j]*odd[i]*odd[j] for i in range(1,112,2) for j in range(1,112,2)),I(0))
 # S(odd,odd)<=native Q(odd,odd), because original complement inverse is positive.
 aeven=a-qodd.hi;ell=aeven-b*b/d
 assert ell>F(136,10**34)
 u=F(cc['constant_rational_scale'])*sqrt_interval(F(21,10))
 ve=[x if i%2==0 else F(0) for i,x in enumerate(v)]
 weak=[I(x) for x in ve];weak[0]=weak[0]-rho*u
 native_row=[sum((Q[i][j]*weak[j] for j in range(0,112,2)),I(0)) for i in range(112)]
 assert all(x.lo==x.hi==0 for i,x in enumerate(native_row) if i%2)
 trial_row=[I(0) for _ in range(112)]
 for row in t3['even_projection_pairings']:trial_row[row['degree']]=interval(row['trial'])
 assert len(t3['even_projection_pairings'])==56
 trials=[trial_row,[interval(p) for p in fresh['native_projection_row']]]
 assert all(trials[1][i].lo==trials[1][i].hi==0 for i in range(1,112,2))
 G=[[interval(p) for p in row] for row in cc['actual_retained_source_gram']]
 V=[[interval(p) for p in row] for row in cc['mixed_trial_action']]
 Gz=[[interval(p) for p in row] for row in cc['trial_action_gram']]
 Qz=[[interval(p) for p in row] for row in cc['trial_native_gram']]
 Bz=[[interval(p) for p in row] for row in cc['mixed_trial_native']]
 overlaps=0
 for got,p in [(Gz[0][0],t3['trial_complement_source_norm_squared']),
               (Qz[0][0],t3['trial_native_pairing']),
               (V[0][0],t3['residual_source_cross']),
               (Bz[0][0],t3['native_cross_pairing'])]:
  saved=interval(p);assert max(got.lo,saved.lo)<=min(got.hi,saved.hi);overlaps+=1
 # Entire source residual: even residual is bounded by the full saved one.
 source_sq=G[0][0]-2*rho*G[0][1]+rho*rho*G[1][1]
 source_action=[V[i][0]-rho*V[i][1] for i in range(2)]
 # Fresh self/mixed native audits preserve the SAME rational trials.
 for got,saved in [(Qz[1][1],fresh['self_native']),(Qz[0][1],fresh['mixed112_native'])]:
  check=interval(saved);assert max(got.lo,check.lo)<=min(got.hi,check.hi);overlaps+=1
 c=F(cc['complement_lower']);M=F(old['surrogate_map_norm_upper'])+F(old['complete_source_map_allowance'])
 assert c==F(699,1000) and M<8
 # Physical orthogonal even quotient: constant coordinate zero, orthogonal to ve tail.
 tail=[F(0) if i==0 else x for i,x in enumerate(ve)]
 mass=sum((x*x for x in tail),F(0));assert mass>F(1,2)
 def quotient(row):
  alpha=sum((tail[i]*row[i] for i in range(112)),I(0))/mass
  return [I(0) if i==0 else row[i]-tail[i]*alpha for i in range(112)]
 det=mid(Gz[0][0])*mid(Gz[1][1])-mid(Gz[0][1])**2
 assert det>0
 t_opt=[(mid(Gz[1][1])*mid(source_action[0])-mid(Gz[0][1])*mid(source_action[1]))/det,
        (mid(Gz[0][0])*mid(source_action[1])-mid(Gz[0][1])*mid(source_action[0]))/det]
 t_one=mid(source_action[0])/mid(Gz[0][0])
 proposals=[(F(0),F(0)),(F(t3['coefficient']),F(0)),(t_one,F(0))]
 proposals +=[(t_opt[0]*F(k,10),t_opt[1]*F(l,10)) for k in range(21) for l in range(21)]
 creditlift=cc['rational_linear_lift']
 proposals.append(tuple(F(creditlift[i][0])-rho*F(creditlift[i][1]) for i in range(2)))
 results=[]
 for proposal in proposals:
  t=[F((p*10**100).__floor__(),10**100) for p in proposal]
  row=quotient([native_row[i]-sum((t[j]*trials[j][i] for j in range(2)),I(0)) for i in range(112)])
  rownorm=norm_upper(row)
  residual=source_sq-2*sum((t[i]*source_action[i] for i in range(2)),I(0))
  residual+=sum((t[i]*Gz[i][j]*t[j] for i in range(2) for j in range(2)),I(0))
  assert residual.hi>=0
  residualnorm=sqrt_upper(residual.hi)
  bound=rownorm+M*residualnorm/c
  results.append((bound,t,rownorm,residualnorm,residual,row))
 best=min(results,key=lambda z:z[0])
 zero=next(z for z in results if z[1]==[0,0])
 one=min((z for z in results if z[1][1]==0),key=lambda z:z[0])
 bound,t,rownorm,resnorm,residual,row=best
 assert bound<one[0]<zero[0] and bound<F(oldb['weak_absolute_completed_mixed_row_upper'])
 budget=bound*bound/ell
 # All56 original odd directions decouple from the NEW exact even weak direction.
 odd_decoupled=all(x.lo==x.hi==0 for i,x in enumerate(row) if i%2)
 assert odd_decoupled
 return {'passed':True,'aperture':'21/20',
  'input_sha256':dict(zip(['native','cc9','old_schur','cc3','nf70','fresh_degree114'],[hashlib.sha256(x).hexdigest() for x in raws])),
  'odd_witness_mass':str(oddmass),'native_odd_witness_energy':bounds(qodd),
  'even_plane_deterministic_lower':[[str(aeven),str(b)],[str(b),str(d)]],
  'even_weak_margin':str(ell),'retained_even_quotient_dimension':54,
  'entire_original_odd_dimension':56,'odd_weak_cross_exactly_zero':True,
  'trial_degrees':[112,114],'trial_rational_normalizations':[t3['trial_rational_normalization'],fresh['rational_normalization']],
  'rational_trial_coefficients':list(map(str,t)),'proposal_count':len(results),
  'lifted_native_projected_row_norm_upper':str(rownorm),
  'whole_source_residual_norm_squared':bounds(residual),'whole_source_residual_norm_upper':str(resnorm),
  'complete_even_quotient_mixed_row_upper':str(bound),
  'weak_inverse_reaction_upper':str(budget),
  'zero_trial_quotient_bound':str(zero[0]),'one_trial_quotient_bound':str(one[0]),
  'fresh_degree114_native_overlap_checks':fresh['independent_cc9_overlap_checks'],
  'correlated_projected_native_row':list(map(bounds,row)),
  'independent_trial_overlap_checks':overlaps,
  'displays':{'odd_mass':float(oddmass),'odd_native_energy_upper':float(qodd.hi),
   'even_weak_margin':float(ell),'trial_coefficients':list(map(float,t)),'lifted_native_row':float(rownorm),
   'whole_residual_norm':float(resnorm),'completed_mixed_row_upper':float(bound),
   'one_trial_quotient_bound':float(one[0]),'zero_trial_quotient_bound':float(zero[0]),'nf70_absolute_bound':float(F(oldb['weak_absolute_completed_mixed_row_upper'])),
   'weak_reaction_budget_upper':float(budget),'nf70_weak_reaction_budget':float(F(oldb['weak_inverse_reaction_absolute_budget_upper']))},
  'whole_even_quotient_mixed_row_upper_evaluated':True,'actual_complement_inverse_evaluated':False,'whole_remaining_matrix_sign':False,
  'whole_odd_form_positive':False,'new_whole_aperture':False,'arithmetic_nondivergence':False,'lean_certified':False}
if __name__=='__main__':
 r=run(*sys.argv[1:7]);Path(sys.argv[7]).write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps({'passed':r['passed'],'displays':r['displays'],'trial_overlaps':r['independent_trial_overlap_checks']},indent=2))
