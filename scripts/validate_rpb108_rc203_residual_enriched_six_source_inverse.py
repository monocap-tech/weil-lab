"""RC203: paid q202 mixed rows and eight-trial/six-response inverse."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import Z,rat,plus,minus,div,bounds,up,down,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc129_four_vector_joint_moment import inv,add
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale
from validate_rpb108_rc202_six_source_residual_action import inputs as old_inputs,reconstruct

def inputs():
    return [Path(__file__).resolve().parents[1]/'certificates/rpb108_rc202_six_source_residual_action.json']+old_inputs()

def change(src,a,b):
    assert src.count(a)==1,(a,src.count(a))
    return src.replace(a,b)

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw]
    qcert,prior=data[:2];assert qcert['milestone']=='RC202' and prior['milestone']=='RC201'
    assert qcert['input_sha256']==hs[1:] and prior['input_sha256']==hs[2:]
    assert qcert['input_half_norm_budget_passed'] and qcert['full_input_and_infinite_output_tails_paid']
    state=reconstruct(paths[2:],replay);d=state['d'];old=d['d'];O=d['O'];z=d['z'];T=d['T']
    q={r['degree']:F(r['coefficient_center']) for r in qcert['finite_focus_direction']}
    cp={r['degree']:F(r['coefficient_center']) for r in qcert['endpoint_action_polynomial']}
    neg={r['degree']:F(r['coefficient_center']) for r in qcert['negative_r_D_inverse_direction_polynomial']}
    reg={r['degree']:F(r['coefficient_center']) for r in qcert['regular_action']['D_inverse_regular_polynomial']}
    qm=list(map(F,qcert['endpoint_exact_signed_moments']));qlam=F(qcert['endpoint_analytic_lambda'])
    assert len(qm)==25 and qcert['finite_input_degree']==512 and qcert['endpoint_analytic_first_even_degree']==4096
    moment_order=list(range(25));moment_order=moment_order[::-1] if replay else moment_order
    amp=sum(abs(qm[k])*F(qlam,z)**k for k in moment_order);delta=sum(abs(qm[k])*F(qlam,z)**k for k in moment_order if k)
    DG=[Z]*8;left=[Z]*8;right=[Z]*8;AQ=[Z]*8
    for n in old['degrees']:
        u,v,mass=d['expandedCache'][n];qn=rat(q.get(n,F(0)));av=rat(q.get(n,F(0))+cp.get(n,F(0))+neg.get(n,F(0))+reg.get(n,F(0)))
        if n>=4096:
            eta=div(rat(F(2*n+1,n*(n+1))),old['D'][n])
            av=plus(av,smul(eta,rat(sum(qm[k]*F(qlam,n*(n+1))**k for k in moment_order))))
        uu=u+[qn];vv=v+[av];d['expandedCache'][n]=(uu,vv,mass)
        for i in range(8):
            DG[i]=plus(DG[i],smul(mass,smul(uu[i],qn)))
            left[i]=plus(left[i],smul(mass,smul(uu[i],av)))
            right[i]=plus(right[i],smul(mass,smul(qn,vv[i])))
            AQ[i]=plus(AQ[i],smul(mass,smul(vv[i],av)))
        if n%8192==0:print('RC203 q202 mixed block',n,flush=True)
    expand=lambda A:[row+[F(0)] for row in A]+[[F(0)]*8]
    gl=expand(d['gl']);gh=expand(d['gh']);kl=expand(d['kl']);kh=expand(d['kh']);al=expand(d['actionLo']);ah=expand(d['actionHi'])
    for i in range(8):
        lo,hi=bounds(DG[i]);gl[i][7]=gl[7][i]=lo;gh[i][7]=gh[7][i]=hi
    weights=[sqrtup(gh[i][i]) for i in range(8)];eps=d['eps']+[F(qcert['complete_actual_canonical_q_action_D_error_norm_upper'])]
    sa=d['sa']+[F(0)];va=d['va']+[amp];rows=[]
    for i in range(8):
        ll,lh=bounds(left[i]);rl,rh=bounds(right[i]);ql,qh=bounds(AQ[i])
        le=up(sa[i]*amp*T+weights[i]*eps[7]);re=up(weights[7]*eps[i])
        low=max(down(ll-le),down(rl-re));high=min(up(lh+le),up(rh+re))
        if i==7:
            low=max(low,F(qcert['actual_q_canonical_pairing_lower']));high=min(high,F(qcert['actual_q_canonical_pairing_upper']))
        assert low<=high
        kl[i][7]=kl[7][i]=low;kh[i][7]=kh[7][i]=high
        lowA=ql if i==7 else down(ql-va[i]*amp*T);highA=up(qh+va[i]*amp*T)
        al[i][7]=al[7][i]=lowA;ah[i][7]=ah[7][i]=highA
        error=up(2*weights[i]*eps[7]+2*weights[7]*eps[i]+eps[i]*eps[7])
        rows.append(dict(other_raw_trial_index=i,source_pairing_lower=str(gl[i][7]),source_pairing_upper=str(gh[i][7]),canonical_pairing_lower=str(low),canonical_pairing_upper=str(high),nominal_action_pairing_lower=str(lowA),nominal_action_pairing_upper=str(highA),actual_action_pairing_lower=str(down(lowA-error)),actual_action_pairing_upper=str(up(highA+error)),actual_action_error_payment_upper=str(error)))
    # Entry enclosures include both signed infinite source tails. Converting
    # the full matrix to Loewner endpoints pays all correlated entry widths.
    Glo,Ghi,_=loewner(gl,gh,weights);assert psd(Glo);inv(Glo)
    d.update(gl=gl,gh=gh,kl=kl,kh=kh,actionLo=al,actionHi=ah,Glo=Glo,Ghi=Ghi,eps=eps,sa=sa,va=va)
    joint=dict(expanded_response_source_D_Gram_lower=prior['source_D_Gram_lower'],expanded_response_source_D_Gram_upper=prior['source_D_Gram_upper'],response_source_order=prior['response_source_order'],raw_trial_basis_order=prior['raw_trial_basis_order']+['q202'])
    path=Path(__file__).with_name('validate_rpb108_rc199_six_source_canonical_inverse.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    start=src.index('    keep=[0,1,2,3,4,6]');end=src.index('\ndef run(')
    src=src[:end]+'\ndef solve(d,joint,hs,replay=False):\n'+src[start:]
    src=src.replace('range(7)','range(8)')
    src=change(src,"    results=[]", "    dq202=QDELTA\n    results=[]")
    src=change(src,"-vlead*Y[6][j] for j in range(6)]", "-vlead*Y[6][j]-QM0*Y[7][j] for j in range(6)]")
    src=change(src,"(vm,Y[6])]:rem=", "(vm,Y[6]),(dq202,Y[7])]:rem=")
    src=change(src,'scale(21*T,rem)','scale(24*T,rem)')
    src=change(src,"[('refined',lower),('structural',scale(F(1,2),GSlo))]", "[('refined',lower),('structural',scale(F(1,2),GSlo)),('inherited',mat(PRIOR['selected_enclosure'],'canonical_inverse_response_lower'))]")
    src=change(src,"[('refined',upper),('structural',scale(1/a,GShi))]", "[('refined',upper),('structural',scale(1/a,GShi)),('inherited',mat(PRIOR['selected_enclosure'],'canonical_inverse_response_upper'))]")
    ns={'__file__':str(path),'QDELTA':delta,'QM0':qm[0],'PRIOR':prior}
    exec(compile(src,'RC203 eight-trial inverse with eight-term tail payment','exec'),ns)
    result=ns['solve'](d,joint,hs,replay)
    assert result['source_D_Gram_lower']==prior['source_D_Gram_lower'] and result['source_D_Gram_upper']==prior['source_D_Gram_upper']
    result.update(milestone='RC203',status='PASS: q202 mixed rows and enriched six-source inverse; acceptance separately reported',starting_commit='7fc63d0356e3bd218d2dcd4cf0f9e3527a822e6f',input_sha256=hs,q202_complete_mixed_rows=rows,raw_trial_D_Gram_entry_lower=ser(gl),raw_trial_D_Gram_entry_upper=ser(gh),raw_trial_D_Gram_Loewner_lower=ser(Glo),raw_trial_D_Gram_Loewner_upper=ser(Ghi),raw_trial_canonical_Gram_entry_lower=ser(kl),raw_trial_canonical_Gram_entry_upper=ser(kh),nominal_raw_action_Gram_entry_lower=ser(al),nominal_raw_action_Gram_entry_upper=ser(ah),individual_raw_trial_action_error_norm_upper=list(map(str,eps)),q202_signed_tail_moments=list(map(str,qm)),q202_tail_absolute_amplitude_upper=str(amp),q202_tail_nonleading_amplitude_upper=str(delta),eight_trial_independence_verified=True,six_response_source_Gram_unchanged=True,previous_same_family_width_upper=prior['relative_inverse_width_upper'],inverse_width_improved_over_RC201=F(result['relative_inverse_width_upper'])<F(prior['relative_inverse_width_upper']),source_family_expanded_not_same_family_precision_comparison=False,native_source_frame_unchanged=True,next_cursor='refine the paid enriched six-source inverse if gate remains open; native z_b6/t10 coverage subsequent')
    print('RC203 selected width/gate',result['relative_inverse_width_upper'],result['canonical_half_Gram_inverse_width_gate_passed'],flush=True)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC203 PASS')
