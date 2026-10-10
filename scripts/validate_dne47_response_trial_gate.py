#!/usr/bin/env python3
"""Independent exact route-ceiling, high-frame and residual-algebra controls."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read
from materialize_dne44_joint_sources import run as materialize
from validate_dne34_source_block import boxes,mm

def run(path,output):
 checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def enclose(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 def log(q):
  k=0
  while q>=2:q/=2;k+=1
  def series(q):
   z=(q-1)/(q+1);s=sum(2*z**(2*j+1)/F(2*j+1) for j in range(180));return (s,s+2*z**361/(F(361)*(1-z*z)))
  x,y=series(q),series(F(2));return (x[0]+k*y[0],x[1]+k*y[1])
 def atan(q):
  s=sum((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(65));e=q**131/F(131);return (s-e,s+e)
 c,ch=read(path);check(c['stage']=='DNE47' and c['parent']=='61b896309a4c426a9259290b92dbd039a26f96ef' and c['parity']=='even');inputs=[read(p) for p in c['input_paths']];check([h for _,h in inputs]==c['input_sha256']);prior,a,current,s=[x for x,_ in inputs];check(a['status']==current['status']=='PASS');check(a['certificate_sha256']==inputs[0][1]);cr=next(r for r in current['rows'] if r['parity']=='even');check(cr['input_sha256'][0]==inputs[3][1] and cr['positive_retained_rank']==43 and cr['negative_uniform_comparison_rank']==1)
 x,y=atan(F(1,5)),atan(F(1,239));pi=(16*x[0]-4*y[1],16*x[1]-4*y[0]);pl=F(c['pi_lower']);check(pl==F(314159,100000)<pi[0]);A=F(c['aperture']);top=F(c['universal_positive_region_top_upper']);check(A==F(53,50) and c['retained_cutoff']==112 and top==F(169,10));check((2*A*pl*top)**2>112*113)
 lg=tuple(map(F,c['top_log_interval']));enclose(lg,log(top));r=F(c['prime_norm_lower']);check(r==F(prior['prime_norm_lower'])==F(a['prime_norm_lower'])>0);ceiling=F(c['positive_region_shell_route_ceiling_upper']);check(ceiling==lg[1]-r);target=F(c['full_even_packet_threshold_lower']);check(target==F(next(x for x in prior['rows'] if x['parity']=='even')['critical_uniform_floor_lower'])>ceiling);check(c['remaining_even_packet_cannot_close_by_positive_region_shell_route'] is True)
 pp=output+'.packet';materialize(s['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();check(ph==c['normalized_packet_sha256']==s['normalized_packet_sha256']);cols=c['physical_high_trial_columns'];check(len(cols)==c['physical_high_trial_dimension']==3);raw=[]
 for i,col in enumerate(cols,1):
  p=packet['columns'][i];pairs=[(n,F(v)) for n,v in zip(p['indices'],p['coefficients']) if n>=112 and F(v)];check(col['parent_packet_column']==i);check(col['indices']==[n for n,_ in pairs]);check(all(n>=112 and n%2==0 for n in col['indices']));mass=sum(v*v for _,v in pairs);scale=F(col['rational_normalization']);check(mass==F(col['original_high_mass_squared'])>0 and scale>0 and scale*scale>mass);v=[x/scale for _,x in pairs];check(v==list(map(F,col['coefficients'])));check(0<sum(x*x for x in v)==F(col['exact_mass_squared'])<1);raw.append(dict(zip(col['indices'],v)))
 G=[[sum(x.get(n,F(0))*y.get(n,F(0)) for n in set(x)|set(y)) for y in raw] for x in raw];saved=boxes(c['physical_trial_Gram']);check(saved==[[(x,x) for x in row] for row in G]);pc=c['physical_trial_positive_certificate'];O=boxes(pc['original_matrix']);U=[list(map(F,row)) for row in pc['exact_congruence_U']];check(len(U)==3 and all(len(row)==3 for row in U))
 for i in range(3):
  check(U[i][i]!=0)
  for j in range(3):check(i<=j or U[i][j]==0);enclose(O[i][j],(G[i][j],G[i][j]))
 UI=[[(x,x) for x in row] for row in U];C=mm([list(x) for x in zip(*UI)],mm(O,UI));S=boxes(pc['congruence_matrix']);m=[]
 for i in range(3):
  for j in range(3):enclose(S[i][j],C[i][j])
  margin=S[i][i][0]-sum(max(abs(x),abs(y)) for j,(x,y) in enumerate(S[i]) if j!=i);check(margin==F(pc['Gershgorin_margins'][i])>0);m.append(margin)
 check(min(m)/sum(x*x for row in U for x in row)==F(pc['coefficient_floor_lower'])>0)
 # Exact noncommutative matrix-algebra controls of the residual identity.
 def mul(X,Y):return [[sum(X[i][t]*Y[t][j] for t in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]
 def tr(X):return list(map(list,zip(*X)))
 def plus(X,Y):return [[x+y for x,y in zip(a,b)] for a,b in zip(X,Y)]
 def scale(X,s):return [[s*x for x in row] for row in X]
 L=[[F(2),F(0)],[F(0),F(5)]];Li=[[F(1,2),F(0)],[F(0),F(1,5)]];Y=[[F(0)],[F(1)]];J=[[F(0),F(1,5)]]
 for f in ([[F(1),F(0)],[F(0),F(1)]],[[F(1),F(2)],[F(3),F(1)]]):
  v=mul(Y,J);res=plus(f,scale(mul(L,v),-1));actual=mul(tr(f),mul(Li,f));first=plus(plus(mul(tr(f),v),mul(tr(v),f)),scale(mul(tr(v),mul(L,v)),-1));check(actual==plus(first,mul(tr(res),mul(Li,res))))
  M=mul(tr(f),Y);Q=mul(tr(Y),mul(L,Y));B=mul(tr(f),mul(L,Y));D=mul(tr(mul(L,Y)),mul(L,Y));G0=mul(tr(f),f);E=plus(B,scale(M,-1));W=plus(D,scale(Q,-1));credit=plus(plus(mul(E,J),mul(tr(J),tr(E))),scale(mul(tr(J),mul(W,J)),-1));upper=plus(first,mul(tr(res),res));check(upper==plus(G0,scale(credit,-1)))
 # The optimized identity control closes a genuine failing sufficient budget.
 credit=[[F(0),F(0)],[F(0),F(4,5)]];G0=[[F(1),F(0)],[F(0),F(1)]]
 def budget(N):return plus(plus(N,scale(G0,-1)),credit)
 good=budget([[F(2),F(0)],[F(0),F(1,2)]]);crossing=budget([[F(2),F(0)],[F(0),F(1,10)]]);mixed=budget([[F(2),F(1)],[F(1),F(7,10)]])
 check(F(1,2)-1<0 and good[0][0]>0 and good[1][1]>0);check(crossing[1][1]<0);check(mixed[1][1]>0 and mixed[0][0]*mixed[1][1]-mixed[0][1]**2<0)
 check(c['required_new_projected_source_correlations']==44*3+3*4//2==138);check(c['current_original_high_floor']==current['original_infinite_F112_floor']=='647/1000');check(c['actual_certified_retained_dimension']==current['all_high_positive_retained_dimension']==87 and c['uncovered_retained_dimension']==25)
 for key in ('trial_native_energy_certified','trial_source_Gram_certified','response_upper_established','source_integrals_recomputed','true_high_inverse_evaluated','whole_aperture_positive','RH','Lean'):check(c[key] is False)
 out=dict(stage='DNE47',status='PASS',exact_rational_checks=checks,certificate_path=path,certificate_sha256=ch,input_sha256=c['input_sha256'],positive_region_shell_route_ceiling_upper=str(ceiling),full_even_packet_threshold_lower=str(target),physical_high_trial_dimension=3,trial_geometry_certified=True,residual_identity_controls_passed=True,positive_crossing_and_mixed_controls_passed=True,required_new_projected_source_correlations=138,original_infinite_F112_floor='647/1000',actual_certified_retained_dimension=87,uncovered_retained_dimension=25,response_upper_established=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'checks; shell route excluded; 3 exact high trials prepared',flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('--output',required=True);a=ap.parse_args();run(a.input,a.output)
