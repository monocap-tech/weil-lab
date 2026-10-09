#!/usr/bin/env python3
"""Direct block-Woodbury response from NF45's paid moment intervals."""
import argparse,json
from pathlib import Path
from fractions import Fraction as F
import certify_cc80_defect_response_acceptance as exact
import certify_cc81_boundary_response_consumer as c
import certify_cc87_seven_source_consumer as seven
import certify_cc85_six_source_consumer as six
import certify_cc83_five_source_consumer as five

K=F(207,1000)
def compact(x): return c.iv(c.pair(x))
def mm(a,b): return [[compact(x) for x in row] for row in c.mm(a,b)]
def sub(a,b):return [[compact(c.sub(x,y)) for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(a,z):return [[compact(c.mul(x,c.iv(z))) for x in row] for row in a]
def absmax(x):return max(abs(x[0]),abs(x[1]))
def square(x):return (F(0) if x[0]<=0<=x[1] else min(x[0]**2,x[1]**2),max(x[0]**2,x[1]**2))
def inverse(a):
    assert a==c.transpose(a)
    mid=[[sum(x)/2 for x in row] for row in a]
    assert all(x>0 for x in exact.pivots(mid))
    j=exact.inv(mid);ji=[[c.iv(x) for x in row] for row in j]
    product=mm(ji,a)
    residual=[[c.sub(c.iv(int(i==k)),v) for k,v in enumerate(row)] for i,row in enumerate(product)]
    rho=max(sum(absmax(x) for x in row) for row in residual);assert rho<1
    jnorm=max(sum(abs(x) for x in row) for row in j)
    error=rho*jnorm/(1-rho)
    return [[compact((x-error,x+error)) for x in row] for row in j],rho,error

def controls():
    results=[]
    for scale in [F(1),F(1,10**18)]:
        n=exact.mat([[2,1,F(1,3)],[1,3,F(1,5)],[F(1,3),F(1,5),4]])
        w=exact.mat([[1,2,scale],[F(1,3),-1,-2*scale],[1,0,3*scale]])
        a=[row[:2] for row in n[:2]];ai=exact.inv(a);b=[[row[2]] for row in n[:2]]
        delta=n[2][2]-exact.mul(exact.mul(exact.tr(b),ai),b)[0][0];assert delta>0
        wb=[row[:2] for row in w];last=[[row[2]] for row in w]
        z=[[last[i][0]-exact.mul(exact.mul(wb,ai),b)[i][0]] for i in range(3)]
        direct=exact.mul(z,exact.tr(z));direct=[[x/delta for x in row] for row in direct]
        full=exact.mul(exact.mul(w,exact.inv(n)),exact.tr(w))
        old=exact.mul(exact.mul(wb,ai),exact.tr(wb))
        assert direct==[[full[i][j]-old[i][j] for j in range(3)] for i in range(3)]
        assert c.det3([[c.iv(x) for x in row] for row in direct])==c.iv(0)
        results.append(dict(scale=str(scale),exact_block_inverse_difference_equals_outer_product=True))
    assert square(c.iv([-1,2]))== (F(0),F(4))
    assert square(c.iv([-2,-1]))== (F(1),F(4))
    return results

def run(root,oldroot):
    rows=[]
    for parity in ['even','odd']:
        d=seven.load(root,'RPB108_NF45_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json')
        q=c.matrix(d['seven_high_native_Gram']);g=c.matrix(d['seven_high_complete_source_Gram'])
        # N=C+T/k = (AH)*(AH)/k-H*AH: physical Gram cancels exactly.
        n=sub(scale(g,1/K),q)
        w=sub(c.matrix(d['joined_seven_high_source_crosses']),scale(c.matrix(d['joined_seven_high_native_crosses']),K))
        ni,rho,error=inverse([row[:6] for row in n[:6]])
        border=[[row[6]] for row in n[:6]]
        solved=mm(ni,border)
        delta=c.sub(n[6][6],mm(c.transpose(border),solved)[0][0]);assert delta[0]>0
        z=sub([[row[6]] for row in w],mm([row[:6] for row in w],solved))
        denominator=c.mul(c.iv(K*K),delta)
        credit=[[compact(c.div(square(z[i][0]) if i==j else c.mul(z[i][0],z[j][0]),denominator)) for j in range(3)] for i in range(3)]
        published=c.matrix(d['conditional_extra_joined_inverse_improvement'])
        assert all(c.overlap(credit[i][j],published[i][j]) for i in range(3) for j in range(3))
        h=list(map(F,d['frozen_NF44_witness']))
        zh=mm([[c.iv(x) for x in h]],z)[0][0]
        gain=c.div(square(zh),denominator)
        oldgain=c.iv(d['conditional_extra_frozen_witness_improvement'])
        assert c.overlap(gain,oldgain)
        baseline=six.load(oldroot,'RPB108_NF44_'+parity.upper()+'_INVERSE_WITNESS_CERTIFICATE_20261009.json')
        assert h==list(map(F,baseline['updated_frozen_rational_witness']))
        for suffix in ['native_Gram','complete_source_Gram']:
            assert [row[:6] for row in d['seven_high_'+suffix][:6]]==baseline['six_high_'+suffix]
        for suffix in ['native_crosses','source_crosses']:
            assert [row[:6] for row in d['joined_seven_high_'+suffix]]==baseline['joined_six_high_'+suffix]
        oldmatrix=c.matrix(baseline['conditional_six_high_joined_Schur_lower_matrix'])
        publishedmatrix=c.matrix(d['conditional_seven_high_joined_Schur_lower_matrix'])
        directmatrix=[[c.add(oldmatrix[i][j],credit[i][j]) for j in range(3)] for i in range(3)]
        assert all(c.overlap(directmatrix[i][j],publishedmatrix[i][j]) for i in range(3) for j in range(3))
        tightened=[[(max(directmatrix[i][j][0],publishedmatrix[i][j][0]),min(directmatrix[i][j][1],publishedmatrix[i][j][1])) for j in range(3)] for i in range(3)]
        e=[row[:2] for row in tightened[:2]];ei=five.inverse2(e);r=[[tightened[0][2]],[tightened[1][2]]]
        s=c.sub(tightened[2][2],mm(mm(c.transpose(r),ei),r)[0][0])
        assert (s[1]<0 if parity=='even' else s[0]>0)
        width_ratio=(oldgain[1]-oldgain[0])/(gain[1]-gain[0])
        rows.append(dict(parity=parity,verified_inverse_residual_row_norm_upper=c.pair(c.iv(rho))[1],
            verified_inverse_entry_error_upper=c.pair(c.iv(error))[1],
            positive_block_denominator=c.pair(denominator),direct_response_border=[c.pair(row[0]) for row in z],
            direct_response_matrix=[[c.pair(x) for x in row] for row in credit],
            direct_frozen_witness_response=c.pair(gain),published_frozen_witness_response=c.pair(oldgain),
            witness_response_interval_width_reduction_factor_lower=c.pair(c.iv(width_ratio))[0],
            tightened_seven_source_lower_matrix=[[c.pair(x) for x in row] for row in tightened],
            tightened_condensed_margin=c.pair(s),
            direct_witness_response_positive=gain[0]>0,
            background_floor_hypothesis=d['background_floor_hypothesis']))
    return dict(milestone='CC88',integration_parent='5c6f6540b5d1bbcea8cc30e577a105da9fe317a4',
        read_only_source='5f8a6c1e54a39236df253a5aae5f7be55fee74ed',parity_checks=rows,exact_controls=controls(),
        native_integrations_replayed=False,background_floor_newly_proved=False,whole_aperture_positive=False)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('NF45_root',type=Path);ap.add_argument('NF44_root',type=Path);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();d=run(a.NF45_root,a.NF44_root);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n')
    for r in d['parity_checks']:print(r['parity'],[float(F(v)) for v in r['direct_frozen_witness_response']],r['direct_witness_response_positive'])
