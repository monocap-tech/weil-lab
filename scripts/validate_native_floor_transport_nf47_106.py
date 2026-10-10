#!/usr/bin/env python3
"""Independent NF47 rational floor, interval inverse, frame and crossing checks.

Does not import the NF47 producer. Does not claim fresh original native-source
replay: the missing immutable archives remain a separately reported blocker.
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path

sys.set_int_max_str_digits(0)
GRID = 10**500
KAPPA = F(207, 1000)
A = F(53, 50)


class Box:
    def __init__(self, low, high=None):
        if isinstance(low, Box):
            self.l, self.h = low.l, low.h
            return
        low, high = F(low), F(low if high is None else high)
        assert low <= high
        self.l = F((low*GRID).__floor__(), GRID)
        self.h = F((high*GRID).__ceil__(), GRID)

    def __add__(self, other):
        other = Box(other)
        return Box(self.l+other.l, self.h+other.h)
    __radd__ = __add__

    def __neg__(self):
        return Box(-self.h, -self.l)

    def __sub__(self, other):
        return self+-Box(other)

    def __rsub__(self, other):
        return Box(other)+-self

    def __mul__(self, other):
        other = Box(other)
        values = [x*y for x in (self.l, self.h) for y in (other.l, other.h)]
        return Box(min(values), max(values))
    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Box(other)
        assert other.l > 0 or other.h < 0
        return self*Box(1/other.h, 1/other.l)

    def mid(self):
        return (self.l+self.h)/2

    def abs(self):
        return max(abs(self.l), abs(self.h))

    def ends(self):
        return [str(self.l), str(self.h)]


def boxmatrix(values):
    return [[Box(*map(F, entry)) for entry in row] for row in values]


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def transpose(x):
    return list(map(list, zip(*x)))


def mm(x, y):
    return [[dot(row, col) for col in zip(*y)] for row in x]


def add(x, y):
    return [[a+b for a, b in zip(rx, ry)] for rx, ry in zip(x, y)]


def scale(x, scalar):
    return [[v*scalar for v in row] for row in x]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def exact_inverse(matrix):
    n = len(matrix)
    augmented = [row[:]+eye(n)[i] for i, row in enumerate(matrix)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if augmented[i][k] != 0)
        augmented[k], augmented[pivot] = augmented[pivot], augmented[k]
        divisor = augmented[k][k]
        augmented[k] = [v/divisor for v in augmented[k]]
        for i in range(n):
            if i != k:
                coefficient = augmented[i][k]
                augmented[i] = [a-coefficient*b for a, b in zip(augmented[i], augmented[k])]
    inverse = [row[n:] for row in augmented]
    assert mm(matrix, inverse) == eye(n) == mm(inverse, matrix)
    return inverse


def inverse_interval(matrix):
    n = len(matrix)
    # The true original matrices are symmetric; use intersection of their
    # redundant enclosures for the single midpoint and uncertainty packet.
    for i in range(n):
        for j in range(i):
            low, high = max(matrix[i][j].l, matrix[j][i].l), min(matrix[i][j].h, matrix[j][i].h)
            assert low <= high
            matrix[i][j] = matrix[j][i] = Box(low, high)
    mid = [[v.mid() for v in row] for row in matrix]
    lower, diagonal = eye(n), []
    for k in range(n):
        value = mid[k][k]-sum((lower[k][j]**2*diagonal[j] for j in range(k)), F(0))
        assert value > 0
        diagonal.append(value)
        for i in range(k+1, n):
            lower[i][k] = (mid[i][k]-sum((lower[i][j]*lower[k][j]*diagonal[j] for j in range(k)), F(0)))/value
    transform = exact_inverse(lower)
    congruence = mm(mm(transform, matrix), transpose(transform))
    gap = min(row[i].l-sum((v.abs() for j, v in enumerate(row) if j != i), F(0))
              for i, row in enumerate(congruence))
    assert gap > 0
    inverse = exact_inverse(mid)
    product = mm(inverse, matrix)
    residual = [[Box(int(i == j))-product[i][j] for j in range(n)] for i in range(n)]
    rho = max(sum((v.abs() for v in row), F(0)) for row in residual)
    assert rho < 1
    error = max(sum(map(abs, row)) for row in inverse)*rho/(1-rho)
    return [[Box(v-error, v+error) for v in row] for row in inverse], dict(
        exact_midpoint_inverse_verified=True, rational_congruence_gap=str(gap),
        inverse_residual_upper=str(rho), inverse_entry_error_upper=str(error))


def logs(n, terms=220):
    z = F(n-1, n+1)
    value = sum((2*z**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    return value, value+2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))


def coefficients(n):
    row = [F(1, 2*n+3)]
    for _ in range(6):
        square = [F(0)]*(2*len(row)-1)
        for i, x in enumerate(row):
            for j, y in enumerate(row):
                square[i+j] += x*y
        row = [F(1, 2*n+3)]+[x/F(2*n+2*j+5) for j, x in enumerate(square)]
    return row


def round_up(x, grid):
    return F((x*grid).__ceil__(), grid)


def round_down(x, grid):
    return F((x*grid).__floor__(), grid)


def validate_floor(cert):
    logarithms = {n: logs(n) for n in (2, 3, 5, 7)}
    logarithms[4] = tuple(2*v for v in logarithms[2])
    logarithms[8] = tuple(3*v for v in logarithms[2])
    logarithms[9] = tuple(2*v for v in logarithms[3])
    logarithms[14] = tuple(a+b for a, b in zip(logarithms[2], logarithms[7]))
    logarithms[15] = tuple(a+b for a, b in zip(logarithms[3], logarithms[5]))
    logarithms[16] = tuple(4*v for v in logarithms[2])
    assert logarithms[8][1] < 2*A < logarithms[9][0]
    def atan(x):
        value = sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(65)), F(0))
        error = x**131/F(131)
        return value-error, value+error
    first, second = atan(F(1, 5)), atan(F(1, 239))
    pi = (16*first[0]-4*second[1], 16*first[1]-4*second[0])
    maximum = F(0)
    # A distinct 12000-cell cover with a separately implemented interval
    # row bound revalidates the 207/1000 target, not just NF10's 17/100.
    mesh = 12000
    for k in range(mesh):
        low, high = -A+2*A*k/mesh, -A+2*A*(k+1)/mesh
        denominator = F(5, 8)+F(3, 8)*(0 if low <= 0 <= high else min(low*low, high*high))/A**2
        numerator = F(0)
        for n in (2, 3, 4, 5, 7, 8):
            amplitude = logarithms[2 if n in (4, 8) else n][1]/F(isqrt(n*10**36), 10**18)
            for sign in [-1, 1]:
                delta = [sign*v for v in logarithms[n]]
                ylow, yhigh = low+min(delta), high+max(delta)
                if yhigh <= -A or ylow >= A:
                    continue
                ylow, yhigh = max(ylow, -A), min(yhigh, A)
                numerator += amplitude*(F(5, 8)+F(3, 8)*max(ylow*ylow, yhigh*yhigh)/A**2)
        maximum = max(maximum, numerator/denominator)
    prime = round_up(maximum, 10**12)
    base = coefficients(112)
    argument = round_up(2*A*pi[1]*16, 10**8)
    rate = 225-2*sum((v*argument**(2*j+2) for j, v in enumerate(base)), F(0))
    assert rate > 80
    for n in range(113, 160):
        assert all(F(0) < x <= y for x, y in zip(coefficients(n), base))
    masses = {}
    for cutoff in [14, 15, 16]:
        low, high = round_down(2*A*pi[0]*cutoff, 10**8), round_up(2*A*pi[1]*cutoff, 10**8)
        assert high*high < 112*113
        double_factorial = factorial(225)//(2**112*factorial(112))
        mass = F(0)
        for n in range(112, 160):
            c = coefficients(n)
            exponent = round_down(sum((c[j]*low**(2*j+2)/F(j+1) for j in range(12)), F(0)), 1000)
            exp_lower = sum((exponent**j/F(factorial(j)) for j in range(155)), F(0))
            bound = 4*A*cutoff*(2*n+1)*high**(2*n)/(75*double_factorial**2*exp_lower)
            mass += round_up(bound, 10**18)
            double_factorial *= 2*n+3
        tail_argument = 2*A*F(22, 7)*cutoff
        ratio = tail_argument**2/F(321*323)
        assert ratio < 1
        mass += round_up(4*A*cutoff*tail_argument**320/(double_factorial**2*(1-ratio)), 10**18)
        masses[str(cutoff)] = str(mass)
    assert masses == cert['background_floor']['fresh_NF10_computation']['masses_upper']
    bands = {t: (logarithms[t][0]-F(7, 216*t*t), logarithms[t][1]-F(7, 216*t*t)) for t in [14, 15, 16]}
    arch = bands[16][0]-(bands[14][1]+F(27, 5))*F(masses['14'])
    arch -= (bands[15][1]-bands[14][0])*F(masses['15'])+(bands[16][1]-bands[15][0])*F(masses['16'])
    pole = 16*A*(A/2)**224/F(factorial(112)**2)
    raw = round_down(arch-F(13, 5)-pole, 10**12)
    assert raw == F(cert['background_floor']['fresh_NF10_computation']['raw_complement_lower'])
    independent_lower = raw+F(13, 5)-prime
    assert independent_lower > KAPPA
    saved = cert['background_floor']
    assert F(saved['strict_rebuilt_lower']) == raw+F(13, 5)-F(saved['fresh_NF10_computation']['prime_interval_upper'])
    assert F(saved['strict_rebuilt_lower']) > KAPPA
    assert F(saved['strict_rational_surplus']) == F(saved['strict_rebuilt_lower'])-KAPPA
    return dict(status='PASS', distinct_prime_mesh=mesh, full_prime_upper=str(prime),
                independent_original_F112_lower=str(independent_lower),
                all_48_degrees_and_infinite_tail_paid=True, both_prime_orientations_and_signed_pole_loss_paid=True)


def read(milestone, suffix):
    return json.loads(Path(f'notes/data/RPB108_NF{milestone}_{suffix}_20261009.json').read_bytes())


def validate_frame(row, idx):
    seed = read(24, 'COMPENSATED_SOURCE_TARGETS')['authenticated_compensated_targets'][idx]
    response = read(27, 'RETAINED_COUPLING_CERTIFICATE')['parity_certificates'][idx]
    shared = read(33, 'FIXED_SHARED_REMAINING_LIFT')['parities'][idx]
    retained = [list(map(F, seed['retained_coefficients'])), list(map(F, response['exact_rational_retained_response'])), list(map(F, shared['fixed_probe_coefficients'][:56]))]
    x, w, u = retained
    assert row['retained_indices'] == seed['retained_indices']
    assert all(dot(a, b) == 0 for i, a in enumerate(retained) for b in retained[:i])
    assert list(map(str, [dot(a, a) for a in retained])) == row['retained_masses']
    p, q = row['old_two_constraint_pivots']
    delta = x[p]*w[q]-x[q]*w[p]
    assert delta != 0
    assert abs(delta) == max(abs(x[i]*w[j]-x[j]*w[i]) for i in range(56) for j in range(i+1, 56))
    free = [j for j in range(56) if j not in (p, q)]
    assert free == row['old_free_coordinates']
    columns = []
    for j in free:
        col = [F(int(i == j)) for i in range(56)]
        col[p], col[q] = (x[q]*w[j]-w[q]*x[j])/delta, (w[p]*x[j]-x[p]*w[j])/delta
        assert dot(x, col) == dot(w, col) == 0
        columns.append(col)
    ell = [dot(u, col) for col in columns]
    assert list(map(str, ell)) == row['third_constraint_coordinates']
    pivot = row['third_constraint_pivot_in_old_free_coordinates']
    assert abs(ell[pivot]) == max(map(abs, ell)) > 0
    t53 = [[a-ell[j]/ell[pivot]*b for a, b in zip(col, columns[pivot])]
           for j, col in enumerate(columns) if j != pivot]
    assert len(t53) == row['exact_remaining_dimension'] == 53
    assert all(dot(r, col) == 0 for r in retained for col in t53)
    remaining = [v for j, v in enumerate(free) if j != pivot]
    assert [[col[i] for i in remaining] for col in t53] == eye(53)
    # Check physical columns independently against both frozen selection
    # targets. Those retain the unchanged original vector identities.
    columns = [(d['indices'], list(map(F, d['coefficients']))) for d in row['unchanged_joined_columns']]
    for (ids, values), low in zip(columns, retained):
        assert [dict(zip(ids, values))[j] for j in seed['retained_indices']] == low
    prefix = ['EVEN', 'ODD'][idx]
    tr38 = read(38, prefix+'_FIXED_SECOND_HIGH_DIRECTION')
    def merged(cols, factors):
        values = {}
        for (ids, coeff), factor in zip(cols, factors):
            for j, v in zip(ids, coeff):
                values[j] = values.get(j, F(0))+factor*v
        ids = sorted(values)
        return ids, [values[j] for j in ids]
    assert merged(columns, list(map(F, tr38['exact_moved_target_coefficients']))) == (tr38['merged_target_indices'], list(map(F, tr38['merged_target_coefficients'])))
    tr36 = read(36, prefix+'_FIXED_COLLECTIVE_CORRECTION')
    cert37 = read(37, prefix+'_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE')
    old = [merged([col, (tr36['correction_indices'], list(map(F, tr36['fixed_rational_correction_coefficients'])))], [F(1), F(v)])
           for col, v in zip(columns, cert37['selected_rational_functional'])]
    assert merged(old, list(map(F, tr36['exact_mixed_target_coefficients']))) == (tr36['merged_target_indices'], list(map(F, tr36['merged_target_coefficients'])))
    # All off-retained coordinates are legitimate high directions; hence
    # e=X alpha+T beta and h->h-(P-X)alpha are exact same-domain transport.
    assert all(j >= 112 or j in seed['retained_indices'] for ids, _ in columns for j in ids)
    return dict(parity=prefix.lower(), status='PASS', exact_rank=53,
                physical_constraints_and_frozen_vector_identities=True, omitted_retained_directions_count=53)


def validate_packet(idx):
    count = 'eight' if idx == 0 else 'seven'
    cert = read(46 if idx == 0 else 45, 'EVEN_NEXT_SHELL_CERTIFICATE' if idx == 0 else 'ODD_INVERSE_WITNESS_CERTIFICATE')
    prior = read(37, ['EVEN', 'ODD'][idx]+'_FREE_CORRECTION_FUNCTIONAL_CERTIFICATE')
    matrices = [boxmatrix(cert[k]) for k in [count+'_high_physical_Gram', count+'_high_native_Gram', count+'_high_complete_source_Gram', 'joined_'+count+'_high_native_crosses', 'joined_'+count+'_high_source_crosses']]
    mass, native, source, cross, covariance = matrices
    c = add(native, scale(mass, -KAPPA))
    _, cp = inverse_interval(c)
    t = add(add(source, scale(native, -2*KAPPA)), scale(mass, KAPPA*KAPPA))
    w = add(covariance, scale(cross, -KAPPA))
    n = add(c, scale(t, 1/KAPPA))
    ni, np = inverse_interval(n)
    g = boxmatrix(prior['original_selected_complete_source_Gram'])
    reaction = add(scale(g, 1/KAPPA), scale(mm(mm(w, ni), transpose(w)), -1/(KAPPA*KAPPA)))
    q = boxmatrix(prior['original_selected_native_energy_Gram'])
    lower = add(q, scale(reaction, -1))
    saved = boxmatrix(cert['conditional_'+count+'_high_joined_Schur_lower_matrix'])
    assert all(max(a.l, b.l) <= min(a.h, b.h) for ra, rb in zip(lower, saved) for a, b in zip(ra, rb))
    # Independent sequential elimination, instead of the producer's 2x2
    # condensed formula. Each interval operation is rounded outwards.
    first = lower[0][0]
    second = lower[1][1]-lower[1][0]*lower[0][1]/first
    right = lower[2][2]-lower[2][0]*lower[0][2]/first
    left_cross = lower[2][1]-lower[2][0]*lower[0][1]/first
    right_cross = lower[1][2]-lower[1][0]*lower[0][2]/first
    last = right-left_cross*right_cross/second
    assert min(first.l, second.l, last.l) > 0
    return dict(parity=['even', 'odd'][idx], status='PASS',
                independent_inverse_enclosures=[cp, np], independent_last_pivot=last.ends(),
                original_source_replay=False, stored_packet_interval_sign=True)


def controls():
    rows = []
    for factor in [F(1), F(1, 10**18)]:
        background = [[F(1), F(1, 2)], [F(1, 2), F(1)]]
        coupling = [F(-1, 4), F(1, 2)]
        true_reaction = dot(coupling, [dot(r, coupling) for r in exact_inverse(background)])
        assert true_reaction == F(7, 12)
        for value in [F(-1, 100), F(0), F(1, 100)]:
            q = F(7, 12)+value
            whole = [[q]+coupling] + [[coupling[i]]+background[i] for i in range(2)]
            null = [F(1), F(2, 3), F(-5, 6)]
            assert dot(null, [dot(r, null) for r in whole]) == value
            if value == 0:
                assert all(dot(r, null) == 0 for r in whole)
            assert q-F(1, 4)-F(1, 16) == F(13, 48)+value > 0
            rows.append(dict(scale=str(factor), exact_joint_margin=str(factor*value), invalid_separate_margin=str(factor*(F(13, 48)+value)), crossing='negative' if value < 0 else 'null' if value == 0 else 'positive'))
    levels = []
    null = [F(1), F(2, 3), F(-5, 6)]
    base = [[F(7, 12), F(-1, 4), F(1, 2)], [F(-1, 4), F(1), F(1, 2)], [F(1, 2), F(1, 2), F(1)]]
    for delta in [F(1, 1000), F(1, 10), F(2)]:
        shifted = add(base, scale(eye(3), delta))
        assert [dot(r, null) for r in shifted] == [delta*v for v in null]
        assert dot(null, [dot(r, null) for r in shifted])/dot(null, null) == delta
        # base is PSD by its positive 2x2 background and zero Schur value;
        # shifted >= delta I, with equality on its original null vector.
        levels.append(dict(whole_physical_mass_shift=str(delta), exact_ground_level=str(delta)))
    return dict(genuine_joint_crossings=rows, whole_mass_positive_levels=levels)


def run(path):
    cert = json.loads(Path(path).read_bytes())
    assert cert['milestone'] == 'NF47' and cert['aperture'] == '53/50'
    assert cert['base_commit'] == '6658ff2837838ab00b9b9c605fdd200d473c3293'
    for name, expected in cert['input_sha256'].items():
        assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == expected, name
    assert cert['unconditional_F112_floor'] and cert['fixed_joined_floor_hypothesis_discharged']
    assert not any(cert[k] for k in ['fixed_joined_original_source_replay_newly_completed', 'complete_remaining_transport_certified', 'whole_aperture_positive', 'RH', 'F4', 'Lean'])
    assert cert['literal_NF46_reproduction']['status'] == 'BLOCKED_MISSING_ORIGINAL_NATIVE_ARCHIVES'
    assert cert['literal_NF46_reproduction']['historical_committed_validation_status'] == 'PASS'
    assert cert['highest_certified_whole_aperture'] == '21/20'
    return dict(milestone='NF47', status='PASS', certificate_sha256=hashlib.sha256(Path(path).read_bytes()).hexdigest(),
                frozen_input_custody=True, original_F112_floor=validate_floor(cert),
                remaining_frame_checks=[validate_frame(row, i) for i, row in enumerate(cert['parity_frames'])],
                stored_packet_checks=[validate_packet(i) for i in range(2)], controls=controls(),
                fresh_NF46_original_source_replay='BLOCKED_MISSING_ORIGINAL_NATIVE_ARCHIVES',
                complete_remaining_transport_certified=False, whole_aperture_positive=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', default='notes/data/RPB108_NF47_FLOOR_TRANSPORT_CERTIFICATE_20261009.json')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    Path(args.output).write_text(json.dumps(run(args.certificate), indent=2, sort_keys=True)+'\n')
