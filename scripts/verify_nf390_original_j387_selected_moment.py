#!/usr/bin/env python3
"""NF390 original selected-space j387 signed moment, restoring the odd pole.

Uses immutable ORIGINAL 242 selected signed WJJ and 968 WJF archive, 
the unchanged original rank/source and physical J242 projection.
No new signed kernel cells, no Fourier quadrature, no full residual upper.

For h=j387 in J242, W(u4,h) != <m(D)u4,h> until the odd pole is restored:
<m(D)u4,h> = Wodd(u4,h) + 2<u4,s><h,s>.
Uses this scalar to certify a necessary low-band mismatch lower, and tests 
the fixed NF387 trial against NF375's original fourth low-band target.
"""
import argparse, hashlib, json, zipfile, time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb, arb_mat, ctx
import verify_rpb108_si29_full_J_L2_normalization as phys
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf374_original_matched_curvature import load,dyad,RANK_SHA,PR355_SHA,NF369_SHA,TNUM
from verify_nf379_original_unfitted_signed_dual import makeF,PREC
from verify_nf380_original_archived_signed_dual import (
  ARCHIVE_SHA,M_SHA,MIX_SHA,FRAME_SHA,NF375_SHA,
  arbball,interval,mat2_ball
)

J387_GIT_BLOB_SHA='d705ae312be5324bff64f3a9540e30e8b8bd34dc'
B=F(11,10)

def read_candidate(path):
    raw=Path(path).read_bytes()
    git_sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\x00'+raw).hexdigest()
    assert git_sha==J387_GIT_BLOB_SHA
    j=json.loads(raw)
    assert j['original_rank_sha256']==RANK_SHA
    assert j['original_nf375_source_sha256']==PR355_SHA
    assert j['original_nf375_git_blob_sha1']=='03c709571046d3f09307614aaded9749f5a15ba1'
    assert j['W_ODD_NEG']==j['RH']=='OPEN'
    ns=j['coefficients_raw_source_numerators']
    assert len(ns)==242 and ns[0]==-10753633 and ns[2]==8887300
    assert all(v==0 for i,v in enumerate(ns) if i not in (0,2))
    assert j['coefficients_dyadic_denominator_power']==48
    return ns,j

def main(args):
    start=time.monotonic()
    assert flint.__version__=='0.8.0'
    ctx.prec=PREC
    rank=load(args.rank,RANK_SHA)
    source=load(args.source,PR355_SHA)['data']
    parent=load(args.nf369,NF369_SHA)['data']
    gate=load(args.nf375,NF375_SHA)
    ns,jmeta=read_candidate(args.j387)
    assert parent['selected_rank']==242 and len(source['target_probes'])==4
    t4=[z for z in gate['directions'][3]['dyadic_cutoff_options'] if z['log2_cutoff']==24]
    assert len(t4)==1 and t4[0]['exact_squared_original_individual_gate'] is True
    tau=F(t4[0]['chosen_future_lowband_target'])
    high=F(t4[0]['highband_upper'])
    assert tau==F(7,25*10**12) and high>0
    assert gate['W_ODD_NEG']==gate['RH']=='OPEN'
    raw=Path(args.archive).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==ARCHIVE_SHA
    with zipfile.ZipFile(args.archive) as z:
        matrix_raw=z.read('original_selected_signed_matrix.json')
        mixed_raw=z.read('original_exterior_refined_mixed.json')
    assert hashlib.sha256(matrix_raw).hexdigest()==M_SHA
    assert hashlib.sha256(mixed_raw).hexdigest()==MIX_SHA
    mat=json.loads(matrix_raw);mixed=json.loads(mixed_raw)
    assert mat['selected_rank']==mixed['retained_source_count']==242
    assert mat['complete_upper_triangle_entries']==242*243//2
    assert mixed['complete_mixed_entry_count']==968
    assert mixed['all_968_seven_prime_and_true_pole_cross_checks_passed']
    assert mat['Laplace_terms']==mixed['Laplace_terms']==384
    assert mat['exact_dyadic_frame_transform_sha256']==FRAME_SHA
    assert mat['input_sha256']['rank']==mixed['rank_input_sha256']==RANK_SHA
    sq1=F(mat['double_frame_uniform_error_Frobenius_squared_upper'])
    sq2=F(mat['native_matrix_radius_Frobenius_squared_upper'])
    assert sq1>=0 and sq2>=0 and sq1+sq2<F(1,10**780)
    freqs,C=makeF(source)
    assert [F(z) for z in mixed['target_sine_frequencies']]==freqs
    for old,new in zip(mixed['target_probes'],source['target_probes']):
        assert [F(z) for z in old['sine_coefficients']]==[F(z) for z in new['sine_coefficients']]
        assert F(old['sinh_coefficient'])==F(new['sinh_coefficient'])
    nodes=[];expected=[];offset=0
    for (c,maxk),count in zip(rank['original_nodes'],rank['selected_multiplicities']):
        assert 0<=count<=maxk
        for k in range(count):
            nodes.append((F(c),k))
            expected.append((offset+k,str(F(c)),k))
        offset+=maxk
    assert len(nodes)==241 and rank['retained_original_pole'] and offset==469
    nodes.append((None,None));expected.append((469,None,None))
    assert [(r['original_source_index'],r['center'],r['order']) for r in mixed['rows']]==expected
    J=[phys.pole_terms() if c is None else phys.source_terms(c,k) for c,k in nodes]
    base=[phys.source_terms(f,0) for f in freqs]+[phys.pole_terms()]
    Fs=[]
    for col in range(4):
        term=[]
        for t in range(33):
            term.extend((p,k,f,v*phys.a(F(C[t,col]))) for p,k,f,v in base[t])
        Fs.append(term)
    print('NF390 reconstruct original physical 242 Gram and four matched source columns',flush=True)
    K=phys.Integrals()
    H=arb_mat(242,242)
    for i in range(242):
        for k in range(i+1):
            H[i,k]=H[k,i]=phys.gram(J[i],J[k],K)
    D=candidate(H)
    N=D.transpose()*H*D
    assert max(sum((abs(N[i,k]-int(i==k)) for k in range(242)),arb(0))
               for i in range(242)) < arb('0.01')
    digest=hashlib.sha256()
    for i in range(242):
        for k in range(242):
            digest.update((json.dumps(phys.dyadic(D[i,k]),separators=(',',':'))+'\n').encode())
    assert digest.hexdigest()==FRAME_SHA, 'original physical frame SHA changed'
    V=arb_mat([[phys.gram(j,f,K) for f in Fs] for j in J])
    Y=N.solve(D.transpose()*V,algorithm='lu')
    X=D*Y
    assert max(abs((H*X-V)[i,k]).upper() for i in range(242) for k in range(4))<arb('1e-80')
    G=arb_mat([[phys.gram(f,g,K) for g in Fs] for f in Fs])
    S=G-V.transpose()*X
    S=(S+S.transpose())/2
    for i in range(4):
        for k in range(4):
            assert (S[i,k]-arbball(parent['physical_quotient_Gram_native'][i][k])).contains(0)
    print('NF390 exact original 16 physical Gram source overlaps and archive frame SHA PASS',flush=True)
    # Original WJJ transformed basis and WJF raw-basis mixed are reused verbatim.
    M=arb_mat(242,242)
    for i,row in enumerate(mat['finite_transformed_signed_matrix_upper_native']):
        assert len(row)==i+1
        for k,t in enumerate(row): M[i,k]=M[k,i]=arbball(t)
    Q=arb_mat([[int(i==k) for k in range(242)] for i in range(242)])
    for k,r in enumerate(mat['householder_vectors']):
        assert r['start']==k and len(r['vector'])==242-k
        v=arb_mat([[arb(0) if i<k else dyad(r['vector'][i-k])] for i in range(242)])
        norm=(v.transpose()*v)[0,0]
        assert norm.lower()>0
        Q=Q-2*(Q*v)*v.transpose()/norm
    assert max(sum((abs((Q.transpose()*Q)[i,k]-int(i==k)) for k in range(242)),arb(0))
               for i in range(242))<arb('1e-800')
    L=arb_mat([[arbball(r['entries'][k]['signed_native']) for k in range(4)] for r in mixed['rows']])
    eps=phys.a(sq1+sq2).sqrt()
    Y0=arb_mat([[dyad(parent['nf369_quotient_response_exact_dyadic_coefficients'][i][k]) for k in range(4)] for i in range(4)])
    T=arb_mat([[phys.a(F(t,2**20)) for t in row] for row in TNUM])
    I=arb_mat([[int(i==k) for k in range(4)] for i in range(4)])
    scal=(I+Y0)*T
    alpha=Y*arb_mat([[scal[k,3]] for k in range(4)])
    f=arb_mat([[-(Y0*T)[k,3]] for k in range(4)])
    z=arb_mat([[phys.a(F(n,2**48))] for n in ns])
    assert (z.transpose()*H*z)[0,0].lower()>0
    beta=N.solve(D.transpose()*H*z,algorithm='lu')
    assert max(abs((D*beta-z)[i,0]).upper() for i in range(242))<arb('1e-85')
    signed_J=mat2_ball(M,Q.transpose()*alpha,Q.transpose()*beta,eps)
    signed_F=(f.transpose()*L.transpose()*z)[0,0]
    original_Wu4_j=signed_J+signed_F
    # IMPORTANT: Wodd=P_I m(D) P_I-2|s><s|, s is the *retained* raw
    # J pole at index 241. Since j in J, pole is NOT zero.
    u4s=(H*D*alpha+V*f)[241,0]
    js=(H*z)[241,0]
    correction=2*u4s*js
    multiplier_moment=original_Wu4_j+correction
    jnorm2=(z.transpose()*H*z)[0,0]
    jnorm=jnorm2.sqrt()
    discrepancy=multiplier_moment-jnorm2
    abs_min=(arb(0) if discrepancy.contains(0) else min(abs(discrepancy.lower()),abs(discrepancy.upper())))
    # For t_L= P_I F^-1(1_{|xi|<=L}m uhat4):
    # |<t_L-j,j>| >= |<m(D)u4,j>-||j||²| - high *||j||.
    # If this > tau*||j|| then the actual NF375 physical lowband upper
    # is IMPOSSIBLE for this fixed j at this cutoff.
    threshold=(phys.a(tau+high)*jnorm).upper()
    candidate_stopped=bool(abs_min>threshold)
    # Positive lower on actual squared Fourier-primal mismatch on whole line.
    lower=arb(0) if abs_min<=phys.a(high)*jnorm.upper() else (abs_min-phys.a(high)*jnorm.upper())/jnorm.upper()
    out={
      'standing':'NF390 ORIGINAL J387 SELECTED SIGNED MOMENT AND POLE-CORRECTED SINGLE-MOMENT TEST; RH OPEN',
      'original_rank_sha256':RANK_SHA,'original_source_sha256':PR355_SHA,
      'original_nf369_sha256':NF369_SHA,
      'original_signed_archive_zip_sha256':ARCHIVE_SHA,
      'original_signed_archive_matrix_sha256':M_SHA,
      'original_signed_archive_mixed_sha256':MIX_SHA,
      'original_frame_sha256':FRAME_SHA,
      'nf387_selected_raw_candidate_git_blob_sha1':J387_GIT_BLOB_SHA,
      'signed_original_archive_JJ_JF_reused_cells':30371,
      'fresh_original_signed_kernel_cells':0,
      'original_physical_16_Gram_overlaps':True,
      'original_selected_frame_sha_pass':True,
      'pole_restored_for_selected_test':True,
      'original_Wodd_u4_j387_interval':interval(original_Wu4_j),
      'original_pole_correction_plus_2_u4s_js_interval':interval(correction),
      'original_multiplier_m_u4_j387_interval':interval(multiplier_moment),
      'original_j387_physical_norm_squared_interval':interval(jnorm2),
      'actual_selected_moment_discrepancy_interval':interval(discrepancy),
      'actual_selected_moment_abs_lower':interval(abs_min)[0],
      'original_NF375_fourth_cutoff':2**24,
      'original_NF375_fourth_lowband_future_target':str(tau),
      'original_NF375_fourth_highband_action_norm_upper':str(high),
      'moment_needed_threshold_upper':str(F(int(0))) if False else interval(phys.a(tau+high)*jnorm),
      'actual_original_j387_specific_NF375_lowband_candidate_stopped':candidate_stopped,
      'actual_original_signed_lowband_integral_computed':False,
      'actual_full_original_lowband_upper_computed':False,
      'full_original_exterior_infinite_inverse_computed':False,
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    # Preserve exact derived moment lower via native dyadic endpoint pair.
    out['minimum_lowband_norm_lower_interval']=interval(lower)
    out['candidate_method_stopped_only_if_strictly_proved']=candidate_stopped
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('NF390 signed selected moment interval',str(multiplier_moment),flush=True)
    print('NF390 original j physical norm2 interval',str(jnorm2),flush=True)
    print('NF390 candidate strict selected moment STOP?',candidate_stopped,flush=True)
    print('NF390 no original continuum lowband upper; whole W-ODD-NEG/RH OPEN',flush=True)
    print('NF390 elapsed seconds',round(time.monotonic()-start,2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for key in ('rank','source','nf369','nf375','j387','archive','output'):
        p.add_argument('--'+key,required=True)
    main(p.parse_args())
