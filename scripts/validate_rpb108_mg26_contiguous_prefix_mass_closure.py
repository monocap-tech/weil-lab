#!/usr/bin/env python3
"""MG26: actual-original contiguous prefix mass-closure for 24D source moments.

Certify H_C, G_C=(Ao F)_form(C), S_C=(Ao F)_strong(C) on
C=[-T,T], from exact rational original-source affine Fourier
intervals on a true PARTITION of every positive frequency 0..T.
Then close *all omitted frequencies* with the original physical
Gram, not only MG19's 24 selected frequency panels:

  Hrem=H-H_C >=0,   Ao>=kappa on all real frequencies,
  Ao<=M_k on |xi|<=2**k, and SM41 true high strong tails.

  L_G = L_GC + kappa (Hlo-U_HC)
  U_G = U_GC + M_k(Hup-L_HC) + tau1 I
  L_S = L_SC + kappa**2(Hlo-U_HC)
  U_S = U_SC + M_k**2(Hup-L_HC) + tau2 I.

These are TRUE ORIGINAL ALL-FREQUENCY LOEWNER source-moment brackets.
This is mass closure: high/unintegrated source covariance is not
replaced by an unrelated scalar I; its upper is H-H_C_lower.

Full rank-one sinh pole response c=Go*e_p and Astar squared mixed
term are enclosed via the original MG24 exact rational machinery.
No automatic strict contraction, invariance, original 470D inverse,
odd signed cap, even/Weil/CC27/RH promotion.
"""
import argparse,json,sys
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)

from validate_rpb108_mg16_weighted_affine_source_moments import (
 ROOT,N,PHYS,POLE,PIVOT,B,ORDERS,CHOSEN_TAUS,
 original_source_centered_windows,
 original_full_25_physical_interval_gram,
 protected_inner_cover,boundary_intervals,derivative_intervals_and_D3,
 interval_out,pair_coefficients,positive_gap,
 hyperbolic_interval,original_full_second_derivative_upper,
 original_exact_physical_fourier_midpoint,
 original_midpoint_derivative_intervals,original_third_spatial_moment,
 transformed_affine,abs_cap,zero,sym,finalize,
 positive_cell_weight_interval
)
from validate_rpb108_mg15_directional_affine_covariance import (
 add_directed_cell,lower_cell_trace
)
from validate_rpb108_mg24_complete_original_coupled_source_enclosures import (
 exact_sqrt_ceil,centers_and_diag_error,deserialize if False else zeros
)
