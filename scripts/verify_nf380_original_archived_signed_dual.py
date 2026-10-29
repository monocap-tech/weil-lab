#!/usr/bin/env python3
"""NF380: one NEW original signed exterior coupling, REUSE archived certified WJJ/WJF.

No renewed 242x242 signed-kernel campaign. All original source labels, physical
J242 projections, complete seven-prime/arch/pole and operator-domain caveats
are unchanged. Correctly includes archival global frame/rounding uncertainty.
No W-ODD-NEG or RH claim from a finite dual result.
"""
import argparse,hashlib,json,zipfile,time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as physical
from verify_rpb108_original_signed_frame_transport import candidate
from verify_rpb108_original_signed_bivariate_kernel import TwoKernel
from verify_nf374_original_matched_curvature import load,dyad,RANK_SHA,PR355_SHA,NF369_SHA,TNUM
from verify_nf379_original_unfitted_signed_dual import makeF,hit,INDEX,PREC,SIGNED_PREC,LAPLACE_TERMS

ARCHIVE_SHA='f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
M_SHA='33b52b01e813982bd1a73b9bb81b0ca79f76e4bfd5af0821c4e13b4360bb40fa'
MIX_SHA='19356d4be60ee492896083c1bf6be18cd8ce2da058ff60008181f56a4c3ccc23'
FRAME_SHA='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'
SLICE_SHA='8148dfed729816d3af4a5ca20798f2a3454cfd99eb53621c8cd4646f24237df8'
NF375_SHA='f0067870a77f3825005395ac0f6f3e928521796ef3251c04463ba402c40cb5ec'

def rat(x):
 n,e=x.man_exp();return F(int(n))*F(2)**int(e)
def interval(x):return [str(rat(x.lower())),str(rat(x.upper()))]
def arbball(z):return arb(dyad(z[0]),dyad(z[1]))
def pad(x,r):return x+arb(0,r.upper())
def colnorm2(C,j):return sum((C[i,j]**2 for i in range(C.nrows())),arb(0)).upper()
def mat2_ball(M,vec1,vec2,eps):
    q=(vec1.transpose()*M*vec2)[0,0]
    payment=(eps*colnorm2(vec1,0).sqrt()*colnorm2(vec2,0).sqrt()).upper()
    return pad(q,payment)

def main():
 p=argparse.ArgumentParser()
 for name in ('rank','source','nf369','nf375','signed-slice','archive','output'):
  p.add_argument('--'+name,required=True)
 a=p.parse_args();start=time.monotonic()
 assert flint.__version__=='0.8.0'
 ctx.prec=PREC
 rank=load(a.rank,RANK_SHA);source=load(a.source,PR355_SHA)['data']
 parent=load(a.nf369,NF369_SHA)['data']
 budgetobj=load(a.nf375,NF375_SHA)
 signed_slice=load(a.signed_slice,SLICE_SHA)['data']
 budget=F(budgetobj['directions'][3]['original_residual_squared_budget']);assert budget>0
 raw=Path(a.archive).read_bytes();assert hashlib.sha256(raw).hexdigest()==ARCHIVE_SHA
 with zipfile.ZipFile(a.archive) as z:
  mat_bytes=z.read('original_selected_signed_matrix.json')
  mixed_bytes=z.read('original_exterior_refined_mixed.json')
 assert hashlib.sha256(mat_bytes).hexdigest()==M_SHA and hashlib.sha256(mixed_bytes).hexdigest()==MIX_SHA
 matrix=json.loads(mat_bytes);mixed=json.loads(mixed_bytes)
 assert matrix['selected_rank']==mixed['retained_source_count']==242
 assert matrix['complete_upper_triangle_entries']==242*243//2
 assert mixed['complete_mixed_entry_count']==968 and mixed['all_968_seven_prime_and_true_pole_cross_checks_passed']
 assert matrix['exact_dyadic_frame_transform_sha256']==FRAME_SHA
 assert matrix['input_sha256']['rank']==mixed['rank_input_sha256']==RANK_SHA
 assert matrix['Laplace_terms']==mixed['Laplace_terms']==384
 sq1=F(matrix['double_frame_uniform_error_Frobenius_squared_upper'])
 sq2=F(matrix['native_matrix_radius_Frobenius_squared_upper'])
 assert 0<=sq1<F(1,10**780) and 0<=sq2<F(1,10**810)
 assert parent['selected_rank']==242 and len(source['target_probes'])==4
 freqs,C=makeF(source)
 rows=[];clusters=[];expected=[];offset=0
 for (c,mmax),keep in zip(rank['original_nodes'],rank['selected_multiplicities']):
  assert 0<=keep<=mmax
  if keep:
   clusters.append((F(c),keep,len(rows)))
   for k in range(keep):rows.append((F(c),k));expected.append((offset+k,str(F(c)),k))
  offset+=mmax
 assert len(rows)==241 and rank['retained_original_pole'] and offset==469
 clusters.append((None,1,241));rows.append((None,0));expected.append((469,None,None))
 assert [(r['original_source_index'],r['center'],r['order']) for r in mixed['rows']]==expected
 J=[physical.pole_terms() if c is None else physical.source_terms(c,k) for c,k in rows]
 bases=[physical.source_terms(c,0) for c in freqs]+[physical.pole_terms()]
 Fs=[]
 for col in range(4):
  arr=[]
  for k in range(33):arr.extend((power,kind,ff,v*C[k,col]) for power,kind,ff,v in bases[k])
  Fs.append(arr)
 n=INDEX;center=F(5*n,11);assert center not in freqs and all(center!=c for c,k in rows if c is not None)
 v=physical.source_terms(center,0)
 targets=Fs+[v]
 print('NF380: original J242 physical frame and target projections (unchanged)',flush=True)
 kernel=physical.Integrals()
 H=arb_mat(242,242)
 for i in range(242):
  for j in range(i+1):H[i,j]=H[j,i]=physical.gram(J[i],J[j],kernel)
 D=candidate(H);N=D.transpose()*H*D
 assert max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))<arb('0.01')
 digest=hashlib.sha256()
 for i in range(242):
  for j in range(242):digest.update((json.dumps(physical.dyadic(D[i,j]),separators=(',',':'))+'\n').encode())
 assert digest.hexdigest()==FRAME_SHA,'physical frame DIFFERENT from original archived matrix'
 V=arb_mat([[physical.gram(j,x,kernel) for x in targets] for j in J])
 Y=N.solve(D.transpose()*V,algorithm='lu');X=D*Y
 assert max(abs((H*X-V)[i,j]).upper() for i in range(242) for j in range(5))<arb('1e-80')
 S=arb_mat([[physical.gram(targets[i],targets[j],kernel)-sum((V[k,i]*X[k,j] for k in range(242)),arb(0)) for j in range(5)] for i in range(5)])
 S=(S+S.transpose())/2
 for i in range(4):
  for j in range(4):assert (S[i,j]-arbball(parent['physical_quotient_Gram_native'][i][j])).contains(0),('original physical NF369',i,j)
 S4=arb_mat([[S[i,j] for j in range(4)] for i in range(4)])
 cross=arb_mat([[S[i,4]] for i in range(4)])
 eta=S4.solve(cross,algorithm='lu')
 qnorm=S[4,4];orth=qnorm-(cross.transpose()*eta)[0,0]
 assert qnorm.lower()>0 and orth.lower()>0
 ratio=orth/qnorm
 robust=bool(qnorm.lower()>arb('0.1') and ratio.lower()>arb('0.1'))
 print('NF380 original n512 physical q',qnorm,'relative outside fitted',ratio,'robust',robust,flush=True)
 if not robust:
  out=dict(standing='NF380_N512_ORIGINAL_PHYSICAL_CANDIDATE_METHOD_STOP',n=n,
   parent_16_original_physical_quotient_overlaps=True,
   original_physical_q_norm2=interval(qnorm),original_outside_E4_norm2=interval(orth),
   original_relative_out_of_fit_mass=interval(ratio),
   archival_original_selected_matrix_SHA256=M_SHA,archival_original_mixed_SHA256=MIX_SHA,
   old_signed_kernel_recomputation_avoided=True,new_original_signed_coupling_computed=False,
   signed_original_kernel_overlap_32=False,method_specific_obstruction_proved=False,
   W_ODD_NEG='OPEN',RH='OPEN')
  Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(out,indent=2)+'\n');return

 # Native corrected *old* signed WJJ is already available in M, in Q^T D^T WJJ D Q frame.
 M=arb_mat(242,242)
 for i,r in enumerate(matrix['finite_transformed_signed_matrix_upper_native']):
  assert len(r)==i+1
  for j,z in enumerate(r):M[i,j]=M[j,i]=arbball(z)
 Q=arb_mat([[int(i==j) for j in range(242)] for i in range(242)])
 for j,reflection in enumerate(matrix['householder_vectors']):
  assert reflection['start']==j and len(reflection['vector'])==242-j
  vv=arb_mat([[arb(0) if i<j else dyad(reflection['vector'][i-j])] for i in range(242)])
  dd=(vv.transpose()*vv)[0,0];assert dd.lower()>0
  Q=Q-2*(Q*vv)*vv.transpose()/dd
 QQ=Q.transpose()*Q
 assert max(sum((abs(QQ[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))<arb('1e-800')
 epsilon=physical.a(sq1+sq2).sqrt()  # archival frame error PLUS archive rounding: conservative
 # Original 968 raw signed mixed native cells are retained, never recalculated.
 L=arb_mat([[arbball(row['entries'][j]['signed_native']) for j in range(4)] for row in mixed['rows']])
 U=arb_mat([[arbball(z) for z in row] for row in mixed['target_signed_kernel_Gram_native']])
 DTL=D.transpose()*L
 Y4=arb_mat([[Y[i,j] for j in range(4)] for i in range(242)])
 QY4=Q.transpose()*Y4
 WXX=arb_mat(4,4)
 for i in range(4):
  for j in range(4):
   WXX[i,j]=mat2_ball(M,arb_mat([[QY4[k,i]] for k in range(242)]),arb_mat([[QY4[k,j]] for k in range(242)]),epsilon)
 WXL=Y4.transpose()*DTL
 CE=U-WXL-WXL.transpose()+WXX
 BP=WXL-WXX
 # Critical original 16 CE and 16 BP independent native source overlap check:
 for i in range(4):
  for j in range(4):
   assert (CE[i,j]-arbball(signed_slice['actual_exterior_signed_Gram_native'][i][j])).contains(0),('CE',i,j)
   assert (BP[i,j]-arbball(signed_slice['nf369_selected_to_original_quotient_signed_coupling_native'][i][j])).contains(0),('BP',i,j)
 print('NF380 archived signed M/WJF and ORIGINAL NF369 32 mixed overlap identities PASS',flush=True)
 # Only genuine NEW original signed kernel inputs: 242 J-v and 33 base-v cells.
 signed=TwoKernel(SIGNED_PREC,LAPLACE_TERMS)
 newJ=arb_mat(242,1)
 for c,pmax,offset in clusters:
  zz=hit(c,pmax,center,1,signed)
  for i in range(pmax):
   item=zz[i][0];assert item.imag.contains(0)
   newJ[offset+i,0]=item.real
 print('NF380 242 new J-v original arch+prime+pole mixed cells complete',flush=True)
 newBase=arb_mat(33,1)
 for i,c in enumerate(list(freqs)+[None]):
  item=hit(c,1,center,1,signed)[0][0];assert item.imag.contains(0)
  newBase[i,0]=item.real
 print('NF380 33 new original critical basis-v signed cells complete',flush=True)
 ctx.prec=PREC
 Y0=arb_mat([[dyad(parent['nf369_quotient_response_exact_dyadic_coefficients'][i][j]) for j in range(4)] for i in range(4)])
 T=arb_mat([[physical.a(F(x,2**20)) for x in row] for row in TNUM])
 Identity=arb_mat([[int(i==j) for j in range(4)] for i in range(4)])
 coeff=(Identity+Y0)*T
 alpha=Y4*arb_mat([[coeff[k,3]] for k in range(4)])
 f=-(Y0*T)[:,3] if False else arb_mat([[-(Y0*T)[k,3]] for k in range(4)])
 beta=arb_mat([[Y[i,4]-sum((Y[i,j]*eta[j,0] for j in range(4)),arb(0))] for i in range(242)])
 qalpha=Q.transpose()*alpha;qbeta=Q.transpose()*beta
 h=C.transpose()*newBase
 aq=(alpha.transpose()*D.transpose()*newJ)[0,0]
 fq=(f.transpose()*h)[0,0]
 aFeta=(alpha.transpose()*DTL*eta)[0,0]
 fFeta=(f.transpose()*U*eta)[0,0]
 aJbeta=mat2_ball(M,qalpha,qbeta,epsilon)
 fJbeta=(f.transpose()*DTL.transpose()*beta)[0,0]
 bperp=aq+fq-aFeta-fFeta-aJbeta-fJbeta
 assert bperp.is_finite()
 # Optional identical complete signed u4-E4 correlation, legacy fitted shadow check:
 WuaF=alpha.transpose()*DTL+f.transpose()*U
 WuaJX=arb_mat([[mat2_ball(M,qalpha,arb_mat([[QY4[k,j]] for k in range(242)]),epsilon) for j in range(4)]]) + f.transpose()*DTL.transpose()*Y4
 WuaE=WuaF-WuaJX
 # Original fitted E4 complete signed response is tiny; compare to prior exact archival certificate.
 fitted_upper=max(abs(WuaE[0,j]).upper() for j in range(4))
 assert fitted_upper<physical.a(F(1,10**45)),'original fitted-four signed action mismatch'
 abslo=arb(0) if bperp.contains(0) else min(abs(bperp.lower()),abs(bperp.upper()))
 dual_lower=(abslo*abslo/orth.upper()).lower()
 obstructs=bool(dual_lower>physical.a(budget))
 out=dict(standing='NF380 ORIGINAL ARCHIVAL REUSE FULL SIGNED ONE-WITNESS RESPONSE; ONLY METHOD-BOUND',
  parent_original_archive_sha256=ARCHIVE_SHA,archive_original_signed_matrix_sha256=M_SHA,
  archive_original_mixed_sha256=MIX_SHA,original_frame_sha256=FRAME_SHA,
  original_rank_sha256=RANK_SHA,original_source_sha256=PR355_SHA,
  selected_rank=242,critical_count=4,unfitted_n=n,
  physical_q_norm2_interval=interval(qnorm),outside_E4_norm2_interval=interval(orth),
  relative_outside_E4_mass_interval=interval(ratio),
  original_physical_16_Gram_overlaps=True,original_signed_32_CE_BP_overlaps=True,
  archive_selected_native_error_frobenius_squared_upper=str(sq1+sq2),
  archive_four_fitted_response_abs_upper=str(fitted_upper),
  actual_new_signed_J_v_cells=242,actual_new_signed_basis_v_cells=33,
  original_WJJ_WJF_archived_cells_reused=29403+968,
  complete_original_signed_u4_qperp_interval=interval(bperp),
  dual_squared_strict_lower=str(rat(dual_lower)),
  original_direction_four_squared_residual_budget=str(budget),
  method_specific_sufficient_residual_obstructed=obstructs,
  original_lowband_integral_computed=False,
  entire_exterior_inverse_computed=False,analytic_domain_review='OPEN',
  W_ODD_NEG='OPEN',RH='OPEN',elapsed_seconds=time.monotonic()-start)
 pp=Path(a.output);pp.parent.mkdir(parents=True,exist_ok=True);pp.write_text(json.dumps(out,indent=2)+'\n')
 print('NF380 actual original SIGNED one-witness response interval',str(bperp)[:140],
       'method-specific STOP?',obstructs,'elapsed',round(time.monotonic()-start,2),flush=True)

if __name__=='__main__':main()
