"""RC124: actual joint finite/analytic endpoint pairing and first positive moment.
Two tested parity families only; no original Weil or full tail-family response.
"""
from fractions import Fraction as F
from pathlib import Path
from decimal import Decimal as D,Context,ROUND_FLOOR,ROUND_CEILING
import json,hashlib,argparse
from validate_rpb108_rc119_reference_preconditioned_source_solver import log2_bounds
from validate_rpb108_rc114_positive_augmentation import up,down
from validate_rpb108_rc47_correlated_native_transport import root,serialize
from validate_rpb108_rc31_trial_riesz import psd
from validate_rpb108_rc65_parity_projected_residual_refinement import add,scale
lc=Context(prec=80,rounding=ROUND_FLOOR);hc=Context(prec=80,rounding=ROUND_CEILING)
def rat(q):return lc.divide(D(q.numerator),D(q.denominator)),hc.divide(D(q.numerator),D(q.denominator))
def plus(a,b):return lc.add(a[0],b[0]),hc.add(a[1],b[1])
def minus(a,b):return lc.subtract(a[0],b[1]),hc.subtract(a[1],b[0])
def mul(a,b):return lc.multiply(a[0],b[0]),hc.multiply(a[1],b[1])
def div(a,b):assert a[0]>=0 and b[0]>0;return lc.divide(a[0],b[1]),hc.divide(a[1],b[0])
def bounds(a):return down(F(a[0]),10**50),up(F(a[1]),10**50)

def run(paths,replay=False):
 raw=[Path(p).read_bytes() for p in paths];prior,tail,metric,prec=map(json.loads,raw);hs=[hashlib.sha256(x).hexdigest() for x in raw]
 assert [x['milestone'] for x in [prior,tail,metric,prec]]==['RC123','RC122','RC121','RC56'] and prior['input_sha256']==[hs[1],hs[2],hs[3]]
 B=F(11,10);ll,lh=log2_bounds(replay);cl,ch=map(F,prec['actual_constant_enclosure']);sl=F(789,125)+cl+ll;sh=F(789,125)+ch+lh;assert sl>2*lh
 s=(rat(sl)[0],rat(sh)[1]);log=(rat(ll)[0],rat(lh)[1]);zero=(D(0),D(0));two=rat(F(2));rows=[]
 for t in tail['parity_signed_endpoint_tail_certificates']:
  odd=t['parity']=='odd';p=int(odd);M=t['finite_output_cutoff'];Rh=M+2048;gexp=1
  while 2**gexp<=Rh:gexp+=1
  Rg=2**gexp-1
  H=[zero]
  for n in range(1,max(2*Rh,Rg)+1):H.append(plus(H[-1],rat(F(1,n))))
  psi={};gpre=qpre=bpre=zero;degree_list=list(range(M+1,Rg+1));
  if replay:degree_list.reverse()
  for n in degree_list:
   if n%2!=p:continue
   z=n*(n+1);dn=plus(H[n],s);v=div(rat(F(2*n+1,z)),dn);psi[n]=v
   gpre=plus(gpre,div(rat(2*B*F(2*n+1,z*z)),dn));qpre=plus(qpre,div(rat(2*B*F(2*n+1,z*z)),mul(dn,dn)));bpre=plus(bpre,mul(rat(2*B/F(z-p*(p+1))),v))
  gpl,gph=bounds(gpre);qpl,qph=bounds(qpre);bpl,bph=bounds(bpre)
  blocks=[];gtl=gth=qtl=F(0)
  for j in range(gexp,gexp+24):
   first=2**j+p;last=2**(j+1)-(2-p);lo=F(1,2)*(F(1,first*(first+1))-F(1,(last+2)*(last+3)));hi=F(1,2)*(F(1,(first-2)*(first-1))-F(1,last*(last+1)))
   dl=sl+j*ll;dh=sh+1+(j+1)*lh;gl=down(2*B*lo/dh,10**50);gh=up(2*B*hi/dl,10**50);ql=down(2*B*lo/(dh*dh),10**50);blocks.append((gl,gh,ql))
  if replay:blocks.reverse()
  for gl,gh,ql in blocks:gtl+=gl;gth+=gh;qtl+=ql
  first=2**(gexp+24)+p;remaining=up(B/((sl+(gexp+24)*ll)*(first-2)*(first-1)),10**50);gth+=remaining
  Glo=down(gpl+gtl,10**40);Ghi=up(gph+gth,10**40);Qlo=qpl+qtl
  zl=(Rg+1)*(Rg+2);mixedlo=down(bpl+gtl,10**40);mixedhi=up(bph+gth/(1-F(p*(p+1),zl)),10**40)
  if not odd:assert mixedlo==Glo and mixedhi==Ghi
  ns=[n for n in range(M+1,Rh+1) if n%2==p];E=zero
  jobs=ns[::-1] if replay else ns
  for n in jobs:
   diag=minus(plus(minus(mul(two,H[2*n]),mul(two,H[n])),rat(F(1,2*n+1))),log);assert diag[0]>0
   E=plus(E,mul(rat(2*B/F(2*n+1)),mul(diag,mul(psi[n],psi[n]))))
  pairs=[(i,j) for i,n in enumerate(ns) for j in range(i+1,len(ns))]
  if replay:pairs.reverse()
  for i,j in pairs:
   n,m=ns[i],ns[j];E=plus(E,mul(rat(4*B/F((m-n)*(m+n+1))),mul(psi[n],psi[m])))
  Elo,Ehi=bounds(E)
  # All omitted coefficients positive: prefix is a genuine lower for tail endpoint energy.
  # h <= J+2log2 = D-(s-2log2) I yields the full correlated diagonal upper.
  HpLo=down(Elo,10**40);HpHi=up(Ghi-(sl-2*lh)*Qlo,10**40);assert 0<HpLo<HpHi<Ghi
  mass=2*B/F(2*p+1);hp=F(p);dconst=F(1) if p==0 else F(4,3);h00lo=mass*(dconst-lh);h00hi=mass*(dconst-ll);g00lo=mass*(hp+sl);g00hi=mass*(hp+sh)
  entryL=[[h00lo,mixedlo],[mixedlo,HpLo]];entryU=[[h00hi,mixedhi],[mixedhi,HpHi]];center=[[(entryL[i][j]+entryU[i][j])/2 for j in range(2)] for i in range(2)];width=[[(entryU[i][j]-entryL[i][j])/2 for j in range(2)] for i in range(2)]
  weight=root(g00hi/Glo,10**6);err0=width[0][0]+weight*width[0][1];err1=width[1][1]+width[0][1]/weight;err=[[err0,F(0)],[F(0),err1]];HL=add(center,err,-1);HU=add(center,err);G0L=[[g00lo,F(0)],[F(0),Glo]];G0U=[[g00hi,F(0)],[F(0),Ghi]];G1L=add(G0L,HU,-1);G1U=add(G0U,HL,-1)
  assert psd(HL) and psd(G1L) and psd(add(HU,HL,-1)) and psd(add(G1U,G1L,-1))
  SigL=add(scale(G0L,F(3,4)),scale(HU,F(-1,4)));SigU=add(G0U,scale(HL,F(-1,2)));assert psd(SigL) and psd(add(SigU,SigL,-1))
  assert SigL[1][1]>Ghi/2 and SigU[1][1]<Glo
  rows.append(dict(parity=t['parity'],joint_family=['physical Legendre P_'+str(p),'actual leading analytic tail psi_0'],tail_cutoff=M,endpoint_energy_prefix_degree=Rh,Gram_and_mixed_prefix_degree=Rg,explicit_endpoint_energy_prefix_coefficient_count=len(ns),positive_dyadic_Gram_tail_blocks=24,infinite_Gram_last_remainder_upper=str(remaining),analytic_tail_D_norm_squared_lower=str(Glo),analytic_tail_D_norm_squared_upper=str(Ghi),analytic_tail_physical_norm_squared_lower=str(down(Qlo,10**40)),actual_analytic_tail_endpoint_energy_lower=str(HpLo),actual_analytic_tail_endpoint_energy_upper=str(HpHi),mixed_endpoint_pairing_lower=str(mixedlo),mixed_endpoint_pairing_upper=str(mixedhi),even_mixed_equals_tail_Gram_proved=not odd,endpoint_pairing_entry_lower=serialize(entryL),endpoint_pairing_entry_upper=serialize(entryU),endpoint_pairing_Loewner_lower=serialize(HL),endpoint_pairing_Loewner_upper=serialize(HU),Gamma_0_Loewner_lower=serialize(G0L),Gamma_0_Loewner_upper=serialize(G0U),Gamma_1_Loewner_lower=serialize(G1L),Gamma_1_Loewner_upper=serialize(G1U),joint_reference_response_Loewner_lower=serialize(SigL),joint_reference_response_Loewner_upper=serialize(SigU),weighted_interval_error_diagonal=serialize(err),positive_joint_endpoint_lower_and_first_moment_lower_verified=True,reference_tail_response_over_Gram_fraction_lower=str(down(SigL[1][1]/Ghi,10**12)),reference_tail_response_over_Gram_fraction_upper=str(up(SigU[1][1]/Glo,10**12)),full_infinite_output_paid=True))
 return dict(milestone='RC124',status='PASS: actual mixed finite/analytic endpoint matrices and first positive moment certified',input_sha256=hs,aperture='11/10',arithmetic='80-digit directed positive endpoint sums; exact rational dyadic tails and weighted Loewner acceptance',parity_actual_joint_endpoint_moment_certificates=rows,actual_joint_endpoint_pairing_evaluated=True,actual_Gamma_1_sandwich_evaluated=True,actual_reference_response_first_moment_sandwich_certified=True,joint_family_dimension_per_parity=2,all_39_analytic_tail_columns_certified=False,high_accuracy_reference_response_completed=False,higher_endpoint_response_moments_evaluated=False,regular_multiplier_action_evaluated=False,canonical_Riesz_iteration_performed=False,original_Weil_or_augmented_actions_performed=False,auxiliary_response_norm_below_one_certified=False,new_positive_native_directions_certified=0,original_count_below_one_hundredth_lower=10,original_count_below_one_hundredth_upper=639,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=4);a=p.parse_args();c=run(a.inputs,a.replay)
 if a.replay:assert json.loads(Path(a.output).read_text())==c
 else:Path(a.output).write_text(json.dumps(c,sort_keys=True,indent=2)+'\n')
 print('RC124 PASS: actual joint endpoint pairing and first response moment; full-family/higher moments open')
