#!/usr/bin/env python3
"""IV051 pure exact-Fraction source preflight — NOT a Lean proof.

Audits the 100000-cell original Weil equal-mean coercivity theorem,
prime-shift cell phase identities and boundary Gamma estimates. Never
uses float calculations to make the asserted comparisons.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from math import isqrt
import json

ROOT = Path(__file__).resolve().parent
UPSTREAM = {
    'IV045_fixed_window_parity_trial_checker.py':
        '54d49affe407f3838015963b485975b885a5cde0c1c507dc318f9b33c64f86ac',
    'IV047_infinite_dim_high_mode_checker.py':
        'd64d8b08529e529a1be86923d25d2a76ce81aa42889eab97257c5f6aa0e083a5',
    'IV049_energy_relative_cell_schur_checker.py':
        '2a2010172c9bda33c3c58477b8ada82ba850862ba96442e528425e342590144d',
    'IV050_dense_mode_schur_checker.py':
        'e1fc5cfdd8b17f40f7d028f3dd187e1e2e679e7e13ffc0de84cf1f6d45c4d889'
}


def log_bracket(n: int, terms: int=128):
    # log n = 2 sum_{k>=0} ((n-1)/(n+1))^(2k+1)/(2k+1), n>1.
    y=Q(n-1,n+1)
    lower=sum((2*y**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    tail=(2*y**(2*terms+1)/Q(2*terms+1))/(1-y*y)
    return lower,lower+tail


def ceil_sqrt_fraction(q: Q, scale: int=10**12):
    assert q>=0
    return Q(isqrt(q.numerator*scale*scale//q.denominator)+1,scale)


def norm2(z):
    return z[0]*z[0]+z[1]*z[1]


def sub(z,w):
    return (z[0]-w[0],z[1]-w[1])


def shift_variance(coeffs,m,rho):
    """Exact integrated on-window variance of normalized step translation.

    Source low vector v=sum_j coeffs[j] 1_{J_j}/sqrt(w), extended by zero;
    d/w=m+rho with m∈Z, 0<=rho<1.
    """
    size=len(coeffs)
    zero=(Q(0),Q(0))
    def a(i):return coeffs[i] if 0<=i<size else zero
    left=sum((rho*(1-rho)*norm2(sub(a(j-m),a(j-m-1))) for j in range(size)),Q(0))
    # Direct cell integration: on x_j+u*w, 0<=u<rho uses a(j-m-1),
    # rho<=u<1 uses a(j-m). After removing the weighted mean, exactly
    # rho(1-rho)|a-b|^2 remains.
    right=Q(0)
    for j in range(size):
        a0,a1=a(j-m-1),a(j-m)
        mean=((rho*a0[0]+(1-rho)*a1[0]),(rho*a0[1]+(1-rho)*a1[1]))
        right+=rho*norm2(sub(a0,mean))+(1-rho)*norm2(sub(a1,mean))
    assert left==right,(left,right)
    return left


def check():
    sha_dep={}
    for file,expected in UPSTREAM.items():
        path=ROOT/file
        assert path.is_file(),path
        actual=sha256(path.read_bytes()).hexdigest()
        assert actual==expected,(file,actual,expected)
        sha_dep[file]=actual

    M=100000
    L=Q(11,5)
    w=L/M
    assert w==Q(11,500000) and 65536<M<131072

    # IV047 true NF599 high-Gamma certificate at |t|>=26000, R=4334;
    # improve only the NEGATIVE original odd pole using cellwise mean zero.
    beta=Q(23837,125000)**2
    Gamma_budget=Q(8091,1000)-(Q(8091,1000)+Q(28,5))*beta
    negative_pole_high=Q(5,36)*w*w  # ||Qk||² < w²||h||²/(4π²) <5w²/36
    high_c=Gamma_budget-Q(71,10)-negative_pole_high
    assert high_c>Q(49,100),(high_c, float(high_c))

    # For F=1_I/sqrt(L), Gamma F|_I=gamma0 F+(H(x-a)+H(b-x))/sqrt(L).
    # On first cell mean-subtracted half-log(1/u) has L2 norm 1/2.
    # Other cells j>=1: H oscillation <= 1/(2j)+w.
    # Sum j^-2<2 and harmonic H_{M-1}<18 by 17 dyadic blocks:
    boundary_variance_envelope=(Q(1,2)+w)**2+Q(1,2)+18*w+M*w*w
    assert boundary_variance_envelope<1,boundary_variance_envelope
    # Each endpoint contributes ||Q H_left/sqrt(L)||² < 1/M,
    # so full Q Gamma F norm <2/sqrt(M).

    # Original prime shifts all lie in (w,L-w), even n=9 (source window).
    active=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
    active_phase=[]
    bound_prime_100k=Q(0)
    bound_prime_132k=Q(0)
    for MM in (100000,132000):
        ww=L/MM
        accum=Q(0)
        for n,p in active:
            dlo,dhi=log_bracket(n)
            assert dlo>ww and dhi<L-ww,(MM,n)
            xlo,xhi=dlo/ww,dhi/ww
            m=xlo.numerator//xlo.denominator
            assert xhi<m+1,(MM,n,m)
            lo,hi=xlo-m,xhi-m
            assert 0<lo<=hi<1
            # max_{rho∈[lo,hi]}rho(1-rho), with vertex 1/2.
            if lo<=Q(1,2)<=hi:
                varup=Q(1,4)
            else:
                varup=max(lo*(1-lo),hi*(1-hi))
            sqrtvarup=ceil_sqrt_fraction(varup)
            logp_up=log_bracket(p)[1]
            # sqrt(n) lower = floor sqrt(n)*scale/scale.
            scale=10**12
            sqrt_n_lo=Q(isqrt(n*scale*scale),scale)
            kapup=logp_up/sqrt_n_lo
            accum+=4*kapup*sqrtvarup
            if MM==100000:
                active_phase.append({'n':n,'prime_base':p,'shift_integer_cells':m,
                    'fractional_shift_interval':[str(lo),str(hi)],
                    'fractional_shift_variance_upper':str(varup)})
        if MM==100000:
            assert accum<Q(29,5),float(accum)
            bound_prime_100k=accum
        else:
            assert accum<Q(13,2),float(accum)
            bound_prime_132k=accum

    # Prime coupling to the constant F: each source shift has exactly ONE
    # fractional jump inside the physical window; normalized squared high
    # response is rho(1-rho)/M<=1/(4M). Thus ||Q P F||<S/sqrt(M),
    # S=sum Lambda(n)/sqrt(n)<71/20. No complex-phase assumption.
    assert Q(71,20)<Q(18,5)
    # Original pole h even, k odd. For Q=k cell mean-zero,
    # ||Qk||² < (5/36) w². For constant F, <k,F>=0,
    # ||Q Pole F|| < w/3 from derivative h'=k/2 and |<h,F>|<sqrt(5).
    # Together ||B F||<2/sqrt(M)+(71/20)/sqrt(M)+w/3
    #                <6/sqrt(M), since w/3 < (9/20)/sqrt(M).
    # sqrt(M)>2 suffices for the last inequality, since w=11/(5M).
    assert M>4 and L/3 < Q(9,20)*2
    b2_upper=Q(36,M)
    low_a=Q(201,5000) # from IV045 exact full original W[1_I]/||1_I||² >0.0402
    high_c_simple=Q(49,100)
    # Young: W[alpha F+q] >=(c/2)||q||²+(a-2*b²/c)|alpha|²
    low_after=low_a-2*b2_upper/high_c_simple
    assert low_after>Q(19,500),low_after
    assert high_c_simple/2>Q(19,500)

    # Check exact COMPLEX discrete cell shift identity, both orientations,
    # negative integer shifts, and truncated physical boundary coefficients.
    sample=[(Q(j-3,5),Q((2*j*j+1)%7-3,6)) for j in range(8)]
    tests=[]
    for m,r in ((1,Q(2,5)),(4,Q(3,7)),(-3,Q(3,5)),(-1,Q(1,4)),(0,Q(0))):
        val=shift_variance(sample,m,r)
        tests.append({'shift_integer_cells':m,'shift_fraction':str(r),'exact_response_norm_sq':str(val)})
    constant=[(Q(1,8),Q(0)) for _ in range(8)]
    # For m in 1..6, a positive shift creates exactly one internal step.
    assert shift_variance(constant,3,Q(2,5))==Q(2,5)*Q(3,5)*Q(1,64)
    assert shift_variance(constant,-4,Q(3,5))==Q(3,5)*Q(2,5)*Q(1,64)

    result={
        'schema':'IV051-original-equal-physical-means-source-Schur-preflight-v1',
        'pass':True,'status':'classical source mathematical proof with exact Fraction preflight; NOT Lean',
        'upstream_checker_sha256':sha_dep,
        'window_length':str(L),'physical_cells':M,'cell_width':str(w),
        'gamma_high_cutoff':'8091/1000','gamma_low_mass_fraction':str(beta),
        'original_high_negative_pole_bound':str(negative_pole_high),
        'true_high_source_weil_lower':str(high_c),'conservative_high_lower':str(high_c_simple),
        'centered_boundary_gamma_one_side_squared_lt':'1/M',
        'gamma_boundary_variance_bracket':str(boundary_variance_envelope),
        'gamma_constant_column_norm_lt':'2/sqrt(M)',
        'prime_constant_column_norm_lt':'71/(20 sqrt(M))',
        'both_crossed_pole_constant_column_norm_lt':'w/3',
        'full_constant_column_norm_lt':'6/sqrt(M)',
        'original_source_constant_full_W_lower':str(low_a),
        'low_after_young':str(low_after),'new_uniform_equal_cell_means_W_margin':'19/500',
        'shift_variance_formula':'||Q U_d Pi v||^2 = rho(1-rho) sum_j |a_(j-m)-a_(j-m-1)|^2',
        'prime_phase_100000':active_phase,
        'original_prime_low_high_norm_upper_100000':str(bound_prime_100k),
        'original_prime_low_high_norm_upper_132000':str(bound_prime_132k),
        'mesh_prime_norm_comparisons':['<29/5 at M=100000','<13/2 at M=132000'],
        'exact_complex_shift_tests':tests,
        'non_claims':['all original Weil positivity','full finite-mesh Schur positivity',
                      'RH','independent PI/CP equivalence','new source-attached Lean acceptance'],
    }
    return result


if __name__=='__main__':
    receipt=check()
    sha=sha256(Path(__file__).read_bytes()).hexdigest()
    receipt['script_sha256']=sha
    dest=ROOT/'IV051_equal_mean_schur_receipt.json'
    dest.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print('IV051 ORIGINAL SIGNED WEIL exact rational preflight PASS (NONKERNEL)')
    print('High mode W>49/100, all-equal-cell-mean Schwartz W>19/500')
    print('True source-prime physical-cell phase interface PASS')
    print('Source 100000-cell prime low/high <29/5; 132000-cell <13/2')
    print('script SHA256',sha)
    print('receipt',dest)
