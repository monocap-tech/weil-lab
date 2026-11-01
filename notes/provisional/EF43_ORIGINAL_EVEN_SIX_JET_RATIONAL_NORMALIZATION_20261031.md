# EF43 — Exact rational normalization of the same six genuine original even SI10 source jets

**2026-10-31. Canonical `W-EVEN-FORM` remains OPEN.** Parent EF42 [draft PR #451](https://github.com/monocap-tech/weil-lab/pull/451), final-head native [Actions #41269577940](https://github.com/monocap-tech/weil-lab/actions/runs/41269577940) SUCCESS. Original first SI10 c0=37/64 source Taylor order 15; six authentic first protected real-even source jets v0=cos, v1=x sin, v2=x²cos, v3=x³sin, v4=x⁴cos, v5=x⁵sin on [-11/10,11/10]. No 469-source replacement; actual original 107 clusters and 469 protected real-even source rows unchanged.

## 1. The representation problem: small monomial pivots are not source-sign evidence

EF42 certified the physical six-jet Gram via directed outward original SI06/EF24/EF29 data. The successive Gram pivots are approximately (1.2363494115, 0.28829890668, 0.16703295695, 0.027484393523, 0.00068092005019, 0.000010037139187). All positive, but the last is far smaller than the first. This demonstrates poor direct *monomial jet* normalization, not degeneracy of the actual six-dimensional source subspace and not an original Weil-form obstruction.

EF42 also certified original full signed physical first-source response H40=z+h40, where z retains ALL seven genuine signed prime-power translated cutoffs n2,n3,n4,n5,n7,n8,n9 and the real positive even pole, while h40 is the first 40 actual quarter-digamma physical cutoff modes with the complete signed original 40x40 Laplace Gram. Original EF42 first-six-source finite L2 projected squared residual D6≈0.040533054506<41/1000. Original infinite arch cutoff m>=40 remainder had L2 norm <57/500+1/10000; original full cofinite ||P_F g_e||<8/25 and unseen energy dual eta<2560/17, still far above EF33 restricted S2>1/500.

## 2. EXACT source-span-preserving rational basis, not approximate source functions

Let G_ij=<v_i,v_j> be the authentic original six-source physical L2 Gram, with native outward fixed-point 10^340 endpoints. EF43 quantizes each G midpoint only to SELECT a rational basis, never to justify a result about the original form. With rational arithmetic, perform six Gram–Schmidt steps on this rational midpoint Gram and use rational near-unit normalizations. This produces an EXACT rational lower-triangular 6x6 matrix C with every C_ii>0; hence

\[
w_i=\sum_{j\le i}C_{ij}v_j,\qquad
\mathrm{span}_{\mathbb R}\{w_0,\ldots,w_5\}
=\mathrm{span}_{\mathbb R}\{v_0,\ldots,v_5\}\subset V_{469}.
\]

The latter identity is exact because C has rational coefficients and nonzero diagonal, regardless of how the approximate midpoint was selected. No physical cutoff, original source row, or signed operator is replaced.

The actual transformed physical Gram K=C G C^T is then recomputed with the ORIGINAL outward intervals, not the quantized midpoint. The intended strict acceptance is a direct original finite-dimensional uniform row-sum bound

\[
\delta=\max_i \sum_j |K_{ij}-\delta_{ij}| < 10^{-7}.
\]

Because K is real symmetric, this implies the original transformed source Gram eigenvalues are in [1-10^-7,1+10^-7]. In particular it is positive definite, and the new representation is well-conditioned in its own physical coordinates. This is distinct from the conditioning of the exact transformation C from unnormalized monomial jets, whose coefficient growth must also be disclosed.

## 3. Independent original signed physical projected-response certificate

Define the genuine full signed six-pairing vector b_i=<H40,v_i> as independently source-certified by EF42, and h=C b. Since K is positive definite and exactly the transformed Gram,

\[
D_6=\|H40\|^2-h^T K^{-1}h.
\]

The symmetric certified order \((1-\delta)I\preceq K\preceq(1+\delta)I\) yields WITHOUT forming K inverse:

\[
\|H40\|^2-\frac{\|h\|^2}{1-\delta}
\le D_6\le
\|H40\|^2-\frac{\|h\|^2}{1+\delta}.
\]

EF43's acceptance requires strict outward interval verification of BOTH bounds, consistency with EF42's independently obtained monomial Schur D6, and a quantitative improved enclosure D6<4054/100000=0.04054. The latter tighter bound is not an extra projection: it only improves the explicit certified ROUNDING of the same authentic six-jet source projection.

With original unchanged full infinite arch tail, the sharper sufficient gate would give

\[
\|P_Fg_e\| <
\sqrt{0.04054}+0.1141
<0.20135+0.1141 <79/250=0.316,
\]
\[
\boxed{\eta< (79/250)^2/(17/25000)=12482/85\approx146.84706}.
\]

This remains very far above EF33 S2>1/500. Any claim of these strict improvements is conditional on the focused exact-native CI assertions passing, and separately on the inherited original Fourier/physical digamma and cofinite form-domain attachment being valid.

## 4. The obligation interface and next advancement

This would close an **original-source representation/conditioning checkpoint**: an explicit invertible rational transformation of the EXACT six genuine original source directions, outward-certified Gram near identity and a separate signed projected-response inequality obtained without a numerically inverted Gram. It DOES NOT create a new source direction or compute the full 469-source projection, actual q-energy Riesz inverse, original complete even Schur sign, or whole Weil/RH.

**EF44** should use the verified orthogonalized six-jet architecture to attempt one or two additional GENUINE original first-center jets (e.g., x^6 cos, x^7 sin) with explicit transformation coefficient growth and interval row-defect budgets. If the exact map becomes impractical despite normalized Gram, record a conditioning/method STOP and reassess basis choice before continuing. Neither method status changes the active `W-EVEN-FORM` obligation.

Native validator: `scripts/validate_rpb108_ef43_original_even_six_jet_rational_normalization.py`; dedicated workflow `.github/workflows/ef43-original-even-six-jet-rational-normalization.yml`. No main merge, no original historical overwrite, no RH claim.
