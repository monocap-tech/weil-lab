#!/usr/bin/env python3
"""CP001 exact Fraction preflight; NOT a Lean kernel or source-bound axiom audit."""
from fractions import Fraction as F


def log_bounds(n: int, terms: int = 48):
    """Rational atanh enclosure for log(n), n>=2; no floating-point log."""
    assert n >= 2
    x = F(n-1, n+1)
    lower = sum((2*x**(2*k+1)/F(2*k+1)) for k in range(terms))
    tail = 2*x**(2*terms+1)/(F(2*terms+1)*(1-x*x))
    return lower, lower+tail


def sub_interval(a,b):
    return a[0]-b[1], a[1]-b[0]


def minus_interval(a):
    return -a[1], -a[0]


def disjoint(a,b):
    return a[1] < b[0] or b[1] < a[0]


def main():
    old_l = (F(-11,10), F(-11,10)+F(1,500))
    old_r = (F(11,10)-F(1,500), F(11,10))
    old = [old_l,old_r]
    for r, expected in [(F(1,1000), F(1,4)), (F(1,500), F(1,10))]:
        new = (F(1,5)-r,F(1,5)+r)
        support_length = F(1,250)+2*r
        assert support_length==({F(1,1000):F(3,500),F(1,500):F(1,125)}[r])
        margin = F(7,10)-75*support_length
        assert margin==expected
        assert disjoint(new,old_l) and disjoint(new,old_r)
        for n in range(2,10):
            logpos=log_bounds(n)
            assert logpos[0]>0
            for e in old:
                for a,b in [(e,new),(new,e),(new,new)]:
                    differences=sub_interval(a,b)
                    assert disjoint(differences,logpos), (r,n,a,b,'positive')
                    assert disjoint(differences,minus_interval(logpos)), (r,n,a,b,'negative')
        print(f'r={r}: support measure={support_length}; margin={margin}; all old-new/new-self active n=2..9 signed gaps EXCLUDED')
    assert (F(2,5)-150*F(1,375))==0
    log9=log_bounds(9)
    old_cross = sub_interval(old_r,old_l)
    assert old_cross[0]<log9[0]<log9[1]<old_cross[1]
    assert F(1)-F(4,5)**2==F(9,25)>0
    assert F(1)-2*F(4,5)==-F(3,5)<0
    print('old-old n=9 overlap RETAINED (rigorously enclosed); pairwise-PSD 3x3 counterexample VERIFIED')
    print('PASS — exact Fraction preflight only, not Lean compilation or Weil-form certification')


if __name__=='__main__':
    main()
