#!/usr/bin/env python3
"""CP030 six-scalar 10^-9 outward cells for original Zeta M=6,N=256.

This is an EXTERNAL integer-directed arithmetic generator, NOT a Lean
certificate. It reuses the exact CP025 255+6 source-oriented evaluator
at its immutable Git blob. Its JSON integers are possible *inputs* to a
future proof of each real/imaginary and rotated-real source inequality;
asserting those integers in Lean as axioms is NOT allowed.

No ordinary CI workflow, new Lake target, source definition, or numerical
admission is created by this script.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / 'scripts/cp025_original_EM_integer_directed_firstjet_root_bracket.py'
LEAN = ROOT / 'cp011_zeta_v435/CP030FiniteComponentCells.lean'
CP028 = ROOT / 'cp011_zeta_v435/CP028CoarseFiniteBoxes.lean'
ENGINE_BLOB = 'e392ad4d5ded49f8314006335fa95ed15c7381de'
ORIGINAL_ZETA_COMMIT = 'c06b4e13d9c847e50a32c3d738271cbad62ae9f3'
SCALE = 10**9
HEIGHTS = {'left': F(15005352,100000), 'right': F(15005353,100000)}
COMP_CAP = F(1,10000)
LEFT_CAP = -F(2,10**7)
RIGHT_FLOOR = F(1,10**6)
EXPECTED_THEOREMS = [
    'norm_of_coordinate_caps',
    'left_coarse_of_scalar',
    'right_coarse_of_scalar',
    'original_narrow_zero_of_scalar_cells',
]

def git_blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def source_audit() -> None:
    if git_blob(ENGINE) != ENGINE_BLOB:
        raise ValueError('CP025 source evaluator drift: no numerical claim authorized')
    s = LEAN.read_text('utf8')
    imports = re.findall(r'(?m)^public import\s+([^\n]+)', s)
    names = re.findall(r'(?m)^theorem\s+(\w+)\b', s)
    ax = re.findall(r'(?m)^#print axioms\s+CP030FiniteComponentCells\.(\w+)\b', s)
    if imports != ['CP028CoarseFiniteBoxes'] or names != EXPECTED_THEOREMS or ax != EXPECTED_THEOREMS:
        raise ValueError('CP030 true source theorem/import/axiom roster drift')
    if re.search(r'(?m)^\s*(?:sorry|admit|axiom|constant|opaque|unsafe)\b', s):
        raise ValueError('CP030 forbidden proof admission')
    for x in ('sourceA tLeft','sourceA tRight','sourceFiniteZ tLeft',
              'sourceFiniteZ tRight','original_narrow_zero_of_two_coarse_boxes'):
        if x not in s:
            raise ValueError('CP030 original source expressions were changed: ' + x)
    prior = CP028.read_text('utf8')
    if 'def FiniteLeftBox : Prop' not in prior or 'def FiniteRightBox : Prop' not in prior:
        raise ValueError('CP028 original coarse box interfaces are not present')
    print('CP030 SOURCE-CONTRACT FOUR CONDITIONAL LEAN CANDIDATES: PASS NOT LEAN')

def exact_controls() -> None:
    assert HEIGHTS['left'] == F('150.05352')
    assert HEIGHTS['right'] == F('150.05353')
    assert F(2,10000) < F(1,1000)
    assert LEFT_CAP < -F(1,10**7)
    assert RIGHT_FLOOR > F(1,10**7)
    # Integer rounding must enclose both positive and negative data.
    for x in (F(-681740867,10**15), F(155197598,10**13), F(1,10**12)):
        a = x.numerator*SCALE//x.denominator
        b = -(-x.numerator*SCALE//x.denominator)
        assert F(a,SCALE) <= x <= F(b,SCALE)
    # Reject false target values stronger than the chosen scalar contracts.
    assert not (F(1,1000) <= F(2,10000))
    assert not (LEFT_CAP <= -F(1,10**6))
    assert not (RIGHT_FLOOR >= F(1,10**4))
    print('CP030 EXACT RATIONAL SIX-CELL SCALAR/ROUNDING CONTROLS: PASS NOT LEAN')

def engine_module():
    spec = importlib.util.spec_from_file_location('cp030_original_cp025_engine', ENGINE)
    if spec is None or spec.loader is None:
        raise ValueError('cannot import pinned CP025 evaluator')
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

def outward_cell(v, engine_scale: int):
    """Floor/ceil an original 10^55 integer interval to 10^-9 integers."""
    return [v.l*SCALE//engine_scale, -(-v.h*SCALE//engine_scale)]

def bounds(cell):
    return F(cell[0],SCALE), F(cell[1],SCALE)

def replay():
    if git_blob(ENGINE) != ENGINE_BLOB:
        raise ValueError('fail closed: original CP025 evaluator was modified')
    m = engine_module()
    if m.S != 10**55 or m.ZETA_COMMIT != ORIGINAL_ZETA_COMMIT:
        raise ValueError('original evaluator scale/commit mismatch')
    m.arithmetic_controls()
    rows = {}
    for side,t in HEIGHTS.items():
        a,_ = m.original_A_and_Ds(t)
        theta,_ = m.original_theta_stirling2_and_prime0(t)
        si,co = m.trig(theta)
        finite = (m.C(co,si)*a).r
        re,im,rot = (outward_cell(v,m.S) for v in (a.r,a.i,finite))
        rlo,rhi = bounds(re)
        ilo,ihi = bounds(im)
        flo,fhi = bounds(rot)
        if not (max(abs(rlo),abs(rhi)) <= COMP_CAP and
                max(abs(ilo),abs(ihi)) <= COMP_CAP):
            raise ValueError(f'{side}: original component caps not met')
        if side == 'left' and not fhi <= LEFT_CAP:
            raise ValueError('original left finite rotated sign not met')
        if side == 'right' and not RIGHT_FLOOR <= flo:
            raise ValueError('original right finite rotated sign not met')
        rows[side] = {
            'exact_height': str(t),
            'A_real_cell_integer_lower_upper_divided_by_10pow9': re,
            'A_imag_cell_integer_lower_upper_divided_by_10pow9': im,
            'thetaStirling2_rotated_real_cell_integer_lower_upper_divided_by_10pow9': rot,
            'component_abs_cap': str(COMP_CAP),
            'sign_boundary': str(LEFT_CAP if side == 'left' else RIGHT_FLOOR),
            'external_exact_directed_interval_checks': True,
            'source_Lean_component_membership_kernel_paid': False,
        }
        print('CP030',side,'integer outward component and rotated cells:',re,im,rot,'EXTERNAL ONLY')
    print('CP030 TRUE ORIGINAL 255+6 FINITE SIX-SCALAR CELLS: 6/6 PASS NOT LEAN')
    return rows

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--self-test',action='store_true')
    p.add_argument('--source-check',action='store_true')
    p.add_argument('--replay',action='store_true')
    p.add_argument('--receipt',type=Path)
    a=p.parse_args()
    if a.self_test: exact_controls()
    if a.source_check: source_audit()
    rows = replay() if a.replay else None
    if a.receipt:
        if rows is None or not a.source_check or not a.self_test:
            raise ValueError('receipt requires real engine replay, exact controls and original source checks')
        data = {
            'status':'CP030_SIX_ORIGINAL_FINITE_SCALAR_CELLS_EXTERNAL_NOT_LEAN',
            'original_zeta_commit':ORIGINAL_ZETA_COMMIT,
            'pinned_cp025_engine_git_blob':git_blob(ENGINE),
            'pinned_cp025_engine_sha256':hashlib.sha256(ENGINE.read_bytes()).hexdigest(),
            'cell_denominator':SCALE,
            'two_heights':rows,
            'six_genuine_original_component_and_rotated_sign_Lean_proofs':False,
            'CP030_conditional_theorem_kernel_accepted':False,
            'CP027_pointwise_Borwein_kernel_accepted':False,
            'original_unconditional_narrow_zeta_zero_kernel_accepted':False,
            'zero_ordinal53':False,
            'global_Weil_positivity_or_RH':False,
        }
        a.receipt.write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
        print(data['status'])
    if not (a.self_test or a.source_check or a.replay):p.print_help()

if __name__ == '__main__':
    try:main()
    except (OSError, ValueError, ZeroDivisionError, AssertionError) as e:
        raise SystemExit('CP030 FAIL CLOSED NOT LEAN: '+str(e))
