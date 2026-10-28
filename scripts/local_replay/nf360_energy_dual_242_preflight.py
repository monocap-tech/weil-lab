#!/usr/bin/env python3
"""Read-only exact-rational algebra: J242 energy-dual Schur acceptance retyping.

Inputs are prior locally retained reports. Verifies their literal exact fractions
and PR #355 archive SHA. Does not assert a native CI certificate, calculate the
242x242 finite inverse matrices, or establish Weil positivity.
"""
from fractions import Fraction as F
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
import json, zipfile, hashlib

root=Path(str(CUSTODY_ROOT))
report=json.loads((root/'nf356_v2_aggregate_report.json').read_text())
eps=F(report['negative_leakage_upper_exact'])
mu=F(report['mu_new_lower_exact'])
assert F(0)<eps<F(1,10000)
assert mu>F(499,50000) # 0.00998
assert mu<F(1,100)
assert F(0)<eps/mu<F(21,12500) # 0.00168
best_theta=mu/(mu+eps)
accept_theta=F(99832,100000)
assert F(0)<accept_theta<best_theta<F(1)
assert F(1)-(F(1)+eps/mu)*accept_theta>0
archive=root/'pr355-exterior.zip'
assert hashlib.sha256(archive.read_bytes()).hexdigest()==report['archives_sha256']['pr355-exterior.zip']
with zipfile.ZipFile(archive) as z:
    o=json.loads(z.read('original_BS_pruned_rank_bound.json'))
    assert o['retained_physical_rank_upper']==242
    assert o['zero_constraint_cluster_count']==40
    assert o['complete_107_clusters_paid']

# A small exact negative control: source P, one sampled E and an unprobed V.
# W = [[1,c,t],[c,mu0,0],[t,0,mu0]].
# K = diag(2,0,0) >= 0, A = W+K. The E coupling & all diagonal form data
# are identical for both t values. A >= kappa_star, Q K Q=0,
# and C_Q=mu0 I. W's sign differs solely by unprobed coupling.
mu0=F(1,100); c=F(1,250); kappa=F(33621,10**9)

def positive_sylvester(matrix):
    # strictly SPD via exact unpivoted LDL leading principal minors
    d1=matrix[0][0]
    d2=matrix[1][1]-matrix[0][1]**2/d1
    s12=matrix[2][1]-matrix[0][2]*matrix[0][1]/d1
    d3=matrix[2][2]-matrix[0][2]**2/d1-s12*s12/d2
    return min(d1,d2,d3)>0, (d1,d2,d3)

cases={}
for tag,t in [('positive',F(1,50)),('negative',F(1,8))]:
    w=[[F(1),c,t],[c,mu0,F(0)],[t,F(0),mu0]]
    a=[[w[i][j]+(F(2) if i==j==0 else F(0)) for j in range(3)] for i in range(3)]
    am=[[a[i][j]-(kappa if i==j else F(0)) for j in range(3)] for i in range(3)]
    ok, pivots=positive_sylvester(am)
    assert ok
    g_e=c*c/mu0
    d=t*t/mu0
    schur=F(1)-g_e-d
    assert (schur>0)==(tag=='positive')
    cases[tag]={'unprobed_mixed_coupling':str(t),
                'sampled_four_probe_like_schur':str(g_e),
                'unprobed_remainder':str(d),
                'full_schur_sign': 'positive' if schur>0 else 'negative',
                'full_schur_exact':str(schur),
                'Astar_minus_kappa_positive':ok,
                'min_exact_LDL_pivot_Astar_minus_kappa':str(min(pivots))}

# Sharpness of the relative ε/μ factor from only PSD K and scalar floors:
# E_A=span e1, F=span e2 and Astar diagonal imply exact Astar-energy
# orthogonality. K is a rank-one PSD matrix and QKQ=eps0, W_F=mu0.
eps0=F(1,10000)
kcross=F(1,100)
assert kcross**2==eps0
a_sharp=[[F(2),F(0)],[F(0),mu0+eps0]]
k_sharp=[[F(1),kcross],[kcross,eps0]]
assert k_sharp[0][0]*k_sharp[1][1]-k_sharp[0][1]**2==0
w_sharp=[[a_sharp[i][j]-k_sharp[i][j] for j in range(2)] for i in range(2)]
assert w_sharp[1][1]==mu0
assert kcross**2/mu0==(eps0/mu0)*k_sharp[0][0]

out={'status':'EXACT_ALGEBRAIC_RETYPING_AND_INFORMATION_BOUNDARY_ONLY',
    'source_rank':242, 'positive_energy_dual_exceptional_space':'Astar^-1(J242)',
    'original_physical_complement':'J242^perp',
    'inherited_epsilon_exact':str(eps),'locally_replayed_mu_exact':str(mu),
    'relative_infinite_Schur_cost_upper_exact':str(eps/mu),
    'relative_infinite_Schur_cost_upper_decimal':float(eps/mu),
    'best_conditional_finite_theta_exact':str(best_theta),
    'best_conditional_finite_theta_decimal':float(best_theta),
    'convenient_exact_sufficient_finite_theta':str(accept_theta),
    'finite_test':'N242 <= theta G242 on every h in selected original J242',
    'finite_test_evaluated':False,
    'abstract_no_go_for_existing_physical_probes':cases,
    'relative_Schur_factor_sharp_negative_control':{
       'Kstar_rank_one_PSD':True,'epsilon':str(eps0),'mu':str(mu0),
       'actual_infinite_Schur_penalty':str(kcross**2/mu0),
       'epsilon_over_mu_times_finite_K_energy':str((eps0/mu0)*k_sharp[0][0]),
       'saturates_bound':True},
    'caution':'counterexample is abstract; it is not an original signed Weil negative mode',
    'native_arb_CI_for_new_mu':False,
    'original_operator_domain_verified':False,
    'W_ODD_NEG':'OPEN', 'RH':'OPEN'}
(root/'nf360_energy_dual_242_report.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['inherited_epsilon_exact','locally_replayed_mu_exact','relative_infinite_Schur_cost_upper_exact','best_conditional_finite_theta_exact']},indent=2))
