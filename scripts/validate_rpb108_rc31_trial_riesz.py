"""Exact finite solves and conservative full canonical residual Gram bounds."""
from fractions import Fraction as F
import json
from pathlib import Path

def mm(A,B): return [[sum((x*y for x,y in zip(a,b)),F(0)) for b in zip(*B)] for a in A]
def tr(A): return list(map(list,zip(*A)))
def psd(A):
    A=[r[:] for r in A]; n=len(A)
    for k in range(n):
        if A[k][k]<0: return False
        if A[k][k]==0:
            if any(A[k][j]!=0 for j in range(k+1,n)): return False
            continue
        for i in range(k+1,n):
            for j in range(k+1,n): A[i][j]-=A[i][k]*A[k][j]/A[k][k]
    return True
def inverse(A):
    n=len(A); X=[a[:]+[F(i==j) for j in range(n)] for i,a in enumerate(A)]
    for k in range(n):
        assert X[k][k]!=0
        p=X[k][k]; X[k]=[v/p for v in X[k]]
        for i in range(n):
            if i!=k:
                p=X[i][k]; X[i]=[a-p*b for a,b in zip(X[i],X[k])]
    return [a[n:] for a in X]
def run(data):
    G=[[F(v) for v in r] for r in data['metric_center']]
    ds=list(map(F,data['physical_mass'])); n=len(ds)
    D=[[ds[i] if i==j else F(0) for j in range(n)] for i in range(n)]
    E=F(data['mass_metric_error_upper']); V=mm(inverse(G),D)
    assert mm(G,V)==D
    J=mm(D,V); H=mm(mm(tr(V),D),V)
    lower=[[J[i][j]-E*H[i][j] for j in range(n)] for i in range(n)]
    U=[[D[i][j]-lower[i][j] for j in range(n)] for i in range(n)]
    assert J==tr(J) and psd(lower) and psd(U)
    assert psd([[G[i][j]-(1-E)*D[i][j] for j in range(n)] for i in range(n)])
    # Find a rational collective full-residual bound in the physical input metric.
    beta=next(F(k,100) for k in range(1,101)
              if psd([[F(k,100)*D[i][j]-U[i][j] for j in range(n)] for i in range(n)]))
    out=dict(milestone='RC31',status='PASS',dimension=n,
             coefficients=[[str(x) for x in row] for row in V],
             full_response_lower=[[str(x) for x in row] for row in lower],
             full_residual_Gram_upper=[[str(x) for x in row] for row in U],
             collective_residual_squared_upper=str(beta),
             per_column_residual_squared_upper=[str(U[i][i]) for i in range(n)],
             per_column_residual_upper_display=[float(U[i][i])**0.5 for i in range(n)],
             full_response_upper='physical mass D',
             native_head_certified=False,aperture_extended=False,
             physical_residuals_evaluated=False)
    return out

if __name__=='__main__':
    import sys
    path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent.parent/'certificates/rpb108_rc30_interval_trial_metric.json'
    print(json.dumps(run(json.loads(path.read_text())),indent=2))
