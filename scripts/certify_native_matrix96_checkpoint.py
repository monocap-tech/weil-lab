"""Hash-bound exact fixed-grid raw native row checkpoints; incomplete, not certificates."""
import gzip,json,os
from pathlib import Path
from certify_native_legendre96_097 import F,I

def save(path,bindings,completed_rows,matrix):
    assert I.grid==10**400
    entries=[]
    for i in range(96):
        for j in range(i+1):
            x=matrix[i][j]
            lo=x.lo*I.grid;hi=x.hi*I.grid
            assert lo.denominator==hi.denominator==1
            entries.append([str(lo.numerator),str(hi.numerator)])
    r=dict(kind='incomplete raw native row checkpoint',bindings=bindings,
           completed_rows=completed_rows,grid_digits=400,lower_triangle=entries)
    raw=json.dumps(r,sort_keys=True,separators=(',',':')).encode()
    target=Path(path);tmp=target.with_name(target.name+'.tmp')
    tmp.write_bytes(gzip.compress(raw,mtime=0));os.replace(tmp,target)

def load(path,bindings):
    r=json.loads(gzip.decompress(Path(path).read_bytes()))
    if r['kind']!='incomplete raw native row checkpoint' or r['bindings']!=bindings:
        raise ValueError('Mismatched native checkpoint binding')
    if r['grid_digits']!=400 or I.grid!=10**400:raise ValueError('Mismatched native checkpoint grid')
    n=r['completed_rows']
    if type(n) is not int or not 0<=n<=96:raise ValueError('Invalid native row count')
    entries=r['lower_triangle']
    if len(entries)!=4656:raise ValueError('Invalid native checkpoint dimension')
    matrix=[[I(0) for _ in range(96)] for _ in range(96)];index=0
    for i in range(96):
        for j in range(i+1):
            lo,hi=[F(int(x),I.grid) for x in entries[index]];index+=1
            if lo>hi:raise ValueError('Reversed native interval')
            if ((i+j)%2 or min(i,j)>=n) and (lo!=0 or hi!=0):
                raise ValueError('Uncomputed or odd native entry populated')
            matrix[i][j]=matrix[j][i]=I(lo,hi)
    return n,matrix
