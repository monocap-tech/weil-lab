"""Exact RC3 covariance controls; no actual zeta rows are evaluated."""
from fractions import Fraction as F
import json

count = 0
def check(v):
    global count
    if not v:
        raise AssertionError(count+1)
    count += 1

# M=[[2,1],[1,2]] >= I, X=e0. Multiple output rows preserve mixed terms.
# Normalize the critical output metric by Dcrit=diag(scales_i**2).
for rows in [((1, 2), (3, -1)), ((2, 1), (1, 4)), ((-2, 3), (4, 5))]:
    for scales in [(F(1), F(1)), (F(1, 10), F(1, 100))]:
        j = [[F(x)/scales[i] for x in row] for i, row in enumerate(rows)]
        residual = [row[1]-row[0]/2 for row in j]
        exact, lower, error, upper = [], [], [], []
        for i in range(2):
            exact.append([]); lower.append([]); error.append([]); upper.append([])
            for z in range(2):
                e = (2*j[i][0]*j[z][0]-j[i][0]*j[z][1]
                     -j[i][1]*j[z][0]+2*j[i][1]*j[z][1])/3
                l = j[i][0]*j[z][0]/2
                r = F(2, 3)*residual[i]*residual[z]
                u = residual[i]*residual[z]
                exact[i].append(e); lower[i].append(l)
                error[i].append(r); upper[i].append(u)
                check(e == l+r)
        for matrix in [error, [[upper[i][z]-error[i][z] for z in range(2)] for i in range(2)]]:
            check(matrix[0][0] >= 0 and matrix[1][1] >= 0)
            check(matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0] >= 0)
        check(error[0][1] == error[1][0])

# Same P=I, N=(a,b) source object gives shell cost and physical Schur form.
b = F(4, 5)
for a in [F(1, 2), F(3, 5), F(7, 10)]:
    lam, defect = a*a, 1-a*a
    shell = b*b/defect
    # J=(0,-ab) annihilates the entire old span(e0).
    j = [F(0), -a*b]
    check(j[0] == 0)
    check(sum(x*x for x in j)/lam == b*b)
    q, source, c = defect, -a*b, 1-b*b
    k = c/2
    n, w = c*c/k-c, source*(c-k)
    h = w/n
    schur = q-source*source/c
    lower = q-source*source/k+(2*w*h-n*h*h)/(k*k)
    check(lower == schur)
    check(schur == defect*(1-shell)/c)
    check((shell < 1) == (schur > 0))
    check((shell == 1) == (schur == 0))
    check((shell > 1) == (schur < 0))

# A finite trial covariance of zero can conceal arbitrarily large
# defect-normalized leakage: M=I, J=(0,1), X=e0.
for d in [F(1), F(1, 10), F(1, 1000)]:
    finite_credit, true_covariance, residual_square = F(0), 1/d, 1/d
    check(true_covariance == finite_credit+residual_square)
    check(true_covariance >= 1)
print(json.dumps({'milestone':'RC3','status':'PASS',
 'exact_rational_checks':count,
 'scope':'mixed positive-inverse covariance and exact source-shell controls',
 'actual_zeta_covariance_evaluated':False,'RH':False,'F4':False,'Lean':False}, indent=2))
