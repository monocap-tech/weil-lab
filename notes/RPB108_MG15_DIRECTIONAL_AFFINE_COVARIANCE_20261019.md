# MG15 — Exact directional original-source affine covariance gate

October 19, 2026. Stacked on MG14 #263, final Actions 39346488631 PASSED. Original W-ODD-NEG, complete even, Weil/CC27 and RH remain OPEN. Full original 470 source Astar resolvent and independent Fourier/form-domain audit remain OPEN.

## Concrete reason for changing the lower reference

MG14 improves both actual physical 24-channel, 24-real-frequency-panel positive source moment REFERENCES from inertia (2+,22−,0) to (3+,21−,0), with positive total lower reference traces. The **actual** source moment is PSD because it integrates a nonnegative original positive Fourier multiplier, but the conservative rational lower-reference matrix remains indefinite with 21 negative directions. This is a limitation of the certificate, not any negative mode in the actual operator.

MG14 pays every Fourier Taylor covariance direction the same scalar cost delta*I24. MG15 instead retains the genuine 24 SOURCE-DEPENDENT interval radii: on each actual source-frequency cell T(xi)=V(xi)+e(xi), V(xi)=v+d*(xi−mid), with |e_i(xi)|<=r_i, from exact original SM44/SM46 source transforms, MG11 endpoint-cancellation coefficients, and actual sinh pole.

## Valid original full-matrix source-weighted enclosure

Write S=sum_i r_i and D=S*diag(r_1,...,r_24). Weighted Cauchy gives, for every vector z,

   (z^T e)^2 <= (sum_i r_i)*(sum_i r_i z_i^2) = z^T D z.

Therefore 0<=e e^T<=D in LOEWNER order. This DOES NOT discard true source cross terms or claim e e^T diagonal.

For rational 0<tau<1, the whole matrix Young inequality is

   -tau V V^T - tau^-1 e e^T
   <= V e^T + e V^T
   <= tau V V^T + tau^-1 e e^T.

Adding V V^T+e e^T gives the precise positive-directional sandwich

   (1−tau)V V^T − (tau^-1−1)D
   <= T T^T
   <= (1+tau)V V^T+(1+tau^-1)D.

Integrate on each symmetric cell of width h. The original affine reference covariance is exactly C=vv^T+(h²/12)dd^T. MG13/14's true original digamma plus all-seven-prime, kink-safe entire-frequency multiplier bounds 0<l<=a_o(xi)<=u imply

   2h l [(1−tau)C − (tau^-1−1)D]
       <= 2 int_cell a_o(xi) T T^T dxi
       <= 2h u [(1+tau)C+(1+tau^-1)D],

and separately with (l²,u²) for the actual A_o-squared strong action source moment. Every 24x24 source cross remains in the v and d rank-one matrices, original sinh pole included.

This test deliberately retains the original SM43 cell weight intervals, source geometry, MG11/12 physical basis and exact 24 panels. The only changed estimator is the positive-semidefinite uncertainty geometry: a source-dependent D replaces the scalar delta*I.

## Falsifiable method comparison

The exact-rational validator executes the entire MG14 calculation and independently reconstructs its 24x24 LOWER and UPPER matrices entry for entry on both moments before accepting any new result. It then computes seven independently valid directional candidate families tau=1/64,1/32,1/16,1/8,1/4,1/2,3/4; one trace-optimal directional family per panel, and an adaptive scalar-vs-directional family per panel. Selection maximizes **only the source lower TRACE**, never assumes cellwise Loewner dominance. Each selected full 24x24 lower AND upper source matrix independently encloses the actual moment.

Every final source matrix has outward rational export fees and an exact rational 24D spectral inertia computation, including all negative lower reference directions. The regression uses exact Fraction 3D nonzero signed source-vector errors to check both sides of the Young+diagonal D inequality independently.

Acceptance: materially improve the lower-reference negative inertia (below 21) or at least shrink the negative spectral charges/margins at fixed 24-panel cost. It is equally acceptable to conclude this strategy fails; then the next investigation should use SM46 weighted J0,J1,J2 source moments or a *matrix correlated residual Gram* rather than add source count or panels.

Only 24 selected physical original frequency cells are enclosed. The complete low-band [0,Lambda], Astar² pole response, true original 23D Galerkin strong residual, entire 470 original odd operator and even/Weil/CC27/RH remain OPEN. No true negative eigenvector can be inferred from lower-reference inertia.

Reproduction:
OPENBLAS_NUM_THREADS=2 OMP_NUM_THREADS=2 python scripts/validate_rpb108_mg15_directional_affine_covariance.py


## Measured MG15 result and acceptance

GitHub Actions [39350281314](https://github.com/monocap-tech/weil-lab/actions/runs/39350281314) PASSED the full 24-channel original two-moment rational calculation, exact MG14 all-576-entry matrix replay, weighted Young regression, independently reconstructed source-affine panels, and exact 24D rational lower inertia for all candidates.

The source-dependent diagonal error bound is selected instead of the MG14 scalar error on ALL 24 original real-frequency cells in BOTH moments.

| Original source moment | MG14 lower trace | MG15 adaptive lower trace | MG14 upper trace | MG15 adaptive upper trace |
|---|---:|---:|---:|---:|
| A_o source first | +0.000922070208 | +0.001186541164 | +0.001562232156 | +0.001299148280 |
| A_o² source second | +0.000000886848 | +0.000001149424 | +0.000001594504 | +0.000001332340 |

Despite these rigorous matrix enclosure trace improvements, exact affine-reference lower inertia remains **(3 positive, 21 negative, 0 zero)** for BOTH moments. MG14 was already (3+,21−,0). The source-dependent error family therefore improves **trace and interval width but NOT the accepted spectral positive-direction count** in the selected trace-maximizing policy. Other tau candidates are recomputed and their exact reference inertias exported independently for diagnosis.

**MG15 method decision:** ACCEPT the validity and modest improvement of source-directional full Loewner errors; DO NOT promote positive trace to positive definiteness or infer actual negative source eigenmodes from conservative negative references. The next method should target spectral weak directions directly, using SM46 weight moments J0,J1,J2 and source-correlated remainder Gram / preconditioned matrix enclosures rather than further splitting every error into an identical scalar or diagonal source fee. The complete frequency band, actual Astar² original pole response, full source470 strong inverse/negative cap, canonical odd/even, Weil and RH remain OPEN.
