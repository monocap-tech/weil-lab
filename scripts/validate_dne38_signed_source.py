#!/usr/bin/env python3
"""Independent rational audit of the joint source and original signed bound."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json
from materialize_dne38_joint_sources import run as materialize
from materialize_dne36_joint_sources import run as materialize_prior
from validate_dne34_source_block import add,mul,neg,boxes,mm,sum_box

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths,output):
 hv,hvh=read('notes/data/RPB108_DNE37_HIGH_FLOOR_VALIDATION_20261010.json');assert hv['status']=='PASS' and hv['original_infinite_F112_floor']=='57/100'
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def encloses(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 def positivity(certificate,expected):
  original=boxes(certificate['original_matrix']);U=[[F(x) for x in row] for row in certificate['exact_congruence_U']];n=len(expected);check(len(U)==n)
  for i in range(n):
   check(U[i][i]!=0)
   for j in range(n):
    check(i<=j or U[i][j]==0);encloses(original[i][j],expected[i][j])
  UI=[[(x,x) for x in row] for row in U];computed=mm([list(x) for x in zip(*UI)],mm(original,UI));saved=boxes(certificate['congruence_matrix']);margins=[]
  for i in range(n):
   for j in range(n):encloses(saved[i][j],computed[i][j])
   margin=saved[i][i][0]-sum(max(abs(x),abs(y)) for j,(x,y) in enumerate(saved[i]) if i!=j);check(margin==F(certificate['Gershgorin_margins'][i]));check(margin>0);margins.append(margin)
  bound=min(margins)/sum(x*x for row in U for x in row);check(F(certificate['coefficient_floor_lower'])==bound and bound>0);return bound
 for ap,bp,cp in zip(paths[::3],paths[1::3],paths[2::3]):
  a,ah=read(ap);b,bh=read(bp);comparison,coh=read(cp);par=b['parity'];cert,ch=read(b['certificate_path']);pp=output+'.packet';materialize(b['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();cols=packet['columns'];count=28;check(len(cols)==28);check(a['columns']==b['columns']==list(range(count)));check(a['regular_order']==360 and b['regular_order']==400);check(a['precision']==600 and b['precision']==620);check(b['column_labels']==[f'TS{i}' for i in range(4)]+[f'X{i}' for i in range(24)])
  # Independent native border reconstruction from original As, Ps and frozen J.
  native,nh=read(cert['input_paths'][1]);frame,fh=read(cert['input_paths'][2]);selected,sh=read(native['input_paths'][2]);check([nh,fh]==cert['input_sha256'][1:3]);check(sh==native['input_sha256'][2]);As=boxes(cert['tightened_scaled_T4_native_matrix']);Ps=boxes(cert['tightened_scaled_T4_W52_border']);J=[[(F(v),F(v)) for v in row] for row in frame['frozen_scaled_projection_J']];AJ=mm(As,J);E=[[add(x,neg(y)) for x,y in zip(p,r)] for p,r in zip(Ps,AJ)];U=[[(F(v),F(v)) for v in row[:24]] for row in cert['exact_rational_congruence_U']];cross=mm(E,U);Q=boxes(b['native_block'])
  for i in range(4):
   for j in range(4):encloses(Q[i][j],As[i][j])
   for j in range(24):encloses(Q[i][4+j],cross[i][j]);check(Q[i][4+j]==Q[4+j][i])
  for i in range(24):
   for j in range(24):encloses(Q[4+i][4+j],tuple(map(F,cert['congruence_matrix'][i][j])))
  prior_path=output+'.prior_packet';materialize_prior(b['certificate_path'],prior_path);prior_packet,prior_hash=read(prior_path);Path(prior_path).unlink();check(cols[:20]==prior_packet['columns']);check([r[:20] for r in packet['native_matrix'][:20]]==prior_packet['native_matrix'])
  check(comparison['stage']=='DNE38')
  for row in (a,b):
   check(row['stage']=='DNE38');check(row['column_labels']==packet['column_labels'])
   check(row['parent']=='f11f94dcd72c2d1a8438bdfbc7e7890b47902088');check(row['parity']==cert['parity']==par);check(row['certificate_sha256']==ch);check(row['normalized_packet_sha256']==ph);check(row['joint_packet_input_sha256']==packet['input_sha256']);check(row['helper_sha256']==hashlib.sha256(Path('scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest());check(row['native_block']==packet['native_matrix']);check(row['retained_projection_indices']==list(range(par=='odd',112,2)));check(row['polynomial_rounding_grid_digits']==250)
   reused,reused_hash=read(row['reused_source_path']);check(reused_hash==row['reused_source_sha256']);check(reused['normalized_packet_sha256']==prior_hash);check(reused['regular_order']==row['regular_order'] and reused['precision']==row['precision']);check(row['reused_joint_dimension']==20 and row['fresh_joint_dimension']==8);check(row['reused_rounded_source_definition_unchanged']);check(reused['column_labels']==row['column_labels'][:20]);check(reused['exact_masses']==row['exact_masses'][:20]);check(reused['physical_norm_upper']==row['physical_norm_upper'][:20]);check(reused['helper_sha256']==row['helper_sha256']);check(reused['certificate_sha256']==row['certificate_sha256'])
   for key in ['retained_rounded_source_coordinates','panel_regular_polynomial_sup_error_upper','logarithmic_polynomial_sup_error_upper','source_L2_error_upper']:
    check(row[key][:20]==reused[key])
   for key in ['complete_rounded_source_Gram','projected_rounded_source_Gram','original_projected_source_Gram','source_Gram_error_payments']:
    check([r[:20] for r in row[key][:20]]==reused[key])
   eta=F(row['uniform_original_source_operator_error_upper']);check(eta>=2*F(53,50)*F(550,19)*F(106,125)**row['regular_order']+F(3,10**99));sq=F(row['physical_interval_sqrt_upper']);ln=F(row['complete_log_norm_upper']);check(sq*sq>=2*F(53,50));check(ln*ln>=F(row['complete_log_squared_norm'][1]));whole=boxes(row['complete_rounded_source_Gram']);coords=boxes(row['retained_rounded_source_coordinates']);projected=boxes(row['projected_rounded_source_Gram']);original=boxes(row['original_projected_source_Gram']);errors=list(map(F,row['source_L2_error_upper']));roots=list(map(F,row['projected_source_norm_upper']));check(len(coords)==count and all(len(v)==56 for v in coords))
   for i,c in enumerate(cols):
    mass=sum(F(v)**2 for v in c['coefficients']);norm=F(c['norm_upper']);check(F(row['exact_masses'][i])==mass==F(c['exact_mass_squared']));check(F(row['physical_norm_upper'][i])==norm);check(norm*norm>mass);rounding=F(row['polynomial_rounding_source_L2_error_upper'][i]);pe=list(map(F,row['panel_regular_polynomial_sup_error_upper'][i]));check(len(pe)==7);check(rounding>=sq*max(pe)+F(row['logarithmic_polynomial_sup_error_upper'][i])*ln/2);check(errors[i]>=eta*norm+rounding);check(roots[i]>0 and roots[i]**2>projected[i][i][1])
    for v in coords[i]:check(v[0]<=v[1])
   for i in range(count):
    for j in range(count):
     check(whole[i][j]==whole[j][i]);check(projected[i][j]==projected[j][i]);check(original[i][j]==original[j][i]);value=add(whole[i][j],neg(sum_box(mul(x,y) for x,y in zip(coords[i],coords[j]))));check(projected[i][j]==value);pay=F(row['source_Gram_error_payments'][i][j]);check(pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]);check(original[i][j]==(value[0]-pay,value[1]+pay))
   for key in ('complete_original_source_action','exact_endpoint_logs','all_six_primes_both_orientations','complete_joint_source_Gram_certified'):check(row[key])
   check(row['half_translation_panels']==7)
   for key in ('sampled_quadrature','complete_remaining_source_Gram_certified','whole_aperture_positive','RH','Lean'):check(row[key] is False)
  A=boxes(a['original_projected_source_Gram']);G=boxes(b['original_projected_source_Gram'])
  for i in range(count):
   for j in range(count):encloses(A[i][j],G[i][j])
  # The unchanged first twenty joint columns reproduce DNE36.
  old,oldhash=read(f'notes/data/RPB108_DNE36_{par.upper()}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');oldG=boxes(old['original_projected_source_Gram'])
  for i in range(20):
   for j in range(20):check(max(G[i][j][0],oldG[i][j][0])<=min(G[i][j][1],oldG[i][j][1]))
  check(comparison['parent']=='f11f94dcd72c2d1a8438bdfbc7e7890b47902088');check(comparison['input_sha256']==[ah,bh]);kappa=F(comparison['original_high_floor']);check(kappa==F(57,100));check(F(frame['original_high_floor'])==F(11,25));hc,hch=read(comparison['high_certificate_path']);check(hch==comparison['high_certificate_sha256']);check(hc['certified_original_F112_lower']==str(kappa));check(any(r['sha256']==hch for r in hv['rows']));H=[[add(mul((kappa,kappa),q),neg(g)) for q,g in zip(qr,gr)] for qr,gr in zip(Q,G)];native_floor=positivity(comparison['joint_native_positive_control'],Q)
  v=list(map(F,comparison['exact_failure_trial']));check(len(v)==count and any(v));qt=sum_box(mul((x*y,x*y),Q[i][j]) for i,x in enumerate(v) for j,y in enumerate(v));gt=sum_box(mul((x*y,x*y),G[i][j]) for i,x in enumerate(v) for j,y in enumerate(v));ht=sum_box(mul((x*y,x*y),H[i][j]) for i,x in enumerate(v) for j,y in enumerate(v));encloses(tuple(map(F,comparison['failure_trial_native_energy'])),qt);encloses(tuple(map(F,comparison['failure_trial_source_energy'])),gt);encloses(tuple(map(F,comparison['failure_trial_signed_budget'])),ht);check(F(comparison['failure_trial_native_energy'][0])>0);check(comparison['joint_uniform_floor_failure_proved']==(F(comparison['failure_trial_signed_budget'][1])<0))
  raw_floor=F(hc['inherited_arch_minus_pole_strict_lower'])-F(hc['rigorous_max_row_ratio_upper']);check(raw_floor==F(comparison['raw_iterated_weight_floor']));check(F(comparison['trial_required_uniform_floor_lower'])==F(comparison['failure_trial_source_energy'][0])/F(comparison['failure_trial_native_energy'][1]));raw_trial=add(mul((raw_floor,raw_floor),tuple(map(F,comparison['failure_trial_native_energy']))),neg(tuple(map(F,comparison['failure_trial_source_energy']))));encloses(tuple(map(F,comparison['raw_weight_floor_trial_signed_budget'])),raw_trial);check(comparison['raw_weight_floor_trial_failure_proved']==(F(comparison['raw_weight_floor_trial_signed_budget'][1])<0))
  n=comparison['certified_joint_prefix_dimension'];check(4<=n<=28);check(comparison['certified_remainder_prefix_dimension']==n-4);check(comparison['full_joint_signed_budget_passed']==(n==28));check(not(comparison['full_joint_signed_budget_passed'] and comparison['joint_uniform_floor_failure_proved']));floor=positivity(comparison['positive_joint_prefix_certificate'],[r[:n] for r in H[:n]]);check(n>=({'even':20,'odd':20}[par]));ids=native['retained_indices'];minor=[[dict(zip(c['indices'],map(F,c['coefficients']))).get(i,F(0)) for i in ids[:n]] for c in cols[:n]]
  obstruction=comparison['first_failing_joint_prefix']
  if n<28:
   check(obstruction['joint_dimension']==n+1);check(obstruction['remainder_dimension']==n-3);w=list(map(F,obstruction['exact_trial']));check(len(w)==n+1 and any(w))
   for name,M in [('native_energy',Q),('source_energy',G),('signed_budget',H)]:
    energy=sum_box(mul((x*y,x*y),M[i][j]) for i,x in enumerate(w) for j,y in enumerate(w));encloses(tuple(map(F,obstruction[name])),energy)
   check(F(obstruction['native_energy'][0])>0);check(F(obstruction['signed_budget'][1])<0);check(obstruction['uniform_floor_failure_proved'])
  else:check(obstruction is None)
  for i in range(n):
   pivot=next(j for j in range(i,n) if minor[j][i]);minor[i],minor[pivot]=minor[pivot],minor[i];check(minor[i][i]!=0)
   for j in range(i+1,n):
    ratio=minor[j][i]/minor[i][i];minor[j]=[x-ratio*y for x,y in zip(minor[j],minor[i])]
  mass=sum(F(c['exact_mass_squared']) for c in cols[:n]);source_trace=sum(G[i][i][1] for i in range(n));check(source_trace>0);schur=floor/kappa;gap=min(schur/(4*(mass+source_trace/kappa**2)),kappa/2);check(gap>0);check(comparison['all_high_positive_retained_rank']==n)
  rows.append(dict(parity=par,primary_sha256=ah,replay_sha256=bh,comparison_sha256=coh,DNE36_joint_replay_sha256=oldhash,complete_joint_source_entries=784,first_failing_joint_prefix_dimension=obstruction['joint_dimension'] if obstruction else None,joint_native_coefficient_floor=str(native_floor),joint_uniform_floor_failure_proved=comparison['joint_uniform_floor_failure_proved'],full_joint_signed_budget_passed=comparison['full_joint_signed_budget_passed'],all_high_positive_retained_rank=n,Schur_coefficient_floor=str(schur),all_high_physical_gap_lower=str(gap)))
 total=sum(r['all_high_positive_retained_rank'] for r in rows);guard=F(1,10**100);minimum=min(F(r['all_high_physical_gap_lower']) for r in rows)
 while guard*10<minimum:guard*=10
 check(0<guard<minimum)
 out=dict(stage='DNE38',status='PASS',exact_rational_checks=checks,high_floor_validation_sha256=hvh,high_floor_rational_checks=hv['exact_rational_checks'],rows=rows,all_high_positive_retained_dimension=total,uncovered_retained_dimension=112-total,all_high_physical_gap_guard=str(guard),complete_joint_source_Grams_certified=True,complete_remaining_source_Gram_certified=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'checks; all-high retained rank',total)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs=6);p.add_argument('--output',required=True);a=p.parse_args();run(a.inputs,a.output)
