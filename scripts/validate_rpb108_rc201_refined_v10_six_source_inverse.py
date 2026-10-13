"""RC201: rebuild the unchanged six-source inverse with RC200's full v10 action."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc199_six_source_canonical_inverse import inputs as old_inputs

def inputs():
    base=Path(__file__).resolve().parents[1]/'certificates'
    return [base/('rpb108_rc'+n+'.json') for n in ['200_extended_v10_endpoint_action','200_materialized_Cv10_carrier','199_six_source_canonical_inverse']]+old_inputs()

def replace(src,a,b):
    assert src.count(a)==1,(a,src.count(a))
    return src.replace(a,b)

def refine198(src):
    marker="    cp={x['degree']:F(x['coefficient_center']) for x in new['endpoint_action_polynomial']}"
    src=replace(src,marker,"    mom=[F(x['center']) for x in NEW_CARRIER['analytic_output_moments'][:25]];epLam=F(NEW_CARRIER['analytic_output_lambda'])\n    cp={2*i:F(int(c),int(NEW_CARRIER['finite_center_scale'])) for i,c in enumerate(NEW_CARRIER['finite_Cv10_coefficient_center_numerators'])}\n"+marker)
    # The legacy statement starts with cp and also defines neg/reg; remove
    # only the old cp assignment while retaining the actual correction data.
    src=replace(src,marker+';', '    ')
    src=replace(src,"        if n>=514:av=plus(av,minus(smul(rat(F(1,2)),vn),smul(div(rat(d['r']),dn),vn)))", "        if n>=514:av=minus(av,smul(div(rat(d['r']),dn),vn))\n        if n>=32768:av=plus(av,smul(rat(F(1,2)),vn))")
    src=replace(src,'        if n>=1538:av=', '        if n>=65536:av=')
    src=replace(src,"eps=list(d['eps'])+[F(new['complete_canonical_v10_action_D_error_norm_upper'])]", "eps=list(d['eps'])+[F(NEW_CERT['complete_canonical_v10_action_D_error_norm_upper'])]")
    return src

def run(paths,replay=False):
    raw=[p.read_bytes() for p in paths];data=list(map(json.loads,raw));hs=[hashlib.sha256(b).hexdigest() for b in raw]
    new,carrier,previous=data[:3]
    assert [x['milestone'] for x in data[:3]]==['RC200','RC200-Cv10-carrier','RC199']
    assert previous['input_sha256']==hs[3:] and new['input_sha256'][0]==hs[2]
    assert new['materialized_endpoint_carrier_sha256']==hs[1]
    assert new['native_v10_source_unchanged'] and not new['new_inverse_response_evaluated']
    assert carrier['source_prefix_degree']==32766 and carrier['output_prefix_degree']==65534 and carrier['centered_input_tail_first_even_degree']==32768
    assert carrier['whole_Cv10_error_norm_upper']==new['complete_endpoint_v10_D_error_norm_upper']
    path=Path(__file__).with_name('validate_rpb108_rc199_six_source_canonical_inverse.py');src=path.read_text().split("\nif __name__=='__main__':")[0]
    marker="    marker='    DG=[Z]*7;left=[Z]*7;right=[Z]*7;AQ=[Z]*7'"
    src=replace(src,marker,'    src=REFINE198(src)\n'+marker)
    src=replace(src,"ns={'__file__':str(path)};exec(compile(src,", "ns={'__file__':str(path),'NEW_CERT':NEW_CERT,'NEW_CARRIER':NEW_CARRIER};exec(compile(src,")
    src=replace(src," and ser(d['actionLo'])==joint['nominal_raw_action_Gram_entry_lower']",'')
    src=replace(src,"[('refined',lower),('structural',scale(F(1,2),GSlo))]", "[('refined',lower),('structural',scale(F(1,2),GSlo)),('inherited',mat(PREVIOUS['selected_enclosure'],'canonical_inverse_response_lower'))]")
    src=replace(src,"[('refined',upper),('structural',scale(1/a,GShi))]", "[('refined',upper),('structural',scale(1/a,GShi)),('inherited',mat(PREVIOUS['selected_enclosure'],'canonical_inverse_response_upper'))]")
    src=replace(src,"return dict(milestone='RC199'", "return dict(raw_trial_canonical_Gram_entry_lower=ser(d['kl']),raw_trial_canonical_Gram_entry_upper=ser(d['kh']),nominal_raw_action_Gram_entry_lower=ser(d['actionLo']),nominal_raw_action_Gram_entry_upper=ser(d['actionHi']),milestone='RC199'")
    ns={'__file__':str(path),'REFINE198':refine198,'NEW_CERT':new,'NEW_CARRIER':carrier,'PREVIOUS':previous}
    exec(compile(src,'RC201 fully refined v10 six-source inverse','exec'),ns);result=ns['run'](paths[3:],replay)
    assert result['source_D_Gram_lower']==previous['source_D_Gram_lower'] and result['source_D_Gram_upper']==previous['source_D_Gram_upper']
    result.update(milestone='RC201',status='PASS: same-family six-source inverse rebuilt with RC200 v10 carrier; gate separately reported',starting_commit='e8739e482f3b4f0dc6da2d1b7d353a226a550b34',input_sha256=hs,previous_same_family_width_upper=previous['relative_inverse_width_upper'],refined_v10_canonical_action_error_norm_upper=new['complete_canonical_v10_action_D_error_norm_upper'],refined_v10_endpoint_carrier_sha256=hs[1],RC200_complete_carrier_and_analytic_output_tail_attached=True,all_mixed_rows_and_residuals_recomputed=True,source_family_expanded_not_same_family_precision_comparison=False,same_six_sources_operator_norm_and_Gram_normalization_as_RC199=True,inverse_width_improved_over_RC199=F(result['relative_inverse_width_upper'])<F(previous['relative_inverse_width_upper']),next_cursor='tighten remaining regular/action payments or enrich actual residual if gate remains open; native z_b6/t10 coverage stays subsequent')
    print('RC201 selected width/gate',result['relative_inverse_width_upper'],result['canonical_half_Gram_inverse_width_gate_passed'],flush=True)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();r=run(inputs(),a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC201 PASS')
