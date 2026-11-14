#!/usr/bin/env python3
"""NF519 true-source original J242 exact physical-frame error and gap gates.

SHA-pin original NF505 and locally certified NF518 Galerkin vector.
Acceptance uses exact Fractions throughout. The 242x242 original raw
historical D frame, raw beta, actual e_D and kernel gap are still OPEN.
"""
import argparse,hashlib,json,math,sys
from fractions import Fraction as Q
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
N505="ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec"
N518="926f8d00d28212f542351760e0c1d814413e8a36a3367d6a58bf837c53865438"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
FRAME="18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf5666e36b430e"
B=Q(549,500)
def read(p):
 b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def sinh_upper(x,n=50):
 s=sum((x**(2*k+1)/math.factorial(2*k+1) for k in range(n)),Q(0))
 first=x**(2*n+1)/math.factorial(2*n+1)
 ratio=x*x/Q((2*n+2)*(2*n+3))
 assert 0<=ratio<Q(1,10)
 return s+first/(1-ratio)
def mm(a,b):
 t=list(zip(*b))
 return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in t] for row in a]
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))
def invert(a):
 n=len(a);m=[list(v)+[Q(int(i==j)) for j in range(n)] for i,v in enumerate(a)]
 for j in range(n):
  k=next(i for i in range(j,n) if m[i][j]);m[k],m[j]=m[j],m[k]
  p=m[j][j];m[j]=[x/p for x in m[j]]
  for i in range(n):
   if i!=j:
    z=m[i][j];m[i]=[x-z*y for x,y in zip(m[i],m[j])]
 return [r[n:] for r in m]
def positive(a):
 n=len(a);L=[[Q(0)]*n for _ in range(n)];p=[Q(0)]*n
 for i in range(n):
  for j in range(i):
   L[i][j]=(a[i][j]-sum((L[i][k]*p[k]*L[j][k] for k in range(j)),Q(0)))/p[j]
  p[i]=a[i][i]-sum((L[i][k]**2*p[k] for k in range(i)),Q(0))
  if p[i]<=0:return False
  L[i][i]=Q(1)
 return True
def exact_controls():
 ntest=0;saw_high=False
 T=[[Q(1),Q(10**30),Q(0)],[Q(0),Q(1),Q(10**42)],[Q(0),Q(0),Q(1)]]
 TT=list(map(list,zip(*T)))
 for m in (6,7,8,9):
  x=[Q(i+1,m+5) for i in range(m)]
  f=[[v,v**3,v**5] for v in x]
  def g(ids):
   return [[2*sum((f[t][i]*f[t][j] for t in ids),Q(0)) for j in range(3)] for i in range(3)]
  G=g(range(m));Gi=invert(G);TG=mm(mm(TT,G),T);TGi=invert(TG)
  assert positive(G)
  for rem in (1,2,3,4):
   if m-rem<3:continue
   D=list(range(m-rem,m));C=g(D)
   tau=sum(mm(Gi,C)[i][i] for i in range(3))
   TC=mm(mm(TT,C),T)
   assert tau==sum(mm(TGi,TC)[i][i] for i in range(3))
   saw_high|=tau>1
   gap=Q(1,10**80)
   Gk=g(range(m-rem))
   K=[[Gk[i][j]-gap*G[i][j] for j in range(3)] for i in range(3)]
   assert positive(K) and positive(mm(mm(TT,K),T))
   for i in D:
    for j in D:
     xx=dot(f[i],[dot(z,f[j]) for z in Gi])
     z=[dot(col,f[i]) for col in TT]
     y=[dot(col,f[j]) for col in TT]
     assert xx==dot(z,[dot(row,y) for row in TGi])
   ntest+=1
 assert ntest>=15 and saw_high
 return ntest
def main():
 p=argparse.ArgumentParser()
 for k in ("nf505","nf518","output"):p.add_argument("--"+k,required=True)
 a=p.parse_args()
 old,sh=read(a.nf505);fit,fh=read(a.nf518)
 assert (sh,fh)==(N505,N518)
 assert old["pass"]=="NF504-native" and old["original_selected_J_dimension"]==242
 assert old["source_original_NF407_sha256"]==SRC and old["source_original_NF406_sha256"]==SEAM
 assert old["original_original_D_frame_SHA256"]==FRAME
 assert fit["pass"]=="NF518-source-certified-242D-historical-D-exterior-coefficient-vector"
 assert fit["original_nf505_native_SHA256"]==sh
 assert fit["original_exact_historical_D_frame_SHA256"]==FRAME
 nodes=old["original_source_basis_nodes"]
 assert len(nodes)==242 and nodes[-1]==["pole",None]
 assert sinh_upper(B/2)<Q(3,5)
 rawtrace=2*B*sum((B**(2*k) for f,k in nodes if f!="pole"),Q(0))+2*B*Q(3,5)**2
 assert rawtrace<Q(830)
 den=int(fit["original_selected_D_frame_coefficients_exact_rational_denominator"])
 v=list(map(int,fit["original_selected_D_frame_coefficients_exact_rational_candidates_numerators"]))
 assert len(v)==242 and den==10**105
 norm1=Q(sum(map(abs,v)),den)
 assert norm1<Q(5,10**8)
 assert 830*242<450**2 and 2*B<Q(3,2)**2
 sourcefit=Q(5,10**83);oldres=Q(13,10**12)
 frameL2=Q(450)*Q(5,10**8)*Q(1,10**14)+sourcefit
 assert frameL2<Q(226,10**21)
 frameE=2*oldres*frameL2+frameL2**2
 assert frameE<Q(6,10**30)
 betaL2=Q(3,2)*Q(1,10**19)+sourcefit
 assert betaL2<Q(151,10**21)
 betaE=2*oldres*betaL2+betaL2**2
 assert betaE<Q(4,10**30)
 oldR=Q(old["original_original_saturated_exterior_residual_outward"][0])
 gamma=Q(old["original_original_gamma_squared"])
 gates=[]
 for name,q,g,target in [
   ("H4094",Q(99,10**29),Q(2,5),Q(1,10**27)),
   ("H4095",Q(99,10**29),Q(1,1000),Q(1,10**27)),
   ("H4094_union_H4095",Q(29,10**28),Q(1,20000),Q(3,10**27))]:
  assert q+frameE<target and q+betaE<target
  assert oldR-target/g>gamma
  gates.append(dict(D=name,CONDITIONAL_trial_e_upper=str(q),
                    CONDITIONAL_kernel_gap_lower=str(g),
                    original_true_e_upper_with_D_frame_tolerance=str(q+frameE),
                    original_true_e_upper_with_weighted_raw_beta_tolerance=str(q+betaE),
                    actual_local_e_and_gap_source_certified=False))
 tests=exact_controls()
 result=dict(pass_="NF519-exact-original-selected-frame-perturbation-and-gap-basis-invariance",
  original_nf505_source_sha256=sh,original_nf518_source_sha256=fh,
  original_nf407_sha256=SRC,original_nf406_sha256=SEAM,
  historical_original_D_frame_sha256=FRAME,
  original_selected_dimension=242,
  raw_J242_original_physical_Gram_trace_upper="830",
  actual_original_a_trial_L1_bound_lt_5e_minus_8=True,
  frame_ENTRYWISE_error_CONDITIONAL_upper="1e-14",
  any_original_subcell_squared_e_error_CONDITIONAL_with_frame_lt_6e_minus_30=True,
  raw_beta_WEIGHTED_L1_error_CONDITIONAL_upper="1e-19",
  any_original_subcell_squared_e_error_CONDITIONAL_with_beta_lt_4e_minus_30=True,
  kernel_gap_iff_Gkeep_minus_gap_G_positive_in_ANY_invertible_selected_frame=True,
  source_exact_basis_invariance_controls=tests,
  trace_leverage_greater_than_one_in_exact_controls=True,
  original_source_conditional_named_NF404_gates=gates,
  actual_historical_D_matrix_recovered=False,
  actual_original_242D_physical_beta_certified=False,
  actual_original_242D_cell_eD_certified=False,
  actual_original_Fredholm_kernel_gap_certified=False,
  original_NF404_named_physical_verdict="OPEN",
  Weil_multiplier_image_graph_domain="OPEN",W_ODD_NEG="OPEN",RH="OPEN")
 result["pass"]=result.pop("pass_")
 Path(a.output).write_text(json.dumps(result,indent=2)+"\n")
 print("NF519 source original J242 exact Fraction frame/gap gate PASS",tests,"independent algebra controls")
 print("Conditional D frame 1e-14 error => every cell e error <6e-30")
 print("Conditional weighted raw beta 1e-19 => every cell e error <4e-30")
 print("Actual raw beta, local e_D and gap not certified; NF404/Weil/RH OPEN")
if __name__=="__main__":main()
