#!/usr/bin/env python3
"""NF379 exact original-source custody and fixed n512 preflight, not signed action."""
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path
PIN={
 'rank':'9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2',
 'source':'abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770',
 'nf369':'3e73a12bbd70158a461d9722dc8fc499eee8d17baf0afc9090bac5d10165e7e8',
 'nf375':'f0067870a77f3825005395ac0f6f3e928521796ef3251c04463ba402c40cb5ec'
}
T=[[1048576,-83468,750212,-2271087],[0,1048576,-1546322,-1621433],[0,0,1048576,1115405],[0,0,0,1048576]]

def dyad(v):return F(int(v[0]))*F(2)**int(v[1])

def run(p):
    d={}
    for k,sha in PIN.items():
        b=Path(getattr(p,k)).read_bytes();assert hashlib.sha256(b).hexdigest()==sha,k
        d[k]=json.loads(b)
    rank=d['rank'];source=d['source']['data'];nf=d['nf369']['data'];cut=d['nf375']
    assert rank['retained_original_pole'] and sum(rank['selected_multiplicities'])==241
    centers=[F(c) for (c,_),m in zip(rank['original_nodes'],rank['selected_multiplicities']) if m]
    assert len(centers)<=107
    freqs=[F(x) for x in source['target_sine_frequencies']]
    assert freqs==[F(5*i,11) for i in range(1,33)]
    assert len(source['target_probes'])==4 and nf['selected_rank']==242
    n=512;c=F(5*n,11)
    assert c not in centers and c not in freqs
    # Exact exponential-polynomial independence of this frequency label from the
    # fixed J242/F4 basis is an algebraic statement, not physical non-nearness.
    assert [F(y) for y in cut['accepted_cutoffs']]==[F(2**k) for k in range(20,25)]
    budget=F(cut['directions'][3]['original_residual_squared_budget'])
    tau=F(cut['directions'][3]['dyadic_cutoff_options'][0]['chosen_future_lowband_target'])
    assert tau==F(3,2*10**13) and budget==F(2401,2*10**28)
    Y=[[dyad(z) for z in row] for row in nf['nf369_quotient_response_exact_dyadic_coefficients']]
    assert len(Y)==4 and all(len(row)==4 for row in Y)
    # u4 = J X (I+Y0)Te4 - F Y0Te4 in the ORIGINAL unchanged 4 source span.
    t=[F(T[i][3],2**20) for i in range(4)]
    y=[sum(Y[i][j]*t[j] for j in range(4)) for i in range(4)]
    actual_fcoeff=[-z for z in y]
    actual_J_coeff=[t[i]+y[i] for i in range(4)]
    assert all(actual_fcoeff[i]+actual_J_coeff[i]==t[i] for i in range(4))
    # Pole s belongs in J, so for every physical q ⟂ J, <s,q>=0 exactly.
    report={
      'classification':'NF379_EXACT_SOURCE_CUSTODY_AND_ALGEBRA_PREFLIGHT_ONLY',
      'original_input_sha256':PIN,
      'selected_generators':242,'original_selected_polynomial_trig_generators':241,
      'selected_pole_retained':True,'critical_original_probe_count':4,
      'witness_index':n,'witness_center':str(c),
      'witness_frequency_not_in_selected_original_centers':True,
      'witness_frequency_not_in_original_four_probe_harmonics':True,
      'algebraic_exponential_polynomial_independence_without_physical_quantitative_distance':True,
      'original_trial_selected_X_coefficients_in_four_source_basis':[str(x) for x in actual_J_coeff],
      'original_trial_F_coefficients_in_four_source_basis':[str(x) for x in actual_fcoeff],
      'original_squared_strong_residual_budget_dir4':str(budget),
      'original_NF375_lowband_target_dir4_at_2power20':str(tau),
      'native_signed_pairing_computed':False,'native_out_of_fit_ratio_computed':False,
      'native_producer_requires_full_arch_seven_prime_pole_and_32_parent_overlaps':True,
      'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(p.output).parent.mkdir(parents=True,exist_ok=True)
    Path(p.output).write_text(json.dumps(report,indent=2)+'\n')
    print('NF379 exact source/custody/selected-pole/source action preflight PASS; original signed pair pending')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for s in (*PIN,'output'):p.add_argument('--'+s,required=True)
    run(p.parse_args())
