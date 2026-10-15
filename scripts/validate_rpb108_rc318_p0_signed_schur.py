"""RC318 — rigorous original signed P0 scalar Schur positivity, rank317 cut.

The signed source on u0 is explicitly known in physical L2. Project
the exact seven-prime step function onto all even Legendre degrees
0..510, and bound its *entire* remaining tail by Parseval:
    tail = ||K_prime u0||_2^2 - sum_{even n<512} |<un,K_prime u0>|^2.
The full source norm is computed from exact overlap lengths of the
fourteen truncated intervals, with rational log/coefficient bounds.
Projection uncertainties are paid with Markov's derivative inequality.

For n>=244 the endpoint cross coefficient is known exactly,
J and scalar vanish, RC46's degree-192 regular polynomial is
orthogonal, and RC46's kernel remainder plus the signed even pole
are bounded in full L2. The D-weighted high response T(v0) is
split into explicit n=244..510 and a rigorously bounded infinite tail.
RC314's *even* high floor converts the resulting residual upper
(T, i.e. the choice Y=0) to a POSITIVE Schur diagonal lower bound.

This proves ONLY S(P0,P0)>0, not positivity of the complete rank317
Schur matrix, the odd sector, Stage I, F4, Lean or RH.
"""
from __future__ import annotations
import argparse,hashlib,json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
CUT=512
FIRST=244
GRID=10**35
OUT=10**25
BUDGET=10**30
PRIMES=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
PINS={
 "certificates/rpb108_rc46_native_archimedean_head.json":"be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc313_prime_pole_distributions.json":"954b4892cf3b4e999e65476d7ce341021528d9e8",
 "certificates/rpb108_rc314_fredholm_schur.json":"6496be8d20176f173c0ff8b6e393b0ccd7c6ff5b",
 "certificates/rpb108_rc315_low_mode_sign.json":"a8cd974c8218e18943dda0082f48cca36a3350a8",
 "certificates/rpb108_rc316_first_high_cross.json":"89f3ad09f2a63c0033c631c788dbe78c67e92e68",
 "certificates/rpb108_rc317_one_mode_response.json":"b4556ed3e65b08fcfb7db5aac0f767383f514bf6",
}

def lo(x,g=OUT):
 return F(x.numerator*g//x.denominator,g)
def hi(x,g=OUT):
 return F((x.numerator*g+x.denominator-1)//x.denominator,g)
def sqrt_up(x,g=10**25):
 assert x>=0
 a=isqrt(x.numerator*g*g//x.denominator)
 assert F(a,g)**2<=x<F(a+1,g)**2
 return F(a+1,g)
def blob(raw):
 return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def log_bounds(n,K=240):
 assert 1<n<=9
 t=F(n-1,n+1)
 s=sum((2*t**(2*k+1)/F(2*k+1) for k in range(K)),F(0))
 rem=2*t**(2*K+1)/(F(2*K+1)*(1-t*t))
 a,b=lo(s,GRID),hi(s+rem,GRID)
 assert 0<a<=s<=s+rem<=b<R
 assert b-a<F(1,10**30)
 return a,b

def source_info():
 rows=[]
 for n,p in PRIMES:
  el,eu=log_bounds(n)
  pl,pu=log_bounds(p)
  v=isqrt(n*GRID*GRID)
  sl,su=F(v,GRID),F(v+1,GRID)
  assert sl*sl<=n<=su*su
  cl,ch=pl/su,pu/sl
  assert 0<cl<=ch
  ell=(el+eu)/2;c=(cl+ch)/2
  z=1-ell/B
  assert -1<z<1
  rows.append(dict(n=n,p=p,el=el,eu=eu,cl=cl,ch=ch,
      c=c,z=z,zradius=(eu-el)/(2*B),cradius=(ch-cl)/2))
 return rows

def prime_norm_upper(rows):
 # Physical u0=1/sqrt(2B) and the 14 physical step intervals:
 # two same-direction overlap lengths: 2*(R-max(ell_i,ell_j));
 # two opposite-direction overlaps: 2*max(0,R-ell_i-ell_j).
 # Divide by 2B. Monotone outward bound uses c_upper, ell_lower.
 val=F(0)
 for a in rows:
  for b in rows:
   side=R-max(a["el"],b["el"])
   opposing=max(F(0),R-a["el"]-b["el"])
   assert side>0
   val+=a["ch"]*b["ch"]*(side+opposing)/B
 return hi(val,BUDGET)

def scaled_prime_and_faults(rows,reverse=False):
 # Exact Legendre recurrence at rational *centers* through P_511.
 # No interval recurrence: uncertainty paid independently by
 # |P_k|<=1 and |P_k'|<=k(k+1)/2 on [-1,1].
 # A_n := sqrt(2n+1)*<un,K_prime u0>.
 centers={n:F(0) for n in range(2,CUT,2)}
 faults={n:F(0) for n in range(2,CUT,2)}
 for row in (reversed(rows) if reverse else rows):
  z=row["z"]
  pm,p=F(1),z # P0,P1
  vals=[pm,p]
  for k in range(1,CUT):
   q=((2*k+1)*z*p-k*pm)/F(k+1)
   pm,p=p,q
   vals.append(q)
  assert len(vals)==CUT+1
  c=row["c"]
  for n in range(2,CUT,2):
   delta=vals[n+1]-vals[n-1]
   assert -2<=delta<=2,("Legendre extremal regression",row["n"],n)
   centers[n]-=c*delta
   derivative_bound=n*n+n+1
   faults[n]+=2*row["cradius"]+c*derivative_bound*row["zradius"]
 assert all(v>=0 for v in faults.values())
 # Zero-degree prime physical coefficient, exact for each source
 # center and rigorous one-sided interval with c and log monotonicity.
 a0min=sum((r["cl"]*(2-r["eu"]/B) for r in rows),F(0))
 a0max=sum((r["ch"]*(2-r["el"]/B) for r in rows),F(0))
 assert 0<a0min<=a0max
 return centers,faults,a0min,a0max

def harmonic_table():
 h=F(0)
 d={0:h}
 for k in range(1,CUT+1):
  h+=F(1,k)
  if k%2==0:d[k]=h
 return d

def run(reverse=False):
 data={}
 for path,pin in sorted(PINS.items(),reverse=reverse):
  raw=(ROOT/path).read_bytes()
  assert blob(raw)==pin,("pinned blob changed",path)
  data[path]=json.loads(raw)
 def src(s):return data["certificates/rpb108_rc"+s+".json"]
 assert src("313_prime_pole_distributions")["original_CC27_Weil_polynomial_form_matches_native_model_on_all_degrees"]
 assert src("314_fredholm_schur")["rank301_feshbach_positivity_equivalent_to_full_positivity"]
 assert src("315_low_mode_sign")["normalized_low_block_positive_2_by_2"]
 assert src("316_first_high_cross")["rank317_high_mode_first_even_cross_nonzero"]
 assert src("317_one_mode_response")["Y_is_nonzero_and_supported_only_at_high_degree_244"]
 arch=src("46_native_archimedean_head")
 assert len(arch["regular_kernel_coefficients"])==193
 epsilon=F(arch["regular_kernel_uniform_error_upper"])
 assert 0<epsilon<F(1,10**22)
 metric=src("129_four_vector_joint_moment")
 smin=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
 smax=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
 assert 3<smin<=smax<5
 full=src("314_fredholm_schur")
 found=[v for v in full["inherited_stronger_RC283_all_reference_choices"]
    if v["parity"]=="even" and v["reference_rank"]==122 and
        v["first_discarded_degree"]==FIRST]
 assert len(found)==1
 mu=F(found[0]["high_complement_D_floor_lower"])
 assert 0<mu
 # B00 physical Q(u0,u0)/s; RC315 interval imported.
 row0=next(v for v in src("315_low_mode_sign")["original_low_diagonals"] if v["n"]==0)
 B00lower=F(row0["physically_normalized_original_Weil_diagonal_interval"][0])/smax
 assert B00lower>F(1,100)
 rows=source_info()
 total_prime_upper=prime_norm_upper(rows)
 center,fault,a0min,a0max=scaled_prime_and_faults(rows,reverse)
 H=harmonic_table()
 # Independent low-prime regression against RC315 interval.
 oldp=map(F,row0["prime"])
 pleft,pright=oldp
 assert pleft<=-a0max<=-a0min<=pright

 projected_lower=lo(a0min*a0min,BUDGET)
 lowcols=1
 signed_cross_replays=[]
 finite_high_upper=F(0)
 for n in range(2,CUT,2):
  # The exact physical prime coefficient equals A_n/sqrt(2n+1).
  cent=center[n]
  rad=hi(fault[n])
  unsigned_lower=max(F(0),lo(abs(cent))-rad)
  projected_lower+=lo(unsigned_lower**2/F(2*n+1),BUDGET)
  lowcols+=1
  if n in (232,244):
   ep=F(2*n+1,n*(n+1))
   scaled_original=cent+ep
   prev=next(v for v in src("316_first_high_cross")["rigorous_high_crosses"]
             if v["first_omitted_even_degree"]==n)
   a,b=map(F,(prev["original_scaled_cross_lower"],
              prev["original_scaled_cross_upper"]))
   assert a<=scaled_original-rad<=scaled_original+rad<=b,(
    "independent RC316 signed cross replay",n)
   signed_cross_replays.append(n)
  if n>=FIRST:
   # Complete signed endpoint+prime finite coefficient; n≥244
   # is orthogonal to J, scalar, degree-192 regular polynomial.
   ep=F(2*n+1,n*(n+1))
   upper=hi(abs(cent+ep)+rad)
   energy=upper*upper/(F(2*n+1)*smin*(H[n]+smin))
   finite_high_upper+=hi(energy,BUDGET)
 assert lowcols==CUT//2
 assert signed_cross_replays==[232,244]
 # Full physical prime tail by Parseval. Source has only even
 # degrees; includes the exact *signed* 14-step interference.
 prime_tail_upper=total_prime_upper-projected_lower
 assert 0<prime_tail_upper<F(1,100)
 # Endpoint coefficients for n>=CUT satisfy exact telescoping:
 # sum_{n>=CUT} (2n+1)/(n^2(n+1)^2)=1/CUT^2.
 # Even degrees only => endpoint tail L2 norm <= 1/CUT.
 high_tail_physical=sqrt_up(prime_tail_upper)+F(1,CUT)
 tail_D_lower=smin*(H[CUT]+smin)
 assert tail_D_lower>1
 infinite_high_upper=hi(high_tail_physical**2/tail_D_lower,BUDGET)
 endpoint_prime_high_squared=finite_high_upper+infinite_high_upper
 # RC46 regular polynomial degree 192 integrates u0 into a
 # degree <=193 polynomial, orthogonal to all high n>=244.
 # Complete physical regular residual <=2B epsilon.
 # Even pole: RC316 Taylor/Legendre bound for n even >=244,
 # |<un,Kpole u0>| <=16B (B/2)^n. Geometric even-degree
 # L2 series <=32B (B/2)^244, since
 # (1-(B/2)^4)^(-1/2)<2.
 # D weighting <=1 for high modes since smin*(H244+smin)>1.
 regular_tail=2*B*epsilon
 pole_tail=32*B*(B/2)**FIRST
 assert regular_tail<F(1,10**20) and pole_tail<F(1,10**40)
 entire_norm_up=sqrt_up(endpoint_prime_high_squared)+regular_tail+pole_tail
 full_T_squared_upper=hi(entire_norm_up**2,BUDGET)
 # RC314 Schur identity with Y=0:
 # S00=B00 - <Tv0,C^-1Tv0>
 #    >= B00_lower - ||T v0||²/mu_even.
 # No other low coordinates removed; a positive scalar Schur
 # diagonal does not establish entire Schur positive definiteness.
 Schur00lower=B00lower-full_T_squared_upper/mu
 assert Schur00lower>0,("crucial strict signed Schur P0 bound")
 old=src("317_one_mode_response")
 old_resid=F(old["full_D_residual_norm_upper"])
 assert entire_norm_up<old_resid/F(100)
 return dict(
   milestone="RC318",
   parent_merge="69de93f053014810f5a8554e202130f9a0025bcb",
   input_git_blob_pins=PINS,
   original_CC27_signed_Weil_operator=True,
   rank317_even_high_degree_start=FIRST,
   exact_prime_terms=14,
   evaluated_even_prime_coefficients_below_cutoff=lowcols,
   Legendre_output_cutoff_first_omitted_even_degree=CUT,
   RC316_232_244_signed_cross_independently_replayed=signed_cross_replays,
   original_physical_prime_full_mass_upper=str(total_prime_upper),
   original_physical_prime_low_projection_energy_lower=str(projected_lower),
   original_physical_prime_high_tail_mass_upper=str(prime_tail_upper),
   complete_original_endpoint_high_tail_L2_upper=str(F(1,CUT)),
   original_archimedean_regular_physical_high_tail_L2_upper=str(hi(regular_tail)),
   original_signed_even_pole_physical_high_tail_L2_upper=str(hi(pole_tail)),
   explicit_D_high_output_244_through_510_energy_upper=str(finite_high_upper),
   all_D_high_output_512_to_infinity_energy_upper=str(infinite_high_upper),
   complete_even_D_high_source_Tv0_norm_upper=str(hi(entire_norm_up)),
   complete_even_D_high_source_Tv0_norm_squared_upper=str(full_T_squared_upper),
   positive_even_high_coercivity_mu_lower=str(mu),
   original_P0_D_normalized_diagonal_B00_lower=str(B00lower),
   original_P0_full_even_high_eliminated_Schur_diagonal_strictly_positive=True,
   certified_original_P0_Schur_diagonal_lower=str(lo(Schur00lower)),
   Schur_corrector_choice="Y=0; rigorously paid direct native signed response T, no unproved inverse",
   RC317_nonzero_trial_preserved_as_separate_upper_Schur_bound=True,
   prime_source_tail_paid_by_exact_step_overlap_and_256_mode_Parseval=True,
   all_infinite_original_source_tails_paid=True,
   full_rank317_principal_Schur_positive=False,
   signed_inverse_response_for_all_columns=False,
   Stage_I_closed=False,F4=False,RH=False,Lean=False,
   next_cursor="RC319: extend the native signed Parseval/weighted-source scalar Schur certificate to P2 and selected mixed even inputs, paying cross-covariance. One positive diagonal does NOT prove the full 122x122 even Schur block; odd 195x195 remains open."
 )
if __name__=="__main__":
 p=argparse.ArgumentParser()
 p.add_argument("--output",type=Path,required=True)
 p.add_argument("--replay",action="store_true")
 a=p.parse_args()
 v=run(reverse=a.replay)
 if a.replay:assert v==json.loads(a.output.read_text(encoding="utf-8"))
 else:a.output.write_text(json.dumps(v,sort_keys=True,indent=2)+"\n",encoding="utf-8")
 print("RC318 CERTIFIED: strictly positive ORIGINAL signed P0 high-eliminated rank317 even Schur scalar. Full Schur/Stage I OPEN",flush=True)
