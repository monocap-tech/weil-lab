"""Independent branch support checks and old-table failure beyond the collision."""
import json
from certify_native_legendre_small_window import F,I,log_rational,sqrt_rational
from certify_native_translation_panel_order import translation_panels


OLD=[[(0,1),(1,1),(2,1),(3,1)],[(0,1),(1,1),(2,1)],[(0,1),(1,1)],[(0,1)],
     [(0,1),(0,-1)],[(0,-1)],[(0,-1),(1,-1)],[(0,-1),(1,-1),(2,-1)],
     [(0,-1),(1,-1),(2,-1),(3,-1)]]


def certificate():
    old_grid=I.grid;I.grid=10**100
    try:
        records=[]
        for a in (F(81,100),F(41,50),F(17,20),F(22,25),F(9,10)):
            geometry=translation_panels(a);d=2*a
            branch_checks=0
            for panel,t in enumerate(geometry['witnesses']):
                independently_active=[]
                for index,n in enumerate((2,3,4,5)):
                    shift=log_rational(F(n))/d
                    for sign in (1,-1):
                        value=I(t)+sign*shift
                        if 0<value.lo<=value.hi<1:independently_active.append((index,sign))
                        else:assert value.hi<0 or value.lo>1
                        branch_checks+=1
                assert set(independently_active)==set(geometry['active'][panel])
            if a<F(9,10):
                assert all(set(x)==set(y) for x,y in zip(geometry['active'],OLD))
            else:
                assert set(geometry['active'][3])=={(0,1),(0,-1),(1,1)}
                assert set(geometry['active'][5])=={(0,1),(0,-1),(1,-1)}
                assert [i for i in range(9) if set(geometry['active'][i])!=set(OLD[i])]==[3,5]
            records.append(dict(aperture=str(a),panel_count=9,labels=geometry['labels'],
                cut_intervals=[[str(x.lo),str(x.hi)] for x in geometry['cuts']],
                active_argument_shifts=geometry['active'],rational_panel_witnesses=list(map(str,geometry['witnesses'])),
                independent_support_branch_checks=branch_checks,reflection_verified=True))
        a=F(9,10);d=2*a;geometry=translation_panels(a)
        # Degree-zero Legendre source: core cancels, so missing shifts cannot cancel.
        amplitude=[log_rational(F(n if n!=4 else 2))/sqrt_rational(F(n)) for n in (2,3,4,5)]
        controls=[]
        for panel in (3,5):
            actual=-sum((amplitude[index] for index,sign in geometry['active'][panel]),I(0))
            stale=-sum((amplitude[index] for index,sign in OLD[panel]),I(0))
            difference=actual-stale;assert difference.hi<0
            controls.append(dict(panel=panel,stale_table_source_difference_interval=[str(difference.lo),str(difference.hi)],
                degree_zero_actual_translation_mismatch=True))
        ell2=log_rational(F(2))/d;ell3=log_rational(F(3))/d
        assert ell2.hi<(I(1)-ell3).lo and ell3.hi<(I(1)-ell2).lo
        for a in (F(0),F(1,2),F(1)):
            try:translation_panels(a)
            except ValueError:pass
            else:raise AssertionError('Unsupported domain accepted')
        log2=log_rational(F(2));log3=log_rational(F(3))
        unresolved=(log2.lo+log2.hi+log3.lo+log3.hi)/4
        try:translation_panels(unresolved)
        except ValueError:pass
        else:raise AssertionError('Unresolved cutoff ordering accepted')
        return dict(status='certified actual supported translation-panel reorder',
            records=records,old_table_actual_source_failure_controls=controls,invalid_domain_controls_rejected=3,
            unresolved_cutoff_order_control_rejected=True,
            complete_source_constructor_extended=False,whole_domain_positivity_at_9_10=False,
            certified_whole_domain_frontier='22/25',global_endpoint_excluded=False,f4_entry_closed=False,lean_formalized=False)
    finally:I.grid=old_grid


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
