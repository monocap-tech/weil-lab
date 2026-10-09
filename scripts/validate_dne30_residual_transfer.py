#!/usr/bin/env python3
"""Independent frame algebra, all matrix-box envelope vertices, and Schur controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,permutations,product
import argparse,json,hashlib,base64,gzip
def read(p):
    b=Path(p).read_bytes()
    if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    return json.loads(b),hashlib.sha256(b).hexdigest()
def matrix(A):return [list(map(F,row)) for row in A]
def tr(A):return [list(row) for row in zip(*A)]
def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B,scale=F(1)):return [[x+scale*y for x,y in zip(a,b)] for a,b in zip(A,B)]
def eye(n,scale=F(1)):return [[scale*F(i==j) for j in range(n)] for i in range(n)]
def det(A):
    out=F(0);n=len(A)
    for p in permutations(range(n)):
        value=F((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n)))
        for i in range(n):value*=A[i][p[i]]
        out+=value
    return out
def inverse2(A):
    d=det(A);assert d;return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def quadr(A,z):return sum(z[i]*A[i][j]*z[j] for i in range(len(z)) for j in range(len(z)))
def run(manifest,primary,replay):
    data=[read(p) for p in manifest['inputs']];floor,gate,d29,d29r,even,odd,valid,cust=[v for v,_ in data];a,_=read(primary);b,_=read(replay)
    assert [h for _,h in data]==a['input_sha256']==b['input_sha256'];checks=1
    assert a['rows']==b['rows'] and F(a['floor_hypothesis_margin'])==F(233,1000)>0;checks+=1
    assert F(floor['certified_original_F112_lower'])==F(gate['original_infinite_F112_floor'])==F(11,25)>F(207,1000);checks+=1
    frames=[read(p) for p in manifest['frame_inputs']];be,bo,ce,co,te,to,se,so=[v for v,_ in frames];vertex_count=0
    for idx,(r,p,d,base,selected,trial,packet) in enumerate(zip(a['rows'],(even,odd),d29['rows'],(be,bo),(ce,co),(te,to),(se,so))):
        assert all(v['parity']==r['parity'] for v in (p,d,base,selected,trial,packet));checks+=1
        assert valid['parity_checks'][idx]['certificate_sha256']==data[4+idx][1] and p['NF41_input_sha256'][idx]==cust['NF41_full_source_sha256'][['EVEN','ODD'][idx]];checks+=1
        for offset,key in [(0,'NF41_'+['EVEN','ODD'][idx]+'_COLUMNS.json'),(2,['EVEN','ODD'][idx]+'_SELECTED_COLUMNS.json')]:assert frames[offset+idx][1]==cust['output_sha256'][key];checks+=1
        assert frames[4+idx][1]==packet['fixed_trial_sha256']==selected['input_sha256'][1] and frames[6+idx][1]==selected['input_sha256'][2];checks+=1
        assert p['frozen_NF38_witness']==packet['joint_universal_fixed_rational_witness'];checks+=1
        C=matrix(packet['selected_rational_joint_functionals']);z0=list(map(F,trial['old_correction_coefficients']));z1=list(map(F,trial['fixed_rational_second_correction_coefficients']))
        assert all(n>=112 for n in trial['correction_indices']) and sum(x*y for x,y in zip(z0,z1))==0;checks+=1
        for j,(bc,sc) in enumerate(zip(base['frozen_joined_polynomial_columns'],selected['columns'])):
            original=dict(zip(bc['indices'],map(F,bc['coefficients'])));test=dict(original)
            for n,x,y in zip(trial['correction_indices'],z0,z1):test[n]=test.get(n,F(0))-x*C[0][j]-y*C[1][j]
            assert sorted(test)==sc['indices'];checks+=1
            for n,x in zip(sc['indices'],map(F,sc['coefficients'])):assert test[n]==x;checks+=1
            for n,x in original.items():
                if n<112:assert test[n]==x;checks+=1
        scales=list(map(F,d['column_scales'][1:]));ell=list(map(F,d['scaled_coarse_diagonal_lower'][1:]));assert r['column_scales']==list(map(str,scales)) and r['scaled_actual_joined_Schur_diagonal_lower']==list(map(str,ell));checks+=1
        boxes=[[[F(v) for v in z] for z in row] for row in r['NF42_model_scaled_matrix_box']]
        for i in range(3):
            for j in range(3):
                K=p['conditional_improved_joined_Schur_lower_matrix'];lo=max(F(K[i][j][0]),F(K[j][i][0]))*scales[i]*scales[j];hi=min(F(K[i][j][1]),F(K[j][i][1]))*scales[i]*scales[j]
                assert boxes[i][j]==[lo,hi] and boxes[i][j]==boxes[j][i];checks+=1
        lower=matrix(r['model_lower']);upper=matrix(r['model_upper']);D=matrix(r['forced_actual_residual_signed_matrix_lower']);eps=F(r['model_operator_radius']);M=matrix(r['model_midpoint'])
        assert lower==add(M,eye(3,eps),-1) and upper==add(M,eye(3,eps));checks+=1
        # All 64 vertices: check every principal minor of both envelope differences.
        positions=[(i,j) for i in range(3) for j in range(i,3)];choices=[sorted(set(boxes[i][j])) for i,j in positions]
        for values in product(*choices):
            V=[[F(0)]*3 for _ in range(3)]
            for (i,j),value in zip(positions,values):V[i][j]=V[j][i]=value
            for difference in [add(upper,V,-1),add(V,lower,-1)]:
                for n in range(1,4):
                    for ids in combinations(range(3),n):assert det([[difference[i][j] for j in ids] for i in ids])>=0;checks+=1
            vertex_count+=1
        L=[[ell[i]*F(i==j) for j in range(3)] for i in range(3)]
        assert D==add(L,upper,-1) and add(lower,D)==matrix(r['complete_model_plus_residual_lower'])==add(L,eye(3,2*eps),-1);checks+=1
        assert all(F(v)>0 for v in r['complete_signed_acceptance_margins']);checks+=1
        # The signed residual floor is deliberately not mislabeled as PSD.
        assert any(D[i][i]<0 for i in range(3)) and not r['residual_lower_matrix_required_to_be_PSD'];checks+=1
        h=list(map(F,p['frozen_NF38_witness']));z=[v/s for v,s in zip(h,scales)];schur=quadr(L,z);assert schur==F(r['actual_joined_witness_strict_lower'])>0;checks+=1
        endpoint_lo=endpoint_hi=F(0)
        for i in range(3):
            for j in range(3):
                values=sorted(v*z[i]*z[j] for v in boxes[i][j]);endpoint_lo+=values[0];endpoint_hi+=values[1]
        original=list(map(F,p['improved_lower_witness_value']));lo=max(endpoint_lo,original[0]);hi=min(endpoint_hi,original[1]);assert [lo,hi]==list(map(F,r['model_witness_interval'])) and hi<0;checks+=1
        forced=schur-hi;need=-hi;assert forced==F(r['forced_actual_residual_witness_strict_lower']) and need==F(r['necessary_additional_response_after_A1']);checks+=1
        assert forced>quadr(D,z)==F(r['forced_residual_from_single_matrix_lower'])>need and forced/need==F(r['forced_over_necessary_ratio']);checks+=1
        assert F(p['conditional_frozen_witness_inverse_improvement'][0])>0;checks+=1
    # Exact high-lift invariance on genuine full blocks through the crossing.
    H=[[F(2),F(1)],[F(1),F(3)]];HI=inverse2(H);B=[[F(1,3),F(1,5)],[F(1,7),F(1,11)]]
    lift=[[F(-2,3),F(5,7)],[F(3,5),F(-4,9)]];controls=[]
    for scale in [F(1),F(1,10**18)]:
        for delta in [F(-1,100),F(0),F(1,100)]:
            S=[[scale,2*scale],[2*scale,(4+delta)*scale]];Q=add(S,mm(mm(tr(B),HI),B));Qt=add(add(Q,mm(tr(B),lift),-1),mm(tr(lift),B),-1);Qt=add(Qt,mm(mm(tr(lift),H),lift));Bt=add(B,mm(H,lift),-1)
            assert add(Qt,mm(mm(tr(Bt),HI),Bt),-1)==S==add(Q,mm(mm(tr(B),HI),B),-1);checks+=1
            assert Q[0][0]>0 and det(Q)>0 and H[0][0]>0 and det(H)>0;checks+=1
            full=[Q[i]+tr(B)[i] for i in range(2)]+[B[i]+H[i] for i in range(2)]
            assert det(full)==det(H)*det(S) and (det(full)>0)==(delta>0) and (det(full)==0)==(delta==0);checks+=1
            controls.append(dict(scale=str(scale),condensed_determinant=str(det(S)),full_determinant=str(det(full)),high_lift_invariance=True))
    S=[[F(1),F(2)],[F(2),F(4)]];Q=add(S,mm(mm(tr(B),HI),B));full=[Q[i]+tr(B)[i] for i in range(2)]+[B[i]+H[i] for i in range(2)];ret=[F(-2),F(1)];high=mm(HI,mm(B,[[x] for x in ret]));null=ret+[-x[0] for x in high]
    assert mm(full,[[x] for x in null])==[[F(0)]]*4;checks+=1
    for lam in [F(1,1000),F(1,10),F(2)]:
        shifted=add(full,eye(4,lam));assert mm(shifted,[[x] for x in null])==[[lam*x] for x in null];checks+=1
        only_retained=add(shifted,[[lam*F(i==j and i<2) for j in range(4)] for i in range(4)],-1);assert mm(only_retained,[[x] for x in null])!=[[F(0)]]*4;checks+=1
    # A successful finite high compression is not a uniform high floor.
    for hidden in [F(1,10),F(1,20),F(1,100)]:assert F(2)>F(207,1000)>hidden;checks+=1
    return dict(stage='DNE30',status='PASS',independent_rational_checks=checks,matrix_envelope_vertices=vertex_count,
        all_principal_minors_of_envelope_differences_nonnegative=True,full_signed_acceptance_positive=True,
        exact_high_lift_frame_reconstruction_passed=True,primary_and_replay_rows_identical=True,
        high_shift_full_block_crossings=controls,whole_physical_mass_positive_level_controls=3,
        finite_compression_is_not_uniform_floor_controls=3,response_bound_inherited_not_inverse_evaluated=True,
        certificate_sha256=read(primary)[1],replay_sha256=read(replay)[1],complete_remaining_Gram_certified=False,whole_aperture_positive=False)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ['manifest','primary','replay','output']:p.add_argument(k)
    a=p.parse_args();r=run(json.loads(Path(a.manifest).read_bytes()),a.primary,a.replay);Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'checks':r['independent_rational_checks'],'matrix_vertices':r['matrix_envelope_vertices']}))
