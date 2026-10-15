"""RC277: exact weighted Schur bound for actual prime shifts and index budgets."""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json
import validate_rpb108_rc276_projection_cross_columns as parent
ROOT=parent.ROOT; B=F(11,10); up=parent.up; down=parent.down
PINS=dict(parent.PINS); HELPER_PINS=dict(parent.HELPER_PINS)
PINS.update({'certificates/rpb108_rc276_projection_cross_columns.json':'66ca887480b4ad22df9021fff994ec9ad71f5486','notes/RPB108_RC276_PROJECTION_CROSS_COLUMNS_20261014.md':'6b4b95b373bc50a29fef9274e52cbf1bcae61c83'})
HELPER_PINS['scripts/validate_rpb108_rc276_projection_cross_columns.py']='5c8a12f5163232769f056a265edef3385d846413'

def minimum(q,l,r):
    """Exact quadratic minimum, including an interior convex vertex."""
    points={l,r}
    if q[2]>0 and l < -q[1]/(2*q[2]) < r:
        points.add(-q[1]/(2*q[2]))
    return min((q[0]+q[1]*x+q[2]*x*x,x) for x in points)

def prime_bound(primes,a,k,reverse=False):
    assert a>0 and k>0
    knots={F(0),B}
    for row in primes:
        el,eh=F(row['translation_lower']),F(row['translation_upper'])
        assert 0<el<=eh<2*B
        for t in [B-el,B-eh,el-B,eh-B]:
            if 0<=t<=B:knots.add(t)
    knots=sorted(knots)
    regions=[(l,r,False) for l,r in zip(knots,knots[1:])]
    # Open interiors exclude endpoint-only activations; every knot is checked
    # separately with non-strict activation, including uncertainty boundaries.
    regions += [(x,x,True) for x in knots]
    answer=[]
    for l,r,point in regions:
        numerator=[F(0),F(0),F(0)]; active=[]
        for row in sorted(primes,key=lambda v:v['n'],reverse=reverse):
            el,eh=F(row['translation_lower']),F(row['translation_upper'])
            cl,ch=F(row['coefficient_lower']),F(row['coefficient_upper'])
            assert 0<cl<=ch
            for sign in [1,-1]:
                possible=(l+el<=B if point else l+el<B) if sign==1 else (r>=el-B if point else r>el-B)
                if not possible:continue
                active.append([row['n'],sign])
                # x>=0: coefficientwise upper enclosure is a pointwise upper
                # enclosure. Actual translations are never replaced by models.
                numerator[0]+=ch*(1+a*eh*eh/(B*B))
                numerator[1]+=2*a/(B*B)*(ch*eh if sign==1 else -cl*el)
                numerator[2]+=ch*a/(B*B)
        q=[k-numerator[0],-numerator[1],k*a/(B*B)-numerator[2]]
        margin,where=minimum(q,l,r)
        if margin<=0:return None
        answer.append(dict(left=str(l),right=str(r),point=point,possibly_active_actual_shifts=sorted(active),row_upper_polynomial=list(map(str,numerator)),Schur_difference_lower_polynomial=list(map(str,q)),exact_minimum=str(margin),minimum_location=str(where)))
    return dict(weight='phi(x)=1+a*(x/B)^2',a=str(a),operator_norm_upper=str(k),positive_weight_lower='1',positive_weight_upper=str(1+a),actual_prime_powers=[r['n'] for r in primes],rational_knots=list(map(str,knots)),regions=answer,all_region_margins_strictly_positive=True,minimum_region_margin=str(min(F(r['exact_minimum']) for r in answer)),reflection_covers_negative_half=True,actual_shift_intervals_retained=True,endpoint_only_activations_checked_separately=True)

def controls():
    assert minimum([F(1),F(-2),F(1)],F(0),F(2))==(F(0),F(1))
    assert minimum([F(1),F(0),F(-1)],F(0),F(2))==(F(-3),F(2))
    # Weighted edge inequality, the algebra underlying selfadjoint Schur.
    for phi,psi,u,v in [(F(3),F(4),F(-2),F(5)),(F(1),F(2),F(3),F(7))]:
        assert psi/phi*u*u+phi/psi*v*v-2*u*v==(psi*u-phi*v)**2/(phi*psi)>=0
    toy=[dict(n=2,translation_lower='1/2',translation_upper='1/2',coefficient_lower='1',coefficient_upper='1')]
    assert prime_bound(toy,F(3,10),F(1)) is None
    assert prime_bound(toy,F(3,10),F(4)) is not None
    return dict(interior_quadratic_vertex_checked=True,weighted_edge_square_identity_checked=True,undersized_Schur_bound_rejected=True)

def run(reverse=False):
    data={}
    for path,sha in sorted(dict(PINS,**HELPER_PINS).items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==sha,(path,'pin')
        if path.endswith('.json'):data[path]=json.loads(raw)
    get=lambda s:data['certificates/rpb108_rc'+s+'.json']
    prime=prime_bound(get('43_native_prime_head')['active_prime_powers'],F(3,10),F(3013,1000),reverse)
    assert prime is not None
    metric=get('129_four_vector_joint_moment')
    sl=F(metric['actual_D_Gram_entry_lower'][0][0])/(2*B)
    regular=F(get('274_mixed_diagonal_inverse')['regular_kernel_Schur_norm_certificate']['complete_actual_regular_operator_norm_upper'])
    oddpole=2*F(get('42_native_signed_pole_head')['sinh_physical_norm_squared_upper'])
    H=[F(0)]
    for n in range(1,2001):H.append(H[-1]+F(1,n))
    rows=[]
    for threshold in [F(0),F(1,100)]:
        parity_rows=[]
        for base,parity in enumerate(['even','odd']):
            C=up(F(789,125)+regular+F(prime['operator_norm_upper'])+base*oddpole)
            scale=1-2*threshold
            first=next(n for n in range(base,2001,2) if scale*(H[n]+sl)>C)
            rank=(first-base)//2
            previous=first-2
            assert first>base and scale*(H[previous]+sl)<=C
            gap=down(scale*(H[first]+sl)-C)
            floor=down((scale-C/(H[first]+sl))/2)
            assert gap>0 and floor>0
            parity_rows.append(dict(parity=parity,physical_negative_allowance_C=str(C),harmonic_shift_lower=str(sl),D_scale=str(scale),first_omitted_Legendre_degree=first,retained_Legendre_degrees=list(range(base,first,2)),moment_codimension=rank,first_omitted_H_plus_s_lower=str(down(H[first]+sl)),previous_degree=previous,previous_diagonal_lower_not_positive=True,physical_complement_gap_lower=str(gap),canonical_complement_gap_lower=str(floor),complement_is_physical_Legendre_moment_annihilator=True))
        total=sum(r['moment_codimension'] for r in parity_rows)
        rows.append(dict(canonical_threshold=str(threshold),parity_certificates=parity_rows,total_index_upper=total,includes_threshold_equality=True))
        print('RC277 threshold '+str(threshold)+': index <= '+str(total)+'; parity ranks '+str([r['moment_codimension'] for r in parity_rows]),flush=True)
    assert rows[0]['total_index_upper']<582 and rows[1]['total_index_upper']<608
    return dict(milestone='RC277',starting_commit='3aae55dbc98a3ab3aaf8ba6c249a0449aae3fb67',input_git_blob_pins=PINS,validator_git_blob_pins=HELPER_PINS,actual_prime_weighted_Schur_certificate=prime,regular_operator_norm_upper=str(regular),odd_negative_pole_norm_upper=str(oddpole),original_diagonal_index_certificates=rows,exact_controls=controls(),original_form_identity='G0=D+h-(789/125)I-Kreg+Kprime+Kpole; h>=0',global_prime_form_bound='Kprime>=-(3013/1000) I_physical',canonical_metric_upper='L<=2D',threshold_lower_form='G0-t L >= (1-2t)D-C I_physical',canonical_complement_gap_formula='((1-2t)-C/(H_first+s_lower))/2',index_contract='On the physical Legendre moment annihilator the threshold form has a strict positive canonical gap; min-max bounds the full canonical threshold index by its moment codimension',original_nonpositive_count_upper=rows[0]['total_index_upper'],original_at_or_below_one_hundredth_count_upper=rows[1]['total_index_upper'],original_below_one_hundredth_count_lower_preserved=10,legacy_rank_639_reference_and_signed_pivots_preserved=True,rank_608_projection_reference_and_positive_pair_preserved=True,full_remaining_606_projection_Schur_gate_evaluated=False,finite_eight_canonical_inverse_width_preserved='485647/1000000',Stage_I_closed=False,RH=False,F4=False,Lean=False,next_cursor='RC278: use the new global actual-prime bound to rebuild a smaller positive projection reference or strengthen the retained principal response bound; full original positivity remains open')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--replay',action='store_true');args=ap.parse_args();result=run(args.replay)
    if args.replay:assert result==json.loads(args.output.read_text())
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print('RC277 VALIDATED: actual weighted prime bound and improved original index budgets',flush=True)
