"""Prime-4 coefficient and seven-panel activation controls at aperture 3/4."""
import json,hashlib
from pathlib import Path
from certify_native_legendre_small_window import F,I,log_rational


def certificate():
    root=Path(__file__).resolve().parents[1]/'notes/data'
    sp=root/'RPB108_PRIME4_SOURCE48_075_CERTIFICATE_20261005.json'
    source=json.loads(sp.read_text())
    assert source['aperture']=='3/4' and source['prime_terms']==[2,3,4]
    d=F(3,2);ell=[log_rational(F(n))/d for n in (2,3,4)]
    cuts=[I(0),I(1)-ell[2],I(1)-ell[1],ell[0],I(1)-ell[0],ell[1],ell[2],I(1)]
    assert all(x.hi<y.lo for x,y in zip(cuts,cuts[1:]))
    expected=[[(0,1),(1,1),(2,1)],[(0,1),(1,1)],[(0,1)],[(0,1),(0,-1)],
              [(0,-1)],[(0,-1),(1,-1)],[(0,-1),(1,-1),(2,-1)]]
    observed=[]
    for left,right in zip(cuts,cuts[1:]):
        t=(left+right)/2;active=[]
        for k,s in enumerate(ell):
            if (t+s).hi<1:active.append((k,1))
            else:assert (t+s).lo>1
            if (t-s).lo>0:active.append((k,-1))
            else:assert (t-s).hi<0
        observed.append(active)
    assert observed==expected and all(len(r['panels'])==7 for r in source['rows'])
    # On normalized p0, the missing (or extra) prime-4 term changes the
    # native/source pairing by log(2)*(1-log(4)/d).
    gap=log_rational(F(2))*(I(1)-log_rational(F(4))/d)
    row_error=F(source['rows'][0]['normalized_uniform_error'])
    assert gap.lo>F(6,1000) and gap.lo>2*row_error
    return dict(aperture='3/4',prime_terms=[2,3,4],panel_count=7,
                panel_translation_indices=observed,all_panel_activation_controls_passed=True,
                actual_prime4_coefficient='log(2)/2',incorrect_prime4_coefficient='log(4)/2',
                prime4_pairing_gap_lower=str(gap.lo),constant_row_source_error_upper=str(row_error),
                prime4_omission_control_rejected=True,prime4_double_coefficient_control_rejected=True,
                source_certificate_sha256=hashlib.sha256(sp.read_bytes()).hexdigest(),
                whole_domain_positivity=False,actual_negative_witness=False,lean_formalized=False)


if __name__=='__main__':print(json.dumps(certificate(),indent=2))
