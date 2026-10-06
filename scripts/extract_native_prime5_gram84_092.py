"""Export the unchanged completed Gram immediately before its separate sign stage."""
import copy,hashlib,inspect,json
from pathlib import Path
import certify_native_prime5_gram84_092 as engine

class GramComplete(Exception):pass

def certificate(checkpoint):
    state=Path(checkpoint).read_bytes();data=json.loads(state)
    assert data['completed_panels']==9
    assert data['bindings']['constructor']==hashlib.sha256(Path(engine.__file__).read_bytes()).hexdigest()
    saved=engine.positive_pivots;result=None
    def capture(matrix):
        nonlocal result
        frame=inspect.currentframe().f_back
        assert frame.f_code is engine.compute.__code__ and 'result' in frame.f_locals
        assert frame.f_locals['G'] is matrix
        result=copy.deepcopy(frame.f_locals['result'])
        assert result['aperture']=='23/25' and result['panel_count']==9
        assert result['whole_domain_positivity'] is False
        result.update(corrected_schur_sign_certified=False,
            full_source_gram_certified=True,no_lift_estimator_status='complete Gram; separate corrected sign pending',
            gram_constructor_sha256=data['bindings']['constructor'],
            complete_panel_checkpoint_sha256=hashlib.sha256(state).hexdigest(),
            extraction_stage='unchanged constructor through complete Gram, intercepted at first sign call')
        raise GramComplete()
    engine.positive_pivots=capture
    try:
        try:engine.certificate(checkpoint)
        except GramComplete:pass
        else:raise AssertionError('The intended Gram/sign boundary was not reached')
    finally:engine.positive_pivots=saved
    assert result is not None
    return result

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
