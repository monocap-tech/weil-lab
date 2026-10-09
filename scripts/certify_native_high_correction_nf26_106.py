#!/usr/bin/env python3
"""NF26: certify one fixed rational high correction via complete source moments.
Diagnostic coefficients choose a trial only. All conclusions use outward
rational moments, the authenticated NF24 energy and paid physical errors.
"""
import argparse,json,hashlib
from fractions import Fraction as F
from math import factorial
import certify_native_correlated_sources_nf25_106 as n

DIGITS=500
n.SCALE=10**DIGITS
n.native.GRID=n.SCALE

def logunit(q):
    z=(q-1)/(q+1);assert z.absupper()<F(1,2)
    power=z;total=n.I(0)
    for k in range(800):total+=2*power/F(2*k+1);power=power*z*z
    za=z.absupper();rem=2*power.absupper()/F(1601)/(1-za*za)
    return total+n.I(-rem,rem)
n.log_unit=logunit

def constants():
    pi=n.ni(16*n.native.atan(F(1,5),terms=350)-4*n.native.atan(F(1,239),terms=350))
    B=n.native.bern(402);m=400
    gamma=n.I(sum((F(1,k) for k in range(1,m+1)),F(0))-F(1,2*m))-n.ni(n.native.log(m))
    for k in range(1,201):gamma+=B[2*k]/F(2*k*m**(2*k))
    rem=abs(B[402])/F(402*m**402);gamma+=n.I(-rem,rem)
    return -gamma-n.logi(2*pi),pi

def source(ids,coeff,c,parity):
    p=n.physical(ids,coeff)
    poly=n.add(n.scale(p,c),n.add(n.singular(p),n.scale(n.convolution(p),-1)))
    m=sum((F(v)*n.sqrt_r(F(2*i+1)/(2*n.A))*n.pole_moment(i) for i,v in zip(ids,coeff)),n.I(0))
    pole=[n.I(0)]*41
    for k in range(0 if parity=='even' else 1,41,2):pole[k]=2*(1 if parity=='even' else -1)*m/F(2**k*factorial(k))
    return p,n.add(poly,pole),n.scale(p,F(-1,2))

def run(targets,trial,projection_certificate):
    c,pi=constants();powers=(2,3,4,5,7,8)
    logs={k:n.ni(n.native.log(k)) for k in powers}
    shifts=[(s*logs[k],(logs[2] if k in (4,8) else logs[k])/n.sqrt_r(F(k))) for k in powers for s in (1,-1)]
    cuts=[n.I(-n.A),n.I(n.A)]+[n.I(n.A)-t if t.l>0 else n.I(-n.A)-t for t,w in shifts]
    cuts.sort(key=lambda v:v.l);assert all(l.h<u.l for l,u in zip(cuts,cuts[1:]))
    epsilon=4*F(106,125)**320/(1-F(106,125));pole_rem=2*(n.A/2)**41/F(factorial(41))
    # exp(a/2) < 7/4 by a positive-series geometric tail. Hence the
    # pole-source remainder factor 4a exp(a/2) is strictly below eight.
    z=n.A/2
    assert 1+z+z*z/(2*(1-z/3))<F(7,4) and 7*n.A<8
    eta_unit=2*n.A*epsilon+8*pole_rem
    result=[]
    for row,rr in zip(targets['authenticated_compensated_targets'],trial['parities']):
        parity=row['parity'];assert rr['parity']==parity
        ids=row['retained_indices']+row['high_indices'];coeff=row['retained_coefficients']+row['exact_rational_high_compensation']
        assert sum(F(v)**2 for v in coeff)<F(1001,1000)**2
        yi=rr['high_indices'];yc=list(map(F,rr['rational_correction_coefficients']))
        assert all(i>=112 and i%2==(0 if parity=='even' else 1) for i in yi)
        assert len(set(yi))==len(yi)==len(yc)
        ym=F(n.sqrt_r(sum(v*v for v in yc)).h,n.SCALE)
        physical=[];poly=[];lp=[]
        for i,v in [(ids,coeff),(yi,yc)]:
            p,b,l=source(i,v,c,parity);physical.append(p);poly.append(b);lp.append(l)
        print(parity,'constructed both sources',flush=True)
        degree=2*max(len(p)-1 for p in poly)
        M,ML,ML2,cellmom=n.moments(cuts,degree,c,pi)
        print(parity,'constructed exact endpoint moments',flush=True)
        cell=[]
        for L,U in zip(cuts,cuts[1:]):
            mid=F(L.h+U.l,2*n.SCALE);active=[]
            for t,w in shifts:
                z=n.I(mid)+t
                inside=-n.A<F(z.l,n.SCALE) and F(z.h,n.SCALE)<n.A
                outside=F(z.h,n.SCALE)<-n.A or F(z.l,n.SCALE)>n.A
                assert inside or outside
                if inside:active.append((t,w))
            cell.append([sum_polys([n.scale(n.shifted(p,t),-w) for t,w in active]) for p in physical])
        print(parity,'constructed all thirteen prime cells',flush=True)
        def pairing(col,test):
            v=n.dot(poly[col],test,M)+n.dot(lp[col],test,ML)
            for pp,(mp,ml) in zip(cell,cellmom):v+=n.dot(pp[col],test,mp)
            return v
        checks=[]
        independent=next(v for v in projection_certificate['original_native_projection_certificates'] if v['parity']==parity)
        for degree,expected in list(zip(row['high_indices'],row['measured_high_source_coordinates']))+[(independent['projection_degree'],independent['original_native_source_pairing'])]:
            measured=pairing(0,n.basis(degree))
            paid=measured+n.I(-F(1001,1000)*eta_unit,F(1001,1000)*eta_unit)
            original=n.I(*map(F,expected))
            assert paid.l<=original.h and paid.h>=original.l
            checks.append(dict(degree=degree,reconstructed_pairing=measured.ends(),original_pairing=original.ends(),overlap_after_paid_error=True))
        # Exact native q is never inferred by integrating the unit-norm p
        # against an approximate source at its 1e-35 cancellation scale.
        cross=pairing(0,physical[1]);yy=pairing(1,physical[1])
        true_cross=cross+n.I(-F(1001,1000)*eta_unit*ym,F(1001,1000)*eta_unit*ym)
        true_yy=yy+n.I(-eta_unit*ym*ym,eta_unit*ym*ym)
        transpose=pairing(1,physical[0])+n.I(-F(1001,1000)*eta_unit*ym,F(1001,1000)*eta_unit*ym)
        assert true_cross.l<=transpose.h and true_cross.h>=transpose.l
        q=n.I(*map(F,row['compensated_energy']));newq=q-2*true_cross+true_yy
        assert newq.l>0
        # Project Ly using its rational moment coordinates; pay its source
        # error in norm, so PE projection contributes no dimension factor.
        lowcoords=[pairing(1,n.basis(i)) for i in row['retained_indices']]
        print(parity,'computed all retained correction coordinates',flush=True)
        ycenters=[v.mid() for v in lowcoords]
        yproj=n.physical(row['retained_indices'],ycenters)
        yround=8*max(F(v.h-v.l,2*n.SCALE) for v in lowcoords)
        pcoords=[n.I(*map(F,z)) for z in row['low_source_coordinates']]
        pproj=n.physical(row['retained_indices'],[v.mid() for v in pcoords])
        pround=8*max(F(v.h-v.l,2*n.SCALE) for v in pcoords)
        b=n.add(n.add(poly[0],n.scale(poly[1],-1)),n.add(n.scale(pproj,-1),yproj))
        l=n.add(lp[0],n.scale(lp[1],-1))
        norm=n.dot(b,b,M)+2*n.dot(b,l,ML)+n.dot(l,l,ML2)
        for pp,(mp,ml) in zip(cell,cellmom):
            prime=n.add(pp[0],n.scale(pp[1],-1))
            norm+=2*n.dot(b,prime,mp)+n.dot(prime,prime,mp)+2*n.dot(l,prime,ml)
        assert norm.l>0
        # p: paid retained midpoint error; y: orthogonal projection is a
        # contraction, plus fixed rational coordinate rounding.
        eta=F(1001,1000)*eta_unit+pround+ym*eta_unit+yround
        upper=(F(n.sqrt_r(F(norm.h,n.SCALE)).h,n.SCALE)+eta)**2
        lowerroot=max(F(0),F(n.sqrt_r(F(norm.l,n.SCALE)).l,n.SCALE)-eta)
        true_norm=n.I(lowerroot**2,upper)
        ratio=true_norm/(F(207,1000)*newq)
        score=newq-true_norm/F(207,1000)
        print(parity,'certified response ratio',float(F(ratio.l,n.SCALE)),float(F(ratio.h,n.SCALE)),flush=True)
        result.append(dict(parity=parity,correction_norm_upper=str(ym),original_cross_Q_p_y=true_cross.ends(),original_correction_energy=true_yy.ends(),
            independent_original_native_pairing_checks=checks,transpose_cross_Q_y_p=transpose.ends(),paid_bilinear_symmetry_check=True,
            corrected_native_energy=newq.ends(),retained_approximant_Ly_coordinates=[v.ends() for v in lowcoords],
            reconstructed_corrected_residual_square=norm.ends(),physical_residual_error_upper=str(eta),
            complete_original_corrected_residual_square=true_norm.ends(),coarse_response_over_corrected_energy=ratio.ends(),
            sufficient_directional_Schur_lower=score.ends(),directional_sufficient_gate_passed=score.l>0,
            directional_sufficient_gate_rejected=ratio.l>n.SCALE,whole_aperture_positive=False))
    return dict(milestone='NF26',aperture='53/50',interval_grid_digits=DIGITS,regular_kernel_N=320,pole_degree=40,original_translation_cells=13,
        diagnostic_data_used_only_to_choose_fixed_rational_trial=True,parity_certificates=result,
        whole_aperture_positive=False,full_residual_Gram=False,RH=False,F4=False,Lean=False)

def sum_polys(pp):
    ans=[n.I(0)]
    for p in pp:ans=n.add(ans,p)
    return ans

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('targets');a.add_argument('trial');a.add_argument('projection_certificate');a.add_argument('--output',required=True);a=a.parse_args()
    raw=open(a.targets,'rb').read();assert hashlib.sha256(raw).hexdigest()=='6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00'
    traw=open(a.trial,'rb').read();praw=open(a.projection_certificate,'rb').read()
    assert hashlib.sha256(praw).hexdigest()=='2483ad7fb07bfdacc846faf4b6926e27178203f8ca58d51c1d89232209d0bae2'
    res=run(json.loads(raw),json.loads(traw),json.loads(praw));res['authenticated_target_sha256']=hashlib.sha256(raw).hexdigest();res['fixed_trial_sha256']=hashlib.sha256(traw).hexdigest();res['projection_certificate_sha256']=hashlib.sha256(praw).hexdigest()
    open(a.output,'w').write(json.dumps(res,indent=2)+'\n')
