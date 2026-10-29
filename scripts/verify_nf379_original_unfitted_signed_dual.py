#!/usr/bin/env python3
"""NF379: one fixed native original signed exterior dual pairing, not RH.

Uses 4096-bit Arb for physical P_J and the original full signed bivariate
archimedean/seven-prime/pole kernel (same source dictionary as PR350).
No source is added to J242. Does not perform a frequency-cell lowband integral.
"""
import argparse, hashlib, json, time, math
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, acb, arb_mat, ctx
import verify_rpb108_si29_full_J_L2_normalization as physical
from verify_rpb108_original_signed_frame_transport import candidate
from verify_rpb108_original_signed_bivariate_kernel import TwoKernel
from verify_nf374_original_matched_curvature import load,dyad,RANK_SHA,PR355_SHA,NF369_SHA,TNUM

# Deliberately fixed before evaluating any complete signed coupling.
INDEX=512
PREC=4096
SIGNED_PREC=3072
LAPLACE_TERMS=384


def exact(x):
    m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def rational_interval(x):
    return [str(exact(x.lower())),str(exact(x.upper()))]
def ball(x):
    n,e=x.man_exp();return [str(n),int(e)]
def native_ball(x):return [ball(x.mid()),ball(x.rad())]
def signed_phase(c,k):
    if c is None:return acb(0,-1)
    return acb((-1)**(k//2)*math.factorial(k))
def hit(c,p,d,q,signed):
    """One original complete signed bivariate jet block; physical labels exact."""
    block=signed.block(c,d,p,q)
    return [[sum((block[t][i][j] for t in range(3)),acb(0)) * signed_phase(c,i)*signed_phase(d,j)
             for j in range(q)] for i in range(p)]
def makeF(source):
    freqs=[F(v) for v in source['target_sine_frequencies']]
    assert len(freqs)==32 and freqs==[F(5*n,11) for n in range(1,33)]
    C=arb_mat(33,4)
    for j,probe in enumerate(source['target_probes']):
        for k,v in enumerate(probe['sine_coefficients']):C[k,j]=physical.a(F(v))
        C[32,j]=physical.a(F(probe['sinh_coefficient']))
    return freqs,C

def main():
    p=argparse.ArgumentParser()
    for name in ('rank','source','nf369','nf375','output'):p.add_argument('--'+name,required=True)
    a=p.parse_args();st=time.monotonic()
    assert flint.__version__=='0.8.0'
    ctx.prec=PREC
    rank=load(a.rank,RANK_SHA);source=load(a.source,PR355_SHA)['data'];nf=load(a.nf369,NF369_SHA)['data']
    gate=load(a.nf375,'f0067870a77f3825005395ac0f6f3e928521796ef3251c04463ba402c40cb5ec')
    budget=F(gate['directions'][3]['original_residual_squared_budget']);assert budget>0
    assert nf['selected_rank']==242 and nf['existing_critical_witness_count']==4
    freqs,C=makeF(source)
    assert len(rank['original_nodes'])==len(rank['selected_multiplicities'])
    clusters=[];rows=[]
    for (center,pmax),count in zip(rank['original_nodes'],rank['selected_multiplicities']):
        assert 0<=count<=pmax
        if count:
            c=F(center);clusters.append((c,count,len(rows)))
            rows.extend([(c,k) for k in range(count)])
    assert len(rows)==241 and rank['retained_original_pole']
    clusters.append((None,1,241));rows.append((None,0))
    J=[physical.pole_terms() if c is None else physical.source_terms(c,k) for c,k in rows]
    base=[physical.source_terms(c,0) for c in freqs]+[physical.pole_terms()]
    Fs=[]
    for col in range(4):
        z=[]
        for k in range(33):
            z.extend((p0,kind,f,v*C[k,col]) for p0,kind,f,v in base[k])
        Fs.append(z)
    n=INDEX;center=F(5*n,11)
    assert center not in freqs and all(center!=c for c,k in rows if c is not None)
    v=physical.source_terms(center,0)
    targets=Fs+[v]
    integrals=physical.Integrals()
    print('NF379 original physical H and 242x5 V',flush=True)
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):H[i,j]=H[j,i]=physical.gram(J[i],J[j],integrals)
    D=candidate(H);N=D.transpose()*H*D
    err=max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))
    assert err<arb('0.01')
    V=arb_mat([[physical.gram(j,x,integrals) for x in targets] for j in J])
    X=D*N.solve(D.transpose()*V,algorithm='lu')
    stat=H*X-V
    statmax=max(abs(stat[i,j]).upper() for i in range(242) for j in range(5))
    assert statmax<arb('1e-80')
    S=arb_mat([[physical.gram(targets[i],targets[j],integrals)
               -sum((V[k,i]*X[k,j] for k in range(242)),arb(0)) for j in range(5)] for i in range(5)])
    S=(S+S.transpose())/2
    par=lambda x:arb(dyad(x[0]),dyad(x[1]))
    for i in range(4):
        for j in range(4):assert (S[i,j]-par(nf['physical_quotient_Gram_native'][i][j])).contains(0)
    S4=arb_mat([[S[i,j] for j in range(4)] for i in range(4)])
    cross=arb_mat([[S[i,4]] for i in range(4)])
    eta=S4.solve(cross,algorithm='lu')
    qnorm=S[4,4];orth=qnorm-(cross.transpose()*eta)[0,0]
    assert qnorm.lower()>0 and orth.lower()>0
    ratio=orth/qnorm
    # Information-sufficiency preflight. A bad physically-fitted candidate stops,
    # it is never secretly substituted with another frequency.
    robust=bool(qnorm.lower()>arb('0.1') and ratio.lower()>arb('0.1'))
    print('NF379 n',n,'physical quotient',str(qnorm),'out-of-fit fraction',str(ratio),'robust',robust,flush=True)

    # Complete ORIGINAL mixed signed form, not the fitted four-zero shadow.
    # Compute only one source-adapted pairing and all its required correlations:
    # WJJ, WJ(base), WJv, W(base,v), W(base,base).
    # The native bivariate kernel has no Fourier quadrature and keeps the arch,
    # seven prime powers and pole exactly as PR350 signed matrix producer.
    signed=TwoKernel(SIGNED_PREC,LAPLACE_TERMS)
    JJ=arb_mat(242,242)
    for ix,(ci,pi,ri) in enumerate(clusters):
        for cj,pj,rj in clusters[:ix+1]:
            block=hit(ci,pi,cj,pj,signed)
            for ii in range(pi):
                for jj in range(pj):
                    s=block[ii][jj];assert s.imag.contains(0)
                    JJ[ri+ii,rj+jj]=JJ[rj+jj,ri+ii]=s.real
        if ix%15==0:print('NF379 original signed J block cluster',ix,'/',len(clusters),'elapsed',round(time.monotonic()-st),flush=True)
    print('NF379 original selected W(J,J) done; new source/candidate mixed blocks',flush=True)
    auxfreq=[(f,0) for f in freqs]+[(None,0),(center,0)]
    JV=arb_mat(242,34)
    for ci,pi,ri in clusters:
        for t,(ct,_) in enumerate(auxfreq):
            block=hit(ci,pi,ct,1,signed)
            for i in range(pi):
                z=block[i][0];assert z.imag.contains(0)
                JV[ri+i,t]=z.real
    AV=arb_mat(34,34)
    for i,(ci,_) in enumerate(auxfreq):
        for j,(cj,_) in enumerate(auxfreq[:i+1]):
            z=hit(ci,1,cj,1,signed)[0][0];assert z.imag.contains(0)
            AV[i,j]=AV[j,i]=z.real
    print('NF379 complete W signed kernel cells constructed',round(time.monotonic()-st),flush=True)
    # Shared original dyadic NF369 matched 4-plane action. u4 = J X (I+Y0)T e4 - F Y0 T e4.
    Y0=arb_mat([[dyad(nf['nf369_quotient_response_exact_dyadic_coefficients'][i][j]) for j in range(4)] for i in range(4)])
    T=arb_mat([[physical.a(F(x,2**20)) for x in row] for row in TNUM]);I=arb_mat([[int(i==j) for j in range(4)] for i in range(4)])
    coeff=(I+Y0)*T
    X4=arb_mat([[X[i,j] for j in range(4)] for i in range(242)])
    uJ=X4*arb_mat([[coeff[i,3]] for i in range(4)])
    uF=C*arb_mat([[T[i,3]-coeff[i,3]] for i in range(4)])
    # actual selected projection of v is J X[:,4]
    x=arb_mat([[X[i,4]] for i in range(242)])
    # exact W(u,v - Jx) = uJ^T (W_Jv-W_JJ*x) + uF^T (W_Fv-W_FJ*x).
    zJ=arb_mat([[JV[i,33]] for i in range(242)])-JJ*x
    zF=arb_mat([[AV[i,33]] for i in range(33)])-arb_mat([[JV[j,i] for j in range(242)] for i in range(33)])*x
    b=(uJ.transpose()*zJ+uF.transpose()*zF)[0,0]
    # Physically remove the four fitted exterior directions from q; their own
    # W coupling is archived as <=1e-50, so we do not mistake near-fitted q
    # for a genuinely new source. Compute native exact E pairings too:
    # W(u,E) = W(u,F-JX4).
    JVf=arb_mat([[JV[i,j] for j in range(33)] for i in range(242)])
    WJF=JVf*C
    AFF=arb_mat([[AV[i,j] for j in range(33)] for i in range(33)])
    WFF=C.transpose()*AFF*C
    WEE=WFF-WJF.transpose()*X4-X4.transpose()*WJF+X4.transpose()*JJ*X4
    WPE=X4.transpose()*(WJF-JJ*X4)
    # Twenty-plus original signed kernel consistency overlaps with the archived
    # NF369 independently built original complete arch/prime/pole result.
    # If even one fails, no new signed coupling is accepted.
    for i in range(4):
        for j in range(4):
            assert (WEE[i,j]-par(nf['actual_exterior_signed_Gram_native'][i][j])).contains(0),('original CE mismatch',i,j)
            assert (WPE[i,j]-par(nf['nf369_selected_to_original_quotient_signed_coupling_native'][i][j])).contains(0),('original BP mismatch',i,j)
    print('NF379 32/32 original signed CE+BP overlap matches PASS',flush=True)
    zEF=WJF-JJ*X4
    zFF=AFF*C-JVf.transpose()*X4
    W4=uJ.transpose()*zEF +uF.transpose()*zFF
    bperp=b-sum((W4[0,j]*eta[j,0] for j in range(4)),arb(0))
    assert b.is_finite() and bperp.is_finite()
    abslo=lambda z:arb(0) if z.contains(0) else min(abs(z.lower()),abs(z.upper()))
    # A positive lower bound for |b_perp|/sqrt(physical orth norm).
    dual_lower=(abslo(bperp)*abslo(bperp)/orth.upper()).lower()
    # Compare exact native dual lower only with the exact inherited NF370
    # individual strong residual squared budget, not a fabricated tolerance.
    obstructs=bool(dual_lower>budget)
    print('NF379 original signed dual obstruction?',obstructs,'budget',str(budget),flush=True)
    report={
      'standing':'NATIVE ORIGINAL FULL SIGNED ONE-DIRECTION UNFITTED DUAL; NO WHOLE-WEIL ACCEPTANCE',
      'original_rank_sha256':RANK_SHA,'source_sha256':PR355_SHA,'nf369_fields_sha256':NF369_SHA,
      'selected_source_count':242,'original_critical_count':4,'unfitted_candidate_n':n,'physical_frame_error_upper':str(err.upper()),
      'physical_normal_equation_error_upper':str(statmax), 'parent_original_16_Gram_overlap':True,
      'physical_q_squared_norm_interval':rational_interval(qnorm),'physical_q_outside_E4_squared_norm_interval':rational_interval(orth),
      'physical_q_outside_E4_ratio_interval':rational_interval(ratio),'physical_orientation_10pct_gate':robust,
      'original_16_CE_and_16_BP_signed_kernel_parent_overlaps':True,
      'complete_original_signed_Wu_q_interval':rational_interval(b),
      'complete_original_signed_Wu_qperp_interval':rational_interval(bperp),
      'complete_original_signed_Wu_E4_intervals':[rational_interval(W4[0,i]) for i in range(4)],
      'strict_original_outside_E4_signed_dual_squared_lower':str(dual_lower),
      'original_nf375_budget_SHA256':'f0067870a77f3825005395ac0f6f3e928521796ef3251c04463ba402c40cb5ec',
      'original_NF370_direction_four_squared_residual_budget':str(budget),
      'method_specific_sufficient_residual_obstructed_by_this_witness':obstructs,
      'signed_native_precision_bits':SIGNED_PREC,'Laplace_terms':LAPLACE_TERMS,
      'integrated_lowband':False,'full_strong_residual_upper':False,
      'whole_infinite_exterior_inverse':False,'W_ODD_NEG':'OPEN','RH':'OPEN',
      'elapsed_seconds':time.monotonic()-st}
    path=Path(a.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(report,indent=2)+'\n')
    print('NF379 ORIGINAL full signed one exterior pairing COMPUTED; remains method-only diagnostic; dual squared lower',dual_lower,flush=True)

if __name__=='__main__':main()
