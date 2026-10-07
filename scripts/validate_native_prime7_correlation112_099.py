"""Independent endpoint-Beta evaluation of the actual prime-7 correlations."""
import hashlib,json
from math import comb,factorial,lcm
from pathlib import Path
from certify_native_legendre_small_window import F,I,legendre,sqrt_rational
from certify_native_exact_logarithm import log_rational
from certify_native_exact_polynomial import correlation

def certificate():
    saved=I.grid;I.grid=10**400
    try:
        a=F(99,100);log7=log_rational(F(7),450);ell=log7/(2*a);width=I(1)-ell
        assert width.lo>0 and ell.lo>F(1,2)
        alpha=log7/sqrt_rational(F(7));polys=legendre(111)
        A=[[comb(n,k)*comb(n+k,k) for k in range(n+1)] for n in range(112)]
        common=factorial(223);fac=[factorial(k) for k in range(224)]
        pairs=sorted({(0,n) for n in range(112)}|{(n,n) for n in range(112)})
        checks=0;maximum_gap=F(0);constant=None
        for i,j in pairs:
            # Independent unit-coordinate integral over t in [0,1-ell].
            # Endpoint expansions use powers of w(1-u),wu; Beta moments are exact.
            coeff=[0]*(i+j+1)
            for k,x in enumerate(A[i]):
                for l,y in enumerate(A[j]):
                    r=k+l
                    assert common%fac[r+1]==0
                    coeff[r]+=(-1)**(r+j)*x*y*fac[k]*fac[l]*(common//fac[r+1])
            beta=I(0)
            for c in reversed(coeff):beta=beta*width+F(c,common)
            beta*=width
            direct=alpha*sqrt_rational(F((2*i+1)*(2*j+1)))*beta*(1+(-1)**(i+j))
            c=correlation(polys[i],polys[j]);value=I(0)
            for x in reversed(c):value=value*(2*ell)+x
            physical=alpha*sqrt_rational(F((2*i+1)*(2*j+1)))*value/2*(1+(-1)**(i+j))
            gap=max(F(0),direct.lo-physical.hi,physical.lo-direct.hi)
            assert gap==0;maximum_gap=max(maximum_gap,gap);checks+=1
            if (i+j)%2:assert direct.lo==direct.hi==physical.lo==physical.hi==0
            if (i,j)==(0,0):
                constant=direct
                assert direct.lo>F(6,10**5)  # omitting prime 7 changes the constant-mode entry
                closed=alpha*(I(2*a)-log7)/a
                assert max(closed.lo,direct.lo)<=min(closed.hi,direct.hi)
        assert checks==223
        return dict(aperture='99/100',independent_endpoint_beta_correlations_checked=checks,
            first_native_row_and_all_112_diagonals_checked=True,
            independent_log_series_terms=450,interval_grid_digits=400,
            all_prime7_normalization_and_reflection_checks_passed=True,
            constant_mode_prime7_interval=[str(constant.lo),str(constant.hi)],
            constant_mode_prime7_display=float(constant.lo),omitted_prime7_constant_control_rejected=True,
            maximum_interval_gap=str(maximum_gap),finite_sign_certified=False,
            whole_domain_positivity=False,f4_entry_closed=False,lean_formalized=False,
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    finally:I.grid=saved

if __name__=='__main__':print(json.dumps(certificate(),indent=2))

