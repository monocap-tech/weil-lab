#!/usr/bin/env python3
"""NF30: fixed additional high correction of the NF29 even response.
Selection and proof are separate commands; original errors are always paid.
"""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import certify_native_high_correction_nf26_106 as base
n=base.n;I=n.I
PATHS=['notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json','notes/data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json','notes/data/RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json','notes/data/RPB108_NF27_RETAINED_COUPLING_CERTIFICATE_20261009.json','notes/data/RPB108_NF29_LIFTED_RESPONSE_CERTIFICATE_20261009.json']
HASHES=['6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','814fe0fcc3aff4eecbe4e6c6eead5ce28927043877c0df9cfa03e3a5c71c2336','f2010510bacac64c45ef1825cd5e2c41e395519417815a43530e44e6cfdbf930','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42','069d4acc267a0ac48154427a033cccca96243743dd31e36449f7189de03e895a']

def inputs():
    raw=[Path(p).read_bytes() for p in PATHS]
    assert [hashlib.sha256(b).hexdigest() for b in raw]==HASHES
    return list(map(json.loads,raw))

class Moments:
    def __init__(self,degree):
        self.c,pi=base.constants();logs={k:n.ni(n.native.log(k)) for k in (2,3,4,5,7,8)}
        self.shifts=[(s*logs[k],(logs[2] if k in (4,8) else logs[k])/n.sqrt_r(F(k))) for k in logs for s in (1,-1)]
        cuts=[I(-n.A),I(n.A)]+[I(n.A)-t if t.l>0 else I(-n.A)-t for t,w in self.shifts]
        cuts.sort(key=lambda z:z.l);assert all(l.h<u.l for l,u in zip(cuts,cuts[1:]))
        self.active=[]
        for L,U in zip(cuts,cuts[1:]):
            mid=F(L.h+U.l,2*n.SCALE);active=[]
            for j,(t,w) in enumerate(self.shifts):
                z=I(mid)+t;inside=-n.A<F(z.l,n.SCALE) and F(z.h,n.SCALE)<n.A
                outside=F(z.h,n.SCALE)<-n.A or F(z.l,n.SCALE)>n.A;assert inside or outside
                if inside:active.append(j)
            self.active.append(active)
        self.M,self.ML,self.ML2,self.cm=n.moments(cuts,degree,self.c,pi)
        self.eta=2*n.A*4*F(106,125)**320/(1-F(106,125))+16*(n.A/2)**41/F(factorial(41))
    def source(self,ids,coeff):
        p,b,l=base.source(ids,coeff,self.c,'even')
        shifted=[n.scale(n.shifted(p,t),-w) for t,w in self.shifts]
        cells=[base.sum_polys([shifted[j] for j in a]) for a in self.active]
        return p,b,l,cells
    def pair(self,s,test):
        p,b,l,cells=s;v=n.dot(b,test,self.M)+n.dot(l,test,self.ML)
        for prime,(mp,ml) in zip(cells,self.cm):v+=n.dot(prime,test,mp)
        return v
    def gram(self,s,t):
        p,b,l,cells=s;pp,bb,ll,cc=t
        v=n.dot(b,bb,self.M)+n.dot(b,ll,self.ML)+n.dot(l,bb,self.ML)+n.dot(l,ll,self.ML2)
        for a,d,(mp,ml) in zip(cells,cc,self.cm):v+=n.dot(b,d,mp)+n.dot(a,bb,mp)+n.dot(a,d,mp)+n.dot(l,d,ml)+n.dot(a,ll,ml)
        return v

def even(data):
    targets,trial,nf26,nf27,nf29=data
    r,y,cv,cw,ch=[d[k][0] for d,k in zip(data,['authenticated_compensated_targets','parities','parity_certificates','parity_certificates','parity_certificates'])]
    assert all(d['parity']=='even' for d in (r,y,cv,cw,ch))
    wi=r['retained_indices']+ch['high_lift_indices']
    wc=list(map(F,cw['exact_rational_retained_response']))+[-F(z) for z in ch['fixed_rational_high_lift']]
    vi=r['retained_indices']+r['high_indices']+y['high_indices']
    vc=list(map(F,r['retained_coefficients']+r['exact_rational_high_compensation']))+[-F(z) for z in y['rational_correction_coefficients']]
    assert sum(z*z for z in vc)<F(1001,1000)**2
    return r,cv,ch,wi,wc,vi,vc

def choose(data):
    r,cv,ch,wi,wc,vi,vc=even(data);m=Moments(720);s=m.source(wi,wc)
    zi=list(range(116,181,2));coordinates=[m.pair(s,n.basis(i)) for i in zi]
    zc=[F((v.mid()/4*10**100).__floor__(),10**100) for v in coordinates]
    e=m.eta*F(n.sqrt_r(sum(v*v for v in wc)).h,n.SCALE)
    paid=[v+I(-e,e) for v in coordinates]
    captured=sum((n.sq(v) for v in paid),I(0));old=I(*map(F,ch['original_complete_residual_Gram'][1][1]))
    print('certified selected-shell square / full square',float(F((captured/old).l,n.SCALE)),float(F((captured/old).h,n.SCALE)),flush=True)
    return dict(milestone='NF30',parity='even',additional_high_indices=zi,fixed_rational_coefficients=list(map(str,zc)),
        selection_rule='NF29 even response source coordinates / 4; downward rounded denominator 10^100',
        reconstructed_selection_coordinates=[v.ends() for v in coordinates],paid_original_selection_coordinates=[v.ends() for v in paid],
        selected_shell_square=captured.ends(),selected_shell_fraction_of_NF29_source_square=(captured/old).ends(),authenticated_input_sha256=HASHES,
        selection_alone_is_not_a_sign_certificate=True)

def subtract(s,t):
    return (n.add(s[0],n.scale(t[0],-1)),n.add(s[1],n.scale(t[1],-1)),n.add(s[2],n.scale(t[2],-1)),[n.add(a,n.scale(b,-1)) for a,b in zip(s[3],t[3])])

def run(data,trial):
    assert trial['authenticated_input_sha256']==HASHES and trial['parity']=='even'
    r,cv,ch,wi,wc,vi,vc=even(data);zi=trial['additional_high_indices'];zc=list(map(F,trial['fixed_rational_coefficients']))
    assert len(zi)==len(set(zi))==len(zc) and all(i>=116 and i%2==0 for i in zi)
    assert max(zi)<=180
    m=Moments(1020);sw=m.source(wi,wc);sz=m.source(zi,zc);sv=m.source(vi,vc)
    print('constructed three complete even sources',flush=True)
    wm=F(n.sqrt_r(sum(z*z for z in wc)).h,n.SCALE);zm=F(n.sqrt_r(sum(z*z for z in zc)).h,n.SCALE)
    wz=m.pair(sw,sz[0])+I(-m.eta*wm*zm,m.eta*wm*zm)
    zz=m.pair(sz,sz[0])+I(-m.eta*zm*zm,m.eta*zm*zm)
    vz=m.pair(sv,sz[0])+I(-F(1001,1000)*m.eta*zm,F(1001,1000)*m.eta*zm)
    reverse_wz=m.pair(sz,sw[0])+I(-m.eta*wm*zm,m.eta*wm*zm)
    reverse_vz=m.pair(sz,sv[0])+I(-F(1001,1000)*m.eta*zm,F(1001,1000)*m.eta*zm)
    assert wz.l<=reverse_wz.h and wz.h>=reverse_wz.l
    assert vz.l<=reverse_vz.h and vz.h>=reverse_vz.l
    q0=I(*map(F,ch['original_finite_energy_Gram'][1][1]));q=q0-2*wz+zz
    qv=I(*map(F,ch['original_finite_energy_Gram'][0][0]));mix=I(*map(F,ch['original_finite_energy_Gram'][0][1]))-vz
    assert q.l>0 and (qv*q-n.sq(mix)).l>0
    # Original Lw_h retained coordinates are recovered from original signed
    # native entries, not the approximate Lw_h source at unit retained mass.
    import gzip
    source={}
    for path,key,sha in [('nf24-inputs/Weil/native112_N720_K620.json.gz','complete_form','f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'),('nf24-inputs/Weil/native_boundary_columns_112_113.json.gz','original_full_source','da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee'),('nf24-inputs/Weil/native_boundary_114_115.json.gz','original_full_source','0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad')]:
        raw=gzip.decompress(Path(path).read_bytes());assert hashlib.sha256(raw).hexdigest()==sha;source.update(json.loads(raw)[key])
    def Q(i,j):return I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
    loww=[sum((z*Q(i,j) for i,z in zip(wi,wc)),I(0)) for j in r['retained_indices']]
    lowz=[m.pair(sz,n.basis(i)) for i in r['retained_indices']]
    lowv=[I(*map(F,p))-I(*map(F,y)) for p,y in zip(r['low_source_coordinates'],cv['retained_approximant_Ly_coordinates'])]
    low=[lowv,[a-b for a,b in zip(loww,lowz)]]
    residual=[sv,subtract(sw,sz)]
    rounding=[8*max(F(z.h-z.l,2*n.SCALE) for z in row) for row in low]
    for j in range(2):
        p,b,l,cells=residual[j];residual[j]=(p,n.add(b,n.scale(n.physical(r['retained_indices'],[v.mid() for v in low[j]]),-1)),l,cells)
    eta=[F(1001,1000)*m.eta+F(cv['correction_norm_upper'])*m.eta+rounding[0],(wm+2*zm)*m.eta+rounding[1]]
    gram=[[I(0),I(0)],[I(0),I(0)]]
    for i in range(2):
        for j in range(i,2):
            gram[i][j]=gram[j][i]=m.gram(residual[i],residual[j]);print('integrated expanded Gram',i,j,flush=True)
    assert min(gram[0][0].l,gram[1][1].l)>0
    norms=[F(n.sqrt_r(F(gram[i][i].h,n.SCALE)).h,n.SCALE) for i in range(2)]
    errors=[[eta[i]*norms[j]+eta[j]*norms[i]+eta[i]*eta[j] for j in range(2)] for i in range(2)]
    true=[[gram[i][j]+I(-errors[i][j],errors[i][j]) for j in range(2)] for i in range(2)]
    old=I(*map(F,ch['original_complete_residual_Gram'][0][0]));assert true[0][0].l<=old.h and true[0][0].h>=old.l
    assert (true[0][0]*true[1][1]-n.sq(true[0][1])).l>0
    energy=[[qv,mix],[mix,q]];score=[[energy[i][j]-true[i][j]/F(207,1000) for j in range(2)] for i in range(2)]
    det=score[0][0]*score[1][1]-n.sq(score[0][1])
    status='PASS' if min(score[0][0].l,score[1][1].l,det.l)>0 else 'UNRESOLVED'
    if score[1][1].h<0 or det.h<0:status='SUFFICIENT_MATRIX_REJECTED'
    print(status,'expanded response ratio',float(F((true[1][1]/q).l,n.SCALE)),float(F((true[1][1]/q).h,n.SCALE)),flush=True)
    out=dict(milestone='NF30',aperture='53/50',parity='even',interval_grid_digits=500,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        authenticated_input_sha256=HASHES,original_wh_z_pairing=wz.ends(),original_z_energy=zz.ends(),original_v_z_pairing=vz.ends(),
        transpose_z_wh_pairing=reverse_wz.ends(),transpose_z_v_pairing=reverse_vz.ends(),paid_bilinear_symmetry_checks=True,
        original_finite_energy_Gram=[[z.ends() for z in row] for row in energy],retained_approximant_Lz_coordinates=[v.ends() for v in lowz],
        reconstructed_residual_Gram=[[z.ends() for z in row] for row in gram],physical_residual_error_bounds=list(map(str,eta)),
        entrywise_source_Gram_errors=[[str(z) for z in row] for row in errors],original_complete_residual_Gram=[[z.ends() for z in row] for row in true],
        sufficient_collective_matrix=[[z.ends() for z in row] for row in score],sufficient_matrix_determinant=det.ends(),
        expanded_response_square_over_energy=(true[1][1]/q).ends(),sufficient_collective_test_status=status,
        retained_components_unchanged=True,NF29_odd_block_unchanged=True,NF29_v_source_square_overlap=True,
        full_retained_background_certified=False,whole_aperture_positive=False,actual_negative_vector_claimed=False,RH=False,F4=False,Lean=False)
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['choose','certify']);p.add_argument('--trial');p.add_argument('--output',required=True);a=p.parse_args()
    data=inputs()
    if a.mode=='choose':out=choose(data)
    else:
        raw=Path(a.trial).read_bytes();out=run(data,json.loads(raw));out['fixed_trial_sha256']=hashlib.sha256(raw).hexdigest()
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
