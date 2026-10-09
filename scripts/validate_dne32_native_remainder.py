#!/usr/bin/env python3
"""Independent native congruence enclosure and physical trace validation."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json
def read(path):
    b=Path(path).read_bytes()
    if path.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    elif path.endswith('.gz'):b=gzip.decompress(b)
    return json.loads(b),hashlib.sha256(b).hexdigest()
def interval_sum(terms):
    lo=hi=F(0)
    for box,coefficient in terms:
        a,b=sorted([F(box[0])*coefficient,F(box[1])*coefficient]);lo+=a;hi+=b
    return lo,hi
def mat(A):return [list(map(F,row)) for row in A]
def transpose(A):return [list(row) for row in zip(*A)]
def multiply(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def run(cert_paths,original_archive,output):
    checks=0;rows=[]
    for cert_path in cert_paths:
        c,ch=read(cert_path);inp=[read(p) for p in c['input_paths']];raw,native,frame,primary,replay=[v for v,h in inp]
        assert [h for v,h in inp]==c['input_sha256'] and raw['original_decoded_archive_sha256']==c['original_decoded_archive_sha256'];checks+=1
        parity=c['parity'];assert native['parity']==frame['parity']==primary['parity']==replay['parity']==parity;checks+=1
        assert [primary['regular_order'],replay['regular_order']]==[900,940] and primary['input_sha256']==replay['input_sha256']==native['input_sha256'];checks+=1
        W=mat(native['exact_W_columns']);ids=native['retained_indices'];free=native['free_coordinates'];n=52;sc=list(map(F,frame['column_scales']));J=mat(frame['frozen_scaled_projection_J'])
        fixed,fixed_hash=read(primary['input_paths'][2]);assert fixed_hash==primary['input_sha256'][2];checks+=1
        norms=[F(1)]+[F(col['norm_upper']) for col in fixed['columns']]
        for source in [primary,replay]:
            assert source['complete_original_source_action'] and source['all_six_primes_both_orientations'] and source['exact_endpoint_log'] and source['half_translation_panels']==7 and not source['sampled_quadrature'];checks+=1
            assert source['original_T4_native_overlap_checks']==16;checks+=1
            err=F(source['uniform_original_source_operator_error_upper']);assert err>0;checks+=1
            for i in range(4):
                for j in range(n):
                    wn=F(source['W_column_norm_upper'][j]);assert wn*wn>sum(x*x for x in W[j]);checks+=1
                    paid=F(source['source_error_payments'][i][j]);assert paid>=err*norms[i]*wn;checks+=1
                    lo,hi=map(F,source['truncated_native_border'][i][j]);bl,bh=map(F,source['original_native_T4_W52_border'][i][j]);assert bl<=lo-paid and bh>=hi+paid;checks+=1
        for col,j in zip(W,free):
            for k in free:assert col[k]==F(j==k);checks+=1
        sparse=[[(i,x) for i,x in enumerate(col) if x] for col in W]
        A=c['tightened_scaled_T4_native_matrix'];P=c['tightened_scaled_T4_W52_border']
        for i in range(4):
            for j in range(4):
                al,au=map(F,primary['fresh_original_T4_native_matrix'][i][j]);bl,bu=map(F,replay['fresh_original_T4_native_matrix'][i][j]);assert al<=bl<=bu<=au;checks+=1
                lo,hi=map(F,frame['tightened_scaled_T4_native_matrix'][i][j]);factor=sc[i]*sc[j]
                for x,y in [(i,j),(j,i)]:
                    a,b=map(F,replay['fresh_original_T4_native_matrix'][x][y]);lo=max(lo,a*factor);hi=min(hi,b*factor)
                assert lo<=hi and F(A[i][j][0])<=lo<=hi<=F(A[i][j][1]);checks+=1
            for j in range(n):
                al,au=map(F,primary['original_native_T4_W52_border'][i][j]);bl,bu=map(F,replay['original_native_T4_W52_border'][i][j]);assert al<=bl<=bu<=au;checks+=1
                assert F(P[i][j][0])<=bl*sc[i]<=bu*sc[i]<=F(P[i][j][1]);checks+=1
        B=c['complete_original_native_remainder_matrix'];bm=[];br=[]
        # Assemble each original finite native quadratic directly, rather than
        # using the producer's two-stage interval matrix multiplication.
        for i in range(n):
            mids=[];rads=[]
            for j in range(n):
                terms=[(raw['complete_original_retained_native'][f'{min(ids[k],ids[l])},{max(ids[k],ids[l])}'],x*y) for k,x in sparse[i] for l,y in sparse[j]]
                terms += [(P[k][i],-J[k][j]) for k in range(4)]+[(P[k][j],-J[k][i]) for k in range(4)]
                terms += [(A[k][l],J[k][i]*J[l][j]) for k in range(4) for l in range(4)]
                lo,hi=interval_sum(terms);bl,bh=map(F,B[i][j]);assert bl<=lo<=hi<=bh;checks+=1
                assert B[i][j]==B[j][i];checks+=1
                mids.append((bl+bh)/2);rads.append((bh-bl)/2)
            bm.append(mids);br.append(rads)
        U=mat(c['exact_rational_congruence_U']);assert len(U)==n and all(len(row)==n for row in U);checks+=1
        for i in range(n):
            assert U[i][i]!=0 and all(U[i][j]==0 for j in range(i));checks+=1
        # Linear uncertainty enclosure for a congruence by an EXACT fixed U.
        cm=multiply(transpose(U),multiply(bm,U));ua=[[abs(x) for x in row] for row in U];cr=multiply(transpose(ua),multiply(br,ua));margins=[]
        for i in range(n):
            for j in range(n):
                lo,hi=map(F,c['congruence_matrix'][i][j]);assert lo<=cm[i][j]-cr[i][j]<=cm[i][j]+cr[i][j]<=hi;checks+=1
            lo=F(c['congruence_matrix'][i][i][0]);off=sum(max(abs(F(c['congruence_matrix'][i][j][0])),abs(F(c['congruence_matrix'][i][j][1]))) for j in range(n) if j!=i)
            assert lo-off==F(c['congruence_Gershgorin_margins'][i])>0;checks+=1;margins.append(lo-off)
        margin=min(margins);assert margin==F(c['congruence_margin_lower']);checks+=1
        gram=[[sum(x*y for x,y in zip(a,b)) for b in W] for a in W]
        assert gram==mat(c['exact_raw_W_mass_matrix']);checks+=1
        WT=transpose(W);WU=[[sum(row[k]*col[k] for k in range(n) if row[k]) for col in transpose(U)] for row in WT]
        mass=sum(x*x for row in WU for x in row);bound=margin/mass
        assert mass==F(c['exact_WU_Frobenius_squared']) and bound==F(c['native_floor_relative_raw_W_mass_lower']);checks+=1
        guard=F(c['native_floor_guard']);required=F(frame['required_hatY_native_floor_relative_W_mass']);assert 0<required<guard<bound;checks+=1
        f2=F(frame['scaled_border_Frobenius_squared_upper']);q=F(frame['native_scaled_identity_lower']);credit=F(frame['optimized_T4_source_credit']);kappa=F(frame['original_high_floor'])
        assert F(c['native_mixed_dual_border_squared_upper'])==f2/(q*guard)<F(c['native_mixed_dual_allocation_squared'])==(credit/(4*kappa))**2;checks+=1
        y_mass=sum(F(v['exact_mass_squared']) for v in frame['exact_frozen_remainder_column_records']);t_mass=[F(1)]+[F(v['exact_mass_squared']) for v in fixed['columns']];scaled_t_mass=sum(s*s*m for s,m in zip(sc,t_mass));eps=credit/(4*kappa)
        assert F(c['exact_total_frozen_remainder_physical_mass'])==y_mass and F(c['exact_total_scaled_tested_physical_mass'])==scaled_t_mass;checks+=1
        assert F(c['remaining_native_physical_gap_guard'])==guard/y_mass>0 and F(c['full_finite_lifted_native_physical_gap_guard'])==(1-eps)/(2*(scaled_t_mass/q+y_mass/guard))>0;checks+=1
        assert c['full_finite_lifted_native_family_positive'];checks+=1
        assert c['remaining_native_energy_certified'] and c['DNE31_mixed_native_border_hypothesis_discharged'] and not c['complete_remaining_source_Gram_certified'] and not c['whole_aperture_positive'];checks+=1
        rows.append(dict(parity=parity,certificate_sha256=ch,native_floor_guard=str(guard),congruence_margin=str(margin),native_border_allocation_discharged=True))
    if original_archive:
        original,oh=read(original_archive);export,_=read(read(cert_paths[0])[0]['input_paths'][0]);assert oh==export['original_decoded_archive_sha256'];checks+=1
        for key,value in export['complete_original_retained_native'].items():
            a,b=map(F,original['complete_form'][key]['full']);lo,hi=map(F,value);assert lo<=a<=b<=hi;checks+=1
    # A positive FULL retained native energy does not pay the high source Gram.
    controls=[]
    for s in [F(3,5),F(4,5),F(1)]:
        determinant=1-F(9,25)-s*s;controls.append(str(determinant));assert (determinant>0)==(s<F(4,5)) and (determinant==0)==(s==F(4,5));checks+=1
        if s==F(4,5):
            M=[[F(1),F(0),F(3,5)],[F(0),F(1),s],[F(3,5),s,F(1)]];z=[F(-3,5),-s,F(1)];assert all(sum(x*y for x,y in zip(row,z))==0 for row in M);checks+=1
            for level in [F(1,1000),F(1,10),F(2)]:
                assert [sum((x+level*F(i==j))*y for j,(x,y) in enumerate(zip(row,z))) for i,row in enumerate(M)]==[level*x for x in z];checks+=1
    out=dict(stage='DNE32',status='PASS',independent_rational_checks=checks,rows=rows,original_native_archive_export_checked=bool(original_archive),complete_native_matrices_verified=True,complete_52_by_52_congruences_verified=True,
        native_vs_full_source_crossing_determinants=controls,whole_physical_mass_positive_level_controls=3,remaining_native_energy_certified=True,complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
    Path(output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','checks':checks,'native_energy_certified':True}),flush=True)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('certificates',nargs=2);p.add_argument('--original-archive');p.add_argument('--output',required=True);a=p.parse_args();run(a.certificates,a.original_archive,a.output)
