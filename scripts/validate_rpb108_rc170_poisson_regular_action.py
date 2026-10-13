"""RC170: supported regular multiplier via a paid positive Poisson quadrature."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, math
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,lc,hc,rat,plus,minus,mul,div,bounds,up,down,sqrtup

def signed_scale(t,a):
    p=rat(t)
    return min(lc.multiply(x,y) for x in p for y in a),max(hc.multiply(x,y) for x in p for y in a)

def atan_small(x):
    assert 0<=x<=F(1,2)
    a=rat(x);square=mul(a,a);term=a;total=Z
    for k in range(80):
        piece=signed_scale(F((-1)**k,2*k+1),term)
        total=plus(total,piece);term=mul(term,square)
    return total[0],hc.add(total[1],hc.divide(term[1],rat(161)[0]))

def pi_bounds():
    # Machin's identity with alternating rational arctangent enclosures.
    a=atan_small(F(1,5));b=atan_small(F(1,239))
    return minus(signed_scale(16,a),signed_scale(4,b))

def atan_point(x,pi):
    if x<0:return signed_scale(-1,atan_point(-x,pi))
    if x>1:return minus(signed_scale(F(1,2),pi),atan_point(1/x,pi))
    if x>F(1,2):return plus(signed_scale(F(1,4),pi),atan_point((x-1)/(x+1),pi))
    return atan_small(x)

def exp_negative(x):
    assert x[0]>=0
    if x[0]>=100:return rat(0)[0],rat(F(1,2**100))[1]
    # Enclose exp(x/128) by positive Taylor terms and its geometric remainder.
    v=div(x,rat(128));assert v[1]<1
    total=rat(1);term=rat(1)
    for k in range(1,61):term=div(mul(term,v),rat(k));total=plus(total,term)
    nxt=div(mul(term,v),rat(61))
    rem=div(nxt,minus(rat(1),div(v,rat(62))))
    total=(total[0],hc.add(total[1],rem[1]))
    for _ in range(7):total=mul(total,total)
    return div(rat(1),total)

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];audit,metric=json.loads(raw[0]),json.loads(raw[1])
    assert audit['milestone']=='RC169' and metric['milestone']=='RC121'
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert audit['input_sha256'][3]==hs[1]
    sl=F(metric['diagonal_reference_floor_lower']);assert sl>F(19,5)
    # e is enclosed by an exact positive factorial series.
    eLo=sum((F(1,math.factorial(k)) for k in range(61)),F(0))
    eHi=eLo+F(1,math.factorial(61))/(1-F(1,62))
    assert 2<eLo<eHi<F(11,4)
    e=(rat(eLo)[0],rat(eHi)[1])
    t0=F(1,10**6);rootratio=F(257,256);ratio=rootratio**2;N=4096
    y=F(1,513)
    lLo=4*sum((y**(2*k+1)/F(2*k+1) for k in range(20)),F(0))
    lHi=lLo+4*y**41/(41*(1-y*y));delta=(lLo+lHi)/2
    # delta encloses the exact log-cell length 2 log(257/256).
    deltaError=(lHi-lLo)/2;t=rat(t0);nodes=[];roundError=F(0);coefficientHash=hashlib.sha256()
    for j in range(N):
        midpoint=mul(t,rat(rootratio));lo,hi=bounds(midpoint);tc=(lo+hi)/2;terr=(hi-lo)/2
        v=minus(rat(1),exp_negative(mul(e,rat(tc))));al,ah=bounds(v);ac=(al+ah)/2;ar=(ah-al)/2
        assert tc>0 and 0<ac<=1
        # Coefficient uncertainty plus the Poisson-node perturbation. Its
        # logarithmic first derivative has L2 and Linfinity norm <=1.
        local=ar+eHi*terr+terr/lo
        roundError+=delta*local+deltaError
        nodes.append((tc,ac));coefficientHash.update((str(tc)+' '+str(ac)+'\n').encode())
        t=mul(t,rat(ratio))
    endLo,endHi=bounds(t);assert endLo>10**6
    near=up(eHi*t0);far=up(4*B/endLo)
    midL2=up(N*lHi**3/12);midSup=up(N*lHi**3/8)
    roundError=up(roundError);epsilon=up(near+far+midL2+roundError);epsSup=up(near+far+midSup+roundError)
    assert epsilon<F(1,5000) and epsSup<F(1,4000)
    print('RC170 full supported-source Poisson quadrature error paid',flush=True)
    pi=pi_bounds();pl,ph=bounds(pi);assert F(3)<pl<ph<F(22,7)
    xs=[F(0),B/2,B];values={str(x):Z for x in xs}
    sequence=nodes[::-1] if replay else nodes
    for tc,ac in sequence:
        for x in xs:
            parts=[]
            for distance in (B-x,B+x):
                args=div(mul(rat(2*distance),pi),rat(tc));alo,ahi=bounds(args)
                parts.append((atan_point(alo,pi)[0],atan_point(ahi,pi)[1]))
            poisson=div(plus(*parts),pi)
            values[str(x)]=plus(values[str(x)],mul(rat(delta*ac),poisson))
    samples=[]
    for x in xs:
        lo,hi=bounds(values[str(x)]);assert lo>0 and hi-lo<F(1,10**30)
        samples.append(dict(x=str(x),approximant_value_lower=str(lo),approximant_value_upper=str(hi),
          true_regular_action_value_lower=str(down(lo-epsSup)),true_regular_action_value_upper=str(up(hi+epsSup))))
    return dict(milestone='RC170',status='PASS: full supported regular-map contract and constant-source action',
      starting_commit='2af9c9b490a9863e1389d60c95a291f826146469',input_sha256=hs,aperture='11/10',
      regular_multiplier='log(1+e/abs(xi)); Fourier convention exp(-2*pi*i*x*xi)',
      Poisson_kernel='2*t/(t^2+4*pi^2*(x-y)^2)',
      regular_integral='R=integral_0^infty (1-exp(-e*t))*chi*P_t*chi dt/t',
      quadrature_representation='sum_j delta*a_j*chi*P_tc_j*chi; rational nodes and positive rational weights reconstructed by validator',
      logarithmic_cell_count=N,first_t=str(t0),cell_ratio=str(ratio),midpoint_ratio=str(rootratio),
      logarithmic_step_lower=str(lLo),logarithmic_step_upper=str(lHi),rational_step_center=str(delta),
      last_t_lower=str(endLo),last_t_upper=str(endHi),node_coefficient_center_sha256=coefficientHash.hexdigest(),
      e_lower=str(eLo),e_upper=str(eHi),pi_lower=str(pl),pi_upper=str(ph),
      small_t_operator_error_upper=str(near),large_t_operator_error_upper=str(far),
      midpoint_physical_L2_operator_error_upper=str(midL2),midpoint_physical_Linfinity_operator_error_upper=str(midSup),
      node_coefficient_and_step_rounding_error_upper=str(roundError),
      supported_physical_L2_operator_error_norm_upper=str(epsilon),supported_physical_Linfinity_operator_error_norm_upper=str(epsSup),
      D_energy_regular_action_operator_error_norm_upper=str(up(epsilon/sl)),
      arbitrary_physical_source_to_D_inverse_error_squared_factor_upper=str(up(epsilon**2/sl)),
      correlated_regular_action_error_Gram_contract='E^* D E <= epsilon^2/s_lower * Q^*Q <= epsilon^2/s_lower^2 * Q^*D Q; E=D^-1(R-Rhat)Q',
      constant_source_physical_action_error_norm_upper=str(up(sqrtup(2*B)*epsilon)),
      constant_source_D_inverse_action_error_norm_upper=str(sqrtup(2*B*epsilon**2/sl)),
      constant_source_action_samples=samples,constant_source_whole_interval_error_paid=True,
      constant_source_represented_action='delta/pi*sum_j a_j*(atan(2*pi*(B-x)/tc_j)+atan(2*pi*(B+x)/tc_j))',
      full_physical_source_map_contract_certified=True,all_infinite_t_tails_paid=True,quadrature_positive_selfadjoint_and_parity_preserving=True,
      actual_regular_constant_source_evaluated=True,required_full_family_D_coefficients_realized=False,canonical_Riesz_iteration_performed=False,
      Stage_I_closed=False,original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='realize D^-1 of the paid regular approximant in the endpoint carrier and combine it with C and -r D^-1; extend the source action to the required physical family with its full correlated errors')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=2)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC170 PASS: regular multiplier map and constant physical source action')
