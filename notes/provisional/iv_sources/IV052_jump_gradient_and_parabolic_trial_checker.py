#!/usr/bin/env python3
"""IV052 source-matched NONKERNEL exact rational checks.

Proof obligations beyond this script: original source Gamma Fourier atom,
closed logarithmic form, full-space Hilbert block Schur, and smooth density.
All comparisons used for certification are made with Fraction/integer arithmetic.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
from math import factorial, isqrt
import json

HERE = Path(__file__).resolve().parent
DEPS = {
    'IV045_fixed_window_parity_trial_checker.py':'54d49affe407f3838015963b485975b885a5cde0c1c507dc318f9b33c64f86ac',
    'IV047_infinite_dim_high_mode_checker.py':'d64d8b08529e529a1be86923d25d2a76ce81aa42889eab97257c5f6aa0e083a5',
    'IV050_dense_mode_schur_checker.py':'e1fc5cfdd8b17f40f7d028f3dd187e1e2e679e7e13ffc0de84cf1f6d45c4d889',
    'IV051_equal_mean_schur_checker.py':'27559e26c5d6d7217664c216b04f42feb6df05eeb411e080cfac837f56e6443a',
}
A=F(11,10)       # half original physical window
L=2*A           # full length
MESHES=(100000,132000)


def log_bracket(x: F, n: int=120):
    assert x>0
    if x==1: return F(0),F(0)
    if x<1:
        l,h=log_bracket(1/x,n)
        return -h,-l
    y=(x-1)/(x+1)
    s=sum((2*y**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    e=2*y**(2*n+1)/(F(2*n+1)*(1-y*y))
    return s,s+e


def arctan_reciprocal(q: int,n:int):
    partial=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(n)),F(0))
    tail=F((-1)**n,(2*n+1)*q**(2*n+1))
    return min(partial,partial+tail),max(partial,partial+tail)


def pi_bracket():
    a,b=arctan_reciprocal(5,24)
    c,d=arctan_reciprocal(239,8)
    return 16*a-4*d,16*b-4*c


def exp_pos_bracket(x:F,n:int=115):
    assert x>=0
    s=term=F(1)
    for j in range(1,n+1):
        term=term*x/j
        s+=term
    nxt=term*x/(n+1)
    ratio=x/F(n+2)
    assert ratio<1,(x,n)
    return s,s+nxt/(1-ratio)


def exp_neg_bracket(x:F,n:int=115):
    lo,hi=exp_pos_bracket(x,n)
    return 1/hi,1/lo


def sqrt_bracket(n:int,scale:int=10**20):
    v=isqrt(n*scale*scale)
    return F(v,scale),F(v+1,scale)


def mult_iv(a,b):
    products=[x*y for x in a for y in b]
    return min(products),max(products)


def gamma_base_interval():
    pi_lo,pi_hi=pi_bracket()
    l2=log_bracket(F(2),120)
    l5=log_bracket(F(5),150)
    lp=(log_bracket(pi_lo,180)[0],log_bracket(pi_hi,180)[1])
    H400=sum((F(1,j) for j in range(1,401)),F(0))
    l400=(4*l2[0]+2*l5[0],4*l2[1]+2*l5[1])
    euler=(H400-l400[1]-F(1,800), H400-l400[0]-F(1,802))
    assert euler[0]>F(577,1000) and euler[1]<F(578,1000)
    base=(-3*l2[1]-euler[1]-pi_hi/2-lp[1],
          -3*l2[0]-euler[0]-pi_lo/2-lp[0])
    assert base[0]>-F(54,10) and base[1]<-F(53,10)
    return base,(pi_lo,pi_hi)


def gamma_parabola_D(N:int=350):
    # Parabolic unit-L2 physical test p(x)=1-(x/A)^2 for |x|<A.
    # Original Gamma difference atoms are D_j=2 integral_0^L exp(-b_j u)(1-C(u)) du+exp(-b_j L)/(j+1/4).
    # Here C(u)=1-c2*u²+|c3|*u³-c5*u^5, 0<=u<=L;
    # c2=5/(4A²), c3=-5/(8A³), c5=1/(32A⁵).
    coefs={2:F(5)/(4*A*A),3:-F(5)/(8*A**3),5:F(1)/(32*A**5)}
    def atom_rational(n):
        alpha=F(n)+F(1,4)
        beta=2*alpha
        inf=2*sum((c*F(factorial(m),1)/beta**(m+1) for m,c in coefs.items()),F(0))
        correction=1/alpha
        for m,c in coefs.items():
            r=sum((F(factorial(m),factorial(k))*L**k/beta**(m+1-k)
                   for k in range(m+1)),F(0))
            correction-=2*c*r
        return inf,correction

    # Sum all rational infinite-upper-limit terms exactly; exponential corrections
    # are relevant only for first 13 atoms and have a certified geometrical tail.
    approx=F(0)
    corr_lo=corr_hi=F(0)
    for n in range(N):
        t,c=atom_rational(n)
        approx+=t
        if n<13:
            elo,ehi=exp_neg_bracket(2*(F(n)+F(1,4))*L,115)
            a,b=(c*elo,c*ehi) if c>=0 else (c*ehi,c*elo)
            corr_lo+=a;corr_hi+=b

    # For n>=13, |correction_n|<1 follows from positive component
    # bounds evaluated at beta>=beta_13 and monotonicity of each term.
    n0=13
    aa=F(n0)+F(1,4);bb=2*aa
    abs_bound=1/aa+2*sum((abs(c)*sum((F(factorial(m),factorial(k))*L**k/bb**(m+1-k)
                        for k in range(m+1)),F(0)) for m,c in coefs.items()),F(0))
    assert abs_bound<1
    exp13=exp_neg_bracket(2*aa*L,115)[1]
    assert exp_pos_bracket(2*L,20)[0]>2
    rem=2*exp13 # geometric ratio exp(-2L)<1/2
    corr_lo-=rem; corr_hi+=rem

    # Every source Gamma atom is nonnegative. For the positive n>=N tail,
    # drop the negative cubic integral, use full gamma integrals on the remaining
    # quadratic and quintic components, and bound the remaining exterior term.
    d=F(N)-F(3,4)
    c2,c5=coefs[2],coefs[5]
    upper_tail=c2/(4*d*d)+3*c5/(4*d**5)+rem
    lo=approx+corr_lo
    hi=approx+corr_hi+upper_tail
    assert 0<lo<hi and hi-lo<F(1,100000)
    return lo,hi,{'terms':N,'tail_upper':str(upper_tail),'early_exponential_correction_terms':13,
                  'sum_rational_to_infty':f'{float(approx):.12f}',
                  'tail_correction_bound':str(rem)}


def prime_parabola():
    c2=F(5)/(4*A**2)
    c3=F(5)/(8*A**3)
    c5=F(1)/(32*A**5)
    vals={2:log_bracket(F(2),120),3:log_bracket(F(3),150),
          5:log_bracket(F(5),160),7:log_bracket(F(7),185)}
    choices=((2,2,1),(3,3,1),(4,2,2),(5,5,1),(7,7,1),(8,2,3),(9,3,2))
    outlo=outhi=F(0)
    details=[]
    for n,p,exp in choices:
        rlo,rhi=vals[p][0]*exp,vals[p][1]*exp
        assert F(0)<rlo<rhi<L
        C_lo=1-c2*rhi**2+c3*rlo**3-c5*rhi**5
        C_hi=1-c2*rlo**2+c3*rhi**3-c5*rlo**5
        assert F(0)<C_lo<=C_hi<=1
        sqlo,sqhi=sqrt_bracket(n)
        kp=(vals[p][0]/sqhi, vals[p][1]/sqlo)
        outlo+=2*kp[0]*C_lo
        outhi+=2*kp[1]*C_hi
        details.append({'n':n,'shift_approx':f'{float(rlo):.9f}',
                        'autocorrelation_approx':f'{float(C_lo):.9f}'})
    return outlo,outhi,details


def pole_parabola():
    pos=exp_pos_bracket(A/2,110)
    neg=(1/pos[1],1/pos[0])
    ch=((pos[0]+neg[0])/2,(pos[1]+neg[1])/2)
    sh=((pos[0]-neg[1])/2,(pos[1]-neg[0])/2)
    lower=16*ch[0]/A-32*sh[1]/A**2
    upper=16*ch[1]/A-32*sh[0]/A**2
    assert lower>0
    norm=16*A/15
    return 2*lower**2/norm,2*upper**2/norm


def parabolic_cell_mean_schur_certificate():
    """Pure rational inequalities in the classical Hilbert-space proof.

    Profile p is L2 normalized. The Gamma source bound is obtained by
    g_a(t)<=|t|/(4*a*a) and sum_{n>=0}1/(n+1/4)^2<18;
    p has ||p'||/||p||=sqrt(5/(2*A*A))<3/2.
    """
    M=100000
    w=L/M
    derivative_ratio_sq=F(5)/(2*A*A)
    assert derivative_ratio_sq<F(9,4)
    # Both boundary jumps of the cell-average projection are <=w^(3/2)/(A||p0||).
    # Internal jumps have square sum <=w^2 ||p'||^2 by Jensen/translation.
    jump_square_ratio=derivative_ratio_sq+F(15)*w/(8*A**3)
    assert jump_square_ratio<F(9,4)
    # Source Gamma operator L2 bound: |gamma(t)| <= 28/5 +(9/2)|t|.
    # Add exact original symmetric prime norm <71/10 and two-pole norm <5.
    # Thus ||Wop p|| <= (28/5+9/2*(3/2)+71/10+5)||p||.
    source_operator_bound=F(28,5)+F(9,2)*F(3,2)+F(71,10)+F(5)
    assert source_operator_bound==F(489,20)
    # q=p-Pi p is in Q; ||q|| <=(w/pi)||p'||<w/2, W[q]>0.
    low_test_lower=F(6,10000)
    low_proj_lower=low_test_lower-source_operator_bound*w
    assert low_proj_lower==F(621,10000000)>0
    # IV052 original full signed dense-cell derivative gate.
    mixed_bound=(25*F(3,2)+F(2,3))*w
    assert mixed_bound==F(229,6)*w
    high=F(49,100)
    mu=F(1,20000)
    schur_upper=mixed_bound*mixed_bound/(high-mu)
    assert high>mu and low_proj_lower-mu>schur_upper
    return {
       'source_parabola_W_lower':'6/10000',
       'derivative_squared_norm_ratio':str(derivative_ratio_sq),
       'discrete_gradient_squared_over_w_squared_upper':str(jump_square_ratio),
       'source_full_W_operator_on_parabola_norm_lt':str(source_operator_bound),
       'zero_mean_projection_error_norm_lt':'w/2',
       'projected_parabola_W_lower':str(low_proj_lower),
       'projected_parabola_full_mixed_norm_lt':str(mixed_bound),
       'projected_parabola_schur_cost_lt':str(schur_upper),
       'projected_parabola_schur_cost_float_display':f'{float(schur_upper):.12f}',
       'new_infinite_dimensional_class_margin':'1/20000',
       'positive_margin_arithmetic':str(low_proj_lower-mu-schur_upper),
       'class_def':'C_c^infty(I) complex f with all cell integrals proportional to those of p(x)=normalize(1-(x/(11/10))²)',
       'nonclaim':'not all affine combinations of the constant and parabolic low directions',
    }


def finite_complex_gradient_check():
    # Identity a_j = sum_{r<=j} Delta_r, with exact zero extension,
    # tested against a discrete even convolution/difference kernel.
    coefs=((F(1),F(2)),(F(-2),F(1)),(F(0),F(3)),(F(5),F(-1)),(F(2),F(0)),(F(0),F(0)))
    zero=(F(0),F(0)); M=len(coefs)
    steps=[coefs[0]]+[(coefs[j][0]-coefs[j-1][0],coefs[j][1]-coefs[j-1][1])
                     for j in range(1,M)]+[(-coefs[-1][0],-coefs[-1][1])]
    def plus(x,y):return (x[0]+y[0],x[1]+y[1])
    def mul(t,x):return (t*x[0],t*x[1])
    def sub(x,y):return (x[0]-y[0],x[1]-y[1])
    assert sum((x[0] for x in steps),F(0))==0
    assert sum((x[1] for x in steps),F(0))==0
    for i in range(M):
        direct=zero
        via=zero
        for j in range(M):
            if j==i:continue
            K=F(1,2**abs(i-j)) # rational even toy K (algebra sanity, not actual Gamma kernel)
            direct=plus(direct,mul(K,sub(coefs[i],coefs[j])))
        for boundary,delta in enumerate(steps):
            response=F(0)
            for j in range(M):
                if j==i:continue
                K=F(1,2**abs(i-j))
                response+=K*(int(i>=boundary)-int(j>=boundary))
            via=plus(via,mul(response,delta))
        assert direct==via,(i,direct,via)
    return True


def check():
    hashes={}
    for name,h in DEPS.items():
        path=HERE/name
        assert path.exists(),name
        current=sha256(path.read_bytes()).hexdigest()
        assert current==h,(name,current,h)
        hashes[name]=h
    base,pi=gamma_base_interval()
    Dlo,Dhi,Dinfo=gamma_parabola_D()
    Plo,Phi,pdetail=prime_parabola()
    Hlo,Hhi=pole_parabola()
    wholelo=base[0]+Dlo-Phi+Hlo
    wholehi=base[1]+Dhi-Plo+Hhi
    assert F(0)<wholelo<wholehi<F(1,1000), (float(wholelo),float(wholehi))
    # New upper variational comparison better than IV046 (<0.0087).
    assert F(6,10000)<wholelo<wholehi<F(7,10000), (float(wholelo),float(wholehi))
    assert wholehi-wholelo<F(1,10000)

    # Exact harmonic and dyadic-proof constants for both original IV047 meshes.
    # Since exp(12)>132000 by 16-term positive rational Taylor,
    # H_M <=1+log M<13 for both M<=132000.
    assert sum((F(12**n,factorial(n)) for n in range(17)),F(0))>132000
    row=4+F(13)+2*L
    assert row==F(107,5)
    prime=F(71,20)
    assert row+prime==F(499,20)<25
    gradient_checks=[]
    for M in MESHES:
        w=L/M
        assert w<F(1,1000)
        R=4334
        band=(2*R*w)**2
        high_gamma=F(8091,1000)-(F(8091,1000)+F(28,5))*band
        high_source=high_gamma-F(71,10)-F(5,36)*w*w
        assert high_source>F(49,100), (M,float(high_source))
        # exact operator bound: ||Q W v|| <25||Delta a||+(2w/3)||v||
        # normalized first Dirichlet sine: ||Delta a|| <pi/(M+1)<22/[7(M+1)]
        assert pi[1]<F(22,7)
        bound=F(25)*F(22,7*(M+1))+F(2,3)*w
        cost=F(100,49)*bound*bound # c_M>49/100 at 100k; need check 132k c_M lower separately
        if M==100000:
            assert cost<F(1,700000)
        gradient_checks.append({'M':M,'w':str(w),'jump_norm_upper_on_sine':str(F(22,7*(M+1))),
                                'full_mixed_column_upper_display':f'{float(bound):.10f}',
                                'energy_relative_cost_display':f'{float(cost):.12f}',
                                'certified_high_Weil_lower_display':f'{float(high_source):.9f}',
                                'high_margin_gt_49_over_100':True})

    assert finite_complex_gradient_check()
    projected=parabolic_cell_mean_schur_certificate()
    return {
      'schema':'IV052-authentic-original-gamma-jump-gradient-and-parabolic-even-source-trial-v1',
      'standing':'exact Fraction preflight PASS; complete analytic source arguments, not Lean kernel',
      'physical_window':'(-11/10,11/10)',
      'source_dependencies':hashes,
      'gamma0_interval_display':[f'{float(x):.12f}' for x in base],
      'D_parabola_interval_display':[f'{float(Dlo):.12f}',f'{float(Dhi):.12f}'],
      'P_parabola_interval_display':[f'{float(Plo):.12f}',f'{float(Phi):.12f}'],
      'pole_parabola_interval_display':[f'{float(Hlo):.12f}',f'{float(Hhi):.12f}'],
      'complete_original_signed_W_parabolic_unit_L2_interval_display':[f'{float(wholelo):.12f}',f'{float(wholehi):.12f}'],
      'strict_source_trial_enclosure':['6/10000','7/10000'],
      'D_atom_certificate':Dinfo,
      'parabolic_equal_profile_infinite_dimensional_schur':projected,
      'original_prime_seven_shift_checkpoints':pdetail,
      'original_Gamma_jump_boundary_law':'Gamma v=gamma0 v+sum_r Delta(a)_r sign(x-x_r) H(|x-x_r|)/sqrt(w)',
      'H_kernel_antiderivative':'H(s)=atanh(exp(-s/2))+atan(exp(-s/2))',
      'block_majorant_coefficients':'2 for touching boundary/output cells, 1/(2*d)+w otherwise',
      'rational_row_sum_bound':'107/5',
      'source_prime_gradient_bound':'71/20 times ||Delta a||',
      'source_pole_smooth_bound':'2*w/3 times ||a||',
      'new_full_original_mixed_bound':'||QWv|| < 25 ||Delta a|| +(2*w/3)||v|| for M=100000 and 132000',
      'sine_low_direction_shur_checks':gradient_checks,
      'finite_complex_jump_telescope_sanity':'PASS, rational discrete convolution (not original source inverse)',
      'nonclaims':['any new Lean acceptance','full fixed-window signed Weil positivity',
                   'positive Schur on first sine without a lower low diagonal','RH','PI/CP equivalence']
    }

if __name__=='__main__':
    data=check()
    data['script_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    p=HERE/'IV052_jump_gradient_and_parabolic_trial_receipt.json'
    p.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print('IV052 exact-rational source preflight PASS — NONKERNEL')
    print('Full original signed W on normalized parabola:',data['complete_original_signed_W_parabolic_unit_L2_interval_display'])
    print('General low-grid original mixed jump bound <25||Delta a||+(2w/3)||v||')
    print('NEW: whole signed Weil positive >1/20000 on parabolic-cell-mean class (analytical/nonkernel)')
    print('Sine-direction energy-relative costs:',[x['energy_relative_cost_display'] for x in data['sine_low_direction_shur_checks']])
    print('script SHA256',data['script_sha256'])
    print('receipt',p)
