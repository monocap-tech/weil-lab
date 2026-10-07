"""Audit custody and exact decoding of an incomplete fresh Gram checkpoint."""
import gzip,hashlib,json,tempfile
from pathlib import Path
from certify_native_legendre_small_window import I
from certify_native_gram_checkpoint import load

def certificate(path):
    raw=Path(path).read_bytes()
    if str(path).endswith('.gz'):raw=gzip.decompress(raw)
    state=json.loads(raw);root=Path(__file__).resolve().parents[1]
    source=root/'notes/data/RPB108_PRIME5_SOURCE84_096_CERTIFICATE_20261007.json.gz'
    expected=dict(source=hashlib.sha256(gzip.decompress(source.read_bytes())).hexdigest(),
        native=hashlib.sha256((root/'notes/data/RPB108_PRIME5_MATRIX84_096_COMPACT80_20261007.json').read_bytes()).hexdigest(),
        aperture='24/25',log_series_terms=500)
    names={'constructor':'certify_native_prime5_gram84_096.py',
        'geometry':'certify_native_translation_panel_order.py','hankel':'certify_native_exact_hankel.py',
        'checkpoint_codec':'certify_native_gram_checkpoint.py'}
    expected.update({k:hashlib.sha256((root/'scripts'/n).read_bytes()).hexdigest() for k,n in names.items()})
    assert state['bindings']==expected
    old=I.grid;I.grid=10**300
    try:
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'checkpoint.json';p.write_bytes(raw)
            done,matrices=load(p,expected);assert 1<=done<9
            assert set(matrices)=={'CS','smooth','cross'}
            wrong=dict(expected,source='0'*64)
            try:load(p,wrong)
            except AssertionError:pass
            else:raise AssertionError('Mismatched source checkpoint accepted')
    finally:I.grid=old
    return dict(aperture='24/25',completed_panels=done,required_panels=9,
        checkpoint_sha256=hashlib.sha256(raw).hexdigest(),bindings=expected,
        decoded_matrix_entries=3*84*84,mismatched_source_control_rejected=True,
        complete_residual_gram_certified=False,corrected_schur_sign_certified=False,
        whole_domain_positivity=False,whole_domain_positivity_frontier='19/20',
        f4_entry_closed=False,lean_formalized=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
