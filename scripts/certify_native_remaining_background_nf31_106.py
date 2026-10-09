#!/usr/bin/env python3
"""NF31: all remaining retained couplings to the fixed successful pairs.
Finite native elimination is not infinite-high collective elimination.
"""
import json,gzip,base64,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import certify_native_high_correction_nf26_106 as base
import certify_native_retained_coupling_nf27_106 as matrix
n=base.n;I=n.I
dot=matrix.dot;mv=matrix.matvec

PATHS=['notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json','notes/data/RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json','notes/data/RPB108_NF27_RETAINED_COUPLING_CERTIFICATE_20261009.json','notes/data/RPB108_NF29_LIFTED_RESPONSE_CERTIFICATE_20261009.json','notes/data/RPB108_NF30_FIXED_EXPANDED_RESPONSE_20261009.json','notes/data/RPB108_NF30_EXPANDED_RESPONSE_CERTIFICATE_20261009.json']
SHA=['6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','f2010510bacac64c45ef1825cd5e2c41e395519417815a43530e44e6cfdbf930','2110e07c7a7e39d2b454cff364c0863f6f3e3ff151cf72309999130f5e17fe42','069d4acc267a0ac48154427a033cccca96243743dd31e36449f7189de03e895a','7460d5ed3b159d34fa002a56382b40f91cde1d7712fe5e2b1b0ff2b4df7cb65b','d0625cefe819f3704dec1d75bf0ad0bcd4ea8a3cd6806ebe6d76056733ac321b']

def inputs():
    raw=[Path(p).read_bytes() for p in PATHS];assert [hashlib.sha256(b).hexdigest() for b in raw]==SHA
    data=list(map(json.loads,raw));source={};hashes=[]
    for path,key,expected in [('nf24-inputs/Weil/native112_N720_K620.json.gz','complete_form','f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'),('nf24-inputs/Weil/native_boundary_columns_112_113.json.gz','original_full_source','da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee'),('nf24-inputs/Weil/native_boundary_114_115.json.gz','original_full_source','0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad')]:
        b=gzip.decompress(Path(path).read_bytes());s=hashlib.sha256(b).hexdigest();assert s==expected;hashes.append(s);source.update(json.loads(b)[key])
    return data,source,hashes

def complement(x,w):
    assert len(x)==len(w)==56 and sum(a*b for a,b in zip(x,w))==0
    # Deterministic maximal constraint minor avoids an arbitrary small pivot.
    p,q=max(((i,j) for i in range(56) for j in range(i+1,56)),key=lambda ij:abs(x[ij[0]]*w[ij[1]]-x[ij[1]]*w[ij[0]]))
    det=x[p]*w[q]-x[q]*w[p];assert det!=0
    free=[j for j in range(56) if j not in (p,q)]
    T=[[F(0)]*54 for i in range(56)]
    for col,j in enumerate(free):
        T[j][col]=1;T[p][col]=(-x[j]*w[q]+x[q]*w[j])/det;T[q][col]=(-x[p]*w[j]+x[j]*w[p])/det
    assert all(sum(a*b for a,b in zip(x,col))==sum(a*b for a,b in zip(w,col))==0 for col in zip(*T))
    return T,p,q,free

def run(data,source):
    targets,nf26,nf27,nf29,trial,nf30=data
    eta=2*n.A*4*F(106,125)**320/(1-F(106,125))+16*(n.A/2)**41/F(factorial(41))
    def Q(i,j):return I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full']))
    rows=[]
    for idx,(r,cv,cw,ch) in enumerate(zip(targets['authenticated_compensated_targets'],nf26['parity_certificates'],nf27['parity_certificates'],nf29['parity_certificates'])):
        parity=r['parity'];assert parity==cv['parity']==cw['parity']==ch['parity']
        ids=r['retained_indices'];x=list(map(F,r['retained_coefficients']));w=list(map(F,cw['exact_rational_retained_response']))
        T,p,q,free=complement(x,w)
        A=[[Q(i,j) for j in ids] for i in ids]
        AT=[[dot(row,col) for col in zip(*T)] for row in A]
        C=[[dot(col,row) for row in zip(*AT)] for col in zip(*T)]
        inv,proof=matrix.inverse(C)
        TB=[[dot(row,col) for col in zip(*inv)] for row in T]
        K=[[dot(row,col) for col in T] for row in TB]
        trace=sum((K[i][i] for i in range(56)),I(0));assert trace.l>0
        lv=[I(*map(F,a))-I(*map(F,b)) for a,b in zip(r['low_source_coordinates'],cv['retained_approximant_Ly_coordinates'])]
        hi=ch['high_lift_indices'];coeff=w+[-F(z) for z in ch['fixed_rational_high_lift']]
        lw=[sum((z*Q(i,j) for i,z in zip(ids+hi,coeff)),I(0)) for j in ids]
        error=[F(cv['correction_norm_upper'])*eta,F(0)]
        if parity=='even':
            assert nf30['sufficient_collective_test_status']=='PASS'
            lz=[I(*map(F,z)) for z in nf30['retained_approximant_Lz_coordinates']]
            lw=[a-b for a,b in zip(lw,lz)]
            error[1]=eta*F(n.sqrt_r(sum(F(z)**2 for z in trial['fixed_rational_coefficients'])).h,n.SCALE)
            energy=nf30['original_finite_energy_Gram'];oldscore=nf30['sufficient_collective_matrix']
        else:
            assert ch['sufficient_collective_test_status']=='PASS'
            energy=ch['original_finite_energy_Gram'];oldscore=ch['sufficient_collective_matrix']
        low=[lv,lw];centers=[[v.mid() for v in row] for row in low]
        radii=[error[i]+8*max(F(v.h-v.l,2*n.SCALE) for v in low[i]) for i in range(2)]
        # All 108 remaining-coordinate couplings per parity. Their physical
        # uncertainty is a ball, not independent interval choices.
        couplings=[[dot(col,b) for col in zip(*T)] for b in low]
        basis_masses=[F(n.sqrt_r(sum(z*z for z in col)).h,n.SCALE) for col in zip(*T)]
        paid_couplings=[[z+I(-error[i]*mass,error[i]*mass) for z,mass in zip(couplings[i],basis_masses)] for i in range(2)]
        hat=[[dot(centers[i],mv(K,centers[j])) for j in range(2)] for i in range(2)]
        assert min(hat[0][0].l,hat[1][1].l)>0
        norms=[F(n.sqrt_r(F(hat[i][i].h,n.SCALE)).h,n.SCALE) for i in range(2)]
        roottrace=F(n.sqrt_r(F(trace.h,n.SCALE)).h,n.SCALE)
        e=[z*roottrace for z in radii]
        payment=[[e[i]*norms[j]+e[j]*norms[i]+e[i]*e[j] for j in range(2)] for i in range(2)]
        reaction=[[hat[i][j]+I(-payment[i][j],payment[i][j]) for j in range(2)] for i in range(2)]
        energy=[[I(*map(F,z)) for z in row] for row in energy]
        finite=[[energy[i][j]-reaction[i][j] for j in range(2)] for i in range(2)]
        det=finite[0][0]*finite[1][1]-n.sq(finite[0][1])
        assert min(finite[0][0].l,finite[1][1].l,det.l)>0
        # This arithmetic ledger deliberately is NOT a collective Schur bound.
        arithmetic=[[I(*map(F,oldscore[i][j]))-reaction[i][j] for j in range(2)] for i in range(2)]
        ad=arithmetic[0][0]*arithmetic[1][1]-n.sq(arithmetic[0][1])
        print(parity,'remaining native background gap',float(1/F(trace.h,n.SCALE)),'finite lifted family PASS',flush=True)
        print(parity,'finite reaction fractions',*[float(F((reaction[i][i]/energy[i][i]).h,n.SCALE)) for i in range(2)],flush=True)
        # Freeze two remaining native response candidates with exact physical
        # orthogonality to x,w. These are candidates for later source work.
        frozen=[];response_checks=[]
        for i in range(2):
            coordinate=mv(inv,[dot(col,centers[i]) for col in zip(*T)])
            rounded=[F((z.mid()*10**100).__floor__(),10**100) for z in coordinate]
            f=[sum(a*b for a,b in zip(row,rounded)) for row in T]
            assert sum(a*b for a,b in zip(x,f))==sum(a*b for a,b in zip(w,f))==0
            # Independent finite gain on the exact frozen candidate.
            gain=2*dot(f,low[i])-dot(f,mv(A,f))
            fm=F(n.sqrt_r(sum(z*z for z in f)).h,n.SCALE)
            gain+=I(-2*error[i]*fm,2*error[i]*fm)
            assert gain.l>0 and gain.l<=reaction[i][i].h and gain.h>=reaction[i][i].l
            frozen.append(list(map(str,f)));response_checks.append(gain.ends())
        rows.append(dict(parity=parity,remaining_dimension=54,retained_constraint_pivots=[p,q],free_retained_coordinates=free,
            exact_constraint_basis_rule='T_j=e_j+(-x_j*w_q+x_q*w_j)/det*e_p+(-x_p*w_j+x_j*w_p)/det*e_q; det=x_p*w_q-x_q*w_p',
            remaining_native_background_positive=True,remaining_inverse_verification=proof,physical_remaining_native_gap_lower=str(1/F(trace.h,n.SCALE)),
            remaining_inverse_physical_trace_upper=str(F(trace.h,n.SCALE)),
            retained_source_ball_radii=list(map(str,radii)),source_coordinate_reconstruction_error_bounds=list(map(str,error)),
            retained_approximant_source_coordinates=[[z.ends() for z in row] for row in low],
            remaining_native_couplings_approximant=[[z.ends() for z in row] for row in couplings],
            remaining_original_native_couplings=[[z.ends() for z in row] for row in paid_couplings],
            midpoint_finite_reaction_Gram=[[z.ends() for z in row] for row in hat],reaction_sqrt_error_bounds=list(map(str,e)),
            finite_reaction_entrywise_error_payments=[[str(z) for z in row] for row in payment],
            original_finite_remaining_reaction_Gram=[[z.ends() for z in row] for row in reaction],
            diagonal_finite_reaction_fractions=[(reaction[i][i]/energy[i][i]).ends() for i in range(2)],
            finite_lifted_pair_after_remaining_elimination=[[z.ends() for z in row] for row in finite],finite_Schur_determinant=det.ends(),
            finite_full_retained_lifted_family_positive=True,
            arithmetic_old_sufficient_matrix_minus_finite_reaction_NOT_collective_bound=[[z.ends() for z in row] for row in arithmetic],
            arithmetic_NOT_collective_determinant=ad.ends(),
            frozen_remaining_native_response_candidates=frozen,independent_frozen_response_native_gain_checks=response_checks,
            candidate_complete_sources_certified=False,remaining_complete_source_Gram_certified=False,whole_aperture_positive=False))
    return dict(milestone='NF31',aperture='53/50',interval_grid_digits=500,parity_certificates=rows,
        all_remaining_native_couplings_paid=True,previous_four_direction_infinite_high_certificate_preserved=True,
        complete_collective_infinite_high_Schur_certified=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args()
    data,source,hashes=inputs();out=run(data,source);out['authenticated_input_sha256']=SHA;out['native_archive_sha256']=hashes
    raw=(json.dumps(out,indent=2)+'\n').encode()
    if a.output.endswith('.b64'):raw=base64.b64encode(gzip.compress(raw,mtime=0))+b'\n'
    Path(a.output).write_bytes(raw)
