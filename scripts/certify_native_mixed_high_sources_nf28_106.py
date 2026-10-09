#!/usr/bin/env python3
"""NF28: complete original high residual Gram of NF26 v and NF27 w.
Only a two-direction collective test; full retained assembly remains open.
"""
import argparse,json,gzip,hashlib
from fractions import Fraction as F
from math import factorial
import certify_native_high_correction_nf26_106 as base
n=base.n;I=n.I

def run(targets,trial,nf26,nf27,native):
    c,pi=base.constants();powers=(2,3,4,5,7,8)
    logs={k:n.ni(n.native.log(k)) for k in powers}
    shifts=[(s*logs[k],(logs[2] if k in (4,8) else logs[k])/n.sqrt_r(F(k))) for k in powers for s in (1,-1)]
    cuts=[I(-n.A),I(n.A)]+[I(n.A)-t if t.l>0 else I(-n.A)-t for t,w in shifts]
    cuts.sort(key=lambda z:z.l);assert all(l.h<u.l for l,u in zip(cuts,cuts[1:]))
    epsilon=4*F(106,125)**320/(1-F(106,125));eta_unit=2*n.A*epsilon+16*(n.A/2)**41/F(factorial(41))
    out=[]
    for row,y,cv,cw in zip(targets['authenticated_compensated_targets'],trial['parities'],nf26['parity_certificates'],nf27['parity_certificates']):
        parity=row['parity'];assert y['parity']==cv['parity']==cw['parity']==parity
        ids=row['retained_indices'];w=list(map(F,cw['exact_rational_retained_response']))
        assert sum(F(x)*z for x,z in zip(row['retained_coefficients'],w))==0
        vi=ids+row['high_indices']+y['high_indices']
        vc=list(map(F,row['retained_coefficients']+row['exact_rational_high_compensation']))+[-F(z) for z in y['rational_correction_coefficients']]
        assert len(vi)==len(set(vi))
        masses=[F(1001,1000),F(n.sqrt_r(sum(z*z for z in w)).h,n.SCALE)]
        assert sum(z*z for z in vc)<masses[0]**2
        lowp=[I(*map(F,z)) for z in row['low_source_coordinates']]
        lowy=[I(*map(F,z)) for z in cv['retained_approximant_Ly_coordinates']]
        lowv=[p-y for p,y in zip(lowp,lowy)]
        def Q(i,j):return I(*map(F,native[f'{min(i,j)},{max(i,j)}']['full']))
        loww=[sum((z*Q(i,j) for i,z in zip(ids,w)),I(0)) for j in ids]
        low=[lowv,loww]
        radii=[8*max(F(z.h-z.l,2*n.SCALE) for z in coords) for coords in low]
        eta=[masses[0]*eta_unit+radii[0]+F(cv['correction_norm_upper'])*eta_unit,masses[1]*eta_unit+radii[1]]
        poly=[];lp=[];phys=[]
        for ii,coeff,coords in [(vi,vc,lowv),(ids,w,loww)]:
            p,b,l=base.source(ii,coeff,c,parity)
            poly.append(n.add(b,n.scale(n.physical(ids,[z.mid() for z in coords]),-1)));lp.append(l);phys.append(p)
        print(parity,'constructed both complete sources',flush=True)
        degree=2*max(len(p)-1 for p in poly)
        M,ML,ML2,cm=n.moments(cuts,degree,c,pi)
        cells=[]
        shifted=[[n.scale(n.shifted(p,t),-weight) for t,weight in shifts] for p in phys]
        for L,U in zip(cuts,cuts[1:]):
            mid=F(L.h+U.l,2*n.SCALE);active=[]
            for k,(t,weight) in enumerate(shifts):
                z=I(mid)+t;inside=-n.A<F(z.l,n.SCALE) and F(z.h,n.SCALE)<n.A
                outside=F(z.h,n.SCALE)<-n.A or F(z.l,n.SCALE)>n.A
                assert inside or outside
                if inside:active.append(k)
            cells.append([base.sum_polys([sp[k] for k in active]) for sp in shifted])
        print(parity,'constructed thirteen cells and exact log moments',flush=True)
        gram=[[I(0),I(0)],[I(0),I(0)]]
        for i in range(2):
            for j in range(i,2):
                value=n.dot(poly[i],poly[j],M)+n.dot(poly[i],lp[j],ML)+n.dot(lp[i],poly[j],ML)+n.dot(lp[i],lp[j],ML2)
                for pp,(mp,ml) in zip(cells,cm):value+=n.dot(poly[i],pp[j],mp)+n.dot(pp[i],poly[j],mp)+n.dot(pp[i],pp[j],mp)+n.dot(lp[i],pp[j],ml)+n.dot(pp[i],lp[j],ml)
                gram[i][j]=gram[j][i]=value
                print(parity,'integrated mixed Gram',i,j,flush=True)
        assert all(gram[i][i].l>0 for i in range(2))
        norms=[F(n.sqrt_r(F(gram[i][i].h,n.SCALE)).h,n.SCALE) for i in range(2)]
        errors=[[eta[i]*norms[j]+eta[j]*norms[i]+eta[i]*eta[j] for j in range(2)] for i in range(2)]
        original=[[gram[i][j]+I(-errors[i][j],errors[i][j]) for j in range(2)] for i in range(2)]
        oldv=I(*map(F,cv['complete_original_corrected_residual_square']))
        assert original[0][0].l<=oldv.h and original[0][0].h>=oldv.l
        qv=I(*map(F,cv['corrected_native_energy']))
        qvw=sum((z*b for z,b in zip(w,lowv)),I(0))
        mixed_error=eta_unit*F(cv['correction_norm_upper'])*masses[1]
        qvw+=I(-mixed_error,mixed_error)
        qww=sum((z*b for z,b in zip(w,loww)),I(0))
        energy=[[qv,qvw],[qvw,qww]]
        native_det=qv*qww-n.sq(qvw);assert qww.l>0 and native_det.l>0
        score=[[energy[i][j]-original[i][j]/F(207,1000) for j in range(2)] for i in range(2)]
        det=score[0][0]*score[1][1]-n.sq(score[0][1])
        status='PASS' if score[0][0].l>0 and score[1][1].l>0 and det.l>0 else 'UNRESOLVED'
        if score[1][1].h<0 or det.h<0:status='SUFFICIENT_MATRIX_REJECTED'
        print(parity,status,'w residual / energy',float(F((original[1][1]/qww).l,n.SCALE)),float(F((original[1][1]/qww).h,n.SCALE)),flush=True)
        out.append(dict(parity=parity,source_order=['NF26_v','NF27_exact_w'],physical_source_error_bounds=list(map(str,eta)),
            reconstructed_mixed_residual_Gram=[[v.ends() for v in r] for r in gram],entrywise_source_Gram_errors=[[str(e) for e in r] for r in errors],
            original_complete_mixed_residual_Gram=[[v.ends() for v in r] for r in original],NF26_source_square_replay_overlap=True,
            original_finite_two_direction_energy=[[v.ends() for v in r] for r in energy],native_energy_determinant=native_det.ends(),
            sufficient_collective_matrix=[[v.ends() for v in r] for r in score],sufficient_matrix_determinant=det.ends(),
            retained_response_residual_square_over_native_energy=(original[1][1]/qww).ends(),
            sufficient_collective_test_status=status,actual_negative_vector_claimed=False,
            full_55_direction_retained_background_certified=False,whole_aperture_positive=False))
    return dict(milestone='NF28',aperture='53/50',regular_kernel_N=320,interval_grid_digits=500,original_translation_cells=13,
        complete_original_two_direction_high_Gram_certified=True,parity_certificates=out,
        whole_aperture_positive=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('targets');a.add_argument('trial');a.add_argument('nf26');a.add_argument('nf27');a.add_argument('native');a.add_argument('--output',required=True);a=a.parse_args()
    paths=[a.targets,a.trial,a.nf26,a.nf27,a.native];raw=[open(p,'rb').read() for p in paths];raw[-1]=gzip.decompress(raw[-1])
    expected=['6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','814fe0fcc3aff4eecbe4e6c6eead5ce28927043877c0df9cfa03e3a5c71c2336','f2010510bacac64c45ef1825cd5e2c41e395519417815a43530e44e6cfdbf930','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42','f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81']
    for b,s in zip(raw,expected):
        if s is not None:assert hashlib.sha256(b).hexdigest()==s
    data=list(map(json.loads,raw));result=run(*data[:-1],data[-1]['complete_form']);result['input_sha256']=[hashlib.sha256(b).hexdigest() for b in raw]
    open(a.output,'w').write(json.dumps(result,indent=2)+'\n')
