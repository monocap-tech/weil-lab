#!/usr/bin/env python3
"""Independent all-rational NF514 selected-subspace leverage replay.

Different sine/cos Taylor degree, arithmetic scales, Machin terms and
direct monomial pair integral (rather than primary squared convolution).
No floating eigensolver, quadrature or RH statement enters acceptance.
"""
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
SHA="ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec"
S=10**170;T=10**270;N=180;B=F(549,500);h=B/4096
def load(path):
 b=Path(path).read_bytes()
 return json.loads(b),hashlib.sha256(b).hexdigest()
def atan(t,n=145):
 v=sum(((-1)**j*t**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
 r=t**(2*n+1)/F(2*n+1)
 return (v,v+r) if n%2==0 else (v-r,v)
def main():
 p=argparse.ArgumentParser()
 for k in ("native","seed","prior","output"):p.add_argument("--"+k,required=True)
 o=p.parse_args()
 native,ns=load(o.native);seed,ss=load(o.seed);old,os=load(o.prior)
 assert ns==SHA and old["original_NF505_native_SHA256"]==ns and old["witness_seed_SHA256"]==ss
 assert native["original_source_basis_nodes"][:23]==seed["original_source_basis_nodes"]
 assert native["original_selected_J_dimension"]==242
 cc=list(map(int,seed["integer_coefficients"]));C=int(seed["coefficient_denominator"])
 assert len(cc)==23 and max(map(abs,cc))==C and sum(map(abs,cc))<5*C
 aa,bb=atan(F(1,5)),atan(F(1,239))
 pl,ph=16*aa[0]-4*bb[1],16*aa[1]-4*bb[0]
 assert 3<pl<ph<F(22,7)
 nodes=[(F(x),int(k)) for x,k in seed["original_source_basis_nodes"]]
 coeff=[0]*200
 for (freq,k),c in zip(nodes,cc):
  left,right=2*freq*pl,2*freq*ph
  w=int(left*S)
  assert F(w,S)<=left and right<F(w+6,S)
  for j in range(N+1):
   if j%2==k%2:continue
   magnitude=S if j==0 else w**j//(S**(j-1)*math.factorial(j))
   sign=-1 if ((j-1)//2 if k%2==0 else j//2)%2 else 1
   coeff[j+k]+=sign*(c*magnitude//C)
 assert all(coeff[j]==0 for j in range(0,len(coeff),2))
 assert 5*F(11,10)**13*F(12)**181/math.factorial(181)<F(1,10**132)
 assert 23*181*F(11,10)**194/S<F(1,10**150)
 delta=F(1,10**120)
 env=sum((F(abs(z),S)*B**i for i,z in enumerate(coeff) if z),F(0))
 assert env<10**20
 err=2*B*(2*env*delta+delta*delta)
 active=[(i,c) for i,c in enumerate(coeff) if c]
 def integral(lo,hi):
  result=fee=0;factor={}
  for i,x in active:
   for j,y in active:
    n=i+j+1
    if n not in factor:
     z=2*(hi**n-lo**n)/n*T
     factor[n]=z.numerator//z.denominator
    result+=x*y*factor[n];fee+=abs(x*y)
  return F(result-fee,S*S*T)-err,F(result+fee,S*S*T)+err
 full=integral(F(0),B);assert full[0]>0
 cases=(("H4095",B-h,B,F(1,5)),
        ("H4094",B-2*h,B-h,F(1,6)),
        ("H4094_union_H4095",B-2*h,B,F(2,5)))
 out={}
 for key,left,right,q in cases:
  interval=integral(left,right)
  assert interval[0]>q*full[1]
  low,high=interval[0]/full[1],interval[1]/full[0]
  prior=old["original_selected_subspace_rayleigh_leverage_lower_by_named_cell"][key]
  assert low<=F(prior["upper"]) and F(prior["lower"])<=high
  out[key]={"lower":str(low),"upper":str(high),
            "strict_simple_floor":str(q)}
  print("NF514 independent exact integral",key,"tau>",q,"PASS",flush=True)
 result={"pass":"NF514-independent-23D-true-source-all-integer-leverage-audit",
 "prior_certificate_SHA256":os,
 "original_NF505_SHA256":ns,
 "source_selected_witness_SHA256":ss,
 "independent_sincos_Taylor_degree":N,
 "independent_fixed_poly_scale":str(S),
 "independent_fixed_monomial_moment_scale":str(T),
 "independent_Machin_terms":145,
 "independent_true_source_witness_rayleigh_intervals":out,
 "actual_full_J242_trace_leverage_bounded_below":True,
 "NF513_conditional_no_go_thresholds_are_impossible_for_actual_selected_space":True,
 "original_globally_fitted_eH":"OPEN","fixed_NF404_named_patch_verdict":"OPEN",
 "Weil_source_image_graph_domain":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
 Path(o.output).write_text(json.dumps(result,indent=2)+"\n")
if __name__=="__main__":main()
