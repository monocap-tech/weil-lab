#!/usr/bin/env python3
"""Independent exact SM40 reconstruction, Simpson/range payments and stop replay."""
import hashlib,json,sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from validate_rpb108_si06_negative_band import PI,WEIGHTS,SHIFTS,YFAC,CONST_UP,prime_interval,log_rational_bounds
from validate_rpb108_si07_negative_support_cover import arch_lower_cell
from functools import lru_cache
PIN={'native':'c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60','negative':'a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f','source_stop':'4cc8e320de50918965ce1c47acbf7cdd87747bdb373c6a5da6a2ae1b3b0d8ba2','threshold':'e3b69d753a1da5eca34c190ed5597ccd031aaba9ee511433bdc7b6759b976915'}
B=F(11,10);KAPPA=F(1,1000)
def plus(x,y):return (x[0]+y[0],x[1]+y[1])
def scale(a,x):return (a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0])
def product(x,y):
 v=[a*b for a in x for b in y];return min(v),max(v)
def sq(x):
 l,h=x;return (F(0) if l<=0<=h else min(l*l,h*h),max(l*l,h*h))
def dy(v):
 n,e=int(v[0]),int(v[1]);return F(n*2**max(e,0),2**max(-e,0))
def native(v):
 m,r=dy(v[0]),dy(v[1]);assert r>=0;return m-r,m+r
@lru_cache(None)
def rational_arch(a):
 y=YFAC*a
 # Independent integer-quarter expression for the same 64-term source.
 head=sum((64*y*y/(F(4*k+1)*((4*k+1)**2+16*y*y)) for k in range(64)),F(0))
 return head+log_rational_bounds(1+(4*y/257)**2)[0]/2-CONST_UP

def weights(neg):
 curvature=8*PI[1]**2*sum((WEIGHTS[n][1]*SHIFTS[n][1]**2 for n in WEIGHTS),F(0));out=[]
 def lift(low):
  need=max(F(0),KAPPA-low);v=(need.numerator*10**6+need.denominator-1)//need.denominator
  return max(F(1,10**6),F(v,10**6))
 for l,r,h in [tuple(map(F,x)) for x in neg['original_leaf_witnesses']]:
  for j in range(4):
   a=l+(r-l)*F(j,4);b=l+(r-l)*F(j+1,4);mid=(a+b)/2
   v0=arch_lower_cell(int(a));v1=rational_arch(a);assert v1>=v0
   # Explicitly reconstruct all THREE old stages, not the producer's simplification.
   w37=min(h+KAPPA,lift(v0+prime_interval(mid)[0]-69*(b-a)/2))
   w39=min(w37,lift(v1+prime_interval(mid)[0]-69*(b-a)/2))
   w40=min(w39,lift(v1+min(prime_interval(a)[0],prime_interval(b)[0])-curvature*(b-a)**2/8))
   assert 0<w40<=h+KAPPA;out.append((a,b,w40))
 return out

def regressions():
 # Simpson's full-width fourth-derivative constant saturates for x^4.
 assert F(2,3)-F(2,5)==F(2**5*factorial(4),2880)
 assert sum(__import__('math').comb(4,j) for j in range(5))==16
 from verify_rpb108_si29_augmented_ritz_method_stop_replay import mm,tr,add,inv,spd
 # Loose envelope E can fail while the TRUE signed A-K is strictly positive.
 G=[[F(2),F(1,4)],[F(1,4),F(3)]];M=[[F(1,50),F(1,100)],[F(1,200),F(1,80)]]
 H=[[F(4),F(1,5)],[F(1,5),F(5)]];A=[G[i]+M[i] for i in range(2)]+[tr(M)[i]+H[i] for i in range(2)]
 N=[[F(1,1000),F(1,2000)],[F(1,3000),F(1,4000)]];EU=[[F(21,10),F(1,4)],[F(1,4),F(2)]];e=F(1,100000)
 EF=[[e,F(0)],[F(0),e]];E=[EU[i]+N[i] for i in range(2)]+[tr(N)[i]+EF[i] for i in range(2)]
 spd(E);spd(add(A,[[x/10 for x in row] for row in E],-1));mu=F(3);spd(add(H,[[mu,F(0)],[F(0),mu]],-1))
 beta=sum(E[i][i] for i in range(4))*e;gap=EU[0][0]-G[0][0];assert gap-beta/mu>0
 for R in (None,[[F(1)],[F(0)]],[[F(1),F(0)],[F(0),F(1)]]):
  if R is None:q=[[F(0)],[F(0)]]
  else:q=mm(R,mm(inv(mm(tr(R),mm(H,R))),mm(tr(R),[[M[0][0]],[M[0][1]]])))
  g=[[F(1)],[F(0)]]+[[-row[0]] for row in q]
  actual=mm(tr(g),mm(add(E,A,-1),g))[0][0];assert actual>=gap-beta/mu>0
 # Young cap C_tau always dominates the same envelope R*R.
 RR=[[F(1),F(1,3)],[F(1,5),F(2)]];D=[[F(1,100),F(-1,200)],[F(1,300),F(1,400)]];R0=add(RR,D)
 e2=sum(x*x for row in D for x in row)
 for tau in (F(1,1024),F(1,8192),F(2)):
  C=[[(1+tau)*v for v in row] for row in mm(tr(R0),R0)]
  for i in range(2):C[i][i]+=(1+1/tau)*e2
  spd(add(C,mm(tr(RR),RR),-1))
 return True

def main():
 z=json.load(open(sys.argv[1]));data={}
 for key,path in zip(PIN,sys.argv[2:]):
  raw=Path(path).read_bytes();assert hashlib.sha256(raw).hexdigest()==z['input_sha256'][key]==PIN[key];data[key]=json.loads(raw)
 assert len(sys.argv)==6 and z['status']=='CONDITIONAL_ORIGINAL_SM40_ENVELOPE_ALL_GALERKIN_ENRICHMENTS_STOP'
 assert z['original_source_count']==z['original_exact_energy_dual_source_count']==470 and z['working_precision_bits']==512 and z['flint_version']=='0.8.0'
 assert z['Fourier_interval_quantization_denominator']==10**24 and z['multiplier_interval_quantization_denominator']==10**12
 assert len(z['physical_signed_form_witnesses'])==len(z['ray_witnesses'])==2
 assert z['subdivisions_per_SM40_cell']==16 and z['frequency_subintervals']==62272
 cells=weights(data['negative']);assert [[str(v) for v in row] for row in cells]==z['original_SM40_cells'] and len(cells)==3892
 mass=sum((2*(b-a)*w for a,b,w in cells),F(0));assert mass==F(z['original_SM40_two_sided_mass'])==F(1073441879,64000000)
 eps=F(0)
 for i,(a,b,w) in enumerate(cells):
  leaf=data['threshold']['leaf_witnesses'][i//4];assert F(leaf['lo'])<=a<b<=F(leaf['hi']);eps+=2*(b-a)*w*F(leaf['Fourier_squared_operator_upper'])
 wmax=max(w for a,b,w in cells);beta=wmax*eps
 assert eps==F(z['whole_envelope_complement_upper'])<F(2431,10**11) and wmax==F(z['envelope_global_operator_upper']) and beta==F(z['whole_envelope_Q_squared_action_upper'])
 assert F(z['complement_Astar_energy_floor'])==KAPPA
 assert F(z['improved_threshold'])==F(data['threshold']['sufficient_energy_dual_threshold'])<1
 d1=4*PI[1]*sum((WEIGHTS[n][1]*SHIFTS[n][1] for n in WEIGHTS),F(0));assert d1==F(z['prime_derivative_upper'])<69 and 20*F(22,7)+69<132==F(z['global_multiplier_derivative_upper'])
 rays=[]
 for r,(alpha,b) in zip(z['physical_signed_form_witnesses'],[(12001,16384),(3013,4096)]):
  assert r['sine']==alpha and r['pole']==b and r['all_physical_identity_checks_passed'] is True
  N=2*B*(alpha+F(3,5)*b)**2;assert N==F(r['physical_norm_upper'])
  balls={k:native(v) for k,v in r['native_balls'].items()}
  arch=plus(plus(product(balls['arch_constant'],balls['norm']),balls['arch_integral']),product(balls['tail'],balls['norm']))
  signed=plus(plus(arch,balls['prime']),scale(-2,sq(balls['pole'])))
  qlo,qhi=F(r['signed_energy_lower']),F(r['signed_energy_upper']);assert 0<qlo<=signed[0]<=signed[1]<=qhi and balls['norm'][1]<=N
  rays.append((alpha,b,N,qhi))
 points={};squares={};mids={}
 for rec in z['native_frequency_points']:
  q=F(rec[0]);assert q not in points;S=tuple(map(F,rec[1]));P=tuple(map(F,rec[2]));assert S[0]<=S[1] and P[0]<=P[1]
  assert all((v*10**24).denominator==1 for v in S+P);points[q]=rec
  squares[q]=[sq(plus(scale(a,S),scale(b,P))) for a,b,N,qhi in rays]
  if rec[3] is not None:
   m=tuple(map(F,rec[3]));assert m[0]<=m[1] and all((v*10**12).denominator==1 for v in m);mids[q]=m
 assert len(points)==124651 and len(mids)==62272
 d4=[(F(88,7)*B)**4*2*B*N for a,b,N,qhi in rays];assert list(map(str,d4))==z['fourth_Fourier_square_derivative_uppers']
 elo=[F(0)]*2;ehi=[F(0)]*2;ku=[F(0)]*2;fees=[F(0)]*2;used=set();usedm=set()
 for a,b,w in cells:
  for j in range(16):
   l=a+(b-a)*F(j,16);r=a+(b-a)*F(j+1,16);mid=(l+r)/2;h=r-l;used.update([l,mid,r]);usedm.add(mid)
   ru=min(w,max(F(0),KAPPA-mids[mid][0]+132*h/2))
   for k in range(2):
    fee=h**5*d4[k]/2880;va,vm,vb=squares[l][k],squares[mid][k],squares[r][k]
    il=max(F(0),h*(va[0]+4*vm[0]+vb[0])/6-fee);ih=h*(va[1]+4*vm[1]+vb[1])/6+fee
    elo[k]+=2*w*il;ehi[k]+=2*w*ih;ku[k]+=2*ru*ih;fees[k]+=2*w*fee
 assert len(used)==len(points) and len(usedm)==len(mids) and list(map(str,fees))==z['envelope_Simpson_error_uppers']
 for i,(r,(a,b,N,qhi)) in enumerate(zip(z['ray_witnesses'],rays)):
  source=elo[i]-ku[i]-qhi;payment=beta*N/KAPPA;left=source-payment
  for key,value in [('envelope_action_lower',elo[i]),('envelope_action_upper',ehi[i]),('true_negative_action_upper',ku[i]),('complete_Astar_energy_upper',ku[i]+qhi),('source_envelope_minus_Astar_lower',source),('whole_infinite_complement_graph_correction_upper',payment),('uniform_energy_lift_envelope_minus_Astar_lower',left)]:assert F(r[key])==value
  assert left>0 and r['strict_stop'] is True
 assert all(z[k] is True for k in ['full_original_973_leaves_paid','all_107_clusters_paid','threshold_up_to_one_stopped','all_Galerkin_trial_enrichments_containing_J_stopped','exact_original_energy_dual_capped_gate_stopped','all_Young_parameters_with_same_envelope_stopped'])
 assert all(z[k] is False for k in ['squared_operator_compression_equality_used','original_signed_negative_direction_proved','energy_graph_true_signed_sign_computed','actual_energy_projection_computed','all_trial_spaces_ruled_out','other_negative_envelopes_ruled_out'])
 assert z['W_ODD_NEG']=='OPEN' and z['inherited_original_domain_review']=='OPEN' and regressions()
 print('INDEPENDENT EXACT ENVELOPE STOP REPLAY PASS: all 3892 weights / 62272 intervals / physical forms / whole-complement lift; all Galerkin enrichments containing J and exact capped gate stopped; original signed gate OPEN')
if __name__=='__main__':main()
