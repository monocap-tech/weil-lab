#!/usr/bin/env python3
"""NF370: SHA-pinned original NF369 4x4 dyadic *acceptance budget* only.
Does not evaluate the missing whole exterior Riesz residual or prove W-ODD-NEG.
"""
import argparse,hashlib,io,json,sys,zipfile
from fractions import Fraction as F
sys.set_int_max_str_digits(100000)
ZIP_SHA="1bacc7ae7967d1282eb28fd9d8566204eb21ba93246f6e81b174a18cc2ab1e96"
JSON_SHA="1b22cd77dd555749b8dcc41f92ddd91d982f2eca23ebf3a7638e512147b39d18"
N=4
MU0=F(49,50000)
TNUM=[[1048576,-83468,750212,-2271087],
      [0,1048576,-1546322,-1621433],
      [0,0,1048576,1115405],
      [0,0,0,1048576]]
D=[F(65,10**19),F(27,10**20),F(21,10**22),F(49,10**23)]
def dyad(p):
    n,e=map(int,p)
    return F(n<<e) if e>=0 else F(n,1<<(-e))
def mat(o,key):
    v=o[key]
    assert len(v)==N and all(len(row)==N for row in v)
    a=[[tuple(map(dyad,v[i][j])) for j in range(N)] for i in range(N)]
    assert all(r>=0 for row in a for m,r in row)
    return a
def lower_admissible(a,shift):
    lo=[[a[i][j][0]-a[i][j][1] for j in range(N)] for i in range(N)]
    hi=[[a[i][j][0]+a[i][j][1] for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            assert max(lo[i][j],lo[j][i])<=min(hi[i][j],hi[j][i])
    m=[[(a[i][j][0]+a[j][i][0])/2 for j in range(N)] for i in range(N)]
    err=[[max(abs(m[i][j]-lo[i][j]),abs(hi[i][j]-m[i][j]),
               abs(m[i][j]-lo[j][i]),abs(hi[j][i]-m[i][j]))
          for j in range(N)] for i in range(N)]
    rho=max(sum(row,F(0)) for row in err)
    return [[m[i][j]-(rho+shift)*int(i==j) for j in range(N)] for i in range(N)]
def ldlt(A):
    L=[[F(int(i==j)) for j in range(N)] for i in range(N)]
    piv=[]
    assert all(A[i][j]==A[j][i] for i in range(N) for j in range(N))
    for k in range(N):
        d=A[k][k]-sum((L[k][j]*L[k][j]*piv[j] for j in range(k)),F(0))
        assert d>0,("nonpositive exact pivot",k)
        piv.append(d)
        for i in range(k+1,N):
            L[i][k]=(A[i][k]-sum((L[i][j]*L[k][j]*piv[j] for j in range(k)),F(0)))/d
    return piv
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--offline",required=True)
    args=a.parse_args()
    b=open(args.offline,"rb").read()
    assert hashlib.sha256(b).hexdigest()==ZIP_SHA
    with zipfile.ZipFile(io.BytesIO(b)) as z:
        raw=z.read("nf369_actual_critical_quotient.json")
    assert hashlib.sha256(raw).hexdigest()==JSON_SHA
    o=json.loads(raw)
    assert o["selected_rank"]==242 and o["existing_critical_witness_count"]==4
    assert o["nf369_actual_full_complement_upper_computed"] is False
    p=mat(o,"nf369_selected_critical_Gram_native")
    d0=mat(o,"nf369_quotient_Galerkin_correction_lower_native")
    delta=F(o["nf369_quotient_response_remainder_upper"])
    assert delta>0
    S=[[(p[i][j][0]-d0[i][j][0],p[i][j][1]+d0[i][j][1])
        for j in range(N)] for i in range(N)]
    lower=lower_admissible(S,delta)
    ldlt(lower)
    T=[[F(v,2**20) for v in row] for row in TNUM]
    assert all(T[i][i]==1 for i in range(N))
    assert all(T[i][j]==0 for i in range(N) for j in range(i))
    tst=[[sum((T[k][i]*lower[k][m]*T[m][j]
               for k in range(N) for m in range(N)),F(0))
          for j in range(N)] for i in range(N)]
    margin=[[tst[i][j]-D[i]*int(i==j) for j in range(N)] for i in range(N)]
    piv=ldlt(margin)
    print("PASS NF370 original NF369 SHA-pinned 4x4 interval budget")
    print("PASS exact rational T^T(P4-D0)T > diag(d)")
    print("positive slack pivots (display only):",[float(x) for x in piv])
    print("dyadic T numerator:",TNUM)
    print("exact d:",[str(x) for x in D])
    print("conditional per-direction strong residual thresholds:",
          [(float(MU0*x/4))**0.5 for x in D])
    print("NO full exterior residual computed; W-ODD-NEG OPEN")
if __name__=="__main__":main()
