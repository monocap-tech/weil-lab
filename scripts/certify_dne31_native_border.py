#!/usr/bin/env python3
"""Complete original native border of DNE29 T4 against DNE24 W52.

Analytic polynomial/log moments, directed Decimal arithmetic, and the
inherited uniform original-source remainder; no quadrature.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse, base64, gzip, hashlib, json, sys, time

PARENT='1daea791c7fe90a355183d19bcf78dd95edc1664'
def read(path):
    b=Path(path).read_bytes()
    if path.endswith('.gz.b64'): b=gzip.decompress(base64.b64decode(b))
    return json.loads(b),hashlib.sha256(b).hexdigest()
def root(x):
    scale=10**160
    v=F(isqrt(x.numerator*scale*scale//x.denominator)+1,scale)
    assert v*v>x
    return v
def compact(out):
    """Outward rational storage; pay source error after rounding truncations."""
    grid=10**110
    def floor(x):return F((F(x)*grid).numerator//(F(x)*grid).denominator,grid)
    def ceil(x):return -floor(-F(x))
    def outward(v):return [str(floor(v[0])),str(ceil(v[1]))]
    err=ceil(out['uniform_original_source_operator_error_upper'])
    out['uniform_original_source_operator_error_upper']=str(err)
    _,par,fixed_path,_,_=out['input_paths'];fixed,_=read(fixed_path)
    norms=[F(1)]+[F(c['norm_upper']) for c in fixed['columns']]
    for i in range(4):
        for j in range(52):
            tr=outward(out['truncated_native_border'][i][j]);pay=ceil(err*norms[i]*F(out['W_column_norm_upper'][j]))
            out['truncated_native_border'][i][j]=tr;out['source_error_payments'][i][j]=str(pay)
            out['original_native_T4_W52_border'][i][j]=[str(F(tr[0])-pay),str(F(tr[1])+pay)]
    out['fresh_original_T4_native_matrix']=[[outward(v) for v in row] for row in out['fresh_original_T4_native_matrix']]
    out['outward_storage_grid']='1/'+str(grid)
    return out
def inverse(A):
    n=len(A);B=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        q=next(j for j in range(i,n) if B[j][i]);B[i],B[q]=B[q],B[i]
        v=B[i][i];B[i]=[x/v for x in B[i]]
        for j in range(n):
            if j!=i:
                v=B[j][i];B[j]=[x-v*y for x,y in zip(B[j],B[i])]
    return [row[n:] for row in B]
def run(parity, output):
    start=time.time();upper=parity.upper();paths=[
        'scripts/dne23_dne16_source_input.py',
        'notes/data/RPB108_DNE15_NF24_TARGETS_20261009.json.gz.b64',
        f'notes/data/RPB108_DNE29_{upper}_SELECTED_COLUMNS_20261009.json.gz.b64',
        'notes/data/RPB108_DNE24_NULL_REDUCTION_CERTIFICATE_20261009.json',
        'notes/data/RPB108_DNE29_OPTIMIZED_LOW_UNION_CERTIFICATE_20261009.json']
    helper=Path(paths[0]).read_bytes();assert hashlib.sha256(helper).hexdigest()=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8'
    targets,th=read(paths[1]);fixed,fh=read(paths[2]);d24,dh=read(paths[3]);d29,qh=read(paths[4])
    assert th=='6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00'
    assert qh=='af2acfa894b79426b3219a0303c2815df721b4bcd4ca0a8d6d271a69606cdd78'
    ix=0 if parity=='even' else 1
    assert fh==['435a347824b6ba783956d212b0c48adc2914c3df1443f6cd1129d0dcc905b718','c4828a354f5d6af5b54e0bc25179ce1d522d68df3cebe75ff9ebef123cc87936'][ix]
    wr=d24['rows'][ix];qr=d29['rows'][ix];assert fixed['parity']==wr['parity']==qr['parity']==parity
    prefix=helper.decode().split('\nps=[p]+')[0]
    assert prefix.count('range(116)')==1
    prefix=prefix.replace('range(116)','range(181)')
    old=sys.argv;sys.argv=[paths[0],parity,paths[1]];d={}
    try:exec(compile(prefix,paths[0],'exec'),d)
    finally:sys.argv=old
    I,Z,A,bases=d['I'],d['Z'],d['A'],d['bases'];plus=d['plus'];conv=d['conv'];polyint=d['polyint']
    low=ix;indices=list(range(low,112,2));piv=wr['constraint_pivots'];free=wr['free_coordinates']
    vectors=[[F(j==0) for j in range(56)]]
    cols=[dict(indices=[low],coefficients=['1'],norm_upper='1')]+fixed['columns']
    for col in fixed['columns']:
        cc=dict(zip(col['indices'],map(F,col['coefficients'])))
        vectors.append([cc.get(n,F(0)) for n in indices])
    inv=inverse([[v[j] for j in piv] for v in vectors]);W=[]
    assert len(free)==52 and inv
    for j in free:
        v=[F(k==j) for k in range(56)]
        for i,k in enumerate(piv):v[k]=-sum(inv[i][l]*vectors[l][j] for l in range(4))
        assert all(sum(x*y for x,y in zip(row,v))==0 for row in vectors)
        W.append(v)
    norms=[root(sum(x*x for x in v)) for v in W]
    ps=[];us=[];pnorm=[]
    for col in cols:
        p=[Z]*(max(col['indices'])+1);dp=[Z]*len(p)
        for n,c in zip(col['indices'],map(F,col['coefficients'])):
            p=plus(p,bases[n],I(c));dp=plus(dp,bases[n],I(c)*I(sum((F(1,k) for k in range(1,n+1)),F(0))))
        ps.append(p);us.append(d['make_u'](p,dp));pnorm.append(F(col['norm_upper']))
        print('original source',parity,len(ps),'seconds',round(time.time()-start,1),flush=True)
    active=(2,3,4,5,7,8);ells={n:I(n).log() for n in active};cs={n:ells[2 if n in (4,8) else n]/I(n).sqrt() for n in active}
    cuts=[I(0),A]+[(ells[n]-A if ells[n].lo>A.hi else A-ells[n]) for n in active];cuts.sort(key=lambda x:x.lo)
    assert all(l.hi<h.lo for l,h in zip(cuts,cuts[1:]))
    maxn=180-low;maxdeg=max(map(len,ps))-1+maxn;logs={}
    for j,x in enumerate(cuts):
        xp=[x**k for k in range(maxdeg+2)];vals=[Z]*(maxdeg+1)
        for sign in (-1,1):
            b=-sign*A;bp=[b**k for k in range(maxdeg+2)];y=A+sign*x;endpoint=y.lo<=0<=y.hi
            if endpoint:assert abs(y.lo)<d['D']('1e-170') and abs(y.hi)<d['D']('1e-170')
            ly=Z if endpoint else y.log();S=Z
            for k in range(maxdeg+1):
                S=b*S+xp[k+1]/(k+1);vals[k]=vals[k]+((Z if endpoint else (xp[k+1]-bp[k+1])*ly)-S)/(k+1)
        for k,v in enumerate(vals):logs[k,j]=v
    moments=[[Z]*(maxn+1) for _ in cols]
    shifts=[{(n,s):d['shift'](p,s*ells[n]) for n in active for s in (-1,1)} for p in ps]
    for panel,(l,h) in enumerate(zip(cuts,cuts[1:])):
        mid=(l+h)/2;maxk=max(map(len,us))+maxn
        pm=[(h**(k+1)-l**(k+1))/(k+1) for k in range(maxk)]
        for i,(p,u) in enumerate(zip(ps,us)):
            uj=list(u)
            for n in active:
                for s in (-1,1):
                    pos=mid+s*ells[n]
                    if pos.lo>-A.lo and pos.hi<A.lo:uj=plus(uj,shifts[i][n,s],-cs[n])
                    else:assert pos.hi<=-A.hi or pos.lo>=A.hi
            for k in range(low,maxn+1,2):
                moments[i][k]=moments[i][k]+sum((v*pm[m+k] for m,v in enumerate(uj)),Z)-sum((v*(logs[m+k,panel+1]-logs[m+k,panel])/2 for m,v in enumerate(p)),Z)
        print('complete native panel',parity,panel,'seconds',round(time.time()-start,1),flush=True)
    coords=[[2*sum((v*m[k] for k,v in enumerate(bases[n])),Z) for n in range(low,maxn+1,2)] for m in moments]
    operr=2*A*I(F(550,19))*I(F(106,125))**d['N']+I('3e-99')
    result=[];truncated=[];errors=[]
    for i,cc in enumerate(coords):
        row=[];tr=[];er=[]
        for v,norm in zip(W,norms):
            value=sum((I(x)*y for x,y in zip(v,cc[:56])),Z);e=operr*I(pnorm[i])*I(norm)
            tr.append(value.data());row.append((value+I(e.hi.copy_negate(),e.hi)).data());er.append(str(e.hi))
        result.append(row);truncated.append(tr);errors.append(er)
    # Independently recorded full native T4 matrix must overlap every fresh entry.
    overlaps=0;fresh_native=[]
    for i in range(4):
        fresh_row=[]
        for j,col in enumerate(cols):
            value=sum((I(F(c))*coords[i][(n-low)//2] for n,c in zip(col['indices'],col['coefficients'])),Z)
            e=operr*I(pnorm[i])*I(pnorm[j]);value=value+I(e.hi.copy_negate(),e.hi)
            lo,hi=map(F,qr['scaled_native_matrix'][i][j]);scale=F(qr['column_scales'][i])*F(qr['column_scales'][j])
            assert F(value.lo)*scale<=hi and lo<=F(value.hi)*scale
            overlaps+=1
            fresh_row.append(value.data())
        fresh_native.append(fresh_row)
    out=dict(stage='DNE31',parent=PARENT,parity=parity,precision=d['P'],regular_order=d['N'],input_paths=paths,input_sha256=[hashlib.sha256(helper).hexdigest(),th,fh,dh,qh],
        remaining_dimension=52,constraint_pivots=piv,free_coordinates=free,retained_indices=indices,
        exact_W_columns=[[str(v) for v in row] for row in W],W_column_norm_upper=list(map(str,norms)),
        original_native_T4_W52_border=result,truncated_native_border=truncated,source_error_payments=errors,
        original_T4_native_overlap_checks=overlaps,fresh_original_T4_native_matrix=fresh_native,uniform_original_source_operator_error_upper=str(operr.hi),
        complete_original_source_action=True,all_six_primes_both_orientations=True,exact_endpoint_log=True,half_translation_panels=7,
        sampled_quadrature=False,complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
    out=compact(out)
    Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'parity':parity,'native_border_entries':208,'native_overlap_checks':overlaps,'elapsed':time.time()-start}),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('parity',choices=['even','odd']);p.add_argument('--output',required=True);a=p.parse_args();run(a.parity,a.output)
