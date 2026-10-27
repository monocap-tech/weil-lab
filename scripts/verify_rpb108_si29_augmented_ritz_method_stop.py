#!/usr/bin/env python3
"""Original full-SI29 augmented Ritz/cap stopping certificate; NOT odd negativity."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from flint import arb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as m
PIN={'native':'c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60',
 'negative':'a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f',
 'schur':'f1149e27da8a0e1d90e48b8ee0eb8a0a0b8ef51d0910499a7fcd19a082efca07',
 'stop':'4cc8e320de50918965ce1c47acbf7cdd87747bdb373c6a5da6a2ae1b3b0d8ba2'}
def dy(v):return arb((int(v[0]),int(v[1])))
def ball(v):return arb(dy(v[0]),dy(v[1]))
def rat(v):
 n,e=int(v[0]),int(v[1]);return F(n*2**max(e,0),2**max(-e,0))
def rootcap(x):
 assert x>0
 q=F(2)**((x.numerator.bit_length()-x.denominator.bit_length())//2)
 while q*q<x:q*=2
 assert q*q>=x and q*q/4<x
 return q

def main():
 parser=argparse.ArgumentParser()
 for key in PIN:parser.add_argument('--'+key+'-certificate',required=True)
 parser.add_argument('--output',default='artifacts/si29_augmented_ritz_method_stop.json');a=parser.parse_args();data={}
 for key,sha in PIN.items():
  raw=Path(getattr(a,key+'_certificate')).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha;data[key]=json.loads(raw)
 z=data['native'];old=data['negative'];schur=data['schur'];stop=data['stop'];ctx.prec=z['working_precision_bits']
 assert ctx.prec==4096 and m.flint.__version__=='0.8.0'
 assert z['normalized_physical_Schur_upper']=='101/100'
 assert schur['native_input_sha256']==PIN['native']
 assert old['matched_native_physical_projection_sha256']==PIN['native'] and old['schur_input_sha256']==PIN['schur']
 assert stop['status']=='CONDITIONAL_EXACT_ORIGINAL_LOW12_SOURCE_ONLY_METHOD_STOP'
 assert stop['original_physical_J_membership']['both_rays_exact_original_J_membership'] is True
 theta=F(stop['method_test_threshold_exact']);assert theta==F(97,100) and F(stop['same_original_SM40_threshold_exact'])<theta
 h=F(schur['normalized_actual_Astar_energy_Schur_clean_lower']);assert h==F(9,9091)
 nodes=[(F(c),p) for c,p in z['original_source_nodes']];features=[(F(c),F(r),d) for c,r,d in z['feature_definitions']]
 assert len(nodes)==107 and sum(p for c,p in nodes)==469 and len(features)==14 and nodes[0][0]==F(37,64)
 X=arb_mat([[ball(v) for v in row] for row in z['full_physical_projection_coefficient_balls']]);C=arb_mat([[dy(v) for v in row] for row in z['exact_dyadic_feature_transform']])
 Q=arb_mat([[-X[i,j] for j in range(14)] for i in range(470)]+[[arb(int(i==j)) for j in range(14)] for i in range(14)])*C
 terms=[m.source_terms(c,k) for c,p in nodes for k in range(p)]+[m.pole_terms()]+[m.feature_terms(f) for f in features]
 kernel=m.Integrals();start=time.monotonic()
 # Independent entire-power Gram check includes ALL three new first-cluster jets.
 m.independent_series_check([(nodes[0][0],nodes[0][1]+3)]+nodes[1:],features,kernel)
 rows=[];beta=F(0)
 for i,((c,p),r) in enumerate(zip(nodes,old['cluster_witnesses'])):
  lo,hi=F(r['lo']),F(r['hi']);assert c==(lo+hi)/2 and p==r['order'] and int(r['cluster'])==i
  radius=(hi-lo)/2;jets=[];finite=F(0)
  for k in range(p,p+3):
   j=arb_mat([[m.gram(m.source_terms(c,k),t,kernel) for t in terms]])*Q
   scale=(2*kernel.pi)**k/factorial(k);v=[j[0,a]*scale for a in range(14)];vb=[m.ball(x) for x in v]
   norm=sum(((abs(rat(x[0]))+rat(x[1]))**2 for x in vb),F(0));cap=rootcap(norm)
   finite+=radius**k*cap;jets.append(dict(degree=k,vector_balls=vb,exact_box_norm_squared_upper=str(norm),dyadic_norm_upper=str(cap)))
  P=p+2;rem=2*m.B*F(101,100)*(F(44,7)*m.B*radius)**(2*P+2)/factorial(P+1)**2
  packet,young=min(((1+d)*finite**2+(1+1/d)*rem,d) for d in [F(2)**k for k in range(-16,17)])
  M2=F(r['two_sided_squared_height_mass']);beta+=M2*packet
  rows.append(dict(cluster=i,lo=str(lo),hi=str(hi),order=p,jets=jets,finite_norm_upper=str(finite),remainder_squared_upper=str(rem),young_parameter=str(young),packet_squared_upper=str(packet),two_sided_squared_height_mass=str(M2),squared_action_payment=str(M2*packet)))
  if i%25==0:print('Complete negative jet cluster',i,'seconds',round(time.monotonic()-start,2),flush=True)
 assert beta<F(9,400000000) and beta<F(old['exact_squared_multiplier_action_upper'])
 # Exact positive sinh series with geometric tail, proving sinh(B/2)<3/5.
 x=m.B/2;sh=sum((x**(2*k+1)/factorial(2*k+1) for k in range(17)),F(0))+x**35/factorial(35)/(1-x*x/F(36*37))
 assert sh<F(3,5)
 rays=[]
 for r,(alpha,b,label) in zip(stop['rays'],[(12001,16384,'direct_Knegative_selected'),(3013,4096,'SM40_cap_selected')]):
  assert r['ray']==label and r['certified_source_only_method_stop'] is True
  gap=F(r['low_0_12_signed_method_lower'])+theta*(F(r['genuine_original_pole_payment_lower'])-F(r['entire_original_Ao_high12_upper']))
  assert gap==F(r['complete_original_Kminus_minus_97pct_Astar_lower'])>0
  norm=2*m.B*(alpha+F(3,5)*b)**2;payment=beta*norm/(theta*h);remaining=gap-payment
  assert remaining>0
  rays.append(dict(ray=label,original_sine_coefficient=alpha,original_pole_coefficient=b,accepted_original_method_gap_lower=str(gap),physical_norm_squared_upper=str(norm),whole_14_correction_payment_upper=str(payment),augmented_graph_method_gap_lower=str(remaining),strict_augmented_ritz_cap_stop=True))
 result=dict(status='CONDITIONAL_ORIGINAL_FULL_SI29_AUGMENTED_RITZ_CAP_METHOD_STOP',input_sha256=PIN,
  original_source_count=470,actual_continuous_feature_count=14,trial_dimension=484,working_precision_bits=4096,
  original_negative_cluster_count=107,original_negative_leaf_count=973,extra_omitted_jets=2,cluster_witnesses=rows,
  exact_KW_squared_operator_upper=str(beta),clean_KW_squared_operator_upper='9/400000000',
  prior_KW_squared_operator_upper=old['exact_squared_multiplier_action_upper'],
  full_action_improvement_factor=str(F(old['exact_squared_multiplier_action_upper'])/beta),
  physical_W_Gram_upper='101/100',quotient_energy_H_lower=str(h),threshold_ceiling=str(theta),
  sinh_B_over_2_upper=str(sh),ray_witnesses=rays,
  graph_definition='g=f-Wq; q=(W*Astar W)^-1 W*Astar f',
  complete_graph_gap_formula='Kminus(g)-theta Astar(g) >= accepted_gap - beta2*||f||^2/(theta*h)',
  stopped_method='exact Astar Galerkin inverse of J470 in span(J470,F14), any cap C>=Kminus and 0<theta<=97/100',
  supported_operator_square_identified_with_squared_multiplier=False,
  energy_projected_negative_action_assumed_invariant=False,
  original_signed_negative_direction_proved=False,all_trial_spaces_ruled_out=False,
  actual_arch_mixed_matrix_computed=False,actual_energy_projection_computed=False,matched_forcing_computed=False,
  original_W_ODD_NEG_closed=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
 out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
 print('FULL SI29 AUGMENTED RITZ/CAP METHOD STOP PASS; both complete graph gaps strict; W-ODD-NEG OPEN; seconds',round(result['elapsed_seconds'],2),flush=True)
if __name__=='__main__':main()
