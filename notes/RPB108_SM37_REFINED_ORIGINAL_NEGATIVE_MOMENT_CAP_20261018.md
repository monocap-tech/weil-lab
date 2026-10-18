# SM37 — Entire original seven-prime signed-negative cap refinement, with matched 25-source pilot comparison

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM36 PR #217.**

## Decision from genuine original SM36 pilot

The first 25 ORIGINAL supported odd source calculation (SM36 focused Actions 39166845041/39167018012 PASS) found manageable physical source Gram condition ~116 and sampled pole-free stiffness condition ~680, with finite pole Sherman–Morrison restored to ~1e−14. The original negative-frequency upper-cap sampled trial generalized maximum was 10.69–10.86 compared with a DIRECT sampled full negative Fourier response maximum 0.997–1.000 on exactly the same 25 source trial: >10× cap inflation. Both were exploratory finite Ritz results, not whole-operator proofs; the direct sampled 0.997–1.000 was itself ABOVE SM34's sufficient 51/56≈0.9107 threshold.

SM37 addresses **the certified cap itself** before requesting a 470-source positive pole-conditioned inverse with a scalar 3.11e−12 full-strong-residual budget.

## Original true whole-real frequency refinement; same 107/890 source carrier

Import the **unchanged exact SI10/SM10 original** 973 unresolved signed-negative source leaves \(\ell=[a,b]\) in 107 disjoint clusters \(J_j\), together with the certified exterior where the original multiplier \(m(\xi)>\kappa=1/1000\). Refine each original unresolved positive-half leaf into four rational subcells:
\[
[a_i,b_i]
=[a+i(b-a)/4,\;a+(i+1)(b-a)/4],\quad i=0,1,2,3.
\]

The **same original seven-prime** true signed \(m=\mathrm{arch}+\mathrm{prime}\) obeys over EACH ENTIRE REAL subcell (not a sample)
\[
m(\xi)\ge L_i:=
\mathrm{arch}_{\rm SI07}(\lfloor a\rfloor)
+\mathrm{prime}_{\rm SI06,lo}\!\left(\frac{a_i+b_i}{2}\right)
-\frac{69}{2}(b_i-a_i).
\]
The SI07 arch bound is uniform for the entire original unit frequency interval, and the signed original SI06 prime bound plus full derivative 69/2 pays the complete subcell. No original high-frequency positive arch tail is truncated by this **negative-source** refinement.

The original SM10 upper step weight on \(\ell\) was \(w_{\rm old}=\kappa+h_{\ell}\), with \(h_\ell\ge0\) an exact outward rational original multiplier-negative envelope. Define a genuinely sharpened, still conservative, nonnegative upper on each subcell
\[
\boxed{
w_i=\min\!\left\{
w_{\rm old},\;
\max\!\left(10^{-6},\;10^{-6}\left\lceil10^6(\kappa-L_i)_+\right\rceil\right)
\right\}.
}
\]
Both arguments of the minimum independently dominate the *true original* \((\kappa-m(\xi))_+\) at **every original real frequency** in the subcell, hence so does their minimum. The floor \(10^{-6}\) keeps every original cluster moment block **strictly positive definite** while permitting legitimate weights below \(\kappa\) on now-certified positive subcells. Importantly,
\[
10^{-6}\le w_i\le w_{\rm old}
\qquad(\forall\text{ original unresolved subcells}).
\]

Preserve each ORIGINAL cluster's boundary, center and SM10 exact 24-bit Taylor order \(p_j\). Thus \(\sum p_j=890\) and the physical source functions
\[
U_{jk}(x)=\frac{(2\pi x)^k}{k!}
\sin(2\pi c_jx+k\pi/2)
\]
are **unchanged**. Construct the entire new exact-rational positive cluster Hankel covariance
\[
C_{j,kl}^{\rm new}
=2\!\int_{J_j}
 w_{\rm new}(\xi)(\xi-c_j)^{k+l}\,d\xi
\quad(0\le k,l<p_j).
\]
The script computes all 107 blocks and uses exact rational LDL to check all **890 pivots strictly positive**. Since \(w_{\rm new}(\xi)\le w_{\rm old}(\xi)\) pointwise on every original signed positive and reflected negative frequency, the complete covariances satisfy
\[
0\prec C_j^{\rm new}\preceq C_j^{\rm old}
\]
in Loewner order, **including all offdiagonal original moment interactions**, not just entries or selected Ritz directions. This positivity follows from the original integral Gram difference
\[
x^*(C_j^{\rm old}-C_j^{\rm new})x
=2\int_{J_j}(w_{\rm old}-w_{\rm new})
\left|\sum_{k=0}^{p_j-1}x_k(\xi-c_j)^k\right|^2d\xi\ge0.
\]

Let \(T_{\rm new}=\sum_{\rm signed}\int w_{\rm new}(\xi)\,d\xi\), an exact rational mass no larger than SM10's old \(T\). The identical Taylor approximation remainder \(2^{-24}\), same original physical support \(B=11/10\), and unchanged SI10 whole-negative frequency support give the **new full original positive-semidefinite operator cap**
\[
\boxed{
0\preceq K_{\neg,o}
\preceq(1+\tau)U C^{\rm new}U^*+\eta_{\rm new}I,
\quad
\tau=1/1024,\quad
\eta_{\rm new}
=(1+\tau^{-1})\,2B\,T_{\rm new}\,2^{-48}.
}
\]
Because \(C^{\rm new}\preceq C^{\rm old}\) and \(\eta_{\rm new}\le\eta_{\rm old}\), this is a **complete original negative-frequency operator upper no worse than SM10** and potentially much sharper in its physical Schur/Loewner role. The original odd pole is NOT part of Kneg, and remains inside \(A_*\); no positive-frequency or whole-Weil sign is inferred.

## Matched practical numerical benchmark (noncertifying)

The same selected original 25-source SM36 trial and source-specific sampled \(\widehat Z\) are reused without refitting or changing source coordinates. Compute the three matrices with identical sampled pole-conditioned positive form:
- Old original **SM10** 890-column/107-block cap \(Z^*U C^{\rm old} U^*Z+\eta_{\rm old}Z^*Z\).
- New **SM37** exact-formula 890-column/107-block cap \(Z^*U C^{\rm new}U^*Z+\eta_{\rm new}Z^*Z\).
- Direct **sampled** original seven-prime \(Z^*K_{\neg,o}^{\rm sampled}Z\).

Compare the three complete 25×25 generalized spectral maxima against the *same* sampled positive trial matrix \(G_0=Z^*A_*^{\rm sampled}Z\), at physical grids \(4096/8192\) and independent FFT padding \(4\times/8\times\). Pilot overlaps and negative direct response are **double-precision diagnostics**, not exact-rational original physical Fourier certificates; the exact rational cap is valid only under inherited SI06/SM10 source-domain/Fourier premises.

The matched pilot also checks numerically that \(N_{\rm new}\preceq N_{\rm old}\), consistent with the **already mathematically established operator inequality**. It never interprets success of a 25-source Ritz block as global 470D original W-ODD-NEG proof.

## Scope and SM38 decision

The **new original full cap** and its exact signed multiplier real-subcell proof / exact 890 pivot LDL are the certification contribution of SM37. The numerical benchmark determines if refining existing frequency envelopes is cost-effective. If its 10× inflation materially shrinks, increase subcell refinement **selectively** where the weighted spectral response is largest; if not, investigate deeper Taylor source cap and Young splitting or a frequency-local, physical-weighted original negative response. Do NOT chase the very conservative global scalar \(\kappa_*^{-2}\) error or scale to all 470 directions until the negative cap is reasonable and the **original positive digamma logarithmic high-frequency Fourier tail and complete strong residual are certified**.

Canonical W-ODD-NEG PS36 O1/O2 complete original odd positivity, even E1–E4, full signed Weil, native CC27 D-Riesz and RH remain **OPEN**. The exact seven-prime signed support/zero-extension mathematical identification and infinite-domain assumptions require independent analytic audit.

Replay: \`python3 scripts/validate_rpb108_sm37_refined_original_negative_cap.py\`. Its output JSON in \`artifacts/sm37_refined_original_negative_cap.json\` is a *mixture* of exact-rational certified **negative-cap weights** and clearly tagged **NONCERTIFYING** sampled Ritz diagnostics. A passing CI does not establish original whole-Weil positivity.
