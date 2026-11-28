#!/usr/bin/env python3
"""IV053 original-source NONKERNEL rational certificate for 2-low + full high class.

Explicit remaining mathematical premises: original source Gamma Fourier atom,
true logarithmic form domain and smooth density, and proven IV051/IV052
Hilbert-space inequalities. The finite preflight does not compile Lean.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
from hashlib import sha256
import importlib.util, json

HERE=Path(__file__).resolve().parent
PREVIOUS={
 'IV045_fixed_window_parity_trial_checker.py':'54d49affe407f3838015963b485975b885a5cde0c1c507dc318f9b33c64f86ac',
 'IV051_equal_mean_schur_checker.py':'27559e26c5d6d7217664c216b04f42feb6df05eeb411e080cfac837f56e6443a',
 'IV052_jump_gradient_and_parabolic_trial_checker.py':'336cc8bdb652b2e745be533e0af298105fd13f9e6f88ad7d34ef78bd0541c0e1',
}
for name,digest in PREVIOUS.items():
    assert sha256((HERE/name).read_bytes()).hexdigest()==digest,(name,'SHA mismatch')
spec=importlib.util.spec_from_file_location('iv052',HERE/'IV052_jump_gradient_and_parabolic_trial_checker.py')
iv=importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
A=iv.A; L=iv.L; M=100000; w=L/M


def mixed_gamma_shape(N=350):
    """Divide the normalized e-p cross Gamma quadratic form by overlap σ=√(5/6)."""
    # C_ep(u)/σ=1-3u²/(4A²)+u³/(4A³), for u∈[0,2A]
    coefs={2:F(3)/(4*A**2),3:-F(1)/(4*A**3)}
    rational=F(0); corr_lo=corr_hi=F(0)
    for n in range(N):
        t=F(n)+F(1,4);beta=2*t
        infinite=2*sum((c*F(factorial(k))/beta**(k+1) for k,c in coefs.items()),F(0))
        correction=1/t
        for k,c in coefs.items():
            inner=sum((F(factorial(k),factorial(j))*L**j / beta**(k+1-j)
                       for j in range(k+1)),F(0))
            correction-=2*c*inner
        rational+=infinite
        if n<13:
            elo,ehi=iv.exp_neg_bracket(beta*L,115)
            if correction>=0: corr_lo+=correction*elo;corr_hi+=correction*ehi
            else:corr_lo+=correction*ehi;corr_hi+=correction*elo
    # n>=13 all signed exponential corrections: bound abs(coefficient_n)<1,
    # use e^(-2(n+1/4)L), geometric ratio <1/2 and common e_13 upper.
    n0=13; alpha=F(n0)+F(1,4);beta=2*alpha
    cabs=1/alpha+2*sum((abs(c)*sum((F(factorial(k),factorial(j))*L**j/beta**(k+1-j)
                      for j in range(k+1)),F(0)) for k,c in coefs.items()),F(0))
    assert cabs<1
    assert iv.exp_pos_bracket(2*L,20)[0]>2 # genuine geometric ratio exp(-2L)<1/2
    extra=2*iv.exp_neg_bracket(beta*L,115)[1]
    corr_lo-=extra;corr_hi+=extra
    # original atom D_n(e,p)/σ >= 0 since normalized cross C(u)≤1, so
    # lower tail can be omitted, upper uses quadratic leading term & tiny exterior.
    assert coefs[2]>0 and coefs[3]<0
    t0=F(N)-F(3,4)
    tail=coefs[2]/(4*t0*t0)+extra
    return rational+corr_lo,rational+corr_hi+tail,{'terms':N,'tail_lt':str(tail)}


def mixed_prime_shape():
    # Original two-sign finite von Mangoldt shift, including 4,8,9.
    vals={2:iv.log_bracket(F(2),120),3:iv.log_bracket(F(3),150),
          5:iv.log_bracket(F(5),160),7:iv.log_bracket(F(7),185)}
    choices=((2,2,1),(3,3,1),(4,2,2),(5,5,1),(7,7,1),(8,2,3),(9,3,2))
    lo=hi=F(0)
    for n,power_base,k in choices:
        shiftlo=vals[power_base][0]*k;shifthi=vals[power_base][1]*k
        assert 0<shiftlo<shifthi<L
        # 1-3 u²/(4a²)+u³/(4a³) is monotonically DECREASING for 0<u<2a.
        def c(u): return 1-F(3)*u*u/(4*A*A)+u**3/(4*A**3)
        clow=c(shifthi);chigh=c(shiftlo)
        assert 0<=clow<=chigh<=1
        sqlo,sqhi=iv.sqrt_bracket(n)
        coefflo=vals[power_base][0]/sqhi
        coeffhi=vals[power_base][1]/sqlo
        lo+=2*coefflo*clow;hi+=2*coeffhi*chigh
    return lo,hi


def mixed_pole_shape():
    # Literal crossed pole on even source e,p divided by overlap σ:
    # <h,e><h,p>/σ = 6 sinh(a/2)*T/a, T=16 cosh(a/2)/a-32 sinh(a/2)/a².
    ppos=iv.exp_pos_bracket(A/2,110)
    pneg=(1/ppos[1],1/ppos[0])
    ch=((ppos[0]+pneg[0])/2,(ppos[1]+pneg[1])/2)
    sh=((ppos[0]-pneg[1])/2,(ppos[1]-pneg[0])/2)
    T=(16*ch[0]/A-32*sh[1]/A**2,16*ch[1]/A-32*sh[0]/A**2)
    assert T[0]>0 and sh[0]>0
    return 6*sh[0]*T[0]/A,6*sh[1]*T[1]/A


def main():
    gamma0,_=iv.gamma_base_interval()
    Dlo,Dhi,Dinfo=mixed_gamma_shape()
    Plo,Phi=mixed_prime_shape()
    Polelo,Polehi=mixed_pole_shape()
    sigma=tuple(t/6 for t in iv.sqrt_bracket(30)) # √(5/6)=√30/6
    # True signed original form! Γ − P + BOTH crossed poles; k=0 for even.
    mixshape=(gamma0[0]+Dlo-Phi+Polelo,gamma0[1]+Dhi-Plo+Polehi)
    mixed=iv.mult_iv(sigma,mixshape)
    assert F(1,2000)<mixed[0]<mixed[1]<F(11,20000),[float(v) for v in mixed] # 0.0005 < W(e,p) < 0.00055
    pp_D_lo,pp_D_hi,_=iv.gamma_parabola_D()
    pp_P_lo,pp_P_hi,_=iv.prime_parabola()
    pp_pole_lo,pp_pole_hi=iv.pole_parabola()
    pp_lo=gamma0[0]+pp_D_lo-pp_P_hi+pp_pole_lo
    pp_hi=gamma0[1]+pp_D_hi-pp_P_lo+pp_pole_hi
    assert F(639,1000000)<pp_lo<pp_hi<F(7,10000),[float(pp_lo),float(pp_hi)]

    # 100000-cell high/low source interface bound (IV051/IV052):
    # ||QWe||<6/sqrt(M)<19/1000, ||QWv||<(229/6)w<84/100000.
    be=F(19,1000);bv=F(84,100000);c=F(49,100)
    assert F(6)**2*F(1000)**2<F(19)**2*M
    assert F(229,6)*w<bv
    # q_p=p−v: ||q_p||<w/2, ||QWe||=be. Thus |W(e,v)|<=|W(e,p)|+be*w/2.
    ep_upper=mixed[1]+be*w/2
    assert ep_upper<F(56,100000),[float(mixed[0]),float(mixed[1]),float(ep_upper)]
    # W(v)=W(p)−2Re W(p,q_p)+W(q_p).
    # ||p−v||<w/2, ||Wop p||<489/20, W(q_p)>=0.
    v_lo=pp_lo-F(489,20)*w
    assert v_lo>F(1,10000),float(v_lo)
    # W−mu*L2 on low basis {e,v}; high lower c−mu.
    # Overlap |<e,v>| <=1. All actual mixed W source terms included.
    mu=F(1,20000)
    a=F(201,5000)-mu-be*be/(c-mu)
    d=v_lo-mu-bv*bv/(c-mu)
    b=ep_upper+mu+be*bv/(c-mu)
    det=a*d-b*b
    assert a>0 and d>0 and det>F(1,1000000),(float(a),float(d),float(b),float(det))
    # A compact *source-enclosed* rational certificate, avoiding giant
    # interval denominators: W[e]>201/5000, W[v]>1/10000,
    # |W(e,v)|<56/100000, ||QWe||<19/1000, ||QWv||<84/100000,
    # C_Q>49/100. No floating-point comparison enters this test.
    assert v_lo>F(1,10000)
    assert ep_upper<F(56,100000)
    ar=F(201,5000)-mu-be*be/(c-mu)
    dr=F(1,10000)-mu-bv*bv/(c-mu)
    br=F(56,100000)+mu+be*bv/(c-mu)
    drat=ar*dr-br*br
    assert ar>0 and dr>0 and drat==F(73541319,48995000000000)
    assert drat>F(1,1000000)
    # Mixed Cauchy upper has no unaccounted infinitely many q modes.
    return {
      'short_independent_rational_schur_determinant':str(drat),
      'short_rational_verified_inputs':{
        'W_e_lower':'201/5000', 'W_v_lower':'1/10000',
        'W_e_v_absolute_upper':'56/100000',
        'QW_e_norm_upper':'19/1000', 'QW_v_norm_upper':'84/100000',
        'high_compression_lower':'49/100', 'target_margin_mu':'1/20000'},
      'schema':'IV053-original-even-two-low-profiles-and-entire-infinite-high-source-rational-v1',
      'status':'exact Fraction PASS, continuum mathematical proof, NOT Lean certified',
      'source_sha256_dependencies':PREVIOUS,
      'mixed_overlap_sigma_display': [f'{float(t):.12f}' for t in sigma],
      'genuine_mixed_gamma_D_over_sigma_display':[f'{float(Dlo):.12f}',f'{float(Dhi):.12f}'],
      'genuine_mixed_prime_P_over_sigma_display':[f'{float(Plo):.12f}',f'{float(Phi):.12f}'],
      'genuine_mixed_poles_over_sigma_display':[f'{float(Polelo):.12f}',f'{float(Polehi):.12f}'],
      'full_genuine_W_e_p_display':[f'{float(t):.12f}' for t in mixed],
      'original_W_parabola_display':[f'{float(pp_lo):.12f}',f'{float(pp_hi):.12f}'],
      'W_v_lower_display':f'{float(v_lo):.12f}',
      'W_e_v_upper_display':f'{float(ep_upper):.12f}',
      'high_compression_lower':str(c),
      'full_low_plus_high_coercivity_claim':str(mu),
      'Schur_normalized_lower_ee_display':f'{float(a):.12f}',
      'Schur_normalized_lower_pp_display':f'{float(d):.12f}',
      'Schur_absolute_mixed_upper_display':f'{float(b):.12f}',
      'Schur_strict_positive_determinant_floor_1e12':str(F((det.numerator*10**12)//det.denominator,10**12)),
      'Schur_strict_positive_determinant_display':f'{float(det):.12f}',
      'low_space':'span of normalized constant I indicator e and physical 100000-cell projection of normalized even parabola p',
      'full_support_space':'complex Schwartz tests with vector of all 100000 physical cell integrals in span of constant and parabolic cell-average patterns',
      'nonclaims':['any full fixed-window Weil positivity','global Weil positivity','RH','new Lean/olean acceptance','independent PI-CP operator equality']
    }

if __name__=='__main__':
    data=main()
    data['script_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    receipt=HERE/'IV053_two_low_profile_schur_receipt.json'
    receipt.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print('IV053 exact Fraction source mixed low Schur PASS (NONKERNEL)')
    print('original W(e,p) interval:',data['full_genuine_W_e_p_display'])
    print('Schur margin determinant:',data['Schur_strict_positive_determinant_display'])
    print('2-low + infinite-dimensional high: W>1/20000 mass, analytic only')
    print('checker SHA:',data['script_sha256'])
