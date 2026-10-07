"""Complete bound raw rows and stop before the optional dense finite sign."""
import gzip,hashlib,json
from pathlib import Path
import certify_native_matrix96_checkpoint as codec
from certify_native_legendre96_0973 import I
from certify_native_prime7_matrix96_0973 import certificate as native

class CompleteRows(Exception):pass

def certificate(path):
    p=Path(path);before=0
    if p.exists():before=json.loads(gzip.decompress(p.read_bytes()))['completed_rows']
    saved=codec.save
    def boundary(target,bindings,done,matrix):
        saved(target,bindings,done,matrix)
        if done==96:raise CompleteRows()
    if before<96:
        codec.save=boundary
        try:native(str(p))
        except CompleteRows:pass
        else:raise AssertionError('Missing complete-row boundary')
        finally:codec.save=saved
    raw=p.read_bytes();state=json.loads(gzip.decompress(raw));assert state['completed_rows']==96
    assert state['bindings']['aperture']=='973/1000' and state['bindings']['bernoulli_pairs']==300
    for name,digest in state['bindings']['scripts'].items():
        assert hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest()==digest
    previous=I.grid;I.grid=10**400
    try:assert codec.load(str(p),state['bindings'])[0]==96
    finally:I.grid=previous
    return dict(aperture='973/1000',initial_completed_rows=before,actual_completed_rows=96,
        complete_checkpoint_sha256=hashlib.sha256(raw).hexdigest(),
        finite_sign_certified=False,whole_domain_positivity=False,f4_entry_closed=False)

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(sys.argv[1]),indent=2))
