#!/usr/bin/env python3
"""Necessary signed join windows and PSD completions of a reduced packet."""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import certify_native_remaining_background_nf31_106 as p

def root_upper(v):return F(p.n.sqrt_r(v).h,p.n.SCALE)
def root_lower(v):return F(p.n.sqrt_r(v).l,p.n.SCALE)
def midpoint(v):return sum(map(F,v))/2

def run(pairs,new):
    k=F(207,1000);rows=[]
    for pair,probe in zip(pairs,new):
        A=pair['sufficient_collective_matrix'];G=pair['original_complete_residual_Gram']
        gp=midpoint(probe['original_complete_projected_source_square'])
        cp=F(probe['floor_score'][1]);assert cp>0
        gram=[[midpoint(v) for v in row] for row in G]
        assert gram[0][0]>0 and gram[0][0]*gram[1][1]>gram[0][1]**2
        native=[[midpoint(v) for v in row] for row in pair['original_finite_energy_Gram']]
        exactA=[[native[i][j]-gram[i][j]/k for j in range(2)] for i in range(2)]
        assert exactA[0][0]>0 and exactA[0][0]*exactA[1][1]>exactA[0][1]**2
        windows=[]
        for j in range(2):
            radius=root_upper(k*k*F(A[j][j][1])*cp)
            assert 0<exactA[j][j]<=F(A[j][j][1])
            cauchy_lower=root_lower(F(G[j][j][0])*F(probe['original_complete_projected_source_square'][0]))
            assert cauchy_lower>radius
            # Both signs yield PSD three-source Gram completions sharing
            # the exact same old two-source block and new source diagonal.
            alpha=root_lower(gp/gram[j][j]);cross=[alpha*gram[i][j] for i in range(2)]
            leftover=gp-alpha*alpha*gram[j][j];assert leftover>=0 and abs(cross[j])>radius
            # For every fixed native center n_j, at least one sign obeys
            # |k*n_j-g_j|>=|g_j|>radius, so that principal minor is negative.
            windows.append(dict(pair_coordinate=j,necessary_covariance_radius_upper=str(radius),
                radius_over_Cauchy_envelope_upper=str(radius/cauchy_lower),
                PSD_completion_cross=list(map(str,cross)),PSD_completion_other_sign=list(map(lambda v:str(-v),cross)),
                PSD_completion_positive_diagonal_remainder=str(leftover),
                at_least_one_completion_violates_necessary_window_for_every_native_center=True))
        rows.append(dict(parity=probe['parity'],necessary_windows=windows,
            reduced_norm_and_diagonal_packet_cannot_certify_join=True,
            actual_signed_join_rejected=False,complete_Weil_identities_nonimplication_claimed=False))
    controls=[]
    for scale in [F(1),F(1,10**18)]:
        for t in [F(99,100),F(1),F(101,100)]:
            schur=2*scale**2*(1-t*t)
            border=[2*scale*t,scale*t];inv=[[F(2,3),F(-1,3)],[F(-1,3),F(2,3)]]
            reaction=sum(border[i]*inv[i][j]*border[j] for i in range(2) for j in range(2))
            assert 2*scale**2-reaction==schur
            q=[[F(2),F(1),border[0]],[F(1),F(2),border[1]],[*border,2*scale**2]]
            determinant=q[0][0]*(q[1][1]*q[2][2]-q[1][2]*q[2][1])-q[0][1]*(q[1][0]*q[2][2]-q[1][2]*q[2][0])+q[0][2]*(q[1][0]*q[2][1]-q[1][1]*q[2][0])
            assert determinant==3*schur
            controls.append(dict(scale=str(scale),mixed_multiplier=str(t),exact_border_Schur=str(schur),
                exact_three_by_three_determinant=str(3*schur),all_diagonals_positive=True))
    # A=[[2,1],[1,2]], b=(2,1), c=2 is PSD and kills (-1,0,1).
    Q=[[F(2),F(1),F(2)],[F(1),F(2),F(1)],[F(2),F(1),F(2)]]
    assert all(sum(v*z for v,z in zip(row,[-1,0,1]))==0 for row in Q)
    levels=[dict(whole_physical_mass_shift=str(s),exact_ground_level=str(s)) for s in [F(1,1000),F(1,10),F(2)]]
    return dict(milestone='CC79',aperture='53/50',parity_certificates=rows,
        genuine_border_crossing_controls=controls,positive_whole_mass_controls=levels,
        simultaneous_six_retained_direction_certificate=False,whole_aperture_positive=False,
        actual_arithmetic_countermodel_claimed=False)

if __name__=='__main__':
    a=argparse.ArgumentParser()
    for name in ['even_pair','odd_parent','even_probe','odd_probe']:a.add_argument(name)
    a.add_argument('--output',required=True);a=a.parse_args()
    raw=[Path(getattr(a,name)).read_bytes() for name in ['even_pair','odd_parent','even_probe','odd_probe']]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==[
        'd0625cefe819f3704dec1d75bf0ad0bcd4ea8a3cd6806ebe6d76056733ac321b',
        '069d4acc267a0ac48154427a033cccca96243743dd31e36449f7189de03e895a',
        '7327c2f3d89327ed1cef95404646c059c3ded4d4881486b1b3beb15651337d4f',
        '17ae9ec6757cd29443fc77af28b86fb3d4b7f9449317886c5aec75bf92a9fb89']
    d=list(map(json.loads,raw));r=run([d[0],d[1]['parity_certificates'][1]],d[2:]);r['input_sha256']=[hashlib.sha256(v).hexdigest() for v in raw]
    Path(a.output).write_text(json.dumps(r,indent=2)+'\n')
    for row in r['parity_certificates']:
        print(row['parity'],*[float(F(z['necessary_covariance_radius_upper'])) for z in row['necessary_windows']])
