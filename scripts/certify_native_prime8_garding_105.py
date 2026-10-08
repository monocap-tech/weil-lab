"""Strict target Garding losses, using the pinned archimedean loss six."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from certify_native_exact_logarithm import log_rational
from certify_native_legendre_small_window import I
saved=I.grid;I.grid=10**140
try:
 path=Path('notes/data/RPB108_PRIME8_WEIGHTED_DEPTH10_105_CERTIFICATE_20261008.json');raw=path.read_bytes();p=json.loads(raw)
 assert p['aperture']=='21/20' and p['prime_powers']==[2,3,4,5,7,8]
 loss=2*sum(map(F,p['amplitude_upper']),F(0));assert loss<7
 a=F(21,20);assert a<log_rational(F(3),450).lo
 assert 4*a*3==F(63,5)<13
 out={'aperture':str(a),'weighted_prime_sha256':hashlib.sha256(raw).hexdigest(),'crude_prime_loss_upper':str(loss),
  'prime_loss_strict_upper':7,'pole_loss_strict_upper':13,'archimedean_loss':6,'garding_constant':26,
  'multiplier_weight_factor':'1/10','strict_losses_verified':True,'whole_domain_positivity':False}
 print(json.dumps(out,indent=2))
finally:I.grid=saved
