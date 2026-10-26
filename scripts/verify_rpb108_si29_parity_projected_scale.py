#!/usr/bin/env python3
"""Original SI29 projected energy/forcing upper bounds using reflected Hermite nodes.

No projected lower bound, condition number, forcing value or inverse response.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order
from verify_rpb108_si29_normalized_residual_coordinates import constants, B, PI_UP

def run(source, coordinates):
    raw = Path(coordinates).read_bytes()
    z = json.loads(raw)
    old_nodes, features = constants(source)
    assert z['interpolation_nodes'] == [[str(c), p] for c, p in old_nodes]
    assert z['feature_definitions'] == [[str(c), str(r), d] for c, r, d in features]
    assert z['exact_modular_jet_rank'] == 14
    M = [[F(v) for v in row] for row in z['frequency_residual_moment_matrix']]
    U = [[F(v) for v in row] for row in z['rational_feature_transform']]
    scales = list(map(F, z['exact_transformed_jet_scales']))
    assert len(U) == len(M) == 14 and all(len(r) == 14 for r in U+M)
    assert all(sum((M[i][k]*U[k][j] for k in range(14)), F(0)) ==
               (scales[i] if i == j else 0) for i in range(14) for j in range(14))
    clusters, _, _, leaves, _ = protected_inner_cover()
    nodes = [((a+b)/2, taylor_order(b-a, 9)[0]) for a,b,_ in clusters]
    assert len(nodes) == 107 and leaves == 973 and sum(p for c,p in nodes) == 469
    assert tuple(nodes[:15]) == old_nodes
    selected = nodes[:40]
    physical_count = sum(p for c,p in selected)
    N = 2*physical_count
    assert physical_count == 215 and N == 430
    R = max(max(c for c,p in selected), max(c+r for c,r,d in features))
    Cx = 2*PI_UP*R + F(N, B)
    assert R == F(7229,128) and Cx < 746
    errors = []
    products = []
    for c,r,d in features:
        # Reflected nodal product at eta in [c-r,c+r]:
        # product_j |eta^2-c_j^2|^p_j. Both endpoints bound each factor
        # since eta>0 and eta^2 is monotone. Nodes themselves may lie inside.
        product = F(1)
        for cj,p in selected:
            product *= max(abs((c-r)**2-cj*cj), abs((c+r)**2-cj*cj))**p
        variation = F(3,2) if d else F(1)
        e = variation*(2*PI_UP*B)**N*product/factorial(N)
        products.append(product)
        errors.append(e)
    g = [sum((abs(U[i][j])*errors[i] for i in range(14)), F(0))
         for j in range(14)]
    trace = 2*B*sum((e*e for e in g), F(0))
    energy = (36*2*B+(2+2*B*Cx)**2)*sum((e*e for e in g), F(0))
    assert max(g) < F(2,10**59)
    hs = F(3,10**59)
    assert trace < hs*hs
    assert energy < F(102,10**113)
    forcing = []
    for bound in (1400000,350000):
        forcing.append(dict(original_ray_Ao_action_norm_upper=bound,
                            actual_Gstar_R0_vector_norm_upper=str(hs*bound)))
    return dict(status='CONDITIONAL_ORIGINAL_FULL_J_PROJECTED_SI29_UPPER_BOUNDS',
        coordinate_json_sha256=hashlib.sha256(raw).hexdigest(),
        full_original_J_count=470, full_cluster_count=107, unresolved_leaf_count=leaves,
        selected_original_nodes=[[str(c),p] for c,p in selected],
        selected_physical_source_count=physical_count, reflected_Hermite_order=N,
        added_physical_source_count=0, convex_hull_radius=str(R),
        derivative_to_uniform_error_factor=str(Cx),
        reflected_band_product_upper=list(map(str,products)),
        actual_feature_uniform_error_upper=list(map(str,errors)),
        actual_coordinate_uniform_error_upper=list(map(str,g)),
        full_J_L2_projected_coordinate_HS_squared_upper=str(trace),
        full_J_L2_projected_coordinate_HS_upper=str(hs),
        full_J_Astar_projected_coordinate_Schur_trace_upper=str(energy),
        full_J_Astar_projected_coordinate_Schur_operator_upper=str(F(102,10**113)),
        original_stopping_ray_matched_forcing_bounds=forcing,
        forcing_scope='Gstar R0 with Jstar R0=0 for the complete original Galerkin residual',
        representative_change='G-(H_reflected-H_106)U=(F-H_reflected)U; difference belongs to full J470',
        exact_projected_T_or_forcing_entries_computed=False,
        projected_T_lower_bound_certified=False,
        energy_conditioning_certified=False, inverse_response_certified=False,
        W_ODD_NEG='OPEN', inherited_original_analytic_domain_review='OPEN',
        even_CC27_Weil_RH='OPEN')

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--source', required=True)
    p.add_argument('--coordinates', required=True)
    p.add_argument('--output', default='artifacts/si29_parity_projected_scale.json')
    args=p.parse_args()
    z=run(args.source,args.coordinates)
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(z,indent=2)+'\n')
    print('PARITY PROJECTED SCALE PASS: same J470 and actual 14 SI29 features')
    print('Projected T operator upper <1.02e-111; HS upper <3e-59')
    print('Matched forcing bounds 4.2e-53 / 1.05e-53; inverse response OPEN')
