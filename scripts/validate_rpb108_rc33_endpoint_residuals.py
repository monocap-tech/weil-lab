"""Exact endpoint log coefficients and physical residual endpoint-tail budgets."""
from fractions import Fraction as F
import json,sys
from pathlib import Path

def run(path):
    data=json.loads(Path(path).read_text())
    V=[[F(x) for x in row] for row in data['coefficients']]
    B=F(11,10); R=2*B; delta=R/2**60
    clower=-F(3203794213,10**9)
    M=1+1/(2*R)-clower
    rows=[]
    for j in range(8):
        a=[V[i][j] for i in range(8)]
        b=sum(a,F(0)); minus=sum(((-1)**i*a[i] for i in range(8)),F(0))
        assert b!=0 and minus==(-1)**j*b
        amp=sum(map(abs,a),F(0))
        lip=sum((F(i*(i+1),2)*abs(a[i])/B for i in range(8)),F(0))
        singular=sum((sum((F(1,k) for k in range(1,i+1)),F(0))*abs(a[i])
                      for i in range(8)),F(0))
        G=1+singular+(-clower+M)*amp+lip*R/2+abs(b)/2
        # log(R/delta)=60 log2<60; both endpoints have same magnitudes.
        tail=2*delta*(b*b/F(4)*(60**2+2*60+2)+abs(b)*G*61+G*G)
        assert tail<F(1,10**12)
        rows.append(dict(column=j,right_trace=str(b),left_trace=str(minus),
            right_log_coefficient=str(-b/2),bounded_remainder_upper=str(G),
            both_endpoint_physical_squared_upper=str(tail)))
    return dict(milestone='RC33',status='PASS',delta=str(delta),columns=rows,
        all_both_endpoint_squared_bounds_below='1/10^12',
        actual_endpoint_log_coefficients=True,interior_residual_certified=False,
        whole_physical_residual_certified=False,aperture_extended=False)

if __name__=='__main__':
    path=sys.argv[1] if len(sys.argv)>1 else Path(__file__).parent.parent/'certificates/rpb108_rc31_trial_riesz.json'
    print(json.dumps(run(path),indent=2))
