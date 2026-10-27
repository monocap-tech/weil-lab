#!/usr/bin/env python3
"""Joint raw precision/tail budget transported through the accepted actual frame."""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
from flint import arb,arb_mat,ctx
import flint
import verify_rpb108_si29_full_J_L2_normalization as m
from verify_rpb108_original_signed_frame_transport import candidate
FRAME='e78c29dc930274e5522c665d073044a6de6ac1fee832cac65c13128f57fe80d4'
OLD='2cb869033f2c6722d356e769f35fc0e1b041ae46a8c11360e66cd7d2c694c548'
RANK='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
CRITICAL='a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'
def rat(x):
 n,e=x.man_exp();return F(int(n))*F(2)**int(e)
def dy(x):
 n,e=x.man_exp();return [str(n),int(e)]
def ball(x):return [dy(x.mid()),dy(x.rad())]
def fromball(v):return arb(arb((int(v[0][0]),int(v[0][1]))),arb((int(v[1][0]),int(v[1][1]))))
def main():
 p=argparse.ArgumentParser()
 for v in ['frame','old','rank','critical','block','output']:p.add_argument('--'+v,required=True)
 a=p.parse_args();start=time.monotonic();data={};hashes={}
 for name,sha in [('frame',FRAME),('old',OLD),('rank',RANK),('critical',CRITICAL),('block',None)]:
  raw=Path(getattr(a,name)).read_bytes();h=hashlib.sha256(raw).hexdigest();assert sha is None or h==sha;data[name]=json.loads(raw);hashes[name]=h
 z=data['block'];old=data['old'];prior=data['frame'];r=data['rank'];cr=data['critical']
 assert z['working_precision_bits']==1024 and z['Laplace_terms']==128 and flint.__version__=='0.8.0'
 assert z['rank_input_sha256']==RANK and z['critical_input_sha256']==CRITICAL
 assert z['target_probes']==old['target_probes']==cr['exact_candidates']['probes']
 assert z['target_sine_frequencies']==old['target_sine_frequencies']
 assert len(z['rows'])==242 and z['complete_mixed_entry_count']==968
 for row,prev in zip(z['rows'],old['rows']):
  for k in ['original_source_index','cluster','center','order']:assert row[k]==prev[k]
  for e,oe in zip(row['entries'],prev['entries']):
   for key in ['arch','prime','pole']:assert (fromball(e['components_native'][key])-fromball(oe['components_native'][key])).contains(0)
   assert (fromball(e['signed_native'])-fromball(oe['signed_native'])).contains(0)
 ctx.prec=4096;kernel=m.Integrals();rows=z['rows']
 terms=[m.pole_terms() if v['original_source_index']==469 else m.source_terms(F(v['center']),v['order']) for v in rows]
 H=arb_mat(242,242)
 for i in range(242):
  for j in range(i+1):H[i,j]=H[j,i]=m.gram(terms[i],terms[j],kernel)
 D=candidate(H);N=D.transpose()*H*D
 errors=[sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242)];assert max(errors)<arb('0.01')
 digest=hashlib.sha256()
 for i in range(242):
  for j in range(242):digest.update((json.dumps(m.dyadic(D[i,j]),separators=(',',':'))+'\n').encode())
 assert digest.hexdigest()==prior['exact_dyadic_frame_transform_sha256']
 norm=sum((D[i,j]**2 for i in range(242) for j in range(242)),arb(0)).sqrt();normhi=rat(norm.upper());assert normhi<F(2)**496
 rho=max(F(int(e['signed_native'][1][0]))*F(2)**int(e['signed_native'][1][1]) for row in rows for e in row['entries'])
 assert rho==F(z['maximum_native_block_radius'])<F(2)**-581
 uniform2=normhi**2*968*rho**2;assert uniform2<F(2)**-160
 C=arb_mat([[fromball(e['signed_native']) for e in row['entries']] for row in rows]);T=D.transpose()*C
 radius2=sum((T[i,t].rad()**2 for i in range(242) for t in range(4)),arb(0));assert radius2<arb(2)**-160
 values=[[ball(T[i,t]) for t in range(4)] for i in range(242)]
 # Both finite physical Grams have lower .99 I. This bounds the form
 # coupling between the two finite physical spaces, not their quotient or
 # external complement, and supplies no strong-action estimate.
 normsquare=sum((rat(abs(T[i,t]).upper())**2 for i in range(242) for t in range(4)),F(0))
 coupling=(arb(str(normsquare))/arb('0.99')**2).sqrt();bound=rat(coupling.upper())
 assert F(cr['physical_Gram_lower'])==F(99,100)
 out=dict(status='CONDITIONAL_ORIGINAL_JOINT_SIGNED_FRAME_ERROR_BUDGET_PASS',input_sha256=hashes,raw_working_precision_bits=1024,raw_Laplace_terms=128,physical_frame_working_precision_bits=4096,flint_version=flint.__version__,retained_source_count=242,critical_target_count=4,exact_dyadic_frame_transform_sha256=digest.hexdigest(),physical_frame_error_row_upper=[str(rat(x.upper())) for x in errors],physical_frame_Gram_lower='99/100',critical_physical_Gram_lower='99/100',frame_Frobenius_norm_upper=str(normhi),maximum_raw_native_radius=str(rho),uniform_transport_Frobenius_error_squared_upper=str(uniform2),diagnostic_transported_error_target_bits=80,diagnostic_budget_is_Schur_budget=False,transported_signed_frame_block_native=values,transported_native_radius_Frobenius_squared_upper=str(rat(radius2.upper())),physical_finite_form_coupling_Frobenius_upper=str(bound),old_all_component_intervals_overlap=True,all_968_prime_pole_checks_passed=z['all_968_seven_prime_and_true_pole_cross_checks_passed'],same_accepted_physical_frame_verified=True,critical_quotient_normalized=False,strong_complementary_action_computed=False,full_selected_signed_matrix_computed=False,finite_BS_block_computed=False,signed_Schur_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
 assert time.monotonic()-start<120
 p=Path(a.output);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('JOINT RAW PRECISION / TAIL -> PHYSICAL FRAME PASS; error squared',float(uniform2),'native radius squared',float(rat(radius2.upper())),'finite form coupling bound',float(bound),'seconds',round(time.monotonic()-start,2))
if __name__=='__main__':main()
