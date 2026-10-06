"""Strict complete-panel reuse after an exclusively post-contraction audit repair."""
import hashlib,json,sys
from pathlib import Path
import certify_native_prime5_gram84_091 as gram
import certify_native_gram_checkpoint as codec

LEGACY_CONSTRUCTOR='d0800e732ff5ee5ebb45c45c69348cecbc5881dd8141422e1d03188a8ceda754'
CONTRACTION_PREFIX='77ef38c2323e3c16d0fe2bdaf916737e51cfd631c2ffefb13b6d7b0ff1ad4f6e'
MARKER=b'    R=[[I(0) for _ in range(84)] for _ in range(84)]'

def certificate(path):
    script=Path(gram.__file__).read_bytes()
    assert script.count(MARKER)==1
    assert hashlib.sha256(script.split(MARKER)[0]).hexdigest()==CONTRACTION_PREFIX
    state=json.loads(Path(path).read_bytes())
    assert state['completed_panels']==9
    assert state['bindings']['constructor']==LEGACY_CONSTRUCTOR
    original=codec.load
    def strict_load(checkpoint,bindings,size=84):
        assert Path(checkpoint).resolve()==Path(path).resolve()
        assert bindings['constructor']==hashlib.sha256(script).hexdigest()
        expected=dict(bindings);expected['constructor']=LEGACY_CONSTRUCTOR
        return original(checkpoint,expected,size)
    codec.load=strict_load
    try:result=gram.certificate(path)
    finally:codec.load=original
    result.update(reused_complete_panel_checkpoint_sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest(),
        unchanged_contraction_prefix_sha256=CONTRACTION_PREFIX,
        legacy_checkpoint_constructor_sha256=LEGACY_CONSTRUCTOR,
        current_constructor_sha256=hashlib.sha256(script).hexdigest(),
        all_nonconstructor_checkpoint_bindings_verified=True)
    return result

if __name__=='__main__':print(json.dumps(certificate(sys.argv[1]),indent=2))
