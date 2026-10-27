#!/usr/bin/env python3
"""Independent exact derivative-cost, pruning and complete BS count replay."""
import hashlib,json,sys
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
PINS=['c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60','19af532b6bbd4a808854696b2a993e7ebd966e04da27fdd5f55e8b736668770b','931e5c64db19b28201ce96958495a8bfd8337eb7ebe08096466d86db29a1f801']
def main():
    assert len(sys.argv)==5
    z=json.load(open(sys.argv[1]));raw=[Path(p).read_bytes() for p in sys.argv[2:]]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==PINS and z['input_sha256']==dict(zip(['native','envelope','prior'],PINS))
    native,env,prior=map(json.loads,raw)
    assert z['status']=='CONDITIONAL_ORIGINAL_BS_PRUNED_RANK_UPPER'
    assert native['full_original_source_count']==env['original_source_count']==z['original_source_rank_upper']==470
    assert env['input_sha256']['native']==PINS[0] and prior['input_sha256']['envelope']==PINS[1]
    assert z['original_nodes']==native['original_source_nodes'];nodes=[(Q(c),p) for c,p in z['original_nodes']]
    assert len(nodes)==107 and sum(p for c,p in nodes)==469
    cells=[tuple(map(Q,row)) for row in env['original_SM40_cells']];assert len(cells)==3892
    B=Q(11,10);K=Q(33621,10**9);target=Q(1,2)
    assert z['physical_half_width']=='11/10' and Q(z['inherited_global_Astar_floor'])==K==Q(prior['inherited_global_Astar_floor'])
    assert Q(z['declared_BS_tail_target'])==target
    tables=[];proof_orders=[];mass=Q(0);cursor=0
    for i,((c,pmax),row) in enumerate(zip(nodes,z['cluster_witnesses'])):
        assert row['cluster']==i and Q(row['center'])==c and row['original_multiplicity']==pmax
        lo,hi=Q(row['lo']),Q(row['hi']);assert c==(lo+hi)/2
        group=[];last=lo
        while cursor<len(cells) and cells[cursor][0]<hi:
            a,b,w=cells[cursor];assert a==last and lo<=a<b<=hi and w>0
            group.append((a,b,w));last=b;cursor+=1
        assert last==hi and len(group)==row['SM40_cell_count']
        weights=[2*(b-a)*w for a,b,w in group];mass+=sum(weights,Q(0));rawcost=[]
        for p in range(pmax+1):
            # Independent form: Cauchy derivative norm times Taylor remainder.
            norm_squared=2*B/(2*p+1)
            bound=sum((m*norm_squared*((Q(44,7)*B*max(abs(a-c),abs(b-c)))**p/factorial(p))**2 for m,(a,b,w) in zip(weights,group)),Q(0))
            rawcost.append(bound)
        chosen=[min(range(p+1),key=lambda k:rawcost[k]) for p in range(pmax+1)]
        table=[rawcost[k] for k in chosen];tables.append(table);proof_orders.append(chosen)
        assert table==list(map(Q,z['local_cost_tables'][i])) and chosen==z['proof_orders_by_available_multiplicity'][i]
        assert all(table[p+1]<=table[p] for p in range(pmax))
    assert cursor==3892 and len(z['cluster_witnesses'])==107 and mass==Q(z['original_SM40_two_sided_mass'])==Q(1073441879,64000000)
    counts=[p for c,p in nodes];epsilon=sum((v[p] for v,p in zip(tables,counts)),Q(0));budget=K*target
    assert epsilon<budget
    for step in z['greedy_removal_trace']:
        options=[(tables[i][p-1]-tables[i][p],i) for i,p in enumerate(counts) if p>0]
        delta,i=min(options);assert i==step['cluster'] and delta==Q(step['increment'])>=0
        assert counts[i]==step['old_multiplicity'] and step['new_multiplicity']==counts[i]-1
        counts[i]-=1;epsilon+=delta
        assert epsilon==Q(step['epsilon_after'])<budget
    options=[tables[i][p-1]-tables[i][p] for i,p in enumerate(counts) if p>0]
    assert options and epsilon+min(options)>=budget  # Greedy endpoint, not a global optimum proof.
    assert counts==z['selected_multiplicities'] and sum(counts)==z['retained_sine_cosine_constraints']==241
    assert z['retained_original_pole'] is True and 1+sum(counts)==z['retained_physical_rank_upper']==242
    assert len(z['greedy_removal_trace'])==z['removed_original_constraints']==228
    zero=0;total=Q(0)
    for i,(n,row) in enumerate(zip(counts,z['cluster_witnesses'])):
        assert row['retained_multiplicity']==n and row['proof_derivative_order']==proof_orders[i][n]
        pay=tables[i][n];assert pay==Q(row['negative_payment'])>0;total+=pay
        if n==0:
            zero+=1;assert row['proof_derivative_order']==0  # Cauchy bound; band NOT discarded.
    assert zero==z['zero_constraint_cluster_count']==40 and total==epsilon==Q(z['pruned_physical_complement_negative_upper'])
    t=epsilon/K;assert t==Q(z['BS_complement_operator_upper'])==Q(z['eigenvalue_upper'])<target
    assert z['eigenvalue_index']==243 and z['critical_count_upper']==242 and z['critical_count_lower']==4
    assert Q(z['fourth_eigenvalue_lower'])==Q(prior['fourth_eigenvalue_lower'])>Q(z['critical_level'])==Q(prior['critical_level'])>target
    assert z['previous_rank_upper']==470 and Q(z['previous_BS_tail_upper'])==Q(prior['BS_complement_operator_upper'])<t
    assert Q(z['complement_inverse_upper'])==1/(1-t) and Q(z['generic_sufficient_finite_threshold'])==1-t
    assert z['complete_107_clusters_paid'] is True and z['complete_3892_cells_paid'] is True
    for k in ['full_J470_compressed_inverse_transferred','actual_reduced_projection_computed','actual_inverse_computed','finite_or_mixed_gate_certified','globally_minimal_rank_claimed','uniform_improvement_over_previous_tail_claimed','global_true_BS_norm_upper_one_certified']:assert z[k] is False
    assert z['W_ODD_NEG']==z['inherited_original_domain_review']=='OPEN'
    # A smaller projection does not inherit an inverse bound on a smaller complement.
    # H=diag(100,1,1), Pfull spans e0,e1: Qfull H Qfull<=I.
    # Psmall spans e1: its enlarged complement includes the 100 direction.
    assert Q(100)>Q(1)
    print('INDEPENDENT ORIGINAL RANK/TARGET REPLAY PASS: all 3892 cells /107 clusters, 228 exact greedy removals; lambda243<1/2 and critical count 4..242; no compressed-inverse transfer; finite/mixed gate OPEN')
if __name__=='__main__':main()
