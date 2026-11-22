#!/usr/bin/env python3
"""Exact-rational CP001 true h=1/2000 shift witness; NOT LEAN."""
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path

def exp_bounds(x, N=36):
    if x == 0: return F(1), F(1)
    assert 0 < x < N+2
    q=sum((x**k/factorial(k) for k in range(N+1)),F(0))
    return q, q+(x**(N+1)/factorial(N+1))/(1-x/F(N+2))

def witness(n,x,gt):
    lo,hi=exp_bounds(x)
    gap=(lo-n) if gt else (n-hi)
    assert gap>0,(n,x,gt)
    return {'n':n,'x':str(x),'exp_greater_than_n':gt,'positive_rational_gap':str(gap)}

def hit(n,lo,hi):
    if exp_bounds(lo)[0]>n or exp_bounds(hi)[1]<n:return False
    assert exp_bounds(lo)[1]<n and exp_bounds(hi)[0]>n,(n,lo,hi)
    return True

def classify(q,r,shift=F(0)):
    c=F(1099,1000);h=F(1,2000)
    cells=[('left',-c,h),('center',q,r),('right',c+shift,h)]
    hits=[];rows=[]
    for i,(name,x,rad) in enumerate(cells):
        for other,y,yr in cells[i:]:
            lo=max(F(0),abs(x-y)-rad-yr)
            hi=abs(x-y)+rad+yr
            assert hi<=F(5,2)
            ns=[n for n in range(2,13) if hit(n,lo,hi)]
            rows.append({'pair':[name,other],'closed_distance_range':[str(lo),str(hi)],'integer_shifts':ns})
            hits += [(name,other,n) for n in ns]
    assert exp_bounds(F(5,2))[1]<13
    return hits,rows

def main():
    h=F(1,2000);c=F(1099,1000);q=F(1,5)
    assert h!=F(1,1000)
    logs=[(2,F(1,250),False),(2,F(112,125),True),
          (3,F(451,500),False),(3,F(162,125),True),
          (4,F(651,500),False),(8,F(549,250),True),
          (9,F(109861,50000),False),(9,F(219723,100000),True),
          (10,F(11,5),False),(13,F(5,2),False),
          (3,F(1),False),(11,F(441,184),False)]
    certs=[witness(*x) for x in logs]
    d0=2*c-F(219723,100000)
    d1=2*c-F(109861,50000)
    assert (d0,d1)==(F(77,100000),F(78,100000))
    assert d1/(2*h)+F(3,50)==F(21,25)
    assert 1-1/(1-F(21,25)**2)==-F(441,184)
    length=2*(F(3,50)*h)
    I=length/F(121)
    assert I==F(3,6050000)
    kI=I/3; norm=kI/(2*h)
    assert (kI,norm)==(F(1,6050000),F(1,6050))
    radius_records={}
    for r in [F(1,1000),F(1,500)]:
        active,rows=classify(q,r)
        assert active==[('left','right',9)]
        assert -F(11,10)<-c-h<-c+h<-F(549,500)
        assert F(549,500)<c-h<c+h<F(11,10)
        assert -c+h<q-r<q+r<c-h
        radius_records[str(r)]={'active_prime_shifts':[list(x) for x in active],'rows':rows}
    collide,_=classify(F(0),F(1,500))
    assert ('left','center',3) in collide and ('center','right',3) in collide
    wide,_=classify(q,F(1,10))
    assert ('left','center',4) in wide
    moved,_=classify(q,F(1,500),F(1,20))
    assert ('left','right',9) not in moved
    wrong_endpoint=-c-F(1,1000)
    assert wrong_endpoint==-F(11,10) and not (-F(11,10)<wrong_endpoint)
    return {'schema':'CP-C1E-TRUE-FROZEN-CP001-rational-v2',
            'status':'PASS EXACT RATIONAL; NOT LEAN',
            'profile':'exp(1-1/(1-u^2)) for abs(u)<1, else zero',
            'old_radius':'1/2000','old_centers':['-1099/1000','1099/1000'],
            'new_center':'1/5','new_radii':['1/1000','1/500'],
            'taylor_N':36,'log_exp_comparisons':certs,
            'delta_bounds':{'strict_lower':str(d0),'strict_upper':str(d1)},
            'profile_subinterval':'abs(x+log9/2)<3h/50; abs(u)<21/25; profile(u)>1/11',
            'lower_bounds':{'I9':str(I),'kappa_times_I9':str(kI),
                            'twice_kappa_times_I9':str(2*kI),
                            'mass_normalized_prime_offdiagonal':str(norm)},
            'by_radius':radius_records,
            'mutation_controls':{'center_zero_creates_n3':True,
                 'new_radius_1over10_creates_n4':True,
                 'right_center_shift_removes_n9':True,
                 'wrong_old_radius_reaches_strict_collar_endpoint':True},
            'Lean_kernel_pass':False,'independent_spectral_comparison':False,
            'full_Weil_positive':False,'RH':False}

if __name__=='__main__':
    ans=main()
    Path('cpc1e-frozen-cp001-prime-geometry.json').write_text(json.dumps(ans,indent=2,sort_keys=True)+'\n')
    print('CP-C1(E) true frozen old h=1/2000, only n9, strict I9>3/6050000, 4 mutation controls: PASS EXACT RATIONAL NOT LEAN')
