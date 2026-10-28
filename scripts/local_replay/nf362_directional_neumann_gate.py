#!/usr/bin/env python3
"""Read-only exact Fraction check: matched positive-energy Neumann Schur remainder.

This checks scalar implications of independently established operator inequalities;
no actual A_F inverse-action moments are evaluated.
"""
from fractions import Fraction as F
import json, hashlib, zipfile
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
from decimal import Decimal, localcontext

BASE=Path(str(CUSTODY_ROOT))
INPUT=json.loads((BASE/'nf361_critical_transfer_no_go.json').read_text())
def f(s): return F(s)
for p, expected in [('nf361-pr348-fourmode.zip',INPUT['pinned_archive_sha256']['pr348']),('pr350-certificate.zip',INPUT['pinned_archive_sha256']['pr350'])]:
    assert hashlib.sha256((BASE/p).read_bytes()).hexdigest()==expected, p
for path,member,expected in [('nf361-pr348-fourmode.zip','original_four_mode_critical_block.json',INPUT['pinned_json_sha256']['pr348']),('pr350-certificate.zip','original_BS_pruned_rank_bound.json',INPUT['pinned_json_sha256']['pr350'])]:
    with zipfile.ZipFile(BASE/path) as z:
        b=z.read(member)
        assert hashlib.sha256(b).hexdigest()==expected
        d=json.loads(b)
        if member.startswith('original_BS_pruned'):
            assert f(d['pruned_physical_complement_negative_upper'])==f(INPUT['selected_complete_Kminus_complement_leakage_eps_exact'])
        else:
            assert f(d['fourth_BS_distance_from_one_upper'])==f(INPUT['original_critical_eta_exact'])

eps=f(INPUT['selected_complete_Kminus_complement_leakage_eps_exact'])
mu=f(INPUT['new_local_exterior_floor_mu_exact'])
eta=f(INPUT['original_critical_eta_exact'])
assert eps>0 and mu>0 and eta>0
r=eps/(mu+eps)
assert r==f(INPUT['new_relative_exterior_K_budget_r_exact'])
mu_old=F(1,1000)-eps
r_old=eps/(mu_old+eps)
assert r_old==eps/F(1,1000)

def show(x, digits=25):
    with localcontext() as ctx:
        ctx.prec=digits+8
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def rows(rr, nn=8):
    return [{'highest_power_included':j,
             'number_of_terms':j+1,
             'remainder_relative_to_D0_exact':str(rr**(j+1)/(1-rr)),
             'remainder_relative_to_Kee_exact':str(rr**(j+2)/(1-rr)),
             'remainder_relative_to_Kee_approx':show(rr**(j+2)/(1-rr)),
             'below_fourmode_eta':rr**(j+2)/(1-rr)<eta,
            } for j in range(nn)]

new=rows(r); old=rows(r_old)
minnew=next(i for i,x in enumerate(new) if x['below_fourmode_eta'])
minold=next(i for i,x in enumerate(old) if x['below_fourmode_eta'])
assert minnew==3, minnew
assert minold>=minnew
# Four-mode upper signed form: k(f)/a(f) <= 1+eta. Let f=e+v
# be A-energy orthogonal. Young with t=1/20 gives
# k(e)/a(f) <= (21/20)(1+eta)+21*r < 11/10.
young_upper=F(21,20)*(1+eta)+21*r
assert young_upper<F(11,10)
critical_tail_over_a=F(11,10)*r**5/(1-r)
assert critical_tail_over_a < eta/F(200)
old_young_upper=F(6,5)*(1+eta)+6*r_old
assert old_young_upper<F(131,100)
old_critical_tail_over_a=F(131,100)*r_old**(minold+2)/(1-r_old)
assert old_critical_tail_over_a < eta/F(5)
# 2x2 rank-one PSD sharpness control: K=[[1,t],[t,t^2]], H=1, epsilon=t^2, mu=1-t^2.
t=F(1,100); tt=t*t
r_test=tt
# x=g=t, D0=t^2=r, D_full=r/(1-r), tail after j=3: r^(j+2)/(1-r)
assert r_test/(1-r_test)-sum((r_test**(j+1) for j in range(4)),F(0))==r_test**5/(1-r_test)
assert r_test<1
# Paired moment identity: u0=H^-1g=t, u1=H^-1 L u0=t^3.
# M0=a(u0,u0)=t^2, M1=k(u0,u0)=t^4,
# M2=a(u1,u1)=t^6, M3=k(u1,u1)=t^8.
u0=t; u1=tt*u0
assert u0*u0 + tt*u0*u0 + u1*u1 + tt*u1*u1 == sum((r_test**(j+1) for j in range(4)),F(0))
out={
  'status':'EXACT_RATIONAL_FINITE_ORDER_DIRECTIONAL_SCHUR_REMAINDER_GATE',
  'operator_scope':'conditional original closed form; unchanged physical J242; no actual inverse moments computed',
  'inputs':['GitHub certified PR348 native four-mode near-null plane','GitHub certified PR350 J242 Kminus leakage','NF356 locally replayed conditional stronger floor'],
  'source_artifacts_sha256_verified':True,
  'eps_exact':str(eps), 'mu_new_local_exact':str(mu), 'eta_4mode_exact':str(eta),
  'r_new_exact':str(r), 'r_new_approx':show(r),
  'r_old_exact':str(r_old), 'r_old_approx':show(r_old),
  'truncation_table_new':new,
  'truncation_table_old':old,
  'minimal_term_count_new_for_tail_below_eta':minnew+1,
  'minimal_term_count_old_for_tail_below_eta':minold+1,
  'critical_4mode_eta_approx':show(eta),
  'four_term_remainder_relative_to_Kee_approx':new[3]['remainder_relative_to_Kee_approx'],
  'four_term_error_over_eta_approx':show((r**5/(1-r))/eta),
  'near_critical_plane_Young_upper_for_Kee_over_Aff_exact':str(young_upper),
  'near_critical_plane_Young_upper_for_Kee_over_Aff_approx':show(young_upper),
  'near_critical_plane_clean_Kee_over_Aff_upper':'11/10',
  'four_term_tail_over_near_critical_Aff_upper_approx':show(critical_tail_over_a),
  'four_term_tail_over_eta_upper_approx':show(critical_tail_over_a/eta),
  'old_six_term_near_critical_Young_Kee_over_Aff_upper':'131/100',
  'old_six_term_tail_over_near_critical_Aff_upper_approx':show(old_critical_tail_over_a),
  'old_six_term_tail_over_eta_upper_approx':show(old_critical_tail_over_a/eta),
  'positive_solve_count_for_four_term_gate':2,
  'positive_solve_count_for_six_term_gate':3,
  'paired_moment_recurrence':'u0=H_F^-1 g, u_{j+1}=H_F^-1 K_F u_j; M_2j=a_F(u_j,u_j), M_(2j+1)=k_F(u_j,u_j)',
  'rank_one_exact_sharpness_control':{'t':'1/100','r':'1/10000','K':'[[1,1/100],[1/100,1/10000]]','H_F':'1','signed_C_F':'9999/10000','j3_tail_exact':str(r_test**5/(1-r_test)),'attained':True},
  'finite_gate':'G-N-sum_{j=0}^3 M_j-(r^5/(1-r)) N >= 0 on original finite selected J242',
  'Mj':'g^* H_F^{-1/2}(H_F^{-1/2} K_F H_F^{-1/2})^j H_F^{-1/2}g, g=Q K Astar^{-1}h',
  'main_remaining':'actual directional positive resolvent moments M0..M3, exact G,N and matrix inequality; stronger floor CI; physical/source form domain review',
  'disclaimer':'The fourth BS near-null criterion only calibrates the truncation error scale. It does not bound the uncomputed directional moments or certify Schur positivity.',
  'github_changes':False, 'W_ODD_NEG':'OPEN','RH':'OPEN'
}
(BASE/'nf362_directional_neumann_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['r_new_approx','r_old_approx','minimal_term_count_new_for_tail_below_eta','minimal_term_count_old_for_tail_below_eta','four_term_remainder_relative_to_Kee_approx','four_term_error_over_eta_approx','four_term_tail_over_eta_upper_approx']},indent=2))
print('new table:',[(x['number_of_terms'],x['remainder_relative_to_Kee_approx'],x['below_fourmode_eta']) for x in new[:6]])
