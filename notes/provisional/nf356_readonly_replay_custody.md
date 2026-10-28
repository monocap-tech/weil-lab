# Weil-Lab — NF356 read-only independent-replay custody (local v2)

**Date:** 2026-10-27 (user-local research date).  **Repository:** `monocap-tech/weil-lab`.
**Reference:** draft PR #355; PR #356 remains unpublished. **No repository writes.**

## Entry conditions

Retain the *original* odd signed physical supported carrier, the true pole,
original multiplier and its complete seven-prime term, original selected
J242 physical complement (241 derivatives + pole). Inherited original
multiplier/Fourier form realization and domain remain a separate OPEN audit.

Archive SHA256 pins: `pr350-certificate.zip` `3389809c3a01c223b95e9dc96ea7c9dd776cb83049bb2d93a3c9d9bbad45af09`, `pr346-affine.zip` `c853b66001e3a36346ce1310df3b60ca694b3b458e8d658a3e6955cf5a14291e`, `pr355-exterior.zip` `f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0`.
The original selected-rank JSON SHA256 is `9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2`.

## Newly completed LOCAL independent checks

1. Recomputed all **62,272** old-cover native endpoint cells using exact rational
   arithmetic, retaining 136 unresolved threshold cells conservatively. Exact
   J242 scalar Fourier-Taylor zeros give
   `Q 1_{m<.01,old-cover} Q <= 0.000234139304421 Q`.
2. Independent *directed-rounding MPFR* (192-bit ctypes, **not mpmath.iv or Arb**)
   proves every one of **107** uncovered frequency gaps on [0,1300] has
   `m(x)>0.0125662247`. It checked **14324** subintervals using
   the original seven-prime multiplier, an explicit Binet/digamma lower,
   and inherited `|m''|<2145`. Interval argument ranges paid using cos 1-Lipschitz.
3. Exact rational Binet recurrence, independently from the finite gaps, gives
   `m(x)>0.039222083` for x>=1300. This **replaces** the earlier
   high-tail statement `m>0.0699` with a weaker but fully explicit bound.
4. With inherited `Q(0.001-m)_+(D)Q <= epsilon Q`, rational recomposition gives
   `Q W_o Q >= 0.0099811248731 Q >0.00998 Q`.
5. Exact dyadic *full 4×4* native matrix comparison proves
   `0.00998 H_phi - N_low > (1/500) I`. The native entry radii are paid;
   full rational LDL passes. **N_low is a lower, not upper, estimate on B*B**.

## Jurisdiction and stop

The previous #355 lower-matrix witness obstruction is removed by the stronger
floor, including its off-diagonal couplings. This does **not** establish
`B*B <= 0.00998 M`, and does **not** bound the full infinite Schur correction
`B* C_Q^(-1) B` from above. The four-probe Schur computation remains a
Galerkin lower approximation only. The original form / operator realization
and form-core audit remain open.

This is a **LOCAL independently replayed conditional Fourier exterior-floor
candidate**, not an accepted GitHub/Arb CI artifact. No new source direction,
complete inverse, new branch, commit, or PR has been created.

**Next necessary typed obligation:** a complete strong coupling upper (or
matched energy-dual residual upper) on the same finite selected energy source
frame, with the untested infinite exterior paid explicitly. Prefer testing a
feasibility budget against the ~0.002 scalar lower-matrix slack before
another precision or dimension campaign. If the upper route is not
possible, stop and return to energy-resolved Schur instead.

**Status:** `W-ODD-NEG=OPEN`; full original RH=OPEN.
