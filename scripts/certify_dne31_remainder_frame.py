#!/usr/bin/env python3
"""Freeze all optimized remainder columns and pay the full native border.

The complete remainder native energy and source Gram are still required.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,base64,gzip,hashlib,json
from certify_dne31_native_border import inverse,read,root

def mm(A,B):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def box(x):return list(map(F,x))
def run(parity,primary_path,replay_path,output):
    primary,ph=read(primary_path);replay,rh=read(replay_path);ix=0 if parity=='even' else 1
    assert primary['parity']==replay['parity']==parity
    assert primary['regular_order']==660 and replay['regular_order']==700
    assert primary['exact_W_columns']==replay['exact_W_columns'] and primary['input_sha256']==replay['input_sha256']
    assert primary['original_T4_native_overlap_checks']==replay['original_T4_native_overlap_checks']==16
    d29,qh=read('notes/data/RPB108_DNE29_OPTIMIZED_LOW_UNION_CERTIFICATE_20261009.json');r=d29['rows'][ix]
    fixed,fh=read(f'notes/data/RPB108_DNE29_{parity.upper()}_SELECTED_COLUMNS_20261009.json.gz.b64')
    assert qh==primary['input_sha256'][-1] and fh==primary['input_sha256'][2]
    scale=list(map(F,r['column_scales']));q=F(r['native_scaled_identity_lower']);credit=F(r['complete_four_column_source_credit']);kappa=F(d29['high_floor'])
    Q=[];native_nested=0
    for i in range(4):
        row=[]
        for j in range(4):
            p=box(primary['fresh_original_T4_native_matrix'][i][j]);b=box(replay['fresh_original_T4_native_matrix'][i][j])
            assert p[0]<=b[0]<=b[1]<=p[1];native_nested+=1
            lower,upper=box(r['scaled_native_matrix'][i][j]);factor=scale[i]*scale[j]
            for run in [primary,replay]:
                for x,y in [(i,j),(j,i)]:
                    lo,hi=box(run['fresh_original_T4_native_matrix'][x][y]);lower=max(lower,lo*factor);upper=min(upper,hi*factor)
            assert lower<=upper
            row.append([lower,upper])
        Q.append(row)
    midpoint=[[(lo+hi)/2 for lo,hi in row] for row in Q]
    Pin=[];checks=0
    for i in range(4):
        rr=[]
        for j in range(52):
            a=box(primary['original_native_T4_W52_border'][i][j]);b=box(replay['original_native_T4_W52_border'][i][j])
            assert a[0]<=b[0]<=b[1]<=a[1];checks+=1
            # Nested higher-order source boxes are individually paid inputs.
            rr.append([(b[0]*scale[i]),(b[1]*scale[i])])
        Pin.append(rr)
    # Diagnostics choose a rational scaled map; only its residual is certified.
    Pr=[[sum(box(v))*scale[i]/2 for v in row] for i,row in enumerate(replay['original_native_T4_W52_border'])]
    J=mm(inverse(midpoint),Pr);den=10**60
    J=[[F(round(x*den),den) for x in row] for row in J]
    K=[[x*s for x in row] for s,row in zip(scale,J)]
    residual=[];maxima=[]
    for i in range(4):
        rr=[];rm=[]
        for j in range(52):
            lo,hi=Pin[i][j]
            for l in range(4):
                v=J[l][j];a,b=sorted([Q[i][l][0]*v,Q[i][l][1]*v]);lo-=b;hi-=a
            rr.append([str(lo),str(hi)]);rm.append(max(abs(lo),abs(hi)))
        residual.append(rr);maxima.append(rm)
    f2=sum(v*v for row in maxima for v in row);coef_error2=f2/(q*q);dual2=f2/q
    # If Q(hatY)>=b G_W, this b suffices for epsilon<c/(4*kappa).
    required_b=dual2*(4*kappa/credit)**2
    W=[list(map(F,row)) for row in primary['exact_W_columns']];ids=primary['retained_indices']
    T=[{ids[0]:F(1)}]+[dict(zip(c['indices'],map(F,c['coefficients']))) for c in fixed['columns']]
    columns=[]
    for j,w in enumerate(W):
        v=dict(zip(ids,w))
        for i,t in enumerate(T):
            for n,x in t.items():v[n]=v.get(n,F(0))-x*K[i][j]
        indices=sorted(v);coeff=[v[n] for n in indices];mass=sum(x*x for x in coeff)
        columns.append(dict(indices=indices,exact_mass_squared=str(mass),norm_upper=str(root(mass))))
    out=dict(stage='DNE31',parent=primary['parent'],parity=parity,input_paths=[primary_path,replay_path],input_sha256=[ph,rh,qh,fh],
        primary_replay_nested_border_checks=checks,primary_replay_nested_T4_native_checks=native_nested,tightened_scaled_T4_native_matrix=[[[str(x) for x in v] for v in row] for row in Q],remaining_dimension=52,optimized_T4_source_credit=str(credit),original_high_floor=str(kappa),native_scaled_identity_lower=str(q),
        residual_uses_nested_higher_order_source_boxes=True,column_scales=list(map(str,scale)),frozen_scaled_projection_J=[[str(x) for x in row] for row in J],frozen_original_projection_K=[[str(x) for x in row] for row in K],
        original_scaled_native_border_residual=residual,scaled_border_Frobenius_squared_upper=str(f2),scaled_exact_projection_coefficient_error_squared_upper=str(coef_error2),
        native_dual_border_relative_W_mass_squared_upper=str(dual2),required_hatY_native_floor_relative_W_mass=str(required_b),
        display_scaled_border_norm_upper=float(root(f2)),display_required_native_floor=float(required_b),
        exact_frozen_remainder_column_records=columns,coefficient_storage='Exact coefficients specified by pinned T4, W and frozen K; materialize_dne31_remainder.py expands them.',frame_rule='hatY=W-T4*K; J=S^-1*K; E_scaled=S*Q(T4,W)-(S*Q(T4,T4)*S)*J',
        quotient_mod_retained_Z8_unchanged=True,full_retained_span_with_T4=True,all_104_remainder_columns_frozen=True,
        native_border_is_not_set_to_zero=True,remaining_native_energy_certified=False,complete_remaining_source_Gram_certified=False,
        remaining_condition='Q(hatY)>=b*G_W with b>required_floor, Gamma_hatY<=(c/2)*Q(hatY), then DNE25 applies',
        whole_aperture_positive=False,RH=False,Lean=False)
    Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({key:out[key] for key in ['parity','primary_replay_nested_border_checks','display_scaled_border_norm_upper','display_required_native_floor']}))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ['parity','primary','replay','output']:p.add_argument(k)
    a=p.parse_args();run(a.parity,a.primary,a.replay,a.output)
