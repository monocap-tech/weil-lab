#!/usr/bin/env python3
"""NF377: native original-physical exterior orientation scan, NOT signed residual acceptance.

No extra selected sources or changed Weil multiplier. Rebuilds J242 and the original
four NF369 exterior F directions exactly. Tests fixed rational sine harmonics outside
PR355's first 32 for substantial *out-of-fit* exterior norm. Strict Arb intervals.
"""
import argparse, json, time, hashlib
from pathlib import Path
from fractions import Fraction as F
import flint
from flint import arb, arb_mat, ctx
import verify_rpb108_si29_full_J_L2_normalization as m
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf374_original_matched_curvature import load, dyad, RANK_SHA, PR355_SHA, NF369_SHA

# Finite predeclared ladder: inspect these frequencies only; no adaptive selection
# across a continuum, no addition to J or F4.
N_LIST=(33,40,48,64,96,128,192,256,384,512,768,1024,2048,4096)
SCALE=10**320

def rat(v):
    n,e=v.man_exp(); return F(int(n))*F(2)**int(e)

def units(v):
    lo=rat(v.lower());hi=rat(v.upper())
    fl=lambda x:x.numerator*SCALE//x.denominator
    ce=lambda x:-fl(-x)
    return [str(fl(lo)),str(ce(hi))]

def fball(v): return arb(dyad(v[0]),dyad(v[1]))

def main():
    p=argparse.ArgumentParser()
    for k in ('rank','source','nf369','output'):p.add_argument('--'+k,required=True)
    p.add_argument('--bits',type=int,default=4096)
    args=p.parse_args(); t0=time.monotonic()
    assert flint.__version__=='0.8.0' and args.bits>=4096
    ctx.prec=args.bits
    rank=load(args.rank,RANK_SHA);source=load(args.source,PR355_SHA)['data'];par=load(args.nf369,NF369_SHA)['data']
    assert par['selected_rank']==242 and par['existing_critical_witness_count']==4
    fs=[F(z) for z in source['target_sine_frequencies']]
    assert fs==[F(5*n,11) for n in range(1,33)]
    rows=[]
    for (c,mult),keep in zip(rank['original_nodes'],rank['selected_multiplicities']):
        assert 0<=keep<=mult
        rows.extend((F(c),k) for k in range(keep))
    assert len(rows)==241 and rank['retained_original_pole']
    rows.append((None,None))
    J=[m.pole_terms() if c is None else m.source_terms(c,k) for c,k in rows]
    F4=[]
    for pp in source['target_probes']:
        z=[]
        for c,a in zip(fs,pp['sine_coefficients']):
            z.extend((pow,kind,fr,val*m.a(F(a))) for pow,kind,fr,val in m.source_terms(c,0))
        z.extend((pow,kind,fr,val*m.a(F(pp['sinh_coefficient']))) for pow,kind,fr,val in m.pole_terms())
        F4.append(z)
    assert len(F4)==4
    test=[m.source_terms(F(5*n,11),0) for n in N_LIST]
    assert all(F(5*n,11) not in fs for n in N_LIST)
    kernel=m.Integrals()
    print('NF377: computing original 242x242 physical Gram',flush=True)
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):H[i,j]=H[j,i]=m.gram(J[i],J[j],kernel)
    D=candidate(H);N=D.transpose()*H*D
    frame_error=max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))
    assert frame_error<arb('0.01')
    print('NF377 original physical frame confirmed; 18 target overlaps',flush=True)
    targets=F4+test
    V=arb_mat([[m.gram(j,f,kernel) for f in targets] for j in J])
    # Avoid quadratic all-target Gram; only original 4x4 Gram and each candidate cross/diagonal.
    G4=arb_mat([[m.gram(a,b,kernel) for b in F4] for a in F4])
    X=D*N.solve(D.transpose()*V,algorithm='lu')
    state=H*X-V
    statmax=max(abs(state[i,k]).upper() for i in range(242) for k in range(len(targets)))
    S4=G4-arb_mat([[sum((V[i,k]*X[i,j] for i in range(242)),arb(0)) for j in range(4)] for k in range(4)])
    S4=(S4+S4.transpose())/2
    for i in range(4):
        for j in range(4):
            assert (S4[i,j]-fball(par['physical_quotient_Gram_native'][i][j])).contains(0),('parent quotient mismatch',i,j)
    print('NF377 inherited physical NF369 quotient overlap 16/16 PASS',flush=True)
    results=[]
    best=None
    for k,n in enumerate(N_LIST):
        idx=4+k
        v=[m.gram(f,test[k],kernel) for f in F4]
        v5=m.gram(test[k],test[k],kernel)
        cross=arb_mat([[v[j]-sum((V[i,j]*X[i,idx] for i in range(242)),arb(0))] for j in range(4)])
        Qnorm=v5-sum((V[i,idx]*X[i,idx] for i in range(242)),arb(0))
        response=S4.solve(cross,algorithm='lu')
        schur=Qnorm-(cross.transpose()*response)[0,0]
        # Check nonnegative Schur and normalized fraction by outward comparison.
        assert Qnorm.lower()>arb(0),('physical quotient not resolved',n)
        assert schur.lower()>arb(0),('out-of-fit quotient not resolved',n)
        ratio=schur/Qnorm
        assert ratio.lower()>arb(0) and ratio.upper()<arb('1.00000000001')
        qualifies=bool(schur.lower()>arb('0.1')*Qnorm.upper() and Qnorm.lower()>arb('0.1'))
        results.append(dict(n=n,frequency=str(F(5*n,11)),raw_exterior_squared_norm_units_1e320=units(Qnorm),
          out_of_fit_squared_norm_units_1e320=units(schur),
          out_of_fit_relative_squared_norm_units_1e320=units(ratio),
          strict_independence_proved=True,strict_quantitative_out_of_fit_10pct_and_norm_10pct=qualifies))
        if qualifies and best is None:best=n
        print('NF377 n',n,'raw Q mass',str(Qnorm),'outside-E ratio',str(ratio), '10%-qualified',qualifies,flush=True)
    # Geometry only: cannot infer any W coupling just from high outside-E ratio.
    assert best is not None,'No quantitatively independent candidate in predeclared ladder; method selection STOP'
    out=dict(status='ORIGINAL_PHYSICAL_ORIENTATION_CERTIFIED_ONLY',flint=flint.__version__,bits=args.bits,
      parent_original_rank_sha256=RANK_SHA,parent_original_sources_sha256=PR355_SHA,parent_nf369_fields_sha256=NF369_SHA,
      original_J_rank=242,unchanged_original_four_critical_probes=4,candidates_n=list(N_LIST),
      parent_16_quotient_Gram_ball_overlaps=True,physical_frame_error_upper=str(frame_error.upper()),
      physical_stationarity_error_upper=str(statmax),
      first_in_ladder_physical_out_of_fit_10pct_and_norm_10pct_n=best,
      tests=results,signed_multipler_coupling_measured=False,signed_frequency_integrated=False,
      lowband_residual_norm_measured=False,whole_exterior_inverse_certified=False,
      W_ODD_NEG='OPEN',RH='OPEN',elapsed_seconds=time.monotonic()-t0)
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF377 independent original orientation gate PASS; signed action STILL OPEN',flush=True)
if __name__=='__main__':main()