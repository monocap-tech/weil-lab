#!/usr/bin/env python3
"""
Experimental provenance-safe causal-certificate probe for SZ GERM-48.

This is reconnaissance only. It deliberately keeps a bounded provenance budget:
    k-label b in [-2,2], p-label c in {0,1}.
A compact row is retained only if every nonzero term remains inside that budget.
No term of an exact row is ever dropped.

The probe reports matrix dimensions/ranks and whether the root X,S columns are
forced by the retained subsystem. It is not a proof artifact.
"""
from __future__ import annotations

from collections import defaultdict, deque
import math
import random
import numpy as np

h = math.log(81 / 80)
k = math.log(16 / 15)
p = math.log(10 / 9)
j = math.log(9 / 8)
s = math.log(5 / 4)

beta = (math.log(3) / math.sqrt(3)) / (math.log(2) / math.sqrt(2))
delta = (math.log(5) / math.sqrt(5)) / (math.log(2) / math.sqrt(2))
mu = beta * beta
G = math.sqrt(2)

def coord(label, r):
    a, b, c = label
    return r + a*h + b*k + c*p

def shifted(label, da=0, db=0, dc=0):
    a, b, c = label
    return (a+da, b+db, c+dc)

def provenance_ok(label):
    _, b, c = label
    return -2 <= b <= 2 and 0 <= c <= 1

def node_valid(kind, label, r, u, eps=1e-11):
    x = coord(label, r)
    if kind == "X":
        return eps < x < s-eps
    return eps < x < u-eps

def make_row(terms, r, u):
    row = defaultdict(float)
    for coeff, kind, label in terms:
        if not provenance_ok(label) or not node_valid(kind, label, r, u):
            return None
        row[(kind, label)] += coeff
    return {key: val for key, val in row.items() if abs(val) > 1e-13}

def exact_rows_at(label, r, u):
    """Whole exact compact/middle rows at the coordinate represented by label."""
    t = coord(label, r)
    eps = 1e-10
    out = []

    if eps < t < u-eps:
        # Compact equation 1.
        terms = [(delta, "S", label), (G, "X", label)]
        if t < p-eps:
            terms += [(-mu, "X", shifted(label, da=1, dc=1))]
        elif t > p+eps:
            terms += [(-mu, "S", shifted(label, dc=-1))]
            if t > j+eps:
                terms += [(-mu, "X", shifted(label, da=-1, dc=-1))]
        if t < u-k-eps:
            terms += [(beta, "S", shifted(label, db=1))]
        row = make_row(terms, r, u)
        if row:
            out.append(("E1", label, row))

        # Compact equation 2.
        terms = [(G, "S", label), (delta, "X", label)]
        if t < j-eps:
            terms += [(-mu, "X", shifted(label, dc=1))]
            if t < u-j-eps:
                terms += [(-mu, "S", shifted(label, da=1, dc=1))]
        elif t > j+eps:
            terms += [(-mu, "S", shifted(label, da=-1, dc=-1))]
        if t > k+eps:
            terms += [(beta, "X", shifted(label, db=-1))]
        row = make_row(terms, r, u)
        if row:
            out.append(("E2", label, row))

    # Exact middle-overlap equations.
    if u+eps < t < s-eps:
        if u < j-eps and t < j-eps:
            row = make_row([
                (mu, "S", shifted(label, dc=-1)),
                (-G, "X", label),
            ], r, u)
            if row:
                out.append(("M1", label, row))

        lo = max(u, j)
        hi = min(s, u+p)
        if lo+eps < t < hi-eps:
            row = make_row([
                (mu, "X", shifted(label, da=-1, dc=-1)),
                (mu, "S", shifted(label, dc=-1)),
                (-G, "X", label),
            ], r, u)
            if row:
                out.append(("M2", label, row))

        if u < j-eps and t > u+p+eps:
            row = make_row([
                (mu, "X", shifted(label, da=-1, dc=-1)),
                (-G, "X", label),
            ], r, u)
            if row:
                out.append(("M3", label, row))

    return out

def build(e, r):
    u = p + e
    seed = (0, 0, 0)
    nodes = set()
    for kind in ("X", "S"):
        if node_valid(kind, seed, r, u):
            nodes.add((kind, seed))

    queue = deque([seed])
    seen = set()
    rows = {}

    while queue:
        label = queue.popleft()
        if label in seen:
            continue
        seen.add(label)

        for row_type, row_label, row in exact_rows_at(label, r, u):
            key = (row_type, row_label)
            if key in rows:
                continue
            rows[key] = row
            for node in row:
                if node not in nodes:
                    nodes.add(node)
                    queue.append(node[1])

    columns = sorted(nodes, key=lambda z: (coord(z[1], r), z[0], z[1]))
    col_index = {col: idx for idx, col in enumerate(columns)}
    matrix = np.zeros((len(rows), len(columns)))

    for i, row in enumerate(rows.values()):
        for node, coeff in row.items():
            matrix[i, col_index[node]] = coeff

    return columns, rows, matrix

def null_projection_norms(matrix):
    if matrix.shape[1] == 0:
        return np.zeros(0)
    _, singular, vh = np.linalg.svd(matrix, full_matrices=True)
    rank = int((singular > 1e-9).sum())
    null = vh[rank:, :]
    if null.shape[0] == 0:
        return np.zeros(matrix.shape[1])
    return np.sqrt((null*null).sum(axis=0))

def witness():
    e = h/2
    r = h/10
    cols, rows, matrix = build(e, r)
    rank = np.linalg.matrix_rank(matrix, tol=1e-9)
    norms = null_projection_norms(matrix)
    root = [
        (cols[i][0], float(norms[i]))
        for i in range(len(cols))
        if cols[i][1] == (0,0,0)
    ]
    print("witness e=h/2 r=h/10")
    print("shape", matrix.shape, "rank", rank, "nullity", matrix.shape[1]-rank)
    print("root null-projection norms", root)

def sample_grid(ne=31, nr=25):
    patterns = {}
    emax = k+h
    for i in range(ne):
        e = 0.0005 + (emax-0.001)*i/(ne-1)
        for q in range(nr):
            r = (0.0003 + 0.9994*q/(nr-1))*h
            cols, rows, matrix = build(e, r)
            signature = (tuple(sorted(rows)), tuple(cols))
            if signature in patterns:
                continue
            rank = np.linalg.matrix_rank(matrix, tol=1e-9)
            norms = null_projection_norms(matrix)
            root_norms = [
                float(norms[ii])
                for ii, col in enumerate(cols)
                if col[1] == (0,0,0)
            ]
            patterns[signature] = (
                matrix.shape,
                rank,
                min(root_norms) if root_norms else float("nan"),
            )

    deficits = [shape[1]-rank for shape, rank, _ in patterns.values()]
    rootmins = [root for _, _, root in patterns.values()]
    print("sampled row-pattern types", len(patterns))
    print("deficiency range", min(deficits), max(deficits))
    print("minimum root null-projection norm", min(rootmins))

if __name__ == "__main__":
    witness()
    sample_grid()
