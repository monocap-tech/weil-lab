"""RC16 exact normalized whole-tail budgets and metric-alignment controls."""
from fractions import Fraction as F
import json
checks=0
def check(v):
    global checks
    if not v: raise AssertionError(checks+1)
    checks+=1
C=F(58)
f=F(1,2100)
gamma=F(627,16000)
delta=F(1,10**6)
tau=C*delta*delta/f
rho_squared=C*C*delta*delta/(f*gamma)
check(tau==F(609,5000000000)<F(1,10**6))
check(rho_squared==F(5887,32656250)<F(1,5000))
schur_cost=rho_squared/(1-tau)
check(schur_cost==F(188384000,1044999872719))
check(schur_cost<F(1,4999)<F(1,4000))
head_floor=F(1,4000)
reserve=head_floor-schur_cost
check(reserve==F(291463872719,4179999490876000)>0)
# Fourier/Taylor construction: high and low residual budgets delta/2 each.
log_cutoff=4/(delta*delta)
check(log_cutoff==4*10**12)
check(1/log_cutoff==(delta/2)**2)
# Rank threshold n >= 6z gives (3z/n)^n <= 2^-n.
for z in [F(1),F(7,3),F(100)]:
    n=int(6*z)+1
    check(3*z/n<F(1,2))
    check((3*z/n)**n<F(1,2)**n)
# Exact two-dimensional alignment control: choose A^(-1/2)=S symmetric.
# P=span(e1), H=span(e2); transformed head is span(S e1).
S=[[F(2),F(1)],[F(1),F(2)]]
transformed_head=[F(2),F(1)]
transformed_tail=[F(1),F(-2)]
check(sum((x*y for x,y in zip(transformed_head,transformed_tail)),F(0))==0)
mapped_tail=[sum((S[i][j]*transformed_tail[j] for j in range(2)),F(0)) for i in range(2)]
check(mapped_tail==[F(0),F(-3)]) # lies in canonical H
wrong_tail=[F(0),F(1)]
wrong_mapped=[sum((S[i][j]*wrong_tail[j] for j in range(2)),F(0)) for i in range(2)]
check(wrong_mapped==[F(1),F(2)]) # canonical-tail claim fails without transforming P
# Tail estimate delta enters quadratically in HKH but linearly in HKP.
for trial_delta in [F(1,1000),F(1,10000),F(1,100000),delta]:
    trial_tau=C*trial_delta**2/f
    trial_rho_squared=C*C*trial_delta**2/(f*gamma)
    check(trial_tau/trial_delta**2==C/f)
    check(trial_rho_squared/trial_delta**2==C*C/(f*gamma))
print(json.dumps({'milestone':'RC16','status':'PASS','exact_rational_checks':checks,
 'cap':'11/10','canonical_physical_tail_norm_upper':str(delta),
 'normalized_whole_tail_norm_upper':str(tau),
 'normalized_cross_norm_squared_upper':str(rho_squared),
 'conditional_head_floor':str(head_floor),'paid_schur_reserve':str(reserve),
 'projection':'normalized head = A_F**(-1/2) times canonical finite head',
 'explicit_rank_cost':'T=exp(4*10**12), n at least (264/7)*B*T',
 'finite_space_numerically_constructed':False,'actual_head_certified':False,
 'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False},indent=2))
