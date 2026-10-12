"""RC157: direct old/new cross pairings of seven paid source actions."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,mul,div,bounds,down,up,sqrtup,ser
from validate_rpb108_rc134_correlated_six_input_covariance import smul
def reconstruct(name,cut,paths,reverse):
    path=Path(__file__).with_name(name);src=path.read_text();ns={'__file__':str(path)}
    exec(compile(src[:src.index(cut)]+'\n    return locals()\n','RC157-'+name,'exec'),ns)
    return ns['run'](paths,reverse)

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths];last,frame,wresponse,vresponse,tresponse=data=list(map(json.loads,raw))
    assert [x['milestone'] for x in data]==['RC156','RC138','RC128','RC131','RC135']
    # RC156's nine declared inputs are recovered from its checkpoint hashes.
    directory=Path(paths[0]).parent
    names=['rpb108_rc154_centered_analytic_tail_action.json','rpb108_rc153_correlated_difference_action.json',
      'rpb108_rc155_seven_source_action_interface.json','rpb108_rc129_four_vector_joint_moment.json',
      'rpb108_rc130_remaining_covariance.json','rpb108_rc134_correlated_six_input_covariance.json',
      'rpb108_rc132_balanced_action_shared_covariance.json','rpb108_rc131_finite_part_response_capture.json',
      'rpb108_rc151_complement_schur.json']
    earlier=[str(directory/n) for n in names]
    assert [hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in earlier]==last['input_sha256']
    assert hashlib.sha256(raw[3]).hexdigest()==last['input_sha256'][7]
    assert frame['input_sha256'][2]==hashlib.sha256(raw[4]).hexdigest()
    assert frame['input_sha256'][4]==hashlib.sha256(raw[2]).hexdigest()
    r=reconstruct('validate_rpb108_rc156_complement_direct_pairings.py','    return dict(',earlier,reverse)
    assert ser(r['QL'])==last['trial_source_pairing_entry_lower']
    assert ser(r['RU'])==last['trial_Gram_entry_upper']
    p,d=r['p'],r['d'];O=p['O'];dn=p['dn'];diag=p['diag']
    hashpayload=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert wresponse['input_sha256'][0]==r['joint']['input_sha256'][1]
    assert frame['input_sha256'][3]==last['input_sha256'][6]
    alpha=F(r['balanced']['alpha'])
    mu=list(map(F,wresponse['collective_response_enrichment_budgets'][2]['analytic_moment_center_coefficients']))
    nuv=list(map(F,vresponse['collective_capture_budgets'][1]['analytic_moment_center_coefficients']))
    nuz=list(map(F,r['balanced']['balanced_action_and_shared_covariance_budgets'][1]['analytic_moment_centers']))
    nut=list(map(F,tresponse['collective_capture_budgets'][1]['analytic_moment_centers']))
    vf={x['degree']:F(x['center']) for x in d['vp_payload']}
    zf={x['degree']:F(x['center']) for x in d['zp_payload']}
    common={n:(vf[n]+zf[n])/2 for n in vf};jobs=sorted(common,reverse=reverse)
    tf={};tpayload=[]
    for n in range(0,O+1,2):
        value=Z
        for m in jobs:
            entry=diag[n] if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,mul(entry,rat(common[m])))
        lo,hi=bounds(div(value,dn[n]));center=down((lo+hi)/2);radius=max(center-lo,hi-center)
        tf[n]=rat(center);tpayload.append(dict(degree=n,center=str(center),radius=str(radius)))
        if n and n%4096==0:print('RC157 t finite output through',n,flush=True)
    assert hashpayload(tpayload)==tresponse['finite_output_polynomial_center_radius_sha256']
    print('RC157 all collective finite polynomial hashes verified',flush=True)
    native=[{},r['sp'],{},{},{},{},tf]
    def eta(n):return div(rat(F(2*n+1,n*(n+1))),dn[n])
    for n in range(0,O+1,2):
        native[0][n]=rat(F(n==0));native[2][n]=eta(n) if 2<=n<=988 else Z
        if n<=4094:native[3][n]=rat(d['g'][n])
        else:native[3][n]=smul(eta(n),rat(sum(v*F(988*989,n*(n+1))**k for k,v in enumerate(mu))))
        for i,finite,moments in ((4,vf,nuv),(5,zf,nuz)):
            if n<=8190:native[i][n]=rat(finite[n])
            else:native[i][n]=smul(eta(n),rat(sum(v*F(4094*4095,n*(n+1))**k for k,v in enumerate(moments))))
    W=[[F(x) for x in row] for row in r['interface']['source_frame_matrix']]
    T=[[F(x) for x in row] for row in frame['trial_action_approximation_matrix']]
    def vector(coeff):
        out={}
        for n in range(0,O+1,2):
            value=Z
            for i in range(7):
                if coeff[i]:value=plus(value,smul(rat(coeff[i]),native[i][n]))
            out[n]=value
        return out
    sources=[vector([W[i][j] for i in range(7)]) for j in range(5)]
    oldtrials=[vector([T[i][j] for i in range(7)]) for j in range(5)]
    # Beyond O, all native analytic vectors share eta_n. Scale polynomial
    # coefficients at the first omitted degree, then retain signed products.
    first=(O+2)*(O+3)
    polys=[[],[F(1)],[],[v*F(988*989,first)**k for k,v in enumerate(mu)],
      [v*F(4094*4095,first)**k for k,v in enumerate(nuv)],
      [v*F(4094*4095,first)**k for k,v in enumerate(nuz)],
      [v*F(8190*8191,first)**k for k,v in enumerate(nut)]]
    def poly(coeff):
        return [sum(coeff[i]*(polys[i][k] if k<len(polys[i]) else F(0)) for i in range(7)) for k in range(max(map(len,polys)))]
    sp=[poly([W[i][j] for i in range(7)]) for j in range(5)]
    tq=[poly([T[i][j] for i in range(7)]) for j in range(5)]
    degrees=r['degrees']
    def pair(a,b,pa,pb):
        value=Z
        for n in degrees:
            mass=smul(rat(2*B/F(2*n+1)),dn[n])
            value=plus(value,smul(mass,smul(a[n],b[n])))
        lo,hi=bounds(value)
        terms=[x*y for x in pa for y in pb]
        return down(lo+p['T']*sum(min(F(0),x) for x in terms)),up(hi+p['T']*sum(max(F(0),x) for x in terms))
    newQlo=[[F(0)]*5 for _ in range(2)];newQhi=[[F(0)]*5 for _ in range(2)]
    oldQlo=[[F(0)]*2 for _ in range(5)];oldQhi=[[F(0)]*2 for _ in range(5)]
    crossRlo=[[F(0)]*2 for _ in range(5)];crossRhi=[[F(0)]*2 for _ in range(5)]
    for i in range(5):
        for j in range(2):
            newQlo[j][i],newQhi[j][i]=pair(r['trials'][j],sources[i],r['tp'][j],sp[i])
            oldQlo[i][j],oldQhi[i][j]=pair(oldtrials[i],r['sources'][j],tq[i],r['ss'][j])
            crossRlo[i][j],crossRhi[i][j]=pair(oldtrials[i],r['trials'][j],tq[i],r['tp'][j])
    # Both directions pay each symmetric endpoint entry. No trial-source
    # matrix symmetry, mixed-error sign, or tail orthogonality is assumed.
    interface=r['interface'];GU=[[F(x) for x in row] for row in interface['full_source_Gram_upper']]
    eps=list(map(F,interface['action_column_D_norm_error_upper']))
    norms=[sqrtup(GU[i][i]) for i in range(7)]
    HL=[[F(0)]*2 for _ in range(5)];HU=[[F(0)]*2 for _ in range(5)];improvement=[]
    for i in range(5):
        for j in range(2):
            lo=F(interface['source_endpoint_pairing_entry_lower'][i][j+5]);hi=F(interface['source_endpoint_pairing_entry_upper'][i][j+5])
            width=hi-lo
            lo=max(lo,down(oldQlo[i][j]-eps[i]*norms[j+5]),down(newQlo[j][i]-eps[j+5]*norms[i]))
            hi=min(hi,up(oldQhi[i][j]+eps[i]*norms[j+5]),up(newQhi[j][i]+eps[j+5]*norms[i]))
            assert lo<=hi
            HL[i][j]=lo;HU[i][j]=hi
            improvement.append(dict(old_source=i,new_source=j,inherited_width=str(width),direct_width=str(hi-lo),width_reduction_factor=str(width/(hi-lo)) if hi>lo else 'exact'))
    assert all(x['width_reduction_factor']=='exact' or F(x['width_reduction_factor'])>=1 for x in improvement)
    assert any(x['width_reduction_factor']=='exact' or F(x['width_reduction_factor'])>2 for x in improvement)
    return dict(milestone='RC157',status='PASS: direct five-by-two mixed source and trial Gram blocks',
        starting_commit='50a537144260f63e735d2d2b579a785f8c097ea3',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],RC156_dependency_sha256=last['input_sha256'],
        implicit_RC152_input_sha256=last['implicit_RC152_input_sha256'],aperture='11/10',
        old_source_order=interface['source_frame'][:5],new_source_order=['psi0','z_b6-v10'],
        finite_pairing_prefix_degree=O,all_new_and_collective_trial_hashes_verified=True,
        new_trial_old_source_pairing_lower=ser(newQlo),new_trial_old_source_pairing_upper=ser(newQhi),
        old_trial_new_source_pairing_lower=ser(oldQlo),old_trial_new_source_pairing_upper=ser(oldQhi),
        old_trial_new_trial_Gram_lower=ser(crossRlo),old_trial_new_trial_Gram_upper=ser(crossRhi),
        source_endpoint_five_by_two_lower=ser(HL),source_endpoint_five_by_two_upper=ser(HU),
        endpoint_cross_width_improvements=improvement,
        all_ten_endpoint_cross_entries_paid_in_both_action_directions=True,
        all_ten_mixed_trial_Gram_entries_paid=True,
        signed_analytic_tail_polynomial_products_paid=True,
        complete_seven_source_pairing_interface_available=True,
        seven_source_inverse_response_certified=False,
        original_Weil_or_augmented_actions_performed=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
        next_cursor='assemble seven-source variational inverse-response matrix from RC149 old block, RC156 complement block, and RC157 cross blocks; certify positive lower and full matrix width separately')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=5)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC157 PASS: five-by-two direct mixed pairings')
