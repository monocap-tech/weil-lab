"""Lossless, input-bound checkpoints for complete fixed-grid Gram panels."""
import json
from pathlib import Path
from certify_native_legendre_small_window import F,I


def encode_endpoint(x):
    scaled=x*I.grid
    assert scaled.denominator==1
    return str(scaled.numerator)


def save(path,bindings,completed,matrices):
    path=Path(path)
    payload=dict(version=1,bindings=bindings,grid=str(I.grid),completed_panels=completed,
        matrices={name:[[[encode_endpoint(x.lo),encode_endpoint(x.hi)] for x in row] for row in matrix]
                  for name,matrix in matrices.items()})
    temporary=path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(payload,separators=(',',':'))+'\n')
    temporary.replace(path)


def load(path,bindings,size=112):
    payload=json.loads(Path(path).read_text())
    assert payload['version']==1 and payload['bindings']==bindings
    assert payload['grid']==str(I.grid)
    completed=payload['completed_panels'];assert type(completed) is int and 0<=completed<=13
    assert set(payload['matrices'])=={'CS','smooth','cross'}
    matrices={}
    for name,values in payload['matrices'].items():
        assert len(values)==size and all(len(row)==size for row in values)
        decoded=[]
        for row in values:
            target=[]
            for pair in row:
                assert len(pair)==2
                lo,hi=[F(int(x),I.grid) for x in pair];assert lo<=hi
                target.append(I(lo,hi))
            decoded.append(target)
        matrices[name]=decoded
    return completed,matrices
