"""RC202: finite actual six-source residual approximation and full canonical action."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,div,bounds,down,up,sqrtup
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc186_residual_enriched_five_source_inverse import total
from validate_rpb108_rc176_f0_regular_output_carrier import root,lower_root
from validate_rpb108_rc171_regular_legendre_projection import rat as hrat,divide,endpoints
from validate_rpb108_rc201_refined_v10_six_source_inverse import inputs as old_inputs

def inputs():
    base=Path(__file__).resolve().parents[1]/'certificates'
    return [base/'rpb108_rc201_refined_v10_six_source_inverse.json']+old_inputs()

def reconstruct(paths,replay):
    path=Path(__file__).with_name('validate_rpb108_rc201_refined_v10_six_source_inverse.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    marker="    ns={'__file__':str(path),'REFINE198':refine198,'NEW_CERT':new,'NEW_CARRIER':carrier,'PREVIOUS':previous}"
    assert src.count(marker)==1
    src=src.replace(marker,"    src=replace(src,'    results=[]','    return locals()\\n    results=[]')\n"+marker)
    marker="result=ns['run'](paths[3:],replay)";assert src.count(marker)==1;src=src.replace(marker,"return ns['run'](paths[3:],replay)")
    ns={'__file__':str(path)};exec(compile(src,'RC202 immutable complete residual reconstruction','exec'),ns)
    return ns['run'](paths,replay)

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw];prior=data[0]
    assert prior['milestone']=='RC201' and prior['input_sha256']==hs[1:]
    d=reconstruct(paths[1:],replay);selected=prior['selected_enclosure'];Y=[[F(x) for x in row] for row in selected['trial_basis_coefficients']]
    assert prior['source_D_Gram_lower']==[[str(x) for x in row] for row in d['GSlo']]
    probes={'mixed_gate_probe':list(map(F,['-3/1000','3/250','-129/1000','1','109/250','-107/250'])),'P0_coordinate':[F(1)]+[F(0)]*5}
    candidates=[];polynomials={}
    for name in sorted(probes,reverse=replay):
        probe=probes[name];y=[sum(Y[k][j]*probe[j] for j in range(6)) for k in range(7)]
        quadratic=lambda key:sum(probe[i]*F(selected[key][i][j])*probe[j] for i in range(6) for j in range(6))
        adaptiveError=root(quadratic('adaptive_action_error_Gram_upper'));directError=up(sum(abs(y[k])*d['eps'][k] for k in range(7)));actualError=min(adaptiveError,directError)
        actualLower=down(lower_root(quadratic('nominal_residual_Gram_lower'))-actualError);assert actualLower>0
        rows=[];energyRadius={256:F(0),512:F(0)};omitted={256:F(0),512:F(0)}
        for n in d['old']['degrees']:
            u,v,mass=d['d']['expandedCache'][n]
            value=minus(total([smul(rat(probe[j]),u[d['keep'][j]]) for j in range(6)]),total([smul(rat(y[k]),v[k]) for k in range(7)]))
            lo,hi=bounds(value);mh=bounds(mass)[1]
            if n<=512:
                c=down((lo+hi)/2);rad=max(c-lo,hi-c);rows.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)))
            for M in [256,512]:
                if n<=M:energyRadius[M]+=up(mh*rad*rad)
                else:omitted[M]+=up(mh*max(abs(lo),abs(hi))**2)
        rows.sort(key=lambda x:x['degree']);tail=quadratic('nominal_residual_tail_Gram_upper');assert tail>=0
        for M in [256,512]:
            nominal=root(energyRadius[M]+omitted[M]+tail);error=up(nominal+actualError);relative=up(error/actualLower)
            row=dict(focus=name,source_probe=list(map(str,probe)),finite_input_degree=M,inverse_trial_focus_coefficients=list(map(str,y)),nominal_input_rounding_D_energy_upper=str(up(energyRadius[M])),omitted_finite_input_D_energy_upper=str(up(omitted[M])),omitted_analytic_input_D_energy_upper=str(up(tail)),nominal_residual_to_polynomial_D_error_norm_upper=str(up(nominal)),adaptive_nominal_to_actual_residual_error_norm_upper=str(up(adaptiveError)),direct_nominal_to_actual_residual_error_norm_upper=str(directError),selected_nominal_to_actual_residual_error_norm_upper=str(up(actualError)),actual_residual_D_norm_lower=str(actualLower),actual_residual_to_polynomial_D_error_norm_upper=str(error),actual_residual_to_polynomial_relative_D_norm_error_upper=str(relative),input_half_norm_budget_passed=relative<F(1,2))
            candidates.append(row);polynomials[(name,M)]=[r for r in rows if r['degree']<=M]
            print('RC202 focus/cutoff/relative',name,M,float(relative),flush=True)
    candidates.sort(key=lambda x:(x['focus'],x['finite_input_degree']))
    chosen=min(candidates,key=lambda x:(F(x['actual_residual_to_polynomial_relative_D_norm_error_upper']),x['finite_input_degree'],x['focus']))
    M=chosen['finite_input_degree'];qrows=polynomials[(chosen['focus'],M)];q={r['degree']:F(r['coefficient_center']) for r in qrows}
    base=d['old'];D=base['D'];metricIndex=[x['milestone'] for x in data].index('RC121');metric=data[metricIndex];regular=data[[x['milestone'] for x in data].index('RC170')];joint=data[[x['milestone'] for x in data].index('RC129')]
    assert metric['endpoint_form_bound']=='0 <= h <= J + 2 log(2) I <= D'
    path=Path(__file__).with_name('validate_rpb108_rc179_focus_residual_canonical_action.py');src=path.read_text().split("\nif __name__=='__main__':")[0];assert src.count('K=192;N=768;J=')==1;src=src.replace('K=192;N=768;J=','K=192;N=1536;J=')
    ns={'__file__':str(path)};exec(compile(src,'RC202 finite regular action','exec'),ns)
    helper=Path(__file__).with_name('validate_rpb108_rc171_regular_legendre_projection.py');hsrc=helper.read_text().split("\nif __name__=='__main__':")[0];assert hsrc.count('prec=360')==2 and hsrc.count("TOL=D('1e-300')")==1
    hsrc=hsrc.replace('prec=360','prec=600').replace("TOL=D('1e-300')","TOL=D('1e-540')");private={};exec(compile(hsrc,'RC202 private directed interval helpers','exec'),private)
    for k in ['ZERO','rat','add','sub','mul','scale','divide','div_int','endpoints','log_point']:ns[k]=private[k]
    ns['root']=lambda x,grid=10**600:root(x,grid)
    reg=ns['regular_action'](q,regular,joint,replay)
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    log=(rat(1-F(joint['actual_endpoint_pairing_entry_upper'][0][0])/(2*B))[0],rat(1-F(joint['actual_endpoint_pairing_entry_lower'][0][0])/(2*B))[1])
    O=4094;H=[Z]
    for n in range(1,2*O+1):H.append(plus(H[-1],rat(F(1,n))))
    endpoint=[];negative=[];ee=F(0);ne=F(0);qlo=qhi=F(0)
    for n in (range(O,-1,-2) if replay else range(0,O+1,2)):
        value=Z
        for m in sorted(q,reverse=replay):
            entry=minus(plus(minus(smul(rat(2),H[2*n]),smul(rat(2),H[n])),rat(F(1,2*n+1))),log) if n==m else rat(F(2*n+1,abs(n-m)*(n+m+1)))
            value=plus(value,smul(entry,rat(q[m])))
        # The signed numerator requires general directed division.
        lo,hi=endpoints(divide((value[0],value[1]),D[n]));c=down((lo+hi)/2);rad=max(c-lo,hi-c)
        endpoint.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)));ee+=up(2*B/F(2*n+1)*F(D[n][1])*rad*rad)
        if n<=M:
            lo,hi=endpoints(divide(hrat(-base['r']*q[n]),D[n]));c=(lo+hi)/2;rad=(hi-lo)/2;negative.append(dict(degree=n,coefficient_center=str(c),coefficient_radius=str(rad)));ne+=up(2*B/F(2*n+1)*F(D[n][1])*rad*rad)
            qlo+=down(2*B/F(2*n+1)*F(D[n][0])*q[n]**2);qhi+=up(2*B/F(2*n+1)*F(D[n][1])*q[n]**2)
    endpoint.sort(key=lambda x:x['degree']);negative.sort(key=lambda x:x['degree']);assert qlo>0
    lam=M*(M+1);rho=F(lam,(O+2)*(O+3));moments=[sum(q[m]*F(m*(m+1),lam)**k for m in sorted(q,reverse=replay)) for k in range(25)]
    A=sum(abs(c) for c in q.values());T=up(B/(F(D[O][0])*(O-1)*O));tailError=up(root(T)*A*rho**25/(1-rho),10**80)
    endpointError=up(root(ee+tailError*tailError));actionError=up(endpointError+root(ne)+F(reg['complete_D_inverse_regular_action_error_norm_upper']))
    transferred=up(actionError+2*F(chosen['actual_residual_to_polynomial_D_error_norm_upper']))
    cp={r['degree']:F(r['coefficient_center']) for r in endpoint};np={r['degree']:F(r['coefficient_center']) for r in negative};rp={r['degree']:F(r['coefficient_center']) for r in reg['D_inverse_regular_polynomial']}
    pair=Z
    for n in sorted(q,reverse=replay):pair=plus(pair,smul(rat(2*B/F(2*n+1)*q[n]*(q[n]+cp[n]+np[n]+rp.get(n,F(0)))),D[n]))
    lo,hi=bounds(pair);pay=root(qhi)*actionError;actualLo=down(lo-pay);actualHi=up(hi+pay)
    assert actualLo>F(metric['actual_canonical_diagonal_metric_lower'])*qhi and actualHi<2*qlo
    print('RC202 selected/action error',chosen['focus'],M,float(actionError),flush=True)
    return dict(milestone='RC202',status='PASS: finite six-source residual direction with complete canonical action; approximation budget separately reported',starting_commit='4b44c5fa403d50de6dab0b2c64d86e21bc8d6b4d',input_sha256=hs,aperture='11/10',canonical_operator='M=D^-1 L',norm='D energy',response_source_order=prior['response_source_order'],evaluated_focus_approximation_candidates=candidates,selected_focus_approximation=chosen,finite_focus_direction_definition='q202=exact rounded finite prefix of RC201 selected represented residual on the selected probe; distinct from q179 and q185',finite_focus_direction=qrows,finite_input_degree=M,finite_focus_D_energy_lower=str(qlo),finite_focus_D_energy_upper=str(qhi),regular_action=reg,endpoint_action_polynomial=endpoint,endpoint_output_degree=O,endpoint_analytic_first_even_degree=O+2,endpoint_analytic_lambda=str(lam),endpoint_exact_signed_moments=list(map(str,moments)),endpoint_analytic_coefficient_formula='eta_n*sum_k=0..24 moment_k*(lambda/[n(n+1)])^k',endpoint_analytic_remainder_D_norm_upper=str(tailError),endpoint_action_full_D_error_norm_upper=str(endpointError),negative_r_D_inverse_direction_polynomial=negative,negative_r_coefficient_error_D_energy_upper=str(up(ne)),complete_actual_canonical_q_action_D_error_norm_upper=str(actionError),complete_actual_focus_residual_action_D_error_norm_upper=str(transferred),actual_q_canonical_pairing_lower=str(actualLo),actual_q_canonical_pairing_upper=str(actualHi),canonical_q_pairing_a_D_to_2_D_verified=True,input_half_norm_budget_passed=chosen['input_half_norm_budget_passed'],full_input_and_infinite_output_tails_paid=True,enriched_inverse_response_evaluated=False,latest_six_source_inverse_width_upper=prior['relative_inverse_width_upper'],six_source_acceptance_closed=False,native_source_frame_unchanged=True,Stage_I_closed=False,Stage_I_completion_ratio=None,RH=False,F4=False,Lean=False,next_cursor='add q202 to the six-source inverse trial space, pay its mixed rows and re-evaluate acceptance')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC202 PASS')
