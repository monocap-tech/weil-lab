#!/usr/bin/env python3
"""NF35 complete signed source crosses and original joined floor matrices."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import certify_native_expanded_shared_lift_nf34_106 as prev
n=prev.n;I=n.I;dot=prev.dot;iv=prev.iv
ROOT34='notes/data/RPB108_NF34_'
SUFFIX34=['EVEN_FIXED_EXPANDED_SHARED_LIFT','ODD_FIXED_EXPANDED_SHARED_LIFT','EVEN_EXPANDED_SHARED_LIFT_CERTIFICATE','ODD_EXPANDED_SHARED_LIFT_CERTIFICATE','EXPANDED_SHARED_LIFT_VALIDATION']
SHA34=['4fa44e021ffd3b408703911c2b4d222c30bde1ac70581eafae81d5d3fbc589a2','5080c348c39f870fe554609ded27748326078f6bd944794ec5f80862e6aaa73c','7327c2f3d89327ed1cef95404646c059c3ded4d4881486b1b3beb15651337d4f','17ae9ec6757cd29443fc77af28b86fb3d4b7f9449317886c5aec75bf92a9fb89','077d1916d44c88396aae4b993f745afd0b5c46b7ba7d6b8591b2895ed008268a']
def parents34():
    raw=[Path(ROOT34+p+'_20261009.json').read_bytes() for p in SUFFIX34]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==SHA34
    out=list(map(json.loads,raw));assert out[-1]['status']=='PASS';return out
def det3(a):
    return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def sign_packet(q,g,masses):
    U=[[q[i][j]-g[i][j]/F(207,1000) for j in range(3)] for i in range(3)]
    d2=U[0][0]*U[1][1]-n.sq(U[0][1]);assert U[0][0].l>0 and d2.l>0
    b0,b1=U[0][2],U[1][2]
    reaction=(U[1][1]*n.sq(b0)-2*U[0][1]*b0*b1+U[0][0]*n.sq(b1))/d2
    margin=U[2][2]-reaction;det=det3(U)
    nd=det3(q);assert q[0][0].l>0 and (q[0][0]*q[1][1]-n.sq(q[0][1])).l>0 and nd.l>0
    status='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS' if margin.l>0 and det.l>0 else 'JOINED_FLOOR_REJECTED' if margin.h<0 and det.h<0 else 'UNRESOLVED'
    extra={}
    if status=='JOINED_THREE_RETAINED_PLUS_ALL_F_PASS':
        inv,proof=prev.old.prev.matrix.inverse(U)
        trace=sum((inv[i][i]*masses[i] for i in range(3)),I(0));assert trace.l>0
        extra=dict(positive_inverse_verification=proof,physical_retained_Schur_gap_lower=str(1/F(trace.h,n.SCALE)))
    elif status=='JOINED_FLOOR_REJECTED':
        a,c,d=U[0][0].mid(),U[0][1].mid(),U[1][1].mid();b,e=b0.mid(),b1.mid();de=a*d-c*c
        coeff=[-F((v*10**100).__floor__(),10**100) for v in [(d*b-c*e)/de,(a*e-c*b)/de]]+[F(1)]
        value=dot(coeff,prev.mv(U,coeff));native=dot(coeff,prev.mv(q,coeff));assert value.h<0 and native.l>0
        extra=dict(fixed_rational_mixed_floor_witness=list(map(str,coeff)),mixed_witness_floor_value=value.ends(),mixed_witness_native_energy=native.ends())
    return dict(sufficient_matrix=[[v.ends() for v in row] for row in U],leading_pair_sufficient_determinant=d2.ends(),
        joined_sufficient_determinant=det.ends(),joined_floor_reaction=reaction.ends(),joined_condensed_margin=margin.ends(),
        joined_native_energy_determinant=nd.ends(),joined_status=status,**extra)

def objects(data,source,parity):
    idx=['even','odd'].index(parity);r=data[0]['authenticated_compensated_targets'][idx];cv=data[1]['parity_certificates'][idx]
    cw=data[2]['parity_certificates'][idx];ch=data[3]['parity_certificates'][idx]
    ids=r['retained_indices'];w=list(map(F,cw['exact_rational_retained_response']));h=ch['high_lift_indices']
    raw=Path('notes/data/RPB108_NF26_FIXED_HIGH_CORRECTIONS_20261009.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='814fe0fcc3aff4eecbe4e6c6eead5ce28927043877c0df9cfa03e3a5c71c2336'
    y=json.loads(raw)['parities'][idx]
    vi=ids+r['high_indices']+y['high_indices'];vc=list(map(F,r['retained_coefficients']+r['exact_rational_high_compensation']))+[-F(v) for v in y['rational_correction_coefficients']]
    ti=ids+h;tc=w+[-F(v) for v in ch['fixed_rational_high_lift']]
    lv=[iv(a)-iv(b) for a,b in zip(r['low_source_coordinates'],cv['retained_approximant_Ly_coordinates'])]
    lt=[sum((v*prev.old.native(source,i,j) for i,v in zip(ti,tc)),I(0)) for j in ids]
    # Unit source error is set below from the same analytic N320/pole tails.
    from math import factorial
    unit=2*n.A*4*F(106,125)**320/(1-F(106,125))+16*(n.A/2)**41/F(factorial(41))
    error=[F(cv['correction_norm_upper'])*unit,F(0)]
    if idx==0:
        zi=data[4]['additional_high_indices'];zc=list(map(F,data[4]['fixed_rational_coefficients']))
        ti+=zi;tc+=[-v for v in zc];lt=[v-iv(z) for v,z in zip(lt,data[5]['retained_approximant_Lz_coordinates'])]
        error[1]=unit*prev.norm(zc);oldblock=data[5]
    else:oldblock=ch
    par33=prev.parents();tr33=par33[0]['parities'][idx];par34=parents34();tr34=par34[idx];cert34=par34[2+idx]
    ui=ids+tr33['high_indices']+tr34['additional_high_indices'];uc=list(map(F,tr33['fixed_probe_coefficients']))+[-F(v) for v in tr34['fixed_rational_additional_coefficients']]
    assert len(ui)==len(set(ui))==len(uc)
    u=uc[:56];oldcoeff=uc[:58]
    low0=[sum((v*prev.old.native(source,i,j) for i,v in zip(ui[:58],oldcoeff)),I(0)) for j in ids]
    lu=[a-iv(b) for a,b in zip(low0,cert34['reconstructed_correction_source_coordinates'][:56])]
    error+=[F(cert34['correction_source_error_upper'])]
    mass=[F(1001,1000),prev.norm(tc),prev.norm(uc)]
    low=[lv,lt,lu]
    eta=[unit*mass[i]+error[i]+8*max(F(v.h-v.l,2*n.SCALE) for v in low[i]) for i in range(3)]
    retained=[list(map(F,r['retained_coefficients'])),w,u]
    assert all(sum(a*b for a,b in zip(retained[i],retained[j]))==0 for i in range(3) for j in range(i))
    physical_mass=[sum(v*v for v in row) for row in retained];assert min(physical_mass)>0
    return dict(ids=ids,columns=[(vi,vc),(ti,tc),(ui,uc)],low=low,retained_errors=error,physical_source_errors=eta,
        source_norm_mass_upper=mass,retained_masses=physical_mass,oldblock=oldblock,parent34=cert34,unit=unit)

def run(data,source,parity):
    o=objects(data,source,parity);ids=o['ids'];columns=o['columns'];low=o['low'];errors=o['retained_errors'];eta=o['physical_source_errors']
    m=prev.old.probe.Moments(1020,parity);assert m.eta==o['unit']
    sources=[m.source(ii,cc) for ii,cc in columns]
    print(parity,'constructed all three joined complete sources',flush=True)
    residual=[(s[0],n.add(s[1],n.scale(n.physical(ids,[v.mid() for v in row]),-1)),s[2],s[3]) for s,row in zip(sources,low)]
    q=[[I(0)]*3 for i in range(3)];g=[[I(0)]*3 for i in range(3)];old=o['oldblock'];p34=o['parent34']
    for i in range(2):
        for j in range(2):q[i][j]=iv(old['original_finite_energy_Gram'][i][j]);g[i][j]=iv(old['original_complete_residual_Gram'][i][j])
    q[2][2]=iv(p34['original_lifted_witness_energy']);g[2][2]=iv(p34['original_complete_projected_source_square'])
    ui,uc=columns[2];u=uc[:56];high=n.physical(ui[56:],uc[56:]);hm=prev.norm(uc[56:]);um=prev.norm(u)
    qproof=[];crosses={};payments={};bounds=[F(n.sqrt_r(F(g[i][i].h,n.SCALE)).h,n.SCALE)+eta[i] for i in range(3)]
    for i in range(2):
        native_retained=dot(u,low[i]);native_high=m.pair(sources[i],high)
        qpay=errors[i]*um+m.eta*o['source_norm_mass_upper'][i]*hm
        q[i][2]=q[2][i]=native_retained+native_high+I(-qpay,qpay)
        qproof.append(dict(retained=native_retained.ends(),high=native_high.ends(),error_payment=str(qpay)))
        cross=m.gram(residual[i],residual[2]);pay=eta[i]*bounds[2]+eta[2]*bounds[i]+eta[i]*eta[2]
        g[i][2]=g[2][i]=cross+I(-pay,pay);crosses[f'{i},2']=cross.ends();payments[f'{i},2']=str(pay)
        print(parity,'certified signed joined source cross',i,2,flush=True)
    signs=sign_packet(q,g,o['retained_masses'])
    print(parity,signs['joined_status'],'condensed margin',*[float(F(v)) for v in signs['joined_condensed_margin']],flush=True)
    return dict(milestone='NF35',parity=parity,aperture='53/50',interval_grid_digits=500,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        authenticated_input_sha256=prev.old.prev.SHA,NF33_input_sha256=prev.SHA33,NF34_input_sha256=SHA34,
        original_joined_native_energy_Gram=[[v.ends() for v in row] for row in q],original_joined_complete_source_Gram=[[v.ends() for v in row] for row in g],
        inherited_retained_masses=list(map(str,o['retained_masses'])),new_native_cross_proof=qproof,
        high_witness_component_norm_upper=str(hm),retained_witness_norm_upper=str(um),
        reconstructed_new_source_crosses=crosses,new_source_cross_error_payments=payments,
        reconstructed_source_norm_upper_bounds=list(map(str,bounds)),physical_source_reconstruction_error_bounds=list(map(str,eta)),
        prior_complete_source_pair_block_preserved=True,NF34_complete_source_square_preserved=True,
        signed_mixed_source_covariance_certified=True,complete_remaining_shared_source_Gram_certified=False,
        actual_negative_original_form_claimed=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False,**signs)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--parity',choices=['even','odd'],required=True);p.add_argument('--output',required=True);a=p.parse_args()
    data,source,hashes=prev.old.prev.inputs();out=run(data,source,a.parity);out['native_archive_sha256']=hashes
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
