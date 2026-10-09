#!/usr/bin/env python3
"""Paid low border for NF38's selected frame at the original .44 high floor."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import argparse,json,hashlib,gzip,base64
import certify_dne28_signed_budget as old
assert hashlib.sha256(Path(old.__file__).read_bytes()).hexdigest()=='067d8a4b04ed0f9830f5c5e1070ffb7221f0cceb518ef27933d80fb1bcffc2c9'
SHA=['ebca74e6237cf401b7480afe08b91caba2c3412dc08e55ac2ac55f1970d8f788','6f1adeb39792345e857806ce4128c72b9b08dabd4d21f6f3bde8a8463bd94671','b6f7134f131dc2698868d676494d171e40340e81c453fb67d0e80520e082ce37','d0dee22dd8803b9f9b2545650a3f0ada382e55d10a36c834bf3350288161aa8c','4317560e2e465841beec0dc44d314dad2c9e847a096a565059f0c593fef026b0','533686e6040631b9faa182d686873d8952368cdb493c46758d665c66484dd90b','435a347824b6ba783956d212b0c48adc2914c3df1443f6cd1129d0dcc905b718','c4828a354f5d6af5b54e0bc25179ce1d522d68df3cebe75ff9ebef123cc87936']
PAIR_SHA=['7a755384fde16b7e7f92f1b66b5754b927c9ef6f9dccb5eac38df83f412b94b8','0eaae8a3e5773b4e5449c9f080b427c24067e6a18e068cea384aacf7675312cf']
REPLAY_SHA=['e1c90ec0125e0cf2211d4bab360cd95b8acc6c111417314fe20dbdbb7d55ac04','1dfb8e06bc9e575839ca0475b4b3edfc6f072806d85c86f4f6b36b2b0ca45e92']
def read(p):
    b=Path(p).read_bytes()
    if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    return json.loads(b),hashlib.sha256(b).hexdigest()
def root(x,d):
    s=10**d;n=isqrt(x.numerator*s*s//x.denominator);v=F(n+1,s);assert v*v>x;return v
def run(paths,digits,root_digits,replay):
    old.Interval.digits=digits;data=[read(p) for p in paths];expected=SHA+(REPLAY_SHA if replay else PAIR_SHA);assert [h for _,h in data]==expected;checks=1
    low,scales,se,so,d26,d28,ce,co,pe,po=[v for v,_ in data];k=F(11,25);rows=[]
    assert d26['input_sha256'][:2]==SHA[2:4] and not d26['low_mode_union_with_this_new_frame_certified'];checks+=1
    for idx,(l,s,sc,col,pair,prior) in enumerate(zip(low['native_parity_gates'],(se,so),scales['rows'],(ce,co),(pe,po),d28['rows'])):
        assert l['parity']==s['parity']==sc['parity']==col['parity']==pair['parity']==prior['parity'];checks+=1
        assert col['input_sha256'][1]==s['fixed_trial_sha256'] and col['input_sha256'][2]==SHA[2+idx] and pair['fixed_columns_sha256']==SHA[6+idx];checks+=1
        assert pair['CC62_low_diagonal_overlap'] and pair['all_six_primes_both_orientations_paid'] and pair['exact_endpoint_log_paid'];checks+=1
        row=dict(congruence_scales=sc['congruence_scales'],original_low_lift_pairings=pair['original_low_selected_pairings'])
        packet=dict(original_native_energy_Gram=s['original_selected_native_energy_Gram'],original_complete_source_Gram=s['original_selected_complete_source_Gram'])
        Q,G,scale=old.matrices(row,l,packet)
        t=F(66,125) if idx==0 else F(211,500);c=F(11,100) if idx==0 else F(7,50);q=F(1,25) if idx==0 else F(7,50)
        ell=[F(1,1000),F(1,4),F(1,10),F(1,2)] if idx==0 else [F(1,100),F(3,25),F(1,5),F(1,50)]
        D=[[v*((1+1/t) if i==j==0 else 1+t) for j,v in enumerate(row)] for i,row in enumerate(G)]
        H=[[Q[i][j]*(k-c)-D[i][j] for j in range(4)] for i in range(4)]
        hpaid=old.ldl(H);checks+=4
        npaid=old.ldl([[Q[i][j]-old.Interval(q if i==j else 0) for j in range(4)] for i in range(4)]);checks+=4
        upaid=old.ldl([[Q[i][j]-D[i][j]/k-old.Interval(ell[i] if i==j else 0) for j in range(4)] for i in range(4)]);checks+=4
        masses=[F(prior['high_completed_column_mass_upper'][0])];native_masses=[]
        for j,cc in enumerate(col['columns']):
            exactmass=sum(F(v)**2 for v in cc['coefficients']);assert exactmass==F(cc['exact_mass_squared']);checks+=1
            norm=root(exactmass,root_digits);native_masses.append(norm);masses.append(norm+root(F(s['original_selected_complete_source_Gram'][j][j][1]),root_digits)/k)
        gap=1/(sum((ss*m)**2/e for ss,m,e in zip(scale,masses,ell))+1/k)
        assert gap>F(prior['physical_gap_strict_lower']) and c>F(prior['complete_four_column_source_credit']);checks+=1
        rows.append(dict(parity=s['parity'],young_source_parameter=str(t),complete_four_column_source_credit=str(c),
            credit_on_old_DNE23_frame=prior['complete_four_column_source_credit'],native_scaled_identity_lower=str(q),
            scaled_coarse_diagonal_lower=list(map(str,ell)),column_scales=list(map(str,scale)),
            fresh_original_low_selected_pairings=pair['original_low_selected_pairings'],
            scaled_native_matrix=[[v.box() for v in row] for row in Q],scaled_block_source_input=[[v.box() for v in row] for row in G],
            scaled_coherent_source_majorant=[[v.box() for v in row] for row in D],signed_comparison_matrix=[[v.box() for v in row] for row in H],
            signed_comparison_LDL=hpaid,native_identity_comparison_LDL=npaid,physical_diagonal_comparison_LDL=upaid,
            exact_selected_column_norm_upper=list(map(str,native_masses)),high_completed_column_mass_upper=list(map(str,masses)),
            physical_gap_strict_lower=str(gap),display_credit=float(c),display_gap=float(gap),
            remaining_condition='c*B_Y-Gamma_Y>0 on THIS optimized native-energy-orthogonal remainder',remaining_source_Gram_certified=False))
    guard=F(24,10**36);assert min(F(r['physical_gap_strict_lower']) for r in rows)>guard;checks+=1
    return dict(stage='DNE29',aperture='53/50',high_floor=str(k),interval_digits=digits,root_digits=root_digits,replay_source_inputs=replay,
        input_sha256=expected,rows=rows,exact_counted_assertions=checks,physical_gap_guard=str(guard),
        NF38_optimized_low_mode_union_certified=True,same_retained_Z8=True,high_lifts_changed_from_DNE23=True,
        new_original_native_low_pairings=6,complete_low_source_crosses_paid_coherently=True,
        positive_retained_dimension=8,uncovered_retained_dimension=104,complete_remaining_Gram_certified=False,
        whole_aperture_positive=False,actual_infinite_inverse_evaluated=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    keys=['low','scales','even','odd','dne26','dne28','columns_even','columns_odd','pair_even','pair_odd']
    for key in keys:p.add_argument(key)
    p.add_argument('--digits',type=int,default=80);p.add_argument('--root-digits',type=int,default=160);p.add_argument('--replay-inputs',action='store_true');p.add_argument('--output',required=True)
    a=p.parse_args();r=run([getattr(a,k) for k in keys],a.digits,a.root_digits,a.replay_inputs);Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({'checks':r['exact_counted_assertions'],'rows':[{k:v[k] for k in ['parity','display_credit','display_gap']} for v in r['rows']]}))
