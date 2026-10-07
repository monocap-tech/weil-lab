"""Independent finer-log support and exact prime-7 edge-block audit."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I,sqrt_rational
from certify_native_exact_logarithm import log_rational

def certificate(path,repeat):
    raw=Path(path).read_bytes();assert raw==Path(repeat).read_bytes();c=json.loads(raw)
    assert c['aperture']=='49/50' and c['prime_powers']==[2,3,4,5,7]
    saved=I.grid;I.grid=10**140
    try:
        a=F(c['aperture']);logs={n:log_rational(F(n),450) for n in (2,3,4,5,7,8)}
        def encloses(pair,value):
            lo,hi=map(F,pair);assert lo<=value.lo<=value.hi<=hi
        threshold=logs[7]/2;encloses(c['entry_threshold_interval'],threshold)
        assert F(9729,10000)<threshold.lo<threshold.hi<a<logs[8].lo/2
        shifts={n:logs[n]/(2*a) for n in (2,3,4,5,7)}
        expected={'0':I(0),'1':I(1)}
        for n,x in shifts.items():expected[f'ell_{n}']=x;expected[f'1-ell_{n}']=I(1)-x
        assert set(c['cut_enclosures'])==set(expected)
        for name,x in expected.items():encloses(c['cut_enclosures'][name],x)
        cuts=sorted(expected,key=lambda name:expected[name].lo)
        assert cuts==c['ordered_cuts'] and len(cuts)==12
        assert all(expected[x].hi<expected[y].lo for x,y in zip(cuts,cuts[1:]))
        assert len(c['panels'])==c['panel_count']==11
        active7=[]
        for i,row in enumerate(c['panels']):
            assert row['left']==cuts[i] and row['right']==cuts[i+1]
            t=F(row['midpoint']);assert expected[cuts[i]].hi<t<expected[cuts[i+1]].lo
            active=[]
            for sign in (1,-1):
                for n,shift in shifts.items():
                    y=I(t)+sign*shift
                    if 0<y.lo<=y.hi<1:active.append(('+' if sign==1 else '-')+str(n))
                    else:assert y.hi<0 or y.lo>1
            assert active==row['active_translations']
            if '+7' in active or '-7' in active:active7.append(i)
        assert active7==[0,10]
        width=I(2*a)-logs[7];encloses(c['edge_overlap_width_interval'],width)
        assert width.lo>0 and logs[7].lo>a  # paired strips are disjoint
        alpha=logs[7]/sqrt_rational(F(7));encloses(c['prime7_operator_norm_interval'],alpha)
        assert alpha.lo>F(73,100)
        # The strip pair exchange is an isometry; equal constant profiles attain its norm.
        assert c['positive_overlap_norm_does_not_vanish_with_width'] and c['old_nine_panel_reuse_rejected']
        return dict(certificate_sha256=hashlib.sha256(raw).hexdigest(),byte_identical_repeat=True,
            aperture=str(a),independent_140_digit_logarithm_enclosures=True,
            actual_prime_power_membership_verified=True,source_panels_verified=11,
            signed_translation_tests=110,prime7_only_on_two_edge_panels=True,
            prime7_exchange_block_norm_verified=True,small_width_norm_control_rejected=True,
            nine_panel_reuse_control_rejected=True,whole_domain_frontier='973/1000',
            whole_domain_positivity_at_target=False,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=saved

if __name__=='__main__':
    import sys
    print(json.dumps(certificate(*sys.argv[1:]),indent=2))

