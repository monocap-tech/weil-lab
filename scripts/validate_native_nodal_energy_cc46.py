"""Exact nodal-balance controls; no actual native null evaluation."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def run():
    n=0
    def check(x):
        nonlocal n
        assert x
        n+=1
    r0=8+2*F(12093,3740)
    check(r0==F(27053,1870)<15)
    for r in (F(1,20),F(1,10),F(1,5)):
        A=1+r; C=F(1,6)
        H=[[ -C,-C],[-C,-C]]
        Q=[[H[i][j]+2*A*A for j in range(2)] for i in range(2)]
        check(H[0][0]==H[0][1]==H[1][1]==-C)
        check(H[0][0]+H[1][1]-2*H[0][1]==0)
        check(Q[0][0]==Q[0][1]==Q[1][1]==2*A*A-C>0)
        check(Q[0][0]*Q[1][1]-Q[0][1]**2==0)
        check(C<=2*A*A)
        for mu in (F(1,3),F(2)):
            shifted=[[H[i][j]-(mu if i==j else 0) for j in range(2)] for i in range(2)]
            check(shifted[0][0]+shifted[1][1]-2*shifted[0][1]==-2*mu)
            check(r0+mu>r0)
    for m in (F(1,10),F(1,2),F(3,4)):
        R=1/(4*m)
        check(2*R*m==F(1,2))
        for L in (F(2),F(3),F(7)):
            check(1+(1-2*R*m)*(L-1)==(1+L)/2)
    return dict(stage='CC46 nodal energy balance',all_passed=True,new_exact_checks=n,
                actual_null_vectors_evaluated=False,arithmetic_floor_certified=False,
                RH_proved=False,lean_certified=False,
                constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_NODAL_ENERGY_CC46_VALIDATION_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
