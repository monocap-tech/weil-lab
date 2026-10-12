"""RC156: direct psi/delta trial Gram and mixed source pairings."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from validate_rpb108_rc127_enriched_even_endpoint_action import B,Z,rat,plus,bounds,up,down,sqrtup,ser
from validate_rpb108_rc134_correlated_six_input_covariance import smul

def reconstruct(name,cut,paths,reverse):
    path=Path(__file__).with_name(name);src=path.read_text();ns={}
    exec(compile(src[:src.index(cut)]+'\n    return locals()\n','RC156-'+name,'exec'),ns)
    return ns['run'](paths,reverse)

def run(paths,reverse=False):
    raw=[Path(p).read_bytes() for p in paths];data=list(map(json.loads,raw))
    psi,delta,interface,joint,old,cov,balanced,capture,conditional=data
    assert [d['milestone'] for d in data]==['RC154','RC153','RC155','RC129','RC130','RC134','RC132','RC131','RC151']
    hashes=[hashlib.sha256(b).hexdigest() for b in raw]
    assert psi['input_sha256']==[hashes[i] for i in (3,4,8,1)]
    assert interface['input_sha256'][3:]==[hashes[0],hashes[1]]
    assert delta['input_sha256']==[hashes[i] for i in (3,6,7,5,8)]+[hashlib.sha256(Path(paths[4]).with_name('rpb108_rc152_complement_action_budget.json').read_bytes()).hexdigest()]
    psi_paths=[paths[i] for i in (3,4,8,1)]
    delta_paths=[paths[i] for i in (3,6,7,5,8)]+[str(Path(paths[4]).with_name('rpb108_rc152_complement_action_budget.json'))]
    p=reconstruct('validate_rpb108_rc154_centered_analytic_tail_action.py','    deltaError=',psi_paths,reverse)
    d=reconstruct('validate_rpb108_rc153_correlated_difference_action.py','    eps=',delta_paths,reverse)
    payload_hash=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert payload_hash(p['payload'])==psi['finite_action_trial_center_radius_sha256']
    assert payload_hash(d['output'])==delta['finite_Cdelta_trial_center_radius_sha256']
    assert p['error']==F(psi['full_Cpsi_trial_D_norm_error_upper'])
    assert d['error']==F(delta['full_Cdelta_trial_D_norm_error_upper'])
    O=p['O'];lam=d['L']*(d['L']+1)
    qp={x['degree']:rat(F(x['center'])) for x in p['payload']}
    qd={x['degree']:rat(F(x['center'])) for x in d['output']}
    sp={};sd={}
    tailpoly=list(map(F,cov['z_minus_v_combined_tail_polynomial']))
    for n in range(0,O+1,2):
        eta=rat(0) if n<990 else p['source'].get(n)
        if n>=990 and eta is None:
            from validate_rpb108_rc127_enriched_even_endpoint_action import div
            eta=div(rat(F(2*n+1,n*(n+1))),p['dn'][n])
        sp[n]=eta
        if n>d['O']:
            amp=sum(v*F(lam,n*(n+1))**k for k,v in enumerate(tailpoly))
            sd[n]=smul(eta,rat(amp))
        else:sd[n]=rat(d['delta'][n])
        if n>p['L']:qp[n]=plus(qp[n],smul(rat(F(1,2)),eta))
        if n not in qd:qd[n]=Z
    sources=[sp,sd];trials=[qp,qd]
    degrees=list(range(0,O+1,2));degrees=degrees[::-1] if reverse else degrees
    def pair(a,b):
        value=Z
        for n in degrees:
            mass=smul(rat(2*B/F(2*n+1)),p['dn'][n])
            value=plus(value,smul(mass,smul(a[n],b[n])))
        return bounds(value)
    QL=[[F(0)]*2 for _ in range(2)];QU=[[F(0)]*2 for _ in range(2)]
    RL=[[F(0)]*2 for _ in range(2)];RU=[[F(0)]*2 for _ in range(2)]
    # Every infinite tail after O is eta times a rational polynomial.
    # Bound signed products after multiplying their coefficients. This
    # keeps delta's sign and avoids independent source-norm charging.
    rho=F(p['lam'],(O+2)*(O+3));oldrho=F(lam,(O+2)*(O+3))
    qpoly=[F(x['center'])*rho**k for k,x in enumerate(p['moments'][:p['K']+1])]
    qpoly[0]+=F(1,2)
    dpoly=[v*oldrho**k for k,v in enumerate(tailpoly)]
    def tail(a,b):
        products=[x*y for x in a for y in b]
        lo=F(p['T'])*sum(min(F(0),v) for v in products)
        hi=F(p['T'])*sum(max(F(0),v) for v in products)
        return down(lo),up(hi)
    tp=[qpoly,[]];ss=[[F(1)],dpoly]
    for i in range(2):
        for j in range(2):
            lo,hi=pair(trials[i],sources[j]);tl,th=tail(tp[i],ss[j])
            QL[i][j]=down(lo+tl);QU[i][j]=up(hi+th)
            lo,hi=pair(trials[i],trials[j]);tl,th=tail(tp[i],tp[j])
            RL[i][j]=down(lo+tl);RU[i][j]=up(hi+th)
    assert RL[0][1]==RL[1][0] and RU[0][1]==RU[1][0]
    # Both directed action identities enclose each symmetric endpoint entry.
    GLU=[[F(v) for v in row] for row in interface['full_source_Gram_upper']]
    norms=[sqrtup(GLU[i][i]) for i in (5,6)]
    errors=[p['error'],d['error']]
    inheritedL=[[F(interface['source_endpoint_pairing_entry_lower'][i][j]) for j in (5,6)] for i in (5,6)]
    inheritedU=[[F(interface['source_endpoint_pairing_entry_upper'][i][j]) for j in (5,6)] for i in (5,6)]
    HL=[[F(0)]*2 for _ in range(2)];HU=[[F(0)]*2 for _ in range(2)]
    for i in range(2):
        for j in range(i,2):
            lo,hi=inheritedL[i][j],inheritedU[i][j]
            for acted,other in ((i,j),(j,i)):
                lo=max(lo,down(QL[acted][other]-errors[acted]*norms[other]))
                hi=min(hi,up(QU[acted][other]+errors[acted]*norms[other]))
            assert lo<=hi
            HL[i][j]=HL[j][i]=lo;HU[i][j]=HU[j][i]=hi
    improvements=[]
    for i,j in ((0,0),(0,1),(1,1)):
        width=HU[i][j]-HL[i][j];oldwidth=inheritedU[i][j]-inheritedL[i][j]
        assert 0<width<=oldwidth
        improvements.append(dict(row=i,column=j,old_width=str(oldwidth),new_width=str(width),improvement_factor=str(oldwidth/width)))
    assert any(F(x['improvement_factor'])>1 for x in improvements)
    return dict(milestone='RC156',status='PASS: direct complementary trial Gram and all mixed source pairings',
        starting_commit='19b254d48e558d0288d786fe02d0334759490931',input_sha256=hashes,
        implicit_RC152_input_sha256=delta['input_sha256'][5],aperture='11/10',
        source_order=['psi0','z_b6-v10'],trial_order=['RC154 qpsi','RC153 qdelta'],
        finite_pairing_prefix_degree=O,both_trial_coefficient_hashes_verified=True,
        trial_source_pairing_entry_lower=ser(QL),trial_source_pairing_entry_upper=ser(QU),
        trial_Gram_entry_lower=ser(RL),trial_Gram_entry_upper=ser(RU),
        source_endpoint_pairing_entry_lower=ser(HL),source_endpoint_pairing_entry_upper=ser(HU),
        source_endpoint_width_improvements=improvements,
        infinite_pairing_tails_paid_with_signed_polynomial_products=True,
        trial_source_pairings_not_assumed_symmetric=True,
        complementary_mixed_endpoint_pairing_both_directions_paid=True,
        five_by_two_trial_source_cross_block_evaluated=False,
        seven_source_inverse_response_certified=False,
        original_Weil_or_augmented_actions_performed=False,
        whole_aperture_positivity_extended=False,RH=False,F4=False,Lean=False,
        next_cursor='evaluate the five-by-two mixed trial/source block, then assemble the full seven-source variational inverse-response enclosure using the paid two-trial Gram and endpoint block')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--replay',action='store_true');p.add_argument('--output',required=True);p.add_argument('inputs',nargs=9)
    a=p.parse_args();r=run(a.inputs,a.replay)
    if a.replay:assert json.loads(Path(a.output).read_text())==r
    else:Path(a.output).write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
    print('RC156 PASS: direct complementary mixed pairings')
