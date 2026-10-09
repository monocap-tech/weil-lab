#!/usr/bin/env python3
"""Discharge NF42's floor and transfer the already-paid actual Schur bound."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,gzip,base64
SHA=['4d11eed40d2660e603a36ade6e3dc4dcfb6a88937788aaf51b37665daf500321','c5a9f3af12264fd0602a6916c756de83d3e0092c99b168d2121fe3a89ab45c83','af2acfa894b79426b3219a0303c2815df721b4bcd4ca0a8d6d271a69606cdd78','cfe0f5799d0abe72c292628a091a43c15026c31e800854c0111f5c3924f9204d','e58c3ea1160fc1c632d50c6d61d7f1595919ed0707bb77a1109662b6830d50c4','24655cd64c0bf8b6b7b9dce654ff10ad3085eb3b56879bc123873cde54df1d9f','69626c40fd55c49a162a494ed70210088148dd86e80dff385698b85f78105471','fda09b0d03cc8211de9ba6e9d746a41108ecc9a7ac7900e138569b9792270475']
def read(p):
    b=Path(p).read_bytes()
    if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    return json.loads(b),hashlib.sha256(b).hexdigest()
def strings(A):return [[str(x) for x in row] for row in A]
def run(paths,use_replay=False):
    data=[read(p) for p in paths];assert [h for _,h in data]==SHA;checks=1
    floor,fg,primary,replay,even,odd,valid,custody=[v for v,_ in data];prior=replay if use_replay else primary;k=F(11,25);old=F(207,1000)
    assert floor['aperture']==prior['aperture']=='53/50' and fg['status']=='PASS';checks+=1
    assert F(floor['certified_original_F112_lower'])==F(fg['original_infinite_F112_floor'])==F(prior['high_floor'])==k>old;checks+=1
    assert valid['status']=='PASS' and all(v['status']=='PASS' for v in valid['parity_checks']);checks+=1
    assert prior['NF38_optimized_low_mode_union_certified'] and prior['same_retained_Z8'] and prior['high_lifts_changed_from_DNE23'];checks+=1
    rows=[]
    for idx,(p,d,pv) in enumerate(zip((even,odd),prior['rows'],valid['parity_checks'])):
        assert p['parity']==d['parity']==pv['parity'] and pv['certificate_sha256']==SHA[4+idx];checks+=1
        assert p['background_floor_hypothesis']=='A >= (207/1000) I on the original remaining high space' and not p['background_floor_newly_proved'];checks+=1
        assert p['NF41_input_sha256'][:2]==[custody['NF41_full_source_sha256']['EVEN'],custody['NF41_full_source_sha256']['ODD']];checks+=1
        sc=list(map(F,d['column_scales'][1:]));ell=list(map(F,d['scaled_coarse_diagonal_lower'][1:]));h=list(map(F,p['frozen_NF38_witness']));assert h[2]==1 and all(v>0 for v in sc+ell);checks+=1
        K=p['conditional_improved_joined_Schur_lower_matrix'];box=[]
        for i in range(3):
            row=[]
            for j in range(3):
                lo=max(F(K[i][j][0]),F(K[j][i][0]));hi=min(F(K[i][j][1]),F(K[j][i][1]));assert lo<=hi;checks+=1
                row.append((lo*sc[i]*sc[j],hi*sc[i]*sc[j]))
            box.append(row)
        M=[[(lo+hi)/2 for lo,hi in row] for row in box];rad=[[(hi-lo)/2 for lo,hi in row] for row in box]
        eps=max(sum(row) for row in rad);assert eps>0;checks+=1
        Klo=[[M[i][j]-(eps if i==j else 0) for j in range(3)] for i in range(3)]
        Kup=[[M[i][j]+(eps if i==j else 0) for j in range(3)] for i in range(3)]
        D=[[(ell[i] if i==j else 0)-Kup[i][j] for j in range(3)] for i in range(3)]
        total=[[Klo[i][j]+D[i][j] for j in range(3)] for i in range(3)]
        margins=[e-2*eps for e in ell]
        for i in range(3):
            for j in range(3):assert total[i][j]==(margins[i] if i==j else 0);checks+=1
        assert min(margins)>0;checks+=1
        z=[hh/ss for hh,ss in zip(h,sc)];a=sum(e*x*x for e,x in zip(ell,z));wlo=whi=F(0)
        for i in range(3):
            for j in range(3):
                vals=sorted(v*z[i]*z[j] for v in box[i][j]);wlo+=vals[0];whi+=vals[1]
        pub=list(map(F,p['improved_lower_witness_value']));wlo=max(wlo,pub[0]);whi=min(whi,pub[1]);assert wlo<=whi<0;checks+=1
        need=-whi;forced=a-whi;matrix_forced=sum(z[i]*D[i][j]*z[j] for i in range(3) for j in range(3))
        assert forced>matrix_forced>need>0;checks+=1
        factor=F(10) if idx==0 else F(140);assert forced>factor*need;checks+=1
        delta=list(map(F,p['conditional_frozen_witness_inverse_improvement']));assert 0<delta[0]<=delta[1];checks+=1
        rows.append(dict(parity=p['parity'],scaled_actual_joined_Schur_diagonal_lower=list(map(str,ell)),column_scales=list(map(str,sc)),
            NF42_model_scaled_matrix_box=[[[str(lo),str(hi)] for lo,hi in row] for row in box],
            model_midpoint=strings(M),model_operator_radius=str(eps),model_lower=strings(Klo),model_upper=strings(Kup),
            forced_actual_residual_signed_matrix_lower=strings(D),residual_lower_matrix_required_to_be_PSD=False,
            complete_model_plus_residual_lower=strings(total),complete_signed_acceptance_margins=list(map(str,margins)),
            frozen_witness=list(map(str,h)),actual_joined_witness_strict_lower=str(a),model_witness_interval=list(map(str,[wlo,whi])),
            necessary_additional_response_after_A1=str(need),forced_actual_residual_witness_strict_lower=str(forced),
            forced_residual_from_single_matrix_lower=str(matrix_forced),forced_over_necessary_ratio=str(forced/need),
            display_forced_response=float(forced),display_necessary_response=float(need),display_ratio=float(forced/need),
            NF42_source_backed_improvement_now_unconditional=list(map(str,delta)),
            NF42_original_negative_lower_certificate_preserved=True,actual_joined_Schur_positive=True,
            actual_residual_inverse_evaluated=False))
    return dict(stage='DNE30',aperture='53/50',input_sha256=SHA,DNE29_replay_bounds_used=use_replay,exact_counted_assertions=checks,
        actual_high_floor=str(k),NF42_required_floor=str(old),floor_hypothesis_margin=str(k-old),
        operator_space_identification='NF42 A and DNE17 C are the original F112 high restriction at a=53/50',
        high_shift_invariance='Schur(B-Z*C)=Schur(B), since Z is entirely original high',
        rows=rows,NF42_floor_hypothesis_discharged=True,actual_three_retained_columns_per_parity_positive=True,
        response_lower_bound_derived_from_DNE29_not_directly_measured=True,
        positive_retained_dimension_already_certified=8,new_positive_retained_directions=0,uncovered_retained_dimension=104,
        physical_gap_guard_unchanged=prior['physical_gap_guard'],remaining_native_orthogonalization_computed=False,
        complete_remaining_source_Gram_certified=False,new_original_source_integrations=False,
        actual_infinite_inverse_evaluated=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('manifest');p.add_argument('--replay-bounds',action='store_true');p.add_argument('--output',required=True);a=p.parse_args();m=json.loads(Path(a.manifest).read_bytes());r=run(m['inputs'],a.replay_bounds)
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'checks':r['exact_counted_assertions'],'rows':[{k:v[k] for k in ['parity','display_forced_response','display_necessary_response','display_ratio']} for v in r['rows']]}))
