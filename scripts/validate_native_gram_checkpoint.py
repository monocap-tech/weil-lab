"""Verify exact endpoints survive recovery; reject changed inputs and incomplete shape."""
import json,tempfile
from pathlib import Path
from certify_native_legendre_small_window import F,I
from certify_native_gram_checkpoint import save,load


def certificate():
    old=I.grid;I.grid=10**300
    try:
        bindings=dict(source='source-A',native='native-A',aperture='9/10')
        matrices={name:[[I(-F(1,10**300),F(2,10**300)),I(F(7,3))],
                        [I(-10**80),I(0)]] for name in ('CS','smooth','cross')}
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'checkpoint.json'
            save(path,bindings,5,matrices);completed,decoded=load(path,bindings,size=2)
            assert completed==5
            assert all((matrices[name][i][j].lo,matrices[name][i][j].hi)==
                       (decoded[name][i][j].lo,decoded[name][i][j].hi)
                       for name in matrices for i in range(2) for j in range(2))
            try:load(path,dict(bindings,source='source-B'),size=2)
            except AssertionError:pass
            else:raise AssertionError('Changed input accepted')
            raw=json.loads(path.read_text());raw['matrices']['CS'][0].pop();path.write_text(json.dumps(raw))
            try:load(path,bindings,size=2)
            except AssertionError:pass
            else:raise AssertionError('Incomplete matrix accepted')
        return dict(exact_fixed_grid_endpoint_roundtrip=True,changed_input_control_rejected=True,
            incomplete_matrix_control_rejected=True,interval_grid_digits=300,
            mathematical_certificate_claim=False)
    finally:I.grid=old


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
