"""Complete rational endpoint/support geometry at aperture 1."""
import hashlib,json
from pathlib import Path
from certify_native_legendre_small_window import F,I
from certify_native_prime7_translation_panels_100 import translation_panels
from certify_native_exact_logarithm import log_rational

def certificate():
    saved=I.grid;I.grid=10**140
    try:
        g=translation_panels(F(1),logarithm=lambda x:log_rational(x,450))
        assert len(g['active'])==11
        return dict(aperture='1',prime_powers=list(g['prime_powers']),panel_count=11,
            labels=g['labels'],cut_intervals=[[str(c.lo),str(c.hi)] for c in g['cuts']],
            active_translations=g['active'],rational_panel_witnesses=list(map(str,g['witnesses'])),
            strict_cut_order=True,reflection_verified=True,interval_grid_digits=140,log_series_terms=450,
            constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            translation_constructor_sha256=hashlib.sha256(Path(__file__).with_name('certify_native_prime7_translation_panels_100.py').read_bytes()).hexdigest(),
            whole_domain_positivity=False,whole_domain_frontier='399/400',f4_entry_closed=False)
    finally:I.grid=saved

if __name__=='__main__':print(json.dumps(certificate(),indent=2))

