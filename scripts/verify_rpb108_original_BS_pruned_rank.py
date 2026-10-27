#!/usr/bin/env python3
"""Exact original constraint pruning for ONE declared BS tail target, 1/2."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
from math import factorial
PINS={'native':'c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60','envelope':'19af532b6bbd4a808854696b2a993e7ebd966e04da27fdd5f55e8b736668770b','prior':'931e5c64db19b28201ce96958495a8bfd8337eb7ebe08096466d86db29a1f801'}
B=F(11,10);OMEGA=F(44,7)*B;KSTAR=F(33621,10**9);TARGET=F(1,2)
def main():
    p=argparse.ArgumentParser()
    for k in PINS:p.add_argument('--'+k,required=True)
    p.add_argument('--output',default='artifacts/original_BS_pruned_rank_bound.json');args=p.parse_args();start=time.monotonic();data={}
    for k,sha in PINS.items():
        raw=Path(getattr(args,k)).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha;data[k]=json.loads(raw)
    native,env,prior=(data[k] for k in PINS)
    assert native['full_original_source_count']==env['original_source_count']==prior['original_physical_source_count']==470
    assert env['input_sha256']['native']==PINS['native'] and prior['input_sha256']['envelope']==PINS['envelope']
    assert F(prior['inherited_global_Astar_floor'])==KSTAR
    nodes=[(F(c),int(p)) for c,p in native['original_source_nodes']]
    assert len(nodes)==107 and sum(p for c,p in nodes)==469
    groups=[]
    for row in env['original_SM40_cells']:
        a,b,w=map(F,row);assert a<b and w>0
        if not groups or a!=groups[-1][-1][1]:groups.append([])
        groups[-1].append((a,b,w))
    assert len(groups)==107 and sum(map(len,groups))==3892
    tables=[];used=[];mass=F(0)
    for (c,pmax),cells in zip(nodes,groups):
        assert c==(cells[0][0]+cells[-1][1])/2
        rawcost=[]
        for p in range(pmax+1):
            factor=2*B*OMEGA**(2*p)/(F(2*p+1)*factorial(p)**2)
            rawcost.append(sum((2*(b-a)*w*factor*max(abs(a-c),abs(b-c))**(2*p) for a,b,w in cells),F(0)))
        # With p available constraints, any lower derivative order is legal.
        chosen=[min(range(p+1),key=lambda k:rawcost[k]) for p in range(pmax+1)]
        tables.append([rawcost[k] for k in chosen]);used.append(chosen)
        mass+=sum((2*(b-a)*w for a,b,w in cells),F(0))
    assert mass==F(1073441879,64000000)
    counts=[p for c,p in nodes];epsilon=sum((v[p] for v,p in zip(tables,counts)),F(0));budget=KSTAR*TARGET
    assert epsilon<budget;trace=[]
    while True:
        choices=[(tables[i][p-1]-tables[i][p],i) for i,p in enumerate(counts) if p>0]
        if not choices:break
        delta,i=min(choices);assert delta>=0
        if epsilon+delta>=budget:break
        old=counts[i];counts[i]-=1;epsilon+=delta
        trace.append(dict(cluster=i,old_multiplicity=old,new_multiplicity=old-1,increment=str(delta),epsilon_after=str(epsilon)))
        assert time.monotonic()-start<30,'bounded 30-second exact rank-allocation guard'
    rank=1+sum(counts)  # retain the original true pole, without using a pole-free floor
    assert rank==242 and len(trace)==470-rank==228
    tail=epsilon/KSTAR;assert tail<TARGET
    lower=F(prior['fourth_eigenvalue_lower']);level=F(prior['critical_level']);assert lower>level>TARGET
    rows=[]
    for i,((c,pmax),n,cells) in enumerate(zip(nodes,counts,groups)):
        p=used[i][n];rows.append(dict(cluster=i,center=str(c),original_multiplicity=pmax,retained_multiplicity=n,proof_derivative_order=p,lo=str(cells[0][0]),hi=str(cells[-1][1]),SM40_cell_count=len(cells),negative_payment=str(tables[i][n])))
    out=dict(status='CONDITIONAL_ORIGINAL_BS_PRUNED_RANK_UPPER',input_sha256=PINS,physical_half_width=str(B),original_source_rank_upper=470,
      retained_original_pole=True,retained_sine_cosine_constraints=sum(counts),retained_physical_rank_upper=rank,removed_original_constraints=len(trace),selected_multiplicities=counts,
      original_nodes=native['original_source_nodes'],cluster_witnesses=rows,local_cost_tables=[[str(x) for x in row] for row in tables],proof_orders_by_available_multiplicity=used,greedy_removal_trace=trace,
      original_SM40_two_sided_mass=str(mass),complete_107_clusters_paid=True,complete_3892_cells_paid=True,zero_constraint_cluster_count=sum(p==0 for p in counts),
      pruned_physical_complement_negative_upper=str(epsilon),inherited_global_Astar_floor=str(KSTAR),declared_BS_tail_target=str(TARGET),BS_complement_operator_upper=str(tail),
      BS_deflation_subspace='range(Kminus^(1/2) J_selected), with J_selected a SUBSPACE of original J470 including the true pole',
      eigenvalue_index=rank+1,eigenvalue_upper=str(tail),critical_level=str(level),critical_count_lower=4,critical_count_upper=rank,fourth_eigenvalue_lower=str(lower),
      previous_rank_upper=470,previous_BS_tail_upper=prior['BS_complement_operator_upper'],complement_inverse_upper=str(1/(1-tail)),generic_sufficient_finite_threshold=str(1-tail),
      full_J470_compressed_inverse_transferred=False,actual_reduced_projection_computed=False,actual_inverse_computed=False,finite_or_mixed_gate_certified=False,
      globally_minimal_rank_claimed=False,uniform_improvement_over_previous_tail_claimed=False,global_true_BS_norm_upper_one_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
    path=Path(args.output);path.parent.mkdir(exist_ok=True,parents=True);path.write_text(json.dumps(out,indent=2)+'\n')
    print('ORIGINAL BS RANK PRUNING PASS: 242 retained constraints, lambda243<1/2; critical count 4..242; full finite/mixed Schur OPEN; seconds',round(out['elapsed_seconds'],2))
    print('Actual tail',float(tail),'zero-constraint clusters still paid',out['zero_constraint_cluster_count'])
if __name__=='__main__':main()
