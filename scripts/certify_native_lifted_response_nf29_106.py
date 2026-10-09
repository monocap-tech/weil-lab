#!/usr/bin/env python3
"""NF29: complete original source Gram after a fixed two-high response lift.
Fixed rational midpoint inverses select trials; only paid intervals prove signs.
The two-direction test is not a complete retained-background certificate.
"""
import argparse, gzip, hashlib, json
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import certify_native_high_correction_nf26_106 as base
n=base.n; I=n.I

def run(targets,trial,nf26,nf27,source):
    c,pi=base.constants()
    logs={k:n.ni(n.native.log(k)) for k in (2,3,4,5,7,8)}
    shifts=[(s*logs[k],(logs[2] if k in (4,8) else logs[k])/n.sqrt_r(F(k))) for k in logs for s in (1,-1)]
    cuts=[I(-n.A),I(n.A)]+[I(n.A)-t if t.l>0 else I(-n.A)-t for t,weight in shifts]
    cuts.sort(key=lambda z:z.l);assert all(l.h<u.l for l,u in zip(cuts,cuts[1:]))
    eta_unit=2*n.A*4*F(106,125)**320/(1-F(106,125))+16*(n.A/2)**41/F(factorial(41))
    def Q(i,j):return I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
    result=[]
    for row,y,cv,cw in zip(targets['authenticated_compensated_targets'],trial['parities'],nf26['parity_certificates'],nf27['parity_certificates']):
        parity=row['parity'];assert parity==y['parity']==cv['parity']==cw['parity']
        ids=row['retained_indices'];w=list(map(F,cw['exact_rational_retained_response']))
        hi=row['high_indices'];assert len(hi)==2
        C=[[Q(i,j) for j in hi] for i in hi]
        k=[sum((z*Q(i,j) for i,z in zip(ids,w)),I(0)) for j in hi]
        a,b,d=C[0][0].mid(),C[0][1].mid(),C[1][1].mid();det=a*d-b*b;assert det>0
        raw=[(d*k[0].mid()-b*k[1].mid())/det,(a*k[1].mid()-b*k[0].mid())/det]
        h=[F((z*10**100).__floor__(),10**100) for z in raw]
        whids=ids+hi;whcoeff=w+[-z for z in h]
        assert sum(F(x)*z for x,z in zip(row['retained_coefficients'],w))==0
        vi=ids+hi+y['high_indices']
        vc=list(map(F,row['retained_coefficients']+row['exact_rational_high_compensation']))+[-F(z) for z in y['rational_correction_coefficients']]
        assert len(vi)==len(set(vi)) and sum(z*z for z in vc)<F(1001,1000)**2
        lowv=[I(*map(F,p))-I(*map(F,q)) for p,q in zip(row['low_source_coordinates'],cv['retained_approximant_Ly_coordinates'])]
        lowwh=[sum((z*Q(i,j) for i,z in zip(whids,whcoeff)),I(0)) for j in ids]
        low=[lowv,lowwh]
        mass=[F(1001,1000),F(n.sqrt_r(sum(z*z for z in whcoeff)).h,n.SCALE)]
        roundoff=[8*max(F(z.h-z.l,2*n.SCALE) for z in coords) for coords in low]
        eta=[mass[0]*eta_unit+roundoff[0]+F(cv['correction_norm_upper'])*eta_unit,mass[1]*eta_unit+roundoff[1]]
        poly=[];lp=[];phys=[]
        for ii,coeff,coords in [(vi,vc,lowv),(whids,whcoeff,lowwh)]:
            p,b,l=base.source(ii,coeff,c,parity)
            poly.append(n.add(b,n.scale(n.physical(ids,[z.mid() for z in coords]),-1)));lp.append(l);phys.append(p)
        print(parity,'constructed fixed lifted sources',flush=True)
        M,ML,ML2,cm=n.moments(cuts,2*max(len(p)-1 for p in poly),c,pi)
        shifted=[[n.scale(n.shifted(p,t),-weight) for t,weight in shifts] for p in phys]
        cells=[]
        for L,U in zip(cuts,cuts[1:]):
            mid=F(L.h+U.l,2*n.SCALE);active=[]
            for j,(t,weight) in enumerate(shifts):
                z=I(mid)+t;inside=-n.A<F(z.l,n.SCALE) and F(z.h,n.SCALE)<n.A
                outside=F(z.h,n.SCALE)<-n.A or F(z.l,n.SCALE)>n.A;assert inside or outside
                if inside:active.append(j)
            cells.append([base.sum_polys([sp[j] for j in active]) for sp in shifted])
        def pairing(i,test):
            value=n.dot(poly[i],test,M)+n.dot(lp[i],test,ML)
            for pp,(mp,ml) in zip(cells,cm):value+=n.dot(pp[i],test,mp)
            return value
        # h is high, hence retained subtraction does not change this pairing.
        hp=n.physical(hi,h);hm=F(n.sqrt_r(sum(z*z for z in h)).h,n.SCALE)
        vh=pairing(0,hp)+I(-mass[0]*eta_unit*hm,mass[0]*eta_unit*hm)
        vw=sum((z*b for z,b in zip(w,lowv)),I(0))
        e=eta_unit*F(cv['correction_norm_upper'])*mass[1];vw+=I(-e,e)
        qwh=sum((z*t*Q(i,j) for i,z in zip(whids,whcoeff) for j,t in zip(whids,whcoeff)),I(0))
        qv=I(*map(F,cv['corrected_native_energy']));qmix=vw-vh
        energy=[[qv,qmix],[qmix,qwh]]
        assert qwh.l>0 and (qv*qwh-n.sq(qmix)).l>0
        gram=[[I(0),I(0)],[I(0),I(0)]]
        for i in range(2):
            for j in range(i,2):
                value=n.dot(poly[i],poly[j],M)+n.dot(poly[i],lp[j],ML)+n.dot(lp[i],poly[j],ML)+n.dot(lp[i],lp[j],ML2)
                for pp,(mp,ml) in zip(cells,cm):value+=n.dot(poly[i],pp[j],mp)+n.dot(pp[i],poly[j],mp)+n.dot(pp[i],pp[j],mp)+n.dot(lp[i],pp[j],ml)+n.dot(pp[i],lp[j],ml)
                gram[i][j]=gram[j][i]=value
                print(parity,'integrated lifted Gram',i,j,flush=True)
        assert all(gram[i][i].l>0 for i in range(2))
        norms=[F(n.sqrt_r(F(gram[i][i].h,n.SCALE)).h,n.SCALE) for i in range(2)]
        errors=[[eta[i]*norms[j]+eta[j]*norms[i]+eta[i]*eta[j] for j in range(2)] for i in range(2)]
        original=[[gram[i][j]+I(-errors[i][j],errors[i][j]) for j in range(2)] for i in range(2)]
        assert (original[0][0]*original[1][1]-n.sq(original[0][1])).l>0
        oldv=I(*map(F,cv['complete_original_corrected_residual_square']))
        assert original[0][0].l<=oldv.h and original[0][0].h>=oldv.l
        score=[[energy[i][j]-original[i][j]/F(207,1000) for j in range(2)] for i in range(2)]
        determinant=score[0][0]*score[1][1]-n.sq(score[0][1])
        status='PASS' if min(score[0][0].l,score[1][1].l,determinant.l)>0 else 'UNRESOLVED'
        if score[0][0].h<0 or score[1][1].h<0 or determinant.h<0:status='SUFFICIENT_MATRIX_REJECTED'
        shell=[sum((z*Q(i,j) for i,z in zip(whids,whcoeff)),I(0)) for j in hi]
        print(parity,status,'lifted response ratio',float(F((original[1][1]/qwh).l,n.SCALE)),float(F((original[1][1]/qwh).h,n.SCALE)),flush=True)
        result.append(dict(parity=parity,high_lift_indices=hi,fixed_rational_high_lift=list(map(str,h)),lifted_response_retained_component_unchanged=True,
            lifted_response_norm_squared=str(sum(z*z for z in whcoeff)),lifted_response_measured_high_coordinates=[z.ends() for z in shell],
            original_finite_energy_Gram=[[z.ends() for z in r] for r in energy],original_native_v_high_lift_pairing=vh.ends(),
            reconstructed_residual_Gram=[[z.ends() for z in r] for r in gram],physical_source_error_bounds=list(map(str,eta)),
            source_Gram_entrywise_error_bounds=[[str(e) for e in r] for r in errors],original_complete_residual_Gram=[[z.ends() for z in r] for r in original],
            sufficient_collective_matrix=[[z.ends() for z in r] for r in score],sufficient_matrix_determinant=determinant.ends(),
            lifted_response_residual_square_over_energy=(original[1][1]/qwh).ends(),sufficient_collective_test_status=status,
            NF26_source_square_overlap=True,actual_negative_vector_claimed=False,full_retained_background_certified=False))
    return dict(milestone='NF29',aperture='53/50',interval_grid_digits=500,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        complete_lifted_two_direction_source_Gram_certified=True,parity_certificates=result,whole_aperture_positive=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    paths=['notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json','notes/data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json','notes/data/RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json','notes/data/RPB108_NF27_RETAINED_COUPLING_CERTIFICATE_20261009.json','nf24-inputs/Weil/native112_N720_K620.json.gz','nf24-inputs/Weil/native_boundary_columns_112_113.json.gz','nf24-inputs/Weil/native_boundary_114_115.json.gz']
    raw=[Path(p).read_bytes() for p in paths];raw[4:]=[gzip.decompress(b) for b in raw[4:]]
    hashes=[hashlib.sha256(b).hexdigest() for b in raw]
    assert hashes==['6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','814fe0fcc3aff4eecbe4e6c6eead5ce28927043877c0df9cfa03e3a5c71c2336','f2010510bacac64c45ef1825cd5e2c41e395519417815a43530e44e6cfdbf930','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42','f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81','da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee','0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad']
    data=list(map(json.loads,raw));source={**data[4]['complete_form'],**data[5]['original_full_source'],**data[6]['original_full_source']}
    out=run(*data[:4],source);out['authenticated_input_sha256']=hashes
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
