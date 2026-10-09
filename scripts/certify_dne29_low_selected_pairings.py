#!/usr/bin/env python3
"""Fresh original low/NF38-selected energy row; complete endpoint and prime action."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,sys,time,gzip,base64
def run(parity,targets,columns,low,helper,output,reverse=False):
    started=time.time();source=Path(helper).read_bytes()
    assert hashlib.sha256(source).hexdigest()=='e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8'
    assert hashlib.sha256(Path(low).read_bytes()).hexdigest()=='ebca74e6237cf401b7480afe08b91caba2c3412dc08e55ac2ac55f1970d8f788'
    column_bytes=Path(columns).read_bytes()
    if columns.endswith('.gz.b64'):column_bytes=gzip.decompress(base64.b64decode(column_bytes))
    fixed=json.loads(column_bytes);assert fixed['parity']==parity
    prefix=source.decode().split('\nps=[p]+')[0];assert prefix.endswith(' return u\n') and prefix.count('range(116)')==1
    # Only basis availability changes; the original low-source formula is identical.
    prefix=prefix.replace('range(116)','range(181)')
    oldargv=sys.argv;sys.argv=[str(helper),parity,targets];d={}
    try:exec(compile(prefix,str(helper),'exec'),d)
    finally:sys.argv=oldargv
    I=d['I'];Z=d['Z'];A=d['A'];bases=d['bases'];plus=d['plus'];conv=d['conv'];N=d['N'];polyint=d['polyint']
    tests=[];norms=[];test_dp=[]
    for col in fixed['columns']:
        coeff=list(map(F,col['coefficients']));mass=sum(v*v for v in coeff);norm=F(col['norm_upper']);assert mass==F(col['exact_mass_squared']) and norm*norm>mass
        test=[Z]*(max(col['indices'])+1);tdp=[Z]*len(test)
        for n,c in zip(col['indices'],coeff):
            test=plus(test,bases[n],I(c));tdp=plus(tdp,bases[n],I(c)*I(sum((F(1,k) for k in range(1,n+1)),F(0))))
        tests.append(test);norms.append(norm);test_dp.append(tdp)
    START=0 if parity=='even' else 1;p=bases[START];dp=[v*START for v in p];u=d['make_u'](p,dp);tests.append(p);norms.append(F(1))
    active=(2,3,4,5,7,8);ells={n:I(n).log() for n in active};cs={n:ells[2 if n in (4,8) else n]/I(n).sqrt() for n in active}
    cuts=[I(0),A]+[(ells[n]-A if ells[n].lo>A.hi else A-ells[n]) for n in active];cuts.sort(key=lambda x:x.lo)
    assert all(l.hi<h.lo for l,h in zip(cuts,cuts[1:]))
    maxdeg=len(p)+max(map(len,tests))-2;logprims={}
    for j,x in enumerate(cuts):
        xp=[x**k for k in range(maxdeg+2)];vals=[Z]*(maxdeg+1)
        for sign in (-1,1):
            b=-sign*A;bp=[b**k for k in range(maxdeg+2)];y=A+sign*x;endpoint=y.lo<=0<=y.hi
            if endpoint:assert abs(y.lo)<d['D']('1e-170') and abs(y.hi)<d['D']('1e-170')
            ly=Z if endpoint else y.log();S=Z
            for k in range(maxdeg+1):
                S=b*S+xp[k+1]/(k+1);v=Z if endpoint else (xp[k+1]-bp[k+1])*ly;vals[k]=vals[k]+(v-S)/(k+1)
        for k,v in enumerate(vals):logprims[k,j]=v
    values=[Z]*len(tests);products=[conv(p,z) for z in tests];shifts={(n,s):d['shift'](p,s*ells[n]) for n in active for s in (-1,1)}
    if reverse:
        reverse_u=[d['make_u'](z,zdp) for z,zdp in zip(tests[:3],test_dp)]+[u]
        reverse_shifts=[{(n,s):d['shift'](z,s*ells[n]) for n in active for s in (-1,1)} for z in tests]
    for j,(l,h) in enumerate(zip(cuts,cuts[1:])):
        mid=(l+h)/2;uj=list(u)
        for n in active:
            for s in (-1,1):
                pos=mid+s*ells[n]
                if pos.lo>-A.lo and pos.hi<A.lo:uj=plus(uj,shifts[n,s],-cs[n])
                else:assert pos.hi<=-A.hi or pos.lo>=A.hi
        for i,test in enumerate(tests):
            singular=sum((v*(logprims[k,j+1]-logprims[k,j])/2 for k,v in enumerate(products[i])),Z)
            if reverse:
                ru=list(reverse_u[i])
                for n in active:
                    for s in (-1,1):
                        pos=mid+s*ells[n]
                        if pos.lo>-A.lo and pos.hi<A.lo:ru=plus(ru,reverse_shifts[i][n,s],-cs[n])
                        else:assert pos.hi<=-A.hi or pos.lo>=A.hi
                values[i]=values[i]+polyint(conv(ru,p),l,h)-singular
            else:values[i]=values[i]+polyint(conv(uj,test),l,h)-singular
        print('low/selected panel',parity,j,'seconds',round(time.time()-started,1),flush=True)
    values=[2*v for v in values];delta=I(F(550,19))*I(F(106,125))**N;operr=2*A*delta+I('3e-99')
    native=[]
    for v,norm in zip(values,norms):
        error=operr*I(norm);native.append(v+I(error.hi.copy_negate(),error.hi))
    row=next(r for r in json.loads(Path(low).read_bytes())['native_parity_gates'] if r['parity']==parity)
    lo,hi=map(F,row['native_Q_diagonal']);assert F(native[-1].lo)<=hi and lo<=F(native[-1].hi)
    out=dict(stage='DNE29',parity=parity,precision=d['P'],regular_order=N,helper_sha256=hashlib.sha256(source).hexdigest(),
        fixed_columns_sha256=hashlib.sha256(column_bytes).hexdigest(),
        original_low_selected_pairings=[v.data() for v in native[:3]],truncated_low_selected_pairings=[v.data() for v in values[:3]],
        selected_column_norm_upper=list(map(str,norms[:3])),uniform_low_source_operator_error_upper=str(operr.hi),
        independent_original_low_diagonal_replay=native[-1].data(),CC62_low_diagonal_overlap=True,
        all_six_primes_both_orientations_paid=True,exact_endpoint_log_paid=True,half_translation_panels=len(cuts)-1,
        helper_change_only_basis_range_116_to_181=True,sampled_quadrature_used=False,
        whole_aperture_positive=False,RH=False,Lean=False)
    if reverse:out['reverse_source_action_used']=True
    Path(output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'parity':parity,'pairings':[[float(v) for v in q.data()] for q in native[:3]],'elapsed':time.time()-started}))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ['parity','targets','columns','low','helper']:p.add_argument(k)
    p.add_argument('--output',required=True);p.add_argument('--reverse',action='store_true');a=p.parse_args();run(a.parity,a.targets,a.columns,a.low,a.helper,a.output,a.reverse)
