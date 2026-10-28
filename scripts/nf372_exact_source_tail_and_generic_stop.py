#!/usr/bin/env python3
"""NF372: SHA-pinned exact-rational four-direction physical/spectral preflight.

No infinite Schur upper, actual matched correction Fourier bound, or RH sign.
Input: immutable PR355/ NF369 original GitHub Actions archives.
Usage:
  python nf372_exact_source_tail_and_generic_stop.py --pr355 PR355.zip --nf369 NF369.zip
"""
import argparse, hashlib, io, json, sys, zipfile
from fractions import Fraction as F
sys.set_int_max_str_digits(100000)
PR355_ZIP='f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
NF369_ZIP='1bacc7ae7967d1282eb28fd9d8566204eb21ba93246f6e81b174a18cc2ab1e96'
NF369_JSON='1b22cd77dd555749b8dcc41f92ddd91d982f2eca23ebf3a7638e512147b39d18'
MIXED_SHA='19356d4be60ee492896083c1bf6be18cd8ce2da058ff60008181f56a4c3ccc23'
B=F(11,10); LAMBDA=2**24; MU=F(49,50000)
TN=[[1048576,-83468,750212,-2271087],
    [0,1048576,-1546322,-1621433],
    [0,0,1048576,1115405],
    [0,0,0,1048576]]
# Established NF370 exact rational anisotropic dyadic budgets.
D=[F(65,10**19),F(27,10**20),F(21,10**22),F(49,10**23)]
CAP=[F(1,10**11),F(13,10**13),F(42,10**15),F(75,10**15)]
N=[4,6,6,3]
SECOND_LOW=[12,24,88,32]
A1CAP=[F(1,200000),F(1,2000000),F(1,10**7),F(1,10**7)]
A3CAP=[100,125,410,110]
BCAP=[F(1,10**9),F(1,4*10**9),F(1,25*10**9),F(1,50*10**9)]
RESERVE=[F(39,10**12),F(8,10**12),F(7,10**13),F(34,10**14)]

def dy(v):
    n,e=map(int,v)
    return F(n<<e) if e>=0 else F(n,1<<(-e))
def read(zpath,zip_sha,member,member_sha=None):
    data=open(zpath,'rb').read()
    assert hashlib.sha256(data).hexdigest()==zip_sha,(zpath,'bad archive SHA')
    with zipfile.ZipFile(io.BytesIO(data)) as z: raw=z.read(member)
    if member_sha: assert hashlib.sha256(raw).hexdigest()==member_sha,('bad member SHA',member)
    return json.loads(raw)
def max_i(M,i):
    return M[i]
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--pr355',required=True);p.add_argument('--nf369',required=True)
    p.add_argument('--report')
    a=p.parse_args()
    j=read(a.nf369,NF369_ZIP,'nf369_actual_critical_quotient.json',NF369_JSON)
    parent=read(a.pr355,PR355_ZIP,'original_exterior_refined_mixed.json',MIXED_SHA)
    assert j['input_sha256']['mixed']==MIXED_SHA
    assert j['selected_rank']==242 and j['existing_critical_witness_count']==4
    assert j['nf369_actual_full_complement_upper_computed'] is False
    assert parent['target_sine_frequencies']==[str(F(5*i,11)) for i in range(1,33)]
    P=parent['target_probes'];assert len(P)==4
    assert len(P[0]['sine_coefficients'])==32
    assert all(len(x['sine_coefficients'])==32 for x in P)
    T=[[F(x,2**20) for x in row] for row in TN]
    Y=[[dy(e) for e in row] for row in j['nf369_quotient_response_exact_dyadic_coefficients']]
    C=[[sum((F(int(k==l))+Y[k][l])*T[l][i] for l in range(4)) for i in range(4)] for k in range(4)]
    S=[[tuple(map(dy,j['physical_quotient_Gram_native'][k][l])) for l in range(4)] for k in range(4)]
    # Interval covariance upper: source native mid plus all interval-radius uncertainty.
    R=[[(F(0),F(0)) for k in range(4)] for l in range(4)]
    rows=[]
    for i in range(4):
        v=[C[k][i] for k in range(4)]
        m=sum((v[k]*S[k][l][0]*v[l] for k in range(4) for l in range(4)),F(0))
        err=sum((abs(v[k]*v[l])*S[k][l][1] for k in range(4) for l in range(4)),F(0))
        upper=m+err
        assert 0 < m-err and upper<CAP[i]*CAP[i],('physical matched exterior trial not bounded',i)
        # Raw original sine coefficients in NF370 transformed test direction.
        fs=[sum((F(P[k]['sine_coefficients'][l])*T[k][i] for k in range(4)),F(0)) for l in range(32)]
        sinh=sum((F(P[k]['sinh_coefficient'])*T[k][i] for k in range(4)),F(0))
        a1=sum(((-1)**(l+1)*(l+1)*v for l,v in enumerate(fs)),F(0))
        a3=sum((abs(v)*(l+1)**3 for l,v in enumerate(fs)),F(0))
        assert abs(a1)<A1CAP[i] and a3<A3CAP[i] and abs(sinh)<BCAP[i]
        # sin^3(n*pi*x/B) test: endpoint and first derivative vanish.
        # sine-sine orthogonality yields exact integral, including all 32 sources.
        n=N[i]
        v=3*fs[n-1] - (9*fs[3*n-1] if 3*n<=32 else 0)
        # pi^2>9; exact rational lower on original f_s'' pairing.
        sine_pairing_lower=F(9*n*n,8*B)*abs(v)
        assert sine_pairing_lower>SECOND_LOW[i]+F(1,10**6)
        # |int(w*phi'')|<3*k^2*||w||_L1(0,B)<(3*(3n)^2)*CAP
        # since k=n*pi/B <3*n for pi<22/7 and B=11/10.
        # Pole second derivative costs |sinh|/2*(cosh(B/2)-1)<|sinh|/2.
        err_weak=3*(3*n)**2*CAP[i]+abs(sinh)/2
        assert sine_pairing_lower-err_weak>SECOND_LOW[i]
        # At lambda=2^24, bounds use pi>3, pi^2<10, 17<17+logLambda<34.
        # J2 < 1/80^2; J4 < 1/10^18 and >4/10^20; J8 < 1/10^46.
        J2upper=F(2*(34**2+2*34+2),LAMBDA)
        J4upper=F(2,LAMBDA**3)*(F(34**2,3)+F(2*34,9)+F(2,27))
        J4lower=F(2,LAMBDA**3)*F(17**2,3)
        J8upper=F(2,LAMBDA**7)*(F(34**2,7)+F(2*34,49)+F(2,343))
        assert J2upper<F(1,80**2)
        assert J4upper<F(1,10**18) and J4lower>F(4,10**20)
        assert J8upper<F(1,10**46)
        eta=F(32,2*B*LAMBDA)**2;assert eta<F(1,2)
        # |Fhat_s| <= (1/(2*pi*B))*(|A1|/xi^2 + A3/(4*B^2*(1-eta)*xi^4));
        # 1/(2*pi*B)<1, 1/(4*B^2*(1-eta))<1.
        sine_tail_cap=A1CAP[i]*F(1,10**9)+A3CAP[i]*F(1,10**23)
        # sinh endpoint-jet: alpha < |b|/5, beta < |b|/12.
        sinh_tail_cap=BCAP[i]/400+BCAP[i]/(12*10**9)
        source_tail_cap=sine_tail_cap+sinh_tail_cap
        assert source_tail_cap<RESERVE[i]/4
        assert RESERVE[i]**2<MU*D[i]/4
        # Generic beta*sqrt(J4) > SECOND_LOW*1e-11, must exceed total residual ceiling.
        # Compare to NF370 exact individual budget, not to a rounded display.
        assert (F(SECOND_LOW[i],10**11))**2 > MU*D[i]/4
        rows.append(dict(direction=i+1,weak_sine_test=n,
          physical_matched_correction_norm_strict_upper=str(CAP[i]),
          exact_test_coefficient_3an_minus_9a3n=str(v),
          weak_second_derivative_L1_strict_lower=SECOND_LOW[i],
          signed_first_Fourier_endpoint_moment=str(a1),
          sine_absolute_cubic_moment_strict_upper=str(A3CAP[i]),
          original_sinh_coefficient=str(sinh),
          complete_raw_source_log_tail_strict_upper=str(source_tail_cap),
          conservative_residual_individual_strict_floor=str(RESERVE[i]),
          raw_source_tail_uses_less_than_one_quarter_of_residual_budget=True,
          generic_second_jet_tail_lower_exceeds_individual_budget=True))
    report=dict(scope='Original NF370 four fixed directions; original NF369 physical quotient; PR355 32-sine sources',
                provenance=dict(pr355_zip_sha256=PR355_ZIP,nf369_zip_sha256=NF369_ZIP,nf369_json_sha256=NF369_JSON,mixed_json_sha256=MIXED_SHA),
                standing='EXACT_RATIONAL_ARCHIVE_REPLAY_ANALYTIC_METHOD_STOP',
                cutoff=LAMBDA,selected_rank=242,directions=rows,
                genuine_matched_correction_tail_upper_computed=False,
                complete_original_lowband_computed=False,
                whole_exterior_schur_upper_computed=False,
                original_operator_domain_global_audit='OPEN',W_ODD_NEG='OPEN',RH='OPEN',github_transfer='NOT PERFORMED')
    print('PASS NF372 SHA-pinned original archive, original 32-sine sources, fixed Y0/T')
    for v in rows:
        print('direction',v['direction'],'||E(I+Y0)t|| <',v['physical_matched_correction_norm_strict_upper'],
              'integral |u_second| >',v['weak_second_derivative_L1_strict_lower'],
              'raw source log-tail <',v['complete_raw_source_log_tail_strict_upper'])
    print('PASS four fixed-cutoff generic two-IBP C2-tail method STOP; exact oscillatory sine source tails small')
    print('NO matched correction tail, lowband, whole-infinite Schur, original-domain, or RH promotion')
    if a.report:
        with open(a.report,'w') as f:json.dump(report,f,indent=2);f.write('\n')
    return report
if __name__=='__main__':
    main()
