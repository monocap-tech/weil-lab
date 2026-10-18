# SM36 — Practical original-operator pilot: actual source geometry, numerical Fourier stiffness and 890-column coupling

**October 18, 2026 · canonical W-ODD-NEG · stacked on SM35 draft PR #216 (focused CI PASSED).**

**Scope: engineering feasibility, NOT a rigorous positivity or interval spectral certificate.** The central goal is to transition from SM35's full-coupled 470-source *acceptance theorem* to evaluations of **actual original physical functions**, and determine whether the existing numerical route is stable enough to justify an expensive full-source certified computation. The first pilot samples 16–32 true original SI10 source functions from clusters throughout the entire negative-frequency range, including near the previously problematic \(14.42\), \(389.56\), and \(882.91\) physical frequency neighborhoods, plus the genuine original odd pole vector \(s(x)=\sinh(x/2)\). It also builds **all 890 original negative-cap Taylor synthesis columns** and their original 107 moment blocks against the pilot solve. No false whole-operator sign can be promoted from this subset.

## 1. Concrete numerical representation of the **original** multiplier

On the original physically supported odd carrier \(L^2([-11/10,11/10])_{\rm odd}\), the original CC27/SI06 seven-prime signed real multiplier is evaluated in exploratory double precision as
\[
m(\xi)=\Re\psi\!\left(\tfrac14+i\pi\xi\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\log p(n)}{\sqrt n}\cos(2\pi\xi\log n),
\]
where \(p(2)=2,p(3)=3,p(4)=2,p(5)=5,p(7)=7,p(8)=2,p(9)=3\).
It is checked **against known original sign anchors** \(m(0.3)>1.4\), \(m(389.38)>2\), \(m(389.56)<-0.4\), \(m(389.75)>2\), and \(m(882.91)<-0.08\). These are numerical **consistency checks** on the formula, **not fresh all-real interval proofs**. The existing SI06–SI10 exact-rational signed intervals remain the rigorous source of that information.

The original positive pole-free and signed negative frequency weights are
\[
a_o(\xi)=\kappa+(m(\xi)-\kappa)_+=\max\{\kappa,m(\xi)\},
\qquad
k_-(\xi)=(\kappa-m(\xi))_+,\quad \kappa=1/1000.
\]
The pilot constructs Fourier quadratures of **the original physical source functions** with these sampled multiplier values, but explicitly labels every resulting stiffness matrix as approximate because neither the infinite logarithmic archimedean tail nor frequency-grid quadrature has been rigorously enclosed.

**Critical detail:** physically supported transforms are nonperiodic. Increasing only the number of physical samples **does not refine the frequency spacing** if the FFT interval stays length \(2B\); the pilot independently varies zero padding \(4\times,8\times\) and physical grid resolution to identify alias/truncation dependence. The continuous original \(|\xi|\to\infty\) logarithmic positive tail remains to be paid in SM37. In particular the original SI06 cutoff at 896 concerns **negative-frequency support only** and does **not** truncate positive \(a_o\).

## 2. Conditioning and rank-one pole restoration without a second solve

Construct exact-formula, exploratory-float physical odd source columns \(V\) for the selected genuine original SI10 parity Taylor generators:
\[
w_{jk}(x)=
\begin{cases}
x^k\sin(2\pi c_jx),&k\text{ even},\\
x^k\cos(2\pi c_jx),&k\text{ odd},
\end{cases}\qquad s(x)=\sinh(x/2).
\]
The pilot reports the physical Gram conditioning \(\operatorname{cond}(V^*V)\), pole-free stiffness conditioning, Fourier Parseval consistency, signed-multiplier normalization, and convergence across grid parameters. **All selected source directions are retained; no singular values are silently truncated.**

For each sampled \(A_o^V\), let \(b=V^*s\) and \(H=V^*V\). Compute the finite-source pole-free solve \(X_0=(A_o^V)^{-1}H\), \(u=(A_o^V)^{-1}b\), and its *trial* rank-one denominator
\[
\tau_V=1-2b^T(A_o^V)^{-1}b.
\]
If \(A_o^V\) and \(A_o^V-2bb^T\) are numerically SPD, the pilot compares the direct source solve with
\[
\boxed{
X_*=
X_0+\frac2{\tau_V}\,u\,(b^TX_0)
}
\]
using the same physical source space. **The finite trial \(\tau_V>0\) is not a proof of the exact infinite-dimensional \(\tau=1-2\langle s,A_o^{-1}s\rangle>0\)**; the original SI29 pole-only certificate remains the separate rigorous premise.

## 3. Entire ORIGINAL SM10 negative-cap block response on the pilot solve

For each of SM10's genuine **107 original signed-negative clusters**, evaluate the original physically supported Taylor synthesis
\[
U_{jk}(x)=\frac{(2\pi x)^k}{k!}
\sin(2\pi c_jx+k\pi/2),
\]
with the true original 24-bit Taylor orders totaling **890 source columns**. The exploratory pilot forms the full *rectangular* physical overlap \(U_j^*Z\) against **every selected source solve column** and builds original block quadratures for
\[
D_j=(1+\tau)\left[
2\int_{J_j}\bigl(h_j(\xi)+\kappa\bigr)
(\xi-c_j)^{k+l}\,d\xi\right]_{k,l},
\quad \tau=1/1024.
\]
Every original 973 dyadic leaf is included in its correct block. The pilot then accumulates
\[
\boxed{
\widehat N_0^{\rm trial}
=\sum_{j=1}^{107}(U_j^*Z)^*D_j(U_j^*Z)
+\eta Z^*Z,
}
\]
including SM10's global infinite-frequency/cross residual \(\eta\) as defined by the original exact arithmetic. **Block entries and physical overlaps are computed in float64 and are NOT yet outward rigorous**. Numerical generalized eigenvalues of \((\widehat N_0^{\rm trial},G_0^{\rm trial})\) are reported for feasibility, **not accepted as whole odd spectral evidence**. Even if all are below 51/56, the entire actual 470-source strong residual and high positive archimedean tail are unmeasured.

The original exact SM10 moment-block LDL certificate, original 973 leaves and signed support proofs are **not replaced** by exploratory numerical quadrature.

## 4. Fail-closed experiment and decision

Run \`python3 scripts/sm36_original_odd_numerical_pilot.py\`. GitHub Actions sets up NumPy/SciPy and writes per-grid JSON metrics as a retrievable workflow artifact; the workflow retains all canonical W-ODD-NEG O1/O2 and RH obligations explicitly OPEN. Run variants cover physical 4096 and 8192 grids, \(4\times\) and \(8\times\) Fourier zero padding, with all pilot original source vectors, original pole and 890-column negative moment blocks.

Interpretation:

- **Pilot succeeds numerically:** source Gram conditioning is manageable or its failure isolated; sampled original Fourier stiffness, finite pole restoration, original block overlaps and selected generalized spectrum can be reproduced under grid refinement. Proceed SM37 to **actual rigorous** archimedean tail/physical cross integral enclosures and an original strong Galerkin residual, before any full 470-source acceptance.
- **Pilot fails conditioning or quadrature convergence:** first rescale and orthogonalize source block coordinates with certified transformations preserving original directions, and/or replace the scalar \(\kappa_*^{-2}\) residual bound by a weighted original negative-frequency-resolved norm. Do not increase the source count to 470 until the single-block numerical stability is understood.
- **Pilot run passes CI:** it establishes engineering execution of original-source formulas and comparison diagnostics **only**, not any real-frequency tail, exact operator sign, O1/O2, even sector, whole Weil, CC27 or RH.

**Important honesty:** An apparent generalized eigenvalue above \(51/56\) here is also **not** a rigorous obstruction to positivity of the original operator: it could reflect the 890-source upper cap, a low-dimensional Galerkin reference, missing residual corrections, or numerical quadrature error. A value below \(51/56\) is **not** a proof either.

**SM37** should prioritize: (i) a rigorous analytic representation and certified tail for the original unbounded archimedean positive Fourier form; (ii) verified physical Gram/source coordinate conditioning and pole-resolvent interval; (iii) a useful frequency-weighted **strong residual** with actual original \(A_o\), then (iv) scale to all 470 odd source generators only if proven feasible. No guarantee of RH is claimed.


## 5. First actual original numerical pilot — reported measurements (run 39166845041, PASSED)

The GitHub Actions pilot ran the **actual SI10 source formulas**, selected **25 real original supported odd source directions**, computed the **original 107-block/890-column physical overlap and moment-cap response**, and uploaded the JSON diagnostic artifact. The original multiplier sign anchors matched their previously certified sign directions; the *exploratory double-precision* numerical measurements were:

| Pilot quantity | 4096 physical / ×4 FFT | 8192 physical / ×4 FFT | 8192 physical / ×8 FFT |
|---|---:|---:|---:|
| Original selected physical source count | 25 | 25 | 25 |
| Physical source Gram condition | 115.599 | 115.601 | 115.601 |
| Sampled pole-free positive stiffness condition | 676.284 | 676.070 | 687.503 |
| Parseval grid consistency relative error | \(1.16\times10^{-15}\) | \(1.24\times10^{-15}\) | \(7.59\times10^{-16}\) |
| Trial pole denominator \(\tau_V\) | 0.640678 | 0.640693 | 0.633099 |
| Direct vs Sherman–Morrison finite pole solve difference | \(7.17\times10^{-15}\) | \(2.77\times10^{-15}\) | \(9.10\times10^{-15}\) |
| Sampled original pole-restored smallest generalized trial stiffness eigenvalue | 0.452711 | 0.452713 | 0.443207 |
| Complete original SM10 **cap** sampled trial generalized eigenvalue max | **10.68820** | **10.68820** | **10.86386** |
| Cap vs sampled direct negative matrix relative Frobenius difference | **8.309** | **8.309** | **8.415** |
| Original cap columns / covariance blocks | 890 / 107 | 890 / 107 | 890 / 107 |
| Original exact-formula \(\eta\) included in float cap | \(3.01436\times10^{-10}\) | same | same |

**Interpretation and critical practical redirection:**
- The selected original source space is **not ill-conditioned enough to explain current failure**: physical Gram \(\sim116\), sampled stiffness \(\sim680\). This does NOT establish conditioning for all 470 source directions, which could be much worse.
- The Sherman–Morrison **algebra and implementation** agree within floating roundoff on the selected finite trial. The *true infinite-dimensional pole correction* remains separately certified only by SI29.
- The negative 890-source **upper-cap trial** has generalized max \(\sim10.7\)-10.9, far **above** SM34's sufficient true generalized threshold \(\theta=51/56\approx0.911\). This **does not prove that the true original odd operator is indefinite**; it is a very conservative cap tested on incomplete, sampled Galerkin solutions and lacks the actual strong residual.
- The conservative cap is numerically substantially larger than the **direct sampled original negative-frequency matrix**, relative Frobenius discrepancy \(>8\). Thus blindly tightening the \(10^{-12}\)-scale positive-resolvent scalar residual would **not** be a sensible first use of compute. The cap's sharpness and direct-negative physics must be separated.
- Doubling physical resolution at fixed padding barely changes the spectral metric here, whereas **doubling Fourier zero padding** shifts the cap generalized eigenvalue from 10.688 to 10.864 and the finite pole denominator from 0.64069 to 0.63310. This diagnoses finite-frequency quadrature/aliasing sensitivity. More stringent independent padding convergence and a rigorous Fourier-grid integration/tail enclosure are needed.

The original \(m(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi+\text{seven signed prime terms}\) has logarithmic positive high-frequency growth. None of the above sampled values constitutes a complete original \(A_o\) form, a verified \(A_o^{-1}\), or a rigorous high-frequency tail approximation. The Parseval consistency check verifies FFT bookkeeping **only**.

**Immediate next computation:** the pilot implementation is being extended to report the **direct sampled negative-frequency generalized maximum** next to the conservative 890-cap maximum on the *same* selected trial. That isolates cap inflation from sample-space spectral difficulty. If the direct-negative trial also exceeds \(51/56\), enlarge/recondition the *actual Galerkin trial* and refine the original positive-frequency quadrature; if the direct-negative trial is low but the cap remains high, sharpen original negative cap weights with signed real-frequency subcell enclosures or a complete negative-frequency-weighted inverse error rather than overrefining the positive solve. Either way, the **complete 470D original interval Loewner** remains unmeasured.
