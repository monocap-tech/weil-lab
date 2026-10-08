#!/usr/bin/env python3
"""RPB108 IP2: exact rational finite controls only; not a zeta/Lean certificate."""
from fractions import Fraction as F


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def dot(u, v):
    return sum(u[i] * v[i] for i in range(len(u)))


checks = 0

# A perfectly localized positive metric does not control signed leakage.
a, b = F(3, 4), F(3, 4)
delta = 1 - a * a
cost = b * b / delta
q = [[delta, -a*b], [-a*b, 1-b*b]]
assert delta == F(7, 16); checks += 1
assert cost == F(9, 7) and cost > 1; checks += 1
assert q[0][0]*q[1][1] - q[0][1]*q[1][0] == F(-1, 8); checks += 1
assert (q[0][0]+q[0][1]) == F(-1, 8); checks += 1

# Off-diagonal coupling in the full inverse via a third packet.
m = [[F(1), F(0), F(1,2)],
     [F(0), F(1), F(1,2)],
     [F(1,2), F(1,2), F(1)]]
mi = [[F(3,2), F(1,2), -F(1)],
      [F(1,2), F(3,2), -F(1)],
      [-F(1), -F(1), F(2)]]
assert mm(m, mi) == [[F(int(i==j)) for j in range(3)] for i in range(3)]; checks += 1
assert m[0][1] == 0 and mi[0][1] == F(1,2); checks += 1

# Operator-valued variance on span(e1,e2): rank-one covariance.
m2 = mm(m, m)
assert [[m2[i][j]-sum(m[i][k]*m[k][j] for k in range(2))
         for j in range(2)] for i in range(2)] == [[F(1,4)]*2 for _ in range(2)]; checks += 1

# Exact residual identity, including the entire omitted direction.
j, z = [F(1), F(2), F(1)], [F(1), F(0), F(0)]
e = [j[i]-mv(m,z)[i] for i in range(3)]
lhs = dot(j, mv(mi,j))
rhs = 2*dot(j,z)-dot(z,mv(m,z))+dot(e,mv(mi,e))
assert lhs == rhs; checks += 1
# M >= (1-1/sqrt(2))I >= (1/4)I, so conservative inverse bound 4 works.
upper = 2*dot(j,z)-dot(z,mv(m,z))+F(4)*dot(e,e)
assert lhs <= upper; checks += 1

# 2x2 packet Schur inverse bound with a rational positive lower m0.
mr = [[F(2), F(1,10)],[F(1,10),F(2)]]
actual = F(2)/(F(4)-F(1,100))
m0 = F(19,10)
packet_upper = 1/(F(2)-F(1,100)/m0)
assert actual <= packet_upper; checks += 1
print(f"RPB108 IP2: {checks} exact rational controls passed")
