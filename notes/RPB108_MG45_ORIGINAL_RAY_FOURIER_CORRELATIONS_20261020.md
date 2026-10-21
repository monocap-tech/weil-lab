## MG45 accepted genuine-original source Fourier result — October 20, 2026

[MG45 original physical Fourier calculation AND independent exact-rational replay, Actions #39544081287](https://github.com/monocap-tech/weil-lab/actions/runs/39544081287) **PASSED** on the corrected source head. The first workflow attempt #39543982157 failed at synthetic self-test only because a stale implementation variable reference \`mg_B\` had not been replaced with the explicit general original B; the corrected run successfully passed the self-test and both original-data calculation and independent audit.

Accepted output artifact: \`mg45-original-signed-source-Fourier-ray-384-cells\` **ID 12320672115**.

| Original MG29 mesh | cutoff k | Genuine rational rays tested | Strictly sharper original signed [0,4] Fourier-cell covariance bound | STRICTLY sharper COMPLETE-frequency bound than MG44 | Nonnegative certified complete source-ray lower |
|---|---:|---:|---:|---:|---:|
| 16 | 12 | 3 | **3/3** | **0/3** | 0/3 |
| 16 | 16 | 3 | **3/3** | **0/3** | 0/3 |
| 32 | 12 | 3 | **3/3** | **0/3** | 0/3 |
| 32 | 16 | 3 | **3/3** | **0/3** | 0/3 |
| **Total** | | **12** | **12/12** | **0/12** | **0/12** |

The independently coded verifier rebuilt all **384** original 32-cell signed physical Fourier source residual inequalities and all four genuine-pole complete-frequency MG32 omitted-frequency Loewner complements, and checked every computed scalar and original response B/source direction with exact Fraction. The independently certified analytic cell bound preserves source-vector cancellation \`v·Bz\` and \`d·Bz\` before taking original SM43 multiplier interval error absolute values; its original source error radius is strictly smaller than the accepted projected old MG32 coordinatewise radius on all 12 tested rays at the integrated-prefix level.

**Method limitation now isolated:** Direct original signed \`[0,4]\` source Fourier correlation measurably improves the low-frequency component of each tested source residual, but the independently accepted **remaining-frequency** MG32 mass/SM41/pole Young upper is too costly to make the resulting complete-frequency scalar residual upper smaller than MG44's separately valid complete-source bound. MG45 accepts only the scalar minimum of two independent full-real-frequency source uppers and therefore reports **zero complete-frequency improvement** and **zero directional source positivity** for all tested rays.

This is a new, rigorous **physical original Fourier source-row** calculation, not an algebraic reweighting of existing first/second global moment matrices, but **it is still only source-ray scoped**. In particular, there is NO new simultaneous full24 Loewner upper from 12 scalar tests, no proof of original all-470 strong inverse or signed 51/56 odd cap, no independent Fourier/form/domain, no complete even/Weil/CC27/RH, and certainly no RH theorem.

**MG46 next acceptance target:** Improve the ACTUAL original omitted-frequency source residual covariance in a way that **subtracts already measured frequency mass from the remainder without double-charge** and retains the signed joint residual. MG35/MG37 established that naively adding another PSD measured-band upper while retaining MG32's untouched remainder cannot improve in Loewner order. Future work must demonstrate a genuine smaller original missing-frequency full24 matrix, or new complete-spectrum coupled source variance information; not more local [0,4] radius tuning.

---

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

Independent original Actions PASSED; verified 384 true original signed source-cell inequalities, 12 improved prefixes, no full-frequency gain or source contraction.
