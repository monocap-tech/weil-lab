#!/usr/bin/env python3
"""Independent exact endpoint audit; no floating-point proof decisions."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read
from validate_dne34_source_block import boxes,add,mul,neg,mm,sum_box
from validate_dne43_high_floor import position

def run(path,output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 def positive(c,M):
  O=boxes(c['original_matrix']);U=[list(map(F,r)) for r in c['exact_congruence_U']];n=len(M)
  check(len(O)==len(U)==n and all(len(r)==n for r in O+U))
  for i in range(n):
   check(U[i][i]!=0)
   for j in range(n):
    check(i<=j or U[i][j]==0);enclose(O[i][j],M[i][j])
  UI=[[(x,x) for x in r] for r in U];K=mm([list(x) for x in zip(*UI)],mm(O,UI));S=boxes(c['congruence_matrix']);m=[]
  for i in range(n):
   for j in range(n):enclose(S[i][j],K[i][j])
   d=S[i][i][0]-sum(max(abs(x),abs(y)) for j,(x,y) in enumerate(S[i]) if j!=i)
   check(d==F(c['Gershgorin_margins'][i]) and d>0);m.append(d)
  d=min(m)/sum(x*x for r in U for x in r);check(d==F(c['coefficient_floor_lower']) and d>0)
 c,ch=read(path);check(c['stage']=='DNE45' and c['parent']=='bb7220c07aa66c2fea00bbc36452a59130ee3fb1')
 inputs=[read(p) for p in c['input_paths']];check([h for _,h in inputs]==c['input_sha256']);p,h,a=[x for x,_ in inputs];check(h['status']==a['status']=='PASS')
 hr=next(r for r in h['rows'] if r['path']==c['input_paths'][0]);check(hr['sha256']==inputs[0][1] and hr['all_rows_verified'])
 check(p['prime_powers']==[2,3,4,5,7,8] and p['both_orientations'] and p['aperture']=='53/50')
 check(p['weight']==c['weight']=='P^17 1' and p['weight_power']==17 and c['band_count']==len(p['rows']))
 # Independent exact summation of integrals, without producer outward-sum code.
 numerator=[F(0),F(0)];denominator=[F(0),F(0)];last=(-1,F(1))
 for row in p['rows']:
  left=(row['left'][0],F(row['left'][1]));right=(row['right'][0],F(row['right'][1]));check(left==last);last=right
  lp=position(left);rp=position(right);length=(rp[0]-lp[1],rp[1]-lp[0]);check(length[0]>0)
  w=tuple(map(F,row['weight']));pw=tuple(map(F,row['prime_weight']));check(0<w[0]<=w[1] and 0<pw[0]<=pw[1])
  numerator[0]+=length[0]*w[0]*pw[0];numerator[1]+=length[1]*w[1]*pw[1]
  denominator[0]+=length[0]*w[0]**2;denominator[1]+=length[1]*w[1]**2
 check(last==(1,F(1)))
 sn=tuple(map(F,c['prime_Rayleigh_numerator']));sd=tuple(map(F,c['prime_Rayleigh_denominator']));enclose(sn,numerator);enclose(sd,denominator);check(sn[0]>0 and sd[0]>0)
 ray=F(c['prime_Rayleigh_lower']);r=F(c['prime_norm_lower']);check(ray==sn[0]/sd[1] and 0<r<ray);check(r==F((ray*10**8).__floor__(),10**8))
 alpha=F(c['fixed_arch_input']);check(alpha==F(p['inherited_arch_minus_pole_strict_lower'])==F(h['arch_minus_pole_strict_lower'])==F(2772351243732,10**12))
 ceiling=F(c['scalar_route_ceiling']);check(ceiling==alpha-r)
 rows=[]
 for row in c['rows']:
  s,sh=read(row['source_path']);prior,ph=read(row['prior_certificate_path']);ar=next(x for x in a['rows'] if x['parity']==row['parity'])
  check(sh==row['source_sha256']==ar['input_sha256'][0]);check(ph==row['prior_certificate_sha256']==ar['certificate_sha256']);check(s['parity']==prior['parity']==row['parity'])
  N=boxes(s['native_block']);G=boxes(s['original_projected_source_Gram']);check(len(N)==len(G)==row['packet_dimension']==44 and all(len(x)==44 for x in N+G));positive(prior['joint_native_positive_control'],N)
  v=list(map(F,row['exact_trial']));check(len(v)==44 and any(v))
  def quadratic(M):return sum_box(mul((x*y,x*y),M[i][j]) for i,x in enumerate(v) for j,y in enumerate(v))
  q=quadratic(N);g=quadratic(G);sq=tuple(map(F,row['trial_native_energy']));sg=tuple(map(F,row['trial_source_energy']));enclose(sq,q);enclose(sg,g);check(sq[0]>0 and sg[0]>0)
  lo=F(row['critical_uniform_floor_lower']);hi=F(row['critical_uniform_floor_upper']);check(lo==sg[0]/sq[1]);check(0<hi-lo==F(row['target_bracket_width'])<=F(3,10**8));check(hi*10**8==(hi*10**8).__floor__())
  H=[[add(mul((hi,hi),x),neg(y)) for x,y in zip(nr,gr)] for nr,gr in zip(N,G)];positive(row['full_packet_target_certificate'],H)
  budget=add(mul((ceiling,ceiling),q),neg(g));saved=tuple(map(F,row['ceiling_trial_budget']));enclose(saved,budget);check(saved[1]<0 and lo>ceiling)
  check(F(row['fixed_arch_input_improvement_necessary_lower'])==lo+r-alpha>0)
  rows.append(dict(parity=row['parity'],critical_uniform_floor_lower=str(lo),critical_uniform_floor_upper=str(hi),route_ceiling_strictly_below_threshold=True,ceiling_trial_strictly_negative=True))
 check({r['parity'] for r in rows}=={'even','odd'});check(c['fixed_input_global_norm_route_cannot_close_full_packet'] is True)
 check(c['current_original_high_floor']=='603/1000' and c['actual_certified_retained_dimension']==a['all_high_positive_retained_dimension']==85 and c['uncovered_retained_dimension']==a['uncovered_retained_dimension']==27)
 for key in ('source_integrals_recomputed','target_high_floor_established','true_high_inverse_evaluated','whole_aperture_positive','RH','Lean'):check(c[key] is False)
 out=dict(stage='DNE45',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=ch,input_sha256=c['input_sha256'],prime_norm_lower=str(r),fixed_arch_input=str(alpha),scalar_route_ceiling=str(ceiling),rows=rows,actual_certified_retained_dimension=85,uncovered_retained_dimension=27,source_integrals_recomputed=False,target_high_floor_established=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'new exact checks; fixed-input scalar route obstructed in both parities',flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--output',required=True);a=ap.parse_args();run(a.input,a.output)
