#!/usr/bin/env python3
"""Exact collective first-high-mode response from NF17/NF18 signed archives.
No complete F112 inverse response or whole-aperture sign is asserted.
"""
import argparse, gzip, hashlib, json
from math import lcm
from fractions import Fraction as F

OLD_SHA='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
NEW_SHA='da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee'
GRID=10**100

def read(path,sha):
    with gzip.open(path,'rb') as h:raw=h.read()
    assert hashlib.sha256(raw).hexdigest()==sha
    return json.loads(raw)

def bareiss_sign(a):
    """Leading-principal determinant signs, exact integer divisions."""
    a=[row[:] for row in a];previous=1;positive=0
    for k in range(len(a)):
        pivot=a[k][k]
        if pivot<=0:return positive, -1 if pivot<0 else 0
        positive+=1
        for i in range(k+1,len(a)):
            for j in range(i,len(a)):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                value,remainder=divmod(numerator,previous)
                assert remainder==0
                a[i][j]=a[j][i]=value
        previous=pivot
    return positive,1

def ceil_fraction(x):return -((-x.numerator)//x.denominator)

def rational_sign(a):
    den=lcm(*(v.denominator for row in a for v in row))
    return bareiss_sign([[int(v*den) for v in row] for row in a])

def certify(old_path,new_path):
    old=read(old_path,OLD_SHA);new=read(new_path,NEW_SHA)
    assert old['aperture']==new['aperture']=='53/50'
    assert old['dim']==112 and new['parent_sha256']==OLD_SHA
    assert new['new_columns']==[112,113]
    records={**old['complete_form'],**new['original_full_source']}
    assert len(old['complete_form'])==3192
    assert len(new['original_full_source'])==114 and len(records)==3306
    centers={};error=F(0);component_checks=0
    for key,p in records.items():
        pole='poles' if 'poles' in p else 'pole'
        assert set(p)=={'arch','prime',pole,'full'}
        for kind in p:
            lo,hi=map(F,p[kind]);assert lo<=hi;component_checks+=1
        lo,hi=map(F,p['full'])
        assert lo<=sum(F(p[k][1]) for k in ('arch','prime',pole))
        assert hi>=sum(F(p[k][0]) for k in ('arch','prime',pole))
        center=(((lo+hi)/2)*GRID).__floor__()
        centers[key]=center
        error=max(error,abs(F(center,GRID)-lo),abs(F(center,GRID)-hi))
    eps_units=ceil_fraction(57*error*GRID)
    eps=F(eps_units,GRID)
    assert eps>=57*error and eps<F(1,10**39)
    result=[]
    for parity,j,lower,upper in [(0,112,F(203,1000),F(204,1000)),
                                 (1,113,F(205,1000),F(206,1000))]:
        ix=list(range(parity,112,2))
        A=[[centers[f'{min(i,k)},{max(i,k)}'] for k in ix] for i in ix]
        b=[centers[f'{i},{j}'] for i in ix];d=centers[f'{j},{j}']
        assert F(d,GRID)-error>3
        shifted=[row[:] for row in A]
        for i in range(56):shifted[i][i]-=10**62
        old_sign=bareiss_sign(shifted)
        assert old_sign==(56,1)
        gates=[]
        for r,direction in [(lower,1),(upper,-1)]:
            # r<=1: full block entry error <=error, hence operator error <=57*error.
            den=r.denominator;num=r.numerator
            M=[[num*A[i][k] for k in range(56)]+[den*b[i]] for i in range(56)]
            M.append([den*x for x in b]+[den*d])
            for i in range(57):M[i][i]+=direction*den*eps_units
            signs=bareiss_sign(M)
            assert signs==((56,-1) if direction==1 else (57,1))
            gates.append(dict(r=str(r),error_direction=direction,
                              positive_leading_minors=signs[0],final_sign=signs[1]))
        # Exact arithmetic controls with the same response brackets. These are
        # abstract completions, not substitute native Weil source identities.
        r=(lower+upper)/2;remaining=1-r
        hidden=[]
        for factor in [F(1,2),F(1),F(2)]:
            high=remaining/factor
            assert high>F(207,1000)
            signed=1-r-remaining*remaining/high
            assert (signed>0 if factor<1 else signed==0 if factor==1 else signed<0)
            model=[[F(1),F(1),remaining],[F(1),1/r,F(0)],
                   [remaining,F(0),high]]
            assert rational_sign(model)==((3,1) if factor<1 else (2,0) if factor==1 else (2,-1))
            hidden.append(dict(hidden_cost_factor=str(factor),high_floor=str(high),
                               corrected_sign='positive' if signed>0 else 'null' if signed==0 else 'negative'))
        # A genuine positive eigenlevel becomes null when the ENTIRE physical
        # mass matrix is shifted. A raw low entry alone is not the shift.
        level=F(1,10**40);a=F(1);cc=F(1);coupling=1-level
        assert (a-level)*(cc-level)-coupling**2==0
        assert a*cc-coupling**2>0 and cc-level>F(207,1000)
        assert rational_sign([[a,coupling],[coupling,cc]])==(2,1)
        assert rational_sign([[a-level,coupling],[coupling,cc-level]])==(1,0)
        result.append(dict(parity='even' if parity==0 else 'odd',high_degree=j,
            collective_response_strict_bracket=[str(lower),str(upper)],
            original_A_positive_minors=old_sign[0],paid_block_gates=gates,
            all_direction_remaining_fraction_lower=str(1-upper),
            hidden_completion_controls=hidden,whole_mass_positive_level_control=True))
    return dict(status='PASS',milestone='CC53',aperture='53/50',
        original_E112_sha256=OLD_SHA,boundary_source_sha256=NEW_SHA,
        original_signed_entries=3306,component_interval_checks=component_checks,
        rounded_matrix_grid=str(GRID),maximum_entry_error=str(error),
        paid_57_by_57_operator_error=str(eps),parities=result,
        exact_bareiss_certifications=6,abstract_hidden_completion_controls=6,
        positive_level_controls=2,
        actual_collective_first_mode_response_certified=True,
        first_mode_corrected_even56_odd56_positive=True,
        complete_F112_inverse_response_certified=False,
        CC52_constrained_carrier_transfer_certified=False,
        whole_original_aperture_positive=False,RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('old');p.add_argument('boundary')
    p.add_argument('--output');args=p.parse_args()
    out=json.dumps(certify(args.old,args.boundary),indent=2)+'\n'
    if args.output:
        with open(args.output,'w') as h:h.write(out)
    print(out)
