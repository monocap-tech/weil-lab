"""Historical quarter golden and fresh native/source constructor rejection controls."""
import hashlib,json
import certify_native_legendre_small_window as native
import certify_native_prime3_source36 as source


def certificate():
    golden=hashlib.sha256((json.dumps(native.certificate(),sort_keys=True,separators=(',',':'))+'\n').encode()).hexdigest()
    assert golden=='4045a32f5e57a0685cf5eb2d46dfde97906ff315b800fbb8757350d186094b37'
    controls=0
    for degree,returned in [(7,True),(83,False),(35,True)]:
        try:native.certificate(native.F(91,100),return_matrix=returned,degree=degree)
        except ValueError:controls+=1
        else:raise AssertionError('Invalid native constructor accepted')
    for degree in (35,47,51):
        try:source.compute(a=native.F(91,100),degree=degree)
        except ValueError:controls+=1
        else:raise AssertionError('Invalid source constructor accepted')
    return dict(quarter_native_golden_unchanged=True,quarter_golden_sha256=golden,
        invalid_constructor_controls_rejected=controls,new_aperture_whole_domain_positivity=False)


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
