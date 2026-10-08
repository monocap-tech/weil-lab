"""Supported operator-domain controls, not actual Weil null data."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def run():
    count=0
    def check(v):
        nonlocal count
        assert v
        count+=1
    n=[F(3,5),F(8,5)];h=[F(3,5),F(2,5)];A=[F(1),F(4)]
    dot=lambda x,y:sum((a*b for a,b in zip(x,y)),F(0))
    norm=lambda x:dot(x,x)
    Ah=[A[i]*h[i] for i in range(2)];r=norm(n);mass=norm(h)
    check(dot(n,h)==1)
    check(Ah==n)
    check(dot(h,Ah)==1)
    check(r==F(73,25))
    check(mass==F(13,25))
    check(norm(Ah)<=r*r*mass)
    # Q=[[16,-24],[-24,36]]/25 is a positive rank-one matrix.
    check((1-n[0]**2)*(4-n[1]**2)-(n[0]*n[1])**2==0)
    check(1-n[0]**2>0 and 4-n[1]**2>0)
    for cutoff in (F(1),F(2),F(4)):
        tail=[h[i] if A[i]>cutoff else F(0) for i in range(2)]
        check(sum((A[i]*tail[i]**2 for i in range(2)),F(0))<=r*r*mass/cutoff)
        check(norm(tail)<=r*r*mass/(cutoff*cutoff))
    pos=[F(2),F(-3)];mu=F(52,25)
    Qpos=[A[i]*pos[i]-n[i]*dot(n,pos) for i in range(2)]
    check(Qpos==[mu*x for x in pos])
    check(dot(pos,Qpos)==mu*norm(pos)>0)
    assert count==16
    return {'stage':'CC41 supported logarithmic localization','all_passed':True,
            'new_exact_checks':count,'inherited_checks_replayed':False,
            'actual_zeta_null_evaluated':False,'null_exclusion_proved':False,
            'unrestricted_multiplier_domain_claimed':False,'RH_proved':False,
            'lean_certified':False,'constructor_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_DIRICHLET_LOG_LOCALIZATION_CC41_VALIDATION_20261008.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
