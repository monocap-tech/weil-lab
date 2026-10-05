"""Actual prime-3 whole-domain sign from the full 36-source Gram and optimized complement."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots
from certify_native_prime3_complement36_optimized import certificate as complement_certificate


def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    cp=root/'RPB108_PRIME3_COMPLEMENT36_OPTIMIZED_CERTIFICATE_20261005.json'
    np=root/'RPB108_PRIME3_MATRIX36_CERTIFICATE_20261005.json'
    gp=root/'RPB108_PRIME3_GRAM36_CERTIFICATE_20261005.json'
    sp=root/'RPB108_PRIME3_SOURCE36_CERTIFICATE_20261005.json'
    complement=json.loads(cp.read_text())
    assert complement==complement_certificate()
    native=json.loads(np.read_text());gram=json.loads(gp.read_text())
    assert gram['native_certificate_sha256']==hashlib.sha256(np.read_bytes()).hexdigest()
    assert gram['source_certificate_sha256']==hashlib.sha256(sp.read_bytes()).hexdigest()
    assert gram['physical_degrees']==gram['projected_away_degrees']==native['physical_degrees']==list(range(36))
    assert gram['aperture']==native['aperture']=='11/20'
    assert complement['physical_lower']=='1/3' and complement['logarithmic_lower']=='9/100'
    beta=F(complement['complement_inverse_factor']);assert beta==3
    old=I.grid;I.grid=10**200
    try:
        Q=[[I(*x) for x in row] for row in native['matrix_intervals']]
        R=[[I(*x) for x in row] for row in gram['residual_gram_surrogate']]
        assert len(Q)==len(R)==36 and all(len(row)==36 for row in Q+R)
        delta=F(gram['actual_gram_operator_error_upper'])
        G=[[Q[i][j]-beta*R[i][j] for j in range(36)] for i in range(36)]
        tau=F(1,10000000)
        while True:
            lower=[row[:] for row in G]
            for i in range(36):lower[i][i]-=beta*delta+tau
            try:pivots=positive_pivots(lower);break
            except ArithmeticError:
                if tau<F(1,10**20):raise
                tau/=2
        trace_upper=sum((R[i][i].hi for i in range(36)),F(0))
        lift2=beta**2*(trace_upper+delta)
        lift_integer=1
        while lift_integer**2<=lift2:lift_integer+=1
        whole=min(tau/(2*(1+lift_integer**2)),F(complement['physical_lower'])/2)
        assert whole>0 and tau==F(1,40000000)
        broken=[row[:] for row in lower];broken[0][0]=I(-1)
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative diagonal control accepted')
        return dict(status='certified actual whole-domain positivity at prime-3 aperture',aperture='11/20',
                    physical_degrees=list(range(36)),projected_away_degrees=list(range(36)),
                    complement_physical_lower='1/3',complement_logarithmic_lower='9/100',
                    complement_inverse_factor=str(beta),corrected_coercivity_lower_bound=str(tau),
                    gram_operator_error_upper=str(delta),surrogate_gram_trace_upper=str(trace_upper),
                    shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],
                    lift_norm_squared_upper=str(lift2),lift_operator_norm_integer_upper=lift_integer,
                    whole_domain_physical_coercivity_lower=str(whole),negative_control_rejected=True,
                    native_certificate_sha256=hashlib.sha256(np.read_bytes()).hexdigest(),
                    gram_certificate_sha256=hashlib.sha256(gp.read_bytes()).hexdigest(),
                    source_certificate_sha256=hashlib.sha256(sp.read_bytes()).hexdigest(),
                    optimized_complement_certificate_sha256=hashlib.sha256(cp.read_bytes()).hexdigest(),
                    whole_domain_positivity=True,corrected_schur_sign_certified=True,
                    fixed_aperture_weak_kernel_zero=True,fixed_aperture_unit_domination=True,
                    global_endpoint_excluded=False,all_window_domination=False,
                    retained_witness_null_transport_closed=False,f4_entry_closed=False,
                    full_transport_closed=False,lean_formalized=False)
    finally:I.grid=old


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
