"""Exact coefficient/remainder checks for NF65; analytic theorem is in the note.

No sampled inequality is substituted for the global Laplace proof. No new
original aperture sign or actual-divisor gain is computed here.
"""
from fractions import Fraction as F
from math import comb, factorial
import json


def bernoulli(n):
    b = [F(1)]
    for k in range(1, n + 1):
        b.append(-sum((F(comb(k + 1, j)) * b[j]
                       for j in range(k)), F(0)) / (k + 1))
    return b


def derivative_numerator(order, q, z):
    """(-1)^order d_q^order f_z(q), entirely rational for rational q,z."""
    degree = order + 1
    real_power = sum((F(comb(degree, 2*j)) * q**(degree-2*j)
                      * (-z)**j for j in range(degree//2 + 1)), F(0))
    return F(factorial(order)) * (q**(-degree)
                                     - real_power/(q*q+z)**degree)


def run():
    checks = 0
    def check(value):
        nonlocal checks
        assert value
        checks += 1

    b = bernoulli(34)
    for k, value in {0:F(1), 1:F(-1,2), 2:F(1,6), 4:F(-1,30),
                     6:F(1,42), 8:F(-1,30), 16:F(-3617,510),
                     34:F(2577687858367,6)}.items():
        check(b[k] == value)
    for k in range(1, 18):
        check((-1)**(k-1)*b[2*k] > 0)
    for k in range(3, 34, 2):
        check(b[k] == 0)

    # This FINITE geometric identity holds on the whole positive half-line,
    # including t far beyond a denominator's Taylor radius sqrt(beta).
    for m in [0, 1, 2, 8, 16]:
        for beta in [F(1), F(36), F(144)]:
            for t in [F(1,8), F(1), F(8), F(100), F(1000)]:
                partial = sum(((-1)**r*t**(2*r)/beta**(r+1)
                               for r in range(m)), F(0))
                residual = 1/(beta+t*t) - partial
                exact = (-1)**m*t**(2*m)/(beta**m*(beta+t*t))
                check(residual == exact)
                check(0 <= (-1)**m*residual <= t**(2*m)/beta**(m+1))

    # Rational multipliers instantiated as algebra checks; uniform positivity
    # and bound are proved via their nonnegative Laplace integrals, not samples.
    for q in [F(1,4), F(9,4), F(129,4)]:
        for z in [F(0), F(1,16), F(1), F(100), F(10000), F(10**12)]:
            check(derivative_numerator(0,q,z) == z/(q*(q*q+z)))
            check(derivative_numerator(1,q,z)
                  == z*(3*q*q+z)/(q*q*(q*q+z)**2))
            for order in [0,1,3,15,31,33]:
                value = derivative_numerator(order,q,z)
                check(0 <= value <= 2*factorial(order)/q**(order+1))
                if z == 0:
                    check(value == 0)

    q = F(129,4)
    rows = []
    for m in [8,10,12,14,16]:
        epsilon = abs(b[2*m+2]) / ((m+1)*q**(2*m+2))
        # Integration of the next global kernel bound gives EXACTLY this.
        integrated_bound = (abs(b[2*m+2])/factorial(2*m+2)
                            * 2*factorial(2*m+1)/q**(2*m+2))
        check(epsilon == integrated_bound)
        rows.append({'bernoulli_corrections':m,
                     'epsilon_numerator':str(epsilon.numerator),
                     'epsilon_denominator':str(epsilon.denominator)})
    epsilon = abs(b[34])/(17*q**34)
    budget = F(1,10**40)
    check(0 < epsilon < budget)
    check(F(4,10**32)-budget > F(3,10**32))
    check(F(2,10**34)-budget > F(1,10**34))
    # The NF64 odd witness needs a substantial tail; the repaired form is
    # positive by the WHOLE original anchor plus the proved uniform error.
    mass = F(31999998475473,32000000000000)
    check((F(4,10**32)-budget)*mass > 0)
    check((F(49,1000)+F(4,10**32)-budget)*mass > 0)
    # Keep every positive eigenlevel shift explicit; approximation control
    # cancels unchanged when the same mu*mass is subtracted from both forms.
    for mu in [F(0),F(1,100),F(3,2)]:
        for original in [F(-1),F(0),F(1),mu]:
            repaired = original-epsilon/2
            check((original-mu)-(repaired-mu) == original-repaired)
            check(0 <= original-repaired <= epsilon)
    check((budget/2)-epsilon >= 0)  # an original positive level needn't certify
    check(epsilon/2-epsilon < 0)   # its repaired value is still allowed negative
    return {'passed':True,'exact_checks':checks,'archimedean_head_terms':32,
            'bernoulli_corrections':16,'q':'129/4',
            'uniform_physical_mass_budget_strict_upper':'1/10^40',
            'epsilon_numerator':str(epsilon.numerator),
            'epsilon_denominator':str(epsilon.denominator),
            'candidate_budgets':rows,
            'anchor_aperture':'1',
            'repaired_anchor_physical_lower':'3/10^32',
            'repaired_anchor_logarithmic_lower':'1/10^34',
            'analytic_global_bound':'finite partial-fraction remainder and nonnegative Laplace weight; see note',
            'whole_repaired_anchor_positive':True,
            'larger_aperture_original_sign_certified':False,
            'new_original_aperture_certificate':False,
            'new_actual_divisor_gain_bound':False,'lean_certified':False}


if __name__ == '__main__':
    print(json.dumps(run(),indent=2))
