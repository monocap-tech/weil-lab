"""RC319 — original signed P2 prime source, complete tail, and P0/P2 low Gram.

The original CC27 Weil source is identified on the D carrier by RC313.
This independent P2 native prime action evaluates all 256 even
projections and the FULL L2 source norm of fourteen signed
piecewise-quadratic translated profiles. The n>=512 tail is
certified by Parseval with an explicit L2 transport error for log
and coefficient enclosures (including their moved support edges).

For P0,P2 low inputs also certify the actual physical original
2x2 Weil principal matrix with signed prime/regular/pole cross,
and rigorously enclose its determinant and second pivot. Then
derive a fully paid D-high source T v2 upper and a conservative
Schur diagonal lower estimate. The latter is not assumed positive.
No full even Schur block or RH result is asserted.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
from math import isqrt, factorial
import validate_rpb108_rc318_p0_signed_schur as rc318

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
CUT=512
FIRST=244
OUT=10**27
BUD=10**30
Z=B/2
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":"be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc314_fredholm_schur.json":"6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc315_low_mode_sign.json":"a8cd974c8218e18943dda0082f48cca36a3350a8",
 "certificates/rpb108_rc318_p0_signed_schur.json":None,
}
def lo(x,g=OUT):return F(x.numerator*g//x.denominator,g)
def hi(x,g=OUT):return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def root_hi(x,g=10**30):
 assert x>=0
 k=isqrt(x.numerator*g*g//x.denominator)
 assert F(k,g)**2<=x<F(k+1,g)**2
 return F(k+1,g)
def blob(raw):return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def poly_mul(x,y):
 out=[F(0)]*(len(x)+len(y)-1)
 for i,a in enumerate(x):
  for j,b in enumerate(y):out[i+j]+=a*b
 return out
def integ(p,l,h):
 return sum((c*(h**(k+1)-l**(k+1))/F(k+1)
             for k,c in enumerate(p)),F(0))
def p2(t):return (3*t*t-1)/2

def step_segments(rows,reverse=False):
 # Center signed original Kprime P_j, j=0,2, in t=x/B.
 # All interval boundaries are strictly in (-1,1).
 terms=[]
 for row in (reversed(rows) if reverse else rows):
  d=(row["el"]+row["eu"])/(2*B)
  c=row["c"]
  assert 0<d<2
  for direction in (-1,1):
   left=max(F(-1),-1-direction*d)
   right=min(F(1),1-direction*d)
   assert left<right
   p0=[-c]
   p2poly=[-c*(3*d*d-1)/2,-3*c*direction*d,-3*c/2]
   terms.append((left,right,p0,p2poly))
 stops=sorted({F(-1),F(1)}|{w for t in terms for w in t[:2]})
 pieces=[]
 for l,h in zip(stops,stops[1:]):
  mid=(l+h)/2
  active=[row for row in terms if row[0]<mid<row[1]]
  a=sum((row[2][0] for row in active),F(0))
  co=[sum((row[3][k] for row in active),F(0)) for k in range(3)]
  pieces.append((l,h,[a],co))
 assert len(terms)==14 and len(pieces)==15
 # Piecewise reflected g_j are even. Tested by coefficients
 # and exact rational swapped boundaries, not visual sampling.
 for l,h,p0,p2c in pieces:
  partner=next((q for a,b,q0,q in pieces if a==-h and b==-l),None)
  assert partner is not None
  assert p2c==[partner[k]*(-1)**k for k in range(3)]
 return pieces

def masscenter(pieces,which):
 # Physical norm of Kprime uj is (2j+1)/2 int g_j(t)^2dt.
 factor=F(1,2) if which==0 else F(5,2)
 return factor*sum((integ(poly_mul(z[2 if which==0 else 3],
                  z[2 if which==0 else 3]),z[0],z[1]) for z in pieces),F(0))

def signed_j2_coefficients(rows,reverse=False):
 # A_n^(2)=sqrt((2n+1)/5)*<un,Kprime u2>.
 # For each positive displacement d, parity yields
 # A_n^(2)=-(2n+1)*sum(c*int_-1^(1-d) Pn(t) P2(t+d)dt).
 # Use only rational Legendre edge values; independent
 # analytic Markov/L2 transport controls uncertain shifts.
 ans={n:F(0) for n in range(0,CUT,2)}
 for row in (reversed(rows) if reverse else rows):
  d=(row["el"]+row["eu"])/(2*B)
  z=1-d;c=row["c"]
  pv=[F(1),z]
  for k in range(1,CUT+2):
   pv.append(((2*k+1)*z*pv[-1]-k*pv[-2])/F(k+1))
  assert len(pv)==CUT+3
  def J(k):
   assert k>=0
   if k==0:return z+1
   return (pv[k+1]-pv[k-1])/F(2*k+1)
  for n in range(0,CUT,2):
   if n==0:
    # P2(t+d)= (3t²+6dt+3d²-1)/2.
    v=(F(3,2)*(z**3+1)/3
      +3*d*(z*z-1)/2
      +(3*d*d-1)*(z+1)/2)
   elif n==2:
    # Direct product of two explicit quadratics.
    v=integ(poly_mul([F(-1,2),F(0),F(3,2)],
      [(3*d*d-1)/2,3*d,F(3,2)]),-1,z)
   else:
    a=F(n+1,2*n+1);b=F(n,2*n+1)
    ap=F(n+2,2*n+3);bp=F(n+1,2*n+3)
    am=F(n,2*n-1);bm=F(n-1,2*n-1)
    # t²Pn = a*ap Pn+2 +(a*bp+b*am)Pn+b*bm Pn-2
    v=(F(3,2)*(a*ap*J(n+2)+(a*bp+b*am)*J(n)+b*bm*J(n-2))
       +3*d*(a*J(n+1)+b*J(n-1))
       +(3*d*d-1)*J(n)/2)
   ans[n]-=F(2*n+1)*c*v
 # Independent physical symmetry can be checked at n=0.
 return ans

def translation_error(rows,which):
 # For zero-extended uj supported on [-B,B], L2 translation
 # modulus <= L_infty*sqrt(delta)+||u_j'||_2*delta.
 # Norm uj =1, ||u0||inf²=1/(2B), ||u2||inf²=5/(2B),
 # ||u0'||_2=0, ||u2'||_2=sqrt(15)/B <4/B.
 # Two translations each: full operator-source defect, with
 # coefficient errors included by contractivity of translations.
 fault=F(0)
 for row in rows:
  de=(row["eu"]-row["el"])/2
  dc=row["cradius"]
  assert de>=0 and dc>=0
  base=(F(1,2*B) if which==0 else F(5,2*B))*de
  eta=root_hi(base)
  if which==2:eta+=4*de/B
  fault+=2*(dc+row["ch"]*eta)
 return hi(fault)

def regular_moments(coeff,eps):
 # Exact C00(r)=2-r, C02(r)=-r(r-2)(r-1)/2,
 # C22(r)=2/5-r+r³/2-3r^5/40, r=|x-y|/B.
 # Entries: reg00=B int_0² C00(r) k(Br)dr
 # reg02/sqrt5=B int_0² C02(r) k(Br)dr
 # reg22=5B int_0² C22(r) k(Br)dr
 rows=[[(0,F(2)),(1,F(-1))],
   [(1,F(-1)),(2,F(3,2)),(3,F(-1,2))],
   [(0,F(2,5)),(1,F(-1)),(3,F(1,2)),(5,F(-3,40))]]
 ans=[]
 for idx,cs in enumerate(rows):
  val=F(0)
  for k,c in enumerate(coeff):
   integral=sum((v*2**(k+j+1)/F(k+j+1) for j,v in cs),F(0))
   val+=c*(B**(k+1))*integral
  val*=5 if idx==2 else 1
  ans.append(val)
 assert 0<ans[0]<1 and ans[1]<0 and 0<ans[2]<1
 # Uniform RC46 kernel error provides ||K-Kpoly||<=2Beps,
 # so every physically orthonormal entry has error <=2Beps;
 # scaled reg02/sqrt5 error <=2Beps/sqrt5 <=Beps.
 return ans,2*B*eps

def even_pole_moments():
 # M0=int_-1^1 cosh(Z t)dt; M2=int P2(t) cosh(Zt)dt.
 # Both positive series. Tail dominated by first omitted term
 # times geometric bound, all rational.
 N=40
 m0=F(0);m2=F(0)
 for k in range(N):
  term=Z**(2*k)/factorial(2*k)
  m0+=2*term/F(2*k+1)
  if k:m2+=term*F(4*k,(2*k+1)*(2*k+3))
 rem=2*Z**(2*N)/factorial(2*N)/(1-Z*Z/F((2*N+1)*(2*N+2)))
 assert 0<rem<F(1,10**80)
 return (m0,m0+rem),(m2,m2+rem)

def run(reverse=False):
 inp={}
 for p,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/p).read_bytes()
  if pin is not None:assert blob(raw)==pin,(p,"source blob mismatch")
  inp[p]=json.loads(raw)
 def get(k):return inp["certificates/rpb108_rc"+k+".json"]
 assert get("318_p0_signed_schur")["original_P0_full_even_high_eliminated_Schur_diagonal_strictly_positive"]
 assert get("313_prime_pole_distributions")["original_CC27_Weil_polynomial_form_matches_native_model_on_all_degrees"]
 rows=rc318.source_info()
 pieces=step_segments(rows,reverse)
 norm0=masscenter(pieces,0)
 norm2=masscenter(pieces,2)
 eps0=translation_error(rows,0)
 eps2=translation_error(rows,2)
 assert eps2<F(1,10**12)
 n0coeff,n0fault,a0min,a0max=rc318.scaled_prime_and_faults(rows,reverse)
 a0center=-sum((r["c"]*(2-(r["el"]+r["eu"])/(2*B)) for r in rows),F(0))
 assert -a0max<=a0center<=-a0min
 a2=signed_j2_coefficients(rows,reverse)
 # Physical prime symmetry: Qprime(u0,u2)=sqrt5*A0^(2)
 #                                =A2^(0)/sqrt5.
 # A2^(0) is the RC318 prime centered output. All rational.
 assert 5*a2[0]==n0coeff[2],("mixed original prime symmetry")
 # L2 step profile norms match direct physical prime source mass.
 assert 0<norm0<6 and 0<norm2<6
 # RC318 independent upper full source mass should enclose
 # center plus its paid translation perturbation.
 rc318_mass=F(get("318_p0_signed_schur")[
    "original_physical_prime_full_mass_upper"])
 assert norm0<=rc318_mass
 coeff_energy=sum((5*a*a/F(2*n+1) for n,a in a2.items()),F(0))
 assert 0<coeff_energy<=norm2,("Bessel exact nonnegative tail")
 physical_tailcenter=norm2-coeff_energy
 # Complete centered and actual P2-source tail (n>=512).
 tailphysicalupper=(root_hi(physical_tailcenter)+eps2)**2
 assert tailphysicalupper>0
 arch=get("46_native_archimedean_head")
 coeff=list(map(F,arch["regular_kernel_coefficients"]))
 epsarch=F(arch["regular_kernel_uniform_error_upper"])
 assert len(coeff)==193
 (r00,r02scaled,r22),regfault=regular_moments(coeff,epsarch)
 # Independent inherited RC315 reg00 must enclose native model
 # with full original analytic kernel error.
 prev0=next(z for z in get("315_low_mode_sign")["original_low_diagonals"] if z["n"]==0)
 assert F(prev0["regular"][0])<=r00<=F(prev0["regular"][1])
 (m0lo,m0hi),(m2lo,m2hi)=even_pole_moments()
 pole00_l=B*m0lo*m0lo;pole00_h=B*m0hi*m0hi
 pole22_l=5*B*m2lo*m2lo;pole22_h=5*B*m2hi*m2hi
 pole02s_l=B*m0lo*m2lo;pole02s_h=B*m0hi*m2hi
 assert F(prev0["pole"][0])<=pole00_l<=pole00_h<=F(prev0["pole"][1])
 # Original low 2x2 physical Gram:
 # Q22 = Q00 + (J22-J00)+(W22-W00)
 #       -(Kreg22-Kreg00)+(Kprime22-Kprime00)
 #       +(Kpole22-Kpole00).
 q00l,q00h=map(F,prev0["physically_normalized_original_Weil_diagonal_interval"])
 base=F(3,2)+F(11,30)
 q22l=(q00l+base-(r22+regfault)+(r00-regfault)
    +(a2[2]-eps2)-(a0center+eps0)+(pole22_l-pole00_h))
 q22h=(q00h+base-(r22-regfault)+(r00+regfault)
    +(a2[2]+eps2)-(a0center-eps0)+(pole22_h-pole00_l))
 assert q22l>F(19,100) and q22h<F(21,100)
 # Q02/sqrt5: W02/sqrt5=1/6, original signed prime
 # coefficient A0^(2), original regular scaled r02scaled,
 # positive even pole B M0 M2. J/scalar are diagonal.
 q02s_l=F(1,6)+a2[0]-eps2/2-(r02scaled+regfault/2)+pole02s_l
 q02s_h=F(1,6)+a2[0]+eps2/2-(r02scaled-regfault/2)+pole02s_h
 assert F(0)<q02s_l<=q02s_h<F(1,10)
 detl=q00l*q22l-5*q02s_h*q02s_h
 deth=q00h*q22h-5*q02s_l*q02s_l
 assert detl>0,("original P0/P2 physical 2x2 strict positivity fails")
 # Original second physical low pivot after P0:
 # Q22 - Q02^2/Q00 >0.
 pivotlower=q22l-5*q02s_h*q02s_h/q00l
 assert pivotlower>0
 # Full D-high source P2, even n>=244:
 # <un,Q u2>=sqrt(5/(2n+1))*(prime A_n^2 + endpoint E[n,2])
 # for n>193, with full RC46 remainder/pole paid.
 metric=get("129_four_vector_joint_moment")
 smin=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
 smax=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
 h=F(0);H={}
 for n in range(CUT+1):
  if n:h+=F(1,n)
  H[n]=h
 Dh2=smin+H[2];Dh244=smin+H[FIRST];Dh512=smin+H[CUT]
 assert Dh2>5 and Dh244>10
 fin=F(0)
 for n in range(FIRST,CUT,2):
  endpoint=F(2*n+1,(n-2)*(n+3))
  amp=abs(a2[n]+endpoint)
  fin+=F(5)*amp*amp/(F(2*n+1)*Dh2*(H[n]+smin))
 # Full actual prime error not propagated per coefficient: its
 # ENTIRE L2 correction is <=eps2, so pay it ONCE by
 # infinite-dimensional triangle/Minkowski, not 256x.
 finite_norm=root_hi(fin)
 eps_weighted=eps2/root_hi(Dh2*Dh244) if False else eps2 # conservative: all denominators >1
 # Endpoint P2 tail physical <=sqrt6/512, since
 # 5*[n(n+1)/((n-2)(n+3))]^2 < 6 for n>=512,
 # and sum_{n>=512} (2n+1)/(n²(n+1)²)=1/512².
 endpoint_tail=root_hi(F(6))/CUT
 infinite_norm=(root_hi(tailphysicalupper)+endpoint_tail)/root_hi(Dh2*Dh512) if False else (
   root_hi(tailphysicalupper)+endpoint_tail)/F(10)
 # Using sqrt(Dh2*Dh512)>10 is guaranteed here; preserve
 # outward bound by checking the exact rational inequality.
 assert Dh2*Dh512>100
 regular_norm=regfault/F(10)
 pole_norm=32*B*Z**FIRST/F(10)
 assert Dh2*Dh244>100
 Tv2_bound=finite_norm+eps_weighted+infinite_norm+regular_norm+pole_norm
 Tv2_sq_up=hi(Tv2_bound**2,BUD)
 ref=get("314_fredholm_schur")
 even=next(c for c in ref["inherited_stronger_RC283_all_reference_choices"]
       if c["parity"]=="even" and c["reference_rank"]==122)
 mu=F(even["high_complement_D_floor_lower"])
 B22lo=q22l/(smax+H[2])
 S22lower=B22lo-Tv2_sq_up/mu
 B00lo=q00l/smax
 # Full mixed D-high source Gram is bounded by Cauchy-Schwarz.
 oldT0=F(get("318_p0_signed_schur")[
   "complete_even_D_high_source_Tv0_norm_squared_upper"])
 full_mixed_high_gram_abs_upper=root_hi(oldT0*Tv2_sq_up)
 # IMPORTANT: even if S22lower>0 and S00lower>0, the complete
 # 2x2 Schur determinant still needs signed inverse covariance.
 lower00=F(get("318_p0_signed_schur")[
   "certified_original_P0_Schur_diagonal_lower"])
 assert lower00>0
 return dict(milestone="RC319",
  parent_merge="6b7a605542b765a6555810098fca86d6610a6d13",
  input_git_blob_pins=PINS,
  original_CC27_signed_source=True,
  piecewise_prime_translation_profiles=14,
  number_of_even_legendre_coefficients_p2=len(a2),
  original_P2_prime_physical_center_norm_squared=str(hi(norm2)),
  original_P2_prime_center_projection_below512_squared=str(lo(coeff_energy)),
  original_P2_prime_center_infinite_tail_squared=str(hi(physical_tailcenter)),
  original_P2_prime_complete_actual_tail_squared_upper=str(hi(tailphysicalupper)),
  prime_translation_full_L2_error_p2_upper=str(eps2),
  direct_P0_P2_prime_cross_reproduces_selfadjoint_symmetry=True,
  original_P0_P2_physical_low_diagonal_P2=[str(lo(q22l)),str(hi(q22h))],
  original_P0_P2_physical_offdiagonal_div_sqrt5=[str(lo(q02s_l)),str(hi(q02s_h))],
  original_P0_P2_physical_two_by_two_determinant_lower=str(lo(detl)),
  original_P0_P2_physical_second_pivot_lower=str(lo(pivotlower)),
  original_P0_P2_low_principal_block_strictly_positive=True,
  P2_D_normalized_complete_high_source_norm_upper=str(hi(Tv2_bound)),
  P2_D_normalized_complete_high_source_squared_upper=str(Tv2_sq_up),
  P2_D_normalized_native_B22_lower=str(lo(B22lo)),
  P2_D_normalized_conservative_Schur_diagonal_lower=str(lo(S22lower)),
  fully_paid_high_Tv0_Tv2_Gram_abs_upper=str(hi(full_mixed_high_gram_abs_upper)),
  P0_Schur_diagonal_positive_inherited_RC318=True,
  full_P0_P2_high_eliminated_Schur_2by2_positive=False,
  full_rank317_principal_Schur_positive=False,
  signed_inverse_response_for_all_columns=False,
  Stage_I_closed=False,F4=False,RH=False,Lean=False,
  next_cursor="RC320: use signed mixed-source covariance and a nonzero multi-high trial to improve the P0/P2 Schur 2x2 lower Loewner bound. Low principal 2x2 positivity alone cannot establish high-eliminated 2x2 positivity; odd 195 and remaining even 120 coordinates remain open."
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 v=run(reverse=a.replay)
 if a.replay:assert v==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(v,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC319: signed P2 source and full tail, positive original low P0/P2 matrix; high-eliminated 2x2 positivity OPEN",flush=True)
