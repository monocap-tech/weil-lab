#!/usr/bin/env python3
"""Actual near-critical first-boundary-invisible vectors, original Q.
Decimal linear algebra proposes rational seeds only; Fraction intervals prove
existence of exact source-zero vectors via a tiny true-native correction.
"""
import argparse,gzip,hashlib,json
from decimal import Decimal as D,localcontext
from fractions import Fraction as F
from certify_native_collective_boundary_cc53 import OLD_SHA,NEW_SHA,read

WITNESS_SHA='b3e23133db4562c1b28816e922f9c085899818399dcfcee74a323b4f6da10d5c'
DEN=10**80
def interval(p):return tuple(map(F,p['full']))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def bound(a):return max(abs(a[0]),abs(a[1]))
def dec(x):return D(x.numerator)/D(x.denominator)

def propose(A,b,w):
    with localcontext() as ctx:
        ctx.prec=120
        m=[[dec((v[0]+v[1])/2) for v in row] for row in A]
        rhs=[dec((v[0]+v[1])/2) for v in b];bc=rhs[:]
        for k in range(56):
            assert m[k][k]>0
            for i in range(k+1,56):
                z=m[i][k]/m[k][k];rhs[i]-=z*rhs[k]
                for j in range(k+1,56):m[i][j]-=z*m[k][j]
        v=[D(0)]*56
        for i in range(55,-1,-1):v[i]=(rhs[i]-sum(m[i][j]*v[j] for j in range(i+1,56)))/m[i][i]
        beta=sum(bc[i]*dec(w[i]) for i in range(56))/sum(bc[i]*v[i] for i in range(56))
        return [int((dec(w[i])-beta*v[i])*D(DEN)) for i in range(56)]

def certify(old_path,new_path,witness_path,seed_path=None):
    old=read(old_path,OLD_SHA);new=read(new_path,NEW_SHA)
    raw=open(witness_path,'rb').read();assert hashlib.sha256(raw).hexdigest()==WITNESS_SHA
    witness=json.loads(raw)
    assert old['aperture']==new['aperture']=='53/50'
    assert new['parent_sha256']==OLD_SHA and witness['parent_source']==OLD_SHA
    saved=json.load(open(seed_path)) if seed_path else None
    if saved:assert saved['coefficient_denominator']==str(DEN)
    seeds={'coefficient_denominator':str(DEN),'classification':'rational candidate seeds only; exact invisible vectors require the defined true-native correction','parities':{}}
    results=[]
    for parity,j,name,normfloor,qfloor,rayceil in [(0,112,'even',F(9,10),F(8,10**35),F(1,10**34)),(1,113,'odd',F(4,5),F(3,10**31),F(4,10**31))]:
        ix=list(range(parity,112,2));p=110+parity
        A=[[interval(old['complete_form'][f'{min(i,k)},{max(i,k)}']) for k in ix] for i in ix]
        b=[interval(new['original_full_source'][f'{i},{j}']) for i in ix]
        w=[F(int(s),int(witness['coefficient_denominator'])) for s in witness['witnesses'][name]['numerators']]
        nums=list(map(int,saved['parities'][name]['numerators'])) if saved else propose(A,b,w)
        if saved:assert saved['parities'][name]['indices']==ix
        assert len(nums)==56
        z=[F(n,DEN) for n in nums]
        norm=sum(v*v for v in z)
        q=(F(0),F(0));bz=(F(0),F(0));mixed=(F(0),F(0))
        for k in range(56):
            bz=add(bz,scale(b[k],z[k]));mixed=add(mixed,scale(A[k][-1],z[k]))
            for l in range(k,56):q=add(q,scale(A[k][l],z[k]*z[l]*(1 if k==l else 2)))
        assert b[-1][0]>(F(2,5) if parity==0 else F(1,2))
        delta=bound(bz)/b[-1][0]
        assert delta<F(1,10**63)
        # z_true=z-delta_true e_p; delta_true=Q(z,phi)/Q(e_p,phi).
        # This EXACT unknown native ratio is bounded above, never set to its midpoint.
        mass_lower=norm-2*delta*abs(z[-1])
        q_upper=q[1]+2*delta*bound(mixed)+delta**2*bound(A[-1][-1])
        q_lower=q[0]-2*delta*bound(mixed)-delta**2*bound(A[-1][-1])
        assert normfloor<mass_lower<=norm<1
        assert q_lower>qfloor and q_upper/mass_lower<rayceil
        # A two-plane min-max certificate concerns ACTUAL retained A eigenvectors,
        # not eigenvectors of the full infinite Q operator.
        qw=(F(0),F(0));qzw=(F(0),F(0))
        for k in range(56):
            for l in range(56):
                qw=add(qw,scale(A[k][l],w[k]*w[l]))
                qzw=add(qzw,scale(A[k][l],z[k]*w[l]))
        ww=sum(v*v for v in w);zw=sum(u*v for u,v in zip(z,w))
        spectral_ceiling=F(1,10**26) if parity==0 else F(1,10**23)
        k00=spectral_ceiling*ww-qw[1]
        k11=spectral_ceiling*norm-q[1]
        k01=(spectral_ceiling*zw-qzw[1],spectral_ceiling*zw-qzw[0])
        assert k00>0 and k11>0 and k00*k11>bound(k01)**2
        seeds['parities'][name]={'indices':ix,'numerators':[str(n) for n in nums],'correction_degree':p,'boundary_degree':j}
        results.append(dict(parity=name,rational_seed_mass=str(norm),
            seed_original_energy_interval=[str(v) for v in q],
            seed_boundary_pairing_interval=[str(v) for v in bz],
            true_correction_absolute_upper=str(delta),
            certified_correction_upper='1/10^63',
            exact_corrected_mass_lower=str(normfloor),
            original_corrected_energy_lower=str(qfloor),
            physical_Rayleigh_strict_upper=str(rayceil),
            retained_spectral_ceiling=str(spectral_ceiling),
            retained_spectral_subspace_dimension_at_least=2,
            two_plane_minmax_determinant_lower=str(k00*k11-bound(k01)**2),
            exact_first_boundary_source_zero=True,
            original_energy_strict_positive=True,
            complete_high_source_zero=False,actual_original_null=False))
    return seeds,dict(status='PASS',milestone='CC54',aperture='53/50',
        source_sha256={'E112':OLD_SHA,'boundary':NEW_SHA,'NF18_witness':WITNESS_SHA},
        proof_arithmetic='Fraction intervals on authenticated full signed sources; Decimal is candidate generation only',
        parities=results,actual_nearcritical_first_boundary_invisible_vectors=True,
        observed_first_mode_lower_frame_bound_possible_on_all_E112=False,
        complete_high_response_evaluated=False,CC52_carrier_transfer=False,
        whole_original_aperture_positive=False,RH=False,Lean=False)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('old');p.add_argument('boundary');p.add_argument('witness')
    p.add_argument('--seeds');p.add_argument('--write-seeds');p.add_argument('--output');a=p.parse_args()
    seeds,result=certify(a.old,a.boundary,a.witness,a.seeds)
    if a.write_seeds:open(a.write_seeds,'w').write(json.dumps(seeds,indent=2)+'\n')
    out=json.dumps(result,indent=2)+'\n'
    if a.output:open(a.output,'w').write(out)
    print(json.dumps({'status':result['status'],'parities':[{k:v for k,v in r.items() if k in ['parity','certified_correction_upper','exact_corrected_mass_lower','original_corrected_energy_lower','physical_Rayleigh_strict_upper','exact_first_boundary_source_zero']} for r in result['parities']]},indent=2))
