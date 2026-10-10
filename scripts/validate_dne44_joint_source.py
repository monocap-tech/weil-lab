#!/usr/bin/env python3
"""Independent rational audit of the joint source and original signed bound."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json
from materialize_dne44_joint_sources import run as materialize
from materialize_dne40_joint_sources import run as materialize_prior
from validate_dne34_source_block import add,mul,neg,boxes,mm,sum_box

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths,output):
 hv,hvh=read('notes/data/RPB108_DNE43_HIGH_FLOOR_VALIDATION_20261010.json');assert hv['status']=='PASS' and hv['original_infinite_F112_floor']=='603/1000'
 prior_validation,pvh=read('notes/data/RPB108_DNE40_SIGNED_SOURCE_VALIDATION_20261010.json');assert prior_validation['status']=='PASS'
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def encloses(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 import ast
 def function_ast(path,name):return ast.dump(next(n for n in ast.parse(Path(path).read_text()).body if isinstance(n,ast.FunctionDef) and n.name==name),include_attributes=False)
 check(function_ast('scripts/certify_dne44_joint_source_Gram.py','packed_conv')==function_ast('scripts/certify_dne40_joint_source_Gram.py','packed_conv'))
 for ap,bp in zip(paths[::2],paths[1::2]):
  a,ah=read(ap);b,bh=read(bp);par=b['parity'];cert,ch=read(b['certificate_path']);pp=output+'.packet';materialize(b['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();cols=packet['columns'];count=44;check(len(cols)==44);check(a['columns']==b['columns']==list(range(count)));check(a['regular_order']==360 and b['regular_order']==400);check(a['precision']==600 and b['precision']==620);check(b['column_labels']==[f'TS{i}' for i in range(4)]+[f'X{i}' for i in range(40)])
  # Independent native border reconstruction from original As, Ps and frozen J.
  native,nh=read(cert['input_paths'][1]);frame,fh=read(cert['input_paths'][2]);selected,sh=read(native['input_paths'][2]);check([nh,fh]==cert['input_sha256'][1:3]);check(sh==native['input_sha256'][2]);As=boxes(cert['tightened_scaled_T4_native_matrix']);Ps=boxes(cert['tightened_scaled_T4_W52_border']);J=[[(F(v),F(v)) for v in row] for row in frame['frozen_scaled_projection_J']];AJ=mm(As,J);E=[[add(x,neg(y)) for x,y in zip(p,r)] for p,r in zip(Ps,AJ)];U=[[(F(v),F(v)) for v in row[:40]] for row in cert['exact_rational_congruence_U']];cross=mm(E,U);Q=boxes(b['native_block'])
  for i in range(4):
   for j in range(4):encloses(Q[i][j],As[i][j])
   for j in range(40):encloses(Q[i][4+j],cross[i][j]);check(Q[i][4+j]==Q[4+j][i])
  for i in range(40):
   for j in range(40):encloses(Q[4+i][4+j],tuple(map(F,cert['congruence_matrix'][i][j])))
  prior_path=output+'.prior_packet';materialize_prior(b['certificate_path'],prior_path);prior_packet,prior_hash=read(prior_path);Path(prior_path).unlink();check(cols[:36]==prior_packet['columns']);check([r[:36] for r in packet['native_matrix'][:36]]==prior_packet['native_matrix'])
  
  for row in (a,b):
   check(row['stage']=='DNE44');check(row['column_labels']==packet['column_labels'])
   check(row['parent']=='5ec8aeeb73fa67eff670e0716a1a752f5d3e64b3');check(row['parity']==cert['parity']==par);check(row['certificate_sha256']==ch);check(row['normalized_packet_sha256']==ph);check(row['joint_packet_input_sha256']==packet['input_sha256']);check(row['helper_sha256']==hashlib.sha256(Path('scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest());check(row['native_block']==packet['native_matrix']);check(row['retained_projection_indices']==list(range(par=='odd',112,2)));check(row['polynomial_rounding_grid_digits']==250)
   reused,reused_hash=read(row['reused_source_path']);check(reused_hash==row['reused_source_sha256']);check(reused['normalized_packet_sha256']==prior_hash);check(reused['regular_order']==row['regular_order'] and reused['precision']==row['precision']);check(row['reused_joint_dimension']==36 and row['fresh_joint_dimension']==8);check(row['reused_rounded_source_definition_unchanged']);check(reused['column_labels']==row['column_labels'][:36]);check(reused['exact_masses']==row['exact_masses'][:36]);check(reused['physical_norm_upper']==row['physical_norm_upper'][:36]);check(reused['helper_sha256']==row['helper_sha256']);check(reused['certificate_sha256']==row['certificate_sha256'])
   for key in ['retained_rounded_source_coordinates','panel_regular_polynomial_sup_error_upper','logarithmic_polynomial_sup_error_upper','source_L2_error_upper']:
    check(row[key][:36]==reused[key])
   for key in ['complete_rounded_source_Gram','projected_rounded_source_Gram','original_projected_source_Gram','source_Gram_error_payments']:
    check([r[:36] for r in row[key][:36]]==reused[key])
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
  # The unchanged first thirty-six joint columns reproduce DNE40.
  old,oldhash=read(f'notes/data/RPB108_DNE40_{par.upper()}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64');oldG=boxes(old['original_projected_source_Gram'])
  for i in range(36):
   for j in range(36):check(max(G[i][j][0],oldG[i][j][0])<=min(G[i][j][1],oldG[i][j][1]))
  inherited=next(r for r in prior_validation['rows'] if r['parity']==par);check(inherited['primary_sha256']==read(a['reused_source_path'])[1]);check(inherited['replay_sha256']==read(b['reused_source_path'])[1])
  rows.append(dict(parity=par,primary_sha256=ah,replay_sha256=bh,complete_joint_source_entries=count*count,reused_joint_dimension=36,fresh_joint_dimension=8,packet_sha256=ph))
 from dne44_integer_moment_dot import integer_dot,outward_moments
 import random
 rng=random.Random(10844)
 for n in (0,1,2,31,111,1101):
  for _ in range(12):
   c=[rng.randrange(-10**80,10**80) for _ in range(n)];m=[]
   for i in range(n):
    v=rng.randrange(-10**90,10**90);m.append((v,v+rng.randrange(10**30)))
   check(integer_dot(c,m)==(sum(min(x*l,x*h) for x,(l,h) in zip(c,m)),sum(max(x*l,x*h) for x,(l,h) in zip(c,m))))
   from types import SimpleNamespace
   raw=[SimpleNamespace(lo=F(l,123),hi=F(h,123)) for l,h in m];grid=10**100;rounded=outward_moments(raw,grid)
   for v,(l,h) in zip(raw,rounded):check(F(l,grid)<=v.lo<=v.hi<=F(h,grid))
   dl,dh=integer_dot(c,rounded);exact_lo=sum(min(x*v.lo,x*v.hi) for x,v in zip(c,raw));exact_hi=sum(max(x*v.lo,x*v.hi) for x,v in zip(c,raw));check(F(dl,grid)<=exact_lo<=exact_hi<=F(dh,grid))
 check({r['parity'] for r in rows}=={'even','odd'})
 out=dict(stage='DNE44',status='PASS',exact_rational_checks=checks,high_floor_validation_sha256=hvh,prior_source_validation_sha256=pvh,rows=rows,complete_joint_source_Grams_certified=True,complete_remaining_source_Gram_certified=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'source checks',flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs=4);p.add_argument('--output',required=True);a=p.parse_args();run(a.inputs,a.output)
