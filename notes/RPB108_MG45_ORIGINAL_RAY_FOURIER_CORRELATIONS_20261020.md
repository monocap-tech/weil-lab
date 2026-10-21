# MG45 — Direct original signed Fourier ray residual before absolute errors

October 20, 2026. Stacked on verified MG44 [PR #293](https://github.com/monocap-tech/weil-lab/pull/293) (accepted original actual 12-ray exact source inequalities [Actions #39542236311](https://github.com/monocap-tech/weil-lab/actions/runs/39542236311)). MG44 improved source residual UPPER projections on all 12 accepted negative Rayleigh rays, but not a single conservative source ray LOWER cleared zero. Its underlying MG24/MG29 global first/second original moment brackets, even when combined by exact block Cauchy-Schwarz, may have discarded cancellations from the original signed Fourier generator itself.

## New original-frequency source information: signed residual **before** squaring

MG45 reopens the actual physically computed original MG29/MG32 adapted Fourier source values and derivatives at all original 32 cells of the entire contiguous [0,4] positive frequency interval, with signed negative-frequency mirror, retaining:
- Original SI10's 25 physical generator catalog and MG11's 23 dual-boundary adapted plus genuine sinh pole 24D source basis;
- MG29's actual original second/third source Taylor curvature and fourth-derivative drift, **not a new approximate generator**;
- SM43's original signed seven-prime/digamma multiplier enclosure \(a(\xi)\in[a_0-\delta_a,a_0+\delta_a]\);
- Original true rank-one odd sinh-pole correction \(2e_p b^\mathsf T B\), with independently certified original physical Gram column \(b_i=\langle s,F_i\rangle\in[b_{0,i}\pm \delta_{b,i}]\).

On each actual original frequency cell, let the row of the original adapted physical Fourier source be \(t(\xi)=v+d h+e(\xi)\) with \(|e_i(\xi)|\le r_i\), \(|h|\le \ell/2\). For a fixed exact original rational source direction \(z\), let \(u=Bz\) and define the exact central signed response vector \(C_0z=z-a_0u+2e_p(b_0\cdot u)\). Then the **actual signed scalar residual** is
\[
r_z(\xi)=t(\xi)\cdot[z-a(\xi)u+2e_p(b\cdot u)].
\]
The true affine nominal values are \(c=v\cdot(C_0z)\), \(d_z=d\cdot(C_0z)\). Rather than independently taking an absolute error for each transformed output coordinate and then multiplying by \(|z_j|\), a single exact rational *new* remainder bound holds:
\[
\begin{aligned}
\rho_z={}&\sum_i r_i |(C_0z)_i|\\
&+\delta_a\left(|v\cdot u|+\frac\ell2|d\cdot u|+
    \sum_i r_i|u_i|\right)\\
&+2\left(|v_p|+\frac\ell2|d_p|+r_p\right)
\sum_i\delta_{b,i}|u_i|.
\end{aligned}
\]
All absolute values in this expression are taken **after** the corresponding signed original source vector contractions, preserving cancellation in \(v\cdot u\) and \(d\cdot u\). The exact original physical pole is included **before** bounding any squared residual.

Using \(|r_z(\xi)-(c+d_zh)|\le \rho_z\), exact affine integration and the ±frequency mirror give the new TRUE ORIGINAL scalar cell covariance upper:
\[
U_{z,\mathrm{cell}}=
2\ell\left(c^2+\frac{\ell^2d_z^2}{12}
+2\rho_z\left(|c|+\frac\ell2|d_z|\right)+\rho_z^2\right).
\]
MG45 independently reconstructs the old componentwise projected MG32 radius \(\rho_\mathrm{coord}(z)=\sum_j |z_j|\,\rho_j^{\mathrm{MG32}}\) for **every** source ray/cell and verifies \(\rho_z\le\rho_\mathrm{coord}\) in exact Fraction. Thus each projected true original scalar cell upper never worsens when the new cancellation is retained.

## Full original frequency accounting: no hidden omitted spectrum

Let \(H_{C,\mathrm{lo}}\) be MG32's independently verified actual [0,4] source mass lower, and \(H_{\mathrm{up}}\) the full original physical source Gram upper. Outside the measured [0,4] band, MG45 inherits and **recomputes** the independently accepted MG32 rank-one-pole-corrected complete-real-frequency remainder Loewner upper, using \(H_{\mathrm{up}}-H_{C,\mathrm{lo}}\), SM41 original strong high-frequency tail, and all nested Young/pole uncertainty fees. It does not double count measured bands or drop the tail.

For each ray \(z\) the new COMPLETE-frequency upper is \(\sum_{32\text{ cells}}U_{z,\mathrm{cell}}+z^\mathsf T U_{\mathrm{MG32,rem}}z\), which is independently valid on the true original \(R(B)\) covariance. Also MG44's accepted whole-source ray upper is valid on the SAME original residual, so its scalar MIN with the newly computed whole-frequency upper is valid. This is **not** a full 24×24 matrix Loewner intersection.

## Exact original test set

The code tests three independently accepted nonzero original rational source rays per each four mesh/cutoff cases (16/32 × \(2^{12}\)/\(2^{16}\)): the archived MG43 strict negative ray, the MG41 actual fee-bearing negative ray, and MG42's upper fee threshold negative ray. The four original MG43 accepted nonscalar response matrices \(B\) are unchanged. There are 12 rays ×32 actual original frequency cells = **384 signed original-source frequency-cell inequalities**.

A second independent validation script (which does not import MG45's computational functions) recomputes each physical source frequency cell via MG32's accepted MG29 generator, every \(\rho_z\), old projected radius, scalar whole cell integral, physical pole term, independent MG32 [0,4]-complement, and inherited MG44 whole ray bound, all with exact rational arithmetic. The final output reports (i) strict source-cell improvements, (ii) strict full-frequency source-ray upper improvements vs MG44, and (iii) nonnegative directional source-lower margins, without promoting one-ray information to all 24D.

This constitutes **genuinely new direct original correlated source-residual information**, not a reweighting of MG24/MG29 matrix intervals and not an unjustified reduced mixed-\(G\) fee. Still no independent Fourier/form-domain identification, finite-source invariance, original all-470 inverse, signed odd 51/56 cap, even/Weil/CC27/RH or RH. All remain OPEN.

## Disposition

Independent original Actions: PENDING.
