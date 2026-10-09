#!/usr/bin/env python3
"""Independent rational audit of the joint source and original signed bound."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json
from materialize_dne35_joint_sources import run as materialize
from validate_dne34_source_block import add,mul,neg,boxes,mm,sum_box

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths,output):
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
  a,ah=read(ap);b,bh=read(bp);comparison,coh=read(cp);par=b['parity'];cert,ch=read(b['certificate_path']);pp=output+'.packet';materialize(b['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();cols=packet['columns'];count=12;check(len(cols)==12);check(a['columns']==b['columns']==list(range(count)));check(a['regular_order']==360 and b['regular_order']==400);check(a['precision']==600 and b['precision']==620);check(b['column_labels']==[f'TS{i}' for i in range(4)]+[f'X{i}' for i in range(8)])
  # Independent native border reconstruction from original As, Ps and frozen J.
  native,nh=read(cert['input_paths'][1]);frame,fh=read(cert['input_paths'][2]);selected,sh=read(native['input_paths'][2]);check([nh,fh]==cert['input_sha256'][1:3]);check(sh==native['input_sha256'][2]);As=boxes(cert['tightened_scaled_T4_native_matrix']);Ps=boxes(cert['tightened_scaled_T4_W52_border']);J=[[(F(v),F(v)) for v in row] for row in frame['frozen_scaled_projection_J']];AJ=mm(As,J);E=[[add(x,neg(y)) for x,y in zip(p,r)] for p,r in zip(Ps,AJ)];U=[[(F(v),F(v)) for v in row[:8]] for row in cert['exact_rational_congruence_U']];cross=mm(E,U);Q=boxes(b['native_block'])
  for i in range(4):
   for j in range(4):encloses(Q[i][j],As[i][j])
   for j in range(8):encloses(Q[i][4+j],cross[i][j]);check(Q[i][4+j]==Q[4+j][i])
  for i in range(8):
   for j in range(8):encloses(Q[4+i][4+j],tuple(map(F,cert['congruence_matrix'][i][j])))
  for row in (a,b):
   check(row['parent']=='75f212e021c28be1094bdcd5b13e084b7f9cb320');check(row['parity']==cert['parity']==par);check(row['certificate_sha256']==ch);check(row['normalized_packet_sha256']==ph);check(row['joint_packet_input_sha256']==packet['input_sha256']);check(row['helper_sha256']==hashlib.sha256(Path('scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest());check(row['native_block']==packet['native_matrix']);check(row['retained_projection_indices']==list(range(par=='odd',112,2)));check(row['polynomial_rounding_grid_digits']==250)
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
  # The unchanged remainder block reproduces DNE34 with no high modes deleted.
  old,oldhash=read(f'notes/data/RPB108_DNE34_{par.upper()}_SOURCE_BLOCK_REPLAY_20261009.json.gz.b64');oldG=boxes(old['original_projected_source_Gram'])
  for i in range(8):
   for j in range(8):check(max(G[4+i][4+j][0],oldG[i][j][0])<=min(G[4+i][4+j][1],oldG[i][j][1]))
  check(comparison['parent']=='75f212e021c28be1094bdcd5b13e084b7f9cb320');check(comparison['input_sha256']==[ah,bh]);kappa=F(comparison['original_high_floor']);check(kappa==F(11,25)==F(frame['original_high_floor']));H=[[add(mul((kappa,kappa),q),neg(g)) for q,g in zip(qr,gr)] for qr,gr in zip(Q,G)];native_floor=positivity(comparison['joint_native_positive_control'],Q)
  v=list(map(F,comparison['exact_failure_trial']));check(len(v)==count and any(v));qt=sum_box(mul((x*y,x*y),Q[i][j]) for i,x in enumerate(v) for j,y in enumerate(v));gt=sum_box(mul((x*y,x*y),G[i][j]) for i,x in enumerate(v) for j,y in enumerate(v));ht=sum_box(mul((x*y,x*y),H[i][j]) for i,x in enumerate(v) for j,y in enumerate(v));encloses(tuple(map(F,comparison['failure_trial_native_energy'])),qt);encloses(tuple(map(F,comparison['failure_trial_source_energy'])),gt);encloses(tuple(map(F,comparison['failure_trial_signed_budget'])),ht);check(F(comparison['failure_trial_native_energy'][0])>0);check(comparison['joint_uniform_floor_failure_proved']==(F(comparison['failure_trial_signed_budget'][1])<0))
  n=comparison['certified_joint_prefix_dimension'];check(4<=n<=12);check(comparison['certified_remainder_prefix_dimension']==n-4);check(comparison['full_joint_signed_budget_passed']==(n==12));check(not(comparison['full_joint_signed_budget_passed'] and comparison['joint_uniform_floor_failure_proved']));floor=positivity(comparison['positive_joint_prefix_certificate'],[r[:n] for r in H[:n]]);check(n>=({'even':7,'odd':6}[par]));ids=native['retained_indices'];minor=[[dict(zip(c['indices'],map(F,c['coefficients']))).get(i,F(0)) for i in ids[:n]] for c in cols[:n]]
  for i in range(n):
   pivot=next(j for j in range(i,n) if minor[j][i]);minor[i],minor[pivot]=minor[pivot],minor[i];check(minor[i][i]!=0)
   for j in range(i+1,n):
    ratio=minor[j][i]/minor[i][i];minor[j]=[x-ratio*y for x,y in zip(minor[j],minor[i])]
  mass=sum(F(c['exact_mass_squared']) for c in cols[:n]);source_trace=sum(G[i][i][1] for i in range(n));check(source_trace>0);schur=floor/kappa;gap=min(schur/(4*(mass+source_trace/kappa**2)),kappa/2);check(gap>0);check(comparison['all_high_positive_retained_rank']==n)
  rows.append(dict(parity=par,primary_sha256=ah,replay_sha256=bh,comparison_sha256=coh,DNE34_remainder_replay_sha256=oldhash,complete_joint_source_entries=144,joint_native_coefficient_floor=str(native_floor),joint_uniform_floor_failure_proved=comparison['joint_uniform_floor_failure_proved'],full_joint_signed_budget_passed=comparison['full_joint_signed_budget_passed'],all_high_positive_retained_rank=n,Schur_coefficient_floor=str(schur),all_high_physical_gap_lower=str(gap)))
 total=sum(r['all_high_positive_retained_rank'] for r in rows);guard=F(1,10**100);minimum=min(F(r['all_high_physical_gap_lower']) for r in rows)
 while guard*10<minimum:guard*=10
 check(0<guard<minimum)
 out=dict(stage='DNE35',status='PASS',exact_rational_checks=checks,rows=rows,all_high_positive_retained_dimension=total,uncovered_retained_dimension=112-total,all_high_physical_gap_guard=str(guard),complete_joint_source_Grams_certified=True,complete_remaining_source_Gram_certified=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'checks; all-high retained rank',total)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs=6);p.add_argument('--output',required=True);a=p.parse_args();run(a.inputs,a.output)
