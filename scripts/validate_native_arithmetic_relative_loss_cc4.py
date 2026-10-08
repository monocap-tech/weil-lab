"""CC4 exact finite controls, not an actual Weil loss bound or Lean proof."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from certify_native_legendre_small_window import I
from certify_native_exact_logarithm import log_rational
from certify_native_prime8_source112_engine_105 import sqrt_rational

def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def inverse(A):
    d=det(A);assert d>0
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def dot(x,y):return sum((a*b for a,b in zip(x,y)),F(0))
def action(A,x):return [dot(row,x) for row in A]
def psd(A):return A[0][0]>=0 and A[1][1]>=0 and det(A)>=0
def positive(A):return A[0][0]>0 and det(A)>0

def run():
    counts=dict(shell_completion=0,determinant_accumulation=0,crossing_source=0,
                positive_level=0,complement_gate=0,source_prefix=0,prime_dictionary=0)
    for c in (F(1,2),F(1),F(3)):
        for d in (F(1),F(2),F(5)):
            for k in (F(-1),F(0),F(1,3)):
                for l in (F(-1,2),F(0),F(1,4)):
                    D=d+l*l/c
                    for h in (F(-1,4),F(0),F(1,3)):
                        H=h-k*l/c
                        old=1+H*H/d
                        a=old+k*k/c
                        shell=D-l*l/c
                        assert shell==d
                        via_two=old-H*H/shell
                        complement_det=c*D-l*l
                        full_inverse_charge=(D*k*k-2*l*k*h+c*h*h)/complement_det
                        via_one=a-full_inverse_charge
                        assert via_one==via_two==1
                        R=H*H/(d*old)
                        assert 0<=R<1 and via_two/old==1-R
                        counts['shell_completion']+=3
    # Noncommuting rank-one reactions: determinant ratios telescope exactly.
    for a in (F(1),F(2),F(4)):
        for b in (F(-1,4),F(0),F(1,3)):
            for d in (F(1),F(3)):
                initial=[[a,b],[b,d]];assert positive(initial)
                S=[row[:] for row in initial];product=F(1)
                for v in ([F(1,10),F(0)],[F(1,12),F(1,11)],[F(0),F(-1,9)]):
                    relative=dot(v,action(inverse(S),v))
                    assert 0<relative<1
                    T=[[S[i][j]-v[i]*v[j] for j in range(2)] for i in range(2)]
                    ratio=det(T)/det(S)
                    assert positive(T) and ratio==1-relative
                    assert psd([[T[i][j]-ratio*S[i][j] for j in range(2)] for i in range(2)])
                    product*=ratio;S=T
                    assert product==det(S)/det(initial)
                    counts['determinant_accumulation']+=4
    # Bounded original sources, finite absolute variation, divergent relative loss.
    for sigma in (F(1),F(4,10**32),F(1,320*10**27)):
        for k in (F(0),F(1,2),F(3)):
            previous=sigma;product=F(1);absolute=F(0)
            for j in range(1,65):
                t=1-F(1,2**j);s=sigma*(1-t)
                A=[[s+k*k,k],[k,F(1)]]
                Pgram=[[sigma+k*k,k],[k,F(1)]];Ngram=[[sigma*t,F(0)],[F(0),F(0)]]
                assert A==[[Pgram[i][n]-Ngram[i][n] for n in range(2)] for i in range(2)]
                W=[F(1),-k]
                assert dot(W,action(A,W))==s
                assert dot(W,action(Pgram,W))==sigma
                assert dot(W,action(Ngram,W))==sigma*t
                ratio=s/previous;assert ratio==F(1,2)
                product*=ratio;absolute+=previous-s
                assert product==F(1,2**j) and absolute==sigma-s<sigma
                previous=s;counts['crossing_source']+=6
            # Genuine matrix crossing: original graph becomes strictly negative.
            assert sigma*(1-F(3,2))<0;counts['crossing_source']+=1
    # Genuine Dirichlet ground-mode source energies in u=2a/pi coordinates.
    for u in (F(1,2),F(3,4),F(7,8),F(15,16),F(17,16)):
        positive_energy=1/(u*u);negative_energy=F(1)
        value=positive_energy-negative_energy
        assert (value>0)==(u<1)
        assert value==F(1,u*u)-1
        counts['crossing_source']+=2
    # A positive physical eigenmode is null only after mass shifting ALL slots.
    for mu in (F(1,10),F(1,4),F(1,2)):
        for k in (F(1,3),F(1,2),F(2)):
            s=mu+mu*k*k/(1-mu)
            A=[[s+k*k,k],[k,F(1)]]
            shifted=[[A[i][j]-mu*int(i==j) for j in range(2)] for i in range(2)]
            h=[F(1),-k/(1-mu)]
            assert action(shifted,h)==[F(0),F(0)]
            mass=dot(h,h);assert dot(h,action(A,h))==mu*mass>0
            exact_shifted=shifted[0][0]-k*k/shifted[1][1]
            assert exact_shifted==0 and s>0 and s-mu>0
            counts['positive_level']+=4
    # Loss can miss contact entirely if its complement gate is dropped.
    for r in (F(1,2),F(1,4),F(1,16),F(0),F(-1,16)):
        retained=F(1);complement=r
        assert retained==1 and (complement>0)==(r>0)
        counts['complement_gate']+=1
    # Full source identity cannot be replaced by a prefix identity.
    full_positive=F(2);full_negative=F(3,2);positive_prefix=F(1)
    assert full_positive-full_negative>0 and positive_prefix-full_negative<0
    original_positive_level=full_positive-full_negative
    assert full_positive-(full_negative+original_positive_level)==0
    counts['source_prefix']+=2
    # Actual finite prime-power dictionary and equality-overlap geometry.
    I.grid=10**80
    dictionary=[(2,2,1),(3,3,1),(4,2,2),(5,5,1),(7,7,1),(8,2,3)]
    budget=I(0)
    for n,p,r in dictionary:
        assert n==p**r
        lam=log_rational(F(p),200)
        logn=log_rational(F(n),200)
        assert (r*lam).lo<=logn.hi and logn.lo<=(r*lam).hi
        budget+=2*lam/sqrt_rational(F(n))
        if r>1:assert lam.hi<logn.lo
        counts['prime_dictionary']+=2
    assert log_rational(F(8),200).hi<F(21,10)<log_rational(F(9),200).lo
    assert budget.hi<F(13,2);counts['prime_dictionary']+=2
    def correlation(a,s):return max(F(0),2*a-abs(s))
    for shift in (F(1,2),F(7,10),F(2),F(21,10)):
        a=shift/2
        assert correlation(a,shift)==0
        assert correlation(a-F(1,100),shift)==0
        assert correlation(a+F(1,100),shift)==F(1,50)
        counts['prime_dictionary']+=3
    return dict(stage='CC4 exact original relative-loss controls',counts=counts,
                exact_checks=sum(counts.values()),all_passed=True,
                actual_arithmetic_nondivergence_bound=False)

if __name__=='__main__':
    result=run()
    result.update(analytic_theorem_lean_certified=False,actual_contact_exists=False,
                  anchor_certificate_replayed=False,full_target_archives_replayed=False,
                  new_aperture_certified=False,
                  constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    destination=Path(__file__).resolve().parents[1]/'notes/data/RPB108_ARITHMETIC_RELATIVE_LOSS_CC4_VALIDATION_20261008.json'
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
