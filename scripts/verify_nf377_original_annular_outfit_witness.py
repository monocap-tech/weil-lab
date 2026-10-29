#!/usr/bin/env python3
"""NF377: select ONE actual original J242+E4-out-of-fit odd annular sign-box.

Physical Gram verified by 4096-bit Arb; annulus moments are exact analytic
trigonometric primitives with outward Arb enclosures. Signed multiplier
measurements at rational knots are POINTS, never lowband integrals.
No new selected carrier generator, no W-ODD-NEG/RH closure.
"""
import argparse
import json
import time
from fractions import Fraction as F
from pathlib import Path

import flint
from flint import arb, arb_mat, ctx

import verify_rpb108_si29_full_J_L2_normalization as m
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf374_original_matched_curvature import (
    load, dyad, RANK_SHA, PR355_SHA, NF369_SHA, TNUM
)
from verify_nf376_original_signed_lowband_probe import interval_units, fball
from validate_rpb108_mg07_two_source_original_low32_affine_stop import signed_m_at

B = F(11, 10)
N = 492
H = B / N
SELECTED_LIMIT = F(1, 2)

def integral_sin_cos(c, maximum, endpoint):
    """Integrals 0..endpoint of x^k sin/cos(2*pi*c*x), k=0..maximum."""
    assert c > 0
    w = 2 * arb.pi() * m.a(c)
    t = m.a(endpoint)
    sn, co = (w * t).sin_cos()
    C = [sn / w]
    S = [(1 - co) / w]
    for k in range(1, maximum + 1):
        C.append(t**k * sn / w - k * S[k - 1] / w)
        S.append(-t**k * co / w + k * C[k - 1] / w)
    return C, S

def source_primitive(c, k, endpoint, cache):
    if c is None:
        t = m.a(endpoint)
        return 2 * ((t / 2).cosh() - 1)
    key = (c, endpoint)
    if key not in cache or len(cache[key][0]) <= k:
        cache[key] = integral_sin_cos(c, k, endpoint)
    Cs, Ss = cache[key]
    return Ss[k] if k % 2 == 0 else Cs[k]

def overlaps_for_annulus(i, rows, probes, frequencies, cache):
    """<delta_i,J/F> for delta_i = (o_2t_i - o_2t_{i-1})."""
    a, b = (i - 1) * H, i * H
    z = arb(2).sqrt()
    bj = [z * (source_primitive(c, k, b, cache) -
               source_primitive(c, k, a, cache)) for c, k in rows]
    freq_delta = [z * (source_primitive(c, 0, b, cache) -
                       source_primitive(c, 0, a, cache)) for c in frequencies]
    pole_delta = z * (source_primitive(None, None, b, cache) -
                      source_primitive(None, None, a, cache))
    bf = [sum((m.a(F(v))*freq_delta[j] for j, v in
               enumerate(probe['sine_coefficients'])), arb(0)) +
          m.a(F(probe['sinh_coefficient']))*pole_delta
          for probe in probes]
    return arb_mat([[v] for v in bj]), arb_mat([[v] for v in bf])

def candidate_order():
    # Short preflight tests, followed by the exhaustive Bessel-backed set.
    seen = set()
    for i in (1, N, N//2):
        seen.add(i)
        yield i
    for i in range(1, N + 1):
        if i not in seen:
            yield i

def main():
    parser = argparse.ArgumentParser()
    for arg in ('rank', 'source', 'nf369', 'output'):
        parser.add_argument('--' + arg, required=True)
    parser.add_argument('--bits', type=int, default=4096)
    args = parser.parse_args()
    assert flint.__version__ == '0.8.0'
    assert args.bits >= 4096
    ctx.prec = args.bits
    start = time.monotonic()
    rank = load(args.rank, RANK_SHA)
    source = load(args.source, PR355_SHA)['data']
    parent = load(args.nf369, NF369_SHA)['data']
    assert parent['selected_rank'] == 242
    assert rank['retained_original_pole']
    freqs = [F(z) for z in source['target_sine_frequencies']]
    assert freqs == [F(5*j, 11) for j in range(1,33)]
    probes = source['target_probes']
    assert len(probes) == 4
    rows = []
    for (c, mult), keep in zip(rank['original_nodes'], rank['selected_multiplicities']):
        assert 0 <= keep <= mult
        rows.extend((F(c), k) for k in range(keep))
    assert len(rows) == 241
    rows.append((None, None))
    J = [m.pole_terms() if c is None else m.source_terms(c,k) for c,k in rows]
    F4 = []
    for probe in probes:
        terms = []
        for c, coef in zip(freqs, probe['sine_coefficients']):
            terms.extend((p, kind, f, z*m.a(F(coef))) for p,kind,f,z in m.source_terms(c,0))
        terms.extend((p,kind,f,z*m.a(F(probe['sinh_coefficient']))) for p,kind,f,z in m.pole_terms())
        F4.append(terms)

    print('NF377: verify unchanged J242 Gram and four original F sources', flush=True)
    kernel = m.Integrals()
    gram = arb_mat(242, 242)
    for i in range(242):
        for j in range(i + 1):
            gram[i,j] = gram[j,i] = m.gram(J[i],J[j],kernel)
    D = candidate(gram)
    Nframe = D.transpose()*gram*D
    err = max((sum((abs(Nframe[i,j]-int(i==j))
                    for j in range(242)), arb(0)) for i in range(242)))
    assert err < arb('0.01')
    V = arb_mat([[m.gram(j, f, kernel) for f in F4] for j in J])
    GF = arb_mat([[m.gram(f, g, kernel) for g in F4] for f in F4])
    X4 = D*Nframe.solve(D.transpose()*V, algorithm='lu')
    S4 = GF - V.transpose()*X4
    S4 = (S4 + S4.transpose())/2
    assert all((S4[i,j]-fball(parent['physical_quotient_Gram_native'][i][j])).contains(0)
               for i in range(4) for j in range(4))
    # Outward certification of S4 positive: four principal interval pivots.
    assert all(S4[i,i].lower() > 0 for i in range(4))
    print('NF377: original frame + parent quartet overlap PASS; select physical annulus', flush=True)
    cache = {}
    selected = None
    visited = []
    norm_sq = m.a(H)
    for i in candidate_order():
        bj,bf = overlaps_for_annulus(i, rows, probes, freqs, cache)
        x = D*Nframe.solve(D.transpose()*bj, algorithm='lu')
        stationarity = gram*x - bj
        residual = norm_sq - (bj.transpose()*x)[0,0]
        cross = bf - V.transpose()*x
        eta = S4.solve(cross, algorithm='lu')
        q2 = residual - (cross.transpose()*eta)[0,0]
        visited.append(i)
        # q2 is physically after projecting out J242 plus all E4.
        if q2.lower() > m.a(H/2):
            selected = (i, bj, bf, x, eta, q2, residual, cross, stationarity)
            break
        if len(visited)%50 == 0:
            print('checked',len(visited),'source annuli',flush=True)
    assert selected is not None, 'FAIL: Bessel guaranteed candidate not found with strict outward enclosure'
    i,bj,bf,x,eta,q2,residual,cross,stationarity = selected
    assert 1<=i<=N and q2.lower()>m.a(H/2)
    assert q2.upper()<=norm_sq.upper()
    print('NF377 annulus',i,'out-of-fit L2 norm fraction > 1/2, PASS',flush=True)

    # Diagnostic, genuinely original signed multiplier KNOTS only.
    # The full continuum integral is a separate independent acceptance gate.
    Y0=parent['nf369_quotient_response_exact_dyadic_coefficients']
    M=arb_mat([[dyad(Y0[j][k])+int(j==k) for k in range(4)] for j in range(4)])
    T=arb_mat([[m.a(F(z,2**20)) for z in row] for row in TNUM])
    t=[T[j,3] for j in range(4)]
    fitted=[sum((M[j,k]*T[k,3] for k in range(4)),arb(0)) for j in range(4)]
    a,b=(i-1)*H,i*H
    diagnostic=[]
    for xi in (F(1,4),F(1),F(4),F(8),F(16),F(32)):
        sinus=m.source_terms(xi,0)
        sj=arb_mat([[m.gram(j,sinus,kernel)] for j in J])
        sf=arb_mat([[m.gram(f,sinus,kernel)] for f in F4])
        # ∫_on annulus sin(2*pi*xi*x) with reflected odd normalization.
        sn_a=source_primitive(xi,0,a,cache)
        sn_b=source_primitive(xi,0,b,cache)
        sdelta=arb(2).sqrt()*(sn_b-sn_a)
        se=sf-X4.transpose()*sj
        sq=sdelta-(sj.transpose()*x)[0,0]-(se.transpose()*eta)[0,0]
        su=sum(((t[j]-fitted[j])*sf[j,0] for j in range(4)),arb(0))
        su+=sum((sj[j,0]*sum((X4[j,k]*fitted[k] for k in range(4)),arb(0))
                 for j in range(242)),arb(0))
        lo,hi=signed_m_at(xi)
        cross_signed=2*su*sq*arb(m.a(lo),m.a(hi)-m.a(lo))
        sign='positive' if cross_signed.lower()>0 else 'negative' if cross_signed.upper()<0 else 'unresolved'
        diagnostic.append({'xi':str(xi),
                           'signed_two_sign_cross_integrand_units_1e320':interval_units(cross_signed),
                           'signed_integrand_sign':sign,
                           'sine_amplitude_q_units_1e320':interval_units(sq)})
    out={
      'status':'CERTIFIED_ONE_ORIGINAL_SIGNBOX_ANNULUS_PHYSICAL_OUT_OF_FIT_AND_SIGNED_KNOTS_ONLY',
      'original_rank_sha256':RANK_SHA,'original_source_sha256':PR355_SHA,
      'original_nf369_fields_sha256':NF369_SHA,
      'original_J242_count':242,'fitted_four_count':4,'new_selected_source':False,
      'physical_half_width':'11/10','total_annuli':N,'partition_spacing':str(H),
      'candidate_order_and_visited':visited,
      'selected_annulus_index':i,'selected_positive_half_interval':[str(a),str(b)],
      'annulus_L2_squared_norm':str(H),
      'certified_outfit_squared_norm_units_1e320':interval_units(q2),
      'certified_outfit_squared_norm_fraction_strict_lower':'1/2',
      'certified_unfitted_absolute_L2_norm_lower':'sqrt(11/9840)',
      'J_projected_norm_squared_units_1e320':interval_units(residual),
      'frame_Gram_16_parent_ball_overlap':True,
      'max_stationarity_residual_upper':str(max(abs(stationarity[j,0]).upper() for j in range(242))),
      'signed_frequency_point_samples':diagnostic,
      'actual_signed_lowband_continuum_integral_computed':False,
      'actual_signed_full_frequency_pairing_computed':False,
      'signed_exterior_Schur_upper_computed':False,
      'operator_domain_transfer_proved':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN',
      'elapsed_seconds':time.monotonic()-start
    }
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF377 physical witness PASS; actual signed continuum OPEN',flush=True)

if __name__=='__main__':
    main()
