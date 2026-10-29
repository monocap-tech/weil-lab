#!/usr/bin/env python3
"""NF376: independent original QJ242 sine probe and TRUE signed lowband point gate.

Native Arb forms and Fourier overlaps, exact inherited signed m at rational knots.
Point evaluations are NOT a band integral or H_i residual norm certificate.
"""
import argparse, hashlib, json, time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, arb_mat, ctx
import verify_rpb108_si29_full_J_L2_normalization as m
from verify_rpb108_original_signed_frame_transport import candidate
from validate_rpb108_mg07_two_source_original_low32_affine_stop import signed_m_at
from verify_nf374_original_matched_curvature import load, dyad, RANK_SHA, PR355_SHA, NF369_SHA, TNUM

def exact(v):
    n,e=v.man_exp()
    return F(int(n))*F(2)**int(e)

def interval_units(v,scale=10**320):
    lo=exact(v.lower()); hi=exact(v.upper())
    floor=lambda f:f.numerator*scale//f.denominator
    ceil=lambda f:-floor(-f)
    return [str(floor(lo)),str(ceil(hi))]

def fball(v):return arb(dyad(v[0]),dyad(v[1]))
def c_mat(row):return arb_mat([row])

def main():
    p=argparse.ArgumentParser()
    for s in ('rank','source','nf369','output'):p.add_argument('--'+s,required=True)
    p.add_argument('--bits',type=int,default=4096)
    args=p.parse_args()
    assert flint.__version__=='0.8.0'
    ctx.prec=args.bits
    start=time.monotonic()
    rank=load(args.rank,RANK_SHA)
    source=load(args.source,PR355_SHA)['data']
    parent=load(args.nf369,NF369_SHA)['data']
    assert parent['selected_rank']==242 and len(source['target_probes'])==4
    freqs=[F(s) for s in source['target_sine_frequencies']]
    assert freqs==[F(5*n,11) for n in range(1,33)]
    rows=[]
    for (c,mult),keep in zip(rank['original_nodes'],rank['selected_multiplicities']):
        assert 0<=keep<=mult
        rows.extend((F(c),k) for k in range(keep))
    assert len(rows)==241 and rank['retained_original_pole']
    rows.append((None,None))
    J=[m.pole_terms() if c is None else m.source_terms(c,k) for c,k in rows]
    F4=[]
    for probe in source['target_probes']:
        pieces=[]
        for c,coef in zip(freqs,probe['sine_coefficients']):
            pieces.extend((e,kind,f,z*m.a(F(coef))) for e,kind,f,z in m.source_terms(c,0))
        pieces.extend((e,kind,f,z*m.a(F(probe['sinh_coefficient']))) for e,kind,f,z in m.pole_terms())
        F4.append(pieces)
    # Independent *exterior diagnostic*, not an enlarged selected carrier:
    # n=33 is the first sine integer harmonic outside the original 32 probe harmonics.
    test=m.source_terms(F(15),0)
    assert F(15)==F(5*33,11)
    allprobes=F4+[test]
    kernel=m.Integrals()
    print('NF376 parent SHA checks PASS; constructing native original 242-source geometry',flush=True)
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):H[i,j]=H[j,i]=m.gram(J[i],J[j],kernel)
    D=candidate(H);N=D.transpose()*H*D
    err=max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))
    assert err<arb('0.01')
    V=arb_mat([[m.gram(j,p,kernel) for p in allprobes] for j in J])
    G=arb_mat([[m.gram(a,b,kernel) for b in allprobes] for a in allprobes])
    X=D*N.solve(D.transpose()*V,algorithm='lu')
    stat=H*X-V
    statmax=max(abs(stat[i,k]).upper() for i in range(242) for k in range(5))
    S=G-V.transpose()*X;S=(S+S.transpose())/2
    for i in range(4):
        for j in range(4):
            assert (S[i,j]-fball(parent['physical_quotient_Gram_native'][i][j])).contains(0),('parent quotient mismatch',i,j)
    assert S[4,4].lower()>arb(0),'new quotient has no certified nonzero norm'
    # Ensure fifth physical quotient is genuinely outside the original four-E plane.
    S4=arb_mat([[S[i,j] for j in range(4)] for i in range(4)])
    cross=arb_mat([[S[i,4]] for i in range(4)])
    eta=S4.solve(cross,algorithm='lu')
    schur=S[4,4]-(cross.transpose()*eta)[0,0]
    assert schur.lower()>arb(0),'fifth quotient independence unresolved'
    # Native outward conditioning observation: most of q5 is already in the
    # FITTED E4 plane, so test the Schur-orthogonal remainder, not raw q5.
    assert schur.upper()*arb(10**20) < 4*S[4,4].lower(), 'near-fitted ratio not established'
    print('NF376 independent q5 and tiny outside-E4 ratio: PASS',flush=True)
    Y0=parent['nf369_quotient_response_exact_dyadic_coefficients']
    M=arb_mat([[dyad(Y0[i][j])+int(i==j) for j in range(4)] for i in range(4)])
    T=arb_mat([[m.a(F(v,2**20)) for v in row] for row in TNUM])
    # Direction 4 prioritized: true trial u4=F t4-QF (I+Y0)t4
    t=[T[j,3] for j in range(4)]
    coeff=[sum((M[j,k]*T[k,3] for k in range(4)),arb(0)) for j in range(4)]
    # 2pi frequency transform fhat=-i <f,sin(2pi xi x)> on entire supported interval.
    # Projection coeffs X from original native physical Gram, not arbitrary heuristic j.
    knots=[F(1,4),F(1,2),F(1),F(2),F(4),F(8),F(15),F(16),F(24),F(32)]
    results=[]
    for xi in knots:
        sinus=m.source_terms(xi,0)
        bJ=[m.gram(q,sinus,kernel) for q in J]
        bF=[m.gram(f,sinus,kernel) for f in F4]
        b5=m.gram(test,sinus,kernel)
        # Exact original matched trial and true independent Q witness.
        u=sum(((t[j]-coeff[j])*bF[j] for j in range(4)),arb(0))
        u+=sum((bJ[i]*sum((X[i,j]*coeff[j] for j in range(4)),arb(0)) for i in range(242)),arb(0))
        q=b5-sum((X[i,4]*bJ[i] for i in range(242)),arb(0))
        e=[bF[j]-sum((X[i,j]*bJ[i] for i in range(242)),arb(0)) for j in range(4)]
        q_perp=q-sum((eta[j,0]*e[j] for j in range(4)),arb(0))
        ml,mh=signed_m_at(xi)
        # Finite exact signed multiplier interval at this genuine rational frequency.
        mlb=m.a(ml);mhb=m.a(mh)
        point=2*u*q
        signed=point*arb(mlb, mhb-mlb)
        signed_perp=2*u*q_perp*arb(mlb,mhb-mlb)
        results.append({'frequency':str(xi),'signed_m_interval':[str(ml),str(mh)],
           'original_u4_Fourier_sine_amplitude_units_1e320':interval_units(u),
           'new_Qwitness_Fourier_sine_amplitude_units_1e320':interval_units(q),
           'original_signed_two_sign_cross_integrand_units_1e320':interval_units(signed),
           'orthogonalized_q5_sine_amplitude_units_1e320':interval_units(q_perp),
           'orthogonalized_signed_two_sign_cross_integrand_units_1e320':interval_units(signed_perp),
           'orthogonalized_cross_integrand_strict_sign':('positive' if signed_perp.lower()>0 else 'negative' if signed_perp.upper()<0 else 'unresolved'),
           'signed_cross_integrand_strict_sign':('positive' if signed.lower()>0 else 'negative' if signed.upper()<0 else 'unresolved')})
        print('original signed lowband knot',str(xi),'signed cross',results[-1]['signed_cross_integrand_strict_sign'],flush=True)
    out={'status':'CERTIFIED_ORIGINAL_QWITNESS_AND_SIGNED_LOWBAND_POINT_SAMPLES_ONLY',
        'working_precision_bits':args.bits,'original_selected_count':242,
        'original_critical_count':4,'diagnostic_exterior_witness':'Q sin(2*pi*15*x) supported [-11/10,11/10]',
        'diagnostic_is_new_selected_source':False,
        'original_n33_not_in_32_critical_probes':True,
        'original_rank_sha256':RANK_SHA,'original_source_sha256':PR355_SHA,'original_nf369_fields_sha256':NF369_SHA,
        'parent_16_original_physical_quotient_ball_overlap':True,
        'frame_row_error_upper':str(err.upper()),
        'physical_stationarity_residual_upper':str(statmax),
        'new_q_squared_norm_units_1e320':interval_units(S[4,4]),
        'new_q_mod_E4_squared_norm_units_1e320':interval_units(schur),
        'new_q_outside_fitted_E4_relative_norm_strict_upper':'2e-10',
        'q5_perp_is_explicitly_constructed_in_true_original_physical_space':True,
        'actual_original_signed_point_samples':results,
        'original_lowband_integrated_signed_coupling_computed':False,
        'j_i_in_J242_constructed_for_lowband':False,
        'full_original_lowband_H_i_norm_computed':False,
        'whole_four_direction_residual_certified':False,
        'W_ODD_NEG':'OPEN','RH':'OPEN','elapsed_seconds':time.monotonic()-start}
    Path(args.output).parent.mkdir(parents=True,exist_ok=True)
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF376 native physical orthogonalized outside-E witness and signed points PASS; integrated lowband OPEN',flush=True)

if __name__=='__main__':main()
