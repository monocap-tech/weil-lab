#!/usr/bin/env python3
"""NF515: exact original NF401/NF494/NF505 source-to-selected-v23 bridge.

Original W=m(D)u4-alpha*sinh(x/2); fixed authentic NF514 23D v.
Compute <W,v>_O by full NF401 raw moments, pole shear and full NF494
H400/U400 two-collar mixed moment. Full 242D fitted local e_H is OPEN.
"""
from fractions import Fraction as F
import argparse,hashlib,json,math,sys
from pathlib import Path
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
H494="39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181"
N505="ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec"
M401="644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515"
SEED="39a8679197447975f54629a04c9608659e47aadf61dffb6e5dea11d0df2dc6b0"
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
B=F(11,10);BO=F(549,500);D=B-BO;S=10**160
def read(p):
 b=Path(p).read_bytes();return json.loads(b),hashlib.sha256(b).hexdigest()
def down(x,scale=10**110):return F(x.numerator*scale//x.denominator,scale)
def up(x,scale=10**110):return F(-((-x.numerator*scale)//x.denominator),scale)
def atan(q,n=140):
 a=sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
 r=q**(2*n+1)/F(2*n+1)
 return (a,a+r) if n%2==0 else (a-r,a)
def logarithm(z,n=135):
 y=z;k=0
 while y>=2:y/=2;k+=1
 while y<1:y*=2;k-=1
 t=(y-1)/(y+1)
 assert 0<=t<=F(1,3)
 def logunit(q):
  a=2*sum((q**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
  return a,a+2*q**(2*n+1)/((2*n+1)*(1-q*q))
 l,u=logunit(t);a,b=logunit(F(1,3))
 return (l+k*a,u+k*b) if k>=0 else (l+k*b,u+k*a)
def sqrtbound(n):
 k=math.isqrt(n*10**200)
 return F(k,10**100),F(k+1,10**100)
def witnesspoly(seed,old):
 nodes=[(F(f),k) for f,k in seed["original_source_basis_nodes"]]
 assert old["original_source_basis_nodes"][:23]==[[str(f),k] for f,k in nodes]
 assert nodes==[(F(37,64),k) for k in range(14)]+[(F(211,128),k) for k in range(9)]
 coef=list(map(int,seed["integer_coefficients"]));den=int(seed["coefficient_denominator"])
 assert len(coef)==23 and max(map(abs,coef))==den and sum(map(abs,coef))<5*den
 a,b=atan(F(1,5)),atan(F(1,239))
 pl,ph=16*a[0]-4*b[1],16*a[1]-4*b[0]
 assert 3<pl<ph<F(22,7)
 trig={}
 for f in set(f for f,k in nodes):
  wl,wh=2*f*pl,2*f*ph
  w=wl*S//1
  assert F(w,S)<=wl and wh<F(w+6,S)
  trig[f]=[S]+[w**j//(S**(j-1)*math.factorial(j)) for j in range(1,161)]
 q=[0]*175
 for c,(f,k) in zip(coef,nodes):
  for j,z in enumerate(trig[f]):
   if j%2==k%2:continue
   sign=-1 if ((j-1)//2 if k%2==0 else j//2)%2 else 1
   q[k+j]+=sign*(c*z//den)
 assert all(q[i]==0 for i in range(0,175,2))
 assert max(f for f,k in nodes)*2*F(22,7)*B<12
 assert 5*B**13*F(12)**161/math.factorial(161)<F(1,10**109)
 assert 23*161*B**174/S<F(1,10**145)
 assert 5*B**13*6*B/S<F(1,10**150)
 return q
def originalNF401(pre,second,seed,path):
 assert pre["pass"]=="NF515-original-NF401-global-pre-shear-v-source-exact"
 assert second["pass"]=="NF515-independent-source-NF401-raw23-aggregate"
 assert pre["original_nf401_sha"]==second["source_NF401_raw_sha256"]==M401
 a=F(int(pre["moment_pre_shear_lower_numerator"]),int(pre["scale"]))
 b=F(int(pre["moment_pre_shear_upper_numerator"]),int(pre["scale"]))
 x=F(int(second["moment_lower_numerator"]),int(second["fixed_dec_scale"]))
 y=F(int(second["moment_upper_numerator"]),int(second["fixed_dec_scale"]))
 assert 0<a<=b and max(a,x)<=min(b,y)
 if path:
  source,sha=read(path)
  assert sha==M401 and source["original_dimension"]==242
  rows=source["original_selected_raw_J_basis_moment_column_outward"]
  cc=list(map(int,seed["integer_coefficients"]));den=int(seed["coefficient_denominator"])
  lo=hi=F(0)
  for c,(l,u) in zip(cc,rows[:23]):
   l,u=F(l),F(u)
   if c>=0:lo+=F(c,den)*l;hi+=F(c,den)*u
   else:lo+=F(c,den)*u;hi+=F(c,den)*l
  assert max(a,lo)<=min(b,hi)
 return a,b
def physical_pole(q):
 # Genuine source-selected sinh(x/2) over full physical I, odd×odd.
 total=F(0)
 for j,c in enumerate(q):
  if not c:continue
  for k in range(150):
   n=2*k+1
   total+=2*F(c,S)*B**(j+n+1)/((j+n+1)*2**n*math.factorial(n))
 first=(B/2)**301/math.factorial(301)
 ratio=(B/2)**2/F(302*303)
 tail=first/(1-ratio)
 env=sum((F(abs(c),S)*B**j for j,c in enumerate(q) if c),F(0))
 assert tail<F(1,10**300) and env<10**20
 # Uniform genuine v-q error <=1e-100 on original full I.
 error=2*B*(F(1,10**100)+env*tail+tail/F(10**100))
 assert error<F(1,10**95)
 return total-error,total+error
def coeff(h,key):
 out=[]
 for l,u in h[key]:
  a,b=F(l),F(u)
  assert a<=b
  out.append((down(a,S),up(b,S)))
 assert len(out)==400
 return out
def original_collar(q,h,old):
 # q(B-d), exact rational binomial shift to true collar d∈[0,1/500].
 vd=[F(0)]*len(q)
 for i,c in enumerate(q):
  if c:
   for k in range(i+1):vd[k]+=F(c,S)*(-1)**k*math.comb(i,k)*B**(i-k)
 H=coeff(h,"original_H_400_native_outward")
 U=coeff(h,"original_U_400_native_outward")
 C0=C1=F(0)
 for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)):
  a,b=logarithm(F(p));s,t=sqrtbound(n)
  C0+=a/t;C1+=b/s
 assert 3<C0<=C1<5 and U[0][1]<0
 ll,lh=logarithm(B/D)
 def product(A,log=False):
  lo=hi=F(0)
  for i,v in enumerate(vd[:90]):
   if not v:continue
   for j,(a,b) in enumerate(A[:130]):
    if v<0:a,b=v*b,v*a
    else:a,b=v*a,v*b
    k=i+j;f=D**(k+1)/F(k+1)
    if log:
     p=f*(ll+F(1,k+1));q=f*(lh+F(1,k+1))
     lo+=a*(q if a<0 else p)
     hi+=b*(p if b<0 else q)
    else:lo+=a*f;hi+=b*f
  return lo,hi
 H0=product(H);U0=product(U,True)
 integral=sum((x*D**(j+1)/(j+1) for j,x in enumerate(vd)),F(0))
 A,B1=U[0][0]*C1,U[0][1]*C0
 Cterm=(min(A*integral,B1*integral),max(A*integral,B1*integral))
 Vtail=sum((abs(x)*D**j for j,x in enumerate(vd) if j>=90),F(0))
 Vsup=sum((abs(x)*D**j for j,x in enumerate(vd)),F(0))
 ht=sum((max(abs(a),abs(b))*D**j for j,(a,b) in enumerate(H) if j>=130),F(0))
 ut=sum((max(abs(a),abs(b))*D**j for j,(a,b) in enumerate(U) if j>=130),F(0))
 hs=sum((max(abs(a),abs(b))*D**j for j,(a,b) in enumerate(H)),F(0))
 us=sum((max(abs(a),abs(b))*D**j for j,(a,b) in enumerate(U)),F(0))
 l1=D*(lh+1)
 polyerror=2*(Vtail*(D*hs+us*l1/2)+Vsup*(D*ht+ut*l1/2))
 rho=D/F(1,25)
 CH=F(10)**420*rho**400/(1-rho)
 CU=F(10)**400*rho**400/(1-rho)
 assert CH<F(1,10**95) and CU<F(1,10**115)
 sourceerror=2*Vsup*(D*CH+CU*l1/2)
 # |∫_S(v-q)W| <=1e-100 sqrt(2D E_S) <1e-110,
 # using NF505's authentic complete two-collar physical W².
 ES=F(old["original_original_W_two_collar_energy_outward"][1])
 assert 0<ES<F(1,10**20) and 2*D*ES<F(1,10**20)
 qerror=F(1,10**110)
 fee=polyerror+sourceerror+qerror
 lo=2*H0[0]+U0[0]+2*Cterm[0]-fee
 hi=2*H0[1]+U0[1]+2*Cterm[1]+fee
 assert lo<=hi<0
 return (lo,hi),(polyerror,sourceerror,qerror)
def main():
 p=argparse.ArgumentParser()
 for k in ("nf494","nf505","seed","nf514","pre","independent_pre","output"):
  p.add_argument("--"+k,required=True)
 p.add_argument("--nf401")
 o=p.parse_args()
 h,sh=read(o.nf494);old,so=read(o.nf505);seed,ss=read(o.seed)
 prior,ps=read(o.nf514);pre,sp=read(o.pre);second,sp2=read(o.independent_pre)
 assert (sh,so,ss)==(H494,N505,SEED)
 assert old["pass"]=="NF504-native" and h["pass"]=="NF494-native"
 assert old["source_original_NF407_sha256"]==h["original_nf407_source_sha256"]==SRC
 assert old["source_original_NF406_sha256"]==h["original_nf406_seams_sha256"]==SEAM
 assert prior["witness_seed_SHA256"]==ss and prior["original_NF505_native_SHA256"]==so
 assert old["original_selected_J_dimension"]==242
 assert h["original_source_400_jet_order"]==400
 original=originalNF401(pre,second,seed,o.nf401)
 q=witnesspoly(seed,old)
 pole=physical_pole(q)
 alpha=F(6677356497477490213,4611686018427387904)
 whole=(original[0]-alpha*pole[1],original[1]-alpha*pole[0])
 collar,fees=original_collar(q,h,old)
 exterior=(whole[0]-collar[1],whole[1]-collar[0])
 assert whole[1]<0 and exterior[1]<0
 norm=tuple(map(F,prior["witness_full_original_O_L2_squared_outward"]))
 P=tuple(map(F,old["original_original_W_exterior_selected_projection_power_outward"]))
 assert 0<norm[0]<=norm[1] and 0<P[0]<=P[1]
 rank1=(exterior[1]**2/norm[1],exterior[0]**2/norm[0])
 ratio=(rank1[0]/P[1],rank1[1]/P[0])
 assert F(48,10000)<ratio[0]<=ratio[1]<F(1,200)
 assert F(2,5)*rank1[0]>F(14,10**25)
 def serial(x):return [str(down(x[0])),str(up(x[1]))]
 result={
  "pass":"NF515-authentic-original-source-selected-v23-exterior-moment-exact",
  "standing":"Source-original NF401/NF404/NF494/NF505 exact selected witness global exterior coupling; no full 242D fitted local eH, Weil source image or RH claim",
  "NF401_original_source_SHA256":M401,"NF494_original_source_SHA256":sh,
  "NF505_original_source_SHA256":so,"NF514_selected_witness_SHA256":ss,
  "NF514_original_witness_certificate_SHA256":ps,
  "source_nf407_sha256":SRC,"source_nf406_sha256":SEAM,
  "original_NF401_pre_shear_210decimal_receipt_SHA256":sp,
  "original_NF401_independent_180decimal_receipt_SHA256":sp2,
  "original_global_I_pre_shear_selected_witness_moment":serial(original),
  "original_global_I_sinh_pole_selected_witness_moment":serial(pole),
  "original_global_I_centered_W_selected_witness_moment":serial(whole),
  "original_terminal_two_collar_W_selected_witness_moment":serial(collar),
  "original_exterior_O_centered_W_selected_witness_moment":serial(exterior),
  "original_witness_norm_squared_on_O":serial(norm),
  "original_exterior_complete_J242_projection_power":serial(P),
  "original_rank_one_v23_projection_power_on_O":serial(rank1),
  "original_rank_one_fraction_of_complete_selected_projection_power":serial(ratio),
  "source_exact_projection_fraction_strict_0p0048_to_0p005":True,
  "rank_one_global_fit_power_on_edge_H4094_union_H4095_lower":str(down(F(2,5)*rank1[0])),
  "collar_error_terms":[str(x) for x in fees],
  "original_NF401_full_rows_source_recomputed":bool(o.nf401),
  "original_complete_J242_globally_fitted_local_eH":"OPEN",
  "original_named_NF404_physical_gate":"OPEN",
  "Weil_source_image_graph_domain":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN"}
 Path(o.output).write_text(json.dumps(result,indent=2)+"\n")
 print("NF515 SOURCE-EXACT original complete physical selected witness moment PASS")
 print("Original <W,v23>_O",float(exterior[0]),float(exterior[1]))
 print("Original rank-one v23 fraction of full J242 selected projection",float(ratio[0]),float(ratio[1]))
 print("Full J242 local eH/Weil source image/RH remain OPEN")
if __name__=="__main__":main()
