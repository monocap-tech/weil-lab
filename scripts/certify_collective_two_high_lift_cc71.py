#!/usr/bin/env python3
"""Joint original native W+H2 sign and fixed rational background lifts."""
import argparse,gzip,hashlib,json
from fractions import Fraction as F
from pathlib import Path
import certify_native_retained_coupling_nf27_106 as c
I=c.I
def mm(A,B):return [[c.dot(row,col) for col in zip(*B)] for row in A]
def transpose(A):return list(map(list,zip(*A)))
def trace(A):return sum((A[i][i] for i in range(len(A))),I(0))
def run(targets,native,first,second):
    data=dict(native);data.update(first);data.update(second);rows=[]
    def entry(i,j):return I(*map(F,data[f'{min(i,j)},{max(i,j)}']['full']))
    for t in targets['authenticated_compensated_targets']:
        ids=t['retained_indices'];x=list(map(F,t['retained_coefficients']));hs=t['high_indices'];assert len(hs)==2
        W=[[F(0)]*55 for _ in range(56)]
        for j in range(55):W[0][j]=-x[j+1]/x[0];W[j+1][j]=F(1)
        A=[[entry(i,j) for j in ids] for i in ids]
        AW=mm(transpose(W),mm(A,W))
        K=mm([[entry(h,i) for i in ids] for h in hs],W)
        C=[[entry(h,j) for j in hs] for h in hs]
        Ci,cproof=c.inverse(C);Z=mm(Ci,K)
        reaction=mm(transpose(K),Z)
        S=[[AW[i][j]-reaction[i][j] for j in range(55)] for i in range(55)]
        Si,sproof=c.inverse(S)
        mass=mm(transpose(W),W)
        inverse_physical_trace=trace(mm(Si,mass));assert inverse_physical_trace.l>0
        bg_gap=1/F(inverse_physical_trace.h,c.n.SCALE)
        highgap=1/F(trace(Ci).h,c.n.SCALE)
        zsquare=sum((v.absupper()**2 for row in Z for v in row),F(0))
        whole_gap=min(bg_gap/(1+2*zsquare),highgap/2);assert whole_gap>0
        # Freeze a genuine rational polynomial lift, then recertify its
        # native energy rather than treating an interval inverse as exact.
        fixed=[[F((v.mid()*10**100).__floor__(),10**100) for v in row] for row in Z]
        cf=mm(C,fixed)
        observed_residual=max((K[i][j]-cf[i][j]).absupper() for i in range(2) for j in range(55))
        assert observed_residual<F(1,10**68)
        kz=mm(transpose(K),fixed);ztk=transpose(kz);ztcz=mm(transpose(fixed),mm(C,fixed))
        lifted=[[AW[i][j]-kz[i][j]-ztk[i][j]+ztcz[i][j] for j in range(55)] for i in range(55)]
        Li,lproof=c.inverse(lifted)
        liftmass=[[mass[i][j]+sum((fixed[h][i]*fixed[h][j] for h in range(2)),F(0)) for j in range(55)] for i in range(55)]
        lifttrace=trace(mm(Li,liftmass));assert lifttrace.l>0
        liftgap=1/F(lifttrace.h,c.n.SCALE)
        # Retained-background true reaction when restricted to H2.
        Ai,aproof=c.inverse(AW);T=mm(Ci,mm(K,mm(Ai,transpose(K))))
        tr=trace(T);det=T[0][0]*T[1][1]-T[0][1]*T[1][0]
        discr=tr*tr-4*det;assert discr.l>0
        sq=I(F(c.n.sqrt_r(F(discr.l,c.n.SCALE)).l,c.n.SCALE),F(c.n.sqrt_r(F(discr.h,c.n.SCALE)).h,c.n.SCALE))
        largest=(tr+sq)/2;assert largest.h<c.n.SCALE
        allids=ids+hs
        fullmatrix=[[entry(i,j) for j in allids] for i in allids]
        Fi,fproof=c.inverse(fullmatrix)
        finite_full_gap=1/F(trace(Fi).h,c.n.SCALE)
        # Principal retained block of the joint inverse is the inverse
        # of the complete two-high retained Schur matrix.
        schur_full_gap=1/F(sum((Fi[i][i] for i in range(56)),I(0)).h,c.n.SCALE)
        assert finite_full_gap>0 and schur_full_gap>0
        rows.append(dict(parity=t['parity'],high_indices=hs,retained_background_dimension=55,
            joint_original_finite_dimension=57,high_inverse_proof=cproof,constrained_native_inverse_proof=aproof,
            collective_two_high_Schur_inverse_proof=sproof,original_W_plus_H2_positive=True,
            retained_Schur_physical_gap_lower=str(bg_gap),whole_W_plus_H2_physical_gap_lower=str(whole_gap),
            true_two_high_collective_loading_interval=largest.ends(),
            fixed_rational_high_lift_coefficients=[[str(v) for v in row] for row in fixed],
            fixed_lift_inverse_proof=lproof,fixed_lift_physical_gap_lower=str(liftgap),
            fixed_lift_measured_high_source_coordinate_upper=str(observed_residual),
            fixed_lift_all_55_directions_positive=True,full_infinite_high_background_certified=False))
        rows[-1].update(complete_original_E_plus_H2_dimension=58,
            complete_original_E_plus_H2_positive=True,complete_original_E_plus_H2_inverse_proof=fproof,
            complete_original_E_plus_H2_physical_gap_lower=str(finite_full_gap),
            complete_retained_two_high_Schur_positive=True,
            complete_retained_two_high_Schur_physical_gap_lower=str(schur_full_gap))
        print(t['parity'],'native H2 loading',float(F(largest.l,c.n.SCALE)),float(F(largest.h,c.n.SCALE)),flush=True)
    controls=[]
    for b in [F(99,100),F(1),F(101,100)]:
        # Native high elimination and rational lift both use actual signed
        # off-diagonals. The genuine crossing must preserve their sign.
        schur=1-b*b;fixed=F(1)
        frozen_energy=1-2*b*fixed+fixed*fixed
        assert frozen_energy-schur==(fixed-b)**2
        controls.append(dict(mixed=str(b),true_Schur=str(schur),fixed_lift_energy=str(frozen_energy),rational_lift_square_identity=True))
    scaled=[]
    eps=F(1,10**18)
    for b in [F(99,100),F(1),F(101,100)]:
        schur=eps**2*(1-b*b);lift=eps**2*(2-2*b)
        assert lift-schur==eps**2*(1-b)**2
        scaled.append(dict(retained_diagonal=str(eps**2),mixed=str(eps*b),high_diagonal='1',true_Schur=str(schur),fixed_lift_energy=str(lift)))
    levels=[]
    for level in [F(1,1000),F(1,10),F(2)]:
        schur=1+level-1/(1+level);assert schur==level*(2+level)/(1+level)>0
        levels.append(dict(whole_mass_shift=str(level),true_Schur=str(schur),physical_ground_level=str(level)))
    return dict(milestone='CC71',aperture='53/50',parity_certificates=rows,
        combined_W_plus_H2_finite_dimension=114,fixed_lift_total_dimension=110,
        combined_complete_original_E_plus_H2_dimension=116,
        genuine_crossing_controls=controls,near_critical_crossing_controls=scaled,positive_whole_mass_levels=levels,whole_aperture_positive=False,
        full_infinite_high_collective_Schur=False,full_Weil_nonimplication_claimed=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for a in ['targets','native','first','second']:p.add_argument(a)
    p.add_argument('--output',required=True);a=p.parse_args()
    raw=[Path(a.targets).read_bytes()]+[gzip.decompress(Path(v).read_bytes()) for v in [a.native,a.first,a.second]]
    hashes=[hashlib.sha256(v).hexdigest() for v in raw]
    assert hashes==['6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00','f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81','da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee','0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad']
    d=list(map(json.loads,raw));r=run(d[0],d[1]['complete_form'],d[2]['original_full_source'],d[3]['original_full_source']);r['input_sha256']=hashes
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
