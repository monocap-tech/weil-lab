#!/usr/bin/env python3
"""NF380: exact rational survivor-count gate, not a native original Gram run."""
from fractions import Fraction as F
import json
import argparse
from pathlib import Path

def lower_count(n,d,t):
    assert F(0)<t<F(1)
    # Max sum when exactly k residual fractions exceed t is <=k+(n-k)t.
    q=(F(n-d)-n*t)/(1-t)
    assert q>0
    return -(-q.numerator//q.denominator)

def main():
    p=argparse.ArgumentParser();p.add_argument('--report',required=True);a=p.parse_args()
    n=492;d=246;B=F(11,10);h=B/n
    assert h==F(11,4920) and n==2*d
    k49=lower_count(n,d,F(49,100))
    k13=lower_count(n,d,F(1,3))
    assert k49==10 and k13==123
    assert 9+(n-9)*F(49,100)==F(24567,100)<n-d
    assert 122+(n-122)*F(1,3)==F(736,3)<n-d
    area=4*B*2**20
    ratio=area/n
    assert ratio==F(5767168,615)
    out=dict(standing='EXACT_GEOMETRIC_SURVIVOR_COUNT_ONLY',
      original_selected_count=242,fitted_E_count_upper=4,
      annuli=n,step=str(h),B=str(B),
      trace_lower=n-d,
      selected_annuli_strictly_above_49_percent_at_least=k49,
      annuli_strictly_above_one_third_at_least=k13,
      lowband_cutoff=2**20,
      illustrative_time_frequency_area=str(area),
      illustrative_area_over_n=str(ratio),
      area_as_exact_finite_rank_claim=False,
      identified_original_annulus=False,
      original_4096bit_native_annulus_certificate_passed=False,
      signed_continuum_computed=False,
      NF375_sufficient_method_stopped=False,
      external_method_promoted=False,
      W_ODD_NEG='OPEN',RH='OPEN')
    path=Path(a.report);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print('NF380 PASS exact survivor count: at least',k49,'above 49%,',k13,'above 1/3. Native annulus still OPEN.')
if __name__=='__main__':main()
