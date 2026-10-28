#!/usr/bin/env python3
"""NF374 independent exact-rational replay: original matched signed high tails.

Consumes archived native Arb outward derivative Gram and original NF372
exact Fractions; does NOT claim full exterior residual or original-domain audit.
"""
import argparse,hashlib,json,re
from fractions import Fraction as F
from decimal import Decimal
from pathlib import Path

# Open rational outward caps; conservative compared with native 4096-bit output.
CURVATURE_UP=(F(23,10**5),F(14,10**6),F(27,10**7),F(21,10**7))
ENDPOINT_UP=(F(81,10**12),F(44,10**13),F(102,10**14),F(78,10**14))
DERIVATIVE_UP=(F(224,10**8),F(13,10**8),F(27,10**9),F(21,10**9))
LOWBAND_TARGET=(F(36,10**12),F(73,10**13),F(59,10**14),F(28,10**14))
D=(F(65,10**19),F(27,10**20),F(21,10**22),F(49,10**23))
MU=F(49,50000)
B=F(11,10)
C0=F(1,240)
C1=F(1,4*10**10)
BALL=re.compile(r'^\[([^ ]+) \+/- ([^\]]+)\]$')

def outward(v):
    # Arb version 0.8.0 prints dyadic rounded outward dyadic intervals as
    # a decimal midpoint +/- explicit nonnegative decimal radius. Exact
    # rational summation is deliberately used for the replay comparison.
    s=str(v).strip()
    match=BALL.fullmatch(s)
    if match:
        mid,rad=map(lambda x:F(Decimal(x)),match.groups())
        assert rad>=0
        return mid+rad
    return F(Decimal(s))

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def run(args):
    native=json.loads(Path(args.native).read_text())
    nf372=json.loads(Path(args.nf372).read_text())
    assert native['standing']=='NATIVE ARB CORRELATED ORIGINAL DERIVATIVE NORM CERTIFICATE ONLY'
    assert native['working_precision_bits']==4096
    assert native['native_parent_physical_quotient_overlap_pass'] is True
    assert native['full_exterior_residual_certified'] is False
    assert native['complete_original_multiplier_high_tail_certified'] is False
    assert native['original_repository_rank_sha256']=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
    assert native['pr355_portable_source_sha256']=='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
    assert native['nf369_portable_fields_sha256']=='3e73a12bbd70158a461d9722dc8fc499eee8d17baf0afc9090bac5d10165e7e8'
    assert nf372['selected_rank']==242
    assert nf372['cutoff']==str(2**24) or nf372['cutoff']==2**24
    assert len(native['nf374_curvature'])==len(native['boundary_jets'])==len(nf372['directions'])==4
    rows=[]
    for i in range(4):
        curvature=native['nf374_curvature'][i]
        endpoint=native['boundary_jets'][i]
        source=nf372['directions'][i]
        assert curvature['direction']==endpoint['direction']==source['direction']==i+1
        assert curvature['sufficient_NF373_K_le_one_hundredth'] is True
        q2=outward(curvature['whole_interval_second_derivative_L2_squared'][1])
        assert q2>=0
        cap=CURVATURE_UP[i]
        assert B/2*q2<cap*cap, ('curvature upper fails',i+1)
        assert outward(curvature['K_integral_abs_upper'])<cap
        assert outward(endpoint['w_endpoint_abs_upper'])<ENDPOINT_UP[i]
        assert outward(endpoint['w_derivative_abs_upper'])<DERIVATIVE_UP[i]
        src=F(source['complete_raw_source_log_tail_strict_upper'])
        # Physical Fourier multiplier m and even/odd pole form restrictions
        # are inherited. All three payments are strict upper inequalities:
        high=src+C0*ENDPOINT_UP[i]+C1*(DERIVATIVE_UP[i]+cap)
        limit_square=MU*D[i]/4
        assert high*high<limit_square, ('original high tail too costly',i+1)
        assert (LOWBAND_TARGET[i]+high)**2<limit_square, ('future low-band target not sufficient',i+1)
        # Exact ratio safety margin: high < budget/4? may fail, no assumption.
        rows.append(dict(direction=i+1,
                         native_whole_derivative_squared_abs_upper=str(q2),
                         rigorous_K_L1_strict_upper=str(cap),
                         source_only_log_tail_strict_upper=str(src),
                         whole_matched_log_tail_strict_upper=str(high),
                         individual_strong_residual_squared_ceiling=str(limit_square),
                         whole_high_tail_below_individual_ceiling=True,
                         future_sufficient_lowband_strict_upper=str(LOWBAND_TARGET[i]),
                         future_lowband_plus_high_criterion_strictly_below_quarter_budget=True,
                         low_band_residual_measured=False))
    assert native['W_ODD_NEG']==native['RH']=='OPEN'
    out=dict(standing='ORIGINAL MATCHED FOUR-DIRECTION HIGH-FREQUENCY SUFFICIENT TAIL CERTIFIED (inherited operator assumptions)',
             native_report_sha256=sha(args.native),original_nf372_report_sha256=sha(args.nf372),
             frequency_cutoff=2**24,original_selected_source_count=242,
             exact_outward_rational_replay=True,directions=rows,
             full_frequency_residual_certified=False,low_band_matched_projection_residual_certified=False,
             infinite_exterior_schur_certified=False,original_domain_review='OPEN',
             other_238_directions='OPEN',W_ODD_NEG='OPEN',RH='OPEN')
    if args.output:Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS all four actual ORIGINAL matched high-frequency multiplier tail sufficient budgets; low-band and full Schur OPEN')
    for r in rows:print('direction',r['direction'],'HIGH<',r['whole_matched_log_tail_strict_upper'])
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True);p.add_argument('--nf372',required=True)
    p.add_argument('--output',default=None)
    run(p.parse_args())
