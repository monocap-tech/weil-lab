#!/usr/bin/env python3
"""Original SM40 envelope stop for all Galerkin enrichments containing J470 and the exact dual."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
from math import factorial
from flint import arb,acb,ctx
import flint
import verify_rpb108_sm40_scalar_envelope_geometry as geo
import verify_rpb108_original_two_ray_signed_physical as phy
PIN={'native':'c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60',
 'negative':'a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f',
 'source_stop':'4cc8e320de50918965ce1c47acbf7cdd87747bdb373c6a5da6a2ae1b3b0d8ba2',
 'threshold':'e3b69d753a1da5eca34c190ed5597ccd031aaba9ee511433bdc7b6759b976915'}
B=F(11,10);SUB=16;D=10**24;MD=10**12;LIP=F(132)
def dy(x):
 n,e=x.man_exp();return [str(n),int(e)]
def rat(v):
 n,e=int(v[0]),int(v[1]);return F(n*2**max(e,0),2**max(-e,0))
def ball(v):return [dy(v.mid()),dy(v.rad())]
def bounds(v,den):
 lo=rat(dy(v.lower()))*den;hi=rat(dy(v.upper()))*den
 return [str(F(lo.numerator//lo.denominator,den)),str(F(-(-hi.numerator//hi.denominator),den))]
def square(x):
 l,h=x;return (F(0) if l<=0<=h else min(l*l,h*h),max(l*l,h*h))

def main():
 p=argparse.ArgumentParser()
 for k in PIN:p.add_argument('--'+k.replace('_','-')+'-certificate',required=True)
 p.add_argument('--output',default='artifacts/sm40_original_envelope_method_stop.json');args=p.parse_args();data={};start=time.monotonic()
 for k,sha in PIN.items():
  raw=Path(getattr(args,k+'_certificate')).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha;data[k]=json.loads(raw)
 assert flint.__version__=='0.8.0';ctx.prec=512
 neg=data['negative'];prior=data['source_stop'];h=F(1,1000)
 assert prior['original_physical_J_membership']['both_rays_exact_original_J_membership'] is True
 assert prior['original_physical_J_membership']['original_true_sinh_pole_in_J'] is True and len(prior['rays'])==2
 assert data['threshold']['physical_half_width']=='11/10'
 assert data['threshold']['input_sha256']['native']==PIN['native'] and data['threshold']['input_sha256']['negative']==PIN['negative']
 assert data['native']['original_source_nodes'][0][0]=='37/64'
 target=F(data['threshold']['sufficient_energy_dual_threshold']);assert F(999787,10**6)<target<1
 # First-derivative global bound: arch <=20pi, prime <69, hence |m'|<132.
 prime_d1=4*geo.PI[1]*sum((geo.WEIGHTS[n][1]*geo.SHIFTS[n][1] for n in geo.WEIGHTS),F(0))
 assert prime_d1<69 and 20*F(22,7)+69<LIP
 for n,pn in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]:
  v=arb(pn).log()/arb(n).sqrt();assert v.lower()>arb(str(geo.WEIGHTS[n][0])) and v.upper()<arb(str(geo.WEIGHTS[n][1]))
 assert arb.pi().lower()>arb(str(geo.PI[0])) and arb.pi().upper()<arb(str(geo.PI[1]))
 rays=[];physical=[]
 sh=sum(((B/2)**(2*k+1)/factorial(2*k+1) for k in range(17)),F(0))+(B/2)**35/factorial(35)/(1-(B/2)**2/F(36*37));assert sh<F(3,5)
 for r,(a,b) in zip(prior['rays'],[(12001,16384),(3013,4096)]):
  N=2*B*(a+F(3,5)*b)**2;z=phy.signed_form(a,b)
  qlo,qhi=map(F,bounds(z['signed'],10**6));assert qlo>0
  physical.append(dict(ray=r['ray'],sine=a,pole=b,physical_norm_upper=str(N),native_balls={k:ball(v) for k,v in z.items() if k!='elapsed'},signed_energy_lower=str(qlo),signed_energy_upper=str(qhi),all_physical_identity_checks_passed=True))
  rays.append((a,b,N,qhi))
 cells,mass=geo.build(neg);cap_epsilon=F(0)
 for i,(a,b,w) in enumerate(cells):
  leaf=data['threshold']['leaf_witnesses'][i//4];assert F(leaf['lo'])<=a<b<=F(leaf['hi'])
  cap_epsilon+=2*(b-a)*w*F(leaf['Fourier_squared_operator_upper'])
 wmax=max(w for a,b,w in cells);beta=wmax*cap_epsilon
 assert cap_epsilon<F(data['threshold']['whole_complement_negative_operator_upper']) and cap_epsilon<F(2431,10**11)
 assert sum(geo.taylor_order(F(c['hi'])-F(c['lo']),24)[0] for c in neg['cluster_witnesses'])==890
 pref=4*F(22,7)*B;derivative4=[pref**4*2*B*N for a,b,N,qhi in rays]
 pr=[(arb(pn).log()/arb(n).sqrt(),2*arb.pi()*arb(n).log()) for n,pn in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]]
 cache={};records=[];squares=[]
 def point(q,need_m=False):
  if q not in cache:
   qs=arb(str(q));s,t=phy.fourier_basis(qs);rec=[str(q),bounds(s,D),bounds(t,D),None];cache[q]=len(records);records.append(rec)
   S,T=tuple(map(F,rec[1])),tuple(map(F,rec[2]));squares.append([square((a*S[0]+b*T[0],a*S[1]+b*T[1])) for a,b,N,qhi in rays])
  ix=cache[q]
  if need_m and records[ix][3] is None:
   qs=arb(str(q));m=acb(arb('1/4'),arb.pi()*qs).digamma().real-arb.pi().log()
   for coeff,shift in pr:m-=2*coeff*(shift*qs).cos()
   records[ix][3]=bounds(m,MD)
  return ix
 envlo=[F(0)]*2;envhi=[F(0)]*2;Khi=[F(0)]*2;errors=[F(0)]*2
 for index,(a,b,w) in enumerate(cells):
  for sub in range(SUB):
   l=a+(b-a)*F(sub,SUB);r=a+(b-a)*F(sub+1,SUB);mid=(l+r)/2;width=r-l
   ia,im,ib=point(l),point(mid,True),point(r);mlo=F(records[im][3][0]);ru=min(w,max(F(0),F(1,1000)-mlo+LIP*width/2))
   for k in range(2):
    va,vm,vb=squares[ia][k],squares[im][k],squares[ib][k];fee=width**5*derivative4[k]/2880
    ilo=max(F(0),width*(va[0]+4*vm[0]+vb[0])/6-fee);ihi=width*(va[1]+4*vm[1]+vb[1])/6+fee
    envlo[k]+=2*w*ilo;envhi[k]+=2*w*ihi;Khi[k]+=2*ru*ihi;errors[k]+=2*w*fee
  if index%500==0:print('Complete envelope cell',index,'seconds',round(time.monotonic()-start,1),flush=True)
  if time.monotonic()-start>120:raise RuntimeError('Bounded 120-second complete scalar computation guard')
 out_rays=[]
 for k,(a,b,N,qhi) in enumerate(rays):
  sourcegap=envlo[k]-Khi[k]-qhi;payment=beta*N/h;gap=sourcegap-payment;assert gap>0
  out_rays.append(dict(ray=physical[k]['ray'],envelope_action_lower=str(envlo[k]),envelope_action_upper=str(envhi[k]),true_negative_action_upper=str(Khi[k]),complete_signed_energy_upper=str(qhi),complete_Astar_energy_upper=str(Khi[k]+qhi),source_envelope_minus_Astar_lower=str(sourcegap),whole_infinite_complement_graph_correction_upper=str(payment),uniform_energy_lift_envelope_minus_Astar_lower=str(gap),strict_stop=True))
 result=dict(status='CONDITIONAL_ORIGINAL_SM40_ENVELOPE_ALL_GALERKIN_ENRICHMENTS_STOP',input_sha256=PIN,
  original_source_count=470,original_exact_energy_dual_source_count=470,original_SM40_cells=[[str(v) for v in row] for row in cells],original_SM40_two_sided_mass=str(mass),original_SM40_taylor_columns=890,
  subdivisions_per_SM40_cell=SUB,native_frequency_points=records,frequency_subintervals=len(cells)*SUB,working_precision_bits=512,flint_version=flint.__version__,
  Fourier_interval_quantization_denominator=D,multiplier_interval_quantization_denominator=MD,global_multiplier_derivative_upper=str(LIP),prime_derivative_upper=str(prime_d1),
  fourth_Fourier_square_derivative_uppers=[str(v) for v in derivative4],envelope_Simpson_error_uppers=[str(v) for v in errors],
  physical_signed_form_witnesses=physical,ray_witnesses=out_rays,whole_envelope_complement_upper=str(cap_epsilon),envelope_global_operator_upper=str(wmax),whole_envelope_Q_squared_action_upper=str(beta),complement_Astar_energy_floor=str(h),improved_threshold=str(target),
  full_original_973_leaves_paid=True,all_107_clusters_paid=True,squared_operator_compression_equality_used=False,
  stopped_family='EVERY exact Astar-Galerkin trial containing ORIGINAL J470, and exact Astar^-1 J470; any C>=original SM40 step-envelope, any 0<theta<=1; all corresponding Young tau>0',
  threshold_up_to_one_stopped=True,all_Galerkin_trial_enrichments_containing_J_stopped=True,exact_original_energy_dual_capped_gate_stopped=True,all_Young_parameters_with_same_envelope_stopped=True,original_signed_negative_direction_proved=False,
  energy_graph_true_signed_sign_computed=False,actual_energy_projection_computed=False,full_arch_mixed_matrix_computed=False,original_full_inverse_computed=False,
  other_negative_envelopes_ruled_out=False,all_trial_spaces_ruled_out=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
 path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(result,separators=(',',':'))+'\n')
 print('SM40 WHOLE ENVELOPE / ALL GALERKIN ENRICHMENTS STOP PASS: ALL theta<=1 and Young tau>0 for this envelope; original signed gate OPEN; seconds',round(result['elapsed_seconds'],1))
if __name__=='__main__':main()
