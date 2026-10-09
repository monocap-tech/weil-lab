#!/usr/bin/env python3
"""Independent exact residual, quotient, mass and source-payment checks.

No producer code is imported. Native source reconstruction is paid by the
directed integration runs and pinned original-source theorem.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json

def read(p):
    b=Path(p).read_bytes()
    if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths,output):
    checks=0;rows=[]
    targets,th=read('notes/data/RPB108_DNE15_NF24_TARGETS_20261009.json.gz.b64')
    response,_=read('notes/data/RPB108_DNE20_NF27_INPUT_20261009.json')
    trial,_=read('notes/data/RPB108_DNE22_NF32_TRIAL_20261009.json')
    d29,qh=read('notes/data/RPB108_DNE29_OPTIMIZED_LOW_UNION_CERTIFICATE_20261009.json')
    for ix,(parity,primary_path,replay_path,frame_path) in enumerate(zip(['even','odd'],paths[::3],paths[1::3],paths[2::3])):
        (a,ah),(b,bh),(cert,ch)=[read(p) for p in (primary_path,replay_path,frame_path)]
        fixed,fh=read(f'notes/data/RPB108_DNE29_{parity.upper()}_SELECTED_COLUMNS_20261009.json.gz.b64')
        assert a['parity']==b['parity']==cert['parity']==parity and cert['input_sha256']==[ah,bh,qh,fh];checks+=1
        assert a['input_sha256']==b['input_sha256'] and a['input_sha256'][1]==th and a['input_sha256'][2]==fh and a['input_sha256'][-1]==qh;checks+=1
        wr=a['exact_W_columns'];assert wr==b['exact_W_columns'] and len(wr)==52;checks+=1
        W=[list(map(F,v)) for v in wr];ids=a['retained_indices'];piv=a['constraint_pivots'];free=a['free_coordinates']
        oldZ=[[F(j==0) for j in range(56)],list(map(F,targets['authenticated_compensated_targets'][ix]['retained_coefficients'])),list(map(F,response['parity_certificates'][ix]['exact_rational_retained_response'])),list(map(F,trial['parities'][ix]['fixed_rational_probe_coefficients']))]
        T=[{ids[0]:F(1)}]+[dict(zip(col['indices'],map(F,col['coefficients']))) for col in fixed['columns']]
        # DNE29's retained frame has the same four-dimensional span as DNE24.
        for col in T:
            v=[col.get(n,F(0)) for n in ids]
            for w in W:assert sum(x*y for x,y in zip(v,w))==0;checks+=1
        for j,w in zip(free,W):
            for z in oldZ:assert sum(x*y for x,y in zip(z,w))==0;checks+=1
            for k in free:assert w[k]==F(k==j);checks+=1
        assert all(len(w)==56 for w in W) and len(free)==52 and len(piv)==4;checks+=1
        qr=d29['rows'][ix];sc=list(map(F,qr['column_scales']));q=F(qr['native_scaled_identity_lower']);c=F(qr['complete_four_column_source_credit']);kappa=F(d29['high_floor'])
        assert cert['column_scales']==qr['column_scales'] and F(cert['native_scaled_identity_lower'])==q>0;checks+=1
        Q=[]
        for i in range(4):
            row=[]
            for j in range(4):
                pl,pu=map(F,a['fresh_original_T4_native_matrix'][i][j]);lo,hi=map(F,b['fresh_original_T4_native_matrix'][i][j]);assert pl<=lo<=hi<=pu;checks+=1
                lower,upper=map(F,qr['scaled_native_matrix'][i][j]);factor=sc[i]*sc[j]
                for run in [a,b]:
                    for x,y in [(i,j),(j,i)]:
                        lo,hi=map(F,run['fresh_original_T4_native_matrix'][x][y]);lower=max(lower,lo*factor);upper=min(upper,hi*factor)
                assert lower<=upper and [lower,upper]==list(map(F,cert['tightened_scaled_T4_native_matrix'][i][j]));checks+=1
                row.append([lower,upper])
            Q.append(row)
        assert Q==[[Q[j][i] for j in range(4)] for i in range(4)];checks+=1
        J=[list(map(F,row)) for row in cert['frozen_scaled_projection_J']];K=[list(map(F,row)) for row in cert['frozen_original_projection_K']]
        assert len(J)==len(K)==4 and all(len(row)==52 for row in J+K);checks+=1
        for i in range(4):
            for j in range(52):assert K[i][j]==sc[i]*J[i][j];checks+=1
        f2=F(0)
        for run in [a,b]:
            assert run['original_T4_native_overlap_checks']==16 and run['all_six_primes_both_orientations'] and run['exact_endpoint_log'] and not run['sampled_quadrature'];checks+=1
            err=F(run['uniform_original_source_operator_error_upper']);assert err>0;checks+=1
            for i in range(4):
                norm=F(1) if i==0 else F(fixed['columns'][i-1]['norm_upper'])
                for j in range(52):
                    wn=F(run['W_column_norm_upper'][j]);assert wn*wn>sum(x*x for x in W[j]);checks+=1
                    pay=F(run['source_error_payments'][i][j]);assert pay>=err*norm*wn;checks+=1
                    tl,tu=map(F,run['truncated_native_border'][i][j]);lo,hi=map(F,run['original_native_T4_W52_border'][i][j])
                    assert lo<=tl-pay and hi>=tu+pay;checks+=1
        for i in range(4):
            for j in range(52):
                pl,pu=map(F,a['original_native_T4_W52_border'][i][j]);lo,hi=map(F,b['original_native_T4_W52_border'][i][j]);assert pl<=lo<=hi<=pu;checks+=1
                lo*=sc[i];hi*=sc[i]
                for l in range(4):
                    x,y=sorted([Q[i][l][0]*J[l][j],Q[i][l][1]*J[l][j]]);lo-=y;hi-=x
                assert [lo,hi]==list(map(F,cert['original_scaled_native_border_residual'][i][j]));checks+=1
                f2+=max(abs(lo),abs(hi))**2
        assert F(cert['scaled_border_Frobenius_squared_upper'])==f2 and F(cert['scaled_exact_projection_coefficient_error_squared_upper'])==f2/(q*q);checks+=1
        dual=f2/q;required=dual*(4*kappa/c)**2
        assert F(cert['native_dual_border_relative_W_mass_squared_upper'])==dual and F(cert['required_hatY_native_floor_relative_W_mass'])==required;checks+=1
        assert F(cert['optimized_T4_source_credit'])==c and cert['residual_uses_nested_higher_order_source_boxes'];checks+=1
        for j,(w,col) in enumerate(zip(W,cert['exact_frozen_remainder_column_records'])):
            expected=dict(zip(ids,w))
            for i,t in enumerate(T):
                for n,x in t.items():expected[n]=expected.get(n,F(0))-x*K[i][j]
            assert sorted(expected)==col['indices'];checks+=1
            actual=[expected[n] for n in col['indices']]
            mass=sum(x*x for x in actual);assert mass==F(col['exact_mass_squared']) and F(col['norm_upper'])**2>mass;checks+=1
            # Exact quotient reconstruction: hatY + T4*K is the old W.
            reconstructed=dict(zip(col['indices'],actual))
            for i,t in enumerate(T):
                for n,x in t.items():reconstructed[n]+=x*K[i][j]
            for n,x in reconstructed.items():assert x==(w[ids.index(n)] if n in ids else F(0));checks+=1
        assert not cert['remaining_native_energy_certified'] and not cert['complete_remaining_source_Gram_certified'] and not cert['whole_aperture_positive'];checks+=1
        rows.append(dict(parity=parity,native_border_entries=208,source_orders=[a['regular_order'],b['regular_order']],frame_sha256=ch,required_native_floor=str(required)))
    # Full source/native blocks with a nonzero border cross positive/null/negative.
    # [[1,e,3/5],[e,1,0],[3/5,0,1]] has Schur determinant 16/25-e^2.
    # Native diagonal energies and the eliminated high block stay positive.
    controls=[]
    for e in [F(3,5),F(4,5),F(1)]:
        determinant=F(16,25)-e*e;controls.append(str(determinant))
        assert (determinant>0)==(e<F(4,5)) and (determinant==0)==(e==F(4,5));checks+=1
        if e==F(4,5):
            M=[[F(1),e,F(3,5)],[e,F(1),F(0)],[F(3,5),F(0),F(1)]];z=[F(1),-e,F(-3,5)]
            assert all(sum(x*y for x,y in zip(row,z))==0 for row in M);checks+=1
            for level in [F(1,1000),F(1,10),F(2)]:
                shifted=[[x+level*F(i==j) for j,x in enumerate(row)] for i,row in enumerate(M)]
                assert [sum(x*y for x,y in zip(row,z)) for row in shifted]==[level*x for x in z];checks+=1
    out=dict(stage='DNE31',status='PASS',independent_rational_checks=checks,rows=rows,total_native_border_entries=416,
        nested_higher_order_source_boxes_verified=True,exact_104_frozen_polynomial_columns_verified=True,
        native_projection_error_paid=True,conditional_native_border_crossing_controls=controls,whole_physical_mass_positive_level_controls=3,
        remaining_native_energy_certified=False,complete_remaining_source_Gram_certified=False,whole_aperture_positive=False,RH=False,Lean=False)
    Path(output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'native_border_entries':416}))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('paths',nargs=6);p.add_argument('--output',required=True);a=p.parse_args();run(a.paths,a.output)
