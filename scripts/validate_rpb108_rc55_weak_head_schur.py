"""RC55: two weak Schur blocks, entry-box controls and directional errors."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,sys,itertools
from validate_rpb108_rc31_trial_riesz import mm,tr,inverse,psd
from validate_rpb108_rc47_correlated_native_transport import matrix,entries,serialize,root

def plus(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def minus(a,b):return plus(a,neg(b))
def times(a,b):
    p=[x*y for x in a for y in b];return min(p),max(p)
def reciprocal(a):
    assert a[0]>0;return 1/a[1],1/a[0]
def divide(a,b):return times(a,reciprocal(b))
def square(a):return (F(0) if a[0]<=0<=a[1] else min(x*x for x in a),max(x*x for x in a))
def center(E):return [[sum(E[tuple(sorted((i,j)))])/2 for j in range(8)] for i in range(8)]
def block(A,S,T):return [[A[i][j] for j in T] for i in S]
def quad(v,A):return sum((v[i]*A[i][j]*v[j] for i in range(8) for j in range(8)),F(0))
def sub(A,B):return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def inv_interval(A):
    a,b,d=A[0][0],A[0][1],A[1][1]
    det=minus(times(a,d),square(b));assert det[0]>0 and a[0]>0 and d[0]>0
    return [[divide(d,det),divide(neg(b),det)],[divide(neg(b),det),divide(a,det)]],det
def schur_intervals(J,S,W):
    A=[[J[tuple(sorted((i,j)))] for j in S] for i in S];AI,det=inv_interval(A)
    out={}
    for i in W:
        for j in W:
            value=J[tuple(sorted((i,j)))]
            for k in range(2):
                for l in range(2):value=minus(value,times(times(J[tuple(sorted((S[k],i)))],AI[k][l]),J[tuple(sorted((S[l],j)))]))
            out[i,j]=value
    return A,AI,det,out

def run(paths,replay=False,cert=None):
    raw=[Path(p).read_bytes() for p in paths]
    native,transport,prime,metric,complete,head=[json.loads(x) for x in raw]
    hashes=[hashlib.sha256(x).hexdigest() for x in raw]
    assert [head['input_sha256'][k] for k in [0,1,3,5,7]]==[hashes[k] for k in [0,2,1,4,3]]
    assert [complete['input_sha256'][k] for k in [0,1,3]]==[hashes[k] for k in [0,2,1]]
    Q=entries(head['actual_original_Weil_low_head_entry_enclosures'])
    M=entries(transport['refined_actual_native_Gram_entry_enclosures'])
    P=matrix(native['physical_native_Gram']);Qc=center(Q);Mc=center(M)
    alpha=F(native['canonical_native_Gram_physical_lower_factor']);rho=F(252,257);theta=F(1,4000)
    assert psd(sub(Mc,[[alpha*x for x in row] for row in P]))
    assert psd(sub([[rho*x for x in row] for row in P],Mc))
    assert head['certified_positive_native_subspace_features']==[0,1,6,7]
    assert F(head['original_Weil_floor_on_certified_four_feature_subspace_lower'])>theta
    J={key:(a-theta*M[key][1],b-theta*M[key][0]) for key,(a,b) in Q.items()}
    assert all(Q[i,j]==M[i,j]==(F(0),F(0)) for i in range(8) for j in range(i,8) if (i-j)%2)
    controls={};schurs=[];vectors=[]
    for S,W in [([0,6],[2,4]),([1,7],[3,5])]:
        A,AI,det,bounds=schur_intervals(J,S,W)
        # Build an exact negative entry-box control by minimizing the
        # strong coefficients for the center's weak Schur quadratic.
        Ac=block(Qc,S,S);B=block(Qc,S,W);D=block(Qc,W,W);AcI=inverse(Ac)
        Sc=sub(D,mm(mm(tr(B),AcI),B))
        if Sc[0][0]<0:w=[F(1),F(0)]
        elif Sc[1][1]<0:w=[F(0),F(1)]
        else:
            assert Sc[0][0]>0 and Sc[0][0]*Sc[1][1]-Sc[0][1]**2<0
            w=[-Sc[0][1]/Sc[0][0],F(1)]
        a=[-x[0] for x in mm(mm(AcI,B),[[x] for x in w])];v=[F(0)]*8
        for i,x in zip(S,a):v[i]=x
        for i,x in zip(W,w):v[i]=x
        assert quad(v,Qc)<0;vectors.append(v)
        schurs.append(dict(strong_features=S,weak_features=W,
            strong_target_block_entry_enclosures=[[[str(x) for x in z] for z in row] for row in A],
            strong_target_block_determinant_enclosure=list(map(str,det)),
            strong_target_block_inverse_entry_enclosures=[[[str(x) for x in z] for z in row] for row in AI],
            weak_target_Schur_entry_enclosures=[dict(i=i,j=j,lower=str(a),upper=str(b)) for (i,j),(a,b) in sorted(bounds.items())],
            negative_control_center_Schur=serialize(Sc)))
        if replay:
            # Exact corner inverse checks and an independent LDL solve.
            for aa,bb,dd in itertools.product(A[0][0],A[0][1],A[1][1]):
                exact=inverse([[aa,bb],[bb,dd]])
                for i in range(2):
                    for j in range(2):assert AI[i][j][0]<=exact[i][j]<=AI[i][j][1]
            aa,bb,dd=Ac[0][0],Ac[0][1],Ac[1][1];pivot=dd-bb*bb/aa;assert pivot>0
            LDL=[[1/aa+bb*bb/(aa*aa*pivot),-bb/(aa*pivot)],[-bb/(aa*pivot),1/pivot]]
            assert LDL==AcI and mm(Ac,LDL)==[[F(1),F(0)],[F(0),F(1)]]
    positive=[[Qc[i][j]+P[i][j]/500 for j in range(8)] for i in range(8)]
    assert all(Q[i,j][0]<=positive[i][j]<=Q[i,j][1] for i in range(8) for j in range(i,8))
    assert psd(sub(positive,[[theta*x for x in row] for row in Mc]))
    strong=[0,1,6,7]
    for control in [Qc,positive]:
        assert psd(sub(block(control,strong,strong),[[x/200 for x in row] for row in block(Mc,strong,strong)]))
    # Both controls share an admissible positive canonical metric center.
    V=matrix(native['native_trial_coefficients']);G=matrix(metric['metric_center']);GT=mm(mm(tr(V),G),V)
    T=matrix(prime['physical_native_trial_Gram']);U=matrix(head['nominal_physical_original_source_Gram_Loewner_upper'])
    Ep=matrix(transport['actual_physical_Riesz_error_Gram_Loewner_upper']);Ec=matrix(transport['actual_canonical_Riesz_error_Gram_Loewner_upper'])
    k=list(map(F,complete['complete_physical_operator_parity_norm_upper']))
    delta=F(complete['archimedean_source_approximation_operator_error_upper']);Em=F(metric['mass_metric_error_upper'])
    H=entries(complete['nominal_complete_signed_remainder_head_entry_enclosures']);directional=[]
    for parity,v in enumerate(vectors):
        pn=quad(v,P);e=quad(v,Ep);ec=quad(v,Ec);tt=quad(v,T);u=quad(v,U)
        assert min(pn,e,ec,tt,u)>0
        linear=2*root(e)*(root(u)+delta*root(tt))
        metric_error=Em*tt;source_error=delta*tt;quadratic=k[parity]*e
        hc=F(0);hr=F(0);boxrad=F(0)
        for i in range(8):
            for j in range(8):
                key=tuple(sorted((i,j)));a,b=H[key]
                hc+=v[i]*v[j]*(a+b)/2;hr+=abs(v[i]*v[j])*(b-a)/2
                a,b=Q[key];boxrad+=abs(v[i]*v[j])*(b-a)/2
        base=quad(v,GT)+hc;rad=metric_error+source_error+linear+quadratic+hr
        lo=base-rad-ec;hi=base+rad
        assert lo<0<hi
        factor=2*boxrad/(hi-lo)
        assert factor>F(12 if parity==0 else 21)
        if replay:
            slack=linear*linear/4-e*(u+delta*delta*tt)
            assert slack>=0 and slack*slack>=4*e*e*delta*delta*u*tt
            # Complete-square witness equality for the center control.
            S=[0,6] if parity==0 else [1,7];W=[2,4] if parity==0 else [3,5]
            Sc=matrix(schurs[parity]['negative_control_center_Schur']);w=[v[i] for i in W]
            assert quad(v,Qc)==sum((w[i]*Sc[i][j]*w[j] for i in range(2) for j in range(2)),F(0))
        directional.append(dict(parity='even' if parity==0 else 'odd',coefficients=list(map(str,v)),
            physical_native_squared_norm=str(pn),negative_control_quadratic=str(quad(v,Qc)),
            actual_Weil_quadratic_lower=str(lo),actual_Weil_quadratic_upper=str(hi),
            physical_normalized_actual_Weil_quadratic_lower=str(lo/pn),physical_normalized_actual_Weil_quadratic_upper=str(hi/pn),
            interval_box_quadratic_width=str(2*boxrad),correlated_directional_width=str(hi-lo),
            directional_width_improvement_factor_lower=str(factor),nominal_trial_head_quadratic=str(base),
            canonical_metric_error_allowance=str(metric_error),archimedean_approximation_allowance=str(source_error),
            physical_Riesz_source_linear_allowance=str(linear),physical_Riesz_quadratic_allowance=str(quadratic),
            negative_canonical_Riesz_error_Gram_allowance=str(ec),nominal_head_rounding_allowance=str(hr)))
    return dict(milestone='RC55',status='PASS',input_sha256=hashes,native_features_certified=list(range(8)),
        full_low_head_target_floor=str(theta),strong_features=[0,1,6,7],weak_features=[2,3,4,5],
        strong_block_actual_floor_lower='1/200',full_low_head_target_reduced_to_two_parity_Schur_blocks=True,
        actual_weak_target_Schur_entry_enclosures=schurs,
        admissible_canonical_metric_control=serialize(Mc),negative_head_entry_box_control=serialize(Qc),
        positive_head_entry_box_control=serialize(positive),positive_control_target_floor_certified=True,
        negative_entry_box_control_has_exact_negative_directions=True,
        control_scope='head entry intervals, parity, positive strong block and global native metric bounds; not all source correlations',
        weak_direction_actual_quadratic_enclosures=directional,
        both_actual_weak_direction_signs_unresolved=True,
        actual_head_indefiniteness_proved=False,original_Weil_head_floor_certified=False,
        retained_low_eight_canonical_source_residual_relative_native_metric_upper=head['whole_actual_canonical_orthogonal_source_residual_Gram_relative_native_metric_upper'],
        previous_residual_bound_preserved=True,full_1250_native_projection_constructed=False,aperture_extended=False)

if __name__=='__main__':
    base=Path(__file__).parent.parent/'certificates'
    defaults=[base/name for name in ['rpb108_rc39_native_low_chebyshev_gram.json','rpb108_rc47_correlated_native_transport.json',
        'rpb108_rc43_native_prime_head.json','rpb108_rc38_thirty_two_metric.json',
        'rpb108_rc52_complete_source_covariance.json','rpb108_rc54_original_source_cancellation.json']]
    if len(sys.argv)>1 and sys.argv[1]=='--replay':
        cert=json.loads(Path(sys.argv[2]).read_text());assert run(sys.argv[3:] or defaults,True,cert)==cert
        print('PASS: exact corner inverse and LDL replay, positive/negative entry-box controls, square-completed weak witnesses and correlated directional error bounds')
    else:print(json.dumps(run(sys.argv[1:] or defaults),indent=2))
