"""RC129: full four-vector Gram, endpoint pairing and reference first moment.
Uses RC128's K=14 collective response; no enlarged covariance/inverse claim.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from validate_rpb108_rc127_enriched_even_endpoint_action import (
 B,Z,rat,plus,minus,mul,div,bounds,down,up,sqrtup,psd,ser,loewner)

def add(A,B,c=F(1)):return [[a+c*b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def transpose(A):return list(map(list,zip(*A)))
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def cong(Y,A):return mm(transpose(Y),mm(A,Y))
def inv(A):
 n=len(A);T=[r[:]+[F(i==j) for j in range(n)] for i,r in enumerate(A)]
 for k in range(n):
  assert T[k][k]!=0;d=T[k][k];T[k]=[x/d for x in T[k]]
  for i in range(n):
   if i!=k:
    d=T[i][k];T[i]=[x-d*y for x,y in zip(T[i],T[k])]
 return [r[n:] for r in T]

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,old,finite,joint=map(json.loads,raw)
 hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [p['milestone'] for p in (prior,old,finite,joint)]==['RC128','RC127','RC126','RC124']
 assert prior['input_sha256']==hs[1:] and old['input_sha256']==hs[2:]
 budget=prior['collective_response_enrichment_budgets'][2];assert budget['retained_tail_highest_order']==14
 eps=F(budget['full_Cf0_approximation_D_norm_error_upper']);jr=joint['parity_actual_joint_endpoint_moment_certificates'][0]
 L=4095;first=L+1;zf=first*(first+1);s=(rat(F(old['D_Gram_Loewner_lower'][0][0])/(2*B))[0],rat(F(old['D_Gram_Loewner_upper'][0][0])/(2*B))[1])
 log=(rat(1-F(old['endpoint_pairing_entry_upper'][0][0])/(2*B))[0],rat(1-F(old['endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
 harmonic=[Z]
 for n in range(1,2*L+1):harmonic.append(plus(harmonic[-1],rat(F(1,n))))
 dn={n:plus(harmonic[n],s) for n in range(0,L+1,2)}
 diagonal={n:minus(plus(minus(mul(rat(2),harmonic[2*n]),mul(rat(2),harmonic[n])),rat(F(1,2*n+1))),log) for n in range(0,L+1,2)}
 f={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(2,989,2)}
 jobs=list(f);jobs=jobs[::-1] if replay else jobs
 g={};coeff=[]
 for n in range(0,L+1,2):
  value=Z
  for m in jobs:
   entry=diagonal[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
   value=plus(value,mul(entry,f[m]))
  lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
  g[n]=center;coeff.append(dict(degree=n,center=str(center),radius=str(radius)))
 assert hashlib.sha256(json.dumps(coeff,sort_keys=True,separators=(',',':')).encode()).hexdigest()==prior['finite_output_polynomial_coefficient_sha256']
 psi={n:div(rat(F(2*n+1,n*(n+1))),dn[n]) for n in range(990,L+1,2)}
 mu=list(map(F,budget['analytic_moment_center_coefficients']));rho=F(prior['tail_geometric_ratio_upper']);assert len(mu)==15 and min(mu)>0
 A=up(sum(mu[k]*rho**k for k in range(15)));T=F(prior['analytic_output_tail_D_Gram_upper'])
 # Actual w=g+analytic tail; supports are D-orthogonal.
 gp=gg=gf=Z
 ns=list(g);order=ns[::-1] if replay else ns
 for n in order:
  mass=mul(rat(2*B/F(2*n+1)),dn[n]);gg=plus(gg,mul(mass,rat(g[n]*g[n])))
  if n in psi:gp=plus(gp,mul(mass,mul(rat(g[n]),psi[n])))
  if n in f:gf=plus(gf,mul(mass,mul(rat(g[n]),f[n])))
 ggl,ggu=bounds(gg);gpl,gpu=bounds(gp);gfl,gfu=bounds(gf)
 GentryL=[[F(0)]*4 for _ in range(4)];GentryU=[[F(0)]*4 for _ in range(4)]
 for i in range(3):GentryL[i][i]=F(old['D_Gram_Loewner_lower'][i][i]);GentryU[i][i]=F(old['D_Gram_Loewner_upper'][i][i])
 GentryL[3][3]=ggl;GentryU[3][3]=up(ggu+A*A*T)
 pairs=[(0,bounds(mul(mul(rat(2*B),s),rat(g[0])))),(1,(gpl,up(gpu+A*T))),(2,(gfl,gfu))]
 for i,(lo,hi) in pairs:GentryL[i][3]=GentryL[3][i]=lo;GentryU[i][3]=GentryU[3][i]=hi
 weights=[sqrtup(GentryU[i][i]) for i in range(4)];GL,GU,Gerror=loewner(GentryL,GentryU,weights)
 gramFloor=[[GentryL[i][i]/1000 if i==j else F(0) for j in range(4)] for i in range(4)]
 assert psd(add(GL,gramFloor,-1))
 print('RC129 full joint D Gram complete',flush=True)
 # Positive finite endpoint sums, followed by all three omitted mixed blocks.
 def kernel(n,m):
  return mul(rat(2*B/F(2*n+1)),diagonal[n]) if n==m else rat(2*B/F(abs(n-m)*(n+m+1)))
 hgg=hpg=Z
 for n in order:
  hgg=plus(hgg,mul(kernel(n,n),rat(g[n]*g[n])))
  for m in order:
   if m>n:hgg=plus(hgg,mul(kernel(n,m),rat(2*g[n]*g[m])))
 for n in (list(psi)[::-1] if replay else psi):
  for m in order:hpg=plus(hpg,mul(kernel(n,m),mul(psi[n],rat(g[m]))))
 Sg=Sp=Z
 for n in order:Sg=plus(Sg,rat(g[n]/(1-F(n*(n+1),zf))))
 for n in (list(psi)[::-1] if replay else psi):Sp=plus(Sp,div(psi[n],rat(1-F(n*(n+1),zf))))
 sg=up(F(Sg[1]));sp=up(F(Sp[1]));hggl,hggu=bounds(hgg);hpgl,hpgu=bounds(hpg)
 HentryL=[[F(0)]*4 for _ in range(4)];HentryU=[[F(0)]*4 for _ in range(4)]
 for i in range(3):
  for j in range(3):HentryL[i][j]=F(old['endpoint_pairing_entry_lower'][i][j]);HentryU[i][j]=F(old['endpoint_pairing_entry_upper'][i][j])
 # h psi/f = D psi/Cf = D psi/w up to the paid RC128 action error.
 pe=up(eps*sqrtup(GentryU[1][1]))
 HentryL[1][2]=HentryL[2][1]=max(HentryL[1][2],down(GentryL[1][3]-pe))
 HentryU[1][2]=HentryU[2][1]=min(HentryU[1][2],up(GentryU[1][3]+pe))
 al=HentryL[0][0]/GentryU[0][0];au=HentryU[0][0]/GentryL[0][0]
 HentryL[0][3]=HentryL[3][0]=down(al*GentryL[0][3]+GentryL[1][3]+GentryL[2][3])
 HentryU[0][3]=HentryU[3][0]=up(au*GentryU[0][3]+GentryU[1][3]+GentryU[2][3])
 HentryL[1][3]=HentryL[3][1]=hpgl
 mixedTail=up(T*(A*sp+sg+A));HentryU[1][3]=HentryU[3][1]=up(hpgu+mixedTail)
 we=up(eps*sqrtup(GentryU[3][3]))
 HentryL[2][3]=HentryL[3][2]=down(GentryL[3][3]-we)
 HentryU[2][3]=HentryU[3][2]=up(GentryU[3][3]+we)
 HentryL[3][3]=hggl;selfTail=up(T*(2*A*sg+A*A));HentryU[3][3]=up(hggu+selfTail)
 assert all(HentryL[i][j]<=HentryU[i][j] for i in range(4) for j in range(4))
 HL,HU,Herror=loewner(HentryL,HentryU,weights)
 assert psd(HL) and psd(add(GL,HU,-1))
 print('RC129 full joint endpoint pairing complete',flush=True)
 # Reference variational trial in this nonorthogonal, overlapping family.
 Gmid=[[ (GL[i][j]+GU[i][j])/2 for j in range(4)] for i in range(4)]
 Hmid=[[ (HL[i][j]+HU[i][j])/2 for j in range(4)] for i in range(4)]
 Y=[[down(x,10**20) for x in row] for row in mm(inv(add(Gmid,Hmid)),Gmid)]
 IminusY=[[F(i==j)-Y[i][j] for j in range(4)] for i in range(4)]
 lower=add(add(GL,cong(IminusY,GU),-1),cong(Y,HU),-1);upper=add(GU,[[x/2 for x in row] for row in HL],-1)
 simple=add([[F(3,4)*x for x in row] for row in GL],[[x/4 for x in row] for row in HU],-1)
 assert psd(lower) and psd(add(upper,lower,-1)) and psd(add(lower,simple,-1))
 return dict(milestone='RC129',status='PASS: full four-vector actual Gram and endpoint first moment, all infinite mixed blocks paid',starting_commit='56a2955125232c11b5fb27d8dc31bec3714c3f90',input_sha256=hs,aperture='11/10',joint_family=['P_0','full infinite psi_0','exact symbolic f_0','RC128 collective w_14'],family_dimension=4,selected_relative_Cf0_action_target='1/1000000000000000000000000',retained_analytic_tail_features=15,finite_prefix_cutoff=L,overlapping_D_supports_retained=True,actual_D_Gram_entry_lower=ser(GentryL),actual_D_Gram_entry_upper=ser(GentryU),actual_D_Gram_Loewner_lower=ser(GL),actual_D_Gram_Loewner_upper=ser(GU),actual_endpoint_pairing_entry_lower=ser(HentryL),actual_endpoint_pairing_entry_upper=ser(HentryU),actual_endpoint_pairing_Loewner_lower=ser(HL),actual_endpoint_pairing_Loewner_upper=ser(HU),weighted_Gram_interval_error_diagonal=list(map(str,Gerror)),weighted_endpoint_interval_error_diagonal=list(map(str,Herror)),analytic_tail_coefficient_domination_constant=str(A),analytic_tail_base_D_energy_upper=str(T),mixed_psi_w_omitted_endpoint_upper=str(mixedTail),w_w_omitted_endpoint_upper=str(selfTail),RC128_Cf0_w_error_paid=str(eps),psi_f_pairing_identity_error_upper=str(pe),f_w_pairing_identity_error_upper=str(we),joint_Gram_positive_and_endpoint_contraction_verified=True,Gram_positive_floor_relative_entry_diagonal='1/1000',Gram_positive_floor_Loewner_matrix=ser(gramFloor),reference_variational_trial_coefficients=ser(Y),reference_inverse_response_Loewner_lower=ser(lower),reference_inverse_response_Loewner_upper=ser(upper),variational_lower_dominates_simple_lower=psd(add(lower,simple,-1)),source_response_over_actual_D_Gram_diagonal_enclosures=[dict(source=['P0','psi0','f0','w14'][i],lower=str(down(lower[i][i]/GentryU[i][i],10**12)),upper=str(up(upper[i][i]/GentryL[i][i],10**12))) for i in range(4)],full_four_vector_first_moment_certified=True,full_four_vector_covariance_evaluated=False,remaining_Cpsi0_and_Cw14_actions_open=True,high_accuracy_reference_inverse_completed=False,regular_multiplier_action_evaluated=False,original_Weil_or_augmented_actions_performed=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=4);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC129 PASS: full four-vector joint first moment paid; remaining action/covariance block open')
