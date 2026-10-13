"""RC171: paid Legendre projection of the regular constant-source action."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
import argparse, hashlib, json, math
from validate_rpb108_rc127_enriched_even_endpoint_action import B,up,down,sqrtup

L=Context(prec=360,rounding=ROUND_FLOOR);H=Context(prec=360,rounding=ROUND_CEILING)
ZERO=(D(0),D(0));TOL=D('1e-300')
def rat(x):
    x=F(x);return L.divide(D(x.numerator),D(x.denominator)),H.divide(D(x.numerator),D(x.denominator))
def add(a,b):return L.add(a[0],b[0]),H.add(a[1],b[1])
def sub(a,b):return L.subtract(a[0],b[1]),H.subtract(a[1],b[0])
def mul(a,b):
    if b[0]>=0:
        if a[0]>=0:return L.multiply(a[0],b[0]),H.multiply(a[1],b[1])
        if a[1]<=0:return L.multiply(a[0],b[1]),H.multiply(a[1],b[0])
        return L.multiply(a[0],b[1]),H.multiply(a[1],b[1])
    if a[0]>=0:return mul(b,a)
    if a[1]<=0 and b[1]<=0:return L.multiply(a[1],b[1]),H.multiply(a[0],b[0])
    return min(L.multiply(x,y) for x in a for y in b),max(H.multiply(x,y) for x in a for y in b)
def scale(c,a):
    c=F(c)
    if c.denominator==1:
        d=D(c.numerator)
        if c>=0:return L.multiply(d,a[0]),H.multiply(d,a[1])
        return L.multiply(d,a[1]),H.multiply(d,a[0])
    return mul(rat(c),a)
def div_int(a,n):return L.divide(a[0],D(n)),H.divide(a[1],D(n))
def divide(a,b):
    assert b[0]>0
    return mul(a,(L.divide(D(1),b[1]),H.divide(D(1),b[0])))
def endpoints(a):return down(F(a[0])),up(F(a[1]))

def atan_small(x):
    assert 0<=x<=F(1,2)
    term=rat(x);sq=mul(term,term);total=ZERO
    for k in range(900):
        total=add(total,scale(F((-1)**k,2*k+1),term));term=mul(term,sq)
        error=H.divide(term[1],D(2*k+3))
        if error<TOL:return L.subtract(total[0],error),H.add(total[1],error)
    raise AssertionError('arctangent remainder not paid')
def pi_bounds():return sub(scale(16,atan_small(F(1,5))),scale(4,atan_small(F(1,239))))
def atan(x,pi):
    if x<0:return scale(-1,atan(-x,pi))
    if x>1:return sub(scale(F(1,2),pi),atan(1/x,pi))
    if x>F(1,2):return add(scale(F(1,4),pi),atan((x-1)/(x+1),pi))
    return atan_small(x)
def log_point(x):
    assert x>0
    k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def core(v):
        y=(v-1)/(v+1);a=rat(y);sq=mul(a,a);term=a;total=ZERO
        for j in range(600):
            total=add(total,scale(F(2,2*j+1),term));term=mul(term,sq)
            rem=divide(scale(F(2,2*j+3),term),sub(rat(1),sq))[1]
            if rem<TOL:return total[0],H.add(total[1],rem)
        raise AssertionError('logarithm remainder not paid')
    if not hasattr(log_point,'log_two'):log_point.log_two=core(F(2))
    return add(core(x),scale(k,log_point.log_two))

def double_factorial(n):
    return math.prod(range(n,0,-2))

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths];regular,audit,metric,joint=map(json.loads,raw)
    assert [d['milestone'] for d in (regular,audit,metric,joint)]==['RC170','RC169','RC121','RC129']
    hs=[hashlib.sha256(b).hexdigest() for b in raw]
    assert regular['input_sha256']==hs[1:3] and audit['input_sha256'][3]==hs[2]
    src=Path(__file__).with_name('validate_rpb108_rc170_poisson_regular_action.py').read_text()
    src=src[:src.index("\nif __name__=='__main__':")]
    src=src.replace('    pi=pi_bounds();pl,ph=bounds(pi);assert F(3)<pl<ph<F(22,7)','    return locals()',1)
    ns={};exec(compile(src,'RC170 reconstruction','exec'),ns)
    d=ns['run'](paths[1:3]);nodes=d['nodes'];delta=d['delta']
    assert d['coefficientHash'].hexdigest()==regular['node_coefficient_center_sha256']
    N=256;pi=pi_bounds();p=(F(regular['pi_lower'])+F(regular['pi_upper']))/2
    piError=max(p-F(regular['pi_lower']),F(regular['pi_upper'])-p)
    low=[ZERO for _ in range(N+1)];farMom=[ZERO for _ in range(32)];farRemainder=F(0);weights=F(0);nearCount=farCount=0
    seq=nodes[::-1] if replay else nodes
    for tc,ac in seq:
        weight=delta*ac;weights+=weight;c=2*p*B/tc
        if c<F(1,4):
            power=rat(c);sq=rat(c*c)
            for k in range(32):farMom[k]=add(farMom[k],scale(weight,power));power=mul(power,sq)
            farRemainder+=up(weight*2*(2*c)**65/(65*p))
            farCount+=1;continue
        h=1/c;hr=rat(h);wr=rat(weight);minusWeight=rat(-2*weight/p)
        q0=(scale(F(1,4),log_point(1+4*c*c)),scale(F(-1,2),atan(2*c,pi)))
        q1=(sub(sub(q0[0],mul(hr,q0[1])),rat(1)),add(q0[1],mul(hr,q0[0])))
        qs=[q0,q1]
        for n in range(1,N+1):
            zq=(sub(qs[-1][0],mul(hr,qs[-1][1])),add(qs[-1][1],mul(hr,qs[-1][0])))
            qs.append(tuple(div_int(sub(scale(2*n+1,zq[i]),scale(n,qs[-2][i])),n+1) for i in range(2)))
        a0=scale(1/p,sub(scale(-4,q0[1]),scale(2*h,q0[0])))
        low[0]=add(low[0],mul(wr,a0))
        for n in range(2,N+1,2):low[n]=add(low[n],mul(minusWeight,sub(qs[n+1][1],qs[n-1][1])))
        nearCount+=1
        if nearCount%512==0:print('RC171 exact Poisson-Legendre node block',nearCount,flush=True)
    # For small c the alternating arctangent expansion is uniformly paid.
    # Combine signed far-node moments before polynomial-to-Legendre projection.
    poly=[ZERO for _ in range(63)]
    for k,moment in enumerate(farMom):
        for j in range(0,2*k+2,2):poly[j]=add(poly[j],scale(F(2*(-1)**k*math.comb(2*k+1,j),(2*k+1)*p),moment))
    for n in range(0,63,2):
        for j in range(n,63,2):
            factor=F((2*n+1)*math.factorial(j),double_factorial(j-n)*double_factorial(j+n+1))
            low[n]=add(low[n],scale(factor,poly[j]))
    print('RC171 finite regular-source Legendre coefficients paid',flush=True)
    sl=F(joint['actual_D_Gram_entry_lower'][0][0])/(2*B);sh=F(joint['actual_D_Gram_entry_upper'][0][0])/(2*B)
    assert sl>F(metric['diagonal_reference_floor_lower'])-F(1,10**20)
    harmonic=F(0);entries=[];roundSquared=F(0);physicalRoundSquared=F(0)
    for n in range(N+1):
        if n:harmonic+=F(1,n)
        if n%2:continue
        lo,hi=endpoints(low[n]);center=(lo+hi)/2;radius=(hi-lo)/2
        assert hi-lo<F(1,10**30)
        dl,dh=sl+harmonic,sh+harmonic
        a=divide(rat(center),(rat(dl)[0],rat(dh)[1]));al,ah=endpoints(a);trial=(al+ah)/2;ar=max(abs(trial-al),abs(trial-ah))
        m=2*B/F(2*n+1);roundSquared+=m*dh*ar*ar;physicalRoundSquared+=m*radius*radius
        entries.append(dict(degree=n,represented_regular_source_coefficient_lower=str(lo),represented_regular_source_coefficient_upper=str(hi),D_inverse_trial_coefficient=str(trial)))
    # Changing pi in the Poisson kernel costs <=4*piError/pi_min per term.
    phase=up(4*piError/F(regular['pi_lower'])*weights);farRemainder=up(farRemainder)
    epsilon=F(regular['supported_physical_L2_operator_error_norm_upper'])
    physicalError=up(sqrtup(2*B)*(epsilon+phase+farRemainder)+sqrtup(physicalRoundSquared))
    # Use a rational LOWER square root when dividing an error norm.
    rootSl=sqrtup(sl)-F(1,10**40);assert rootSl>0 and rootSl*rootSl<=sl
    lowError=up(physicalError/rootSl+sqrtup(roundSquared))
    I2=up(F(regular['e_upper'])*F(regular['pi_upper'])**2/3)
    differentialNorm=up(sqrtup(8*B*B*I2)+4*F(regular['e_upper'])*B*sqrtup(2*B))
    # RP0 is even. Its first omitted degree is N+2.
    nextDegree=N+2;Hnext=harmonic+F(1,N+1)+F(1,N+2);z=nextDegree*(nextDegree+1)
    tailSquared=up(differentialNorm**2/(z*z*(sl+Hnext)))
    totalSquared=up(lowError**2+tailSquared);total=sqrtup(totalSquared)
    ln2=log_point(F(2));l2lo,l2hi=endpoints(ln2)
    correction=divide(sub(rat(1-F(789,125)),ln2),(rat(sl)[0],rat(sh)[1]));cl,ch=endpoints(correction);cc=(cl+ch)/2
    correctionError=up(sqrtup(2*B*sh)*(ch-cl)/2)
    actionError=up(total+correctionError)
    r0lo,r0hi=endpoints(low[0]);pairError=epsilon+phase+farRemainder
    canonicalGramLo=down(2*B*(sl+1-l2hi-F(789,125)+r0lo-pairError))
    canonicalGramHi=up(2*B*(sh+1-l2lo-F(789,125)+r0hi+pairError))
    assert canonicalGramHi>=canonicalGramLo>2*B*F(257,252)
    assert total<F(1,5000) and actionError<F(1,5000)
    return dict(milestone='RC171',status='PASS: full regular constant-source D inverse and canonical first action',starting_commit='2fb1048057f4e0fc60c235f1ecfef42f3cea6fbe',input_sha256=hs,aperture='11/10',
      maximum_even_trial_degree=N,first_omitted_even_degree=nextDegree,physical_regular_coefficient_enclosures=entries,
      near_Poisson_node_count=nearCount,far_Poisson_node_count=farCount,far_arctangent_retained_terms=32,
      far_arctangent_source_uniform_error_upper=str(farRemainder),Poisson_pi_replacement_operator_error_upper=str(phase),
      coefficient_and_D_constant_rounding_error_squared_upper=str(up(roundSquared)),
      projected_regular_action_D_error_norm_upper=str(lowError),
      regular_source_Legendre_differential_norm_upper=str(differentialNorm),
      full_omitted_D_inverse_regular_source_energy_upper=str(tailSquared),
      full_D_inverse_regular_constant_source_error_squared_upper=str(totalSquared),full_D_inverse_regular_constant_source_error_norm_upper=str(total),
      canonical_constant_action_P0_correction_center=str(cc),canonical_constant_action_P0_correction_error_norm_upper=str(correctionError),
      canonical_constant_action_representation='M_L P0 approx (1+correction_center)P0+f0+psi0+regular_D_inverse_polynomial; M_L=D^-1 L',
      canonical_constant_action_D_error_norm_upper=str(actionError),
      actual_canonical_constant_direction_Gram_lower=str(canonicalGramLo),actual_canonical_constant_direction_Gram_upper=str(canonicalGramHi),
      constant_direction_metric_interval_is_not_global_coercivity_improvement=True,
      weighted_second_derivative_tail_uses_actual_regular_action=True,all_omitted_coefficients_paid=True,
      regular_source_legendre_carrier_realized=True,canonical_constant_source_first_action_certified=True,
      full_seven_source_canonical_action_realized=False,canonical_Riesz_iteration_performed=False,Stage_I_closed=False,
      original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
      next_cursor='extend the paid regular-carrier action to the required physical source family or execute a correlated canonical inverse correction with all successive endpoint and regular action contracts paid')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--replay',action='store_true');p.add_argument('inputs',nargs=4)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC171 PASS: regular source carrier and canonical first action')
