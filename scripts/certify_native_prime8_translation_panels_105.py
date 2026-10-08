"""Certify supported prime translations by endpoint order, above the first prime-7 threshold."""
from certify_native_legendre_small_window import F,I,log_rational


def translation_panels(a,logarithm=log_rational):
    if a!=F(21,20):raise ValueError('Only aperture 21/20 is supported')
    d=2*a
    logs={n:logarithm(F(n)) for n in (2,3,4,5,7,8,9)}
    if not logs[8].hi<d<logs[9].lo:
        raise ValueError('This interface requires log(8)<2a<log(9)')
    powers=(2,3,4,5,7,8)
    shifts={n:logs[n]/d for n in powers}
    entries=[('0',I(0),None),('1',I(1),None)]
    for index,n in enumerate(powers):
        entries.append((f'1-log({n})/(2a)',I(1)-shifts[n],(index,1)))
        entries.append((f'log({n})/(2a)',shifts[n],(index,-1)))
    entries.sort(key=lambda item:item[1].lo+item[1].hi)
    if not all(x[1].hi<y[1].lo for x,y in zip(entries,entries[1:])):
        raise ValueError('Cutoff order not certified strictly')
    locations={tag:index for index,(_,_,tag) in enumerate(entries) if tag is not None}
    active=[];witnesses=[]
    for panel in range(13):
        # The exact order proves support on the entire open panel.
        row=[]
        for index in range(6):
            if panel<locations[index,1]:row.append((index,1))
            if panel>=locations[index,-1]:row.append((index,-1))
        # A separately chosen rational point checks the branch implementation.
        midpoint=(entries[panel][1].hi+entries[panel+1][1].lo)/2
        for index,n in enumerate(powers):
            for sign in (1,-1):
                argument=I(midpoint)+sign*shifts[n]
                supported=(index,sign) in row
                if supported:assert 0<argument.lo<=argument.hi<1
                else:assert argument.hi<0 or argument.lo>1
        active.append(row);witnesses.append(midpoint)
    for panel in range(13):
        assert set(active[12-panel])=={(index,-sign) for index,sign in active[panel]}
    for index in range(14):
        reflected=I(1)-entries[index][1]
        assert (reflected.lo,reflected.hi)==(entries[13-index][1].lo,entries[13-index][1].hi)
    return dict(prime_powers=powers,labels=[x[0] for x in entries],
        cuts=[x[1] for x in entries],active=active,witnesses=witnesses)


