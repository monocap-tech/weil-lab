"""Genuine mixed parity blocks, Loewner allowances and actual batch custody."""
from validate_native_two_retained_block_cc9 import mm,tr,minus
from validate_native_two_trial_solve_cc8 import F,solve
from validate_native_odd_enlargement_cc10 import det
from itertools import combinations
from pathlib import Path
import json,hashlib
import gzip
import sys
sys.set_int_max_str_digits(0)

def psd(A):
    n=len(A)
    return all(det([[A[i][j] for j in subset] for i in subset])>=0
               for k in range(1,n+1) for subset in combinations(range(n),k))

def run():
    cases=0
    for c in (F(1,2),F(699,1000),F(2)):
        C=[[F(0) for _ in range(5)] for _ in range(5)]
        for i in range(5):C[i][i]=c+i+1
        C[0][1]=C[1][0]=F(1,4);C[2][3]=C[3][2]=F(1,3);C[3][4]=C[4][3]=F(-1,5)
        for e in (F(0),F(1,100),F(-1,100)):
            B=[[F(1),F(2),F(0),F(0),F(0)],[-F(1),F(1),F(0),F(0),F(0)],
               [e,F(0),F(1),F(1,3),F(0)],[2*e,F(0),F(0),F(1),F(1,2)],
               [-e,F(0),F(1,4),F(0),F(1)]]
            for t in (F(0),F(1,10)):
                T=[[t,F(1,20),F(0),F(0),F(0)],[F(-1,20),t,F(0),F(0),F(0)]]+[[F(0)]*5 for _ in range(3)]
                CT=mm(C,T);R=minus(B,CT)
                bu=mm(tr(B),T);ub=mm(tr(T),B);uc=mm(tr(T),CT);rr=mm(tr(R),R)
                upper=[[bu[i][j]+ub[i][j]-uc[i][j]+rr[i][j]/c for j in range(5)] for i in range(5)]
                exact=mm(tr(B),tr([solve(C,list(col)) for col in zip(*B)]))
                assert psd(minus(upper,exact))
                assert all(upper[1][j]==0 for j in range(2,5))
                # The entire odd source Gram, including off-diagonals, is paid.
                bg=mm(tr(B),B)
                assert all(upper[i][j]==bg[i][j]/c for i in range(2,5) for j in range(2,5))
                cases+=1
    assert not psd([[F(1),F(2),F(0)],[F(2),F(1),F(0)],[F(0),F(0),F(1)]])
    # Whole row-radius allowance, followed by an exact congruence.
    radius_cases=0
    for k in range(12):
        E=[[F((k+i+j)%5-2,100) for j in range(5)] for i in range(5)]
        eps=max(sum(map(abs,row),F(0)) for row in E)
        allowance=[[E[i][j]+(eps if i==j else 0) for j in range(5)] for i in range(5)]
        assert psd(allowance)
        scales=[F(10**16),F(1),F(1),F(1),F(1)]
        assert psd([[allowance[i][j]/(scales[i]*scales[j]) for j in range(5)] for i in range(5)])
        radius_cases+=1
    root=Path(__file__).resolve().parents[1]/'notes/data'
    p=root/'RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json';d=json.loads(p.read_text())
    oldpath=root/'RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json';old=json.loads(oldpath.read_text())
    previous=json.loads((root/'RPB108_ODD_ENLARGEMENT_CC10_CERTIFICATE_20261008.json').read_text())
    assert d['input_sha256']['cc9']==hashlib.sha256(oldpath.read_bytes()).hexdigest()
    block=d['original_completed_schur_lower_block']
    assert [r[:2] for r in block[:2]]==old['original_completed_schur_lower_block']
    def overlap(a,b):return max(F(a[0]),F(b[0]))<=min(F(a[1]),F(b[1]))
    assert overlap(d['odd_native_block'][0][0],previous['odd_native_energy'])
    assert overlap(d['complete_projected_odd_source_gram'][0][0],previous['odd_projected_source_norm_squared'])
    assert overlap(block[0][2],previous['original_completed_schur_lower_block'][0][2])
    assert d['odd_native_pairing_audits']==168 and d['odd_native_symmetry_overlap_audits']==6
    assert d['odd_degrees']==[1,3,5] and d['all_prime_powers']==[2,3,4,5,7,8]
    scales=list(map(F,d['coordinate_congruence_scales']))
    grid=10**d['finite_matrix_grid_digits']
    mids=[[F((((F(x[0])+F(x[1]))*scales[i]*scales[j]/2)*grid).__floor__(),grid) for j,x in enumerate(row)] for i,row in enumerate(block)]
    radius=max(sum((max(mids[i][j]-F(x[0])*scales[i]*scales[j],F(x[1])*scales[i]*scales[j]-mids[i][j]) for j,x in enumerate(row)),F(0)) for i,row in enumerate(block))
    eps=F((radius*grid).__ceil__(),grid)
    assert eps==F(d['whole_scaled_row_radius'])
    G=[[x-(eps if i==j else 0) for j,x in enumerate(row)] for i,row in enumerate(mids)]
    assert G==[list(map(F,row)) for row in d['deterministic_scaled_lower_matrix']]
    assert all(det([row[:k] for row in G[:k]])>0 for k in range(1,6))
    inv=[solve(G,[F(i==j) for i in range(5)]) for j in range(5)]
    traceinverse=sum((scales[i]**2*inv[i][i] for i in range(5)),F(0))
    masstrace=sum(map(F,old['retained_masses']),F(0))+sum(map(F,d['odd_masses']),F(0))
    tau=1/(traceinverse*masstrace);mu=min(tau/266,F(699,2000));canonical=mu/(10*(mu+26))
    assert tau==F(d['slice_retained_physical_margin']) and mu==F(d['whole_infinite_slice_physical_margin'])
    assert canonical==F(d['whole_infinite_slice_canonical_margin'])
    O=[row[2:] for row in G[2:]];oi=[solve(O,[F(i==j) for i in range(3)]) for j in range(3)]
    otrace=sum((oi[i][i] for i in range(3)),F(0))
    ell=G[0][0]/scales[0]**2-(G[0][1]/scales[0])**2/G[1][1]
    crossnorm2=sum((max(map(abs,map(F,block[0][j])))**2 for j in range(2,5)),F(0))
    assert crossnorm2*otrace/ell==F(d['odd_batch_relative_weak_reaction_upper'])
    assert len(d['entire_56_odd_native_weak_row'])==56
    # Independent native-row endpoint sums, without constructor intervals.
    saved=json.loads((root/'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json').read_text())
    raw=gzip.decompress((root/'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
    assert hashlib.sha256(raw).hexdigest()==d['input_sha256']['native']==saved['input_sha256']['native']
    native=json.loads(raw);Q=[[None]*112 for _ in range(112)];index=0
    for i in range(112):
        for j in range(i+1):
            lo,hi=native['lower_triangle_row_major'][index];index+=1
            Q[i][j]=Q[j][i]=(F(int(lo),10**80),F(int(hi),10**80))
    v=list(map(F,saved['rational_coefficient_witness']))
    for r,k in zip(d['entire_56_odd_native_weak_row'],range(1,112,2)):
        lo=sum((v[j]*(Q[k][j][0] if v[j]>=0 else Q[k][j][1]) for j in range(1,112,2)),F(0))
        hi=sum((v[j]*(Q[k][j][1] if v[j]>=0 else Q[k][j][0]) for j in range(1,112,2)),F(0))
        assert F(r[0])<=lo<=hi<=F(r[1])
    rowmass=sum((max(map(abs,map(F,r)))**2 for r in d['entire_56_odd_native_weak_row']),F(0))
    nativebound=F(d['entire_56_odd_native_weak_row_norm_upper'])
    wholebound=F(d['entire_56_odd_completed_weak_row_norm_upper'])
    assert nativebound**2>=rowmass
    sourcebound=(wholebound-nativebound)*F(699,1000)/64
    assert sourcebound>0 and sourcebound**2>=F(old['odd_original_witness_mass'])
    assert F(saved['surrogate_map_norm_upper'])+F(saved['complete_source_map_allowance'])<8
    assert F(d['entire_56_odd_completed_weak_row_norm_upper'])**2/ell==F(d['entire_56_odd_plane_inverse_reaction_allowance'])
    assert not d['entire_56_odd_block_positive_claimed']
    assert F(d['entire_56_odd_completed_weak_row_norm_upper'])<F(53,10**26)
    assert F(d['entire_56_odd_plane_inverse_reaction_allowance'])<F(3,10**17)
    assert F(d['odd_batch_relative_weak_reaction_upper'])<F(2,10**16)
    assert d['five_retained_plane_positive'] and d['protected_slice_codimension']==107
    assert mu>F(7,10**36) and canonical>F(2,10**38)
    assert not d['whole_aperture_positive'] and not d['full_112_retained_sign']
    return dict(passed=True,genuine_five_column_mixed_parity_cases=cases,
        whole_row_radius_congruence_cases=radius_cases,independent_cc10_overlap_audits=3,
        actual_odd_native_overlaps=174,historical_cc9_block_preserved=True,
        independently_recomputed_entire_odd_native_row_entries=56,
        five_retained_plane_positive=True,protected_slice_codimension=107,
        entire_56_odd_plane_inverse_reaction_strict_upper='3/10^17',
        whole_aperture_positive_claimed=False)

if __name__=='__main__':print(json.dumps(run(),indent=2))
