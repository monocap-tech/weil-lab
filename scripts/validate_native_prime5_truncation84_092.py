"""Exact highest-degree diagonal truncation diagnostic for the width repair."""
import json
from math import factorial
from certify_native_legendre_small_window import F,legendre
from certify_native_exact_polynomial import correlation

def certificate():
    a=F(23,25);L=4*a;n=83
    p=legendre(n)[n]
    c=[a*x*2**k for k,x in enumerate(correlation(p,p))]
    delta=2*a/F(2*n+1);assert c[0]==delta
    mass=sum(map(abs,c));abound=F(3,4)*L*delta+sum(map(abs,c[1:]))
    exponential_error=40*L**261/F(factorial(261))*(delta+mass/F(4**261))
    def width(K):
        kernel_error=4*(L/6)**(2*K+2)/(1-(L/6)**2)
        return 2*(F(23,5)*exponential_error+abound*kernel_error)*F(2*n+1)/(2*a)
    old=width(230);new=width(240)
    assert old>F(1,10**35) and new<F(1,10**38)
    return dict(aperture='23/25',physical_degree=n,exponential_order=260,
        original_bernoulli_pairs=230,repaired_bernoulli_pairs=240,
        original_diagonal_truncation_width=str(old),original_width_display=float(old),
        repaired_diagonal_truncation_width=str(new),repaired_width_display=float(new),
        old_truncation_alone_exceeds_required_total_width=True,
        repaired_diagonal_truncation_below='1/10^38',
        complete_native_entry_widths_pending=True,whole_domain_positivity=False,
        f4_entry_closed=False,lean_formalized=False)

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
