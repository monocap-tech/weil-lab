#!/usr/bin/env python3
"""Independent rational replay checks for DNE33 complete source diagonals."""
from pathlib import Path
from fractions import Fraction as F
import base64,gzip,hashlib,json,argparse
from materialize_dne32_normalized_sources import run as materialize

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()

def run(paths,output):
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 for primary_path,replay_path in zip(paths[::2],paths[1::2]):
  a,ah=read(primary_path);b,bh=read(replay_path);par=a['parity'];cert,ch=read(a['certificate_path']);packet_path=output+'.packet';materialize(a['certificate_path'],packet_path);packet,ph=read(packet_path);Path(packet_path).unlink();col=packet['columns'][a['column']]
  check(a['parent']==b['parent']=='c392b8eb26f54734d6bfcab77e3f6e85397fff9b');check(a['parity']==b['parity']==cert['parity']);check(a['column']==b['column']==0)
  check(a['regular_order']==360 and b['regular_order']==400);check(a['precision']==600 and b['precision']==620)
  check(a['certificate_sha256']==b['certificate_sha256']==ch);check(a['normalized_packet_sha256']==b['normalized_packet_sha256']==ph)
  check(a['helper_sha256']==b['helper_sha256']==hashlib.sha256(Path('scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest())
  mass=sum(F(v)**2 for v in col['coefficients']);norm=F(col['norm_upper']);check(mass==F(col['exact_mass_squared']));check(norm*norm>mass)
  credit=F(11,100) if par=='even' else F(7,50);C=list(map(F,cert['congruence_matrix'][0][0]));check(C[0]>0)
  for r in (a,b):
   check(F(r['exact_mass_squared'])==mass);check(F(r['norm_upper'])==norm);check(r['native_diagonal']==cert['congruence_matrix'][0][0]);check(F(r['source_credit'])==credit)
   check(F(r['proposed_source_budget_upper'])==credit*C[1]/2)
   eta=F(2)*F(53,50)*F(550,19)*F(106,125)**r['regular_order']+F(3,10**99)
   check(F(r['uniform_original_source_operator_error_upper'])>=eta);pay=F(r['coordinate_error_payment']);check(pay>=F(r['uniform_original_source_operator_error_upper'])*norm+F(r['polynomial_rounding_source_L2_error_upper']));check(r['polynomial_rounding_grid_digits']==250)
   check([x['index'] for x in r['high_source_probes']]==list(range(112+(par=='odd'),181,2)))
   total=F(0)
   for x in r['high_source_probes']:
    n=x['index'];check(n>=112 and n%2==(par=='odd'))
    tr=list(map(F,x['truncated_coordinate']));v=list(map(F,x['original_coordinate']));check(tr[0]<=tr[1]);check(v==[tr[0]-pay,tr[1]+pay]);dist=max(F(0),v[0],-v[1]);check(F(x['squared_coordinate_lower'])==dist*dist);total+=dist*dist
   check(F(r['finite_Bessel_source_squared_lower'])==total);check(r['source_matrix_bound_failure_proved']==(total>credit*C[1]/2));check(F(r['uniform_high_floor'])==F(11,25));check(F(r['uniform_floor_budget_upper'])==F(11,25)*C[1]);check(r['uniform_floor_source_comparison_failure_proved']==(total>F(11,25)*C[1]))
   best=max(r['high_source_probes'],key=lambda x:F(x['squared_coordinate_lower']));check(r['strongest_single_probe']==best['index']);check(r['single_probe_failure_proved']==(F(best['squared_coordinate_lower'])>credit*C[1]/2))
   check(r['retained_projection_indices']==list(range(par=='odd',112,2)));check(len(r['retained_rounded_source_coordinates'])==56)
   rl,rh=map(F,r['complete_rounded_source_norm_squared'])
   for box in r['retained_rounded_source_coordinates']:
    x,y=map(F,box);check(x<=y);rl-=max(x*x,y*y);rh-=F(0) if x<=0<=y else min(x*x,y*y)
   check(list(map(F,r['projected_rounded_source_norm_squared']))==[rl,rh]);check(F(r['physical_interval_sqrt_upper'])**2>=2*F(53,50));check(F(r['complete_log_norm_upper'])**2>=F(r['complete_log_squared_norm'][1]));check(len(r['panel_regular_polynomial_sup_error_upper'])==7);check(F(r['polynomial_rounding_source_L2_error_upper'])>=F(r['physical_interval_sqrt_upper'])*max(map(F,r['panel_regular_polynomial_sup_error_upper']))+F(r['logarithmic_polynomial_sup_error_upper'])*F(r['complete_log_norm_upper'])/2)
   lo,hi=map(F,r['projected_rounded_source_norm_squared']);root=F(r['projected_source_norm_upper']);gp=F(r['source_Gram_error_payment']);check(0<lo<=hi);check(root>0 and root*root>hi);check(gp>=2*pay*root+pay*pay);ol,oh=map(F,r['original_projected_source_norm_squared']);check((ol,oh)==(lo-gp,hi+gp));check(total<=oh);check(oh<credit*C[0]/2);check(r['source_diagonal_budget_passed'])
   for key in ('complete_original_source_action','exact_endpoint_logs','all_six_primes_both_orientations'):check(r[key])
   check(r['half_translation_panels']==7)
   for key in ('sampled_quadrature','complete_source_Gram_certified','whole_aperture_positive','RH','Lean'):check(r[key] is False)
  for x,y in zip(a['high_source_probes'],b['high_source_probes']):
   check(x['index']==y['index']);lo,hi=map(F,x['original_coordinate']);l,h=map(F,y['original_coordinate']);check(lo<=l<=h<=hi)
  al,ahigh=map(F,a['original_projected_source_norm_squared']);bl,bhigh=map(F,b['original_projected_source_norm_squared']);check(al<=bl<=bhigh<=ahigh)
  frame,fh=read(cert['input_paths'][2]);check(fh==cert['input_sha256'][2]);kappa=F(frame['original_high_floor']);q=F(frame['native_scaled_identity_lower']);eps=credit/(4*kappa);r=credit/2;check(kappa==F(11,25));check(q>0 and credit==F(frame['optimized_T4_source_credit']));check(F(cert['native_mixed_dual_border_squared_upper'])<eps*eps);schur=(credit-r)/kappa-eps;check(schur==credit/(4*kappa) and schur>0)
  native,nh=read(cert['input_paths'][1]);check(nh==cert['input_sha256'][1]);selected,sh=read(native['input_paths'][2]);check(sh==native['input_sha256'][2]);ids=native['retained_indices'];trial=[{ids[0]:F(1)}]+[dict(zip(t['indices'],map(F,t['coefficients']))) for t in selected['columns']]+[dict(zip(col['indices'],map(F,col['coefficients'])))];minor=[[v.get(n,F(0)) for n in ids[:5]] for v in trial]
  for i in range(5):
   pivot=next(j for j in range(i,5) if minor[j][i]);minor[i],minor[pivot]=minor[pivot],minor[i];check(minor[i][i]!=0)
   for j in range(i+1,5):
    ratio=minor[j][i]/minor[i][i];minor[j]=[x-ratio*y for x,y in zip(minor[j],minor[i])]
  M=2*(F(cert['exact_total_scaled_tested_physical_mass'])/q+mass/C[0]);physical_gap=min(schur/(4*(M+(kappa-credit+r)/(kappa*kappa))),kappa/2);check(physical_gap>0)
  rows.append(dict(parity=par,primary_sha256=ah,replay_sha256=bh,strongest_single_probe=b['strongest_single_probe'],finite_Bessel_source_squared_lower=b['finite_Bessel_source_squared_lower'],proposed_source_budget_upper=b['proposed_source_budget_upper'],original_projected_source_norm_squared=b['original_projected_source_norm_squared'],source_diagonal_budget_passed=True,new_retained_rank_with_all_F112=5,original_high_floor=str(kappa),native_border_allocation=str(eps),Schur_energy_lower=str(schur),all_high_physical_gap_lower=str(physical_gap)))
 guard=F(3,10**38);check(all(F(row['all_high_physical_gap_lower'])>guard for row in rows))
 out=dict(all_high_physical_gap_guard=str(guard),stage='DNE33',status='PASS',exact_rational_checks=checks,rows=rows,certified_complete_source_diagonals=2,remaining_source_diagonals=102,all_high_positive_retained_dimension=10,uncovered_retained_dimension=102,all_mixed_source_entries_certified=False,complete_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'rational checks')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs=4);p.add_argument('--output',required=True);a=p.parse_args();run(a.inputs,a.output)
