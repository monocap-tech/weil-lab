"""Exact controls for the NF66 supported tail-defect floor.

The all-vector theorem is analytic; finite samples do not establish it.
Uses unchanged NF64 rational physical witnesses, not discovered new vectors.
"""
from fractions import Fraction as F
from pathlib import Path
import json
try:
    from validate_native_archimedean_tail_repair import bernoulli
except ModuleNotFoundError:
    from scripts.validate_native_archimedean_tail_repair import bernoulli


def ceiling(x):
    return (x.numerator+x.denominator-1)//x.denominator


def floor_budget(N,m,B):
    q=F(4*N+1,4)
    k=ceiling(4*B)
    return F(2)/(F(3)**ceiling(q+1)*q*F(64)**m
                 *(64+(1+1/q)**2)*k*k)


def run():
    checks=0
    def check(v):
        nonlocal checks
        assert v
        checks+=1
    b=bernoulli(34)
    epsilon=abs(b[34])/(17*F(129,4)**34)
    rows=[]
    for B in [F(1),F(21,20),F(2),F(10)]:
        q=F(129,4)
        k=ceiling(4*B)
        lower=floor_budget(32,16,B)
        check(k>=4*B)
        check(0<lower<epsilon<F(1,10**40))
        for j in range(17):
            t=1+F(j,16)/q
            check(k*t/2>=2*B)
            check(t**33>=1)
            check(q*t<=q+1<=ceiling(q+1))
            # The n=1 summand lower bound uses b_1=(2pi)^2<64.
            # Test exact rational denominator controls, NOT pi samples.
            for beta in [F(36),F(40),F(63)]:
                term=2*t**33/(beta**16*(beta+t*t))
                bound=2/(F(64)**16*(64+(1+1/q)**2))
                check(term>bound)
        rows.append({'aperture_cap':str(B),'translation_steps':k,
                     'kappa_numerator':str(lower.numerator),
                     'kappa_denominator':str(lower.denominator)})
    check(floor_budget(32,16,F(21,20))>F(2,10**50))
    # Arbitrary supported rational step functions: exact continuous shifts.
    root=Path(__file__).resolve().parents[1]
    data=json.loads((root/'notes/data/RPB108_ARCH_CUTOFF32_WITNESSES_20261008.json').read_text())
    for w in data['witnesses']:
        a=F(w['a']); values=[F(n,w['value_denominator']) for n in w['cell_value_numerators']]
        d=2*a/len(values)
        corr=[sum((values[i]*values[i+j] for i in range(len(values)-j)),F(0))
              for j in range(len(values))]+[F(0)]
        mass=d*corr[0]
        def correlation(s):
            if s>=2*a: return F(0)
            cells=s/d
            index=cells.numerator//cells.denominator
            frac=cells-index
            return d*((1-frac)*corr[index]+frac*corr[index+1])
        for j in range(17):
            t=1+F(j,16)/F(129,4);s=t/2;k=ceiling(4*a)
            check(correlation(k*s)==0)
            check(mass-correlation(s)>=mass/(k*k))
            check(mass-correlation(s)<=2*mass)
    # Exactly coupled retained/complement control: comparison contacts while
    # the original Schur block is still positive. All perturbed blocks retained.
    kappa=floor_budget(32,16,F(21,20))
    defect=2*kappa
    mixing=F(2,3)
    original_complement=F(1)
    comparison_complement=original_complement-defect
    check(comparison_complement>0)
    for sigma in [F(1),F(1,10**32)]:
        # Original A=[[sigma(1-t)+mixing^2,mixing],[mixing,1]].
        # Subtract defect*I from both diagonal blocks, not just retained block.
        threshold=defect*(1+mixing**2/comparison_complement)/sigma
        contact=1-threshold
        check(0<contact<1)
        original_S=sigma*(1-contact)
        lower_S=original_S+mixing**2-defect-mixing**2/comparison_complement
        check(original_S>0)
        check(lower_S==0)
        check(defect*(1+mixing**2)<=original_S)
        # At original contact t=1 the repaired graph trial is negative.
        graph_mass=1+mixing**2
        check(-defect*graph_mass<0)
        # Relative defect diverges on ORIGINAL-positive retained graph vectors.
        ratios=[]
        for j in range(1,21):
            original_S=sigma/F(2)**j
            ratio=defect*graph_mass/original_S
            check(ratio>0)
            if ratios: check(ratio==2*ratios[-1])
            ratios.append(ratio)
    # Positive original eigenlevel never becomes original zero by subtraction.
    for mu in [kappa/2,kappa,2*kappa,F(1)]:
        check(mu-(mu-defect)==defect)
        check((mu-defect)-mu==-defect)
        check(mu>0)
    return {'passed':True,'exact_checks':checks,
            'N':32,'even_corrections':16,
            'uniform_supported_floor_at_cap_21_20_strict_lower':'2/10^50',
            'floor_budgets':rows,
            'original_witnesses_reused':2,
            'new_original_negative_vector':False,
            'hypothetical_contact_only':True,
            'new_aperture_certificate':False,
            'arithmetic_relative_loss_nondivergence_proved':False,
            'lean_certified':False}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
