"""Propagate constant-enclosure widths through all shifted Legendre coefficients."""
import json
from math import comb,isqrt
from certify_native_legendre_small_window import F,I,atan,bernoulli
from certify_native_exact_logarithm import log_rational

def certificate():
    old=I.grid;I.grid=10**400
    try:
        norms=[F(1),F(3)]
        for n in range(1,111):norms.append((3*(2*n+1)*norms[-1]-n*norms[-2])/(n+1))
        assert all(x==sum(comb(n,k)*comb(n+k,k) for k in range(n+1)) for n,x in enumerate(norms))
        amplification=sum((F(2*n+1)*x*x for n,x in enumerate(norms)),F(0))
        def root_upper(x):
            grid=10**160;r=isqrt((x*grid*grid).__floor__())
            return F(r+1,grid)
        out={}
        for terms in (80,160):
            pi=16*atan(F(1,5),terms)-4*atan(F(1,239),terms)
            logpi=I(log_rational(pi.lo,220).lo,log_rational(pi.hi,220).hi)
            radius=(logpi.hi-logpi.lo)/2
            allowance=root_upper(radius*radius*amplification)
            out['pi'+str(terms)]=dict(logarithm_radius=str(radius),propagated_map_allowance=str(allowance),display=float(allowance))
        B=bernoulli(114)
        for order in (50,56):
            error=abs(B[2*order+2])/F((2*order+2)*100**(2*order+2))
            allowance=root_upper(error*error*amplification)
            out['gamma'+str(order)]=dict(remainder=str(error),propagated_map_allowance=str(allowance),display=float(allowance))
        assert F(out['pi80']['propagated_map_allowance'])>F(7,10**30)
        assert F(out['pi160']['propagated_map_allowance'])<F(1,10**120)
        assert F(out['gamma50']['propagated_map_allowance'])<F(6,10**41)
        assert F(out['gamma56']['propagated_map_allowance'])<F(4,10**50)
        return dict(aperture='1',source_columns=112,
            independent_recurrence_and_binomial_l1_norm_checks=112,
            squared_physical_amplification=str(amplification),constant_budgets=out,
            inherited_pi_enclosure_budget_rejected=True,
            repaired_constants_below_source_truncation_budget=True,
            actual_constant_error_lower_claimed=False,full_source_certified=False,
            whole_domain_positivity=False,whole_domain_frontier='399/400',f4_entry_closed=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))

