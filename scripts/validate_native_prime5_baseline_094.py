"""Independent support, chain, pole and logarithmic complement arithmetic."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
from certify_native_legendre_small_window import I,atan,sqrt_rational
from certify_native_exact_logarithm import log_rational

def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();c=json.loads(raw)
    a=F(47,50);d=2*a;k=84;assert c['aperture']==str(a)
    old=I.grid;I.grid=10**100
    try:
        logs={n:log_rational(F(n),400) for n in (2,3,4,5,7,8,9,100)}
        assert logs[5].hi<d<logs[7].lo and logs[8].lo>d and logs[9].lo>d
        assert a<logs[3].lo and d<2*logs[3].lo and logs[2].hi<a and d<3*logs[2].lo
        overlap=d-logs[5].lo
        assert 0<overlap<logs[5].lo-logs[3].hi and overlap<2*logs[3].lo-logs[5].hi
        roots={n:sqrt_rational(F(n)) for n in (2,3,5)}
        A2=logs[2].hi/roots[2].lo;A4=logs[2].hi/2
        A3=logs[3].hi/roots[3].lo;A5=logs[5].hi/roots[5].lo
        norm24=F(c['joint_prime24_operator_upper']);norm35=F(c['joint_prime35_operator_upper'])
        # Characteristic equations for the three- and four-vertex fibers.
        assert norm24**2-A4*norm24-2*A2*A2>=0
        assert norm35**2-A5*norm35-A3*A3>0
        B=[[F(0),A3,F(0),F(0)],[A3,F(0),A5,F(0)],
           [F(0),A5,F(0),A3],[F(0),F(0),A3,F(0)]]
        checked=0
        for sign in (-1,1):
            m=[[norm35*int(i==j)+sign*B[i][j] for j in range(4)] for i in range(4)]
            for j in range(4):
                pivot=m[j][j];assert pivot>0;checked+=1
                for i in range(j+1,4):
                    for z in range(i,4):
                        m[i][z]-=m[i][j]*m[j][z]/pivot;m[z][i]=m[i][z]
        pole=16*a*(a/2)**(2*k)/factorial(k)**2
        assert pole==F(c['pole_absolute_upper']) and a/2<logs[2].lo
        pi=16*atan(F(1,5))-4*atan(F(1,239));assert pi.hi<F(22,7)
        gamma=sum((F(1,n) for n in range(1,101)),F(0))-logs[100].lo
        floor=-gamma-3*logs[2].hi-pi.hi/2-log_rational(pi.hi,400).hi
        assert floor>-F(27,5)
        cutoff=F(c['logarithmic_cutoff']);assert cutoff==F(19,2)
        # w=log(exp(1)+|xi|); w<=log|xi|+3/|xi| on the high region.
        assert log_rational(F(3),400).lo>1 and log_rational(cutoff+3,400).hi<3
        high=F(9,10)*log_rational(cutoff,400).lo-F(3,10)/cutoff-F(7,216)/cutoff**2-norm24-norm35
        assert high>=F(c['logarithmic_high_symbol_gap_lower'])>0
        y=2*a*F(22,7)*cutoff;ratio=y*y/F((2*k+1)*(2*k+3));assert 0<ratio<1
        rho=4*a*cutoff*y**(2*k)/prod(range(1,2*k+2,2))**2/(1-ratio)
        assert rho==F(c['logarithmic_low_frequency_mass_upper'])
        lower=F(1,10)-(F(27,5)+norm24+norm35+F(3,10))*rho-pole
        assert lower==F(c['logarithmic_unrounded_lower'])>F(c['logarithmic_lower'])==F(9,100)
        return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),byte_identical_repeat=True,
            aperture=str(a),actual_prime_support_geometry_verified=True,chain_psd_pivots_checked=checked,
            pole_and_global_floor_verified=True,independent_complete_logarithmic_mass_formula_verified=True,
            high_frequency_symbol_comparison_coefficient='9/10',logarithmic_lower='9/100',
            whole_domain_positivity=False,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=old

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
