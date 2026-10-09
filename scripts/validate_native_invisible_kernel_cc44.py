"""Exact sign/susceptibility controls; not actual Weil eigenvectors."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mv(A,x): return [dot(row,x) for row in A]
def determinant(A):
    if len(A)==1: return A[0][0]
    return sum((-1)**j*A[0][j]*determinant([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A)))
def run():
    count=0
    def check(x):
        nonlocal count
        assert x
        count+=1
    g,z,w=[F(1)]*3,[F(1),F(-1),F(0)],[F(1),F(1),F(-2)]
    H=[[-g[i]*g[j]/3+w[i]*w[j]/6 for j in range(3)] for i in range(3)]
    for r in (F(1,20),F(1,10),F(1,5)):
        c=[g[i]+r*w[i] for i in range(3)]
        Q=[[H[i][j]+2*c[i]*c[j] for j in range(3)] for i in range(3)]
        check(all(H[i][j]<0 for i in range(3) for j in range(i)))
        check(all(x>0 for x in c))
        check(mv(H,g)==[-x for x in g])
        check(mv(H,z)==[0]*3)
        check(mv(H,w)==w)
        check(dot(c,z)==0 and mv(Q,z)==[0]*3)
        check(0<12*r*r/5<1)
        for mask in range(1,8):
            ix=[i for i in range(3) if mask & (1<<i)]
            check(determinant([[Q[i][j] for j in ix] for i in ix])>=0)
        for a,b,e in ((F(1),F(2),F(3)),(F(-2),F(1),F(4)),(F(0),F(3),F(-1))):
            x=[a*g[i]+b*w[i]+e*z[i] for i in range(3)]
            # Physical normalized ground coordinate is sqrt(3)*a;
            # write the square without introducing an irrational coordinate.
            rhs=15*(a+12*r*b/5)**2+6*b*b-F(72,5)*r*r*b*b
            check(dot(x,mv(Q,x))==rhs)
        check(dot(w,mv(H,w))-dot(w,w)==0)
        check(dot(c,w)==6*r and dot(w,mv(Q,w))-dot(w,w)==72*r*r>0)
    return dict(stage='CC44 invisible kernel',all_passed=True,new_exact_checks=count,
                actual_zeta_eigenvectors_evaluated=False,arithmetic_floor_certified=False,
                RH_proved=False,lean_certified=False,
                constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_INVISIBLE_KERNEL_CC44_VALIDATION_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
