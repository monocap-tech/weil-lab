#!/usr/bin/env python3
"""IV045: exact rational fixed-window even source Weil trial and index-free scalar gate.

Pure standard library. Proves rational enclosures for the interval-indicator
Gamma/prime/two-pole quadratic form, GIVEN the classically derived source
Gamma difference form and literal prime/pole coefficients. Does NOT verify
Fourier inversion in Lean or any global spectral index/inverse moment.
"""
from fractions import Fraction as Q
from math import isqrt, factorial
from pathlib import Path
from hashlib import sha256
import json

L=Q(11,10)
M=2*L

def bracket_arctan_inv(q,N):
    # arctan(1/q), alternating, with opposite parity truncated values.
    terms=[Q((-1)**i,(2*i+1)*q**(2*i+1)) for i in range(N+1)]
    s=sum(terms[:-1],Q(0))
    other=s+terms[-1]
    return min(s,other),max(s,other)

def bracket_pi():
    a,b=bracket_arctan_inv(5,24)
    c,d=bracket_arctan_inv(239,8)
    return 16*a-4*d,16*b-4*c

def bracket_log(x,N=90):
    if x<=0: raise ValueError(x)
    if x==1:return Q(0),Q(0)
    if x<1:
        a,b=bracket_log(1/x,N)
        return -b,-a
    y=(x-1)/(x+1)
    assert 0<y<1
    s=sum((2*y**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    tail=2*y**(2*N+1)/(Q(2*N+1)*(1-y*y))
    return s,s+tail

def bracket_exp_pos(x,N=90):
    assert x>=0
    term=Q(1)
    s=term
    for k in range(1,N+1):
        term=term*x/k
        s+=term
    next_term=term*x/Q(N+1)
    ratio=x/Q(N+2)
    if ratio>=1: raise ValueError((x,N))
    hi=s+next_term/(1-ratio)
    return s,hi

def bracket_exp_neg(x,N=90):
    a,b=bracket_exp_pos(x,N)
    return 1/b,1/a

def bracket_sqrt(n,scale=10**15):
    k=isqrt(n*scale*scale)
    return Q(k,scale),Q(k+1,scale)

pi_lo,pi_hi=bracket_pi()
log2=bracket_log(Q(2),90)
log3=bracket_log(Q(3),120)
log5=bracket_log(Q(5),160)
log7=bracket_log(Q(7),190)
log_pi_lo=bracket_log(pi_lo,160)[0]
log_pi_hi=bracket_log(pi_hi,160)[1]
assert pi_lo>Q(314,100) and pi_hi<Q(315,100)

# Euler--Mascheroni constant enclosure:
# H_N-log N-1/(2N) < gamma_E < H_N-log N-1/(2(N+1)).
N_E=400
H=sum((Q(1,n) for n in range(1,N_E+1)),Q(0))
# 400 = 2^4*5^2
log400=(4*log2[0]+2*log5[0],4*log2[1]+2*log5[1])
euler_lo=H-log400[1]-Q(1,2*N_E)
euler_hi=H-log400[0]-Q(1,2*(N_E+1))
assert euler_lo<euler_hi

gamma0_lo=-3*log2[1]-euler_hi-pi_hi/2-log_pi_hi
gamma0_hi=-3*log2[0]-euler_lo-pi_lo/2-log_pi_lo
assert gamma0_lo<gamma0_hi

# Catalan G = sum (-1)^j/(2j+1)^2, absolute alternating residual.
N_G=250
Gpart=sum((Q((-1)**j,(2*j+1)**2) for j in range(N_G)),Q(0))
G_next=Q(1,(2*N_G+1)**2)
Glo,Ghi=(Gpart,Gpart+G_next) if N_G%2==0 else (Gpart-G_next,Gpart)
assert Glo<Ghi
# sum_n 1/(2(n+1/4)^2) = pi^2/2 + 4*Catalan.
Slo=pi_lo*pi_lo/2+4*Glo
Shi=pi_hi*pi_hi/2+4*Ghi

# D[1_(-L,L)] = above full series minus exact exp term series.
NEXP=4
cor_lo=Q(0)
cor_hi=Q(0)
for n in range(NEXP):
    a=Q(n)+Q(1,4)
    fac=Q(1)/(2*a*a)
    elo,ehi=bracket_exp_neg((4*n+1)*L,95)
    cor_lo+=fac*elo
    cor_hi+=fac*ehi
# Uncomputed exponential tail <= exp(-(4 NEXP+1)L) * [1/(2(NEXP-3/4))]
exp_tail_hi=bracket_exp_neg((4*NEXP+1)*L,95)[1]/(2*(Q(NEXP)-Q(3,4)))
Dlo=Slo-cor_hi-exp_tail_hi
Dhi=Shi-cor_lo
assert Dlo<Dhi

# Prime n=2,3,4,5,7,8,9 only; both orientations.
active=[(2,log2,log2),(3,log3,log3),
        (4,log2,(2*log2[0],2*log2[1])),
        (5,log5,log5),(7,log7,log7),
        (8,log2,(3*log2[0],3*log2[1])),
        (9,log3,(2*log3[0],2*log3[1]))]
Plo=Q(0);Phi=Q(0)
for n,(lp_lo,lp_hi),(shift_lo,shift_hi) in active:
    sqrt_lo,sqrt_hi=bracket_sqrt(n)
    assert shift_hi<M,(n,float(shift_hi),float(M))
    Plo+=2*(lp_lo/sqrt_hi)*(M-shift_hi)
    Phi+=2*(lp_hi/sqrt_lo)*(M-shift_lo)

# pole[1_(-L,L)] = 16(cosh L - 1) = 8(exp L + exp(-L) - 2).
exp_lo,exp_hi=bracket_exp_pos(L,95)
exp_n_lo,exp_n_hi=1/exp_hi,1/exp_lo
polelo=8*(exp_lo+exp_n_lo-2)
polehi=8*(exp_hi+exp_n_hi-2)

Wlo=gamma0_lo*M+Dlo-Phi+polelo
Whi=gamma0_hi*M+Dhi-Plo+polehi
qlo=Wlo/M
qhi=Whi/M
assert Q(0)<qlo<qhi<Q(1,20), (float(qlo),float(qhi))
# Sharper outward integer-decimal bracket, extremely useful for falsification.
assert Q(402,10000) < qlo < qhi < Q(405,10000), (float(qlo),float(qhi))
assert gamma0_hi<0 and Dlo>0 and Plo>0 and polelo>0

# Negative even T on this trial; the positive even pole actually repairs it.
Tlo=gamma0_lo*M+Dlo-Phi
Thi=gamma0_hi*M+Dhi-Plo
assert Thi<0 and Wlo>0

# Independent ODD trial S(x)=sign(x) 1_(-L,L), living in the same
# closed Gamma form domain. The source prime autocorrelation at shift d:
# C_S(d)=2L-3d for 0<=d<=L, and C_S(d)=d-2L for L<=d<=2L.
# Exact Dirichlet atom D_a[S]=(3-4e^(-2aL)+e^(-4aL))/(2a²).
# The constant infinite sum is 3*(pi²/2+4Catalan).

def interval_mul(A,B):
    products=[x*y for x in A for y in B]
    return min(products),max(products)

NB=10
B_lo=B_hi=C_lo=C_hi=Q(0)
for n in range(NB):
    a=Q(n)+Q(1,4)
    factor=1/(2*a*a)
    elo,ehi=bracket_exp_neg((4*n+1)*L/2,105)
    B_lo+=factor*elo
    B_hi+=factor*ehi
    elo,ehi=bracket_exp_neg((4*n+1)*L,105)
    C_lo+=factor*elo
    C_hi+=factor*ehi
Btail_hi=bracket_exp_neg((4*NB+1)*L/2,110)[1]/(2*(Q(NB)-Q(3,4)))
Ctail_hi=bracket_exp_neg((4*NB+1)*L,110)[1]/(2*(Q(NB)-Q(3,4)))
Dodd_lo=3*Slo-4*(B_hi+Btail_hi)+C_lo
Dodd_hi=3*Shi-4*B_lo+C_hi+Ctail_hi
assert Dodd_lo<Dodd_hi
Podd_lo=Podd_hi=Q(0)
for n,(lp_lo,lp_hi),(shift_lo,shift_hi) in active:
    assert shift_hi<L if n in (2,3) else shift_lo>L
    if shift_hi<L:
        cov=(M-3*shift_hi,M-3*shift_lo)
    else:
        cov=(shift_lo-M,shift_hi-M)
    rootlo,roothi=bracket_sqrt(n)
    kappa=(lp_lo/roothi,lp_hi/rootlo)
    lo,hi=interval_mul(kappa,cov)
    Podd_lo+=2*lo
    Podd_hi+=2*hi

# |<k,S>|²=32*(cosh(L/2)-1)^2, true NEGATIVE source pole.
epos_lo,epos_hi=bracket_exp_pos(L/2,100)
eneg_lo,eneg_hi=1/epos_hi,1/epos_lo
chlo=(epos_lo+eneg_lo)/2
chhi=(epos_hi+eneg_hi)/2
assert chlo>1
poleodd_lo=32*(chlo-1)**2
poleodd_hi=32*(chhi-1)**2
Wodd_lo=gamma0_lo*M+Dodd_lo-Podd_hi-poleodd_hi
Wodd_hi=gamma0_hi*M+Dodd_hi-Podd_lo-poleodd_lo
assert Q(202,1000)<Wodd_lo/M<Wodd_hi/M<Q(203,1000), (float(Wodd_lo/M),float(Wodd_hi/M))
# The even constrained quotient value from this witness is
# -1+W[F]/|<h,F>|²; any hypothesized even positivity requires A_e >= -1,
# while the explicit witness certifies A_e < -1 + 83/10000.
even_relative_slack_lo=Wlo/polehi
even_relative_slack_hi=Whi/polelo
assert Q(82,10000)<even_relative_slack_lo<even_relative_slack_hi<Q(83,10000)

# The index-free form gate is exact algebra for any Hermitian form Q and functional l:
# W_s[f]=Q[f]+s|l(f)|²; W_s>=0 iff (Q>=0 on ker l) and
# inf_{l(f)=1} Q[f] >= -s. We check a complex rational 2-d model,
# including a zero mode and a pathological non-coercive crossing case.
def q2(a,b,c,u,v):
    # real symmetric [[a,b],[b,c]]
    return a*u*u+2*b*u*v+c*v*v
# l(u,v)=u, f=(u,v): if Q|ker l has c>=0 then affine
# minimization at u=1 is (a-b²/c) for c>0,
# and -infty when c=0,b !=0.
for a,b,c,sign in [(-2,Q(1,2),Q(2),1),
                     (Q(-1,2),Q(1,4),Q(2),1),
                     (Q(2),Q(1),Q(2),-1),
                     (Q(0),Q(0),Q(0),1),
                     (Q(1),Q(1),Q(0),1)]:
    if c>0:
        inf=a-b*b/c
        assert q2(a,b,c,Q(1),-b/c)==inf
        criterion=(inf>=-sign)
        determinant=(a+sign)*c-b*b
        assert criterion==(determinant>=0)
    elif b==0:
        assert q2(a,b,c,Q(1),Q(1))==a
    else:
        assert q2(a,b,c,Q(1),-Q(10**6)*b)<0

receipt={
 'stage':'IV045',
 'standing':'exact rational enclosure of a single original full-window even FORM-domain trial; no spectral lower-bound proof or Lean kernel acceptance',
 'physical_support':'(-11/10,11/10)',
 'trial':'F = 1_(-11/10,11/10) even, in closed Gamma form domain, approximable by genuine even C_c-infinity Schwartz',
 'exact_source_gamma0':'-3 log2 - EulerMascheroni - pi/2 - log pi',
 'exact_source_D':'pi²/2+4 Catalan - sum_(n>=0) exp(-(4n+1)*11/10)/(2*(n+1/4)²)',
 'exact_source_P':'sum_(n=2,3,4,5,7,8,9) 2 Lambda(n)/sqrt(n) * (11/5-log n)',
 'exact_source_poles':'16(cosh(11/10)-1)',
 'EulerGamma_enclosure_source':'H400-log400-1/800 < EulerGamma < H400-log400-1/802',
 'catalan_terms':N_G,'euler_H_N':N_E,'exp_correction_terms':NEXP,
 'bounds_float_display_only':{key:[f'{float(v[0]):.12f}',f'{float(v[1]):.12f}'] for key,v in {
  'gamma0':(gamma0_lo,gamma0_hi),
  'Dirichlet_D':(Dlo,Dhi),
  'prime_P':(Plo,Phi),
  'both_poles':(polelo,polehi),
  'even_trial_full_W':(Wlo,Whi),
  'even_trial_normalized':(qlo,qhi),
  'even_trial_pole_free_T':(Tlo,Thi)
 }.items()},
 'rigorous_lower_normalized':'402/10000',
 'rigorous_upper_normalized':'405/10000',
 'odd_trial':{'form':'S=sgn(x)*1_I', 'source_D_formula':'3*(pi²/2+4Catalan)-4 sum exp(-(4n+1)L/2)/(2a_n²)+sum exp(-(4n+1)L)/(2a_n²)','source_prime_correlation':'C(d)=2L-3d if 0<=d<=L, C(d)=d-2L if L<=d<=2L', 'Gamma_D_interval':[f'{float(Dodd_lo):.12f}',f'{float(Dodd_hi):.12f}'],'Prime_interval':[f'{float(Podd_lo):.12f}',f'{float(Podd_hi):.12f}'],'negative_pole_abs_interval':[f'{float(poleodd_lo):.12f}',f'{float(poleodd_hi):.12f}'],'whole_W_interval':[f'{float(Wodd_lo):.12f}',f'{float(Wodd_hi):.12f}'],'normalized_interval_float':[float(Wodd_lo/M),float(Wodd_hi/M)],'rigorous_normalized_bracket':['202/1000','203/1000']},
 'even_constrained_slack_interval_float':[float(even_relative_slack_lo),float(even_relative_slack_hi)],
 'minmax_even_upper':'lambda_min(W_even) <= 405/10000 (strict via smooth approximation; source mathematical not Lean)',
 'finite_rank_exact_gate': 'on each parity s=+1 (even), -1 (odd), Q+s|l|² >=0 iff Q>=0 on ker(l) and inf_{l(f)=1} Q[f]>=-s; handles zero modes',
 'limitations':'no W>=0 proof on full window; zero-mode cases included only in index-free variational gate; no certified whole source resolvent',
 'no_new_ci':True
}
receipt['checker_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
out=Path(__file__).with_name('IV045_fixed_window_parity_trial_receipt.json')
out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print('IV045 exact-rational fixed-window even source trial PASS (NONKERNEL)')
for k,v in receipt['bounds_float_display_only'].items():print(' ',k,':',v[0],'..',v[1])
print('Rigorous normalized even trial bound: 0.0402 < W[F]/||F||² < 0.0405')
print('Rigorous normalized odd trial bound: 0.202 < W[S]/||S||² < 0.203')
print('Even constrained pole repair slack in (0.0082,0.0083)')
print('index-free finite rank gate algebra PASS')
print('script_sha256',receipt['checker_sha256'])
print('receipt',out)
