#!/usr/bin/env python3
"""Complete original negative strong-action and J470/W14 mixed budgets.

Exact SI10 geometry and rational composition of pinned native jet data.
No individual negative mixed entry or full matched response is computed.
"""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_si10_complement_positivity import KAPPA,protected_inner_cover
from validate_rpb108_si07_negative_support_cover import END,DEPTH,M,DEN,arch_lower_cell,ceil_fraction
from validate_rpb108_si06_negative_band import prime_interval
from validate_rpb108_mg07_global_negative_sup import exact_bound

NEG_SHA='a8f0ad60bf61914669d5cb19d36c070345745f2cd0fb54917231a3a1383331f3'
FRAME_SHA='87d6f3ae24cde489adaf9ab3ac7efa612bc82bd78c6c9e94866802fdc550052f'
SCHUR_SHA='f1149e27da8a0e1d90e48b8ee0eb8a0a0b8ef51d0910499a7fcd19a082efca07'
NATIVE_SHA='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'

def read(path,sha):
    raw=Path(path).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
    return json.loads(raw)

def original_leaf_geometry():
    leaves=[];accepted=0
    def visit(l,r,j,depth):
        nonlocal accepted
        mid=(l+r)/2;lower=arch_lower_cell(j)+prime_interval(mid)[0]-M*(r-l)/2
        if lower>KAPPA:
            accepted+=1;return
        if depth<DEPTH:
            visit(l,mid,j,depth+1);visit(mid,r,j,depth+1);return
        h=F(max(0,ceil_fraction(-lower*DEN)),DEN)
        assert h>=max(F(0),-lower)
        leaves.append((l,r,h))
    for j in range(END):visit(F(j),F(j+1),j,0)
    assert len(leaves)==973 and accepted==9261
    clusters=[]
    for l,r,h in leaves:
        m1=2*(r-l)*(h+KAPPA);m2=2*(r-l)*(h+KAPPA)**2
        if clusters and l==clusters[-1][1]:
            a,_,s,t=clusters[-1];clusters[-1]=(a,r,s+m1,t+m2)
        else:clusters.append((l,r,m1,m2))
    assert len(clusters)==107
    canonical,_,_,count,_=protected_inner_cover()
    assert count==973
    for (l,r,m1,_),(a,b,mass) in zip(clusters,canonical):
        assert (l,r)==(a,b) and m1==mass+2*KAPPA*(r-l)
    return leaves,clusters

def compression_regression():
    # Exact isometry into a larger observation space. Compression and
    # squaring are NOT interchangeable; the needed inequality is strict.
    V=[[F(3,5),F(-4,13)],[F(4,5),F(3,13)],[F(0),F(12,13)]]
    def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
    vt=list(map(list,zip(*V)))
    assert mm(vt,V)==[[F(1),F(0)],[F(0),F(1)]]
    r=[F(1),F(2),F(5)]
    K=mm(vt,[[r[i]*v for v in row] for i,row in enumerate(V)])
    L=mm(vt,[[r[i]**2*v for v in row] for i,row in enumerate(V)])
    K2=mm(K,K);gap=[[L[i][j]-K2[i][j] for j in range(2)] for i in range(2)]
    assert K[0][1]!=0 and gap[0][0]>0 and gap[1][1]>0
    assert gap[0][0]*gap[1][1]>=gap[0][1]**2 and gap[0][1]==gap[1][0]
    assert K2!=L and K[0][1]**2<=K2[1][1]<=L[1][1]
    # A component's inverse charge must not be added to another charge
    # without paying the cross term. Young at t=1 pays it exactly here.
    assert (F(1)+F(1))**2>F(1)**2+F(1)**2
    assert (F(1)+F(1))**2==2*F(1)**2+2*F(1)**2
    return dict(strict_compression_square_inequality_checked=True,
                nonzero_mixed_block_checked=True,unpaid_component_charge_addition_rejected=True)

def main():
    p=argparse.ArgumentParser();p.add_argument('--negative-certificate',required=True)
    p.add_argument('--frame-certificate',required=True);p.add_argument('--schur-certificate',required=True)
    p.add_argument('--output',default='artifacts/si29_original_negative_mixed_budget.json')
    args=p.parse_args();start=time.monotonic()
    neg=read(args.negative_certificate,NEG_SHA);frame=read(args.frame_certificate,FRAME_SHA)
    schur=read(args.schur_certificate,SCHUR_SHA)
    assert neg['status']=='ACTUAL_NORMALIZED_FULL_J_NEGATIVE_CLUSTER_LOEWNER_UPPER'
    assert neg['native_input_sha256']==frame['native_input_sha256']==NATIVE_SHA
    assert schur['native_input_sha256']==NATIVE_SHA
    assert schur['accepted_full_trial_input_sha256']==FRAME_SHA
    assert neg['original_J_count']==470 and neg['actual_feature_count']==14
    assert neg['cluster_count']==107 and neg['negative_leaf_count']==973
    assert neg['energy_projected_negative_operator_computed'] is False
    assert frame['physical_Gram_upper']=='101/100' and frame['full_trial_dimension']==484
    assert F(schur['normalized_actual_Astar_energy_Schur_inverse_upper'])==F(100001,99)
    assert KAPPA==F(1,1000)
    leaves,clusters=original_leaf_geometry();rows=[];beta=F(0);beta2=F(0)
    for i,((l,r,m1,m2),w) in enumerate(zip(clusters,neg['cluster_witnesses'])):
        assert (l,r)==(F(w['lo']),F(w['hi'])) and m1==F(w['shifted_two_sided_mass'])
        order=w['order'];radius=(r-l)/2
        first=radius**(2*order)*F(w['jet_norm_squared_upper'])
        rem=F(w['remainder_norm_squared_upper']);delta=F(w['young_parameter'])
        assert first>=0 and rem>=0 and delta>0
        packet=(1+delta)*first+(1+1/delta)*rem
        assert packet*m1==F(w['cluster_negative_operator_upper'])
        beta+=m1*packet;beta2+=m2*packet
        rows.append(dict(cluster=i,lo=str(l),hi=str(r),order=order,
             two_sided_mass=str(m1),two_sided_squared_height_mass=str(m2),
             whole_cluster_packet_squared_upper=str(packet),squared_action_payment=str(m2*packet)))
    assert beta==F(neg['exact_negative_operator_upper'])<F(1,500000)
    assert beta2<F(9,10**6)
    H=F(exact_bound()['original_negative_norm_upper'])
    assert H==F(871887,70000) and beta2<H*beta
    source_norm=F(101,100);mixed2=source_norm*beta2
    eta=F(3001,10**6);assert mixed2<eta**2
    inv=F(100001,99);charge=inv*mixed2;clean_charge=F(91,10000)
    assert charge<inv*eta**2<clean_charge
    result=dict(status='CONDITIONAL_COMPLETE_ORIGINAL_NEGATIVE_STRONG_ACTION_AND_MIXED_BUDGET',
      negative_input_sha256=NEG_SHA,frame_input_sha256=FRAME_SHA,schur_input_sha256=SCHUR_SHA,
      matched_native_physical_projection_sha256=NATIVE_SHA,original_J_count=470,actual_feature_count=14,
      original_cluster_count=107,original_negative_leaf_count=973,
      negative_multiplier='(kappa-m)_+, including kappa shift before squaring',
      original_leaf_witnesses=[[str(l),str(r),str(h)] for l,r,h in leaves],cluster_witnesses=rows,
      exact_W_K_W_upper=str(beta),exact_squared_multiplier_action_upper=str(beta2),
      clean_KW_squared_operator_upper='9/1000000',global_supremum_times_action_upper=str(H*beta),
      squared_action_improvement_over_global_supremum=str(H*beta/beta2),
      source_physical_Gram_upper=str(source_norm),exact_normalized_negative_mixed_squared_upper=str(mixed2),
      normalized_negative_mixed_operator_upper=str(eta),actual_energy_Schur_inverse_upper=str(inv),
      exact_negative_only_inverse_charge_upper=str(charge),negative_only_inverse_charge_upper=str(clean_charge),
      raw_coordinate_covariance='(Jstar Kminus W)(Wstar Kminus J) <= beta2 Jstar J',
      source_normalized_mixed='Mminus=(JD)star Kminus W, with accepted Dstar Jstar J D <= 101/100 I',
      supported_operator_square_identified_with_squared_multiplier=False,
      exact_regression=compression_regression(),individual_negative_mixed_entries_computed=False,
      archimedean_mixed_computed=False,complete_Astar_mixed_computed=False,
      energy_projection_computed=False,matched_forcing_computed=False,inverse_response_value_certified=False,
      prime_raw_error_transported_to_normalized_source_coordinates=False,
      full_component_inverse_charges_added_without_cross_payment=False,
      W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print('FULL ORIGINAL NEGATIVE MIXED BUDGET PASS: ||(JD)star Kminus W|| < 3001/10^6; negative-only inverse charge < 91/10000')
    print('Squared negative action',float(beta2),'global-sup improvement',float(H*beta/beta2),'seconds',round(time.monotonic()-start,2))
if __name__=='__main__':main()
