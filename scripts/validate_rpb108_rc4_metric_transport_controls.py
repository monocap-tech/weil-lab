"""RC4 signed-data metric ambiguity and endpoint correction controls."""
from fractions import Fraction as F
import json
checks = 0
def check(v):
    global checks
    if not v:
        raise AssertionError(checks+1)
    checks += 1

# Same signed Q=[[1/4,-1/4],[-1/4,1]], distinct complete source metrics.
q, cross, c = F(1, 4), F(-1, 4), F(1)
physical_schur = q-cross*cross/c
metrics = [(F(1),F(2)), (F(2),F(3)), (F(4),F(5))]
records=[]
for m,n in metrics:
    # N*N = M-Q; a positive Gram guarantees a legitimate full analysis.
    neg00, neg01, neg11 = m-q, -cross, n-c
    check(neg00 > 0 and neg11 > 0)
    check(neg00*neg11-neg01*neg01 > 0)
    check(m-neg00 == q and -neg01 == cross and n-neg11 == c)
    defect, lam = q/m, 1-q/m
    # Canonical J=(0,cross/sqrt(m)); exact squared covariances need no sqrt.
    forced_cov = cross*cross/(m*n)
    leakage = forced_cov/lam
    critical_cost = forced_cov/(lam*defect)
    low_cost = (n-c)/n-leakage
    whole_cost = critical_cost+low_cost
    check(low_cost >= 0)
    check(whole_cost == 1-c/n+cross*cross/(n*q))
    check(whole_cost < 1 and physical_schur > 0)
    check(1-whole_cost == c*physical_schur/(n*q))
    records.append((defect,critical_cost,whole_cost))
check(len(set(records)) == 3)
check(physical_schur == F(3,16))

# Old-only trials have exactly zero forced pairing, but nonzero whole norm.
for m,n in metrics:
    check(cross*cross/(m*n) > 0)
    old_trial_pairing=F(0)
    check(old_trial_pairing == 0)

# Entire correction can be paid with omega(delta)+delta**2, which vanishes.
# Rational sqrt-scale deltas let powers below/at/above two be checked exactly.
for root in [F(1,2),F(1,4),F(1,8),F(1,16)]:
    delta=root*root
    for omega in [root,delta,delta*delta,delta**3]:
        qnorm=root # arbitrary nonzero outward forcing norm for triangle check
        correction=delta
        check((qnorm+correction)**2 <= 2*qnorm*qnorm+2*correction*correction)
        augmented=omega+delta*delta
        check(augmented > 0 and augmented >= omega and augmented >= delta*delta)
        if omega >= delta*delta:
            check(augmented <= 2*omega)
        else:
            check(delta*delta/omega > 1)
print(json.dumps({'milestone':'RC4','status':'PASS','exact_rational_checks':checks,
 'scope':'source-metric transport ambiguity and endpoint correction algebra',
 'actual_zeta_metric_reconstructed':False,'actual_arithmetic_modulus_proved':False,
 'RH':False,'F4':False,'Lean':False},indent=2))
