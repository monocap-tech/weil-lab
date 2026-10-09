#!/usr/bin/env python3
"""Independent rational projection, Gram transfer, budget and all-high audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json,random
from materialize_dne32_normalized_sources import run as materialize
from certify_dne34_source_block import packed_conv

def read(p):
 b=Path(p).read_bytes()
 if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest()
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):
 v=[x*y for x in a for y in b];return (min(v),max(v))
def neg(a):return (-a[1],-a[0])
def boxes(M):return [[tuple(map(F,v)) for v in row] for row in M]
def mm(A,B):return [[sum_box(mul(x,y) for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def sum_box(xs):
 out=(F(0),F(0))
 for x in xs:out=add(out,x)
 return out

def run(paths,output):
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def encloses(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 rng=random.Random(10834)
 for n,m,bits in [(1,1,0),(1,6,20),(8,7,40),(31,27,120),(120,110,1000)]:
  for _ in range(8):
   a=[rng.randrange(-(1<<bits),1<<bits) for i in range(n)];b=[rng.randrange(-(1<<bits),1<<bits) for i in range(m)];expected=[sum(a[i]*b[k-i] for i in range(n) if 0<=k-i<m) for k in range(n+m-1)];check(packed_conv(a,b)==expected)
 for ap,bp,comparison_path in zip(paths[::3],paths[1::3],paths[2::3]):
  a,ah=read(ap);b,bh=read(bp);comparison,coh=read(comparison_path);par=b['parity'];count=len(b['columns']);cert,ch=read(b['certificate_path']);pp=output+'.packet';materialize(b['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();cols=packet['columns'][:count];check(a['columns']==b['columns']==list(range(count)));check(count==8);check(a['regular_order']==360 and b['regular_order']==400);check(a['precision']==600 and b['precision']==620)
  for row in (a,b):
   check(row['parent']=='f1c9f51985a11e4d5d34b92ff83a2b9240a98f9b');check(row['parity']==cert['parity']==par);check(row['certificate_sha256']==ch);check(row['normalized_packet_sha256']==ph);check(row['helper_sha256']==hashlib.sha256(Path('scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest());check(row['native_block']==[[cert['congruence_matrix'][i][j] for j in range(count)] for i in range(count)]);check(row['retained_projection_indices']==list(range(par=='odd',112,2)));check(row['polynomial_rounding_grid_digits']==250)
   eta=F(row['uniform_original_source_operator_error_upper']);check(eta>=2*F(53,50)*F(550,19)*F(106,125)**row['regular_order']+F(3,10**99));sq=F(row['physical_interval_sqrt_upper']);ln=F(row['complete_log_norm_upper']);check(sq*sq>=2*F(53,50));check(ln*ln>=F(row['complete_log_squared_norm'][1]));whole=boxes(row['complete_rounded_source_Gram']);coords=boxes(row['retained_rounded_source_coordinates']);projected=boxes(row['projected_rounded_source_Gram']);original=boxes(row['original_projected_source_Gram']);errors=list(map(F,row['source_L2_error_upper']));roots=list(map(F,row['projected_source_norm_upper']))
   check(len(coords)==count and all(len(v)==56 for v in coords))
   for i,c in enumerate(cols):
    mass=sum(F(v)**2 for v in c['coefficients']);norm=F(c['norm_upper']);check(F(row['exact_masses'][i])==mass==F(c['exact_mass_squared']));check(F(row['physical_norm_upper'][i])==norm);check(norm*norm>mass);rounding=F(row['polynomial_rounding_source_L2_error_upper'][i]);pe=list(map(F,row['panel_regular_polynomial_sup_error_upper'][i]));check(len(pe)==7);check(rounding>=sq*max(pe)+F(row['logarithmic_polynomial_sup_error_upper'][i])*ln/2);check(errors[i]>=eta*norm+rounding);check(roots[i]>0 and roots[i]**2>projected[i][i][1])
    for v in coords[i]:check(v[0]<=v[1])
   for i in range(count):
    for j in range(count):
     check(whole[i][j]==whole[j][i]);check(projected[i][j]==projected[j][i]);check(original[i][j]==original[j][i]);value=add(whole[i][j],neg(sum_box(mul(x,y) for x,y in zip(coords[i],coords[j]))));check(projected[i][j]==value);pay=F(row['source_Gram_error_payments'][i][j]);check(pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]);check(original[i][j]==(value[0]-pay,value[1]+pay))
   for key in ('complete_original_source_action','exact_endpoint_logs','all_six_primes_both_orientations'):check(row[key])
   check(row['half_translation_panels']==7)
   for key in ('sampled_quadrature','complete_remaining_source_Gram_certified','whole_aperture_positive','RH','Lean'):check(row[key] is False)
  A=boxes(a['original_projected_source_Gram']);G=boxes(b['original_projected_source_Gram']);C=boxes(b['native_block'])
  for i in range(count):
   for j in range(count):encloses(A[i][j],G[i][j])
  # DNE33 control: the common-grid source calculation reproduces its pilot.
  d33,h33=read(f'notes/data/RPB108_DNE33_{par.upper()}_SOURCE_DIAGONAL_REPLAY_20261009.json.gz.b64');pilot=tuple(map(F,d33['original_projected_source_norm_squared']));check(max(pilot[0],G[0][0][0])<=min(pilot[1],G[0][0][1]))
  check(comparison['input_sha256']==[ah,bh]);check(comparison['native_certificate_sha256']==ch);credit=F(b['source_credit']);check(credit==F(comparison['tested_source_credit']));kappa=F(comparison['original_high_floor']);check(kappa==F(11,25));eps=F(comparison['native_dual_border_upper']);dual=F(cert['native_mixed_dual_border_squared_upper']);check(F(comparison['native_dual_border_squared_upper'])==dual);check(eps>0 and eps*eps>dual)
  check([F(x['source_budget']) for x in comparison['source_budget_controls']]==[credit/2,credit]);check(all(x['failure_proved'] for x in comparison['source_budget_controls']))
  for control in comparison['source_budget_controls']:
   v=list(map(F,control['exact_trial']));check(len(v)==count and any(v));r=F(control['source_budget']);energy=sum_box(mul((x*y,x*y),C[i][j]) for i,x in enumerate(v) for j,y in enumerate(v));source=sum_box(mul((x*y,x*y),G[i][j]) for i,x in enumerate(v) for j,y in enumerate(v));budget=sum_box(mul((x*y,x*y),add(mul((r,r),C[i][j]),neg(G[i][j]))) for i,x in enumerate(v) for j,y in enumerate(v));encloses(tuple(map(F,control['native_energy'])),energy);encloses(tuple(map(F,control['source_energy'])),source);check(F(control['native_energy'][0])>0);encloses(tuple(map(F,control['budget_quadratic'])),budget);check(control['failure_proved']==(F(control['budget_quadratic'][1])<0))
  n=comparison['certified_prefix_count'];check(1<=n<=count);check(comparison['complete_requested_block_budget_passed']==(n==count));budget=comparison['source_budget_certificate'];r=F(budget['source_ratio_upper']);check(r>0 and r+kappa*eps<credit);H=boxes(budget['source_budget_matrix']);U=[[F(x) for x in row] for row in budget['exact_congruence_U']];check(len(U)==n)
  for i in range(n):
   check(U[i][i]!=0)
   for j in range(n):
    check(i<=j or U[i][j]==0);encloses(H[i][j],add(mul((r,r),C[i][j]),neg(G[i][j])))
  UI=[[(x,x) for x in row] for row in U];K=mm([list(x) for x in zip(*UI)],mm(H,UI));saved=boxes(budget['budget_congruence_matrix']);margins=[]
  for i in range(n):
   for j in range(n):encloses(saved[i][j],K[i][j])
   margin=saved[i][i][0]-sum(max(abs(x),abs(y)) for j,(x,y) in enumerate(saved[i]) if i!=j);check(margin==F(budget['budget_Gershgorin_margins'][i]));check(margin>0);margins.append(margin)
  standalone=comparison['standalone_remainder_uniform_floor_certificate'];check(F(standalone['source_ratio_upper'])==kappa);SH=boxes(standalone['source_budget_matrix']);SU=[[F(x) for x in row] for row in standalone['exact_congruence_U']];check(len(SU)==count)
  for i in range(count):
   check(SU[i][i]!=0)
   for j in range(count):
    check(i<=j or SU[i][j]==0);encloses(SH[i][j],add(mul((kappa,kappa),C[i][j]),neg(G[i][j])))
  SUI=[[(x,x) for x in row] for row in SU];SK=mm([list(x) for x in zip(*SUI)],mm(SH,SUI));savedSK=boxes(standalone['budget_congruence_matrix'])
  for i in range(count):
   for j in range(count):encloses(savedSK[i][j],SK[i][j])
   sm=savedSK[i][i][0]-sum(max(abs(x),abs(y)) for j,(x,y) in enumerate(savedSK[i]) if i!=j);check(sm==F(standalone['budget_Gershgorin_margins'][i]));check(sm>0)
  schur=(credit-r)/kappa-eps;check(schur==F(comparison['Schur_energy_lower']) and schur>0);check(comparison['all_high_positive_retained_rank']==4+n)
  frame,fh=read(cert['input_paths'][2]);check(fh==cert['input_sha256'][2]);q=F(frame['native_scaled_identity_lower']);check(q>0 and credit==F(frame['optimized_T4_source_credit']));native,nh=read(cert['input_paths'][1]);check(nh==cert['input_sha256'][1]);selected,sh=read(native['input_paths'][2]);check(sh==native['input_sha256'][2]);ids=native['retained_indices'];trial=[{ids[0]:F(1)}]+[dict(zip(t['indices'],map(F,t['coefficients']))) for t in selected['columns']]+[dict(zip(c['indices'],map(F,c['coefficients']))) for c in cols[:n]];minor=[[v.get(i,F(0)) for i in ids[:4+n]] for v in trial]
  for i in range(4+n):
   pivot=next(j for j in range(i,4+n) if minor[j][i]);minor[i],minor[pivot]=minor[pivot],minor[i];check(minor[i][i]!=0)
   for j in range(i+1,4+n):
    ratio=minor[j][i]/minor[i][i];minor[j]=[x-ratio*y for x,y in zip(minor[j],minor[i])]
  cm=F(cert['congruence_margin_lower']);check(cm>0);mass=sum(F(c['exact_mass_squared']) for c in cols[:n]);M=2*(F(cert['exact_total_scaled_tested_physical_mass'])/q+mass/cm);gap=min(schur/(4*(M+(kappa-credit+r)/kappa**2)),kappa/2);check(gap>0)
  rows.append(dict(parity=par,primary_sha256=ah,replay_sha256=bh,comparison_sha256=coh,coherent_source_block_dimension=count,source_block_entries=count*count,certified_prefix_count=n,all_high_positive_retained_rank=4+n,source_ratio_upper=str(r),Schur_energy_lower=str(schur),all_high_physical_gap_lower=str(gap),half_credit_budget_failure_proved=comparison['source_budget_controls'][0]['failure_proved'],full_credit_budget_failure_proved=comparison['source_budget_controls'][1]['failure_proved'],standalone_remainder_uniform_floor_budget_passed=True))
 total=sum(row['all_high_positive_retained_rank'] for row in rows);guard=F(1,10**100);minimum=min(F(row['all_high_physical_gap_lower']) for row in rows)
 while guard*10<minimum:guard*=10
 check(0<guard<minimum)
 out=dict(stage='DNE34',status='PASS',exact_rational_checks=checks,exact_signed_convolution_controls=40,rows=rows,all_high_positive_retained_dimension=total,uncovered_retained_dimension=112-total,all_high_physical_gap_guard=str(guard),coherent_complete_source_blocks_certified=True,frozen_scalar_credit_route_obstructed=True,standalone_remainder_uniform_floor_budget_passed=True,complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('PASS',checks,'checks; all-high retained rank',total)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('inputs',nargs=6);p.add_argument('--output',required=True);a=p.parse_args();run(a.inputs,a.output)
