# RC257 — full physical residual-source Fourier enclosure

Parent: `08cd38aeefcaed789de95df6d1822db3d8035324` (RC256).
Branch: `research/rpb108-route-consolidation`.

RC257 evaluates the outside-band Fourier energy of the complete retained
physical residual polynomial through degree 256 and encloses the Fourier
energy of the actual full source. The original two sources, four trials per
parity, fixed rational trial Z, and actual rational augmentation are unchanged.
This extends the RC256 conditional two-band calculation; it does not certify
either source's positive signed gap or the full rank-639 criterion.

Certified results (decimal values shown for orientation; certificate stores
exact rational outward bounds):

| Quantity | Even | Odd |
| --- | ---: | ---: |
| Retained polynomial outside energy upper | 0.001931114 | 0.001906634 |
| Actual full-source outside energy upper | 0.023814340 | 0.027474918 |
| RC256 strict sufficient outside-energy budget | 0.002415316 | 0.002345353 |
| Current envelope allowance at zero retained leakage | 0.012687298 | 0.014906111 |
| Selected two-band tau | 79/400 | 1761/10000 |
| Previous inverse-response upper | 0.593215220 | 0.745085473 |
| Current inverse-response upper | 0.593215220 | 0.670898393 |
| Current signed-gap lower | -0.504656024 | -0.573815577 |

The odd inverse upper improves by about 0.07418708 (9.96%). Neither actual
outside energy is proved to exceed its budget: both lower bounds remain zero.
The even outside upper is capped by the total physical source-energy bound.

The physical source is g_e = D e = G0 Pbase - G Z, with e = N0 Pbase - N Z.
The canonical metric M = D^-1 L remains separate from the actual augmented
operator N. The diagonal D has H_n+s, with harmonic H_n, on physical Legendre
modes. No n(n+1) substitution is made in this diagonal.

## Exact retained polynomial calculation

At s_mid = (s_lower+s_upper)/2, let a_n = (H_n+s_mid)e_center,n
for 0 <= n <= 256. Its Fourier transform is evaluated by the exact spherical
Bessel sine/cosine inverse-power polynomials. All mode coefficients are
combined before squaring, retaining every cross term.

For I_m(z) = integral_z^infinity exp(2it)t^(-m) dt, the calculation uses

    (m-1) I_m(z) = 2 i I_(m-1)(z) + exp(2iz) z^(1-m).

The base I_2 interval uses 500 integration-by-parts terms in generation and
520 in replay. Forward recurrence is applied to unscaled moments, with
explicit outward intervals on a 1600-decimal grid. A 220-term sine/cosine
Taylor calculation encloses the phase. Its integer-turn reduction uses
Machin's identity pi = 16 atan(1/5) - 4 atan(1/239), 600 alternating terms
per arctangent, explicit next-term errors, and an outward 450-decimal pi
interval. The reduced argument is enclosed on a 400-decimal grid.

This sharper pi interval is a computational phase control only. The original
pinned pi uncertainty is still paid in the Fourier lower-limit and prefactor
comparison. It does not change U or the actual rational Fourier augmentation.
An independent low-degree aggregate comparison with RC243's per-order
integration-by-parts calculation checks the moment recurrence.

## Complete source and inverse enclosure

Write g_e = p_256 + r. The retained finite coefficient/actual-s uncertainty
and omitted model output are orthogonal physical Legendre blocks. Therefore
the inherited valid error radius is

    E = sqrt(E_finite + E_omitted) + E_global_fault_norm.

All original regular-kernel, prime-arithmetic, pole-Taylor and rational
augmentation faults remain included. Let Y_lower, Y_upper enclose the retained
polynomial's outside-band energy, and let S bound the actual full source's
physical energy. Projection contraction and the triangle inequality give

    max(0, sqrt(Y_lower)-E)^2 <= X
    X <= min(S, (sqrt(Y_upper)+E)^2),

where X is the actual full source's outside-band Fourier energy. No omitted
Legendre-output energy is identified with a Fourier outside-band energy.

For each of RC256's 1000 rational tau candidates, retain
G >= eta_tau L + beta_tau C_U. If I = eta_tau+beta_tau >
O = eta_tau log(U)_lower > 0, then

    <e,N^-1 e>_D <= S/I + X_upper(1/O - 1/I).

RC257 selects the least certified correction on that finite grid and
intersects the resulting inverse and signed-gap enclosures with RC256.
No continuous optimization claim is made.

Even if retained leakage were zero, the present triangle envelope would
still pay E^2. That allowance exceeds the RC256 sufficient strict two-band
budget in both parities. This is a limitation of this particular bound, not
a lower bound on the actual source's outside energy and not an operator
obstruction. Fourier-aware control of the omitted physical output, or a
different response trial, is needed to pursue closure with these budgets.

## Scope and reproduction

Run from the repository root:

    python scripts/validate_rpb108_rc257_physical_source_fourier_tail.py --output certificates/rpb108_rc257_physical_source_fourier_tail.json
    python scripts/validate_rpb108_rc257_physical_source_fourier_tail.py --output certificates/rpb108_rc257_physical_source_fourier_tail.json --replay

The validator verifies 206 inherited blob pins. Replay reverses polynomial
summation and tau-search order, uses a longer base asymptotic expansion, and
requires exact equality with the stored certificate. All rounding is outward.

The full signed rank-639 response and original full auxiliary norm gate are
unevaluated. The separate finite eight-source canonical inverse width remains
485647/1000000; its one-half comparison is not the current source-response
threshold. Stage I, RH, F4 and Lean remain open/false.

Next: RC258 should resolve omitted physical source output jointly in Fourier
space or change the response trial. Reducing retained polynomial leakage
alone cannot close the current triangle-envelope budgets.
