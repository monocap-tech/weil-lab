"""CC32 finite conditional row-selection controls, not actual zeta data."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_uniform_critical_rank_cc31 import run as inherited_run
from validate_native_critical_flux_limit_cc29 import family,add,scale
from validate_native_forced_source_cc20 import mm,tr,eye,sub
ROOT=Path(__file__).resolve().parents[1]

def run():
    counts={k:0 for k in ('filter_constants','rotating_row','coherent_trace_selection','power_cost','genuine_crossing')}
    def check(v,k):
        assert v,k
        counts[k]+=1
    gamma=F(1,8);M=F(2);C=16*M*M/(gamma*gamma);eta=F(1,4)
    check(C==4096,'filter_constants')
    check(4*M*M/C==gamma*gamma/4,'filter_constants')
    AA=[[F(1),F(0)],[F(0),F(1,2)]]
    AT=add(AA,scale(gamma,[[F(1),F(1)],[F(1),F(1)]]))
    for j in (8,12,16,24,32,40):
        delta=F(1,2**(2*j));AS,E=family(delta)
        d=delta+F(1,2)*delta*delta/(1+delta*delta)
        epsilon=C*d
        check(delta<=epsilon<=eta,'filter_constants')
        check(F(1,2)+delta>epsilon,'filter_constants')
        y=[[F(1)],[F(0)]];v=mm(E,y)
        err=mm(tr(sub(y,v)),sub(y,v))[0][0]
        check(err<=d/epsilon==1/C,'rotating_row')
        H=sub(AT,AS);flux=mm(mm(tr(v),H),v)[0][0]
        check(flux>=gamma/2,'rotating_row')
        # True eigenvector is (1,delta)/sqrt(1+delta^2); ratio is rational.
        z=[[F(1)],[delta]]
        a=mm(mm(tr(z),H),z)[0][0]/(1+delta*delta)
        check(a>=flux>=gamma/2,'rotating_row')
        lam=1-delta
        check(lam*a>=(1-eta)*gamma/2,'rotating_row')
        for alpha in (1,2,3):
            check(a/(delta**alpha)>=gamma/(2*(C*d)**alpha),'power_cost')
    for root_d in (1,2,3,4):
        r=root_d*root_d;y=[F(1,root_d)]*r
        check(sum(v*v for v in y)==1,'coherent_trace_selection')
        for j in (8,16,24):
            d=F(1,2**j);epsilon=C*d
            if epsilon>eta:continue
            # A_a=I; H=d I + gamma y y*. Rank r is finite.
            diagonal=[d+gamma*v*v for v in y]
            quadratic=d+gamma
            check(sum(diagonal)>=quadratic>=gamma/2,'coherent_trace_selection')
            check(max(diagonal)>=gamma/(2*r),'coherent_trace_selection')
            check(d<=epsilon,'filter_constants')
            check((1-d)*max(diagonal)>=(1-eta)*gamma/(2*r),'coherent_trace_selection')
    v=F(17,16)
    for j in (8,16,32,48,64):
        u=1-F(1,2**j);gap=1-u*u;leak=2*u*(v-u)
        check(leak>F(1,16),'genuine_crossing')
        check(leak/gap>F(2)**(j-6),'genuine_crossing')
    inherited=inherited_run()
    assert inherited['all_passed'] and inherited['total_exact_checks']==25375
    paths=['scripts/validate_native_uniform_critical_rank_cc31.py',
           'notes/REFLECTED_PACKET_BRIDGE_108_FORCED_SOURCE_CC20_20261008.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_CRITICAL_FLUX_LIMIT_CC29_20261008.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_UNIFORM_CRITICAL_RANK_CC31_20261008.md']
    return {'stage':'CC32 individual persistent row at hypothetical contact',
            'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
            'inherited_cc31_checks':25375,'total_exact_checks':25375+sum(counts.values()),
            'conditional_actual_result':'some eigenrow has delta_i<=16 M^2 d_s/gamma^2 and leakage >=gamma/(2 d_B)',
            'actual_contact_exists_claimed':False,'actual_scalar_upper_bound_proved':False,
            'actual_critical_covariance_evaluated':False,'continuous_eigenvector_branch_assumed':False,
            'fixed_target_enlargement_preserved':True,'fixed_critical_target_band_preserved':True,
            'new_aperture':False,'RH_proved':False,'lean_certified':False,
            'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_PERSISTENT_CRITICAL_ROW_CC32_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
