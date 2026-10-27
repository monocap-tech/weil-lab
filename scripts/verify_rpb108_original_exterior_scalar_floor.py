#!/usr/bin/env python3
"""Actual exterior residual probes against four finite signed-energy directions.

Tests the sufficient L2 exterior-floor route; does not bound the full
infinite inverse-complement Schur correction above.
"""
import argparse,hashlib,json,time,sys
from pathlib import Path
from fractions import Fraction as F
import flint
from flint import arb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as m
from verify_rpb108_original_signed_frame_transport import candidate
sys.set_int_max_str_digits(100000)
MATRIX='33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa'
FRAME='e78c29dc930274e5522c665d073044a6de6ac1fee832cac65c13128f57fe80d4'
RANK='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
CRITICAL='a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'
def dy(x):
 n,e=x.man_exp();return [str(n),int(e)]
def rat(x):
 n,e=x.man_exp();return F(int(n))*F(2)**int(e)
def exact(v):return arb((int(v[0]),int(v[1])))
def fromball(v):return arb(exact(v[0]),exact(v[1]))
def ball(x):return [dy(x.mid()),dy(x.rad())]
def balls(M):return [[ball(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def interval(x):return [str(rat(x.lower())),str(rat(x.upper()))]
def rounded_mid(x,bits=1024):
 old=ctx.prec;ctx.prec=bits;y=(x+arb(0)).mid();ctx.prec=old;return y
def midmatrix(M):return arb_mat([[rounded_mid(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())])
def identity_errors(M):return [rat(sum((abs(M[i,j]-int(i==j)) for j in range(M.ncols())),arb(0)).upper()) for i in range(M.nrows())]
def main():
 p=argparse.ArgumentParser()
 for name in ['matrix','frame','rank','critical','mixed','output']:p.add_argument('--'+name,required=True)
 a=p.parse_args();start=time.monotonic();data={};hashes={}
 for name,sha in [('matrix',MATRIX),('frame',FRAME),('rank',RANK),('critical',CRITICAL),('mixed',None)]:
  raw=Path(getattr(a,name)).read_bytes();h=hashlib.sha256(raw).hexdigest();assert sha is None or h==sha;data[name]=json.loads(raw);hashes[name]=h
 z=data['matrix'];mixed=data['mixed'];rank=data['rank'];cr=data['critical'];frame=data['frame']
 assert z['finite_selected_signed_positive_definite_certified'] and z['selected_rank']==242
 assert mixed['working_precision_bits']==3072 and mixed['Laplace_terms']==384 and mixed['Laplace_tail_exponent']==2420
 assert mixed['rank_input_sha256']==RANK and mixed['critical_input_sha256']==CRITICAL
 assert mixed['target_probes']==cr['exact_candidates']['probes'] and mixed['target_sine_frequencies']==cr['exact_candidates']['sine_frequencies']
 assert mixed['all_968_seven_prime_and_true_pole_cross_checks_passed'] and mixed['complete_mixed_entry_count']==968
 assert flint.__version__=='0.8.0';ctx.prec=4096;rows=mixed['rows'];assert len(rows)==242
 terms=[m.pole_terms() if r['original_source_index']==469 else m.source_terms(F(r['center']),r['order']) for r in rows]
 H=arb_mat(242,242);phy=m.Integrals()
 for i in range(242):
  for j in range(i+1):H[i,j]=H[j,i]=m.gram(terms[i],terms[j],phy)
 D=candidate(H);N=D.transpose()*H*D;errors=identity_errors(N);assert max(errors)<F(1,100)
 digest=hashlib.sha256()
 for i in range(242):
  for j in range(242):digest.update((json.dumps(m.dyadic(D[i,j]),separators=(',',':'))+'\n').encode())
 assert digest.hexdigest()==z['exact_dyadic_frame_transform_sha256']==frame['exact_dyadic_frame_transform_sha256']
 Q=arb_mat([[int(i==j) for j in range(242)] for i in range(242)])
 for j,vdata in enumerate(z['householder_vectors']):
  assert vdata['start']==j;v=arb_mat(242,1)
  for i,value in enumerate(vdata['vector'],j):v[i,0]=exact(value)
  den=sum((v[i,0]**2 for i in range(242)),arb(0));assert den>0;Q=Q-2*(Q*v)*v.transpose()/den
 qerrors=identity_errors(Q.transpose()*Q);assert max(qerrors)<F(1,10**900)
 G=Q.transpose()*N*Q;assert max(identity_errors(G))<F(1,100)
 U=D*Q
 # Original physical functions F and exact defining projection X=G^-1 U*F.
 cs=list(map(F,mixed['target_sine_frequencies']));targets=[]
 for probe in mixed['target_probes']:
  t=[]
  for c,coef in zip(cs,map(F,probe['sine_coefficients'])):t.extend((p,tau,f,v*m.a(coef)) for p,tau,f,v in m.source_terms(c,0))
  t.extend((p,tau,f,v*m.a(F(probe['sinh_coefficient']))) for p,tau,f,v in m.pole_terms());targets.append(t)
 JF=arb_mat([[m.gram(t,f,phy) for f in targets] for t in terms]);Fm=arb_mat([[m.gram(f,g,phy) for g in targets] for f in targets]);V=U.transpose()*JF
 X=G.solve(V,algorithm='lu');S=Fm-V.transpose()*X
 Scheck=Fm-V.transpose()*X-X.transpose()*V+X.transpose()*G*X
 assert all((S[i,j]-Scheck[i,j]).contains(0) for i in range(4) for j in range(4))
 for i in range(4):
  for j in range(4):
   lo,hi=map(F,frame['physical_critical_quotient_Gram_intervals'][i][j]);assert (S[i,j]-arb(str((lo+hi)/2),arb(str((hi-lo)/2)))).contains(0)
 DE=candidate(S);serr=identity_errors(DE.transpose()*S*DE);assert max(serr)<F(1,100)
 # All retained finite signed entries are original coordinate M=U*W U.
 M=arb_mat(242,242)
 for i,row in enumerate(z['finite_transformed_signed_matrix_upper_native']):
  for j,b in enumerate(row):M[i,j]=M[j,i]=fromball(b)
 Gamma=arb_mat([[fromball(e['signed_native']) for e in row['entries']] for row in rows]);T=U.transpose()*Gamma
 FQ=arb_mat([[fromball(b) for b in row] for row in mixed['target_signed_kernel_Gram_native']])
 exterior_coupling=T-M*X
 CE=FQ-T.transpose()*X-X.transpose()*T+X.transpose()*M*X
 mu=F(1,1000)-F(rank['pruned_physical_complement_negative_upper']);assert mu>F(98,10**5)
 Cscaled=DE.transpose()*(CE-m.a(mu)*S)*DE;DC=candidate(Cscaled);cerr=identity_errors(DC.transpose()*Cscaled*DC);assert max(cerr)<F(1,100)
 # Source signed-energy coordinates come entirely from the accepted finite
 # matched Schur split, with exact dyadic coefficient choices.
 SL=arb_mat([[fromball(b) for b in row] for row in z['finite_Schur_lower_native']]);A4=midmatrix(candidate(SL));Y=arb_mat([[exact(v) for v in row] for row in z['matched_exact_dyadic_inverse_action_candidate']])
 P=midmatrix(arb_mat([[A4[i,j] for j in range(4)] for i in range(4)]+[[-sum((Y[i,k]*A4[k,j] for k in range(4)),arb(0)) for j in range(4)] for i in range(238)]))
 Energy=P.transpose()*M*P;energyerr=identity_errors(Energy);assert max(energyerr)<F(1,100)
 Z=exterior_coupling.transpose()*P
 Yl2=midmatrix(S.solve(Z,algorithm='lu'));L2lower=Z.transpose()*Yl2+Yl2.transpose()*Z-Yl2.transpose()*S*Yl2
 Yc=midmatrix(CE.solve(Z,algorithm='lu'));Schurlower=Z.transpose()*Yc+Yc.transpose()*Z-Yc.transpose()*CE*Yc
 snorm2=rat(sum((DE[i,j]**2 for i in range(4) for j in range(4)),arb(0)).upper());sfloor=F(99,100)/snorm2;cfloor=mu*sfloor
 RC=CE*Yc-Z;rc2=rat(sum((abs(RC[i,j])**2 for i in range(4) for j in range(4)),arb(0)).upper());rhoC=rc2/cfloor
 # This is an upper bound for the FOUR-PROBE Galerkin correction only.
 probe_trace_upper=sum((rat(Schurlower[i,i].upper()) for i in range(4)),F(0))+4*rhoC
 probe_energy_operator_upper=probe_trace_upper/F(99,100)
 assert probe_energy_operator_upper<F(2,1000)

 cases=[]
 for i in range(4):
  qlo,qhi=map(F,interval(Energy[i,i]));blo,bhi=map(F,interval(L2lower[i,i]));clo,chi=map(F,interval(Schurlower[i,i]));assert qlo>0
  ratio=blo/(mu*qhi);actual_lower_ratio=clo/qhi
  cases.append(dict(direction=i,source_signed_energy_interval=[str(qlo),str(qhi)],projected_strong_norm_variational_interval=[str(blo),str(bhi)],scalar_floor_budget_upper=str(mu*qhi),scalar_floor_violation_factor_lower=str(ratio),complementary_Schur_variational_interval=[str(clo),str(chi)],complementary_Schur_fraction_lower=str(actual_lower_ratio),four_probe_Schur_fraction_upper=str((chi+rhoC)/qlo)))
 stopped=any(F(v['scalar_floor_violation_factor_lower'])>1 for v in cases)
 negative_extension=any(F(v['complementary_Schur_fraction_lower'])>1 for v in cases)
 out=dict(status='CONDITIONAL_ORIGINAL_ACTUAL_EXTERIOR_PROBE_SCALAR_FLOOR_DIAGNOSTIC',input_sha256=hashes,working_precision_bits=4096,raw_mixed_precision_bits=3072,raw_mixed_Laplace_terms=384,flint_version=flint.__version__,selected_rank=242,existing_critical_witness_count=4,source_direction_count=4,physical_frame_transform_sha256=digest.hexdigest(),physical_frame_error_row_upper=list(map(str,errors)),householder_orthogonality_error_row_upper=list(map(str,qerrors)),physical_quotient_Gram_native=balls(S),physical_quotient_normalized_error_row_upper=list(map(str,serr)),actual_exterior_signed_Gram_native=balls(CE),exterior_floor_subtraction_preconditioned_error_row_upper=list(map(str,cerr)),signed_energy_source_exact_dyadic_coefficients=[[dy(P[i,j]) for j in range(4)] for i in range(242)],signed_energy_Gram_native=balls(Energy),signed_energy_error_row_upper=list(map(str,energyerr)),actual_exterior_weak_coupling_native=balls(Z),exact_L2_variational_coefficients=[[dy(Yl2[i,j]) for j in range(4)] for i in range(4)],projected_strong_norm_variational_lower_matrix_native=balls(L2lower),exact_complement_variational_coefficients=[[dy(Yc[i,j]) for j in range(4)] for i in range(4)],complementary_Schur_variational_lower_matrix_native=balls(Schurlower),physical_quotient_preconditioner_Frobenius_squared_upper=str(snorm2),physical_quotient_coefficient_floor=str(sfloor),four_probe_signed_coefficient_floor=str(cfloor),four_probe_inverse_action_residual_Frobenius_squared_upper=str(rc2),four_probe_Schur_remainder_operator_upper=str(rhoC),four_probe_Schur_energy_operator_upper=str(probe_energy_operator_upper),four_probe_upper_is_global_upper=False,inherited_global_exterior_floor=str(mu),cases=cases,scalar_floor_strong_action_method_stopped=stopped,negative_extension_witness_found=negative_extension,complete_strong_action_computed=False,global_Schur_penalty_upper_computed=False,global_infinite_Schur_sign_certified=False,physical_residuals_are_exact_defining_projection=True,rounded_projection_treated_as_exact=False,selected_source_space_enlarged=False,new_original_witnesses_introduced=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
 assert time.monotonic()-start<150,'bounded exterior physical projection / actual coupling diagnostic'
 path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('ACTUAL EXTERIOR COUPLING PROBE: scalar floor stopped',stopped,'negative finite extension',negative_extension,'seconds',round(time.monotonic()-start,2),flush=True)
 print('Refined raw native radius',arb(mixed['maximum_native_block_radius']).str(8),flush=True)
 for case in cases:print('direction',case['direction'],'scalar violation factor lower',arb(case['scalar_floor_violation_factor_lower']).str(8),'four-probe Schur fraction lower',arb(case['complementary_Schur_fraction_lower']).str(8),flush=True)
if __name__=='__main__':main()
