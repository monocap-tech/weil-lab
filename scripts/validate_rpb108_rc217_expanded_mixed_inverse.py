"""RC217: compatible ten-trial mixed/action matrices and first eight-source inverse enclosure."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,minus,div,bounds,down,up,sqrtup,psd,ser,loewner
from validate_rpb108_rc134_correlated_six_input_covariance import smul
from validate_rpb108_rc129_four_vector_joint_moment import inv,add,cong,mm
from validate_rpb108_rc177_three_source_canonical_action_gram import mat,scale,width
from validate_rpb108_rc203_residual_enriched_six_source_inverse import inputs as legacy_inputs
ROOT=Path(__file__).resolve().parents[1]
PINS={"certificates/rpb108_rc121_diagonal_metric_equivalence.json":"089664ca7eb9139fec1ba0f58b4cfbf25902f51a","certificates/rpb108_rc127_enriched_even_endpoint_action.json":"b98167d6e34f983cfa4e3e5b3f496931f468da04","certificates/rpb108_rc128_collective_second_response.json":"9f5671fce28949322d02f98a9d2a83f2efb53f8c","certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f","certificates/rpb108_rc132_balanced_action_shared_covariance.json":"035eac34848eb3f8f0a2d65424340050936e980c","certificates/rpb108_rc133_six_vector_joint_matrices.json":"d86fb5a684dc8d0f37517c34fae03f5f1455b78c","certificates/rpb108_rc134_correlated_six_input_covariance.json":"451dd35ea6af09b6d307b39f6cd7156ce92307c3","certificates/rpb108_rc135_common_response_capture.json":"2de31504cf1bc7645d3dc850f147ad6bb0582cfb","certificates/rpb108_rc136_seven_vector_joint_matrices.json":"84ed91819c32053ae78caf340758e7d0c07a9568","certificates/rpb108_rc154_centered_analytic_tail_action.json":"28c2027b223be6d5d137a76d15bbcad3be04d54f","certificates/rpb108_rc170_poisson_regular_action.json":"690b571c35d3f49302223b306488008c9b907272","certificates/rpb108_rc171_regular_legendre_projection.json":"b905565d7c15e557ce41207774dd0e338070650f","certificates/rpb108_rc172_quadratic_regular_action.json":"895448d42fc03b9875dcd3ecf8dd2923ef51a44b","certificates/rpb108_rc174_regular_source_tail_compression.json":"f0e3837e3dc0a6dc03cfa0d9195fa632348313bd","certificates/rpb108_rc175_f0_regular_physical_source.json":"659754cd0766a38413019dbe0141295d8e815877","certificates/rpb108_rc176_f0_regular_output_carrier.json":"f81ba3a2b18abf516fee9837bf59ff3342c4001c","certificates/rpb108_rc177_three_source_canonical_action_gram.json":"0d1dfd962b1eb3e199d6df9f093e32dfd5a0e232","certificates/rpb108_rc178_three_source_canonical_inverse.json":"5e41c31af560052d1949e5c61174109f663dcce2","certificates/rpb108_rc179_focus_residual_canonical_action.json":"1f6a9930e0182635ddebd373fc0b300f136fe069","certificates/rpb108_rc180_residual_enriched_canonical_inverse.json":"8b48993a4d01c58b5c2b2e6ebd3b01f14198fd0a","certificates/rpb108_rc181_psi_action_completion_dashboard.json":"ceed57e11d269b11b1aee30cfe215efab5c37ff0","certificates/rpb108_rc182_four_source_canonical_inverse.json":"6071904d1a7602622028f86e7a52205753c2488e","certificates/rpb108_rc182_materialized_Cpsi_carrier.json":"0eb05b44e2bad1e4c3d2a366c758a563d639a7df","certificates/rpb108_rc183_materialized_w14_canonical_carrier.json":"4469fa1b92e6e1e9f08598ce707cfb43b240784a","certificates/rpb108_rc183_w14_canonical_action.json":"cc4e2d8b95144282eaeeebc980ecf204ed173c66","certificates/rpb108_rc184_five_source_canonical_inverse.json":"4ceedcd939c7eed8bcccab5ab915ca6642ef8e24","certificates/rpb108_rc185_five_source_focus_action.json":"e68b983718244e40b61ae01392156c20a2a76a2a","certificates/rpb108_rc186_residual_enriched_five_source_inverse.json":"11719b721921073aebe5d2356747d6a40aff01d0","certificates/rpb108_rc187_correlated_variational_refinement.json":"38a50d04e1bd99fb7e40329087c2a43795197702","certificates/rpb108_rc188_extended_psi_endpoint_action.json":"91a4bf81150ecf6be696b1004b79a67c2bdbec50","certificates/rpb108_rc188_materialized_Cpsi_carrier.json":"ce137b872381e32291a416ec1a2c247ac97e1a7a","certificates/rpb108_rc189_refined_psi_five_source_inverse.json":"9e1d13385e55c6576bce0806575320f2052546f0","certificates/rpb108_rc190_extended_w14_endpoint_action.json":"aa139a1ddbb285b4c8fc20f5b8b90b910eeae529","certificates/rpb108_rc190_materialized_Cw14_carrier.json":"76627bff4e17f78a6e0ffd4acdac5e459aa7d023","certificates/rpb108_rc191_two_refined_actions_five_source_inverse.json":"efa7dfd9f5e763db340820341f214562a19f47ef","certificates/rpb108_rc192_low_polynomial_regular_actions.json":"1ddada7c8f1e3829ed56bc9725c09f7cfa9e5977","certificates/rpb108_rc193_extended_f0_regular_action.json":"299fc1207f0e90478e0bebd0e082e2981a8c514e","certificates/rpb108_rc194_q185_analytic_endpoint_tail.json":"d98da5ef1042ef2c28f974b11b59ce0b40db6879","certificates/rpb108_rc195_refined_five_source_inverse.json":"a61cc3f75829b151ea2ea77d3574556aac62d8ca","certificates/rpb108_rc196_adaptive_action_error_inverse.json":"9285682f3de512714c7f280148aad9e6959bdff8","certificates/rpb108_rc197_native_v10_canonical_action.json":"6e759211fbc8de8e4b6c4ed5fd4c62a5e5241455","certificates/rpb108_rc198_v10_mixed_action_rows.json":"9f9dfabab81640c79a1b3b21ab54b50dbd7cbb81","certificates/rpb108_rc199_six_source_canonical_inverse.json":"32c08337c0d300a98d74ca0c437df6e66a2fe79d","certificates/rpb108_rc200_extended_v10_endpoint_action.json":"3e0a948321e87b840dae6a83319a2d06dfc8eede","certificates/rpb108_rc200_materialized_Cv10_carrier.json":"4a470657c7dd0b3264174de321f0f8fca0dfa36b","certificates/rpb108_rc201_refined_v10_six_source_inverse.json":"cf224ee3495e23376bff696ee0bac9c81ff9cca7","certificates/rpb108_rc202_six_source_residual_action.json":"695d477b22e41eec7f3b82e7a793794e05ac17bb","certificates/rpb108_rc203_residual_enriched_six_source_inverse.json":"5d321b659367ba459682b557b12ef63451f63e49","certificates/rpb108_rc212_native_t10_canonical_action.json":"442f9963189a32fa8185daf5558e0673753ed0f1","certificates/rpb108_rc213_eight_source_error_interface.json":"23aaa6e712fca038e87603471f59c08066d6a0a9","certificates/rpb108_rc214_correlated_difference_canonical_action.json":"c2599b388cd75d0528635496d9418e061e9385db","certificates/rpb108_rc215_correlated_common_error_preflight.json":"31338be9ef05d8677f2325a6f2fbb708f94fb812","certificates/rpb108_rc216_refined_t10_canonical_action.json":"5073f4155d7f45f5d28bcd5330a107a42bc952e8"}
HELPER_PINS={"scripts/validate_rpb108_rc127_enriched_even_endpoint_action.py":"d5d82bf70c1a178f0fe1da61f27b8623e42ed361","scripts/validate_rpb108_rc129_four_vector_joint_moment.py":"1229dc4a9db7509b9f6afea7116349891b618f4c","scripts/validate_rpb108_rc132_balanced_action_shared_covariance.py":"0a083ba5df42b81db924340972b51ac7e4762920","scripts/validate_rpb108_rc133_six_vector_joint_matrices.py":"f675827ba027147ebc384f2596d994afff9de685","scripts/validate_rpb108_rc134_correlated_six_input_covariance.py":"ac0d5ba0acb48182f0eed3ef452ddca1fbef2f0e","scripts/validate_rpb108_rc170_poisson_regular_action.py":"2224bbdeca1f1e041d37031e5d1ddfc9ad0e986a","scripts/validate_rpb108_rc171_regular_legendre_projection.py":"29a8ab157b16d262a78abe9bf9348a271a34fff5","scripts/validate_rpb108_rc176_f0_regular_output_carrier.py":"38fa42607e423de666ffbb4ebc0f703c7c0fe1d7","scripts/validate_rpb108_rc177_three_source_canonical_action_gram.py":"d9d0575e6dda8e0b6f66ffaf83d0474b2715ba5b","scripts/validate_rpb108_rc179_focus_residual_canonical_action.py":"012cc045537e82d78a51299ffb9c5356a488ac6a","scripts/validate_rpb108_rc184_five_source_canonical_inverse.py":"bb5339138ff3dbc90521fa131f6221e23c49e4f2","scripts/validate_rpb108_rc185_five_source_focus_action.py":"15c017543efd99248b958e0ce48fcc7bb6ac75c1","scripts/validate_rpb108_rc186_residual_enriched_five_source_inverse.py":"afce718195cb46a78224f137dec6de9382ef43f2","scripts/validate_rpb108_rc189_refined_psi_five_source_inverse.py":"544740ee9274417e0ed2d5c0fe385bf476941557","scripts/validate_rpb108_rc191_two_refined_actions_five_source_inverse.py":"b5eab21b3e3098c36f3a0a515d9c1eaed7da8bb9","scripts/validate_rpb108_rc195_refined_five_source_inverse.py":"31fa6e809a06da59f3dea2615d38840be86d8cdc","scripts/validate_rpb108_rc198_v10_mixed_action_rows.py":"46de46eb61fa91894c8315c155c68cfc07735f0b","scripts/validate_rpb108_rc199_six_source_canonical_inverse.py":"85b30e8997b9c8c7eb4166a77c28811e37081834","scripts/validate_rpb108_rc201_refined_v10_six_source_inverse.py":"a3cd26942d90662ad6a351febe5e812c4a9a04d9","scripts/validate_rpb108_rc202_six_source_residual_action.py":"9a072690851db23fb14bd54596ab6af72e9f3f44","scripts/validate_rpb108_rc203_residual_enriched_six_source_inverse.py":"a0e6b3982e757dfb485a3f2b92b06c60a6bacc8e","scripts/validate_rpb108_rc204_signed_error.py":"5362ddfbfaf443875fa7914aa90bb00b58b00281","scripts/validate_rpb108_rc205_signed_error_inverse.py":"2953a3b86fc7560b31ec02c6761483d4f6c39fc1","scripts/validate_rpb108_rc206_directional_error_inverse.py":"7ada815599b8d2b607aed030e38b8daa01801496","scripts/validate_rpb108_rc210_collective_regular_input_tail.py":"03dae85f568ea15d8a0a64482eda41bf0b42bccc","scripts/validate_rpb108_rc216_refined_t10_canonical_action.py":"39a99e7163894018641813f8b8036de295900f28"}
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def run(reverse=False):
    data={}
    for p,sha in HELPER_PINS.items():assert blob((ROOT/p).read_bytes())==sha,(p,'helper Git blob mismatch')
    for p,sha in PINS.items():
        b=(ROOT/p).read_bytes();assert blob(b)==sha,(p,'input Git blob mismatch');data[p]=json.loads(b)
    get=lambda n:data['certificates/rpb108_rc'+n+'.json']
    prior=get('203_residual_enriched_six_source_inverse');dc=get('214_correlated_difference_canonical_action');tc=get('216_refined_t10_canonical_action');joint=get('213_eight_source_error_interface')
    assert tc['correlated_eight_source_half_Gram_action_error_gate_passed']
    path=ROOT/'scripts/validate_rpb108_rc203_residual_enriched_six_source_inverse.py'
    src=path.read_text().split("\nif __name__=='__main__':")[0]
    marker='    joint=dict(expanded_response_source_D_Gram_lower='
    assert src.count(marker)==1;src=src.replace(marker,'    return locals()\n'+marker)
    ns={'__file__':str(path)};exec(compile(src,'RC217 legacy eight-carrier reconstruction','exec'),ns)
    oldstate=ns['run'](legacy_inputs(),reverse);d=oldstate['d'];old=oldstate['old']
    assert ser(d['actionLo'])==prior['nominal_raw_action_Gram_entry_lower'] and list(map(str,d['eps']))==prior['individual_raw_trial_action_error_norm_upper']
    # Reconstruct the entire historical native t polynomial, not just a prefix.
    path=ROOT/'scripts/validate_rpb108_rc216_refined_t10_canonical_action.py'
    src=path.read_text().split("\nif __name__=='__main__':")[0]
    src=src.replace('range(1,2*8190+3)','range(1,2*16382+3)').replace('range(0,8193,2)','range(0,16385,2)')
    assert src.count('for n in range(0,M+1,2):')==1
    src=src.replace('for n in range(0,M+1,2):','for n in range(0,16383,2):')
    marker="    energyLo=F(full['actual_D_Gram_entry_lower'][6][6])"
    assert src.count(marker)==1;src=src.replace(marker,'    return locals()\n'+marker)
    ns={'__file__':str(path)};exec(compile(src,'RC217 complete native t generator','exec'),ns);native=ns['run'](reverse)
    t=native['native'];delta={n:native['z'][n]-native['v'][n] for n in native['z']}
    payload=[dict(degree=r['degree'],center=r['center'],radius=r['generator_radius']) for r in native['prefixRows']]
    digest=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    capture=get('135_common_response_capture');assert digest==capture['finite_output_polynomial_center_radius_sha256']
    deltaHash=hashlib.sha256(json.dumps([dict(degree=n,center=str(delta[n])) for n in sorted(delta)],sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert deltaHash==dc['full_difference_source_sha256']
    print('RC217 full native difference and t hashes verified',flush=True)
    dm=list(map(F,get('134_correlated_six_input_covariance')['z_minus_v_combined_tail_polynomial']));dlambda=4094*4095
    tm=list(map(F,capture['collective_capture_budgets'][1]['analytic_moment_centers']));tlambda=F(capture['tail_Lambda']);assert len(tm)==11
    cp=[{r['degree']:F(r['coefficient_center']) for r in c['endpoint_action_polynomial']} for c in [dc,tc]]
    rp=[{r['degree']:F(r['coefficient_center']) for r in c['regular_action']['D_inverse_regular_polynomial']} for c in [dc,tc]]
    moments=[list(map(F,c['endpoint_signed_moment_coefficients'])) for c in [dc,tc]]
    epLambda=[F(c['endpoint_analytic_lambda']) for c in [dc,tc]]
    O=d['O'];z=(O+2)*(O+3);tail=d['T'];assert O>=16382
    sa=d['sa']+[sum(abs(x)*F(dlambda,z)**k for k,x in enumerate(dm)),sum(abs(x)*F(tlambda,z)**k for k,x in enumerate(tm))]
    va=d['va']+[F(3,2)*sa[8+i]+sum(abs(x)*F(epLambda[i],z)**k for k,x in enumerate(moments[i])) for i in range(2)]
    assert F(old['D'][O][0])>old['r']
    eps=d['eps']+[F(dc['complete_canonical_delta_action_D_error_norm_upper']),F(tc['complete_canonical_t10_action_D_error_norm_upper'])]
    DG=[[Z]*10 for _ in range(2)];left=[[Z]*10 for _ in range(2)];right=[[Z]*10 for _ in range(2)];AQ=[[Z]*10 for _ in range(2)]
    degrees=old['degrees'][::-1] if reverse else old['degrees']
    for n in degrees:
        u,v,mass=d['expandedCache'][n];D=old['D'][n]
        eta=div(rat(F(2*n+1,n*(n+1))),D) if n else Z
        dn=rat(delta[n]) if n<=8190 else smul(eta,rat(sum(dm[k]*F(dlambda,n*(n+1))**k for k in range(len(dm)))))
        tn=rat(t[n]) if n<=16382 else smul(eta,rat(sum(tm[k]*F(tlambda,n*(n+1))**k for k in range(len(tm)))))
        newU=[dn,tn];newV=[]
        for k,c in enumerate([dc,tc]):
            av=plus(newU[k],rat(cp[k].get(n,F(0))+rp[k].get(n,F(0))))
            av=minus(av,smul(div(rat(old['r']),D),newU[k]))
            if n>=4096:av=plus(av,smul(rat(F(1,2)),newU[k]))
            if n>=8192:av=plus(av,smul(eta,rat(sum(moments[k][j]*F(epLambda[k],n*(n+1))**j for j in range(25)))))
            newV.append(av)
        uu=u+newU;vv=v+newV
        for k in range(2):
            for i in range(10):
                DG[k][i]=plus(DG[k][i],smul(mass,smul(uu[i],newU[k])))
                left[k][i]=plus(left[k][i],smul(mass,smul(uu[i],newV[k])))
                right[k][i]=plus(right[k][i],smul(mass,smul(newU[k],vv[i])))
                AQ[k][i]=plus(AQ[k][i],smul(mass,smul(vv[i],newV[k])))
        if n%8192==0:print('RC217 compatible mixed block',n,flush=True)
    expand=lambda A:[row+[F(0)]*2 for row in A]+[[F(0)]*10 for _ in range(2)]
    gl=expand(d['gl']);gh=expand(d['gh']);kl=expand(d['kl']);kh=expand(d['kh']);al=expand(d['actionLo']);ah=expand(d['actionHi'])
    for k in range(2):
        j=8+k
        for i in range(10):
            lo,hi=bounds(DG[k][i]);pay=sa[i]*sa[j]*tail
            gl[i][j]=gl[j][i]=lo if i==j else down(lo-pay);gh[i][j]=gh[j][i]=up(hi+pay)
    norms=[sqrtup(gh[i][i]) for i in range(10)];rows=[]
    for k in range(2):
        j=8+k
        for i in range(10):
            ll,lh=bounds(left[k][i]);rl,rh=bounds(right[k][i]);ql,qh=bounds(AQ[k][i])
            le=up(sa[i]*va[j]*tail+norms[i]*eps[j]);re=up(sa[j]*va[i]*tail+norms[j]*eps[i])
            low=max(down(ll-le),down(rl-re));high=min(up(lh+le),up(rh+re));assert low<=high
            # When both rows are new, intersect their independently calculated
            # self-adjoint enclosures instead of overwriting the earlier row.
            if i==8 and j==9:low=max(low,kl[i][j]);high=min(high,kh[i][j]);assert low<=high
            kl[i][j]=kl[j][i]=low;kh[i][j]=kh[j][i]=high
            lowA=ql if i==j else down(ql-va[i]*va[j]*tail);highA=up(qh+va[i]*va[j]*tail)
            if i==8 and j==9:lowA=max(lowA,al[i][j]);highA=min(highA,ah[i][j]);assert lowA<=highA
            al[i][j]=al[j][i]=lowA;ah[i][j]=ah[j][i]=highA
            err=up(2*norms[i]*eps[j]+2*norms[j]*eps[i]+eps[i]*eps[j])
            rows.append(dict(new_trial_index=j,other_trial_index=i,canonical_pairing_lower=str(low),canonical_pairing_upper=str(high),nominal_action_pairing_lower=str(lowA),nominal_action_pairing_upper=str(highA),actual_action_pairing_error_payment=str(err)))
    # Congruence preserves the original eight-source span. The conditioned
    # source order is the historical six followed by delta and t10.
    A=[[F(0)]*8 for _ in range(8)]
    for j,i in enumerate([0,7,2,1,3,4,5,6]):A[i][j]=F(1)
    A[4][6]=F(-1)
    G=cong(A,mat(joint,'source_D_Gram_rational_floor'));GH=cong(A,mat(joint,'expanded_source_D_Gram_upper'));assert psd(G);inv(G)
    keep=[0,1,2,3,4,6,8,9]
    Klo,Khi,_=loewner([[kl[i][j] for j in keep] for i in keep],[[kh[i][j] for j in keep] for i in keep],[sqrtup(GH[i][i]) for i in range(8)])
    metric=get('121_diagonal_metric_equivalence');a=F(metric['actual_canonical_diagonal_metric_lower']);assert 0<a<2
    KM=scale(F(1,2),add(Klo,Khi));GM=scale(F(1,2),add(G,GH));X=mm(inv(KM),GM)
    X=[[down(x,10**30) for x in row] for row in X];J=[[F(i==j)-X[i][j] for j in range(8)] for i in range(8)]
    # Variational inverse lower bound with a source-span trial:
    # Q >= 2 sym(G_actual X) - X* K_actual X.
    ritz=add(add(G,cong(X,G)),cong(J,GH),-1);ritz=add(ritz,cong(X,Khi),-1)
    structuralLow=scale(F(1,2),G);structuralHigh=scale(1/a,GH)
    # Operator-convex spectral chord on [a,2]:
    # M^-1 <= ((a+2)I-M)/(2a).
    chord=scale(1/(2*a),add(scale(a+2,GH),Klo,-1))
    candidates=[]
    for ln,L in [('structural',structuralLow),('source_span_variational',ritz)]:
        for hn,H in [('structural',structuralHigh),('spectral_chord',chord)]:
            gap=add(H,L,-1)
            if not psd(L) or not psd(gap):continue
            beta=width(gap,G);gate=add(scale(F(1,2),G),gap,-1);assert psd(add(scale(beta,G),gap,-1))
            candidates.append(dict(lower_type=ln,upper_type=hn,inverse_response_lower=ser(L),inverse_response_upper=ser(H),relative_inverse_width_upper=str(beta),half_Gram_gate_passed=psd(gate),half_Gram_gate_matrix=ser(gate)))
    chosen=min(candidates,key=lambda c:(F(c['relative_inverse_width_upper']),c['lower_type'],c['upper_type']))
    print('RC217 first expanded inverse width / gate',chosen['relative_inverse_width_upper'],chosen['half_Gram_gate_passed'],flush=True)
    return dict(milestone='RC217',starting_commit='58119a94295f3bfe1b1f4cf5197d1049f08c4aa5',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,
        raw_trial_order=prior['raw_trial_basis_order']+['delta=z_b6-v10','t10'],conditioned_response_source_order=['P0','P2','f0','psi0','w14','v10','delta=z_b6-v10','t10'],original_response_source_order=joint['response_source_order'],conditioned_to_original_source_matrix=ser(A),
        finite_pairing_prefix_last_degree=O,full_t10_native_finite_center_radius_sha256=digest,full_t10_native_hash_verified=True,full_delta_native_sha256=deltaHash,full_delta_native_hash_verified=True,
        complete_column_action_D_error_norm_upper=list(map(str,eps)),raw_source_D_Gram_entry_lower=ser(gl),raw_source_D_Gram_entry_upper=ser(gh),raw_actual_canonical_Gram_entry_lower=ser(kl),raw_actual_canonical_Gram_entry_upper=ser(kh),raw_nominal_action_Gram_entry_lower=ser(al),raw_nominal_action_Gram_entry_upper=ser(ah),
        new_complete_mixed_action_rows=rows,all_20_new_mixed_rows_supplied=True,full_finite_native_sources_and_signed_infinite_tails_paid=True,source_and_action_carriers_compatible=True,
        conditioned_source_D_Gram_lower=ser(G),conditioned_source_D_Gram_upper=ser(GH),conditioned_canonical_Gram_lower=ser(Klo),conditioned_canonical_Gram_upper=ser(Khi),
        source_span_variational_trial=ser(X),spectral_metric_lower=str(a),evaluated_inverse_enclosures=candidates,selected_inverse_enclosure=chosen,relative_inverse_width_upper=chosen['relative_inverse_width_upper'],canonical_half_Gram_inverse_width_gate_passed=chosen['half_Gram_gate_passed'],
        expanded_eight_source_inverse_response_evaluated=True,inverse_method='source-span variational lower and spectral chord/structural upper; residual-transport refinement remains separate',
        passed_RC216_action_error_factor_unchanged=tc['correlated_eight_source_action_error_factor_upper'],accepted_six_source_inverse_width_unchanged='4361/10000',source_span_expanded_not_same_family_precision_comparison=True,ten_trial_source_independence_not_assumed=True,expanded_finite_residual_Gram_assembled=False,
        complex_response_mixtures_paid=True,Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC218: assemble the ten-trial/eight-response residual and coupled error transport, then refine the first expanded inverse enclosure')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--replay',action='store_true');a=p.parse_args();d=run(a.replay)
    if a.replay:assert json.loads(a.output.read_text())==d
    else:a.output.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
    print('RC217 PASS: expanded inverse enclosure, acceptance',d['canonical_half_Gram_inverse_width_gate_passed'])

