#!/usr/bin/env python3
"""Synthetic exact equivalence tests for NF623 (not original solve evidence)."""
from fractions import Fraction as F
from random import Random
from verify_nf623_uniform_physical_payments import exact_gates, products, transpose, cached_products

def mm(x,y):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*y)] for row in x]

def main():
    rng=Random(623)
    for _ in range(50):
        n=4
        D=[[rng.randint(-5,5) for j in range(n)] for i in range(n)]
        H=[[rng.randint(-9,9) for j in range(n)] for i in range(n)]
        V=[[rng.randint(-9,9) for j in range(2)] for i in range(n)]
        w=[2,-3]; y=[1,-3,4,0]; S,T,U,Q0=8,4,16,100
        eH,eV=F(3,100),F(1,100)
        mid=[F(0)]*n; rad=[F(1)]*n
        defects,residuals,r,pay=exact_gates(D,S,H,V,w,T,y,U,eH,eV,mid,rad,mm,Q0)
        A,b,Ay,Dy=products(D,H,V,w,y,mm)
        cache=cached_products(D,H,V,w,y,mm)
        assert (cache['A'],cache['b'],cache['Ay'],cache['Dy'])==(A,b,Ay,Dy)
        assert exact_gates(D,S,H,V,w,T,y,U,eH,eV,mid,rad,mm,Q0,cache=cache)==(defects,residuals,r,pay)
        DA=[[abs(v) for v in row] for row in D]
        EA=mm(mm(transpose(DA),[[1]*n for _ in range(n)]),DA)
        for i in range(n):
            directD=sum(abs(F(int(i==j))-F(A[i][j],Q0*S*S))+eH*F(EA[i][j],S*S) for j in range(n))
            directR=abs(F(b[i],Q0*S*T)-F(Ay[i],Q0*S*S*U))+eV*sum(F(abs(D[k][i]*x),S*T) for k in range(n) for x in w)+eH*sum(F(EA[i][j]*abs(y[j]),S*S*U) for j in range(n))
            assert defects[i]==directD and residuals[i]==directR
            assert pay[i]==abs(F(Dy[i],S*U))+2*r*sum(F(abs(x),S) for x in D[i])
    print('50 exact synthetic equivalence tests PASS; 200 rows and both center-product associations matched')
if __name__=='__main__': main()
