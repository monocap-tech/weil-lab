"""CC33 finite remainder/projection controls; no zeta upper bound."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
from validate_native_persistent_critical_row_cc32 import run as inherited_run
ROOT=Path(__file__).resolve().parents[1]

def run():
    counts={k:0 for k in ('principal_cancellation','noncommuting_metric','squared_correction','compact_crossing','power_absorption')}
    def check(v,k):
        assert v,k
        counts[k]+=1
    for j in (2,4,8,16,32,48):
        u=1-F(1,2**j);delta=1-u*u;lam=u*u;v=F(1,4)
        for b in (F(-1,4),F(0),F(1,4),F(1,2)):
            q=b-u*v;row=lam*b-u*v;correction=delta*b
            check(row==q-correction,'principal_cancellation')
            check((1-u*u)-delta==0,'principal_cancellation')
            # M inverse is (1-b^2)^-1 [[1,-b],[-b,1]].
            jj=row*row/(1-b*b);qq=q*q/(1-b*b);ee=correction*correction/(1-b*b)
            U2=1+abs(b);c2=1-abs(b)
            check(ee<=delta*delta*U2/c2,'noncommuting_metric')
            check((b!=0)==(correction!=0),'noncommuting_metric')
            check(jj<=2*qq+2*ee,'squared_correction')
            check(qq<=2*jj+2*ee,'squared_correction')
            if b==0:
                check(jj==lam*v*v==qq,'compact_crossing')
                determinant=delta*(1-v*v)-lam*v*v
                check(determinant==delta-v*v,'compact_crossing')
                check((determinant<0)==(delta<v*v),'compact_crossing')
                check(jj>=F(9,256),'compact_crossing')
        check(delta*delta<=delta,'power_absorption')
        check(delta*delta<=1 and delta*delta==delta**2,'power_absorption')
    inherited=inherited_run()
    assert inherited['all_passed'] and inherited['total_exact_checks']==25477
    paths=['scripts/validate_native_persistent_critical_row_cc32.py',
           'notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_LOG_SOURCE_ANALYSIS_20261003.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_FORCED_SOURCE_CC20_20261008.md',
           'notes/REFLECTED_PACKET_BRIDGE_108_PERSISTENT_CRITICAL_ROW_CC32_20261008.md']
    return {'stage':'CC33 actual native remainder forcing after principal cancellation',
            'all_passed':True,'new_counts':counts,'new_exact_checks':sum(counts.values()),
            'inherited_cc32_checks':25477,'total_exact_checks':25477+sum(counts.values()),
            'analytic_identity':'j_i=(I-Pi_D)(C_t-delta_i M_t)h_i',
            'analytic_correction':'positive-inverse norm difference <=(U_B/c_B)delta_i',
            'actual_native_remainder_suppression_proved':False,
            'actual_critical_covariance_evaluated':False,'negative_source_compactness_claimed':False,
            'full_Q_bounded_physical_L2_operator_claimed':False,
            'new_aperture':False,'RH_proved':False,'lean_certified':False,
            'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
            'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_NATIVE_REMAINDER_FORCING_CC33_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('all_passed','new_counts','total_exact_checks')},indent=2))
