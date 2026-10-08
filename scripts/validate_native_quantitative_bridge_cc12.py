"""Exact complete-source bridge, conditioning, crossing and actual residual gate."""
from validate_native_two_retained_block_cc9 import mm,tr,minus
from validate_native_two_trial_solve_cc8 import F,solve
from validate_native_odd_enlargement_cc10 import det
from itertools import combinations
from pathlib import Path
import json,hashlib,gzip,sys
sys.set_int_max_str_digits(0)

def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def inv(A):return tr([solve(A,[F(i==j) for i in range(len(A))]) for j in range(len(A))])
def plus(A,B):return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def scale(A,t):return [[t*x for x in r] for r in A]
def ia(a,b):return (a[0]+b[0],a[1]+b[1])
def im(a,b):
    q=[x*y for x in a for y in b];return min(q),max(q)
def isn(a):return -a[1],-a[0]
def idiv(a,b):
    assert b[0]>0;return im(a,(1/b[1],1/b[0]))
def ip(x):return tuple(map(F,x))
def encloses(stored,computed):return F(stored[0])<=computed[0]<=computed[1]<=F(stored[1])
def psd(A):
    return all(det([[A[i][j] for j in s] for i in s])>=0 for k in range(1,len(A)+1) for s in combinations(range(len(A)),k))
def inertia(A):
    A=[r[:] for r in A];pos=neg=zero=0
    while A:
        n=len(A);p=next((i for i in range(n) if A[i][i]!=0),None)
        if p is not None:
            a=A[p][p];pos+=int(a>0);neg+=int(a<0)
            r=[i for i in range(n) if i!=p]
            A=[[A[i][j]-A[i][p]*A[p][j]/a for j in r] for i in r]
        else:
            pair=next(((i,j) for i in range(n) for j in range(i) if A[i][j]!=0),None)
            if pair is None:zero+=n;break
            p,q=pair;b=A[p][q];pos+=1;neg+=1
            r=[i for i in range(n) if i not in pair]
            A=[[A[i][j]-(A[i][p]*A[q][j]+A[i][q]*A[p][j])/b for j in r] for i in r]
    return pos,neg,zero

def bridge(P,N,E,Fc):
    PE=mm(P,E);PF=mm(P,Fc);NE=mm(N,E);NF=mm(N,Fc)
    L=mm(tr(PF),PF);C=minus(L,mm(tr(NF),NF));assert psd(C) and det(C)>0
    qp=minus(mm(tr(PF),PE),mm(tr(NF),NE))
    WP=minus(E,mm(Fc,mm(inv(L),mm(tr(PF),PE))))
    WQ=minus(E,mm(Fc,mm(inv(C),qp)))
    MP=mm(tr(mm(P,WP)),mm(P,WP));Y=mm(N,WP)
    D0=minus(eye(len(N)),mm(NF,mm(inv(L),tr(NF))))
    assert inv(D0)==plus(eye(len(N)),mm(NF,mm(inv(C),tr(NF))))
    S=minus(minus(mm(tr(PE),PE),mm(tr(NE),NE)),mm(tr(qp),mm(inv(C),qp)))
    assert S==minus(MP,mm(tr(Y),mm(inv(D0),Y)))
    assert WQ==plus(WP,mm(Fc,mm(inv(L),mm(tr(NF),mm(N,WQ)))))
    assert mm(tr(PF),mm(P,WP))==[[F(0)]*len(E[0]) for _ in range(len(Fc[0]))]
    Q=minus(mm(tr(P),P),mm(tr(N),N))
    assert mm(tr(Fc),mm(Q,WQ))==[[F(0)]*len(E[0]) for _ in range(len(Fc[0]))]
    Dout=minus(eye(len(N)),mm(N,mm(inv(mm(tr(P),P)),tr(N))))
    assert Dout==minus(D0,mm(Y,mm(inv(MP),tr(Y))))
    assert inertia(S)[1:]==inertia(Dout)[1:]
    c=det(C)/(C[0][0]+C[1][1]);mp2=sum((x*x for r in P for x in r),F(0))
    assert psd(minus(D0,scale(eye(len(N)),c/mp2)))
    return S,Dout

def controls():
    cases=positive=negative=0
    P=[[F(2),F(1,4),F(0),F(1,3),F(0)],
       [F(0),F(2),F(1,5),F(0),F(1,4)],
       [F(0),F(0),F(2),F(1,7),F(1,6)],
       [F(0),F(0),F(0),F(2),F(1,3)],
       [F(0),F(0),F(0),F(0),F(2)]]
    Fc=[[F(0),F(0)] for _ in range(3)]+eye(2)
    for k in (F(1,2),F(1),F(2),F(3)):
        for f in (F(1,5),F(1,3)):
            N=[[k,F(1,3),F(0),f,F(0)],
               [F(0),k/2,F(1,5),F(0),f],
               [F(1,5),F(0),k/3,f/2,f/3]]
            for basis in (eye(3),[[F(1),F(1,3),F(0)],[F(0),F(2),F(1,4)],[F(0),F(0),F(1)]]):
                E=basis+[[F(0)]*3 for _ in range(2)]
                S,Dout=bridge(P,N,E,Fc);cases+=1
                if inertia(S)[1]:negative+=1
                else:positive+=1
    # A true finite matrix source family crosses with protected D0=1.
    sigma=F(1,10**32);root=F(1,10**16);crossing=0
    for k in (F(0),F(1),F(-1,3)):
        old=sigma
        for j in range(1,9):
            u=1-F(1,2**j);new=sigma*(1-u*u)
            assert 0<new<old;old=new;crossing+=1
        for u in (F(0),F(1,2),F(1),F(3,2)):
            P2=[[root,F(0)],[k,F(1)]];N2=[[root*u,F(0)]]
            Q=minus(mm(tr(P2),P2),mm(tr(N2),N2))
            S=Q[0][0]-Q[0][1]**2/Q[1][1]
            assert S==sigma*(1-u*u) and Q[1][1]==1
            # Positive lift is (1,-k), M=sigma, Y=root*u, D0=1.
            assert S==sigma-(root*u)**2;crossing+=1
    # Shifted unit contact is a positive ORIGINAL physical eigenmode.
    P2=[[root,F(0)],[F(0),F(1)]];N0=[[F(0),F(0)]]
    Q0=minus(mm(tr(P2),P2),mm(tr(N0),N0));Nshift=N0+[[root,F(0)],[F(0),root]]
    shifted=minus(mm(tr(P2),P2),mm(tr(Nshift),Nshift))
    assert Q0[0][0]==sigma>0 and shifted[0][0]==0 and shifted[1][1]==1-sigma
    # Actual critical representer -> Q graph, including the entire incoming
    # source-orthogonal shell. Gap-small graph error does not suppress L.
    critical=0
    for j in range(1,13):
        k=1-F(1,2**j);r=3*k/5;b=4*k/5;lam=k*k;gap=1-lam;C=1-b*b
        Z=[r/lam,b/lam];graph=[Z[0],r*b*Z[0]/C]
        error=[Z[i]-graph[i] for i in range(2)]
        assert error==[F(0),gap*b/(lam*C)]
        assert r*Z[0]+b*Z[1]==1
        incoming=F(1,10)
        qgraphincoming=-(r*graph[0]+b*graph[1])*incoming
        qerrorincoming=-b*error[1]*incoming
        assert -(qgraphincoming+qerrorincoming)==incoming
        assert gap-incoming*incoming==1-lam-incoming*incoming
        if j>=8:assert gap-incoming*incoming<0
        critical+=1
    # Same physical Q, arbitrarily different source-relative conditioning.
    conditioning=0
    for k in (F(0),F(1),F(10),F(100)):
        Padd=[[F(2),F(0)],[F(0),F(1)],[k,F(0)]]
        Nadd=[[F(1),F(0)],[k,F(0)]]
        Qadd=minus(mm(tr(Padd),Padd),mm(tr(Nadd),Nadd))
        assert Qadd==[[F(3),F(0)],[F(0),F(1)]]
        Mret=4+k*k;reaction=1+k*k
        assert Mret-reaction==3 and 1-reaction/Mret==3/Mret
        conditioning+=1
    # Replay the existing exact loss/prime/mass controls WITHOUT rewriting them.
    from validate_native_arithmetic_relative_loss_cc4 import run
    cc4=run();assert cc4['all_passed']
    return dict(complete_mixed_covariance_bridge_cases=cases,positive_cases=positive,
        negative_cases=negative,protected_source_crossing_checks=crossing,
        critical_graph_and_entire_incoming_shell_controls=critical,
        unchanged_physical_form_source_conditioning_controls=conditioning,
        original_positive_eigenmode_shift_control=True,cc4_replayed_exact_controls=cc4['exact_checks'],
        cc4_control_counts=cc4['counts'])

def run():
    checks=controls();root=Path(__file__).resolve().parents[1]/'notes/data'
    d=json.loads((root/'RPB108_QUANTITATIVE_BRIDGE_CC12_CERTIFICATE_20261008.json').read_text())
    for k,p in {'cc3':'RPB108_COUPLED_TRIAL_CC3_CERTIFICATE_20261008.json',
                'cc9':'RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json',
                'cc10':'RPB108_ODD_ENLARGEMENT_CC10_CERTIFICATE_20261008.json',
                'cc11':'RPB108_ODD_BATCH_CC11_CERTIFICATE_20261008.json',
                'saved':'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json'}.items():
        assert hashlib.sha256((root/p).read_bytes()).hexdigest()==d['input_sha256'][k]
    G=[list(map(F,r)) for r in d['three_plane_deterministic_lower']]
    previous=json.loads((root/'RPB108_ODD_ENLARGEMENT_CC10_CERTIFICATE_20261008.json').read_text())
    block=previous['original_completed_schur_lower_block'];s=[F(10**16),F(1),F(1)];grid=10**100
    centres=[[F((((F(x[0])+F(x[1]))*s[i]*s[j]/2)*grid).__floor__(),grid) for j,x in enumerate(row)] for i,row in enumerate(block)]
    rad=max(sum((max(centres[i][j]-F(x[0])*s[i]*s[j],F(x[1])*s[i]*s[j]-centres[i][j]) for j,x in enumerate(row)),F(0)) for i,row in enumerate(block))
    pad=F((rad*grid).__ceil__(),grid)
    assert pad==F(d['scaled_whole_row_radius'])
    assert G==[[(centres[i][j]-(pad if i==j else 0))/(s[i]*s[j]) for j in range(3)] for i in range(3)]
    assert G[1][2]==G[2][1]==0 and G[1][1]>0 and G[2][2]>0
    rho=solve([r[1:] for r in G[1:]],G[0][1:]);ell=G[0][0]-sum((G[0][i+1]*rho[i] for i in range(2)),F(0))
    assert rho==list(map(F,d['recomputed_weak_shear'])) and ell==F(d['recomputed_weak_margin'])>0
    cc9=json.loads((root/'RPB108_TWO_RETAINED_BLOCK_CC9_CERTIFICATE_20261008.json').read_text())
    Gram=[[(F(0),F(0)) for _ in range(3)] for _ in range(3)]
    for i in range(2):
        for j in range(2):Gram[i][j]=ip(cc9['actual_retained_source_gram'][i][j])
    Gram[2][2]=ip(previous['odd_projected_source_norm_squared'])
    beta=F(previous['whole_mixed_source_cross_bound']);Gram[0][2]=Gram[2][0]=(-beta,beta)
    w=[F(1),-rho[0],-rho[1]];qs=(F(0),F(0))
    for i in range(3):
        for j in range(3):qs=ia(qs,im((w[i]*w[j],)*2,Gram[i][j]))
    assert encloses(d['weak_source_norm_squared'],qs)
    A=[[ip(x) for x in row] for row in cc9['trial_action_gram']]
    V=[ia(ip(row[0]),im((-rho[0],)*2,ip(row[1]))) for row in cc9['mixed_trial_action']]
    assert all(encloses(saved,actual) for saved,actual in zip(d['weak_trial_action_cross'],V))
    den=ia(im(A[0][0],A[1][1]),isn(im(A[0][1],A[1][0])));assert den[0]>0
    numerator=ia(im(A[1][1],im(V[0],V[0])),im(A[0][0],im(V[1],V[1])))
    numerator=ia(numerator,isn(im((F(2),F(2)),im(A[0][1],im(V[0],V[1])))))
    residual_min=ia(qs,isn(idiv(numerator,den)))
    assert residual_min[0]>F(24,10**33) and encloses(d['minimum_residual_in_two_trial_action_span'],residual_min)
    t=list(map(F,d['original_trial_coefficients']));actualres=qs
    for i in range(2):actualres=ia(actualres,im((-2*t[i],)*2,V[i]))
    for i in range(2):
        for j in range(2):actualres=ia(actualres,im((t[i]*t[j],)*2,A[i][j]))
    assert encloses(d['actual_trial_residual_norm_squared'],actualres)
    assert F(d['minimum_residual_in_two_trial_action_span'][0])>0
    M=F(d['complete_retained_source_map_upper']);c=F(d['original_complement_lower'])
    floor=M*M*F(d['minimum_residual_in_two_trial_action_span'][0])/(c*c*ell)
    assert floor==F(d['any_two_trial_absolute_residual_template_budget_floor'])
    assert floor>F(194) and floor>F(d['quotient_native_rayleigh_upper_for_exact_schur'][1])
    assert F(d['minimum_residual_in_two_trial_action_span'][0])>F(24,10**33)
    assert F(d['quotient_native_rayleigh_upper_for_exact_schur'][1])<F(241,1000)
    r=list(map(F,d['physical_109_quotient_test_vector']))
    saved=json.loads((root/'RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json').read_text());v=list(map(F,saved['rational_coefficient_witness']))
    assert r[0]==r[1]==0 and sum((a*b for a,b in zip(r,v)),F(0))==0
    assert sum((x*x for x in r),F(0))==F(d['quotient_test_mass'])>0
    raw=gzip.decompress((root/'RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz').read_bytes())
    assert hashlib.sha256(raw).hexdigest()==d['input_sha256']['native']
    triangle=json.loads(raw)['lower_triangle_row_major'];qlo=qhi=F(0);index=0
    for i in range(112):
        for j in range(i+1):
            lo,hi=map(lambda x:F(int(x),10**80),triangle[index]);index+=1
            factor=r[i]*r[j]*(1 if i==j else 2)
            qlo+=factor*(lo if factor>=0 else hi);qhi+=factor*(hi if factor>=0 else lo)
    mass=F(d['quotient_test_mass']);qlo/=mass;qhi/=mass
    reported=d['quotient_native_rayleigh_upper_for_exact_schur']
    assert F(reported[0])<=qlo<=qhi<=F(reported[1])
    allowance=F(d['correlated_residual_weak_row_allowance']);head=F(d['correlated_trial_native_weak_row_norm_upper'])
    residual_bound=(allowance-head)*c/M
    assert residual_bound>=0 and residual_bound**2>=F(d['actual_trial_residual_norm_squared'][1])
    assert allowance**2/ell==F(d['correlated_residual_weak_reaction_budget'])
    assert F(d['correlated_residual_weak_reaction_budget'])<F(d['recomputed_absolute_weak_reaction_budget'])
    assert len(d['whole_112_correlated_trial_native_weak_row'])==112
    assert len(d['whole_112_trial_native_rows'])==2 and all(len(r)==112 for r in d['whole_112_trial_native_rows'])
    assert d['native_row_storage_grid_digits']==100
    allpairs=d['whole_112_correlated_trial_native_weak_row']+[x for row in d['whole_112_trial_native_rows'] for x in row]
    assert all((F(endpoint)*10**100).denominator==1 for pair in allpairs for endpoint in pair)
    rowmass=sum((max(map(abs,map(F,x)))**2 for x in d['whole_112_correlated_trial_native_weak_row']),F(0))
    assert head*head>=rowmass
    assert d['independent_trial_row_overlap_audits']==64
    assert d['all_prime_powers']==[2,3,4,5,7,8] and d['both_signed_poles']
    assert d['classification']=='C' and not d['new_whole_matrix_sign'] and not d['arithmetic_nondivergence']
    return {'passed':True,**checks,'independent_actual_trial_row_overlap_audits':64,
        'three_plane_metric_recomputed':True,'entire_109_quotient_uniform_residual_template_obstructed':True,
        'classification':'C','nonpositive_dimension_upper_preserved':107,
        'certified_whole_aperture_preserved':'1','global_or_paused_refs_modified':False}

if __name__=='__main__':print(json.dumps(run(),indent=2))
