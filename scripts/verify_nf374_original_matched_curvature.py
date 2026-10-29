#!/usr/bin/env python3
"""NF374: actual matched exterior curvature via full original second-derivative Gram.

Exact parent source definitions, true physical Gram via Arb interval integrals.
This checks a finite-source boundary interface, not whole-frequency residual or RH.
"""
import argparse
import hashlib
import json
import time
from fractions import Fraction as F
from pathlib import Path

import flint
from flint import arb, arb_mat, ctx
import verify_rpb108_si29_full_J_L2_normalization as m
from verify_rpb108_original_signed_frame_transport import candidate

RANK_SHA = '9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
PR355_SHA = 'abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
NF369_SHA = '3e73a12bbd70158a461d9722dc8fc499eee8d17baf0afc9090bac5d10165e7e8'
TNUM = [[1048576,-83468,750212,-2271087],
        [0,1048576,-1546322,-1621433],
        [0,0,1048576,1115405],
        [0,0,0,1048576]]

def load(path,sha):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sha, (path,'SHA mismatch')
    return json.loads(raw)

def dyad(pair):
    n,e = map(int,pair)
    return arb((n,e))

def endpoints(x):
    lo,hi=x.lower(),x.upper()
    return [str(lo),str(hi)]

def source_endpoint(c,k,d):
    """Value / first derivative of the original physical odd supported generator."""
    B=m.a(m.B)
    omega=2*arb.pi()*m.a(c)
    sine,cosine=(omega*B).sin_cos()
    if k%2==0:
        if d==0: return B**k*sine
        return (k*B**(k-1)*sine if k else arb(0)) + B**k*omega*cosine
    if d==0: return B**k*cosine
    return k*B**(k-1)*cosine-B**k*omega*sine

def evaluate_endpoint(raw_nodes,cr_probes,frequencies,rawX,c,d):
    """w=F c-J X c; coefficient-correlation retained in Arb expression."""
    f=arb(0)
    for j,probe in enumerate(cr_probes):
        q=c[j]
        for freq,coef in zip(frequencies,probe['sine_coefficients']):
            f += q*m.a(F(coef))*source_endpoint(F(freq),0,d)
        f += q*m.a(F(probe['sinh_coefficient']))*((m.a(m.B)/2).sinh() if d==0 else (m.a(m.B)/2).cosh()/2)
    for row,(center,k) in enumerate(raw_nodes):
        q=sum((rawX[row,j]*c[j] for j in range(4)),arb(0))
        if center is None:
            f -= q*((m.a(m.B)/2).sinh() if d==0 else (m.a(m.B)/2).cosh()/2)
        else:
            f -= q*source_endpoint(center,k,d)
    return f

def original_second_derivative(terms):
    """Exactly differentiate supported original smooth function twice on open (-B,B).

    Odd parity is retained and derivatives of sinh represented by complex sin.
    This does NOT include distributional boundary derivatives of zero extension.
    """
    out=[]
    for p,kind,f,coeff in terms:
        omega=flint.acb(2*arb.pi()*m.a(f[0]),m.a(f[1]))
        if p>=2:
            out.append((p-2,kind,f,coeff*p*(p-1)))
        if p>=1:
            out.append((p-1,'c' if kind=='s' else 's',f,
                        coeff*(2*p)*omega*(1 if kind=='s' else -1)))
        out.append((p,kind,f,-coeff*omega*omega))
    return out

def run(args):
    start=time.monotonic();assert flint.__version__=='0.8.0'
    ctx.prec=args.bits
    rank=load(args.rank,RANK_SHA)
    source=load(args.source,PR355_SHA)['data']
    nf369=load(args.nf369,NF369_SHA)['data']
    assert nf369['selected_rank']==242 and nf369['existing_critical_witness_count']==4
    assert nf369['nf369_actual_full_complement_upper_computed'] is False
    assert nf369['input_sha256']['rank']==RANK_SHA
    assert nf369['input_sha256']['mixed']=='19356d4be60ee492896083c1bf6be18cd8ce2da058ff60008181f56a4c3ccc23'
    probes=source['target_probes'];freqs=source['target_sine_frequencies']
    assert len(probes)==4 and len(freqs)==32
    assert [F(z) for z in freqs]==[F(5*n,11) for n in range(1,33)]
    raw_nodes=[]
    for (c,p),count in zip(rank['original_nodes'],rank['selected_multiplicities']):
        assert 0 <= count <= p
        raw_nodes.extend((F(c),k) for k in range(count))
    assert len(raw_nodes)==241 and rank['retained_original_pole']
    raw_nodes.append((None,None))
    terms=[m.pole_terms() if c is None else m.source_terms(c,k) for c,k in raw_nodes]
    critical=[]
    for probe in probes:
        t=[]
        for c,coef in zip(freqs,probe['sine_coefficients']):
            t.extend((p,kind,f,v*m.a(F(coef))) for p,kind,f,v in m.source_terms(F(c),0))
        t.extend((p,kind,f,v*m.a(F(probe['sinh_coefficient']))) for p,kind,f,v in m.pole_terms())
        critical.append(t)
    print('NF374 source custody accepted; begin original 242x242 physical Gram',flush=True)
    kernel=m.Integrals()
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):H[i,j]=H[j,i]=m.gram(terms[i],terms[j],kernel)
    D=candidate(H)
    N=D.transpose()*H*D
    max_err=max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))
    assert max_err < arb('0.01'), ('physical frame not certified',str(max_err))
    print('NF374 original physical frame confirmed; evaluate original 242x4 source overlaps',flush=True)
    V=arb_mat([[m.gram(src,f,kernel) for f in critical] for src in terms])
    G=arb_mat([[m.gram(f,g,kernel) for g in critical] for f in critical])
    Q=D.transpose()*V
    Y=N.solve(Q,algorithm='lu')
    rawX=D*Y
    # Check stationary projection in the ORIGINAL 242 source coordinates.
    phys_res=H*rawX-V
    res_upper=max(abs(phys_res[i,j]).upper() for i in range(242) for j in range(4))
    S=G-V.transpose()*rawX
    S=(S+S.transpose())/2
    fromball=lambda v: arb(dyad(v[0]),dyad(v[1]))
    archived=nf369['physical_quotient_Gram_native']
    # A parent matched physical quotient gram is a powerful identity check.
    matches=[]
    for i in range(4):
        for j in range(4):
            x=S[i,j]-fromball(archived[i][j])
            matches.append(x.contains(0))
    assert all(matches), 'computed physical projection does not overlap original NF369 native physical quotient Gram'
    Y0=nf369['nf369_quotient_response_exact_dyadic_coefficients']
    C=arb_mat([[dyad(Y0[i][j])+int(i==j) for j in range(4)] for i in range(4)])
    T=arb_mat([[m.a(F(v,2**20)) for v in row] for row in TNUM])
    M=C*T
    outputs=[]
    for i in range(4):
        z=[M[j,i] for j in range(4)]
        val=evaluate_endpoint(raw_nodes,probes,freqs,rawX,z,0)
        der=evaluate_endpoint(raw_nodes,probes,freqs,rawX,z,1)
        outputs.append({'direction':i+1,'w_endpoint_interval':endpoints(val),
                        'w_derivative_endpoint_interval':endpoints(der),
                        'w_endpoint_abs_upper':str(abs(val).upper()),
                        'w_derivative_abs_upper':str(abs(der).upper())})
        print('NF374 i',i+1,'w(B) bound',str(abs(val).upper())[:90],
              "w'(B) bound",str(abs(der).upper())[:90],flush=True)
    # NF374: original FULL correlated second derivative Gram, not termwise
    # absolute derivative estimates. Entire coefficients from same physical
    # J242 native solve as above. This includes all signed cross terms.
    print('NF374 original matched second derivative Gram: 242x242 source terms',flush=True)
    source2=[original_second_derivative(t) for t in terms]
    critical2=[original_second_derivative(t) for t in critical]
    H2=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):
            H2[i,j]=H2[j,i]=m.gram(source2[i],source2[j],kernel)
        if i%60==0:print('NF374 H2 row',i,flush=True)
    V2=arb_mat([[m.gram(s,f,kernel) for f in critical2] for s in source2])
    G2=arb_mat([[m.gram(f,g,kernel) for g in critical2] for f in critical2])
    # true w=F M-J X M on fixed original physical frame. We retain
    # all cross terms and the actual correlation among 242 coefficients.
    A2=G2-V2.transpose()*rawX-rawX.transpose()*V2+rawX.transpose()*H2*rawX
    A2=(A2+A2.transpose())/2
    deriv_gram=M.transpose()*A2*M
    deriv_gram=(deriv_gram+deriv_gram.transpose())/2
    curv=[]
    for i in range(4):
        sq=deriv_gram[i,i]
        assert sq.upper()>=arb(0), ('original derivative norm impossible',i+1)
        # K_i = integral_0^B |w_i''| <= sqrt(B/2)*norm_{L2(-B,B)}(w_i'')
        cap=(m.a(F(11,20))*sq.upper()).sqrt()
        accepts=cap<m.a(F(1,100))
        curv.append(dict(direction=i+1,
                         whole_interval_second_derivative_L2_squared=[str(sq.lower()),str(sq.upper())],
                         K_integral_abs_upper=str(cap.upper()),
                         sufficient_NF373_K_le_one_hundredth=bool(accepts)))
        print('NF374 direction',i+1,'K_i upper',str(cap.upper())[:100],
              'K<=1/100?',accepts,flush=True)
    out={'standing':'NATIVE ARB CORRELATED ORIGINAL DERIVATIVE NORM CERTIFICATE ONLY',
         'original_repository_rank_sha256':RANK_SHA,
         'pr355_portable_source_sha256':PR355_SHA,
         'nf369_portable_fields_sha256':NF369_SHA,
         'source_provenance':'Original Actions parent ZIP/JSON SHA-verified on NF372 local creation; CI reads same pinned field slices',
         'working_precision_bits':args.bits,'flint_version':flint.__version__,
         'selected_source_count':242,'critical_source_count':4,
         'physical_frame_max_row_error_upper':str(max_err.upper()),
         'physical_normal_equation_max_residual_upper':str(res_upper),
         'native_parent_physical_quotient_overlap_pass':all(matches),
         'boundary_jets':outputs,'nf374_curvature':curv,
         'nf374_direction_four_K_le_1over100':curv[3]['sufficient_NF373_K_le_one_hundredth'],
         'complete_original_multiplier_high_tail_certified':False,
         'full_exterior_residual_certified':False,'W_ODD_NEG':'OPEN','RH':'OPEN',
         'original_operator_domain_audit':'OPEN','elapsed_seconds':time.monotonic()-start}
    if args.output:
        path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(out,indent=2)+'\n')
    print('NF374 FINISHED: original exterior curvature status direction4 =',curv[3]['sufficient_NF373_K_le_one_hundredth'], '; whole signed Schur OPEN',flush=True)
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--rank',required=True)
    p.add_argument('--source',required=True)
    p.add_argument('--nf369',required=True)
    p.add_argument('--bits',type=int,default=4096)
    p.add_argument('--output',default='artifacts/nf374_original_exterior_curvature.json')
    run(p.parse_args())
