#!/usr/bin/env python3
"""Independent exact selected-column, original symmetry, and matrix-box replay."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,json,hashlib,base64,gzip
import validate_dne28_signed_budget as v
assert hashlib.sha256(Path(v.__file__).read_bytes()).hexdigest()=='d866758351e03deb9cf49e37bc7240432baa3115ccbb466e27f99d5f8c9bd7dc'
def read(p):
    b=Path(p).read_bytes()
    if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    return json.loads(b),hashlib.sha256(b).hexdigest()
def run(paths,extra,primary,replay):
    data=[read(p) for p in paths];low,scales,se,so,d26,d28,ce,co,pe,po=[x for x,_ in data]
    a,_=read(primary);b,_=read(replay);assert [h for _,h in data]==a['input_sha256'];checks=1
    be,bo,te,to,re,ro,pre,pro,targets,response,trial=[read(p)[0] for p in extra]
    assert b['input_sha256'][:8]==a['input_sha256'][:8] and [read(p)[1] for p in extra[6:8]]==b['input_sha256'][8:];checks+=1
    k=F(11,25);records=[]
    for idx,(r,rp,l,s,sc,col,pair,rev,pr,base,t) in enumerate(zip(a['rows'],b['rows'],low['native_parity_gates'],(se,so),scales['rows'],(ce,co),(pe,po),(re,ro),(pre,pro),(be,bo),(te,to))):
        assert all(z['parity']==r['parity'] for z in (rp,l,s,sc,col,pair,rev,pr,base,t));checks+=1
        assert read(extra[idx])[1]==col['input_sha256'][0] and read(extra[2+idx])[1]==s['fixed_trial_sha256']==col['input_sha256'][1];checks+=1
        assert rev['reverse_source_action_used'] and pair['fixed_columns_sha256']==pr['fixed_columns_sha256']==rev['fixed_columns_sha256']==a['input_sha256'][6+idx];checks+=1
        retained=[targets['authenticated_compensated_targets'][idx]['retained_coefficients'],response['parity_certificates'][idx]['exact_rational_retained_response'],trial['parities'][idx]['fixed_rational_probe_coefficients']]
        C=[list(map(F,row)) for row in s['selected_rational_joint_functionals']];z0=list(map(F,t['old_correction_coefficients']));z1=list(map(F,t['fixed_rational_second_correction_coefficients']))
        selected_dicts=[]
        for j,(bc,cc) in enumerate(zip(base['frozen_joined_polynomial_columns'],col['columns'])):
            d=dict(zip(bc['indices'],map(F,bc['coefficients'])))
            for n,x,y in zip(t['correction_indices'],z0,z1):d[n]=d.get(n,F(0))-C[0][j]*x-C[1][j]*y
            assert sorted(d)==cc['indices'];checks+=1
            for n,cv in zip(cc['indices'],map(F,cc['coefficients'])):assert d[n]==cv;checks+=1
            for n,cv in zip(targets['authenticated_compensated_targets'][idx]['retained_indices'],map(F,retained[j])):assert d[n]==cv;checks+=1
            mass=sum(cv*cv for cv in d.values());assert mass==F(cc['exact_mass_squared']) and F(cc['norm_upper'])**2>mass;checks+=1
            selected_dicts.append(d)
            for original in (pair,pr,rev):
                N=original['regular_order'];eta=2*F(53,50)*F(550,19)*F(106,125)**N+F(3,10**99)
                err=F(original['uniform_low_source_operator_error_upper']);assert err>=eta;checks+=1
                tr=v.box(original['truncated_low_selected_pairings'][j]);paid=v.box(original['original_low_selected_pairings'][j]);e=err*F(cc['norm_upper']);assert paid[0]<=tr[0]-e and paid[1]>=tr[1]+e;checks+=1
            boxes=[v.box(o['original_low_selected_pairings'][j]) for o in (pair,pr,rev)];assert max(x[0] for x in boxes)<=min(x[1] for x in boxes);checks+=1
            assert v.inside(boxes[1],boxes[0]);checks+=1
        h=list(map(F,t['exact_moved_target_coefficients']))
        for n,value in zip(t['merged_target_indices'],map(F,t['merged_target_coefficients'])):
            assert sum(h[j]*F(dict(zip(bc['indices'],bc['coefficients'])).get(n,'0')) for j,bc in enumerate(base['frozen_joined_polynomial_columns']))==value;checks+=1
        tau=F(r['young_source_parameter']);credit=F(r['complete_four_column_source_credit']);scale=[F(1)]+list(map(F,sc['congruence_scales']))
        assert 0<credit<k and credit>F(d28['rows'][idx]['complete_four_column_source_credit']);checks+=1
        Q=[[v.box(z) for z in row] for row in r['scaled_native_matrix']];G=[[v.box(z) for z in row] for row in r['scaled_block_source_input']]
        D=[[v.box(z) for z in row] for row in r['scaled_coherent_source_majorant']];H=[[v.box(z) for z in row] for row in r['signed_comparison_matrix']]
        Q0=[[(F(0),F(0)) for _ in range(4)] for _ in range(4)];G0=[[(F(0),F(0)) for _ in range(4)] for _ in range(4)]
        Q0[0][0]=v.box(l['native_Q_diagonal']);P0=F(l['full_F112_source_square'][1]);G0[0][0]=(P0,P0)
        for j in range(3):Q0[0][j+1]=Q0[j+1][0]=v.box(pair['original_low_selected_pairings'][j])
        for i in range(3):
            for j in range(3):
                for field,M in [('original_selected_native_energy_Gram',Q0),('original_selected_complete_source_Gram',G0)]:
                    x=v.box(s[field][i][j]);y=v.box(s[field][j][i]);M[i+1][j+1]=(max(x[0],y[0]),min(x[1],y[1]));assert M[i+1][j+1][0]<=M[i+1][j+1][1];checks+=1
        for i in range(4):
            for j in range(4):
                assert v.inside(v.scale(Q0[i][j],scale[i]*scale[j]),Q[i][j]);checks+=1
                assert v.inside(v.scale(G0[i][j],scale[i]*scale[j]),G[i][j]);checks+=1
                assert v.inside(v.scale(G[i][j],1+1/tau if i==j==0 else 1+tau),D[i][j]);checks+=1
                assert v.inside(v.minus(v.scale(Q[i][j],k-credit),D[i][j]),H[i][j]);checks+=1
                for field in ['scaled_native_matrix','scaled_block_source_input','scaled_coherent_source_majorant','signed_comparison_matrix']:assert v.inside(v.box(rp[field][i][j]),v.box(r[field][i][j]));checks+=1
        q=F(r['native_scaled_identity_lower']);ell=list(map(F,r['scaled_coarse_diagonal_lower']))
        N=[[v.minus(Q[i][j],(q,q) if i==j else (F(0),F(0))) for j in range(4)] for i in range(4)]
        U=[[v.minus(v.minus(Q[i][j],v.scale(D[i][j],1/k)),(ell[i],ell[i]) if i==j else (F(0),F(0))) for j in range(4)] for i in range(4)]
        for name,M in [('source_credit',H),('native_identity',N),('physical_diagonal',U)]:
            vs,cs,mins=v.vertex_sylvester(M);checks+=cs;records.append(dict(parity=r['parity'],matrix=name,vertices=vs,positive_leading_minors=cs,minimal_leading_determinants=mins))
        mass=list(map(F,r['high_completed_column_mass_upper']));assert mass[0]==F(d28['rows'][idx]['high_completed_column_mass_upper'][0]);checks+=1
        for j,d in enumerate(selected_dicts):
            nm=F(r['exact_selected_column_norm_upper'][j]);assert nm*nm>sum(x*x for x in d.values());checks+=1
            correction=(mass[j+1]-nm)*k;assert correction>0 and correction*correction>F(s['original_selected_complete_source_Gram'][j][j][1]);checks+=1
        gap=1/(sum((ss*m)**2/e for ss,m,e in zip(scale,mass,ell))+1/k);assert gap==F(r['physical_gap_strict_lower'])>F(a['physical_gap_guard'])>F(d28['physical_gap_guard']);checks+=1
        assert F(rp['physical_gap_strict_lower'])>=gap and r['complete_four_column_source_credit']==rp['complete_four_column_source_credit'];checks+=1
        for z in product(range(-1,2),repeat=5):
            norm=sum(abs(x)*ss*m for x,ss,m in zip(z[:4],scale,mass))+abs(z[4]);energy=sum(e*x*x for e,x in zip(ell,z[:4]))+k*z[4]**2;assert energy>=gap*norm*norm;checks+=1
    # Coherent source Cauchy can be saturated; a true positive/null/negative crossing.
    controls=[]
    for rho in [F(99,100),F(1),F(101,100)]:
        d=v.determinant([[F(1),rho],[rho,F(1)]]);assert (d>0)==(rho<1) and (d==0)==(rho==1);checks+=1;controls.append(dict(border=str(rho),determinant=str(d)))
    for lam in [F(1,10),F(1),F(2)]:assert v.determinant([[1+lam,F(1)],[F(1),1+lam]])>0 and (1+lam)-1==lam;checks+=1
    return dict(stage='DNE29',status='PASS',independent_rational_checks=checks,complete_symmetric_box_vertex_checks=records,
        original_low_pairings_primary_replay_reverse_all_overlap=True,selected_columns_exactly_reconstructed=True,retained_components_match_DNE24_constraints=True,
        physical_completion_controls=486,genuine_crossing_controls=controls,certificate_sha256=read(primary)[1],replay_sha256=read(replay)[1],
        complete_remaining_Gram_certified=False,whole_aperture_positive=False)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('manifest');p.add_argument('primary');p.add_argument('replay');p.add_argument('output');a=p.parse_args();m=json.loads(Path(a.manifest).read_bytes())
    r=run(m['consumer_inputs'],m['extra_inputs'],a.primary,a.replay);Path(a.output).write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'checks':r['independent_rational_checks'],'vertices':sum(v['vertices'] for v in r['complete_symmetric_box_vertex_checks'])}))
