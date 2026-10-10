"""Exact RC23 matrix gate. Supplied whole-operator error bounds are hypotheses.

No arguments: run synthetic acceptance/rejection controls.
One JSON path: assess M,A,U,V, trial C, its cNorm bound, and nonnegative
rational errors eM,eA,eU,eV; use rational strings or integers.
This checks finite matrix inequalities, never actual Weil source attachment.
"""
from fractions import Fraction as F
import json
import sys

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(str,int)):
        raise ValueError('Use rational strings or integers, not floats.')
    return F(x)

def matrix(x,symmetric=True):
    if not isinstance(x,list) or not x: raise ValueError('Empty matrix.')
    n=len(x)
    if any(not isinstance(row,list) or len(row)!=n for row in x):
        raise ValueError('Matrix must be square.')
    out=[[rational(v) for v in row] for row in x]
    if symmetric and any(out[i][j]!=out[j][i] for i in range(n) for j in range(n)):
        raise ValueError('This real gate requires symmetric matrices.')
    return out

def shifted(A,c):
    return [[v-(c if i==j else 0) for j,v in enumerate(row)] for i,row in enumerate(A)]

def transpose(A): return [list(row) for row in zip(*A)]
def multiply(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]

def psd(A,strict=False):
    """Exact symmetric Schur elimination, including singular PSD pivots."""
    A=[row[:] for row in A]
    while A:
        pivot=A[0][0]
        if pivot<0: return False
        if pivot==0:
            if strict or any(A[0][j]!=0 for j in range(1,len(A))): return False
            A=[row[1:] for row in A[1:]]
            continue
        A=[[A[i][j]-A[i][0]*A[0][j]/pivot for j in range(1,len(A))]
           for i in range(1,len(A))]
    return True

def gram_errors(v,s,e,d):
    """v,s bound approximate feature/source maps; e,d bound their errors."""
    if min(v,s,e,d)<0: raise ValueError('Negative norm bound.')
    return {'eM':2*v*e+e*e,'eA':19*(2*v*e+e*e),
            'eU':2*s*d+d*d,'eV':v*d+s*e+e*d}

def assess(data):
    matrices={k:matrix(data[k]) for k in ['M','A','U','V']}
    M,A,U,V=[matrices[k] for k in ['M','A','U','V']]
    n=len(M)
    if any(len(x)!=n for x in matrices.values()): raise ValueError('Dimension mismatch.')
    C=matrix(data['C'],symmetric=False)
    cNorm=rational(data['cNorm'])
    if len(C)!=n or cNorm<0: raise ValueError('Bad trial coefficient/norm bound.')
    errors={k:rational(data[k]) for k in ['eM','eA','eU','eV']}
    if min(errors.values())<0: raise ValueError('Negative error bound.')
    eM,eA,eU,eV=[errors[k] for k in ['eM','eA','eU','eV']]
    m=F(1,4000); beta_sq=F(1,90000)
    metric_ok=psd(shifted(M,eM),strict=True)
    head=[[A[i][j]-m*M[i][j] for j in range(n)] for i in range(n)]
    head_ok=psd(shifted(head,eA+m*eM))
    # Certify ||C||<=cNorm using a separate exact positive block.
    norm_block=[[F(0) for _ in range(2*n)] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            norm_block[i][j]=cNorm if i==j else 0
            norm_block[i+n][j+n]=cNorm if i==j else 0
            norm_block[i][j+n]=C[i][j]
            norm_block[i+n][j]=C[j][i]
    coefficient_ok=psd(norm_block)
    VC=multiply(V,C)
    CtV=multiply(transpose(C),V)
    CtMC=multiply(multiply(transpose(C),M),C)
    # E is the Gram of sigma-R C. Orthogonal residual Gamma <= E.
    E=[[U[i][j]-VC[i][j]-CtV[i][j]+CtMC[i][j] for j in range(n)] for i in range(n)]
    source=[[beta_sq*M[i][j]-E[i][j] for j in range(n)] for i in range(n)]
    source_error=(beta_sq+cNorm*cNorm)*eM+2*cNorm*eV+eU
    source_ok=coefficient_ok and psd(shifted(source,source_error))
    return {'conditional_matrix_gate_pass':metric_ok and head_ok and source_ok,
            'metric_positive':metric_ok,'head_bound_pass':head_ok,
            'source_bound_pass':source_ok,'dimension':n,
            'matches_RC22_head_dimension':n==8600,
            'trial_coefficient_norm_pass':coefficient_ok,
            'source_residual_error_budget':str(source_error),
            'supplied_error_bounds_independently_verified':False,
            'actual_native_attachment_verified':False,
            'whole_centered_aperture_extended':False}

def controls():
    checks=0
    def check(v):
        nonlocal checks
        assert v, checks+1
        checks+=1
    check(psd([[F(1),F(0)],[F(0),F(0)]]))
    check(not psd([[F(0),F(1)],[F(1),F(0)]]))
    check(not psd([[F(1),F(2)],[F(2),F(1)]]))
    check(not psd([[F(1),F(0)],[F(0),F(0)]],strict=True))
    M=[[1,0],[0,2]]
    def fixture(leak=F(1,360000),error=F(0),head=F(2)):
        return {'M':M,'A':[[str(head),0],[0,str(2*head)]],
                'V':[[str(head-1),0],[0,str(2*(head-1))]],
                'U':[[str((head-1)**2+leak),0],[0,str(2*((head-1)**2+leak))]],
                'C':[[str(head-1),0],[0,str(head-1)]],'cNorm':str(abs(head-1)),
                'eM':str(error),'eA':str(error),'eU':str(error),'eV':str(error)}
    good=assess(fixture())
    check(good['conditional_matrix_gate_pass'])
    check(not good['matches_RC22_head_dimension'])
    check(not good['whole_centered_aperture_extended'])
    check(assess(fixture(error=F(1,10**9)))['conditional_matrix_gate_pass'])
    bad=assess(fixture(leak=F(1,10000)))
    check(bad['head_bound_pass'] and not bad['source_bound_pass'])
    check(not bad['conditional_matrix_gate_pass'])
    check(not assess(fixture(error=F(1,100)))['conditional_matrix_gate_pass'])
    check(not assess(fixture(head=F(-1)))['head_bound_pass'])
    underreported=fixture()
    underreported['cNorm']='1/2'
    check(not assess(underreported)['trial_coefficient_norm_pass'])
    singular=fixture()
    singular['M']=[[0,0],[0,2]]
    check(not assess(singular)['metric_positive'])
    bounds=gram_errors(F(2),F(3),F(1,1000),F(1,500))
    check(bounds['eM']==F(4001,1000000))
    check(bounds['eA']==19*bounds['eM'])
    check(bounds['eU']==F(3001,250000))
    check(bounds['eV']==F(3501,500000))
    for bad_value in [0.01,True]:
        try: rational(bad_value)
        except ValueError: check(True)
        else: check(False)
    try: matrix([[1,2],[0,1]])
    except ValueError: check(True)
    else: check(False)
    check(F(1,4000)-F(1,8892)==F(1223,8892000)>0)
    return {'milestone':'RC23','status':'PASS','exact_controls':checks,
            'controls_are_synthetic':True,'actual_RC22_matrices_evaluated':False,
            'whole_centered_aperture_extended':False,'RH':False,'F4':False,'Lean':False}

if __name__=='__main__':
    try:
        result=controls() if len(sys.argv)==1 else assess(json.load(open(sys.argv[1])))
        print(json.dumps(result,indent=2))
        if not result.get('conditional_matrix_gate_pass',result.get('status')=='PASS'): sys.exit(1)
    except (ValueError,KeyError,TypeError,ZeroDivisionError) as error:
        print(json.dumps({'status':'REJECT','reason':str(error)}))
        sys.exit(1)
