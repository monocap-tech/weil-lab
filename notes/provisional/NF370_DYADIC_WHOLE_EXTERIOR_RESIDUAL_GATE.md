# NF370 — Dyadic directional residual gate for the **whole** original exterior

**Jurisdiction:** W-ODD-NEG remains OPEN; fixed original 242 selected directions and the unchanged original four PR348 critical functions. This is a **finite matrix preconditioning and conditional acceptance criterion**, not a computed original infinite Schur correction, strong residual or RH proof. Derived from the SHA-pinned actual original NF369 4x4 native output (artifact 12849890537, archive SHA256 1bacc7ae7967d1282eb28fd9d8566204eb21ba93246f6e81b174a18cc2ab1e96; native JSON SHA256 1b22cd77dd555749b8dcc41f92ddd91d982f2eca23ebf3a7638e512147b39d18). The entire earlier 49-file NF356–364 staging transfer remains INCOMPLETE.

## Use the existing matched *dyadic* exterior trial, not a fresh inverse

Write p:R⁴→J242 for the actual physical projections of the four critical vectors, E:R⁴→F=J242^perp for their actual physical quotients. Let c=w|F be the positive restricted complete original signed form and B(z)(v)=w(p_z,v). Its associated operator C is c's Riesz realization, NOT Q W^-1 Q. PR369 supplies an exact dyadic coefficient matrix Y0 for y_z=E Y0 z, the entire original signed selected Gram P4, and the complete *variational* trial correction

  D0 = 2 sym(B_E Y0) - Y0^T C_E Y0,
  B_E=E*B, C_E=E*C E,

all enclosed by original native intervals. Define the *whole infinite* residual functional

  R(z)(v) = w(p_z - y_z,v),  v∈F∩D(c).

For ANY such trial y, exact Hilbert-space completion of the square gives

  P4 - B*C^-1 B = (P4-D0) - R*C^-1 R.                  (1)

No assertion of Galerkin stationarity is needed: the dyadic Y0 is admissible, and its tiny nonzero matched finite inverse residual stays INSIDE R. This avoids silently swapping a rounded Y0 for an exact CE inverse. PR369's finite Galerkin upper was not a bound for the full infinite response, and (1) does not make it one.

## Certified short-dyadic anisotropic lower for P4-D0

Using the NF369 matrix intervals, their full symmetric row-error payment, and even subtracting the positive accepted finite inverse-error scalar rho, an independent *exact Fraction* 4×4 LDL proves the lower matrix A>=0. Define the explicit integer upper triangular transform

  T=(1/1048576) *
  [[1048576, -83468, 750212, -2271087],
   [0,       1048576, -1546322, -1621433],
   [0,       0,        1048576,  1115405],
   [0,       0,        0,        1048576]].

It is EXACT DYADIC, with determinant 1. Define simple rational diagonal budgets

  d = (6.5e-18, 2.7e-19, 2.1e-21, 4.9e-22)  [exact terminating rationals].

Exact 4×4 LDL, NOT floating diagonalization, proves

  T^T A T  > diag(d1,d2,d3,d4).                         (2)

The four strict LDL pivots of the difference are approximately
  (8.04747418e-19, 3.12284614e-20, 3.08459690e-22, 6.36276482e-23),
printed for orientation only; acceptance is rational.

This changes the acceptance task into *four correlated, whitened original directions*, without changing J242 or adding physical witnesses.

## Real full-infinite upper test (NOT YET MET)

Put t_i=T e_i and let ||R(t_i)||_{c*} be the exact norm in the dual of c's exterior energy space. A sufficient four-plane **whole-infinite** Schur positivity criterion is

       SUM_(i=1)^4  ||R(t_i)||_{c*}² / d_i  <= 1.         (3)

Proof: with V=[C^-1/2 R t_i /sqrt(d_i)], V*V is PSD and its operator norm ≤trace(V*V). If that trace≤1, then T^T R*C^-1 R T≤diag(d)≤T^T(P4-D0)T, and (1) gives true whole-four-plane signed positivity. This is not the full 242-dimensional acceptance.

If each residual has an actual strong exterior L² representative h_i=Q W(p_{t_i}−y_{t_i}), the older accepted floor c≥mu0||.||² with **mu0=49/50000=0.00098** gives the sufficient (not necessary) *individual* bounds

  ||h_i||² <= (mu0/4) d_i.

Numerical allowable strong-residual norms are approximately:
  i=1: 3.99061e-11,
  i=2: 8.13327e-12,
  i=3: 7.173e-13,
  i=4: 3.465e-13.

These are **future acceptance thresholds**, NOT observed original strong residuals. A single scalar floor from the worst 4×4 eigenvalue would demand ~2.4e-13 for every raw direction; the short dyadic transform relaxes the first direction by over two orders of magnitude without discarding off-diagonal matrix information.

The form-dual criterion (3) requires no strong operator domain at all, but does require a certified full exterior dual norm. The strong option requires original operator realization, cutoff tails, the complete pole and seven-prime symbol, and matched whole-frequency residuals. Both are still **UNCOMPUTED**.

## Stopping point / next action

Do not compute another 8D finite Schur or enlarge sources. Use the existing exactly specified dyadic y=E Y0 and the four rationally transformed t_i to construct a **single** certifiable whole-exterior weak residual upper (first the weakest cost direction; no assumption that its residual is small). No proof promotion. W-ODD-NEG, its remaining 238 selected directions, full even, actual-zeta transfer, and RH remain OPEN.

Replay: scripts/local_replay/nf370_dyadic_residual_budget.py, SHA-pinned original NF369 native artifact; CI is an exact-rational matrix acceptance, not the uncomputed original residual acceptance.
