#!/usr/bin/env python3
"""UOI044: exact-integer upper certificates for finite prime-shell collar interactions.
Computes exact resonance integer windows with rational exp enclosures, determines
all prime powers by full trial division, and encloses each log(p)/sqrt(n) by a
rational integer microgrid. Proves B<=Bupper and Collatz-Wielandt upper tests.
NOT a Lean compiler or native-source theorem attachment.
"""
from fractions import Fraction as F
from math import isqrt, factorial
import json
from pathlib import Path
SQRT_SCALE=1_000_000
GRID=1_000_000
G=F(2195428693,1996093750)

def ceil_fraction(x):
    return -(-x.numerator//x.denominator)

def exp_bracket(w):
    # e^w>sum_{k=0}^5 w^k/k! for w>0.
    # tail beginning k=6 has successive term ratios <=w/7.
    assert F(0)<w<F(1,2)
    L=sum((w**k/F(factorial(k)) for k in range(6)),F(0))
    rem=w**6/F(factorial(6))/(1-w/7)
    return L,L+rem

def rigorous_interval(j,k):
    N=8**(k-j)
    w=F(1,1000*8**j)+F(1,1000*8**k)
    L,U=exp_bracket(w)
    # Need exact integer boundaries by proving the uncertain ranges contain
    # no integer. Floors of N/exp(w) and N exp(w) identified exactly.
    lo_under=F(N,1)/U;lo_over=F(N,1)/L
    hi_under=F(N,1)*L;hi_over=F(N,1)*U
    low0=lo_under.numerator//lo_under.denominator
    low1=lo_over.numerator//lo_over.denominator
    high0=hi_under.numerator//hi_under.denominator
    high1=hi_over.numerator//hi_over.denominator
    assert low0==low1,(j,k,'lower ambiguous',low0,low1)
    assert high0==high1,(j,k,'upper ambiguous',high0,high1)
    return low0+1,high0

def prime_sieve(limit):
    sieve=bytearray(b'\x01')*(limit+1)
    sieve[:2]=b'\x00\x00'
    for i in range(2,isqrt(limit)+1):
        if sieve[i]:sieve[i*i:limit+1:i]=b'\x00'*(((limit-i*i)//i)+1)
    return [i for i in range(2,limit+1) if sieve[i]]

def von_mangoldt_base(n,primes):
    # Exactly 0 unless n=p^e, e>=1 for prime p; if so return p.
    assert n>=2
    for p in primes:
        if p*p>n:break
        if n%p==0:
            m=n
            while m%p==0:m//=p
            return p if m==1 else 0
    return n # prime by exhaustive trial division

def log_prime_upper(p):
    # log2<7/10, and log(r) <= (r-r^-1)/2 for r>=1.
    k=p.bit_length()-1
    two=1<<k
    return F(7*k,10)+F(p*p-two*two,2*p*two)

def coeff_ceil_micro(p,n):
    # lower rational square root rL <= sqrt(n)
    rL=isqrt(n*SQRT_SCALE*SQRT_SCALE)
    logU=log_prime_upper(p)
    return ceil_fraction(logU*SQRT_SCALE*GRID/rL)

def alpha_table(m):
    hi=max(rigorous_interval(j,k)[1] for j in range(m) for k in range(j+1,m))
    primes=prime_sieve(isqrt(hi))
    A=[[0]*m for _ in range(m)]; info=[]
    for j in range(m):
        for k in range(j+1,m):
            lo,hi=rigorous_interval(j,k)
            entries=[]
            for n in range(max(lo,2),hi+1):
                p=von_mangoldt_base(n,primes)
                if p:
                    q=coeff_ceil_micro(p,n)
                    entries.append((n,p,q))
            sq=sum(q*q for n,p,q in entries)
            ceil_alpha=isqrt(sq)+1 if sq else 0
            A[j][k]=A[k][j]=ceil_alpha
            info.append((j,k,lo,hi,len(entries),ceil_alpha,tuple(n for n,p,q in entries[:12])))
    return A,info

def collatz_bound(A,w):
    return max(F(sum(a*x for a,x in zip(row,w)),GRID*w_i) for row,w_i in zip(A,w))

def main():
    for m in (5,8,10):
        A,info=alpha_table(m)
        print('m=',m,'edges=',len(info),'max_n=',max(t[3] for t in info),flush=True)
        print('  numerical-free maximum row bound:',max(F(sum(row),GRID) for row in A))
        if m==5:
            print('  pair (0,4):', next(x for x in info if x[:2]==(0,4)))
            assert next(x for x in info if x[:2]==(0,4))[-1]==(4093,4096,4099)
            assert max(F(sum(row),GRID) for row in A)<F(17,25)
        if m==8:
            w=[428,321,300,319,401,384,365,285]
        elif m==10:
            w=[451,298,239,233,313,319,344,342,315,250]
        else:
            w=[409,458,495,458,409]
        bound=collatz_bound(A,w)
        print('  rational positive-vector spectral upper:',float(bound),str(bound),'with weights',w)
        print('  Gamma-relative rho upper',float(bound/G))
        print('  W mass lower',float(G-bound))
        if m==10:
            assert bound < F(949,1000),(bound,'need improved vector')
            assert G-F(949,1000) > F(3,20)
            print('  rigorously boxed stage-10 bound: P(f) < 949/1000 ||f||², W_lit(f) > 3/20 ||f||²')
            statement={
                'schema':'UOI044-exact-arithmetic-stage10-prime-operator-screen-v1',
                'status':'analytic integer arithmetic; NOT Lean kernel accepted',
                'family':'UOI040 D_10: I_j=( (j+1/2)log8 -1/(1000*8^j), (j+1/2)log8+1/(1000*8^j) ) for 0<=j<10',
                'original_source_sha':'614ba879f7389fdb620c474adaee273b00eac71c',
                'prime_quadratic':'P(f)=sum_n Lambda(n)/sqrt(n)(C_f(log n)+C_f(-log n))',
                'gamma_lower_fraction':str(G),
                'scalar_operator_microgrid_denominator':GRID,
                'matrix_upper_microgrid_int':A,
                'positive_schur_vector':w,
                'row_weighted_upper_fractions':[str(F(sum(a*x for a,x in zip(row,w)),GRID*w_j)) for row,w_j in zip(A,w)],
                'maximum_weighted_upper':str(bound),
                'target_upper':'949/1000',
                'gamma_minus_target_lower':str(G-F(949,1000)),
                'simplified_Weil_lower':'3/20',
                'edge_resonance_summary':[dict(j=j,k=k,smallest_candidate=lo,largest_candidate=hi,prime_power_count=c,alpha_upper_micro=a,first_12_prime_powers=ns) for j,k,lo,hi,c,a,ns in info],
                'assumptions':['analytically established UOI040 Gamma lower G on local 3-moment neutral compact smooth tests', 'original source literal full +/-log n prime normalization and both pole moments', 'exact integer prime-power classification via exhaustive trial division', 'Schur bound and disjoint translations on narrower right collar'],
                'not_proved':['Lean source/domain identity for arbitrary support','any uniform m→infinity bound', 'whole Schwartz Weil positivity','RH']
            }
            out=Path(__file__).with_name('UOI044_stage10_exact_arithmetic_receipt.json')
            out.write_text(json.dumps(statement,indent=2,sort_keys=True)+'\n')
            print('  receipt:',out)
        if m==8:
            assert bound < G
        if m==5:
            assert G-F(17,25)>F(2,5)
    print('PASS: source-geometry finite m=5,8,10 scalar norm enclosures under stated analytic Gamma lower.')
if __name__=='__main__':main()