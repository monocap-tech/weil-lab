# MG20 — Original nonflat source excitation versus certificate-loss diagnostic

October 19–20, 2026. This diagnostic follows the verified MG18 original relative multiplier method and MG19's more stringent multiplier-envelope intersection, both scoped to the same 24 rigorously nonconstant MG17 source-frequency cells. Original W-ODD-NEG, even, Weil/CC27/RH, and independent Fourier/form-domain premises remain OPEN.

## The distinction

On 24 original physical source channels—23 MG11 exact double-boundary-vanishing supported odd generators plus genuine sinh pole—MG18's certified original \(A_o\) and \(A_o^2\) LOWER matrix references remain of exact inertia (3 positive, 21 negative, 0 zero), despite strong lower-trace improvement. The actual moment operators are positive semidefinite because they integrate positive weights against original Fourier-source rank-one covariance. The lower-reference negative directions are not actual negative modes.

There are two very different explanations for their failure to certify further positivity:

1. The selected true Fourier source functions may simply excite too few independent coefficient directions on these narrow panels. Adding numerical precision does not fix absent information.
2. The chosen panels may provide rich affine source excitation, but overly broad Fourier source Taylor and multiplier uncertainty costs bury the independent directions. Here a correlated matrix error budget is the right target.

MG20 distinguishes these possibilities for the **rational IDEAL affine reference**, not yet for the unknown true original source response.

## Exact mathematical construction

On each of exactly the same 24 MG17 certified original nonflat cells, replay the full SI10 25 original supported physical source catalog and exact MG11 dual boundary coefficients. SM44/SM46 certified original Fourier analytic intervals give rational approximation vectors \(v_j,d_j\in\mathbf Q^{24}\) to the true source value/derivative at cell center, with nonzero error radii. Those errors are acknowledged but OMITTED from the ideal-reference matrix on purpose.

For each cell, SM43A/SM46 supplies a positive piecewise-affine original multiplier reference \(w_{\rm ref}(\xi)>0\). For p=1 and p=2, its exact rational centered weighted moments are

\[
J_{k,j}^{(p)}=\int_{\text{cell}}w_{\rm ref}(\xi)^p(\xi-m_j)^k\,d\xi,
\quad k=0,1,2.
\]

The complete source-affine rational reference covariance is

\[
\mathcal R_p
=2\sum_{j=1}^{24}
\left[
J_{0,j}^{(p)}v_jv_j^\top+
J_{1,j}^{(p)}(v_jd_j^\top+d_jv_j^\top)+
J_{2,j}^{(p)}d_jd_j^\top
\right].
\]

All 24×24 source cross entries and the pole channel remain present. Because the original reference weight is positive over an interval of positive length,

\[
J_{0,j}^{(p)}>0,\quad
J_{0,j}^{(p)}J_{2,j}^{(p)}-(J_{1,j}^{(p)})^2>0.
\]

Thus the exact rank of \(\mathcal R_p\) is precisely the rank of the 48 rational vectors \(\{v_j,d_j\}_{j=1}^{24}\), independently of p. MG20 tests this with TWO entirely rational procedures: direct Gaussian elimination of the rectangular 48×24 source response array and exact rational 24×24 symmetric inertia of the complete \(\mathcal R_1,\mathcal R_2\).

The test also records midpoint-only and derivative-only exact rational ranks. It deliberately omits interval error fees from \(\mathcal R_p\); **even a positive definite ideal reference IS NOT a certified positive lower bound for the true original Fourier source moment**.

## Method-gate interpretation

- If the ideal rational combined source span is defective, first redesign the panel selection to excite more distinct original Fourier source directions. The current fixed-panel experiment cannot prove complete source coercivity with this reference alone.
- If the rational ideal span has full dimension 24, the source-response reference is rich enough in principle, so the outstanding 21 negative actual LOWER-reference directions measure certificate loss. Focus next on correlated source remainder Grammian and/or a certified preconditioner in the ideal reference geometry, not another multiplier scalar ratio.
- In either case this is a method-diagnostic result, **not a Galerkin residual, actual 470 source inverse, odd/even Weil or RH theorem**. Original infinite-dimensional complement and domains must be addressed independently.

All calculations replay the original nonflat frequency panel scout and exact physical source transforms, with no numerical eigenvalue tests substituted for rational proof.
