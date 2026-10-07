"""First prime-7 overlap, eleven source panels and exact edge-block norm."""
import json
from certify_native_legendre_small_window import F,I,sqrt_rational
from certify_native_exact_logarithm import log_rational

def certificate():
    saved=I.grid;I.grid=10**100
    try:
        a=F(49,50);logs={n:log_rational(F(n),400) for n in (2,3,4,5,7,8)}
        threshold=logs[7]/2
        assert F(97,100)<F(9729,10000)<threshold.lo<threshold.hi<a<logs[8].lo/2
        cuts=[('0',I(0)),('1',I(1))]
        shifts={n:logs[n]/(2*a) for n in (2,3,4,5,7)}
        for n,x in shifts.items():cuts.extend([(f'ell_{n}',x),(f'1-ell_{n}',I(1)-x)])
        cuts.sort(key=lambda x:x[1].lo)
        assert len(cuts)==12 and all(x[1].hi<y[1].lo for x,y in zip(cuts,cuts[1:]))
        panels=[]
        for left,right in zip(cuts,cuts[1:]):
            midpoint=(left[1].hi+right[1].lo)/2;active=[]
            for sign in (1,-1):
                for n,x in shifts.items():
                    y=I(midpoint)+sign*x
                    if 0<y.lo<=y.hi<1:active.append(('+' if sign==1 else '-')+str(n))
                    else:assert y.hi<0 or y.lo>1
            panels.append(dict(left=left[0],right=right[0],midpoint=str(midpoint),active_translations=active))
        width=I(2*a)-logs[7];assert 0<width.lo<=width.hi<logs[7].lo
        alpha=logs[7]/sqrt_rational(F(7))
        # On the paired edge strips T7 maps (f_left,f_right) to alpha*(f_right,f_left).
        # The strips have positive width and are disjoint: norm exactly alpha.
        assert panels[0]['active_translations'][-1]=='+7'
        assert panels[-1]['active_translations'][-1]=='-7'
        assert all('7' not in ','.join(row['active_translations']) for row in panels[1:-1])
        return dict(aperture=str(a),prime_powers=[2,3,4,5,7],prime4_amplitude='log(2)/2',
            entry_threshold='log(7)/2',entry_threshold_interval=[str(threshold.lo),str(threshold.hi)],
            edge_overlap_width_interval=[str(width.lo),str(width.hi)],edge_overlap_width_display=float(width.hi),
            prime7_operator_norm_interval=[str(alpha.lo),str(alpha.hi)],prime7_operator_norm_display=float(alpha.hi),
            edge_block_norm_identity='alpha times the exchange operator on two equal disjoint strips',
            positive_overlap_norm_does_not_vanish_with_width=True,
            ordered_cuts=[name for name,_ in cuts],cut_enclosures={name:[str(x.lo),str(x.hi)] for name,x in cuts},
            panels=panels,panel_count=11,old_nine_panel_reuse_rejected=True,
            whole_domain_frontier='973/1000',new_native_sign=False,new_source=False,new_gram=False,
            f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=saved

if __name__=='__main__':print(json.dumps(certificate(),indent=2))

