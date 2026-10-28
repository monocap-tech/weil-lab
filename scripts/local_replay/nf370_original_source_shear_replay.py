#!/usr/bin/env python3
"""NF370: original PR369 exact dyadic source/selected 4x4 shear consistency.
No full infinite signed Schur upper and no native-Arb re-evaluation.
"""
import argparse,hashlib,zipfile,io,json,sys
from fractions import Fraction as F
sys.set_int_max_str_digits(100000)
ZIP_SHA="1bacc7ae7967d1282eb28fd9d8566204eb21ba93246f6e81b174a18cc2ab1e96"
JSON_SHA="1b22cd77dd555749b8dcc41f92ddd91d982f2eca23ebf3a7638e512147b39d18"
def dy(p):
 n,e=map(int,p)
 return F(n<<e) if e>=0 else F(n,1<<(-e))
def ball(v):
 c,r=dy(v[0]),dy(v[1]);assert r>=0
 return c-r,c+r
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(a,b):
 z=[x*y for x in a for y in b]
 return min(z),max(z)
def zero():return F(0),F(0)
def ma(A,B):return [[add(a,b) for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def ms(A,B):return [[sub(a,b) for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def tr(A):return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def mm(A,B):
 out=[]
 for i in range(len(A)):
  row=[]
  for j in range(len(B[0])):
   v=zero()
   for k in range(len(B)):v=add(v,mul(A[i][k],B[k][j]))
   row.append(v)
  out.append(row)
 return out
def contains0(A):return all(a<=0<=b for row in A for a,b in row)
def mat(x,key):
 M=x[key];assert len(M)==4 and all(len(row)==4 for row in M)
 return [[ball(M[i][j]) for j in range(4)] for i in range(4)]
def coeff(x,key):
 M=x[key];assert len(M)==4 and all(len(row)==4 for row in M)
 return [[(dy(M[i][j]),dy(M[i][j])) for j in range(4)] for i in range(4)]
def main():
 p=argparse.ArgumentParser();p.add_argument("--offline",required=True);p.add_argument("--report");a=p.parse_args()
 raw=open(a.offline,"rb").read();assert hashlib.sha256(raw).hexdigest()==ZIP_SHA
 with zipfile.ZipFile(io.BytesIO(raw)) as z:
  data=z.read("nf369_actual_critical_quotient.json")
 assert hashlib.sha256(data).hexdigest()==JSON_SHA
 x=json.loads(data)
 assert x["selected_rank"]==242 and x["existing_critical_witness_count"]==4
 assert x["nf369_actual_full_complement_upper_computed"] is False
 W=mat(x,"nf369_original_four_mode_signed_Gram_native")
 P=mat(x,"nf369_selected_critical_Gram_native")
 B=mat(x,"nf369_selected_to_original_quotient_signed_coupling_native")
 C=mat(x,"actual_exterior_signed_Gram_native")
 Y=coeff(x,"nf369_quotient_response_exact_dyadic_coefficients")
 I=[[(F(int(i==j)),F(int(i==j))) for j in range(4)] for i in range(4)]
 # The actual physical selected/quotient original signed form recomposition.
 assert contains0(ms(W,ma(ma(ma(P,B),tr(B)),C)))
 # f=p+q, the source exterior probe coupling is E*W f = B*+C.
 d=ma(tr(B),C)
 Ys=ma(Y,I)
 rb=ms(mm(C,Y),tr(B))
 rd=ms(mm(C,Ys),d)
 assert contains0(ms(rb,rd))
 # Two exactly matched Galerkin variational lower matrices.
 Db=ms(ma(mm(B,Y),mm(tr(Y),tr(B))),mm(mm(tr(Y),C),Y))
 Dd=ms(ma(mm(tr(d),Ys),mm(tr(Ys),d)),mm(mm(tr(Ys),C),Ys))
 assert contains0(ms(ms(P,Db),ms(W,Dd)))
 report=dict(
  standing="original NF369 SHA-pinned dyadic shear consistency only",
  original_archive_sha256=ZIP_SHA,original_json_sha256=JSON_SHA,
  selected_rank=242,critical_rank=4,
  matched_original_source_trial="I+projected_probe_candidate",
  full_original_source_4x4_recomposition_pass=True,
  matched_residual_shear_pass=True,
  finite_original_source_schur_shear_pass=True,
  full_infinite_exterior_upper=False,
  original_strong_forcing_computed=False,
  W_ODD_NEG="OPEN",RH="OPEN",domain_review="OPEN")
 if a.report:
  with open(a.report,"w") as fp:json.dump(report,fp,indent=2);fp.write("\n")
 print("PASS NF370 SHA-pinned original 4x4 selected/quotient signed recomposition")
 print("PASS NF370 original-source shifted exact dyadic Galerkin response Y_source=I+Y_projected")
 print("PASS NF370 exact interval matched residual and Schur invariance")
 print("No unprobed infinite exterior upper or RH promotion")
if __name__=="__main__":main()
