"""CC19 exact information-limit controls; no zeta leakage certificate.

Differential controls use u=2s/pi, v=2t/pi. Their rational formulas
are independently derived from the exact Dirichlet Green solution in
the accompanying note. Finite controls do not prove the analytic model.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json
from validate_native_source_shell_gain import run as inherited_run

ROOT=Path(__file__).resolve().parents[1]

def run():
    counts={k:0 for k in ('differential_crossing','positive_level',
                         'critical_power_multishell','finite_rank',
                         'weighted_covariance','dini_budget')}
    def check(ok,kind):
        assert ok,kind
        counts[kind]+=1
    differential=[]
    for j in range(1,81):
        u=1-F(1,2**j); d=1-u*u
        leak=2*u*(1-u)
        ratio=leak/d
        check(d>0 and leak>0,'differential_crossing')
        check(ratio==2*u/(1+u),'differential_crossing')
        check(0<ratio<1,'differential_crossing')
        check(1-ratio==(1-u)/(1+u),'differential_crossing')
        # Superlinear alpha=1/2: ratio squared grows at least 2^(j-3).
        check(leak*leak/(d*d*d)>F(2)**(j-3),'differential_crossing')
        for v in (F(17,16),F(9,8),F(3,2)):
            out=2*u*(v-u)
            check(out/d==2*u*(v-u)/((1-u)*(1+u)),
                  'differential_crossing')
            check(out/d>ratio,'differential_crossing')
            check(out>2*u*(v-1),'differential_crossing')
        if j in (1,4,16,40,80):
            differential.append({'j':j,'old_defect':str(d),
                'contact_leakage':str(leak),'weighted_lower':str(ratio),
                'beyond_contact_weighted_lower':str(2*u*(F(9,8)-u)/d)})
    # Original q=derivative mass minus physical mass. Shift adds mu mass
    # to the complete negative analysis, giving potential 1+mu=25/16.
    kappa=F(25,16); mu=kappa-1; v=F(4,5)
    check(kappa*v*v==1,'positive_level')
    check(1/(v*v)-1==mu>0,'positive_level')
    for j in range(1,81):
        u=v*(1-F(1,2**j)); shifted=1-kappa*u*u
        shifted_leak=kappa*2*u*(v-u)
        original=1-u*u
        check(shifted>0 and original>F(9,25),'positive_level')
        check(shifted_leak/shifted==2*u/(v+u),'positive_level')
        check(0<shifted_leak/shifted<1,'positive_level')
        check(2*u*(v-u)/original<shifted_leak/shifted,'positive_level')
        check(kappa*u*u==u*u+mu*u*u,'positive_level')
    # Critical-power leakage F(r)<=r/2 holds for every r, yet cost=N/4.
    # For each interval between atoms, F is constant; its ratio to r
    # is maximized at the smallest r. Checking all atoms proves the bound.
    multishell=[]
    for n in range(1,81):
        defects=[F(1,2**j) for j in range(1,n+1)]
        weights=[d/4 for d in defects]
        check(sum(weights,F(0))<F(1,4),'critical_power_multishell')
        cost=sum((w/d for w,d in zip(weights,defects)),F(0))
        check(cost==F(n,4),'critical_power_multishell')
        for d in defects:
            cumulative=sum((w for w,e in zip(weights,defects) if e<=d),F(0))
            check(cumulative<=d/2,'critical_power_multishell')
        if n in (1,4,16,80):
            multishell.append({'rank':n,'raw_norm_squared':str(sum(weights,F(0))),
                              'weighted_cost':str(cost),'linear_constant':'1/2'})
    # Independent finite critical rank changes the conclusion: per-mode
    # linear suppression gives cost <= rank*L. This does not certify L.
    for rank in range(1,17):
        for exponent in (4,16,64):
            constant=F(1,4*rank)
            ds=[F(1,2**(exponent+j)) for j in range(rank)]
            ws=[constant*d for d in ds]
            cost=sum((w/d for w,d in zip(ws,ds)),F(0))
            check(cost==rank*constant==F(1,4),'finite_rank')
            for d,w in zip(ds,ws):
                check(w<=constant*d,'finite_rank')
    # Matrix covariance domination is exactly weighted operator norm
    # domination. Rank-one whole-shell model, including mixed entries.
    for d1 in (F(1,4),F(1,2**20),F(1,2**80)):
      for d2 in (F(1,3),F(1,2**30)):
       for a,b in ((F(1,4),F(1,3)),(F(1,2),F(1,2)),(F(1),F(1))):
        # L=[d1*a,d2*b]^T, G=diag(d1^2,d2^2).
        q=a*a+b*b
        covariance=[[d1*d1*a*a,d1*d2*a*b],
                    [d1*d2*a*b,d2*d2*b*b]]
        D=[[q*d1*d1-covariance[0][0],-covariance[0][1]],
           [-covariance[1][0],q*d2*d2-covariance[1][1]]]
        check(D[0][0]>=0 and D[1][1]>=0,'weighted_covariance')
        check(D[0][0]*D[1][1]-D[0][1]*D[1][0]==0,'weighted_covariance')
        check(covariance[0][0]/(d1*d1)+covariance[1][1]/(d2*d2)==q,
              'weighted_covariance')
        check((q<1)==(a*a+b*b<1),'weighted_covariance')
    # Dyadic Dini leakage F(r_j)<=c*r_j/(j+1)^2 gives a summable
    # gap-independent operator majorant (the exact integral is analytic).
    for n in (8,16,32,64,128):
        partial=sum((F(1,(j+1)**2) for j in range(1,n+1)),F(0))
        check(partial<F(1),'dini_budget')
        check(partial+F(1,n+1)<1,'dini_budget')
    inherited=inherited_run()
    assert inherited['passed'] and inherited['exact_checks']==1572
    return {'stage':'CC19 complete-source shell leakage information limit',
            'classification':'C: structural implication refuted; actual arithmetic estimate open',
            'all_passed':True,'new_exact_checks':sum(counts.values()),
            'counts':counts,'inherited_nf67_exact_checks':inherited['exact_checks'],
            'total_exact_checks':sum(counts.values())+inherited['exact_checks'],
            'differential_controls':differential,'multishell_controls':multishell,
            'minimal_critical_arithmetic_target':'L L* <= q G, with independently bounded low cost ell and q+ell<1',
            'finite_rank_linear_target':'rank d and per-mode weight <=C*defect imply critical cost <=d*C',
            'actual_zeta_correlation_estimate_certified':False,
            'actual_zeta_estimate_disproved':False,'actual_zeta_contact_exists':False,
            'new_aperture_certified':False,'whole_domain_anchor':'21/20 inherited CC18',
            'global_nonstalling':False,'lean_certified':False,
            'scope':'Exact rational controls plus analytic differential/logarithmic crossing proofs; no replacement of zeta arithmetic.',
            'input_sha256':{'nf67_validator':hashlib.sha256(
                (ROOT/'scripts/validate_native_source_shell_gain.py').read_bytes()).hexdigest(),
                'cc18_summary':hashlib.sha256(
                (ROOT/'notes/data/RPB108_JOINED_CC18_SUMMARY_20261008.json').read_bytes()).hexdigest()},
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_SHELL_LEAKAGE_CC19_VALIDATION_20261008.json').write_text(
        json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('all_passed','counts','total_exact_checks')},indent=2))
