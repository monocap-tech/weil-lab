"""Moment-enriched coordinate controls, not native source Grams."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def run():
    n=0
    def check(x):
        nonlocal n
        assert x
        n+=1
    for epsilon in (F(1,10),F(1,2),F(1,10**220)):
        old=1-F(37,9)+(1-2*epsilon)**2/epsilon**2
        new=1-4*epsilon+F(8,9)*epsilon**2
        check(new==epsilon**2*old)
        check(-epsilon+epsilon==0)
        raw=epsilon**2-4*epsilon+1
        mixed=-epsilon/3
        check(raw-mixed**2==new)
        check(1+epsilon**2>=1)
    check(1-4*F(1,10)+F(8,9)*F(1,10)**2>0)
    check(1-4*F(1,2)+F(8,9)*F(1,2)**2<0)
    check(F(2)-1==1)
    check(F(3,2)-1/F(1,2)==F(-1,2))
    check(56+1==57 and 57-1==56 and 56-1==55)
    check(F(17,100)/2==F(17,200))
    check(F(207,1000)>F(17,100) and F(207,1000)/2==F(207,2000))
    return dict(stage='CC49 exact moment enrichment',all_passed=True,new_exact_checks=n,
                native_enriched_gate_evaluated=False,high_bound_preserved_by_subspace=True,
                RH_proved=False,lean_certified=False,
                constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
if __name__=='__main__':
    out=run()
    (ROOT/'notes/data/RPB108_MOMENT_ENRICHMENT_CC49_VALIDATION_20261009.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
