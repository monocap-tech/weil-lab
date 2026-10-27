#!/usr/bin/env python3
"""Complete selected original signed matrix and matched finite Schur4 certificate."""
import argparse,hashlib,json,time,sys
sys.set_int_max_str_digits(100000)
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import flint
from flint import arb,acb,acb_series,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as m
import verify_rpb108_si29_original_prime_mixed as translated
from verify_rpb108_original_signed_frame_transport import candidate
from verify_rpb108_original_signed_bivariate_kernel import TwoKernel
FRAME='e78c29dc930274e5522c665d073044a6de6ac1fee832cac65c13128f57fe80d4'
RANK='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
BUDGET='eececa96d8db2ab1625c79bf3a13d2ce14d2de97c921c9dec967834281f16e90'
BLOCK='2cb869033f2c6722d356e769f35fc0e1b041ae46a8c11360e66cd7d2c694c548'
def dy(x):
 n,e=x.man_exp();return [str(n),int(e)]
def rat(x):
 n,e=x.man_exp();return F(int(n))*F(2)**int(e)
def ball(x):return [dy(x.mid()),dy(x.rad())]
def exact(v):return arb((int(v[0]),int(v[1])))
def rounded(x,bits):
 old=ctx.prec;ctx.prec=bits;y=x+arb(0);ctx.prec=old;return y

def householder(columns):
 n=len(columns);Q=arb_mat([[int(i==j) for j in range(n)] for i in range(n)]);vs=[]
 for j in range(4):
  u=arb_mat([[exact(columns[i][j])] for i in range(n)]);y=Q.transpose()*u
  v=arb_mat(n,1)
  for i in range(j,n):v[i,0]=rounded(y[i,0],256).mid()
  length=sum((y[i,0]**2 for i in range(j,n)),arb(0)).sqrt()
  v[j,0]=rounded(v[j,0]+(1 if y[j,0].mid()>=0 else -1)*length,256).mid()
  den=sum((v[i,0]**2 for i in range(n)),arb(0));assert den>0
  Q=Q-2*(Q*v)*v.transpose()/den
  vs.append(dict(start=j,vector=[dy(v[i,0]) for i in range(j,n)]))
 E=Q.transpose()*Q;errors=[sum((abs(E[i,j]-int(i==j)) for j in range(n)),arb(0)) for i in range(n)];assert max(errors)<arb('1e-900')
 return Q,vs,errors

def pivots4(M):
 L=arb_mat(4,4);ds=[]
 for i in range(4):
  for j in range(i):
   if ds[j].contains(0):return None
   L[i,j]=(M[i,j]-sum((L[i,k]*L[j,k]*ds[k] for k in range(j)),arb(0)))/ds[j]
  L[i,i]=1;ds.append(M[i,i]-sum((L[i,k]**2*ds[k] for k in range(i)),arb(0)))
 return ds

def main():
 p=argparse.ArgumentParser()
 for name in ['frame','rank','budget','block','candidate','output']:p.add_argument('--'+name,required=True)
 a=p.parse_args();start=time.monotonic();data={};hashes={}
 for name,sha in [('frame',FRAME),('rank',RANK),('budget',BUDGET),('block',BLOCK),('candidate',None)]:
  raw=Path(getattr(a,name)).read_bytes();h=hashlib.sha256(raw).hexdigest();assert sha is None or sha==h;data[name]=json.loads(raw);hashes[name]=h
 assert flint.__version__=='0.8.0';rank=data['rank'];rows=data['block']['rows'];fixed=data['candidate'];assert fixed['dimension']==242 and fixed['critical_columns']==4
 assert len(fixed['columns'])==242 and all(len(r)==4 for r in fixed['columns'])
 k=TwoKernel(3072,384);W=arb_mat(242,242);clusters=[];offset=0
 for (c,pmax),n in zip(rank['original_nodes'],rank['selected_multiplicities']):
  if n:clusters.append((F(c),n,offset));offset+=n
 assert offset==241;clusters.append((None,1,241));assert rows[-1]['original_source_index']==469
 phy=m.Integrals();terms=[m.pole_terms() if r['original_source_index']==469 else m.source_terms(F(r['center']),r['order']) for r in rows]
 sourcepoles=[m.gram(t,m.pole_terms(),phy) for t in terms]
 clips=[]
 for power,prime in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]:
  clip=translated.Clipped(arb(power).log());clips.append((2*arb(prime).log()/arb(power).sqrt(),clip,[translated.shifted(t,clip) for t in terms]))
 rho=F(0);count=0;componenthash=hashlib.sha256();rawhash=hashlib.sha256();diagonal_checks=0;onevar_checks=0
 for ci,(c,p,base) in enumerate(clusters):
  for cj,(d,q,other) in enumerate(clusters[:ci+1]):
   parts=k.block(c,d,p,q)
   if c==d:
    point=k.k.diagonal(k.frequency(c));assert all((parts[j][0][0]-point[j]).contains(0) for j in range(3));diagonal_checks+=1
    assert all((parts[j][u][v]-parts[j][v][u]).contains(0) for j in range(3) for u in range(p) for v in range(q))
   else:
    Ac,Ic=k.data(c,p);Ad,Id=k.data(d,q);ctx.cap=p;v=acb_series([k.frequency(c),1]);Av=acb_series(Ac[:p]);Iv=acb_series(Ic[:p]);old=k.k.mixed(v,Av,Iv,k.frequency(d),Ad[0],Id[0],c is None)
    assert all((parts[j][u][0]-(old[j][u] if isinstance(old[j],acb_series) else old[j])).contains(0) for j in range(3) for u in range(p));onevar_checks+=p*3
   for u in range(p):
    for v in range(q):
     if c==d and u<v:continue
     i,j=base+u,other+v
     factor=(-k.k.I if c is None else (-1)**(u//2)*factorial(u))*(-k.k.I if d is None else (-1)**(v//2)*factorial(v))
     vals=[part[u][v]*factor for part in parts];assert all(x.imag.contains(0) for x in vals)
     independent_prime=-sum((w*translated.clipped_gram(terms[i],shifted[j],clip) for w,clip,shifted in clips),arb(0));independent_pole=-2*sourcepoles[i]*sourcepoles[j]
     assert (vals[1].real-independent_prime).contains(0),(i,j,'prime');assert (vals[2].real-independent_pole).contains(0),(i,j,'pole')
     value=sum(vals,acb(0));assert value.is_finite() and value.imag.contains(0);W[i,j]=W[j,i]=value.real;rho=max(rho,rat(value.real.rad()));count+=1
     componenthash.update((json.dumps([i,j,[ball(x.real) for x in vals],ball(independent_prime),ball(independent_pole)],separators=(',',':'))+'\n').encode())
     rawhash.update((json.dumps([i,j,ball(value.real)],separators=(',',':'))+'\n').encode())
  if ci%10==0:print('Completed cluster',ci,'entries',count,'seconds',round(time.monotonic()-start,2),flush=True)
  assert time.monotonic()-start<150,'bounded complete signed raw matrix plus independent checks guard'
 assert count==242*243//2
 print('COMPLETE original raw matrix AND all prime/pole checks',count,'seconds',round(time.monotonic()-start,2),flush=True)
 ctx.prec=4096;phy=m.Integrals();terms=[m.pole_terms() if r['original_source_index']==469 else m.source_terms(F(r['center']),r['order']) for r in rows];H=arb_mat(242,242)
 for i in range(242):
  for j in range(i+1):H[i,j]=H[j,i]=m.gram(terms[i],terms[j],phy)
 D=candidate(H);N=D.transpose()*H*D;errs=[sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242)];assert max(errs)<arb('0.01')
 digest=hashlib.sha256()
 for i in range(242):
  for j in range(242):digest.update((json.dumps(m.dyadic(D[i,j]),separators=(',',':'))+'\n').encode())
 assert digest.hexdigest()==data['frame']['exact_dyadic_frame_transform_sha256']
 norm=rat(sum((D[i,j]**2 for i in range(242) for j in range(242)),arb(0)).sqrt().upper());assert norm<F(2)**496
 uniform2=F(2)**(4*496)*242**2*rho**2;assert uniform2<F(2)**-160
 T=D.transpose()*W*D;Q,vs,qerr=householder(fixed['columns']);M0=Q.transpose()*T*Q
 M=arb_mat(242,242)
 for i in range(242):
  for j in range(i+1):
   assert (M0[i,j]-M0[j,i]).contains(0)
   M[i,j]=M[j,i]=rounded(M0[i,j],1536)
 radius2=rat(sum((M[i,j].rad()**2 for i in range(242) for j in range(242)),arb(0)).upper());assert radius2<F(2)**-160
 hi=arb_mat([[M[i,j] for j in range(4,242)] for i in range(4,242)]);B=arb_mat([[M[i,j] for j in range(4)] for i in range(4,242)]);C=arb_mat([[M[i,j] for j in range(4)] for i in range(4)])
 Dhi=candidate(hi);Nh=Dhi.transpose()*hi*Dhi;herr=[sum((abs(Nh[i,j]-int(i==j)) for j in range(238)),arb(0)) for i in range(238)];assert max(herr)<arb('0.01')
 hinorm2=rat(sum((Dhi[i,j]**2 for i in range(238) for j in range(238)),arb(0)).upper());gamma=F(99,100)/hinorm2;assert gamma>0
 Y=hi.solve(B,algorithm='lu');Ymid=arb_mat([[rounded(Y[i,j],1024).mid() for j in range(4)] for i in range(238)])
 Z=hi*Ymid;R=Z-B;res2=rat(sum((abs(R[i,j])**2 for i in range(238) for j in range(4)),arb(0)).upper());penalty=res2/gamma
 upper=C-B.transpose()*Ymid-Ymid.transpose()*B+Ymid.transpose()*Z
 lower=upper-arb_mat([[arb(str(penalty)) if i==j else arb(0) for j in range(4)] for i in range(4)])
 piv=pivots4(lower);positive=piv is not None and all(v>0 for v in piv)
 print('FINITE complement238 floor',float(gamma),'Schur4 lower pivots',[v.str(8) for v in piv] if piv else 'unresolved','positive',positive,flush=True)
 out=dict(status='CONDITIONAL_COMPLETE_ORIGINAL_SELECTED_SIGNED_MATRIX_AND_FINITE_SCHUR',input_sha256=hashes,raw_working_precision_bits=3072,Laplace_terms=384,Laplace_tail_exponent=k.k.tail_exponent,analytic_tail_strip_imaginary_bound='3/4',Cauchy_radius='1/4',raw_Laplace_tail_upper=str(rat(k.k.tail)),flint_version=flint.__version__,selected_rank=242,complete_upper_triangle_entries=count,complete_real_matrix_entries=242**2,all_prime_pole_physical_cross_checks=count,coincident_block_diagonal_checks=diagonal_checks,distinct_one_variable_coefficient_checks=onevar_checks,maximum_required_I_jet_order=27,raw_component_and_independent_checks_sha256=componenthash.hexdigest(),raw_signed_matrix_sha256=rawhash.hexdigest(),maximum_raw_entry_radius=str(rho),physical_frame_working_precision_bits=4096,exact_dyadic_frame_transform_sha256=digest.hexdigest(),physical_frame_error_row_upper=[str(rat(x.upper())) for x in errs],frame_Frobenius_norm_upper=str(norm),double_frame_uniform_error_Frobenius_squared_upper=str(uniform2),diagnostic_transport_target_bits=80,diagnostic_target_is_Schur_budget=False,householder_vectors=vs,householder_orthogonality_error_row_upper=[str(rat(x.upper())) for x in qerr],finite_transformed_signed_matrix_upper_native=[[ball(M[i,j]) for j in range(i+1)] for i in range(242)],native_matrix_radius_Frobenius_squared_upper=str(radius2),finite_complement_dimension=238,finite_complement_preconditioned_error_row_upper=[str(rat(x.upper())) for x in herr],finite_complement_preconditioner_Frobenius_squared_upper=str(hinorm2),finite_complement_coefficient_floor=str(gamma),matched_exact_dyadic_inverse_action_candidate=[[dy(Ymid[i,j]) for j in range(4)] for i in range(238)],matched_forcing_residual_Frobenius_squared_upper=str(res2),finite_Schur_remainder_operator_upper=str(penalty),finite_Schur_upper_native=[[ball(upper[i,j]) for j in range(4)] for i in range(4)],finite_Schur_lower_native=[[ball(lower[i,j]) for j in range(4)] for i in range(4)],finite_Schur_lower_pivots_native=[ball(v) for v in piv] if piv else None,finite_selected_signed_positive_definite_certified=positive,global_complementary_action_computed=False,full_infinite_Schur_certified=False,finite_BS_block_computed=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
 assert time.monotonic()-start<300,'bounded total finite block / Schur guard'
 path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('COMPLETE FINITE SIGNED MATRIX PASS; positivity',positive,'seconds',round(time.monotonic()-start,2),flush=True)
if __name__=='__main__':main()
