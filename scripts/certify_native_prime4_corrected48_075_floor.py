"""Sharper lawful correction using the independently certified full 48-source Gram."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,positive_pivots
from certify_native_prime4_complement48_075_floor import certificate as complement_certificate
from certify_native_prime4_gram48_075 import negative_candidate


def certificate():
    old=I.grid;I.grid=10**200
    try:return compute()
    finally:I.grid=old


def compute():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    paths={k:root/v for k,v in dict(native='RPB108_PRIME4_MATRIX48_075_CERTIFICATE_20261005.json',
            source='RPB108_PRIME4_SOURCE48_075_CERTIFICATE_20261005.json',
            gram='RPB108_PRIME4_GRAM48_075_CERTIFICATE_20261005.json').items()}
    native,source,gram=[json.loads(paths[k].read_text()) for k in ('native','source','gram')]
    hashes={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in paths.items()}
    assert native['aperture']==source['aperture']==gram['aperture']=='3/4'
    assert gram['native_certificate_sha256']==hashes['native'] and gram['source_certificate_sha256']==hashes['source']
    assert gram['native_source_pairing_count']==2304 and gram['projected_away_degrees']==list(range(48))
    assert native['physical_degrees']==list(range(48)) and len(source['rows'])==48
    complement=complement_certificate()
    assert complement['physical_lower']=='12/25' and complement['complement_inverse_factor']=='25/12'
    Q=[[I(*x) for x in row] for row in native['matrix_intervals']]
    R=[[I(*x) for x in row] for row in gram['residual_gram_surrogate']]
    eta=F(source['source_map_error_upper']);M=F(gram['surrogate_residual_map_norm_upper'])
    delta=F(gram['actual_gram_operator_error_upper'])
    assert delta==eta*(2*M+eta)
    trace=sum((R[i][i].hi for i in range(48)),F(0))
    assert M*M>=trace
    beta=F(25,12)
    G=[[Q[i][j]-beta*R[i][j] for j in range(48)] for i in range(48)]
    corrected=[row[:] for row in G]
    for i in range(48):corrected[i][i]-=beta*delta
    try:positive_pivots(corrected)
    except ArithmeticError:
        v=negative_candidate(G);assert v is not None
        norm=sum((x*x for x in v),F(0))
        value=sum((v[i]*G[i][j]*v[j] for i in range(48) for j in range(48)),I(0))
        upper=value.hi+beta*delta*norm
        raw=sum((v[i]*Q[i][j]*v[j] for i in range(48) for j in range(48)),I(0))
        residual=sum((v[i]*R[i][j]*v[j] for i in range(48) for j in range(48)),I(0))
        assert upper<0 and raw.lo>0 and residual.lo-delta*norm>0
        critical=raw.hi/(residual.lo-delta*norm)
        return dict(status='certified negative direction of sharper actual Q48-(25/12)R48 estimator',
            aperture='3/4',physical_degrees=list(range(48)),input_certificate_sha256=hashes,
            complement_inverse_factor=str(beta),physical_complement_lower='12/25',
            actual_gram_operator_error_upper=str(delta),estimator_negative_vector=[str(x) for x in v],
            actual_estimator_quadratic_upper=str(upper),actual_estimator_rayleigh_upper=str(upper/norm),
            same_vector_raw_quadratic_lower=str(raw.lo),critical_inverse_upper=str(critical),
            required_physical_coercivity_lower=str(1/critical),negative_estimator_control_raw_positive=True,
            corrected_schur_sign_certified=False,whole_domain_positivity=False,actual_negative_witness=False,
            global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)
    tau=F(1,10**16)
    while True:
        lower=[row[:] for row in G]
        for i in range(48):lower[i][i]-=beta*delta+tau
        try:pivots=positive_pivots(lower);break
        except ArithmeticError:
            if tau<F(1,10**25):raise
            tau/=2
    broken=[row[:] for row in lower];broken[0][0]=I(-1)
    try:positive_pivots(broken)
    except ArithmeticError:pass
    else:raise AssertionError('Negative diagonal control accepted')
    lift2=beta**2*(trace+delta);lift=1
    while lift*lift<=lift2:lift+=1
    whole=min(tau/(2*(1+lift*lift)),F(6,25))
    assert 2*whole<=F(12,25)
    return dict(status='certified positive actual corrected 48-source form with refined archimedean floor complement',
        aperture='3/4',physical_degrees=list(range(48)),input_certificate_sha256=hashes,
        native_source_pairing_count=2304,physical_complement_lower='12/25',logarithmic_complement_lower='9/100',
        complement_inverse_factor=str(beta),actual_gram_operator_error_upper=str(delta),
        corrected_coercivity_lower_bound=str(tau),shifted_pivot_lower_bounds=[str(x.lo) for x in pivots],
        lift_norm_squared_upper=str(lift2),lift_operator_norm_integer_upper=lift,
        whole_domain_physical_coercivity_lower=str(whole),negative_control_rejected=True,
        full_residual_gram_certified=True,corrected_schur_sign_certified=True,whole_domain_positivity=True,
        fixed_aperture_weak_kernel_zero=True,fixed_aperture_unit_domination=True,
        old_factor_5_over_2_estimator_negative=True,old_estimator_is_actual_negative_witness=False,
        global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
