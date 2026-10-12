"""RC130: paid remaining two-column covariance and reference Schur upper.
Four-vector endpoint family only; no original Weil action or positivity.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import (
 B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner)
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,cong,inv,transpose

def imul(a,b):
 products=[x*y for x in a for y in b];return min(products),max(products)
def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,response,old=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in (prior,response,old)]==['RC129','RC128','RC127']
 assert prior['input_sha256'][:2]==hs[1:] and response['input_sha256'][0]==hs[2]
 def mat(k):return [[F(x) for x in r] for r in prior[k]]
 GL=mat('actual_D_Gram_Loewner_lower');GU=mat('actual_D_Gram_Loewner_upper')
 HL=mat('actual_endpoint_pairing_entry_lower');HU=mat('actual_endpoint_pairing_entry_upper')
 GentryU=mat('actual_D_Gram_entry_upper');GentryL=mat('actual_D_Gram_entry_lower')
 L=4095;O=8191;s=(rat(GentryL[0][0]/(2*B))[0],rat(GentryU[0][0]/(2*B))[1])
 log=(rat(1-HU[0][0]/(2*B))[0],rat(1-HL[0][0]/(2*B))[1])
 harmonic=[Z]
 for n in range(1,2*O+1):harmonic.append(plus(harmonic[-1],rat(F(1,n))))
 dn={n:plus(harmonic[n],s) for n in range(0,O+1,2)}
 diagonal={n:minus(plus(minus(mul(rat(2),harmonic[2*n]),mul(rat(2),harmonic[n])),rat(F(1,2*n+1))),log) for n in range(0,O+1,2)}
 f={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(2,989,2)}
 jobs=list(f);jobs=jobs[::-1] if replay else jobs
 g={};payload=[]
 for n in range(0,L+1,2):
  value=Z
  for m in jobs:
   entry=diagonal[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,f[m]))
  lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  g[n]=center;payload.append(dict(degree=n,center=str(center),radius=str(radius)))
 assert hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()==response['finite_output_polynomial_coefficient_sha256']
 psi={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(990,L+1,2)}
 source=[psi,{n:rat(x) for n,x in g.items()}]
 action=[{},{}];trial=[{},{}];roundEnergy=[F(0)]*2
 for j,u in enumerate(source):
  jobs=list(u);jobs=jobs[::-1] if replay else jobs
  for n in range(0,O+1,2):
   value=Z
   for m in jobs:
    entry=diagonal[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
    value=plus(value,mul(entry,u[m]))
   lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
   action[j][n]=(lo,hi);trial[j][n]=center
   roundEnergy[j]+=up(2*B/F(2*n+1)*F(dn[n][1])*radius*radius,10**100)
  print('RC130 finite action column',j,'complete',flush=True)
 inputTail=F(prior['analytic_tail_base_D_energy_upper']);A=F(prior['analytic_tail_coefficient_domination_constant'])
 outputBase=up(B/(F(plus(harmonic[O-1],s)[0])*(O-2)*(O-1)))
 errors=[];outputTail=[]
 for j,u in enumerate(source):
  total=Z
  for n in (list(u)[::-1] if replay else u):total=plus(total,u[n])
  factor=up(F(total[1])/(1-F((L-1)*L,(O+1)*(O+2))))
  tail=up(outputBase*factor*factor,10**100);outputTail.append(tail)
  errors.append(up(sqrtup(roundEnergy[j])+sqrtup(tail)+(1 if j==0 else A)*sqrtup(inputTail)))
 # Lower H2 entries retain positive finite input/output. Upper entries pay all errors.
 QL=[[F(0)]*2 for _ in range(2)];QU=[[F(0)]*2 for _ in range(2)]
 prefixL=[[F(0)]*2 for _ in range(2)]
 degrees=list(range(0,O+1,2));degrees=degrees[::-1] if replay else degrees
 for i in range(2):
  for j in range(i,2):
   a=b=Z
   for n in degrees:
    mass=mul(rat(2*B/F(2*n+1)),dn[n])
    a=plus(a,mul(mass,rat(trial[i][n]*trial[j][n])))
    b=plus(b,mul(mass,mul((rat(action[i][n][0])[0],rat(action[i][n][1])[1]),(rat(action[j][n][0])[0],rat(action[j][n][1])[1]))))
   QL[i][j],QU[i][j]=bounds(a);prefixL[i][j]=bounds(b)[0]
   QL[j][i]=QL[i][j];QU[j][i]=QU[i][j];prefixL[j][i]=prefixL[i][j]
 norms=[sqrtup(QU[i][i]) for i in range(2)];H2L=prefixL;H2U=[[F(0)]*2 for _ in range(2)]
 for i in range(2):
  for j in range(2):
   e=up(errors[i]*norms[j]+errors[j]*norms[i]+errors[i]*errors[j])
   H2U[i][j]=up(QU[i][j]+e)
   if i==j:H2U[i][j]=min(H2U[i][j],HU[[1,3][i]][[1,3][i]])
   assert H2L[i][j]<=H2U[i][j]
 # G^-1 entry intervals derived from its Loewner enclosure, not inverted entrywise.
 invL=inv(GU);invU=inv(GL);difference=add(invU,invL,-1);assert psd(difference)
 IL=[[F(0)]*4 for _ in range(4)];IU=[[F(0)]*4 for _ in range(4)]
 for i in range(4):
  for j in range(4):
   center=(invL[i][j]+invU[i][j])/2;radius=sqrtup(difference[i][i]*difference[j][j])/2
   IL[i][j]=down(center-radius);IU[i][j]=up(center+radius)
 cols=[1,3];PL=[[F(0)]*2 for _ in range(2)];PU=[[F(0)]*2 for _ in range(2)]
 for i,ci in enumerate(cols):
  for j,cj in enumerate(cols):
   for k in range(4):
    for l in range(4):
     v=imul(imul((HL[ci][k],HU[ci][k]),(IL[k][l],IU[k][l])),(HL[l][cj],HU[l][cj]))
     PL[i][j]+=v[0];PU[i][j]+=v[1]
 # Interval arithmetic preserves symmetry; intersect with residual Gram positivity.
 RL=[[down(H2L[i][j]-PU[i][j]) for j in range(2)] for i in range(2)]
 RU=[[up(H2U[i][j]-PL[i][j]) for j in range(2)] for i in range(2)]
 for i,ci in enumerate(cols):
  RL[i][i]=max(F(0),RL[i][i]);RU[i][i]=min(RU[i][i],GentryU[ci][ci])
 RU[0][0]=min(RU[0][0],F(old['projected_covariance_entry_upper'][1][1]))
 cross=sqrtup(RU[0][0]*RU[1][1]);RL[0][1]=RL[1][0]=max(RL[0][1],RL[1][0],-cross);RU[0][1]=RU[1][0]=min(RU[0][1],RU[1][0],cross)
 assert all(RL[i][j]<=RU[i][j] for i in range(2) for j in range(2))
 # Full four-input covariance: zero P0, paid f0 row, actual remaining block.
 fullL=[[F(0)]*4 for _ in range(4)];fullU=[[F(0)]*4 for _ in range(4)]
 for i,ci in enumerate(cols):
  for j,cj in enumerate(cols):fullL[ci][cj]=RL[i][j];fullU[ci][cj]=RU[i][j]
 fvar=F(response['collective_response_enrichment_budgets'][2]['new_f0_projected_covariance_upper']);fullU[2][2]=fvar
 for i,ci in enumerate(cols):
  e=sqrtup(fvar*RU[i][i]);fullL[2][ci]=fullL[ci][2]=-e;fullU[2][ci]=fullU[ci][2]=e
 weights=[sqrtup(GentryU[i][i]) for i in range(4)];Rlo,Rhi,err=loewner(fullL,fullU,weights);assert psd(Rhi)
 wrel=down(RL[1][1]/GentryU[3][3],10**12)
 # Paid reference Schur upper. Actual complementary I+C lies between I and 2I.
 Hlo=mat('actual_endpoint_pairing_Loewner_lower');Hhi=mat('actual_endpoint_pairing_Loewner_upper')
 Mlow=add(add(GL,Hlo),Rhi,-1);schurAvailable=psd(Mlow)
 schurUpper=None;schurFractions=[];responseLower=mat('reference_inverse_response_Loewner_lower');oldUpper=mat('reference_inverse_response_Loewner_upper')
 if schurAvailable:
  K=inv(Mlow);Gmid=[[(GL[i][j]+GU[i][j])/2 for j in range(4)] for i in range(4)];E=add(GU,GL,-1);E=[[x/2 for x in r] for r in E]
  assert psd(E);trace=sum(E[i][j]*K[j][i] for i in range(4) for j in range(4));assert trace>=0
  t=F(1,1000);main=cong(Gmid,K)
  schurUpper=add([[(1+t)*x for x in r] for r in main],[[(1+1/t)*trace*x for x in r] for r in E])
  assert psd(add(schurUpper,responseLower,-1))
  for i in range(4):
   a=main[i][i];d=trace*E[i][i];optimized=a+d+2*sqrtup(a*d)
   schurFractions.append(dict(source=['P0','psi0','f0','w14'][i],reference_response_over_own_D_Gram_lower=str(down(responseLower[i][i]/GentryU[i][i],10**12)),Schur_matrix_upper=str(up(schurUpper[i][i]/GentryL[i][i],10**12)),coordinate_optimized_Schur_upper=str(up(optimized/GentryL[i][i],10**12)),best_coordinate_upper_from_separate_valid_bounds=str(up(min(optimized,schurUpper[i][i],oldUpper[i][i])/GentryL[i][i],10**12))))
 payload=[dict(degree=n,centers=[str(trial[j][n]) for j in range(2)]) for n in range(0,O+1,2)]
 return dict(milestone='RC130',status='PASS: remaining two-column covariance and complete four-input residual enclosed',starting_commit='8e7e6c5004087a24fe9d95be3777576495edcd37',input_sha256=hs,aperture='11/10',joint_family=['P_0','full infinite psi_0','exact symbolic f_0','RC128 collective w_14'],remaining_action_columns=['Cpsi_0','Cw_14'],input_prefix_cutoff=L,output_prefix_cutoff=O,finite_action_trial_coefficient_sha256=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest(),finite_action_trial_coefficient_count_per_column=len(payload),finite_action_trial_generator='positive endpoint action of psi prefix and RC128 g_hat; even outputs through 8190, 1e-40 rational centers',input_psi_tail_D_energy_upper=str(inputTail),input_w_tail_D_energy_upper=str(up(A*A*inputTail)),finite_action_output_tail_D_energy_upper=list(map(str,outputTail)),finite_action_rounding_D_energy_upper=list(map(str,roundEnergy)),full_action_D_norm_error_upper=list(map(str,errors)),remaining_endpoint_second_moment_entry_lower=ser(H2L),remaining_endpoint_second_moment_entry_upper=ser(H2U),inverse_Gram_entry_lower=ser(IL),inverse_Gram_entry_upper=ser(IU),remaining_projection_Gram_entry_lower=ser(PL),remaining_projection_Gram_entry_upper=ser(PU),remaining_projected_covariance_entry_lower=ser(RL),remaining_projected_covariance_entry_upper=ser(RU),full_projected_covariance_entry_lower=ser(fullL),full_projected_covariance_entry_upper=ser(fullU),full_projected_covariance_Loewner_lower=ser(Rlo),full_projected_covariance_Loewner_upper=ser(Rhi),weighted_covariance_interval_error_diagonal=list(map(str,err)),exact_P0_covariance_row_zero=True,paid_f0_covariance_upper=str(fvar),w14_covariance_over_own_D_Gram_lower=str(wrel),w14_covariance_positive_certified=wrel>0,whole_four_vector_small_variance_target_below_this_lower_impossible=wrel>0,full_remaining_block_and_all_four_input_mixtures_paid=True,reference_Schur_compression_lower=ser(Mlow),positive_reference_Schur_compression_certified=schurAvailable,reference_Schur_response_Loewner_upper=ser(schurUpper) if schurUpper is not None else None,reference_response_coordinate_enclosures=schurFractions,reference_Schur_upper_uses_paid_Gram_uncertainty=True,coordinate_optimized_upper_is_not_a_joint_Loewner_matrix=True,high_accuracy_reference_inverse_completed=False,regular_multiplier_action_evaluated=False,original_Weil_or_augmented_actions_performed=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=3);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC130 PASS: complete residual covariance paid; original Weil and accurate inverse remain open')
