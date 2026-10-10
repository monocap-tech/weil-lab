import sys,json,gzip,base64,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D,localcontext
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'notes/cc101-source/scripts'))
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
ROOT=Path('notes/cc104-source/notes/data');K=F(289,500)
def read(name):
 b=(ROOT/name).read_bytes();return json.loads(gzip.decompress(base64.b64decode(b))) if name.endswith('b64') else json.loads(b)
def unpack(rows,n):
 it=iter(rows);out=[[None]*n for _ in range(n)]
 for i in range(n):
  for j in range(i,n):out[i][j]=out[j][i]=c.iv(next(it))
 return out
def block(a,b,d):return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c.transpose(b),d)]
def inverse(a):
 n=len(a)
 with localcontext() as ctx:
  ctx.prec=160
  dec=lambda x:D(x.numerator)/D(x.denominator)
  m=[[dec(sum(v)/2) for v in row]+[D(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
  for k in range(n):
   pivot=m[k][k];assert pivot>0
   m[k]=[x/pivot for x in m[k]]
   for i in range(n):
    if i!=k:
     v=m[i][k];m[i]=[x-v*y for x,y in zip(m[i],m[k])]
  j=[[F(x) for x in row[n:]] for row in m]
 ji=[[c.iv(x) for x in row] for row in j];product=r.mm(ji,a)
 rho=max(sum(r.absmax(c.sub(c.iv(int(i==k)),v)) for k,v in enumerate(row)) for i,row in enumerate(product));assert rho<1
 err=rho*max(sum(abs(x) for x in row) for row in j)/(1-rho)
 return [[r.compact((x-err,x+err)) for x in row] for row in j],rho
def sign(a):
 n=len(a)
 with localcontext() as ctx:
  ctx.prec=160;dec=lambda x:D(x.numerator)/D(x.denominator)
  mid=[[dec(sum(x)/2) for x in row] for row in a];L=[[D(int(i==j)) for j in range(n)] for i in range(n)];p=[]
  for k in range(n):
   pivot=mid[k][k]-sum(L[k][j]**2*p[j] for j in range(k))
   if pivot<=0:
    v=[D(0)]*n;v[k]=D(1)
    for j in reversed(range(k)):v[j]=-sum(L[i][j]*v[i] for i in range(j+1,k+1))
    v=list(map(F,v));value=c.quad(a,v)
    return {'status':'REJECTED' if value[1]<0 else 'UNRESOLVED','pivot':k,'witness':list(map(str,v)),'value':c.pair(value)}
   p.append(pivot)
   for i in range(k+1,n):L[i][k]=(mid[i][k]-sum(L[i][j]*L[k][j]*p[j] for j in range(k)))/pivot
 floor,cert=proof.proof(a)
 return {'status':'POSITIVE','floor':str(floor),'proof':cert}
def run(parity,idx):
 check_custody(parity,idx)
 o=read(f'RPB108_NF49_{parity.upper()}_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64')
 h=read(f'RPB108_NF52_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64')
 joined=read(f'RPB108_NF37_{parity.upper()}_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json')
 native=read('RPB108_NF48_REMAINING_NATIVE_CERTIFICATE_20261009.json.gz.b64')['parity_certificates'][idx]
 Q=block(c.matrix(joined['original_selected_native_energy_Gram']),c.matrix(native['original_remaining_native_couplings']),c.matrix(native['original_remaining_native_Gram']))
 G=block(c.matrix(joined['original_selected_complete_source_Gram']),c.transpose(c.matrix(o['original_remaining_joined_source_crosses'])),unpack(o['original_remaining_complete_source_Gram_upper'],53))
 M,QH,GH,B,S=[c.matrix(h[key]) for key in ['enlarged_high_physical_Gram','enlarged_high_native_Gram','enlarged_high_complete_source_Gram','enlarged_joint_high_native_crosses','enlarged_joint_high_complete_source_crosses']]
 C=r.sub(QH,r.scale(M,K));N=r.sub(r.scale(GH,1/K),QH);W=r.sub(S,r.scale(B,K))
 print(parity,'proving surplus',flush=True);cf,cp=proof.proof(C)
 print(parity,'proving denominator',flush=True);nf,np=proof.proof(N);NI,rho=inverse(N)
 print(parity,'inverse paid',float(rho),flush=True)
 gain=r.scale(r.mm(r.mm(W,NI),c.transpose(W)),1/K**2)
 plain=r.sub(Q,r.scale(G,1/K));lower=[[r.compact(c.add(x,y)) for x,y in zip(a,b)] for a,b in zip(plain,gain)]
 lower=[[(min(lower[i][j][0],lower[j][i][0]),max(lower[i][j][1],lower[j][i][1])) for j in range(56)] for i in range(56)]
 status=sign(lower)
 trials=[]
 for label,raw in [('NF52_rejecting',h['joint_lower_bound_sign']['fixed_rational_lower_bound_witness']),('normalized_NF51',h['fixed_high_selection']['normalized_NF51_joint_witness'])]:
  z=list(map(F,raw));wz=c.mm([list(map(c.iv,z))],W)
  q=c.quad(Q,z);g=c.quad(G,z);credit=c.mul(c.mm(c.mm(wz,NI),c.transpose(wz))[0][0],c.iv(1/K**2))
  plainvalue=c.sub(q,c.mul(g,c.iv(1/K)));direct=c.add(plainvalue,credit)
  trials.append({'label':label,'plain_value':c.pair(plainvalue),'response_credit':c.pair(credit),'refined_value':c.pair(direct),'positive':direct[0]>0})
  print(parity,label,[float(x) for x in direct],flush=True)
 if 'witness' in status:
  z=list(map(F,status['witness']))
  wz=c.mm([list(map(c.iv,z))],W)
  q=c.quad(Q,z);g=c.quad(G,z)
  credit=c.mul(c.mm(c.mm(wz,NI),c.transpose(wz))[0][0],c.iv(1/K**2))
  direct=c.add(c.sub(q,c.mul(g,c.iv(1/K))),credit)
  status['correlated_value']=c.pair(direct);status['status']='REJECTED' if direct[1]<0 else 'UNRESOLVED'
 print(parity,status['status'],status.get('pivot'),[float(F(x)) for x in status.get('correlated_value',[])],flush=True)
 out={'parity':parity,'kappa':str(K),'surplus_proof':cp,'denominator_proof':np,'inverse_rho':str(rho),'sign':status,'old_witness_trials':trials}
 prefixes=[]
 for count in ([12] if parity=='even' else [20]):
  floor,cert=proof.proof([row[:count] for row in lower[:count]])
  prefixes.append(dict(dimension=count,coefficient_floor=str(floor),positive_proof=cert))
 z=list(map(F,status['witness']))
 midpoint=[[c.iv(sum(x)/2) for x in row] for row in lower]
 midpoint_value=c.quad(midpoint,z);assert midpoint_value[1]<0
 out['interval_box_midpoint_negative_exact_value']=c.pair(midpoint_value)
 out['interval_box_is_not_uniformly_positive']=True
 out['paid_whole_matrix_negative_sign_certified']=False
 out['positive_prefixes']=prefixes
 out['actual_negative_original_form_claimed']=False
 return out

def check_custody(parity,idx):
 manifest=json.loads((ROOT.parent.parent/'input_custody.json').read_text())
 for pin in manifest['files']:
  assert hashlib.sha256((ROOT.parent.parent/pin['path']).read_bytes()).hexdigest()==pin['stored_sha256']
 def sha(name):return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
 report=read(f'RPB108_NF52_{parity.upper()}_JOINT_REFINEMENT_VALIDATION_20261010.json')
 assert report['status']=='PASS' and report['inherited_NF51_certificate_and_validation_authenticated']
 assert report['certificate_sha256']==sha(f'RPB108_NF52_{parity.upper()}_JOINT_REFINEMENT_CERTIFICATE_20261010.json.gz.b64')
 older=read(f'RPB108_NF49_{parity.upper()}_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64')
 audit=read(f'RPB108_NF49_{parity.upper()}_COMPLETE_TRANSPORT_VALIDATION_20261010.json')
 assert audit['status']=='PASS' and audit['encoded_certificate_sha256']==sha(f'RPB108_NF49_{parity.upper()}_COMPLETE_TRANSPORT_CERTIFICATE_20261010.json.gz.b64')
 for name,digest in older['frozen_input_sha256'].items():
  assert hashlib.sha256((ROOT.parent.parent/name).read_bytes()).hexdigest()==digest
 joined=read(f'RPB108_NF37_{parity.upper()}_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE_20261009.json')
 native=read('RPB108_NF48_REMAINING_NATIVE_CERTIFICATE_20261009.json.gz.b64')['parity_certificates'][idx]
 assert native['joined_native_Gram']==joined['original_selected_native_energy_Gram']
 assert older['original_remaining_dimension']==53 and older['complete_remaining_source_transport_data_certified']
 def payment(raw,saved,ea,eb,na,nb):
  for i,row in enumerate(raw):
   for j,x in enumerate(row):
    pay=ea[i]*nb[j]+eb[j]*na[i]+ea[i]*eb[j]
    a=c.add(c.iv(x),(-pay,pay));b=c.iv(saved[i][j])
    assert b[0]<=a[0]<=a[1]<=b[1]
 e=list(map(F,older['remaining_source_physical_errors']));n=list(map(F,older['remaining_source_approximant_norm_upper']))
 raw=unpack(older['reconstructed_remaining_source_Gram_upper'],53);paid=unpack(older['original_remaining_complete_source_Gram_upper'],53)
 payment(raw,paid,e,e,n,n)
 for label in ['joined','high']:
  payment(older['reconstructed_remaining_'+label+'_source_crosses'],older['original_remaining_'+label+'_source_crosses'],
   e,list(map(F,older[label+'_source_physical_errors'])),n,list(map(F,older[label+'_source_approximant_norm_upper'])))
 standing_path=Path(__file__).resolve().parents[1]/'notes/data/RPB108_CC103_DNE39_COLLECTIVE_20261010.json'
 assert hashlib.sha256(standing_path.read_bytes()).hexdigest()=='aa0bf248e7664a03395da760436355c6e456c8c0f7a65635bb9799f5508e10d4'
 standing=json.loads(standing_path.read_text());assert standing['original_high_floor']==str(K)

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('source_root',type=Path);parser.add_argument('--output',type=Path,required=True)
 args=parser.parse_args();ROOT=args.source_root/'notes/data'
 rows=[run(p,i) for i,p in enumerate(['even','odd'])]
 out=dict(milestone='CC104',integration_parent='d96eee9a638ec5923886a832f0b7af57a459bb7e',
  read_only_Native_Source='19c11a4f9f8f03b039fcb30a8addf4d96029c53c',original_high_floor=str(K),
  parity_checks=rows,exact_rank_one_controls=r.controls(),full_joint_dimension_per_parity=56,
  source_analytic_integrations_and_original_rank_proofs_inherited=True,source_integrals_recomputed=False,
  shared_high_surplus_and_inverse_denominator_positive=True,
  all_tested_NF52_and_normalized_NF51_witnesses_positive=True,
  current_integrated_positive_retained_rank=56,remaining_uncovered_retained_dimension=56,
  full_paid_joint_response_sign='UNRESOLVED',whole_aperture_positive=False,RH=False,F4=False,Lean=False)
 assert all(all(t['positive'] for t in row['old_witness_trials']) for row in rows)
 args.output.write_text(json.dumps(out,indent=2)+'\n')
 print('CC104 PASS: common-floor response rebuilt; old witnesses lifted; whole gate unresolved')
