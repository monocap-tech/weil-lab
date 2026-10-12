"""RC151: structural conditional response on the two uncovered directions."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import down,up,psd,ser
from validate_rpb108_rc129_four_vector_joint_moment import add,mm,transpose,cong,inv
from validate_rpb108_rc150_source_coverage import run as rc150_run

def run(paths,replay=False):
    raw=[Path(p).read_bytes() for p in paths]
    prior=json.loads(raw[0]);assert prior==rc150_run(paths[1:],replay)
    joint=json.loads(raw[14]);assert joint['milestone']=='RC136'
    W=[[F(x) for x in row] for row in prior['augmented_source_frame']]
    GL=[[F(x) for x in row] for row in joint['actual_D_Gram_Loewner_lower']]
    GU=[[F(x) for x in row] for row in joint['actual_D_Gram_Loewner_upper']]
    L,U=cong(W,GL),cong(W,GU)
    assert psd(L) and psd(add(U,L,-1))
    def schur(M):
        A=[row[:5] for row in M[:5]]
        B=[row[5:] for row in M[:5]]
        C=[row[5:] for row in M[5:]]
        return add(C,mm(transpose(B),mm(inv(A),B)),-1)
    SL,SU=schur(L),schur(U)
    assert SL==[[F(x) for x in row] for row in prior['actual_D_Gram_complement_Schur']]
    assert psd(SL) and psd(add(SU,SL,-1))
    # Schur complementation is monotone for positive block forms. For the true
    # response Sigma, 1/2 G <= Sigma <= G gives the conditional bound below.
    lower=[[x/2 for x in row] for row in SL]
    upper=SU
    gap=add(upper,lower,-1)
    assert psd(lower) and psd(gap)
    def yes(n):return psd(add([[F(n,10**6)*x for x in row] for row in SL],gap,-1))
    hi=1
    while not yes(hi):hi*=2;assert hi<10**12
    lo=0
    while hi-lo>1:
        mid=(lo+hi)//2
        if yes(mid):hi=mid
        else:lo=mid
    beta=F(hi,10**6);assert yes(hi) and not yes(lo)
    witness=[down(-SL[0][1]/SL[0][0],10**12),F(1)]
    def quad(M):return sum(witness[i]*M[i][j]*witness[j] for i in range(2) for j in range(2))
    qlo,qhi,qgap=quad(SL),quad(SU),quad(gap)
    assert 0<qlo<=qhi and qgap>qhi/2
    # Exact finite model: equal paid and complement diagonal responses can
    # coexist with opposite mixed signs under 1/2 I <= Sigma <= I.
    toy=[[[F(3,4),sign*F(1,4)],[sign*F(1,4),F(3,4)]] for sign in (1,-1)]
    ident=[[F(i==j) for j in range(2)] for i in range(2)]
    assert all(psd(add(M,[[x/2 for x in row] for row in ident],-1)) and psd(add(ident,M,-1)) for M in toy)
    assert toy[0][0][0]==toy[1][0][0] and toy[0][1][1]==toy[1][1][1]
    return dict(milestone='RC151',status='PASS: positive conditional two-source response with quantified structural precision gap',
        starting_commit='b13ec66e6da25fa81854c421d89f9cf49a07eb19',
        input_sha256=[hashlib.sha256(b).hexdigest() for b in raw],aperture='11/10',
        complement_sources=['psi0','z_b6-v10'],paid_source_count=5,carrier_dimension=7,
        conditional_source_Gram_lower=ser(SL),conditional_source_Gram_upper=ser(SU),
        conditional_reference_response_lower=ser(lower),conditional_reference_response_upper=ser(upper),
        conditional_response_relative_width_upper=str(beta),
        conditional_witness_mixture=list(map(str,witness)),
        witness_conditional_source_energy_lower=str(down(qlo,10**24)),
        witness_conditional_source_energy_upper=str(up(qhi,10**24)),
        witness_structural_response_width_lower=str(down(qgap,10**24)),
        witness_width_over_source_upper_lower=str(down(qgap/qhi,10**6)),
        structural_half_Gram_width_gate_fails=True,
        opposite_mixed_row_controls=ser(toy),
        mixed_response_rows_not_determined_by_paid_block_and_complement_diagonals=True,
        actual_complement_response_columns_evaluated=False,
        original_Weil_or_augmented_actions_performed=False,whole_aperture_positivity_extended=False,
        RH=False,F4=False,Lean=False,
        next_cursor='evaluate psi0 and difference actions and their mixed response rows; structural complement bound alone is too wide')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=19)
    a=p.parse_args();result=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==result
    else:Path(a.output).write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC151 PASS: two-direction conditional response audit')
