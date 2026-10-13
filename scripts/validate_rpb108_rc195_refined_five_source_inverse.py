"""RC195: full mixed inverse reconstruction with RC192--194 action carriers."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc191_two_refined_actions_five_source_inverse import inputs as base_inputs,refine184 as prior_refine184

def inputs():
    root=Path(__file__).resolve().parents[1]/'certificates'
    return [root/('rpb108_rc'+n+'.json') for n in ['192_low_polynomial_regular_actions','193_extended_f0_regular_action','194_q185_analytic_endpoint_tail','191_two_refined_actions_five_source_inverse']]+base_inputs()

def change(src,old,new,count=1):
    assert src.count(old)==count,(old,src.count(old))
    return src.replace(old,new)

def refine184(src):
    src=prior_refine184(src)
    marker="    q={x['degree']:F(x['coefficient_center']) for x in qcert['finite_focus_direction']}"
    src=change(src,marker,"    r0={x['degree']:F(x['coefficient_center']) for x in LOW['actions'][0]['regular_action']['D_inverse_regular_polynomial']};r2={x['degree']:F(x['coefficient_center']) for x in LOW['actions'][1]['regular_action']['D_inverse_regular_polynomial']}\n    rf={x['degree']:F(x['coefficient_center']) for x in FZERO['regular_action']['D_inverse_regular_polynomial']}\n"+marker)
    return src

def refine186(src):
    # All finite q185 endpoint tail coefficients are reconstructed, not just
    # its old error number. RC194 signs remain in every finite mixed row.
    src=change(src,"'REFINED_W_CARRIER':REFINED_W_CARRIER}","'REFINED_W_CARRIER':REFINED_W_CARRIER,'LOW':LOW,'FZERO':FZERO}")
    marker="    eps=list(map(F,data[10]['individual_full_action_D_error_norm_upper']))"
    src=change(src,marker,"    qmom=[F(x['exact_signed_coefficient']) for x in QTAIL['analytic_tail_moments']];qlam=F(QTAIL['analytic_tail_lambda'])\n    eps=[F(LOW['actions'][0]['complete_canonical_action_D_error_norm_upper']),F(LOW['actions'][1]['complete_canonical_action_D_error_norm_upper']),F(FZERO['canonical_f0_trial_D_error_norm_upper'])]")
    src=change(src,"F(new['complete_actual_canonical_q_action_D_error_norm_upper'])","F(QTAIL['complete_actual_canonical_q_action_D_error_norm_upper'])")
    marker="        u,v,mass=d['cache'][n];u=[u[i] for i in [0,1,2,4,5]]+[rat(q.get(n,F(0)))];v=[v[i] for i in [0,1,2,4,5]]+[rat(vq.get(n,F(0)))];cache[n]=(u,v,mass)"
    replacement="        u,v,mass=d['cache'][n];u=[u[i] for i in [0,1,2,4,5]]+[rat(q.get(n,F(0)))];v=[v[i] for i in [0,1,2,4,5]]+[rat(vq.get(n,F(0)))]\n        if n>=4096:v[5]=plus(v[5],smul(div(rat(F(2*n+1,n*(n+1))),D[n]),rat(sum(qmom[k]*F(qlam,n*(n+1))**k for k in range(25)))))\n        cache[n]=(u,v,mass)"
    src=change(src,marker,replacement)
    src=change(src,"Aw,Ap,F(3,2)*Aw+Bw,F(0)","Aw,Ap,F(3,2)*Aw+Bw,sum(abs(qmom[k])*F(qlam,z)**k for k in range(25))")
    src=change(src,"lo,hi=bounds(mixed[i][j]);ml[i][j]=lo;mh[i][j]=up(hi+sa[i]*va[j]*T)","lo,hi=bounds(mixed[i][j]);ml[i][j]=down(lo-sa[i]*va[j]*T) if j==5 else lo;mh[i][j]=up(hi+sa[i]*va[j]*T)")
    src=change(src,"ql[i][j]=ql[j][i]=lo;qh[i][j]=qh[j][i]=up(hi+va[i]*va[j]*T)","ql[i][j]=ql[j][i]=down(lo-va[i]*va[j]*T) if i!=j and (i==5 or j==5) else lo;qh[i][j]=qh[j][i]=up(hi+va[i]*va[j]*T)")
    src=change(src,"F(new['actual_q_canonical_pairing_lower']),F(new['actual_q_canonical_pairing_upper'])","F(QTAIL['actual_q_canonical_pairing_lower']),F(QTAIL['actual_q_canonical_pairing_upper'])")
    return src

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw]
    low,fzero,qtail,previous=data[:4]
    assert [x['milestone'] for x in data[:4]]==['RC192','RC193','RC194','RC191']
    assert previous['input_sha256']==hs[4:] and qtail['input_sha256'][0]==hs[1] and fzero['input_sha256'][0]==hs[0]
    assert low['input_sha256'][0]==hs[3]
    assert qtail['input_sha256'][1]==hs[[x['milestone'] for x in data].index('RC185')]
    assert qtail['analytic_tail_first_even_degree']==4096 and len(qtail['analytic_tail_moments'])==25
    assert [x['source'] for x in low['actions']]==['P0','P2']
    path=Path(__file__).with_name('validate_rpb108_rc191_two_refined_actions_five_source_inverse.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    src=change(src,"    marker='    for name in sorted(trials,reverse=replay):';assert src.count(marker)==1","    src=REFINE186(src)\n    marker='    for name in sorted(trials,reverse=replay):';assert src.count(marker)==1")
    src=change(src,"'REFINED_W_CERT':newW}","'REFINED_W_CERT':newW,'LOW':LOW,'FZERO':FZERO,'QTAIL':QTAIL}")
    src=change(src,"    assert prior['source_D_Gram_lower']==ser(Glo)","    prior=PREVIOUS\n    assert prior['source_D_Gram_lower']==ser(Glo)")
    # The new signed analytic q185 tail has a nonzero leading eta term.
    src=change(src,"-(cw0*mu[0]+d['omega'][0])*Y[4][j] for j in range(5)]","-(cw0*mu[0]+d['omega'][0])*Y[4][j]-d['qmom'][0]*Y[5][j] for j in range(5)]")
    marker="        tailHi=add(scale(F(3,2)*T,outer(lead)),scale(12*T,rem));Nhi=add(prefixHi,tailHi)"
    replacement="        dq=sum(abs(d['qmom'][k])*F(d['qlam'],d['z'])**k for k in range(1,25))\n        rem=add(rem,scale(dq*dq,outer(Y[5])))\n        tailHi=add(scale(F(3,2)*T,outer(lead)),scale(15*T,rem));Nhi=add(prefixHi,tailHi)"
    src=change(src,marker,replacement)
    ns={'__file__':str(path),'REFINE186':refine186,'LOW':low,'FZERO':fzero,'QTAIL':qtail,'PREVIOUS':previous}
    exec(compile(src,'RC195 full historical inverse refinement','exec'),ns)
    ns['refine184']=refine184
    result=ns['run'](paths[4:],replay)
    result.update(milestone='RC195',status='PASS: fully reconstructed five-source inverse with RC192--194; gate separately reported',starting_commit='1271113c5c7b9e7617f8c20e7a272b7f9496dda0',input_sha256=hs,RC192_low_polynomial_actions_attached=True,RC193_f0_regular_action_attached=True,RC194_signed_q185_analytic_endpoint_tail_attached=True,analytic_q185_tail_moments=qtail['analytic_tail_moments'],analytic_q185_tail_lambda=qtail['analytic_tail_lambda'],signed_q185_mixed_tail_lower_and_upper_paid=True,inverse_width_improved_over_RC191=F(result['relative_inverse_width_upper'])<F(previous['relative_inverse_width_upper']),same_operator_norm_and_five_response_sources_as_RC191=True,next_cursor='inspect same-family residual and action uncertainty if acceptance remains open; otherwise extend native v10/z_b6/t10 coverage')
    # The generated legacy return has historical comparison labels. Preserve
    # their provenance but make the active comparison RC191 explicit.
    result['historical_generator']='RC191 variational solver with explicit RC195 carrier/tail refinements'
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC195 PASS')
