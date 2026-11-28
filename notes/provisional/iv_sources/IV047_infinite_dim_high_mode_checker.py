#!/usr/bin/env python3
"""IV047: exact-rational nonkernel audit of high-mode original Weil coercivity.

Verifies source NF599 finite Gamma gain >8 at |t|>=30000, the universal
original n=2,3,4,5,7,8,9 two-sided prime norm bound <71/10,
the true two-crossed-pole negative odd eigenvalue <12/25,
all geometry/Fourier low-band/Schur constants exactly.

The Fourier projection/Poincare and form-closure arguments are *mathematical*
proofs documented in the report, not claims of Lean kernel certification.
No repo modifications or CI work.
"""
from fractions import Fraction as Q
from math import isqrt, factorial
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'IV047_infinite_dim_high_mode_receipt.json'
PRED={
 'IV040_gamma_cutoff_optimization_checker.py':'4da2cdfce4bca0a98479969a01cb93010304bf4289e0329032c4f037198db33f',
 'IV044_pole_parity_schur_checker.py':'b2142d08a295819bd27e554e23c91e7ba774e5fcfa29920c23f1c990ec5a5b1f',
 'IV046_fixed_window_multicell_variational_checker.py':'d2ae448c0c28981fed1ebc8d271a1370070a24cf88649f50acf7af18759e59ac',
}
# Verify SHA when the named exact-source earlier artifacts exist; record all.
predecessor_sha={}
for name, expected in PRED.items():
    actual=sha256((ROOT/name).read_bytes()).hexdigest()
    predecessor_sha[name]=actual
    assert actual==expected, (name,actual,expected)

# Gamma lower: t=30,000, a_n=(4n+1)/4
# g_n(t)=16*t^2 / [(4n+1)*((4n+1)^2+4*t^2)].
T=30000
NF_TERMS=20000
SCALE=10**7
TOTAL_NUM=16*T*T
DENSQ=4*T*T
floor_terms=[]
for n in range(NF_TERMS):
    k=4*n+1
    denom=k*(k*k+DENSQ)
    z=(TOTAL_NUM*SCALE)//denom
    # z/10^7 <= exact source gain by floor definition.
    floor_terms.append(z)
FLOOR_TOTAL=sum(floor_terms)
assert FLOOR_TOTAL==136191112,FLOOR_TOTAL
GAIN_LO=Q(FLOOR_TOTAL,SCALE)
GAMMA_ZERO_LO=-Q(28,5)
GAMMA_T_LO=GAMMA_ZERO_LO+GAIN_LO
assert GAMMA_T_LO>8

# The source window 1.1 allows translations only n<=9.
def log_bracket(n,terms=96):
    y=Q(n-1,n+1)
    v=sum((2*y**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    tail=(2*y**(2*terms+1)/Q(2*terms+1))/(1-y*y)
    return v,v+tail

def upward(q,scale):
    p=q*scale
    return Q(-(-p.numerator//p.denominator),scale)

def lower_sqrt(n,scale=10**8):
    return Q(isqrt(n*scale*scale),scale)

assert log_bracket(2)[0]+log_bracket(5)[0]>Q(11,5) # log 10 > 2.2
active=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
PRIME_NORM_UP=Q(0)
primes=[]
for n,p in active:
    l,u=log_bracket(p)
    log_up=upward(u,10**10)
    sqrt_lo=lower_sqrt(n)
    assert 0<sqrt_lo and sqrt_lo*sqrt_lo<=n
    term=2*log_up/sqrt_lo
    PRIME_NORM_UP+=term
    primes.append({'n':n,'prime_base':p,'twosided_norm_upper_float':float(term)})
assert PRIME_NORM_UP<Q(71,10),float(PRIME_NORM_UP)

# Original two crossed moments: the negative eigenvector is
# k(x)=sqrt(2)*sinh(x/2)*1_I with k2=2*(sinh(11/10)-11/10).
a=Q(11,10)
slo=sum((a**(2*j+1)/factorial(2*j+1) for j in range(6)),Q(0))
first=a**13/factorial(13)
ratio=a*a/Q(14*15)
shi=slo+first/(1-ratio)
K2_UP=2*(shi-a)
assert 0<K2_UP<Q(12,25)

# Original physical window I=(-11/10,11/10): 
# 132000 * (1/60000) = 11/5 exactly.
I_LENGTH=Q(11,5)
M=132000
W=I_LENGTH/M
assert W==Q(1,60000)
R=5000  # unitary Fourier frequencies xi, with gamma argument t=-2*pi*xi
# If |xi|>=5000, |t|>=10000*pi>30000 because pi>3.
assert 2*R*3==T
# Cellwise zero-mean + sharp interval Poincare, Fourier Bernstein:
# low Fourier L2 mass <= (2*w*R)^2 * whole mass.
LOW_FRACTION=(2*W*R)**2
assert LOW_FRACTION==Q(1,36)

GAMMA_COEFF=Q(8)-(Q(8)+Q(28,5))*LOW_FRACTION
assert GAMMA_COEFF==Q(343,45)
SIGNED_LO=GAMMA_COEFF-Q(71,10)-Q(12,25)
assert SIGNED_LO==Q(19,450)>0
assert (Q(21,50)-(Q(68,5))*LOW_FRACTION)==SIGNED_LO

# Two optional, sharper mesh variants by exactly the same proof.
optional={}
for mesh in (176000,220000):
    cellw=I_LENGTH/mesh
    beta=(2*R*cellw)**2
    lower=Q(21,50)-Q(68,5)*beta
    assert lower>0
    optional[str(mesh)]={'width':str(cellw),'low_band_fraction':str(beta),'full_weil_high_mode_lower':str(lower),'numerical_value':float(lower)}
assert optional['176000']['full_weil_high_mode_lower']=='83/400'
assert optional['220000']['full_weil_high_mode_lower']=='71/250'

# Coarser *100,000-cell* finite-codimension variant. Reoptimize the actual
# NF599 finite positive gains, not an extrapolation from the |t|>=30000 case.
# 2*pi*4334 > 26000 follows from pi>3, since 6*4334=26004.
T_COARSE=26000
N_COARSE=100000
SCALE_COARSE=10**8
NUM_COARSE=16*T_COARSE*T_COARSE
DEN_COARSE=4*T_COARSE*T_COARSE
FLOOR_COARSE=sum((NUM_COARSE*SCALE_COARSE)//((4*n+1)*((4*n+1)**2+DEN_COARSE)) for n in range(N_COARSE))
assert FLOOR_COARSE==1369127830, FLOOR_COARSE
GAMMA_COARSE_LO=GAMMA_ZERO_LO+Q(FLOOR_COARSE,SCALE_COARSE)
GAMMA_COARSE_BUDGET=Q(8091,1000)
assert GAMMA_COARSE_LO>GAMMA_COARSE_BUDGET
R_COARSE=4334
assert 6*R_COARSE>T_COARSE
M_COARSE=100000
W_COARSE=I_LENGTH/M_COARSE
assert W_COARSE==Q(11,500000)
BETA_COARSE=(2*R_COARSE*W_COARSE)**2
assert BETA_COARSE==Q(23837,125000)**2
W_COARSE_LO=GAMMA_COARSE_BUDGET-(GAMMA_COARSE_BUDGET-GAMMA_ZERO_LO)*BETA_COARSE-Q(71,10)-Q(12,25)
assert W_COARSE_LO==Q(205113627821,15625000000000)
assert W_COARSE_LO>Q(1,100)

# A 2x2 exact countermodel: positive diagonal compression and Q-bound
# alone DO NOT certify positive whole form; offdiagonal Schur matters.
A=Q(1,100);D=SIGNED_LO;B=Q(1,10)
DETERMINANT=A*D-B*B
assert A>0 and D>0 and DETERMINANT<0
assert DETERMINANT==-Q(431,45000)

report={
  'stage':'IV047',
  'status':'original-source mathematical infinite-dimensional theorem, pure exact-rational local checker PASS; NOT Lean kernel',
  'support_window':'(-11/10,11/10)',
  'fourier_convention':'unitary F(f)(xi)=integral f(x)*exp(-2*pi*i*x*xi) dx',
  'gamma_cutoff_abs_t':T,
  'gamma_nf599_gain_terms':NF_TERMS,
  'gamma_gain_floor_scale':SCALE,
  'gamma_gain_floor_integer_sum':FLOOR_TOTAL,
  'gamma_gain_rational_lower':str(GAIN_LO),
  'gamma_symbol_at_cutoff_strict_rational_lower':str(GAMMA_T_LO),
  'certified_conservative_gamma_cutoff':'>8 for |t|>=30000',
  'original_active_prime_indices':[x for x,_ in active],
  'original_prime_full_twosided_norm_upper_float':float(PRIME_NORM_UP),
  'prime_bound_comparison':'<71/10',
  'original_odd_negative_pole_norm_square_upper_float':float(K2_UP),
  'negative_pole_bound_comparison':'<12/25',
  'partition_cell_count':M,
  'partition_width':str(W),
  'conditional_subspace':'all L2 I-supported gamma-form-domain q with integral(q,I_j)=0 for every cell',
  'fourier_low_band_halfwidth_xi':R,
  'fourier_low_band_relative_mass_upper':str(LOW_FRACTION),
  'gamma_high_mode_lower_coefficient':str(GAMMA_COEFF),
  'complete_original_signed_weil_high_mode_lower_coefficient':str(SIGNED_LO),
  'explicit_negative_index_bound':'n_-(W) <= 132000; even and odd <=66000, under classical closed-form compact-resolvent construction',
  'optional_meshes':optional,
  'improved_finite_codimension_variant':{
      'partition_cell_count':M_COARSE,
      'partition_width':str(W_COARSE),
      'NF599_gain_t':T_COARSE,
      'NF599_gain_terms':N_COARSE,
      'NF599_gain_integer_floor_scale':SCALE_COARSE,
      'NF599_gain_integer_floor_sum':FLOOR_COARSE,
      'original_gamma_symbol_strict_lower':str(GAMMA_COARSE_LO),
      'conservative_gamma_high_cutoff':str(GAMMA_COARSE_BUDGET),
      'Fourier_low_band_R':R_COARSE,
      'Fourier_low_fraction':str(BETA_COARSE),
      'complete_original_signed_W_high_mode_lower':str(W_COARSE_LO),
      'coarse_rational_positive_bound':'>1/100',
      'even_odd_finite_codimension_each':M_COARSE//2,
  },
  'positive_two_blocks_not_enough_schur_counterexample':{'A':str(A),'D':str(D),'B':str(B),'det':str(DETERMINANT)},
  'finite_low_mode_compression_and_offdiagonal_schur':'UNRESOLVED; no whole window positivity',
  'classical_math_not_verified_by_script':['Fourier projection duality','cellwise sharp Neumann Poincare','bandlimited Bernstein inequality','form-domain closure','original gamma-Fourier source attachment','finite Schur complement operators'],
  'predecessor_source_checker_sha256':predecessor_sha,
  'no_new_ci':True,
  'no_global_Weil_positivity_or_RH_claim':True,
}
report['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
print('IV047 exact integer/rational high-mode source preflight PASS — NONKERNEL')
print('NF599 floor gains: ',FLOOR_TOTAL,'/',SCALE,'; gamma at |t|>=30000 >',GAMMA_T_LO,'> 8')
print('P original twosided < 71/10 and true negative pole eigenvalue <12/25')
print('partition',M,'cells of width',W, '; Fourier low-band fraction <=',LOW_FRACTION)
print('Gamma high-mode >',GAMMA_COEFF,'; full signed Weil >',SIGNED_LO,' times L2 mass')
print('optimized 100000-cell variant: gamma >',GAMMA_COARSE_LO,'; low band <=',BETA_COARSE,'; W >',W_COARSE_LO,'> 1/100')
print('Schur necessity toy determinant: ',DETERMINANT,'<0 (both diagonal blocks >0)')
print('script SHA256:',report['checker_sha256'])
print('receipt:',OUT)
