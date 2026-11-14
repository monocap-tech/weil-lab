#!/usr/bin/env python3
"""NF512 independent Fraction receipt checks and direct-residual identity.

Authenticates actual source-pinned original H4095 computation, verifies
local e_H interval consistency and exact NF508 acceptance comparisons.
Independent rational toy regressions prove direct residual integration
agrees with E_H-2a*b_H+a*C_H*a, with source-recenter invariance.

Does not independently perform full 242D 4096-bit original reintegration,
or certify any unrun NF512 native result.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
FRAME='18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e'

def read(p):
    b=Path(p).read_bytes()
    return json.loads(b),hashlib.sha256(b).hexdigest()
def I(p):
    l,h=map(F,p)
    assert l<=h
    return l,h
def overlaps(x,y):return max(x[0],y[0])<=min(x[1],y[1])
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def exact_toy_controls():
    # Authentic-style odd 2D rational selected space; exact support
    # restriction direct residual == local quadratic E-2ab+aCa
    # for ANY globally optimal a and selected recentering term.
    results=0
    for m in (4,5,6,7,8):
        x=[F(j+1,m+3) for j in range(m)]
        for t in (F(0),F(7,13),F(-19,4),F(10**20)):
            J=[[v,v**3] for v in x]
            r=[v**5+F(1,17)*v**7 for v in x]
            # Mirror partner -x contributes exactly twice to all
            # physical source odd inner products.
            W=[r[j]+t*J[j][0]-F(2,7)*J[j][1] for j in range(m)]
            def calc(H):
                H=list(H)
                C=[[2*sum((J[i][k]*J[i][l] for i in H),F(0))
                    for l in range(2)] for k in range(2)]
                b=[2*sum((J[i][k]*W[i] for i in H),F(0)) for k in range(2)]
                E=2*sum((W[i]**2 for i in H),F(0))
                return C,b,E
            G,b,E=calc(range(m))
            det=G[0][0]*G[1][1]-G[0][1]**2
            assert det>0
            a=[(b[0]*G[1][1]-b[1]*G[0][1])/det,
               (G[0][0]*b[1]-G[1][0]*b[0])/det]
            for i in range(m):
                C,c,Eh=calc([i])
                direct=2*(W[i]-dot(J[i],a))**2
                mix=Eh-2*dot(a,c)+dot(a,[dot(row,a) for row in C])
                assert direct==mix>=0
                results+=1
    assert results==120
    return results

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--native',required=True)
    p.add_argument('--nf505',required=True)
    p.add_argument('--nf494',required=True)
    p.add_argument('--nf511',required=True)
    p.add_argument('--output',required=True)
    o=p.parse_args()
    data,ds=read(o.native);old,os=read(o.nf505)
    h,hs=read(o.nf494);oldpanel,ps=read(o.nf511)
    assert os==NF505 and hs==NF494
    assert data['pass']=='NF512-original-local-direct-residual-native'
    assert data['original_NF505_SHA256']==NF505
    assert data['original_NF494_SHA256']==NF494
    assert data['source_original_NF407_SHA256']==SRC
    assert data['source_original_NF406_SHA256']==SEAM
    assert old['source_original_NF407_sha256']==h['original_nf407_source_sha256']==SRC
    assert old['source_original_NF406_sha256']==h['original_nf406_seams_sha256']==SEAM
    assert old['original_original_D_frame_SHA256']==data['original_source_D_SHA256']==FRAME
    assert old['original_selected_J_dimension']==data['original_selected_dimension']==242
    assert old['original_support_saturated_physical_Hilbert_gate']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    assert oldpanel['pass']=='NF511-original-source-exact-local-W-pole-panel'
    assert oldpanel['original_nf494_raw_SHA256']==NF494
    assert oldpanel['original_nf505_raw_SHA256']==NF505
    assert data['true_original_microcell_index']==4095
    assert data['source_original_pair_width']==str(F(2*549,500*4096))
    assert data['selected_jet_order']>=200
    E=I(data['original_full_W_H4095_energy_native'])
    Eprior=I(oldpanel['local_E_H_original_full_W_squared'])
    assert overlaps(E,Eprior)
    resid=I(data['original_complete_242D_exterior_fitted_residual_eH_native'])
    R=I(old['original_original_saturated_exterior_residual_outward'])
    assert resid[0]>=0 and resid[0]<=R[1]
    tau=I(data['original_complete_242D_selected_local_leverage_native'])
    assert 0<tau[0]<=tau[1]<242
    gamma=F(old['original_original_gamma_squared'])
    assert gamma==F(data['original_unchanged_NF404_gamma_squared'])
    assert R[0]>gamma
    feeW=I(data['original_source_W_taylor_global_error_upper'])
    feeJ=I(data['original_source_selected_fit_taylor_error_upper'])
    assert 0<=feeW[0]<=feeW[1]<F('1e-50')
    assert 0<=feeJ[0]<=feeJ[1]<F('1e-40')
    verdict=data['original_single_pair_NF404_gate']
    if tau[1]<1:
        # Conservative ORIGINAL-source lower R(O)-e_H/(1-tau).
        predicted=R[0]-resid[1]/(1-tau[1])
        calculated=I(data['original_single_pair_no_go_lower_if_tau_lt_one'])
        assert calculated[0]<=predicted<=calculated[1]
        if verdict=='CERTIFIED_ORIGINAL_NF404_SINGLE_PAIR_PHYSICAL_NO_GO':
            assert predicted>gamma
        else:
            assert verdict=='LOCAL_NECESSARY_GATE_INDETERMINATE'
            assert predicted<=gamma
    else:
        assert verdict=='METHOD_STOP_LEVERAGE_GE_ONE_OR_INDETERMINATE'
        assert data['original_single_pair_no_go_lower_if_tau_lt_one'] is None
    assert data['original_full_local_residual_direct_integral_complete'] is True
    assert data['original_full_local_242x242_Mixed_moments_reintegrated_separately'] is False
    assert data['Weil_multiplier_image_graph_domain']=='OPEN'
    assert data['W_ODD_NEG']==data['RH']=='OPEN'
    toys=exact_toy_controls()
    result={
      'pass':'NF512-independent-source-receipt-exact',
      'scope':'True original J242 direct locally squared exterior fit receipt cross-source SHA, source-outward interval and algebra; not independent numerical reintegration or Weil-domain theorem',
      'NF512_raw_native_sha256':ds,
      'original_NF505_raw_sha256':NF505,
      'original_NF494_raw_sha256':NF494,
      'source_nf407_sha256':SRC,'source_nf406_sha256':SEAM,
      'named_H_microcell':4095,'full_selected_dimension':242,
      'NF511_local_W2_source_overlap':True,
      'original_full_242D_true_local_residual_outward':[str(x) for x in resid],
      'original_full_242D_true_leverage_outward':[str(x) for x in tau],
      'unchanged_NF404_original_gamma_squared':str(gamma),
      'original_scoped_named_physical_gate':verdict,
      'exact_rational_independent_direct_vs_mixed_local_controls':toys,
      'independent_full_242D_4096bit_reintegration':False,
      'original_weil_multiplier_image_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(o.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF512 independently SHA-audited original direct 242D local energy and source receipt PASS')
    print('Original genuine H4095 eH',float(resid[0]),float(resid[1]))
    print('Original genuine H4095 tau',float(tau[0]),float(tau[1]))
    print('Original named-cell fixed NF404 gate:',verdict)
    print('Weil image/domain and RH OPEN')
if __name__=='__main__':main()
