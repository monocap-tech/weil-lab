#!/usr/bin/env python3
"""NF29 independent signed native projection and finite-energy checks."""
import argparse,base64,gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import check_native_mixed_projection_nf28_106 as checker
n=checker.n;I=n.I

def run(certificate):
    paths=['notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json','notes/data/RPB108_NF27_RETAINED_COUPLING_CERTIFICATE_20261009.json','notes/data/RPB108_NF24_NATIVE_RESIDUAL_PROJECTIONS_117_118_20261009.json.gz.b64']
    raw=[Path(p).read_bytes() for p in paths];raw[2]=gzip.decompress(base64.b64decode(raw[2]))
    hashes=[hashlib.sha256(b).hexdigest() for b in raw]
    assert hashes==['6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42','4c8b0067088486e20f31a7904d3bf56a9f654e982b15450efa85cd6b25e24346']
    targets,nf27,projection=map(json.loads,raw)
    trialraw=Path('notes/data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json').read_bytes()
    assert hashlib.sha256(trialraw).hexdigest()==certificate['authenticated_input_sha256'][1]
    trial=json.loads(trialraw)
    source={}
    for path,key in [('nf24-inputs/Weil/native112_N720_K620.json.gz','complete_form'),('nf24-inputs/Weil/native_boundary_columns_112_113.json.gz','original_full_source'),('nf24-inputs/Weil/native_boundary_114_115.json.gz','original_full_source')]:
        b=gzip.decompress(Path(path).read_bytes());assert hashlib.sha256(b).hexdigest() in certificate['authenticated_input_sha256'];source.update(json.loads(b)[key])
    def Q(i,j):return I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
    energy_checks=[];mixed_checks=[]
    c,pi=checker.base.constants()
    logs={k:n.ni(n.native.log(k)) for k in (2,3,4,5,7,8)}
    shifts=[(s*logs[k],(logs[2] if k in (4,8) else logs[k])/n.sqrt_r(F(k))) for k in logs for s in (1,-1)]
    cuts=[I(-n.A),I(n.A)]+[I(n.A)-t if t.l>0 else I(-n.A)-t for t,weight in shifts]
    cuts.sort(key=lambda z:z.l)
    eta_unit=2*n.A*4*F(106,125)**320/(1-F(106,125))+16*(n.A/2)**41/F(factorial(41))
    for row,wc,cc,y in zip(targets['authenticated_compensated_targets'],nf27['parity_certificates'],certificate['parity_certificates'],trial['parities']):
        assert row['parity']==wc['parity']==cc['parity']
        ids=row['retained_indices'];w=list(map(F,wc['exact_rational_retained_response']))
        hi=cc['high_lift_indices'];h=list(map(F,cc['fixed_rational_high_lift']))
        original=sum((z*t*Q(i,j) for i,z in zip(ids,w) for j,t in zip(ids,w)),I(0))
        cross=sum((z*t*Q(i,j) for i,z in zip(ids,w) for j,t in zip(hi,h)),I(0))
        correction=sum((z*t*Q(i,j) for i,z in zip(hi,h) for j,t in zip(hi,h)),I(0))
        independent=original-2*cross+correction
        reported=I(*map(F,cc['original_finite_energy_Gram'][1][1]))
        assert independent.l<=reported.h and independent.h>=reported.l
        assert independent.l>0 and (2*cross-correction).l>0
        energy_checks.append(dict(parity=row['parity'],independent_expanded_lift_energy=independent.ends(),producer_energy_overlap=True,
            removed_native_energy=(2*cross-correction).ends(),removed_fraction=((2*cross-correction)/original).ends()))
        # Independent mixed-energy route: original native Q(p,h) minus
        # reconstructed Q(y,h). Both small factors enter the paid y error.
        yc=list(map(F,y['rational_correction_coefficients']))
        p,b,l=checker.base.source(y['high_indices'],yc,c,row['parity'])
        test=n.physical(hi,h);M,ML,ML2,cm=n.moments(cuts,len(b)+len(test),c,pi)
        yh=n.dot(b,test,M)+n.dot(l,test,ML)
        shifted=[n.scale(n.shifted(p,t),-weight) for t,weight in shifts]
        for (L,U),(mp,ml) in zip(zip(cuts,cuts[1:]),cm):
            mid=F(L.h+U.l,2*n.SCALE);active=[]
            for j,(t,weight) in enumerate(shifts):
                z=I(mid)+t;inside=-n.A<F(z.l,n.SCALE) and F(z.h,n.SCALE)<n.A
                outside=F(z.h,n.SCALE)<-n.A or F(z.l,n.SCALE)>n.A;assert inside or outside
                if inside:active.append(j)
            yh+=n.dot(checker.base.sum_polys([shifted[j] for j in active]),test,mp)
        ym=F(n.sqrt_r(sum(z*z for z in yc)).h,n.SCALE);hm=F(n.sqrt_r(sum(z*z for z in h)).h,n.SCALE)
        yh+=I(-eta_unit*ym*hm,eta_unit*ym*hm)
        ph=sum((z*I(*map(F,v)) for z,v in zip(h,row['measured_high_source_coordinates'])),I(0))
        independent_vh=ph-yh;producer_vh=I(*map(F,cc['original_native_v_high_lift_pairing']))
        assert independent_vh.l<=producer_vh.h and independent_vh.h>=producer_vh.l
        mixed_checks.append(dict(parity=row['parity'],original_native_p_high_pairing=ph.ends(),paid_y_high_pairing=yh.ends(),independent_v_high_pairing=independent_vh.ends(),producer_mixed_energy_overlap=True))
        print(row['parity'],'independent mixed-energy decomposition passed',flush=True)
        # The existing independent checker accepts an arbitrary coefficient
        # list. Its signed oracle includes original entries through degree115.
        row['retained_indices']=ids+hi
        wc['exact_rational_retained_response']=list(map(str,w+[-z for z in h]))
    out=checker.run(targets,nf27,projection['complete_original_signed_source'])
    out['milestone']='NF29';out['input_sha256']=hashes;out['independent_finite_energy_checks']=energy_checks
    out['independent_mixed_energy_checks']=mixed_checks
    for cc in certificate['parity_certificates']:
        u=[[I(*map(F,z)) for z in r] for r in cc['sufficient_collective_matrix']]
        determinant=u[0][0]*u[1][1]-n.sq(u[0][1])
        advertised=I(*map(F,cc['sufficient_matrix_determinant']))
        assert determinant.ends()==advertised.ends()
        status=cc['sufficient_collective_test_status']
        if status=='PASS':assert min(u[0][0].l,u[1][1].l,determinant.l)>0
        elif status=='SUFFICIENT_MATRIX_REJECTED':assert u[0][0].h<0 or u[1][1].h<0 or determinant.h<0
    out['sufficient_matrix_signs_independently_rechecked']=True
    controls=[]
    for b in (F(99,100),F(1),F(101,100)):
        schur=1-b*b;fixed=2-2*b
        assert fixed-schur==(1-b)**2
        controls.append(dict(mixed=str(b),exact_Schur=str(schur),fixed_lift_energy=str(fixed),optimization_gap=str((1-b)**2)))
    out['exact_positive_zero_negative_lift_controls']=controls
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('certificate');p.add_argument('--output',required=True);a=p.parse_args()
    raw=Path(a.certificate).read_bytes();out=run(json.loads(raw));out['certificate_sha256']=hashlib.sha256(raw).hexdigest()
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
