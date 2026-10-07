"""Actual first-two-row native recovery audit; no full matrix sign claim."""
import gzip,hashlib,json,tempfile
from pathlib import Path
import certify_native_matrix112_checkpoint as codec
from certify_native_prime7_matrix112_0995 import certificate as native

class RowBoundary(Exception):pass

def certificate():
    saved=codec.save
    with tempfile.TemporaryDirectory() as directory:
        direct=Path(directory)/'direct.gz';resumed=Path(directory)/'resumed.gz'
        def run(path,stop):
            def boundary(target,bindings,done,matrix):
                saved(target,bindings,done,matrix)
                if done==stop:raise RowBoundary()
            codec.save=boundary
            try:native(str(path))
            except RowBoundary:pass
            else:raise AssertionError('Expected partial-row boundary was not reached')
            finally:codec.save=saved
        run(direct,2)
        run(resumed,1)
        one=gzip.decompress(resumed.read_bytes());first=json.loads(one);assert first['completed_rows']==1
        run(resumed,2)
        a=gzip.decompress(direct.read_bytes());b=gzip.decompress(resumed.read_bytes())
        assert a==b
        data=json.loads(a);assert data['completed_rows']==2
        assert all(x['aperture']=='199/200' for x in [data['bindings']])
        return dict(actual_completed_rows=2,resumed_from_row_count=1,
            independent_fresh_vs_resumed_raw_rows_equal=True,
            checkpoint_sha256=hashlib.sha256(a).hexdigest(),
            raw_even_entries_checked=112,whole_native_matrix_pending=True,
            finite_sign_certified=False,whole_domain_positivity=False,f4_entry_closed=False)

if __name__=='__main__':print(json.dumps(certificate(),indent=2))


