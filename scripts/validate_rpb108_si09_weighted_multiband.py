#!/usr/bin/env python3
"""SI09: exact-rational weighted/merged multiband rank-error optimization.

Starting with SI07's proven ORIGINAL SIGNED negative-frequency interval cover,
construct a trace-mass-weighted Taylor certificate on physically supported
modulated-polynomial subspaces. Every accepted greedy move preserves the full
operator-norm error bound. No floats are used for decisions or certificates.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from functools import lru_cache
from math import factorial
from validate_rpb108_si06_negative_band import B, prime_interval
from validate_rpb108_si07_negative_support_cover import (
    END, DEPTH, M, DEN, arch_lower_cell, ceil_fraction,
)
from validate_rpb108_si08_multiband_rank import PI_UP, taylor_order

BIT_TARGETS = (40, 64, 80, 96)


@dataclass(frozen=True)
class Group:
    left: F
    right: F
    mass: F   # full + and - certified upper integral of m_- on this band
    order: int

    @property
    def width(self):
        return self.right - self.left


def original_clusters():
    leaves = []
    accepted = 0

    def visit(left, right, arch, depth):
        nonlocal accepted
        mid = (left + right) / 2
        lower = arch + prime_interval(mid)[0] - M*(right-left)/2
        if lower > 0:
            accepted += 1
            return
        if depth < DEPTH:
            visit(left, mid, arch, depth+1)
            visit(mid, right, arch, depth+1)
            return
        height = F(ceil_fraction((-lower)*DEN), DEN)
        assert 0 < height and height >= -lower
        leaves.append((left, right, height))

    for j in range(END):
        visit(F(j), F(j+1), arch_lower_cell(j), 0)

    assert len(leaves) == 972 and accepted == 9261
    leaves.sort(key=lambda z: z[0])
    assert sum((r-l for l,r,_ in leaves), F(0)) == F(243,16)
    groups = []
    for left, right, height in leaves:
        mass = 2*height*(right-left)
        if groups and left == groups[-1].right:
            prior = groups[-1]
            groups[-1] = Group(prior.left, right, prior.mass+mass, 0)
        else:
            groups.append(Group(left, right, mass, 0))
    assert len(groups) == 107
    assert sum((g.width for g in groups), F(0)) == F(243,16)
    total_mass = sum((g.mass for g in groups), F(0))
    assert total_mass < 38
    assert 2*B*total_mass < 83
    return groups, total_mass


@lru_cache(maxsize=None)
def eps(width, order):
    assert order >= 0 and width >= 0
    if order == 0:
        return F(1)
    radius = PI_UP*B*width
    # Taylor integral remainder: |e^(it)-sum_(k<p)(it)^k/k!|
    # <= |t|^p/p!, but the zero approximant always yields error <=1.
    return min(F(1), radius**order/F(factorial(order)))


def error_sum(groups):
    return sum((g.mass*eps(g.width, g.order) for g in groups), F(0))


def rank(groups):
    # both + and - clusters, plus the EXACT negative odd pole vector
    return 2*sum(g.order for g in groups)+1


def weighted_drop(groups, error_target):
    groups = list(groups)
    used = error_sum(groups)
    removed = 0
    while True:
        best = None
        for j, group in enumerate(groups):
            if group.order == 0:
                continue
            old = eps(group.width, group.order)
            new = eps(group.width, group.order-1)
            delta = group.mass*(new-old)
            assert delta >= 0
            if used+delta >= error_target:
                continue
            if best is None or delta < best[0]:
                best = (delta, j)
        if best is None:
            break
        delta, j = best
        group = groups[j]
        groups[j] = Group(group.left, group.right, group.mass, group.order-1)
        used += delta
        removed += 1
    assert used == error_sum(groups)
    assert used < error_target
    return groups, removed


def merge_no_extra_error(groups):
    groups = list(groups)
    merges = 0
    saved_orders = 0
    while True:
        selected = None
        for j in range(len(groups)-1):
            a, b = groups[j], groups[j+1]
            old = a.mass*eps(a.width,a.order) + b.mass*eps(b.width,b.order)
            upper_order = a.order+b.order-1
            width = b.right-a.left
            if upper_order < 0:
                continue
            candidate = None
            for p in range(upper_order+1):
                if (a.mass+b.mass)*eps(width,p) <= old:
                    candidate = p
                    break
            if candidate is None:
                continue
            saving = a.order+b.order-candidate
            if saving > 0 and (selected is None or saving > selected[0]):
                selected = (saving,j,candidate)
        if selected is None:
            break
        saving,j,p=selected
        a,b=groups[j],groups[j+1]
        groups[j:j+2]=[Group(a.left,b.right,a.mass+b.mass,p)]
        merges += 1
        saved_orders += saving
    return groups, merges, saved_orders


def validate():
    raw,total_mass=original_clusters()
    print("SI09 source: exact original signed SI07 cover, 107 positive clusters")
    print("total signed negative m_- integrated mass upper:",float(total_mass))
    print("physical negative operator trace upper:",float(2*B*total_mass))
    positive_result = False
    for bits in BIT_TARGETS:
        # SI08's certified starting point: each cluster has epsilon<2^-bits.
        seeded=[Group(g.left,g.right,g.mass,taylor_order(g.width,bits)[0])
                for g in raw]
        baseline=rank(seeded)
        expected={40:2503,64:3541,80:4165,96:4757}[bits]
        assert baseline == expected
        target=F(1,2**(bits-8))/(4*B)
        assert error_sum(seeded) < target
        weighted,first_drops=weighted_drop(seeded,target)
        merged,merge_count,merge_saved=merge_no_extra_error(weighted)
        optimized,last_drops=weighted_drop(merged,target)
        cost=error_sum(optimized)
        assert cost < target
        assert sum(g.mass for g in optimized)==total_mass
        assert rank(optimized)<=baseline and rank(optimized)%2==1
        # Every grouped interval remains bounded within [0,896] and the
        # original fully-certified negative Fourier cover is contained.
        assert optimized[0].left == raw[0].left
        assert optimized[-1].right == raw[-1].right
        for a,b in zip(optimized,optimized[1:]):
            assert a.right <= b.left
        if rank(optimized)<baseline: positive_result=True
        print("bits:",bits, "SI08 rank:",baseline,
              "SI09 certified rank:",rank(optimized),
              "bands:",len(optimized),
              "weighted order drops:",first_drops+last_drops,
              "safe merges:",merge_count,
              "saved orders from merges:",merge_saved,
              "error <",f"2^-{bits-8}")
        print("actual rational norm-error upper approximation:",float(4*B*cost))
    assert positive_result
    print("SI09 PASS: fully certified weighted/merged negative-operator compression")
    print("All rank/error statements concern negative SOURCE only; full Weil positivity, Stage I, RH OPEN.")


if __name__ == "__main__":
    validate()
