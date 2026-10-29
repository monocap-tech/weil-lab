#!/usr/bin/env python3
"""NF375 source-matched original signed-tail low-band ENTRY gate.

Certifies cheaper dyadic cutoffs and explicit residual budgets using original
PR355 critical sources, certified NF374 4096-bit Arb endpoint/derivative/curvature
caps, and inherited entire signed m bound. This does NOT measure low-band.
"""
import argparse, hashlib, json, re
from decimal import Decimal
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

SRC_SHA='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
NATIVE_SHA='a725a6da6bf29ce21b1955df8f4d0b35b87ff8f003d09cdff13581d1b82f7559'
CAP_K=(F(23,10**5),F(14,10**6),F(27,10**7),F(21,10**7))
CAP_A=(F(81,10**12),F(44,10**13),F(102,10**14),F(78,10**14))
CAP_D=(F(224,10**8),F(13,10**8),F(27,10**9),F(21,10**9))
MU=F(49,50000)
D=(F(65,10**19),F(27,10**20),F(21,10**22),F(49,10**23))
T=[[F(v,2**20) for v in row] for row in [[1048576,-83468,750212,-2271087],[0,1048576,-1546322,-1621433],[0,0,1048576,1115405],[0,0,0,1048576]]]
CONFIG={
 20:(F(28,10**12),F(57,10**13),F(34,10**14),F(15,10**14)),
 21:(F(32,10**12),F(65,10**13),F(46,10**14),F(20,10**14)),
 22:(F(34,10**12),F(70,10**13),F(53,10**14),F(25,10**14)),
 23:(F(36,10**12),F(73,10**13),F(58,10**14),F(27,10**14)),
 24:(F(36,10**12),F(73,10**13),F(59,10**14),F(28,10**14)),
}
BALL=re.compile(r'^\[([^ ]+) \+/- ([^\]]+)\]$')

def file_sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def upward(s):
    z=BALL.fullmatch(str(s));
    if z:
        m,r=map(lambda t:F(Decimal(t)),z.groups())
        assert r>=0
        return m+r
    return F(Decimal(str(s)))

def sqrt_up(q):
    assert q>=0
    S=10**44
    n=q.numerator*S*S//q.denominator
    return F(isqrt(n)+1,S)

def calc(k,a1,a3,b,A,d,K):
    assert k>=16
    lam=2**k
    rho=F(32,2*F(11,10)*lam)**2
    assert rho<F(1,2)
    # Exact upper: log(2)<7/10; hence 17+log(2^k)< L.
    L=F(17)+F(7*k,10)
    j2=F(2,lam)*(L*L+2*L+2)
    j4=F(2,lam**3)*(L*L/3+2*L/9+F(2,27))
    j8=F(2,lam**7)*(L*L/7+2*L/49+F(2,343))
    u2,u4,u8=map(sqrt_up,(j2,j4,j8))
    # Original 32 sine grid Fourier transform: 1/(2*pi*B) <1/6;
    # cubic remainder coefficient 1/(4*B^2*(1-rho))<1.
    sine=abs(a1)*u4/6+a3*u8/6
    # Supported sinh: alpha<|b|/5, beta<|b|/12.
    sinh=abs(b)*u2/5+abs(b)*u4/12
    # Matched original QF correction: NF374 Arb endpoint + K curvature.
    correction=A*u2/3+(d+K)*u4/18
    return sine+sinh+correction,(sine,sinh,correction),(u2,u4,u8)

def run(source_path,native_path,output=None):
    assert file_sha(source_path)==SRC_SHA
    assert file_sha(native_path)==NATIVE_SHA
    src=json.loads(Path(source_path).read_text())
    nat=json.loads(Path(native_path).read_text())
    assert src['custody']['parent_original_json_sha256']=='19356d4be60ee492896083c1bf6be18cd8ce2da058ff60008181f56a4c3ccc23'
    assert nat['native_parent_physical_quotient_overlap_pass'] is True
    assert nat['working_precision_bits']==4096
    assert nat['selected_source_count']==242 and nat['critical_source_count']==4
    assert nat['full_exterior_residual_certified'] is False
    p=src['data']['target_probes'];freq=src['data']['target_sine_frequencies']
    assert len(p)==4 and [F(s) for s in freq]==[F(5*i,11) for i in range(1,33)]
    rows=[]
    for i in range(4):
        cur=nat['nf374_curvature'][i];jet=nat['boundary_jets'][i]
        assert cur['direction']==jet['direction']==i+1
        assert upward(jet['w_endpoint_abs_upper'])<CAP_A[i]
        assert upward(jet['w_derivative_abs_upper'])<CAP_D[i]
        assert upward(cur['K_integral_abs_upper'])<CAP_K[i]
        fs=[sum((F(p[t]['sine_coefficients'][n])*T[t][i] for t in range(4)),F(0)) for n in range(32)]
        a1=sum(((-1)**(n+1)*(n+1)*fs[n] for n in range(32)),F(0))
        a3=sum((abs(fs[n])*(n+1)**3 for n in range(32)),F(0))
        b=sum((F(p[t]['sinh_coefficient'])*T[t][i] for t in range(4)),F(0))
        budget=MU*D[i]/4
        opts=[]
        for k,targets in CONFIG.items():
            target=targets[i]
            tail,parts,j=calc(k,a1,a3,b,CAP_A[i],CAP_D[i],CAP_K[i])
            accept=bool((tail+target)**2 < budget)
            opts.append(dict(log2_cutoff=k,cutoff=2**k,highband_upper=str(tail),
                             highband_source_sine_upper=str(parts[0]),
                             highband_source_sinh_upper=str(parts[1]),
                             highband_matched_exterior_upper=str(parts[2]),
                             chosen_future_lowband_target=str(target),
                             exact_squared_original_individual_gate=accept))
            assert accept, ('new NF375 directional reduced-cutoff gate fails',i+1,k)
        rows.append(dict(direction=i+1,signed_original_first_sine_moment=str(a1),
                         original_sine_absolute_cubic_moment=str(a3),
                         original_sinh_coefficient=str(b),
                         original_residual_squared_budget=str(budget),
                         dyadic_cutoff_options=opts))
    report=dict(standing='CERTIFIED ORIGINAL MATCHED HIGHBAND CUTOFF-REDUCTION AND LOWBAND ENTRY ONLY',
                scope='SAME original J242/four sources/NF369 Y0/NF370 T; no lowband computation',
                source_sha256=SRC_SHA,native_report_sha256=NATIVE_SHA,
                inherited_multiplier_bound='|m(xi)|<=17+log|xi| for |xi|>=1',
                analytic_tail_identity='Jq=2 int_Lambda^infty (17+log xi)^2 / xi^q dxi, q=2,4,8',
                analytic_log_inequality='log2<7/10, pi>3',
                accepted_cutoffs=[2**k for k in CONFIG],
                result='Original high-band sufficient tests permit as low as 2^20 with reallocated four lower low-band norm targets; 2^24 preserves earlier NF374 targets while 2^23 nearly preserves them',
                directions=rows,measured_original_lowband=False,
                original_whole_residual_certified=False,
                other_238_directions='OPEN',original_operator_domain_audit='OPEN',W_ODD_NEG='OPEN',RH='OPEN')
    if output:Path(output).write_text(json.dumps(report,indent=2)+'\n')
    for k in CONFIG:
        print('NF375 certified cutoff 2^%d, 4 directions, low-band H targets:'%k,[str(t) for t in CONFIG[k]])
    print('PASS original high-band repaid at smaller cutoffs. Actual LOWBAND NOT evaluated.')
    return report

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True)
    ap.add_argument('--native',required=True);ap.add_argument('--output');args=ap.parse_args()
    run(args.source,args.native,args.output)