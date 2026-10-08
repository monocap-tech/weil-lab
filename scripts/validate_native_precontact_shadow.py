"""PS1 finite rational controls. No actual zeros, spectral solver, or Lean proof."""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import json

checks = 0
def check(p):
    global checks
    assert p
    checks += 1

def log_bounds(n, terms=100):
    z = F(n-1, n+1)
    lo = 2*sum((z**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    hi = lo + 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
    return lo, hi

# Conservative actual prime coefficient budget; finite scalar algebra only.
roots = {2:F(7,5), 3:F(17,10), 4:F(2), 5:F(11,5), 7:F(13,5)}
total = F(0)
for n, root in roots.items():
    check(root*root <= n)
    prime = 2 if n == 4 else n
    total += 2*log_bounds(prime)[1]/root
check(total < 6)
check(log_bounds(7)[1] < 2)
check(log_bounds(2)[0] > F(1,2))

# Pole constants on B=21/20. Bound exp(B)<3 by a rational Taylor tail.
B = F(21,20)
term = F(1)
partial = term
for k in range(1,21):
    term *= B/k
    partial += term
tail = term*(B/21)/(1-B/22)
check(partial+tail < 3)
# exp(-B)<1 gives cosh(B)<2; sinh(B)<exp(B)/2<2.
check(4*(2+2*B) < 20)

# Microscopic continuation without constructing 2**(10**36).
N = 10**36
delta = F(2,10**34)
budget = F(48,N)+F(121,N*N)
check(budget < delta/4)
check(delta-budget > 3*delta/4)
check(2**8 == 16**2)
for n in range(16,1025,2):
    check(2*n*n >= (n+2)**2)
    check(2**(n//2) >= n*n)
# A rational log10(2)>3/10 check: 2**10>10**3.
check(2**10 > 10**3)

# Generic crossing with compact positive physical mass; first r levels use mass 1.
for r in range(1,9):
    masses = [F(1)]*r + [F(1,j+2) for j in range(5)]
    for s in [F(1,2),F(1,10),F(1,1000),F(0),F(-1,1000)]:
        A = [s]*r + [F(1)]*5
        neg2 = [1-s]*r+[F(0)]*5
        physical = [q/m for q,m in zip(A,masses)]
        check(all(q == 1-n for q,n in zip(A,neg2)))
        check(sum(v<0 for v in physical) == (r if s<0 else 0))
        check(sum(v==0 for v in physical) == (r if s==0 else 0))
        check(min(physical[r:]) >= 2)
        check(max(neg2) == 1-s)
        if s>0:
            check(min(A) == s)
            check(max(neg2)<1)

# Exact quantitative gain/margin bounds in independent diagonal systems.
for p in [(F(2),F(3)),(F(1),F(4)),(F(3,2),F(5,2))]:
    for defects in [(F(1,10),F(1,3)),(F(1,1000),F(1,2))]:
        q = [p[i]**2*defects[i] for i in range(2)]
        d = min(q)
        c2,C2 = min(x*x for x in p),max(x*x for x in p)
        dg = min(defects)
        check(c2*dg<=d<=C2*dg)
        check(d/C2<=dg<=d/c2)

# Exact physical mass shift and resolvent sandwich in scalar channels.
for a,m in [(F(1,10),F(1,2)),(F(-1,10),F(1,3)),(F(2),F(1,5))]:
    beta = F(10)
    resolvent = m/(a+beta*m)
    check(resolvent == 1/(a/m+beta))
    check(a+beta*m>0)
    shifted = a-F(1,7)*m
    check(shifted != a-F(1,7))

# Actual-control source residual algebra; this is a synthetic numerical instance.
p2,n2,m,mu = F(4),F(1),F(2),F(3,2)
check(p2-n2 == mu*m)
check(n2/p2 < 1)
check((n2+mu*m)/p2 == 1)

with localcontext() as ctx:
    ctx.prec = 60
    b8 = Decimal(8).ln()/2
    arch_budget = 5*b8.ln()
    check(arch_budget > Decimal('0.19'))
    illustrative = {'prime8_threshold':str(b8),
                    'arch_budget_at_threshold':str(arch_budget),
                    'arch_budget_to_delta_ratio':str(arch_budget/Decimal('2e-34'))}

if __name__ == '__main__':
    print(json.dumps({'checks':checks,'passed':True,
        'scope':'finite rational algebra and scalar budget controls only',
        'budget_numerator':budget.numerator,'budget_denominator':budget.denominator,
        'radius_representation':'2^(-10^36); not instantiated',
        'illustrative_decimal_values_not_interval_certificates':illustrative,
        'actual_spectral_computation':False,'analytic_certification':False,
        'lean_certification':False},indent=2))
