#!/usr/bin/env python3
"""Weil-Lab NF361: read-only exact-rational transfer/no-go.

This is a finite arithmetic replay of the new analytic lemma, NOT a Lean
proof, new Arb enclosure, proof of positivity, or repository acceptance.

Analytic lemma (assumptions): H=E_A ⊕ F is Astar-form orthogonal;
K>=0, W=Astar-K, W|F>=mu I and K|F<=eps I.
Then K|F<=eps/(mu+eps)*Astar|F. If an n-dimensional physical
form-domain plane L has K>= (1-eta)*Astar on L, its energy projection
P_A(L) is an n-dimensional plane E' in E_A, with
K>= (mu/(mu+eps)-eta)*Astar on E'. Thus the nth generalized
K/Astar eigenvalue on E_A is >= mu/(mu+eps)-eta.
"""
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
from fractions import Fraction as Q
from hashlib import sha256
from zipfile import ZipFile
import json

ROOT=Path(str(CUSTODY_ROOT))
CASES={
    'pr348': (ROOT/'nf361-pr348-fourmode.zip',
              '735ab9b78b6df9b09590ba70a8e51049aa19e73ebb526f22c58797b455cc4968',
              'original_four_mode_critical_block.json',
              'a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922'),
    'pr350': (ROOT/'pr350-certificate.zip',
              '3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09',
              'original_BS_pruned_rank_bound.json',
              '9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'),
}
def open_pinned(which):
    path,archive_sha,file,json_sha=CASES[which]
    assert path.exists(),path
    assert sha256(path.read_bytes()).hexdigest()==archive_sha, f'archive hash mismatch: {path}'
    with ZipFile(path) as z: b=z.read(file)
    assert sha256(b).hexdigest()==json_sha, f'JSON hash mismatch: {file}'
    return json.loads(b)

critical=open_pinned('pr348')
selected=open_pinned('pr350')
report=json.loads((ROOT/'nf360_energy_dual_242_report.json').read_text())
assert critical['near_critical_dimension_lower']==4
assert critical['W_ODD_NEG']=='OPEN'
assert selected['retained_physical_rank_upper']==242
assert selected['zero_constraint_cluster_count']==40

sigma=Q(critical['signed_Gram_operator_absolute_upper'])
kappa=Q(critical['inherited_Astar_floor'])
glower=Q(critical['physical_Gram_lower'])
eta=Q(critical['fourth_BS_distance_from_one_upper'])
assert sigma/(kappa*glower)==eta
assert eta<Q(3,10**12)
assert Q(critical['fourth_BS_eigenvalue_lower'])==1-eta

eps=Q(selected['pruned_physical_complement_negative_upper'])
assert eps==Q(report['inherited_epsilon_exact'])
mu=Q(report['locally_replayed_mu_exact'])
assert mu>Q(499,50000) and mu<Q(1,100)
theta0=Q(12479,12500)
r=eps/(mu+eps)
theta_star=mu/(mu+eps)
forced_lower=theta_star-eta
strict_margin=forced_lower-theta0
assert strict_margin>0
# Uniform sufficient gate implies W(f)/Astar(f)>=delta.
delta=1-(theta0+r)
assert delta==theta_star-theta0
assert delta>eta
# Any exterior floor above this threshold contradicts the same fixed theta0.
mu_gate_infeasible_above = eps*(theta0+eta)/(1-theta0-eta)
assert mu>mu_gate_infeasible_above

# The retained *old* floor gives a certified-input-only analogue.
mu_old=Q(1,1000)-eps
assert mu_old>Q(0)
r_old=eps/(mu_old+eps)
theta_old=mu_old/(mu_old+eps)
assert theta_old==1-eps/Q(1,1000)
assert theta_old-eta>0

out={
    'status':'EXACT_VARIATIONAL_NO_GO_FOR_NF360_SCALAR_SUFFICIENT_GATE',
    'scope':'Conditional original closed-form/operator identification; new mu locally verified, not native-GitHub-accepted',
    'source_CI':'PR348 GitHub Actions run 40516665209; PR350 pinned archive',
    'pinned_archive_sha256':{k:v[1] for k,v in CASES.items()},
    'pinned_json_sha256':{k:v[3] for k,v in CASES.items()},
    'dimension_of_accepted_near_critical_plane':4,
    'finite_inverse_response_dimension_upper':242,
    'original_critical_eta_exact':str(eta),
    'selected_complete_Kminus_complement_leakage_eps_exact':str(eps),
    'new_local_exterior_floor_mu_exact':str(mu),
    'new_relative_exterior_K_budget_r_exact':str(r),
    'optimal_from_scalar_assumptions_theta_star_exact':str(theta_star),
    'fourth_generalized_eigenvalue_lower_exact':str(forced_lower),
    'tested_uniform_sufficient_theta0_exact':str(theta0),
    'contradiction_margin_fourth_eigenvalue_minus_theta0_exact':str(strict_margin),
    'hypothetical_uniform_positive_Astar_reserve_exact':str(delta),
    'exterior_floor_threshold_for_no_go_exact':str(mu_gate_infeasible_above),
    'values_for_readability':{k:format(float(v),'.17g') for k,v in
        {'eta':eta,'eps':eps,'mu_new':mu,'r_new':r,'theta_star':theta_star,
         'theta4_lower':forced_lower,'theta0':theta0,'gap':strict_margin,
         'hypothetical_W_over_Astar_reserve':delta,
         'mu_new_no_go_threshold':mu_gate_infeasible_above,'mu_old':mu_old,
         'theta_old':theta_old,'theta4_old_lower':theta_old-eta}.items()},
    'logical_conclusion':'N242 <= (12479/12500) G242 is impossible if the new floor and the accepted four-mode bounds hold in the same operator realization. No actual inverse matrix required.',
    'stronger_multiplicity_conclusion':'At least four generalized N242/G242 eigenvalues are >= theta_star - eta, by injection of the Astar-energy projection of the accepted 4-plane.',
    'independent_of_new_mu':'The general lower-bound theorem also holds with the inherited old floor mu_old=0.001-eps; its numerical lower bound is reported.',
    'not_proved':['global_W_odd_positivity','new_mu_GitHub_native_certificate','full_W_domain_transfer','actual_finite_inverse_response_matrix'],
    'W_ODD_NEG':'OPEN', 'RH':'OPEN'}
(ROOT/'nf361_critical_transfer_no_go.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'], 'hashes_match':True,'near_critical_dim':4,
  'theta0':out['values_for_readability']['theta0'],
  'theta4_lower':out['values_for_readability']['theta4_lower'],
  'minimum_contradiction_margin':out['values_for_readability']['gap'],
  'inherited_floor_theta4_lower':out['values_for_readability']['theta4_old_lower'],
  'odd':'OPEN'},indent=2))
