"""RC159: conditioned common-eta source Gram tail with signed cancellation."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import psd,ser,up
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths]
    audit,interface,joint,w,v,z,t=map(json.loads,raw)
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert [d['milestone'] for d in (audit,interface,joint,w,v,z,t)]==['RC158','RC155','RC136','RC128','RC131','RC132','RC135']
    assert audit['input_sha256'][2]==hs[1] and audit['input_sha256'][5]==hs[2]
    assert joint['input_sha256'][0]==hs[6] and joint['input_sha256'][3]==hs[5]
    assert joint['input_sha256'][4]==hs[4] and joint['input_sha256'][7]==hs[3]
    mat=lambda d,k:[[F(x) for x in row] for row in d[k]]
    W=mat(interface,'source_frame_matrix');X=mat(audit,'conditioned_source_transform');U=mm(W,X)
    GL=mat(joint,'actual_D_Gram_Loewner_lower');oldGU=mat(joint,'actual_D_Gram_Loewner_upper')
    oldtail=list(map(F,joint['analytic_tail_D_energy_upper']))
    # RC136's upper is its finite-prefix upper plus seven independent tails.
    prefixUpper=add(oldGU,[[7*oldtail[i] if i==j else F(0) for j in range(7)] for i in range(7)],-1)
    prefixLower=GL
    assert psd(prefixLower) and psd(add(prefixUpper,prefixLower,-1))
    moments=[[],[F(1)],[],list(map(F,w['collective_response_enrichment_budgets'][2]['analytic_moment_center_coefficients'])),
      list(map(F,v['collective_capture_budgets'][1]['analytic_moment_center_coefficients'])),
      list(map(F,z['balanced_action_and_shared_covariance_budgets'][1]['analytic_moment_centers'])),
      list(map(F,t['collective_capture_budgets'][1]['analytic_moment_centers']))]
    scales=[0,0,0,988*989,4094*4095,4094*4095,8190*8191]
    first=16384*16385;count=max(map(len,moments))
    native=[[moments[i][k]*F(scales[i],first)**k if k<len(moments[i]) else F(0) for k in range(count)] for i in range(7)]
    coefficients=mm(transpose(native),U)
    leading=coefficients[0]
    orders=list(range(1,count));orders=orders[::-1] if reverse else orders
    remainder=[sum(abs(coefficients[k][j]) for k in orders) for j in range(7)]
    T=oldtail[1];assert T>0
    # For x=first/[n(n+1)] in (0,1], each conditioned source tail
    # equals eta_n*(a_j+sum_{k>=1} b_kj*x^k). Combine signed b_kj
    # before absolute values. The residual column energies are <=T*r_j²;
    # Cauchy pays every mixture by 7T diag(r_j²). Young combines that
    # residual with the shared rank-one leading eta feature.
    leadingMatrix=[[T*x*y for y in leading] for x in leading]
    remainderMatrix=[[7*T*remainder[i]**2 if i==j else F(0) for j in range(7)] for i in range(7)]
    GLo=cong(U,prefixLower);prefixHi=cong(U,prefixUpper);oldHi=cong(U,oldGU)
    assert GLo==mat(audit,'conditioned_source_Gram_lower')
    def width(gap):
        def yes(n):return psd(add([[F(n,10**6)*v for v in row] for row in GLo],gap,-1))
        hi=1
        while not yes(hi):hi*=2
        lo=0
        while hi-lo>1:
            mid=(hi+lo)//2
            if yes(mid):hi=mid
            else:lo=mid
        assert yes(hi) and not yes(lo)
        return F(hi,10**6)
    candidates=[];best=None
    parameters=[F(1,1000),F(1,100),F(1,50),F(1,20),F(1,10),F(1,2),F(1)]
    if reverse:parameters.reverse()
    for tau in parameters:
        tail=add([[(1+tau)*v for v in row] for row in leadingMatrix],[[(1+1/tau)*v for v in row] for row in remainderMatrix])
        GHi=add(prefixHi,tail);gap=add(GHi,GLo,-1);assert psd(tail) and psd(gap)
        beta=width(gap);candidates.append(dict(tau=str(tau),relative_Gram_width_upper=str(beta)))
        if best is None or (beta,tau)<best[0]:best=((beta,tau),GHi,tail)
    (beta,tau),GHi,tail=best
    previous=F(audit['source_Gram_enclosure_relative_width_upper'])
    assert beta<previous/20
    witness=list(map(F,audit['enclosure_width_failure_witness']))
    quad=lambda A:sum(witness[i]*A[i][j]*witness[j] for i in range(7) for j in range(7))
    qlo=quad(GLo);oldwidth=quad(add(oldHi,GLo,-1));newwidth=quad(add(GHi,GLo,-1))
    assert qlo>0 and 0<newwidth<oldwidth
    # Native-coordinate upper retains the same full seven-source carrier.
    order=[0,2,3,4,6,1,5];P=[[F(j==i) for j in range(7)] for i in order]
    Wi=mm(inv(mm(P,W)),P);Ui=mm(inv(X),Wi)
    assert mm(U,Ui)==[[F(i==j) for j in range(7)] for i in range(7)]
    nativeHi=cong(Ui,GHi);assert psd(add(nativeHi,GL,-1))
    candidates.sort(key=lambda d:F(d['tau']))
    return dict(milestone='RC159',status='PASS: correlated common-eta source Gram tail refinement',
      starting_commit='8ee21aeb4fdbebfca69ed28f30f836202a5e5061',input_sha256=hs,aperture='11/10',
      finite_Gram_prefix_degree=16382,first_omitted_even_degree=16384,
      native_scaled_tail_polynomial_coefficients=ser(native),
      conditioned_scaled_tail_polynomial_coefficients=ser(coefficients),
      conditioned_leading_eta_coefficients=list(map(str,leading)),
      conditioned_higher_moment_amplitude_upper=list(map(str,remainder)),
      common_eta_tail_D_energy_upper=str(T),selected_Young_parameter=str(tau),candidate_widths=candidates,
      conditioned_correlated_tail_Gram_upper=ser(tail),
      conditioned_source_Gram_lower=ser(GLo),conditioned_source_Gram_upper=ser(GHi),
      native_source_Gram_Loewner_upper=ser(nativeHi),
      relative_source_Gram_width_upper=str(beta),previous_relative_source_Gram_width_upper=str(previous),
      global_width_bound_improvement_factor=str(previous/beta),
      RC158_witness_source_Gram_lower=str(qlo),RC158_witness_old_Gram_width=str(oldwidth),
      RC158_witness_new_Gram_width=str(newwidth),RC158_witness_new_width_over_lower=str(newwidth/qlo),
      RC158_witness_width_improvement_factor=str(oldwidth/newwidth),
      structural_inverse_width_upper_after_Gram_refinement=str(F(1,2)+beta),
      shared_leading_tail_correlation_retained=True,signed_source_combination_before_absolute_values=True,
      original_lower_Gram_and_source_frame_unchanged=True,
      variational_inverse_enclosure_rerun=False,half_Gram_inverse_width_gate_passed=False,
      original_Weil_or_augmented_actions_performed=False,
      whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='transport the correlated tail Gram bound into the conditioned functional and residual intervals; rerun the seven-source variational inverse enclosure and matrix-width gate')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=7)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC159 PASS: correlated source Gram tail')
