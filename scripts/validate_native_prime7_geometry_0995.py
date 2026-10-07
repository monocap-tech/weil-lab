"""Independent finer endpoint and complete support audit for the eleven-panel geometry."""
import hashlib,json,sys
from pathlib import Path
from certify_native_legendre_small_window import F,I
from certify_native_exact_logarithm import log_rational

def certificate(path):
    raw=Path(path).read_bytes();c=json.loads(raw)
    assert c['aperture']=='199/200' and c['prime_powers']==[2,3,4,5,7]
    saved=I.grid;I.grid=10**180
    try:
        a=F(199,200);powers=[2,3,4,5,7]
        logs={n:log_rational(F(n),500) for n in powers+[8]}
        assert logs[7].hi<2*a<logs[8].lo
        shifts={n:logs[n]/(2*a) for n in powers}
        endpoints={'0':I(0),'1':I(1)}
        for n in powers:
            endpoints[f'log({n})/(2a)']=shifts[n]
            endpoints[f'1-log({n})/(2a)']=I(1)-shifts[n]
        ordered=sorted(endpoints,key=lambda k:endpoints[k].lo)
        assert ordered==c['labels'] and len(ordered)==12
        intervals=[tuple(map(F,p)) for p in c['cut_intervals']]
        for label,(lo,hi) in zip(ordered,intervals):
            assert lo<=endpoints[label].lo<=endpoints[label].hi<=hi
        assert all(x[1]<y[0] for x,y in zip(intervals,intervals[1:]))
        assert all((1-hi,1-lo)==intervals[11-i] for i,(lo,hi) in enumerate(intervals))
        checks=0
        for panel in range(11):
            t=F(c['rational_panel_witnesses'][panel]);assert intervals[panel][1]<t<intervals[panel+1][0]
            active=[]
            for index,n in enumerate(powers):
                for sign in (1,-1):
                    v=I(t)+sign*shifts[n]
                    if 0<v.lo<=v.hi<1:active.append([index,sign])
                    else:assert v.hi<0 or v.lo>1
                    checks+=1
            assert active==c['active_translations'][panel]
            # The only support events are the included translation endpoints.
            assert len(set(map(tuple,active)))==len(active)
        displaced=intervals[:];displaced[1]=(F(-1),F(-1))
        assert not all(x[1]<y[0] for x,y in zip(displaced,displaced[1:]))
        assert len(endpoints)-1==11 and c['panel_count']==11
        return dict(aperture='199/200',geometry_sha256=hashlib.sha256(raw).hexdigest(),finer_endpoint_inclusions=12,
            independent_support_checks=checks,complete_support_event_set_verified=True,
            reflection_verified=True,displaced_endpoint_control_rejected=True,
            whole_domain_positivity=False,whole_domain_frontier='99/100',f4_entry_closed=False)
    finally:I.grid=saved

if __name__=='__main__':print(json.dumps(certificate(sys.argv[1]),indent=2))

