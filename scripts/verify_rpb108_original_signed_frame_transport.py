#!/usr/bin/env python3
"""Bounded original selected physical frame and independent-box error transport."""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
import flint
from flint import arb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as m
RANK='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
BLOCK='2cb869033f2c6722d356e769f35fc0e1b041ae46a8c11360e66cd7d2c694c548'
def rat(x):
 n,e=x.man_exp();return F(int(n))*F(2)**int(e)
def ball(v):return arb(arb((int(v[0][0]),int(v[0][1]))),arb((int(v[1][0]),int(v[1][1]))))
def interval(x):return [str(rat(x.lower())),str(rat(x.upper()))]
def candidate(H):
 n=H.nrows();L=arb_mat(n,n)
 for i in range(n):
  for j in range(i+1):
   x=(H[i,j].mid()-sum((L[i,k]*L[j,k] for k in range(j)),arb(0))).mid()
   if i==j:assert x>0;L[i,j]=x.sqrt().mid()
   else:L[i,j]=(x/L[j,j]).mid()
 I=arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
 return L.transpose().solve(I,algorithm='lu').mid()
def main():
 p=argparse.ArgumentParser();p.add_argument('--rank',required=True);p.add_argument('--block',required=True);p.add_argument('--output',required=True);args=p.parse_args();start=time.monotonic();data={}
 for name,sha in [('rank',RANK),('block',BLOCK)]:
  raw=Path(getattr(args,name)).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha;data[name]=json.loads(raw)
 z=data['block'];r=data['rank'];rows=z['rows'];assert len(rows)==242 and z['complete_mixed_entry_count']==968
 expected=[];offset=0
 for (c,pmax),count in zip(r['original_nodes'],r['selected_multiplicities']):
  expected.extend((offset+j,str(F(c)),j) for j in range(count));offset+=pmax
 expected.append((469,None,None));assert [(v['original_source_index'],v['center'],v['order']) for v in rows]==expected
 assert flint.__version__=='0.8.0';ctx.prec=4096;kernel=m.Integrals()
 terms=[m.pole_terms() if v['original_source_index']==469 else m.source_terms(F(v['center']),v['order']) for v in rows]
 H=arb_mat(242,242)
 for i in range(242):
  for j in range(i+1):H[i,j]=H[j,i]=m.gram(terms[i],terms[j],kernel)
 D=candidate(H);N=D.transpose()*H*D
 errors=[sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242)]
 assert max(errors)<arb('0.01');assert time.monotonic()-start<120
 print('Original selected physical frame verified',round(time.monotonic()-start,2),flush=True)
 digest=hashlib.sha256()
 for i in range(242):
  for j in range(242):digest.update((json.dumps(m.dyadic(D[i,j]),separators=(',',':'))+'\n').encode())
 C=arb_mat([[ball(e['signed_native']) for e in row['entries']] for row in rows]);T=D.transpose()*C
 # Exact defining D is dyadic; interval R encloses the EXACT range radius of
 # the linear image of the independent Cartesian input box. It need not be
 # an attained error of the actual correlated analytic entries.
 def input_radius(j,t):
  v=rows[j]['entries'][t]['signed_native'][1]
  return arb((int(v[0]),int(v[1])))
 R=arb_mat([[sum((abs(D[j,i])*input_radius(j,t) for j in range(242)),arb(0)) for t in range(4)] for i in range(242)])
 worst=max(((rat(R[i,t].lower()),i,t) for i in range(242) for t in range(4)));assert worst[0]>10**30
 norm2=sum((D[i,j]**2 for i in range(242) for j in range(242)),arb(0));norm=norm2.sqrt();E=0
 while not norm<arb(2)**E:E+=1
 # Diagnostic target ONLY. This is not an established Schur stability budget.
 target=80;rawbits=E+5+target
 assert 968<32**2 and norm*arb(968).sqrt()*arb(2)**(-rawbits)<arb(2)**(-target)
 targets=[]
 for av,b in zip([list(map(F,x['sine_coefficients'])) for x in z['target_probes']],[F(x['sinh_coefficient']) for x in z['target_probes']]):
  tr=[]
  for c,a in zip(map(F,z['target_sine_frequencies']),av):tr.extend((p,t,f,v*m.a(a)) for p,t,f,v in m.source_terms(c,0))
  tr.extend((p,t,f,v*m.a(b)) for p,t,f,v in m.pole_terms());targets.append(tr)
 B=arb_mat([[m.gram(src,f,kernel) for f in targets] for src in terms]);Fm=arb_mat([[m.gram(f,g,kernel) for g in targets] for f in targets])
 V=D.transpose()*B;Y=N.solve(V,algorithm='lu');S=Fm-V.transpose()*Y
 # Verify the physical quotient via the equivalent residual Gram including
 # both cross terms, rather than interpreting a rounded projection as exact.
 S2=Fm-V.transpose()*Y-Y.transpose()*V+Y.transpose()*N*Y
 assert all((S[i,j]-S2[i,j]).contains(0) for i in range(4) for j in range(4))
 assert all(S[i,i]>0 for i in range(4))
 out=dict(status='CONDITIONAL_SELECTED_PHYSICAL_FRAME_AND_RAW_BOX_TRANSPORT_STOP',rank_input_sha256=RANK,block_input_sha256=BLOCK,working_precision_bits=4096,flint_version=flint.__version__,retained_source_count=242,critical_target_count=4,exact_dyadic_frame_transform_sha256=digest.hexdigest(),physical_frame_error_row_upper=[str(rat(x.upper())) for x in errors],physical_frame_Gram_lower='99/100',physical_frame_Gram_upper='101/100',frame_coefficient_max_interval=interval(max(abs(D[i,j]) for i in range(242) for j in range(242))),frame_Frobenius_norm_interval=interval(norm),frame_Frobenius_norm_power_two_exponent=E,transported_independent_box_radius_intervals=[[interval(R[i,t]) for t in range(4)] for i in range(242)],worst_box_row=worst[1],worst_box_target=worst[2],worst_box_exact_dyadic_frame_column=[m.dyadic(D[j,worst[1]]) for j in range(242)],worst_box_radius_lower=str(worst[0]),diagnostic_transported_Frobenius_error_target_bits=target,uniform_raw_entry_absolute_error_sufficient_bits=rawbits,diagnostic_budget_is_Schur_budget=False,current_native_transported_radius_max_interval=interval(max(T[i,t].rad() for i in range(242) for t in range(4))),physical_critical_quotient_Gram_intervals=[[interval(S[i,j]) for j in range(4)] for i in range(4)],quotient_diagonal_positive=True,quotient_conditioning_certified=False,physical_frame_verified=True,current_independent_raw_box_transport_inconclusive=True,actual_analytic_correlated_error_lower_bound_claimed=False,precision_only_change_without_Laplace_tail_change_sufficient_claimed=False,full_selected_signed_matrix_computed=False,strong_complementary_coupling_computed=False,signed_Schur_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
 assert time.monotonic()-start<120
 path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,separators=(',',':'))+'\n')
 print('FRAME / BOX TRANSPORT STOP PASS; D norm < 2^%d; uniform raw error 2^-%d gives diagnostic 2^-80; seconds %.2f'%(E,rawbits,time.monotonic()-start))
if __name__=='__main__':main()
