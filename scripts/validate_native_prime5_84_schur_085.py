"""Independent stored-certificate custody and outward sign-margin checks."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path
from certify_native_legendre_small_window import I,positive_pivots


def certificate(repeat_path,audit_path):
    root=Path(__file__).resolve().parents[1]/'notes/data'
    gram_path=root/'RPB108_PRIME5_GRAM84_085_CERTIFICATE_20261006.json'
    assert gram_path.read_bytes()==Path(repeat_path).read_bytes()
    c=json.loads(gram_path.read_text())
    source_path=root/'RPB108_PRIME5_SOURCE84_085_CERTIFICATE_20261006.json'
    native_path=root/'RPB108_PRIME5_MATRIX84_085_COMPACT80_20261006.json'
    source=json.loads(source_path.read_text());native=json.loads(native_path.read_text())
    assert c['aperture']==source['aperture']==native['aperture']=='17/20'
    assert native['matrix_encoding']=='row-major lower triangle integer endpoints on grid 10^-80'
    triangle=native['lower_triangle_row_major'];assert len(triangle)==3570
    entries=[[None]*84 for _ in range(84)];index=0
    for i in range(84):
        for j in range(i+1):
            pair=[F(int(x),10**80) for x in triangle[index]];index+=1
            assert pair[0]<=pair[1]
            if (i+j)%2:assert pair==[F(0),F(0)]
            entries[i][j]=entries[j][i]=pair
    native['matrix_intervals']=entries
    assert c['source_certificate_sha256']==hashlib.sha256(source_path.read_bytes()).hexdigest()
    assert c['native_certificate_sha256']==hashlib.sha256(native_path.read_bytes()).hexdigest()
    assert c['physical_degrees']==c['projected_away_degrees']==list(range(84))
    assert c['native_source_pairing_count']==7056 and c['panel_count']==9 and c['all_mixed_terms_retained']
    R=[[(F(lo),F(hi)) for lo,hi in row] for row in c['residual_gram_surrogate']]
    assert c['residual_interval_encoding']=='exact finite decimal strings on outward grid 10^-300'
    assert all((x*10**300).denominator==1 for row in R for pair in row for x in pair)
    assert len(R)==84 and all(len(row)==84 for row in R)
    assert all(R[i][j]==R[j][i] and R[i][j][0]<=R[i][j][1] for i in range(84) for j in range(84))
    width=max(hi-lo for row in R for lo,hi in row)
    assert width==F(c['maximum_entry_width']) and width<F(1,10**55)
    eta=F(source['source_map_error_upper']);M=F(c['surrogate_residual_map_norm_upper'])
    trace=sum((R[i][i][1] for i in range(84)),F(0))
    assert M>=0 and M*M>=trace
    delta=eta*(2*M+eta)
    assert delta==F(c['actual_gram_operator_error_upper']) and delta<F(1,10**30)
    beta=F(c['complement_inverse_factor']);assert beta==F(40,23)
    assert all(c[k] is False for k in ('global_endpoint_excluded','f4_entry_closed','full_transport_closed','lean_formalized'))
    if c['whole_domain_positivity']:
        tau=F(c['corrected_coercivity_lower_bound']);assert tau>0
        pivots=list(map(F,c['shifted_pivot_lower_bounds']))
        assert len(pivots)==84 and min(pivots)>0
        I.grid=10**160
        lower=[[I(*entries[i][j])-beta*I(*R[i][j]) for j in range(84)] for i in range(84)]
        for i in range(84):lower[i][i]-=beta*delta+tau
        fresh=positive_pivots(lower)
        assert len(fresh)==84 and all(x.lo>0 for x in fresh)
        broken=[row[:] for row in lower];broken[0][0]=I(-1)
        try:positive_pivots(broken)
        except ArithmeticError:pass
        else:raise AssertionError('Negative control accepted')
        lift2=beta*beta*(trace+delta);assert lift2==F(c['lift_norm_squared_upper'])
        L=c['lift_operator_norm_integer_upper'];assert L*L>lift2
        whole=tau*F(23,40)/(tau+F(23,40)*(1+L*L))
        assert whole==F(c['whole_domain_physical_coercivity_lower'])
        assert F(c['logarithmic_coercivity_lower'])==whole/(10*(whole+23))
        assert c['corrected_schur_sign_certified'] and c['negative_control_rejected']
        assert c['fixed_aperture_weak_kernel_zero'] and c['fixed_aperture_unit_domination']
    else:
        v=list(map(F,c['estimator_negative_vector']));assert len(v)==84
        norm=sum((x*x for x in v),F(0));upper=lower=F(0)
        for i in range(84):
            for j in range(84):
                qlo,qhi=map(F,native['matrix_intervals'][i][j]);rlo,rhi=R[i][j];weight=v[i]*v[j]
                upper+=weight*((qhi-beta*rlo) if weight>=0 else (qlo-beta*rhi))
                lower+=weight*(qlo if weight>=0 else qhi)
        upper+=beta*delta*norm
        assert upper<0 and upper<=F(c['actual_estimator_quadratic_upper'])
        assert lower>0 and lower>=F(c['same_vector_raw_quadratic_lower'])
        assert c['actual_negative_witness'] is False and c['corrected_schur_sign_certified'] is False
    audit=json.loads(Path(audit_path).read_text())
    assert audit['actual_source_pair_checks']==audit['actual_endpoint_log_pair_checks']==9
    assert all(audit[k] for k in ('independent_direct_double_sum_agreement','original_convolution_interval_containment','large_integer_carry_controls_passed','mismatched_projection_controls_rejected'))
    return dict(certificate_reproduced_byte_for_byte=True,certificate_sha256=hashlib.sha256(gram_path.read_bytes()).hexdigest(),
                source_and_native_hashes_verified=True,residual_dimension=84,native_source_pairing_count=7056,
                symmetry_and_all_entry_widths_verified=True,exact_decimal_grid_endpoint_count=14112,
                source_error_correction_verified=True,
                fresh_160_digit_corrected_sign_verified=c['whole_domain_positivity'],
                exact_negative_estimator_direction_verified=not c['whole_domain_positivity'],
                same_direction_positive_native_energy_verified=not c['whole_domain_positivity'],
                sign_and_lift_margin_fields_verified=True,whole_domain_positivity=c['whole_domain_positivity'],
                independent_hankel_audit=audit,global_endpoint_excluded=False,f4_entry_closed=False,
                full_transport_closed=False,lean_formalized=False)


if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))
