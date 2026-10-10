#!/usr/bin/env python3
"""Independent rational consumer of freshly computed coherent Z21 source data."""
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc97_collective_signed_consumer as prior

K=F(57,100)
def read(p):return prior.rawread(p.parent,p.name)
def proof(M,frozen=None):
 if frozen is None:
  from certify_dne32_native_remainder import I,precondition
  U=precondition([[I(*x) for x in row] for row in M])
 else:U=[[F(x) for x in row] for row in frozen]
 n=len(M);assert len(U)==n and all(len(row)==n for row in U)
 assert all(U[i][i]!=0 and all(U[i][j]==0 for j in range(i)) for i in range(n))
 ui=[[c.iv(x) for x in row] for row in U]
 paid=r.mm(c.transpose(ui),r.mm(M,ui))
 margins=[paid[i][i][0]-sum(r.absmax(paid[i][j]) for j in range(n) if j!=i) for i in range(n)]
 assert min(margins)>0
 floor=min(margins)/sum(x*x for row in U for x in row)
 return floor,dict(frozen_rational_congruence=[list(map(str,row)) for row in U],
  paid_minimum_Gershgorin_margin=c.pair(c.iv(min(margins)))[0],coefficient_floor_lower=c.pair(c.iv(floor))[0])
def run(root,inputs,oldroot,frozen=None):
 sys.path.insert(0,str((root/'scripts').resolve()))
 integration=root.resolve().parents[1]
 high,highsha=read(integration/'notes/data/RPB108_CC100_FRESH_HIGH_FLOOR_AUDIT_20261010.json')
 standing,_=read(integration/'notes/data/RPB108_CC100_CURRENT_HIGH_FLOOR_20261010.json')
 assert highsha==standing['fresh_high_floor_validation_sha256'] and high['status']=='PASS' and high['original_infinite_F112_floor']==str(K)
 assert highsha=='39b0e25e4a78625fc4ac997a4f8ca06b818d5f740c76f8a1bf6546095e0dd12f'
 assert hashlib.sha256((root/'scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest()=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8'
 rows=[];checks=0
 def check(v):
  nonlocal checks
  assert v;checks+=1
 def encloses(a,b):check(a[0]<=b[0]<=b[1]<=a[1])
 for parity in ['even','odd']:
  pp=inputs/('RPB108_CC101_'+parity.upper()+'_PRIMARY_20261010.json.gz.b64')
  rp=inputs/('RPB108_CC101_'+parity.upper()+'_REPLAY_20261010.json.gz.b64')
  a,ah=read(pp);b,bh=read(rp)
  packet,ph=read(inputs/('RPB108_CC101_'+parity.upper()+'_PHYSICAL_PACKET_20261010.json.gz.b64'));cols=packet['columns']
  check(len(cols)==21 and packet['column_labels']==[f'TS{i}' for i in range(4)]+[f'X{i}' for i in range(17)])
  cert,ch=read(root/b['certificate_path']);native,nh=read(root/cert['input_paths'][1]);frame,fh=read(root/cert['input_paths'][2])
  selected,sh=read(root/native['input_paths'][2]);check([nh,fh]==cert['input_sha256'][1:3]);check(sh==native['input_sha256'][2])
  check(b['certificate_sha256']==a['certificate_sha256']==ch)
  # Independent sparse expansion ties each physical source column to the frozen native frame.
  retained=native['retained_indices'];tested=[{retained[0]:F(1)}]+[dict(zip(x['indices'],map(F,x['coefficients']))) for x in selected['columns']]
  scales=list(map(F,frame['column_scales']));uu=[[F(x) for x in row] for row in cert['exact_rational_congruence_U']]
  ww=[[F(x) for x in row] for row in native['exact_W_columns']];kk=[[F(x) for x in row] for row in frame['frozen_original_projection_K']]
  for i in range(4):
   check(dict(zip(cols[i]['indices'],map(F,cols[i]['coefficients'])))=={n:x*scales[i] for n,x in tested[i].items()})
  for j in range(17):
   poly={n:sum(ww[t][i]*uu[t][j] for t in range(52)) for i,n in enumerate(retained)}
   for i,t in enumerate(tested):
    v=sum(kk[i][k]*uu[k][j] for k in range(52))
    for n,x in t.items():poly[n]=poly.get(n,F(0))-x*v
   check(poly==dict(zip(cols[4+j]['indices'],map(F,cols[4+j]['coefficients']))))
  # Reconstruct complete original native border with exact, unrounded interval products.
  A=c.matrix(cert['tightened_scaled_T4_native_matrix']);P=c.matrix(cert['tightened_scaled_T4_W52_border'])
  J=[[c.iv(v) for v in row] for row in frame['frozen_scaled_projection_J']]
  AJ=c.mm(A,J);E=[[c.sub(x,y) for x,y in zip(ar,br)] for ar,br in zip(P,AJ)]
  U=[[c.iv(v) for v in row[:17]] for row in cert['exact_rational_congruence_U']];cross=c.mm(E,U);Q=c.matrix(b['native_block'])
  for i in range(4):
   for j in range(4):encloses(Q[i][j],A[i][j])
   for j in range(17):encloses(Q[i][4+j],cross[i][j]);check(Q[i][4+j]==Q[4+j][i])
  for i in range(17):
   for j in range(17):encloses(Q[4+i][4+j],c.iv(cert['congruence_matrix'][i][j]))
  check(a['regular_order']==360 and b['regular_order']==400 and a['precision']==600 and b['precision']==620)
  for d in [a,b]:
   check(d['columns']==list(range(21)) and d['parity']==parity and d['column_labels']==packet['column_labels'])
   check(d['normalized_packet_sha256']==ph and d['joint_packet_input_sha256']==packet['input_sha256'])
   check(d['native_block']==packet['native_matrix'])
   check(d['helper_sha256']==hashlib.sha256((root/'scripts/dne23_dne16_source_input.py').read_bytes()).hexdigest())
   check(d['complete_original_source_action'] and d['exact_endpoint_logs'] and d['all_six_primes_both_orientations'])
   check(d['complete_joint_source_Gram_certified'] and not d['sampled_quadrature'])
   check(d['retained_projection_indices']==list(range(int(parity=='odd'),112,2)))
   eta=F(d['uniform_original_source_operator_error_upper']);check(eta>=2*F(53,50)*F(550,19)*F(106,125)**d['regular_order']+F(3,10**99))
   sq=F(d['physical_interval_sqrt_upper']);ln=F(d['complete_log_norm_upper'])
   check(sq*sq>=2*F(53,50) and ln*ln>=F(d['complete_log_squared_norm'][1]))
   whole=c.matrix(d['complete_rounded_source_Gram']);coords=c.matrix(d['retained_rounded_source_coordinates'])
   proj=c.matrix(d['projected_rounded_source_Gram']);G=c.matrix(d['original_projected_source_Gram'])
   errors=list(map(F,d['source_L2_error_upper']));roots=list(map(F,d['projected_source_norm_upper']))
   for i,col in enumerate(cols):
    mass=sum(F(x)**2 for x in col['coefficients']);norm=F(col['norm_upper'])
    check(mass==F(col['exact_mass_squared'])==F(d['exact_masses'][i]) and norm==F(d['physical_norm_upper'][i]) and norm*norm>mass)
    pe=list(map(F,d['panel_regular_polynomial_sup_error_upper'][i]));check(len(pe)==7)
    rounding=F(d['polynomial_rounding_source_L2_error_upper'][i])
    check(rounding>=sq*max(pe)+F(d['logarithmic_polynomial_sup_error_upper'][i])*ln/2)
    check(errors[i]>=eta*norm+rounding and roots[i]**2>proj[i][i][1] and len(coords[i])==56)
    for j in range(21):
     check(G[i][j]==G[j][i] and whole[i][j]==whole[j][i])
     recon=c.sub(whole[i][j],c.sumiv(c.mul(x,y) for x,y in zip(coords[i],coords[j])))
     check(recon==proj[i][j]);pay=F(d['source_Gram_error_payments'][i][j])
     check(pay>=errors[i]*roots[j]+errors[j]*roots[i]+errors[i]*errors[j]);check(G[i][j]==c.add(recon,(-pay,pay)))
  Ga=c.matrix(a['original_projected_source_Gram']);G=c.matrix(b['original_projected_source_Gram'])
  for i in range(21):
   for j in range(21):encloses(Ga[i][j],G[i][j])
  historical,hh=read(oldroot/('notes/data/RPB108_DNE36_'+parity.upper()+'_JOINT_SOURCE_REPLAY_20261010.json.gz.b64'))
  check(hh=={'even':'490f65448eb319990e35ba56d2a33e53eee22b2dd1639a95c1c18f7967e7591c','odd':'04d2beb2122afb00cd2f73ab7b63586c98f9425f6b2053cfe455bc603cb69321'}[parity])
  check(ch==historical['certificate_sha256'])
  for key in ['native_block','original_projected_source_Gram','complete_rounded_source_Gram','projected_rounded_source_Gram','source_Gram_error_payments']:
   for i in range(20):
    for j in range(20):check(b[key][i][j]==historical[key][i][j])
  # New exact retained-rank proof, independent of original source-coordinate intervals.
  ids=native['retained_indices'][:21]
  minor=[[dict(zip(col['indices'],map(F,col['coefficients']))).get(i,F(0)) for i in ids] for col in cols]
  for i in range(21):
   pivot=next(j for j in range(i,21) if minor[j][i]);minor[i],minor[pivot]=minor[pivot],minor[i];check(minor[i][i]!=0)
   for j in range(i+1,21):
    ratio=minor[j][i]/minor[i][i];minor[j]=[x-ratio*y for x,y in zip(minor[j],minor[i])]
  frow=next(x for x in frozen['parity_checks'] if x['parity']==parity) if frozen else None
  nf,np=proof(Q,frow['native_positive_proof']['frozen_rational_congruence'] if frow else None)
  H=[[c.sub(c.mul(c.iv(K),q),g) for q,g in zip(qrow,grow)] for qrow,grow in zip(Q,G)]
  hf,hp=proof(H,frow['signed_positive_proof']['frozen_rational_congruence'] if frow else None)
  mass=sum(map(F,b['exact_masses']));trace=sum(G[i][i][1] for i in range(21));gap=min(hf/K/(4*(mass+trace/K**2)),K/2)
  check(gap>F(1,10**37))
  rows.append(dict(parity=parity,primary_decoded_sha256=ah,replay_decoded_sha256=bh,physical_packet_decoded_sha256=ph,
   inherited_twenty_source_decoded_sha256=hh,new_exact_retained_rank=21,retained_rank_minor_indices=ids,
   native_positive_proof=np,signed_positive_proof=hp,original_all_high_physical_gap_lower=c.pair(c.iv(gap))[0]))
 out=dict(milestone='CC101',integration_parent='07d68dc04c8cccde065b3d20b6563b260625447e',
  read_only_DNE='f11f94dcd72c2d1a8438bdfbc7e7890b47902088',status='PASS',exact_rational_checks=checks,
  inherited_high_floor_validation_sha256=highsha,
  parity_checks=rows,current_original_high_floor=str(K),current_collective_retained_rank=42,remaining_retained_dimension=70,
  original_all_high_physical_gap_guard='1/'+str(10**37),complete_source_entries_rechecked=882,
  fresh_complete_original_source_integrations=True,primary_replay_containment_checked=True,
  exact_retained_rank_proofs_fresh=True,original_analytic_source_and_high_floor_theorems_inherited=True,
  complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
 if frozen:check(out==frozen)
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('source_root',type=Path);ap.add_argument('input_root',type=Path);ap.add_argument('old_source_root',type=Path)
 ap.add_argument('--output',type=Path,required=True);ap.add_argument('--verify-certificate',type=Path)
 a=ap.parse_args();frozen=json.loads(a.verify_certificate.read_text()) if a.verify_certificate else None
 d=run(a.source_root,a.input_root,a.old_source_root,frozen);a.output.write_text(json.dumps(d,indent=2)+'\n')
 print('CC101 PASS:',d['exact_rational_checks'],'rational checks; 42 retained directions plus all F112')
