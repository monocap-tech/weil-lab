#!/usr/bin/env python3
"""NF25: pay all physical errors in the three-source moment Gram and test
the original CC64 correlation majorant on the exact NF24 rational targets.
Failure of a sufficient upper estimator is not a negative Weil vector.
"""
import argparse,json,gzip,hashlib
from fractions import Fraction as F
from math import factorial
import certify_native_correlated_sources_nf25_106 as n

def enlarged(v,e):return v+n.I(-e,e)
def ends(v):return [F(v.l,n.SCALE),F(v.h,n.SCALE)]
def certify(targets,approx,source):
    assert targets['aperture']==approx['aperture']=='53/50'
    assert approx['regular_kernel_degree']==320 and approx['interval_grid_digits']==280
    assert len(targets['authenticated_compensated_targets'])==len(approx['parities'])==2
    eta_arch=2*n.A*4*F(106,125)**320/(1-F(106,125))
    pole_rem=2*(n.A/2)**41/F(factorial(41))
    results=[]
    for w,a in zip(targets['authenticated_compensated_targets'],approx['parities']):
        assert w['parity']==a['parity']
        coeff=list(map(F,w['retained_coefficients']+w['exact_rational_high_compensation']))
        assert sum(v*v for v in coeff)<F(1001,1000)**2
        assert len(w['retained_indices'])==56
        assert len(a['independent_original_native_pairing_checks'])==6
        for check in a['independent_original_native_pairing_checks']:
            v=n.I(*map(F,check['reconstructed_pairing']))+n.I(-F(check['paid_L2_error']),F(check['paid_L2_error']))
            original=n.I(*map(F,check['original_pairing']))
            assert v.l<=original.h and v.h>=original.l
        g=[[n.I(*map(F,v)) for v in row] for row in a['reconstructed_three_source_Gram']]
        assert all(g[i][i].l>0 for i in range(3))
        masses=[F(1001,1000),F(1),F(1)]
        projection=list(map(F,a['projection_center_L2_errors']))
        eta=[m*(eta_arch+8*pole_rem)+e for m,e in zip(masses,projection)]
        norms=[F(n.sqrt_r(F(g[i][i].h,n.SCALE)).h,n.SCALE) for i in range(3)]
        errors=[[eta[i]*norms[j]+eta[j]*norms[i]+eta[i]*eta[j] for j in range(3)] for i in range(3)]
        exact=[[enlarged(g[i][j],errors[i][j]) for j in range(3)] for i in range(3)]
        high=w['high_indices']
        C=[[n.I(*map(F,source[f'{min(i,j)},{max(i,j)}']['full'])) for j in high] for i in high]
        H=[[exact[i+1][j+1]-sum((C[i][k]*C[k][j] for k in range(2)),n.I(0)) for j in range(2)] for i in range(2)]
        hdet=H[0][0]*H[1][1]-n.sq(H[0][1])
        assert H[0][0].l>0 and hdet.l>0
        gd=exact
        jointdet=gd[0][0]*(gd[1][1]*gd[2][2]-n.sq(gd[1][2]))-gd[0][1]*(gd[0][1]*gd[2][2]-gd[1][2]*gd[0][2])+gd[0][2]*(gd[0][1]*gd[1][2]-gd[1][1]*gd[0][2])
        assert jointdet.l>0
        u=[n.I(*map(F,z)) for z in w['measured_high_source_coordinates']]
        energy=n.I(*map(F,w['compensated_energy']))
        kappa=F(207,1000)
        P=exact[0][0]
        V=[[exact[i+1][j+1]-kappa*C[i][j] for j in range(2)] for i in range(2)]
        det=V[0][0]*V[1][1]-n.sq(V[0][1])
        assert V[0][0].l>0 and det.l>0
        z=[exact[0][i+1]-kappa*u[i] for i in range(2)]
        credit=(V[1][1]*n.sq(z[0])-2*V[0][1]*z[0]*z[1]+V[0][0]*n.sq(z[1]))/det
        assert credit.l>0
        response=(P-credit)/kappa
        coarse=P/(kappa*energy)
        refined=response/energy
        assert coarse.l>n.SCALE and refined.l>n.SCALE
        assert F(refined.h,n.SCALE)<F(coarse.l,n.SCALE)
        if w['parity']=='even':assert F(168,100)<F(refined.l,n.SCALE) and F(refined.h,n.SCALE)<F(170,100)
        else:assert F(133,100)<F(refined.l,n.SCALE) and F(refined.h,n.SCALE)<F(136,100)
        # An explicit fixed rational Y supplies an independently evaluated
        # sufficient bound; its choice is not itself a proof of optimality.
        vm=[[q.mid() for q in row] for row in V];zm=[q.mid() for q in z]
        dm=vm[0][0]*vm[1][1]-vm[0][1]**2
        yy=[(vm[1][1]*zm[0]-vm[0][1]*zm[1])/dm,
            (vm[0][0]*zm[1]-vm[0][1]*zm[0])/dm]
        y=[F((v*10**80).__floor__(),10**80) for v in yy]
        approx_norm=g[0][0]-2*sum((y[i]*g[0][i+1] for i in range(2)),n.I(0))+sum(
            (y[i]*y[j]*g[i+1][j+1] for i in range(2) for j in range(2)),n.I(0))
        assert approx_norm.l>0
        error=eta[0]+sum((abs(y[i])*eta[i+1] for i in range(2)),F(0))
        sqrt_upper=F(n.sqrt_r(F(approx_norm.h,n.SCALE)).h,n.SCALE)
        paid_upper=(sqrt_upper+error)**2
        finite=2*sum((u[i]*y[i] for i in range(2)),n.I(0))-sum(
            (y[i]*y[j]*C[i][j] for i in range(2) for j in range(2)),n.I(0))
        paid_bound=n.I(paid_upper/kappa)+finite
        assert F(paid_bound.h,energy.l)>1
        residual_ratio=P/energy
        results.append(dict(parity=w['parity'],physical_source_L2_error_bounds=list(map(str,eta)),
            original_complete_three_source_Gram=[[q.ends() for q in row] for row in exact],
            paid_Gram_entry_errors=[[str(v) for v in row] for row in errors],
            complete_residual_square_over_energy=residual_ratio.ends(),
            original_C2=[[v.ends() for v in row] for row in C],original_measured_residual_u=[v.ends() for v in u],
            measured_high_tail_Gram_H=[[v.ends() for v in row] for row in H],
            measured_high_tail_Gram_determinant=hdet.ends(),joint_source_Gram_determinant=jointdet.ends(),
            shifted_source_correlation_zbar=[v.ends() for v in z],
            positive_correlation_matrix_V=[[v.ends() for v in row] for row in V],
            V_determinant=det.ends(),correlation_credit=credit.ends(),
            correlation_credit_over_energy=(credit/energy).ends(),
            coarse_response_majorant_over_energy=coarse.ends(),
            optimal_two_mode_correlated_majorant_over_energy=refined.ends(),
            explicit_rational_Y=list(map(str,y)),explicit_Y_source_error=str(error),
            explicit_Y_combined_approximant_square=approx_norm.ends(),
            explicit_Y_paid_response_upper=str(F(paid_bound.h,n.SCALE)),
            coarse_sufficient_gate_rejected=True,optimal_two_mode_correlated_sufficient_gate_rejected=True,
            actual_original_inverse_response_evaluated=False,actual_negative_vector=False))
    return dict(milestone='NF25',status='PASS: complete native directional Gram and scoped estimator rejection',aperture='53/50',
        whole_three_source_original_Gram_certified=True,parity_certificates=results,
        full_58_source_Gram=False,whole_aperture_positive=False,RH=False,F4=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('targets');p.add_argument('gram');p.add_argument('e112');p.add_argument('first');p.add_argument('second');p.add_argument('--output',required=True);a=p.parse_args()
    raw=open(a.targets,'rb').read();assert hashlib.sha256(raw).hexdigest()=='6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00'
    targets=json.loads(raw);source={};sha=['f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81','da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee','0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad']
    for (f,k),s in zip([(a.e112,'complete_form'),(a.first,'original_full_source'),(a.second,'original_full_source')],sha):
        b=gzip.decompress(open(f,'rb').read());assert hashlib.sha256(b).hexdigest()==s;source.update(json.loads(b)[k])
    result=certify(targets,json.load(open(a.gram)),source)
    result['input_source_sha256']=sha;result['target_sha256']=hashlib.sha256(raw).hexdigest()
    result['rational_moment_Gram_sha256']=hashlib.sha256(open(a.gram,'rb').read()).hexdigest()
    open(a.output,'w').write(json.dumps(result,indent=2)+'\n')
