#!/usr/bin/env python3
"""Exact spectral-density witnesses for SI29 rank modulo the full original J470.

The analytic proof is in the companion note. Point evaluation is used only
after entire continuation and spectral uniqueness, NOT as an L2-bounded
physical dual functional. No quantitative projected eigenvalue is claimed.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from verify_rpb108_si29_normalized_residual_coordinates import constants, inverse
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR

def density(feature, eta):
    c,r,d = feature
    if not c-r < eta < c+r:
        return F(0)
    return 1/(2*r) if d == 0 else 3*(eta-c)/(2*r*r)

def matmul(a,b):
    return [[sum((x*y for x,y in zip(row,col)),F(0))
             for col in zip(*b)] for row in a]

def run(source, coordinates):
    old_nodes, features = constants(source)
    assert features == tuple((c,r,d) for c,r,delta,d in FEATURES)
    assert len(features) == 14 and KAPPA_STAR == F(33621,10**9)
    raw = Path(coordinates).read_bytes()
    z = json.loads(raw)
    assert z['feature_definitions'] == [[str(c),str(r),d] for c,r,d in features]
    M = [[F(v) for v in row] for row in z['frequency_residual_moment_matrix']]
    U = [[F(v) for v in row] for row in z['rational_feature_transform']]
    scales = list(map(F,z['exact_transformed_jet_scales']))
    assert len(U) == len(M) == len(scales) == 14 and all(scales)
    assert all(len(row)==14 for row in U+M)
    assert matmul(M,U) == [[scales[i] if i==j else F(0)
                            for j in range(14)] for i in range(14)]
    clusters,_,_,leaves,_ = protected_inner_cover()
    nodes = [((a+b)/2,taylor_order(b-a,9)[0]) for a,b,_ in clusters]
    assert len(nodes)==107 and leaves==973 and sum(p for c,p in nodes)==469
    assert tuple(nodes[:15])==old_nodes
    assert all(p>0 and c>0 for c,p in nodes)
    assert all(a[0]<b[0] for a,b in zip(nodes,nodes[1:]))
    bands = sorted(set((c-r,c+r) for c,r,d in features))
    assert len(bands)==12
    assert all(0<a<b for a,b in bands)
    assert all(a[1]<=b[0] for a,b in zip(bands,bands[1:]))
    groups=[]; points=[]
    for lo,hi in bands:
        ids=[i for i,(c,r,d) in enumerate(features) if (c-r,c+r)==(lo,hi)]
        degrees=sorted(features[i][2] for i in ids)
        assert degrees in ([0],[0,1])
        c=(lo+hi)/2; r=(hi-lo)/2
        # Stay strictly inside each band and away from every atomic node.
        candidates=[c+r*F(k,4) for k in (0,-2,2,-1,1,-3,3)]
        chosen=[x for x in candidates if all(x!=cj for cj,p in nodes)][:len(ids)]
        assert len(chosen)==len(ids) and len(set(chosen))==len(ids)
        groups.append(dict(band=[str(lo),str(hi)],feature_indices=ids,
                           witness_points=list(map(str,chosen))))
        points.extend(chosen)
    assert len(points)==14 and len(set(points))==14
    D=[[density(f,x) for f in features] for x in points]
    Di=inverse(D)
    identity=[[F(i==j) for j in range(14)] for i in range(14)]
    assert matmul(D,Di)==matmul(Di,D)==identity
    witnesses=[]
    for x in points:
        # At eta=x, L's nonzero real-frequency response is
        # -(4*pi^2*x^2+1/4)*(4*pi^2)^469*product(c_j^2-x^2)^p_j.
        product=F(1)
        for c,p in nodes:
            product*=(c*c-x*x)**p
        assert product!=0
        lo,hi=next((lo,hi) for lo,hi in bands if lo<x<hi)
        radius=min([x-lo,hi-x]+[abs(x-c) for c,p in nodes])/2
        assert radius>0 and lo<x-radius<x+radius<hi
        assert all(not x-radius<=c<=x+radius for c,p in nodes)
        witnesses.append(dict(eta=str(x),nonzero_nodal_product=str(product),
                              atom_free_interior_neighborhood_radius=str(radius)))
    return dict(status='EXACT_ORIGINAL_SI29_QUOTIENT_RANK_GEOMETRY_WITH_ANALYTIC_PROOF',
        coordinate_json_sha256=hashlib.sha256(raw).hexdigest(),
        original_source_nodes=[[str(c),p] for c,p in nodes],
        original_J_rank=470,actual_auxiliary_feature_count=14,
        feature_definitions=[[str(c),str(r),d] for c,r,d in features],
        disjoint_interior_band_count=12,feature_groups=groups,
        mean_first_moment_density_convention=['1/(2*r)','3*(eta-c)/(2*r^2)'],
        density_evaluation_matrix=[[str(v) for v in row] for row in D],
        density_evaluation_matrix_inverse=[[str(v) for v in row] for row in Di],
        spectral_witnesses=witnesses,
        physical_formula_annihilator='(D_x^2-1/4)*product_j(D_x^2+4*pi^2*c_j^2)^p_j',
        annihilator_order=2+2*sum(p for c,p in nodes),
        annihilator_applied_to_zero_extensions=False,
        actual_feature_quotient_rank_modulo_full_J470=14,
        actual_augmented_physical_span_dimension=484,
        actual_G_quotient_rank_modulo_full_J470=14,
        invertibility_basis='analytic quotient independence plus inherited Astar coercivity',
        original_Astar_coercivity=str(KAPPA_STAR),
        projected_T_positive_definite_conditional_on_original_domain=True,
        projected_T_inverse_exists_conditional_on_original_domain=True,
        quantitative_projected_T_lower_bound_computed=False,
        energy_conditioning_certified=False,normalized_forcing_entries_computed=False,
        inverse_response_value_certified=False,
        required_dense_484_inverse_for_this_rank_proof=False,
        mathematical_standing='Analytic proof plus exact-rational original geometry and witness replay; not Lean formalized',
        independent_analytic_domain_review='OPEN',W_ODD_NEG='OPEN',even_CC27_Weil_RH='OPEN')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--source',required=True)
    p.add_argument('--coordinates',required=True)
    p.add_argument('--output',default='artifacts/si29_full_J_quotient_rank.json')
    args=p.parse_args()
    z=run(args.source,args.coordinates)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(z,indent=2)+'\n')
    print('SI29 FULL-J QUOTIENT RANK PASS: all actual 14 directions survive J470')
    print('Projected energy inverse exists under inherited original coercivity/domain')
    print('Quantitative lower bound, conditioning and inverse response remain OPEN')
