#!/usr/bin/env python3
"""Rational audit of freshly reconstructed selected original source rows."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,base64,gzip,argparse,sys
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc104_joint_response_rebase as previous
BASE=Path(__file__).resolve().parents[1];K=F(289,500)
def read(name):
 p=BASE/name
 if not p.exists():p=BASE/(name+'.gz.b64')
 b=p.read_bytes();stored=hashlib.sha256(b).hexdigest()
 if p.name.endswith('.b64'):b=gzip.decompress(base64.b64decode(b))
 return json.loads(b),hashlib.sha256(b).hexdigest(),stored
def run():
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def encloses(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 for idx,parity in enumerate(['even','odd']):
  packet,ph,_=read(f'notes/data/RPB108_CC105_{parity.upper()}_PHYSICAL_PACKET_20261010.json');cols=packet['columns'];count=len(cols)
  check(packet['exact_retained_constraint_frame_verified'] and packet['exact_high_physical_Gram_verified']);check(count==12-idx)
  frame,_,_=read('notes/cc104-source/notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json');fr=frame['parity_frames'][idx]
  pp=[dict(zip(v['indices'],map(F,v['coefficients']))) for v in fr['unchanged_joined_columns']];ids=fr['retained_indices'];constraints=[[v.get(i,F(0)) for i in ids] for v in pp]
  for i in range(3):
   for j in range(i):check(sum(a*b for a,b in zip(constraints[i],constraints[j]))==0)
  piv=fr['old_two_constraint_pivots']+[fr['old_free_coordinates'][fr['third_constraint_pivot_in_old_free_coordinates']]]
  free=[j for j in fr['old_free_coordinates'] if j!=piv[2]];check(len(free)==53)
  z=list(map(F,packet['source_trial_coefficients']));norm=F(packet['source_trial_normalizing_upper']);poly=dict(zip(cols[0]['indices'],map(F,cols[0]['coefficients'])))
  reconstructed={i:sum(z[k]*pp[k].get(i,F(0)) for k in range(3)) for i in poly}
  for j,beta in zip(free,z[3:]):reconstructed[ids[j]]+=beta
  # Independent three-constraint solve, rather than the producer's T54/T53 map.
  system=[[constraints[i][j] for j in piv]+[z[i]*sum(v*v for v in constraints[i])-sum(constraints[i][j]*reconstructed.get(ids[j],F(0)) for j in range(56) if j not in piv)] for i in range(3)]
  for k in range(3):
   pivot=next(j for j in range(k,3) if system[j][k]);system[k],system[pivot]=system[pivot],system[k];v=system[k][k];system[k]=[x/v for x in system[k]]
   for j in range(3):
    if j!=k:
     v=system[j][k];system[j]=[x-v*y for x,y in zip(system[j],system[k])]
  for j,row in zip(piv,system):reconstructed[ids[j]]=row[3]
  for i in poly:check(reconstructed.get(i,F(0))/norm==poly[i])
  mass=sum(x*x for x in reconstructed.values());check(mass==F(packet['source_trial_physical_mass_squared']) and mass/norm**2==F(cols[0]['exact_mass_squared']))
  a,ah,_=read(f'notes/data/RPB108_CC105_{parity.upper()}_SOURCE_PRIMARY_20261010.json')
  b,bh,_=read(f'notes/data/RPB108_CC105_{parity.upper()}_SOURCE_REPLAY_20261010.json')
  for data in [a,b]:
   check(data['stage']=='CC105' and data['normalized_packet_sha256']==ph and data['certificate_sha256']==ph)
   check(data['complete_original_source_action'] and data['exact_endpoint_logs'] and data['all_six_primes_both_orientations'])
   check(not data['sampled_quadrature'] and data['complete_trial_high_source_star_and_diagonals_certified'])
   check(data['retained_projection_indices']==list(range(idx,112,2)))
   check(data['helper_sha256']=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8')
   eta=F(data['uniform_original_source_operator_error_upper']);check(eta>=F(106,50)*F(550,19)*F(106,125)**data['regular_order']+F(3,10**99))
   coords=c.matrix(data['retained_rounded_source_coordinates']);full=c.matrix(data['complete_source_coordinates']);errors=list(map(F,data['source_L2_error_upper']));norms=list(map(F,data['projected_source_norm_upper']))
   check(full[0][:56]==coords[0]);check(F(data['physical_interval_sqrt_upper'])**2>=F(106,50))
   check(F(data['complete_log_norm_upper'])**2>=F(data['complete_log_squared_norm'][1]))
   for i,col in enumerate(cols):
    mass=sum(F(x)**2 for x in col['coefficients']);pn=F(col['norm_upper']);check(mass==F(data['exact_masses'][i])==F(col['exact_mass_squared']));check(pn*pn>mass)
    rounding=F(data['polynomial_rounding_source_L2_error_upper'][i]);check(rounding>=F(data['physical_interval_sqrt_upper'])*max(map(F,data['panel_regular_polynomial_sup_error_upper'][i]))+F(data['logarithmic_polynomial_sup_error_upper'][i])*F(data['complete_log_norm_upper'])/2)
    check(errors[i]>=eta*pn+rounding)
    for j in range(count):
     if i!=0 and j!=0 and i!=j:
      check(data['original_projected_source_Gram'][i][j] is None);continue
     whole=c.iv(data['complete_rounded_source_Gram'][i][j]);projected=c.sub(whole,c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])))
     check(projected==c.iv(data['projected_rounded_source_Gram'][i][j]));pay=F(data['source_Gram_error_payments'][i][j]);check(pay>=errors[i]*norms[j]+errors[j]*norms[i]+errors[i]*errors[j])
     check(c.add(projected,(-pay,pay))==c.iv(data['original_projected_source_Gram'][i][j]))
    check(norms[i]**2>F(data['projected_rounded_source_Gram'][i][i][1]))
    approximate=c.sumiv(c.mul(c.iv(v),full[0][(degree-idx)//2]) for degree,v in zip(col['indices'],col['coefficients']))
    encloses(c.iv(data['original_trial_native_pairings'][i]),c.add(approximate,(-errors[0]*pn,errors[0]*pn)))
   check(data['physical_norm_upper']==[col['norm_upper'] for col in cols])
  check((a['regular_order'],a['precision'])==(360,760));check((b['regular_order'],b['precision'])==(400,800))
  for i in range(count):
   encloses(c.iv(a['original_trial_native_pairings'][i]),c.iv(b['original_trial_native_pairings'][i]))
   for j in range(count):
    if i==0 or j==0 or i==j:encloses(c.iv(a['original_projected_source_Gram'][i][j]),c.iv(b['original_projected_source_Gram'][i][j]))
  h,hh,_=read(f'notes/cc104-source/notes/data/RPB108_NF52_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64')
  QH=c.matrix(h['enlarged_high_native_Gram']);GH=c.matrix(h['enlarged_high_complete_source_Gram']);M=c.matrix(h['enlarged_high_physical_Gram'])
  fixed,_,_=read('notes/cc105-source/notes/data/'+('RPB108_NF46_EVEN_FIXED_NEXT_SHELL_20261009.json' if idx==0 else 'RPB108_NF45_ODD_FIXED_INVERSE_WITNESS_20261009.json'))
  expected=fixed['seven_high_columns' if idx==0 else 'six_high_columns']+[dict(indices=fixed['selection_indices'],coefficients=fixed['fixed_rational_eighth_high_coefficients' if idx==0 else 'fixed_rational_seventh_high_coefficients'])]
  for nf in [50,51,52]:
   data,_,_=read(f'notes/cc{105 if nf<52 else 104}-source/notes/data/RPB108_NF{nf}_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64')
   sel=data['fixed_high_selection'];expected.append(dict(indices=sel['selection_indices'],coefficients=sel['fixed_rational_high_coefficients']))
  for i,col in enumerate(expected):
   actual=dict(zip(cols[i+1]['indices'],map(F,cols[i+1]['coefficients'])));check(actual==dict(zip(col['indices'],map(F,col['coefficients']))));check(min(actual)>=112)
   for j,col2 in enumerate(expected):
    other=dict(zip(col2['indices'],map(F,col2['coefficients'])));mass=sum(v*other.get(k,F(0)) for k,v in actual.items());encloses(M[i][j],c.iv(mass))
  C=r.sub(QH,r.scale(M,K));N=r.sub(r.scale(GH,1/K),QH)
  _,cp=previous.proof.proof(C);_,np=previous.proof.proof(N);NI,rho=previous.inverse(N)
  for i in range(count-1):
   fresh=c.iv(b['original_projected_source_Gram'][i+1][i+1]);check(c.overlap(fresh,GH[i][i]))
  full=c.matrix(b['complete_source_coordinates']);errors=list(map(F,b['source_L2_error_upper']))
  native=list(map(c.iv,b['original_trial_native_pairings']));reverse=[]
  for i in range(1,count):
   approx=c.sumiv(c.mul(c.iv(v),full[i][(degree-idx)//2]) for degree,v in zip(cols[0]['indices'],cols[0]['coefficients']))
   pay=errors[i]*F(cols[0]['norm_upper']);other=c.add(approx,(-pay,pay));check(c.overlap(native[i],other))
   native[i]=(max(native[i][0],other[0]),min(native[i][1],other[1]));reverse.append(c.pair(other))
  qa,qah,_=read(f'notes/data/RPB108_CC105_{parity.upper()}_NATIVE_PRIMARY_20261010.json')
  qb,qbh,_=read(f'notes/data/RPB108_CC105_{parity.upper()}_NATIVE_REPLAY_20261010.json')
  for data,order,precision in [(qa,580,1000),(qb,620,1040)]:
   check(data['stage']=='CC105' and data['normalized_packet_sha256']==ph and data['certificate_sha256']==ph)
   check((data['regular_order'],data['precision'])==(order,precision))
   check(len(data['original_trial_native_pairings'])==len(data['source_L2_error_upper'])==1)
   check(data['helper_sha256']==b['helper_sha256'] and data['exact_masses']==b['exact_masses'][:1])
   eta=F(data['uniform_original_source_operator_error_upper']);check(eta>=F(106,50)*F(550,19)*F(106,125)**order+F(3,10**99))
   rounding=F(data['polynomial_rounding_source_L2_error_upper'][0]);check(rounding>=F(data['physical_interval_sqrt_upper'])*max(map(F,data['panel_regular_polynomial_sup_error_upper'][0]))+F(data['logarithmic_polynomial_sup_error_upper'][0])*F(data['complete_log_norm_upper'])/2)
   error=F(data['source_L2_error_upper'][0]);pn=F(cols[0]['norm_upper']);check(error>=eta*pn+rounding)
   approx=c.sumiv(c.mul(c.iv(v),c.iv(data['complete_source_coordinates'][0][(degree-idx)//2])) for degree,v in zip(cols[0]['indices'],cols[0]['coefficients']))
   encloses(c.iv(data['original_trial_native_pairings'][0]),c.add(approx,(-error*pn,error*pn)))
  q=c.iv(qb['original_trial_native_pairings'][0]);encloses(c.iv(qa['original_trial_native_pairings'][0]),q);check(c.overlap(native[0],q))
  g=c.iv(b['original_projected_source_Gram'][0][0]);w=[[c.sub(c.iv(b['original_projected_source_Gram'][0][i+1]),c.mul(c.iv(K),native[i+1])) for i in range(count-1)]]
  credit=c.mul(c.mm(c.mm(w,NI),c.transpose(w))[0][0],c.iv(1/K**2));plain=c.sub(q,c.mul(g,c.iv(1/K)));value=c.add(plain,credit)
  check(q[0]>0 and g[0]>0 and credit[0]>0);check(plain[1]<0 and value[1]<0)
  target=F(29,50);Ct=r.sub(QH,r.scale(M,target));Nt=r.sub(r.scale(GH,1/target),QH)
  _,ctp=previous.proof.proof(Ct);_,ntp=previous.proof.proof(Nt);NTI,trho=previous.inverse(Nt)
  wt=[[c.sub(c.iv(b['original_projected_source_Gram'][0][i+1]),c.mul(c.iv(target),native[i+1])) for i in range(count-1)]]
  targetplain=c.sub(q,c.mul(g,c.iv(1/target)));targetcredit=c.mul(c.mm(c.mm(wt,NTI),c.transpose(wt))[0][0],c.iv(1/target**2));targetvalue=c.add(targetplain,targetcredit)
  check(targetplain[1]<0 and targetvalue[0]>0)
  old,_,_=read('notes/data/RPB108_CC104_JOINT_RESPONSE_REBASE_20261010.json');oldvalue=c.iv(old['parity_checks'][idx]['sign']['correlated_value']);scale=F(packet['source_trial_normalizing_upper'])**2
  oldvalue=c.div(oldvalue,c.iv(scale));check(c.overlap(oldvalue,value))
  rows.append(dict(parity=parity,primary_decoded_sha256=ah,replay_decoded_sha256=bh,native_primary_decoded_sha256=qah,native_replay_decoded_sha256=qbh,physical_packet_decoded_sha256=ph,
   original_NF52_certificate_decoded_sha256=hh,high_surplus_proof=cp,high_denominator_proof=np,inverse_residual_upper=c.pair(c.iv(rho))[1],
   exact_physical_trial_mass_squared=cols[0]['exact_mass_squared'],native_trial_energy=c.pair(q),projected_trial_source_square=c.pair(g),
   native_trial_high_row=[c.pair(x) for x in native[1:]],reverse_native_trial_high_row=reverse,
   signed_trial_high_surplus_source_row=[c.pair(x) for x in w[0]],plain_floor_value=c.pair(plain),response_credit=c.pair(credit),refined_response_value=c.pair(value),
   inherited_entrywise_trial_interval_normalized=c.pair(oldvalue),interval_width_reduction_factor_lower=c.pair(c.iv((oldvalue[1]-oldvalue[0])/(value[1]-value[0])))[0],
   response_sign='POSITIVE' if value[0]>0 else 'REJECTED' if value[1]<0 else 'UNRESOLVED',
   conditional_trial_target_floor=str(target),conditional_target_plain_value=c.pair(targetplain),conditional_target_response_credit=c.pair(targetcredit),conditional_target_refined_value=c.pair(targetvalue),
   conditional_target_surplus_proof=ctp,conditional_target_denominator_proof=ntp,conditional_target_inverse_residual_upper=c.pair(c.iv(trho))[1],
   target_original_floor_newly_proved=False,conditional_target_is_not_whole_collective_positivity=True,
   original_negative_form_claimed=False))
 return dict(milestone='CC105',parent='0230c9ec6cb034f1713b30c7652568fcaafc30c5',original_high_floor=str(K),exact_rational_checks=checks,parity_checks=rows,
  fresh_analytic_source_reconstructions=True,all_original_infinite_source_tails_paid=True,full_collective_matrix_positive=False,
  integrated_retained_rank=56,uncovered_retained_dimension=56,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();d=run();Path(a.output).write_text(json.dumps(d,indent=2)+'\n')
 for row in d['parity_checks']:print(row['parity'],row['response_sign'],[float(F(x)) for x in row['refined_response_value']])
