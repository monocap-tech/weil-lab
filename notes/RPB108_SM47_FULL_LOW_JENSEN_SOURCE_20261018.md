# SM47 — Original full low-frequency 25-source Jensen lower

**October 18, 2026.** Stacked on SM46 draft PR #228. Canonical W-ODD-NEG odd O1/O2, even E1–E4, signed Weil positivity, CC27 and RH remain **OPEN**.

## Why the representation changes

SM46 successfully computed a *two-sided* true-original, complete 25×25 rational physical Fourier source-window approximation, with combined selected-window error **76.978784539** (true signed multiplier interpolation **45.610847484**; source Fourier integration **31.367937056**). Those 16 source-centered windows measure only **1029/64** inside the original positive low region **[0,4096]**. The bound remains too loose for a native Astar inverse.

SM47 instead certifies a **one-sided lower** for the complete low region. The already-proved SM42 Parseval floor accounts for *every* real original positive frequency in [0,4096]. Existing SM12 rigorously sign-positive real intervals supply quantitative Jensen gains; every other positive excess is discarded as **nonnegative**. The resulting positive reference is *not* added to the overlapping SM46 window matrix, preventing double-counting. This is a distinct and narrower certificate, **not a like-for-like decrease in SM46's approximation error**.

## Original physical source identity and global floor

Take all **25 actual SI10 zero-extended supported odd** source functions \(g_i\) on \([-B,B]\), \(B=11/10\): sixteen \(\sin(2\pi c_jx)\), eight \(x\cos(2\pi c_jx)\), and genuine \(s(x)=\sinh(x/2)\). Their real sine transforms and original full physical Gram are

\[
T_i(\xi)=\int_{-B}^{B}g_i(x)\sin(2\pi\xi x)\,dx,\qquad
H_{ij}=\int_{-B}^{B}g_i(x)g_j(x)\,dx
=2\int_0^\infty T_i(\xi)T_j(\xi)\,d\xi.
\]

With the **original signed seven-prime/digamma** multiplier \(m(\xi)\), define the true positive weight \(a_o(\xi)=\max\{\kappa,m(\xi)\}\), \(\kappa=10^{-3}\). On these 25 sources,

\[
A_{\mathrm{low},25}
=2\int_0^{4096}a_o(\xi)\,T(\xi)T(\xi)^T\,d\xi.
\]

The inherited SM42/SM41 exact source high-frequency tail is

\[
2\int_{4096}^{\infty}T(\xi)T(\xi)^T\,d\xi
\preceq \frac{2E}{4096}I_{25},
\qquad E=\frac{202}{25}.
\]

Thus \(A_{\mathrm{low},25}\succeq\kappa(H-2E/4096\,I_{25})\) without needing a finite-cell representation across the entire positive low spectrum.

## Additional true-positive Jensen matrix

SM12 verifies **17 disjoint original signed-positive whole-real intervals**
\(I_j=[c_j-r,c_j+r]\subset (0,4096)\), radius \(r=1/100\), with the **actual** \(m(\xi)>\kappa+\Delta\) throughout each interval, where \(\Delta=2\). Let

\[
u_j=\frac{1}{2r}\int_{I_j} T(\xi)\,d\xi,
\qquad \gamma=4r\Delta=\frac{2}{25}.
\]

Jensen on each real band, with positive integrand and disjoint interiors, yields the true operator lower

\[
\boxed{
A_{\mathrm{low},25}\succeq
\kappa\left(H-\frac{2E}{4096}I_{25}\right)
+\gamma\sum_{j=1}^{17}u_ju_j^T.}
\tag{SM47-A}
\]

**This is a complete-low one-sided source form**, not full signed odd form positivity.

## Certified exact rational 25×25 matrix

The original SM44/SM46 rational interval physical Fourier transform at band midpoint \(c_j\) provides a rational vector \(v_j\) with midpoint interval radii \(r^{(0)}_{ij}\). The exact average cancels the source frequency linear term. SM46 local true original \(T''\)/\(T'''\) identities give, on the genuine whole band,

\[
|u_{ij}-v_{ij}|
\le e_{ij}:=r^{(0)}_{ij}+\frac{K_{ij}r^2}{6},
\quad K_{ij}=
\min\!\left\{K_{i,\mathrm{global}},
|T_i''(c_j)|_{\mathrm{upper}}+r M_{3,i}\right\}.
\]

The true sinh pole uses its inherited supported \(T''\) bound; no general \(k>1\) original polynomial source is silently introduced.

Define the exact rational positive semidefinite reference

\[
P_{47}=\gamma\sum_{j=1}^{17}v_jv_j^T.
\]

With \(V_j^2=\sum_i v_{ij}^2\), \(R_j^2=\sum_i e_{ij}^2\), and exact rational upward square-root enclosures,

\[
\left\|\gamma\sum_j u_ju_j^T-P_{47}\right\|
\le\epsilon_P:=
\gamma\sum_j\left[2\sqrt{V_j^2R_j^2}+R_j^2\right].
\]

From the existing **true original** SM42 complete 25×25 physical interval Gram, construct symmetric rational \(H_q\) and \(\epsilon_H\) as the exact maximum absolute row-sum of the entrywise enclosure errors. Rigorous outward rounding is applied to the *full* error bounds **after** the Fraction estimates are derived; it must not decrease a fee.

The executable resulting all-source lower is

\[
\boxed{
A_{\mathrm{low},25}\succeq
\kappa H_q+P_{47}-
\left[\epsilon_P+\kappa\left(\epsilon_H+\frac{2E}{4096}\right)\right]I_{25}.}
\tag{SM47-B}
\]

All **625** rational source cross entries and actual sinh pole are present. The unrounded reference \(P_{47}\) is PSD by Gram structure. The displayed final lower matrix, after subtracting its complete scalar error, is **not automatically PSD**. No spectral inertia or complete inverse is inferred.

## Fail-closed numerical gates and remaining proof obligations

The validator must rerun the actual SM12 17-band original signed-positive **whole-real** certificate; prove disjointness and support inside [0,4096]; build every original SI10 source frequency mean interval and full all-cross rational matrices; retain SM42 whole-original-low Parseval floor and exact high tail; and require \(\epsilon_P<1/10\) plus at least one actual supported source-coordinate gain exceeding the **entire** outward error. No sampled Fourier or generalized eigenvalue is used to certify original sign.

The original 470 high-degree physical polynomial source transforms, pole-conditioned Astar full inverse and strong residual, entire original odd O1/O2 or exact negative-frequency Schur, even E1–E4, Weil/CC27/RH and independent original physical Fourier/closed-form-domain audit remain **OPEN**. SM47 does not determine the even/odd negative index, orthogonal remainder positivity, or effective pole compensation. SM48 should confront the new 25-source original low lower with the actual negative-cap source geometry, then extend only with a *complete-operator* residual certificate.

## Verification and source custody

Validator: \`scripts/validate_rpb108_sm47_original_full_low_jensen.py\`. Focused workflow: \`.github/workflows/rpb108-sm47-full-low-jensen.yml\`. Evidence and active obligation: \`research/obligations.json\`. The inherited original-form/closed-domain analytic equalities remain conditional premises of this machine certificate, not independently peer-reviewed mathematical proofs.

## First verified focused execution (source head 691a6043)

**GitHub Actions run [39190147371](https://github.com/monocap-tech/weil-lab/actions/runs/39190147371): SUCCESS.** Both original full-low exact rational 25-source Jensen validator and all fail-closed scope checks completed. The former initial run 39189958127 had already passed the mathematical acceptance predicates but failed solely on Python 3.11's 4300-digit integer-string serialization cap. That was corrected by outward **upward** rational quantization of the *already computed* complete error bounds before writing the 625-entry matrix. This correction does not reduce any certified fee.

- All **17 original SM12 true signed-positive REAL bands** revalidated, all on [0,4096] and mutually disjoint.
- Complete **25×25 rational lower** and **25×25 rational positive Jensen reference** formed with all original 16 sine, 8 xcos and actual sinh pole sources and cross terms.
- Full original 25-source physical Gram matrix row-sum enclosure `epsilon_H <= 39591/500000000000` (approximately 0.000000079182).
- Seventeen-source Jensen Fourier-mean Gram **full-matrix** enclosure `epsilon_P <= 32699183/125000000000` (approximately **0.000261593464**).
- Total including actual SM42 full-low Fourier high-tail `epsilon_total <= 33192357/125000000000` (approximately **0.000265538856**).
- **12 of 25 original physical source-coordinate diagonal gains** overcome this *total* scalar fee; 408 certified strict true source-local second-derivative improvements.
- These are original *one-sided* lower figures, **not comparable as the same matrix error** to SM46's 76.9788 two-sided selected-window approximation. Full 25-source spectral positivity and complete all-470 odd signed operator are not established.

**Custody:** first substantive Actions passed on source head 691a6043. This appended report and manifest reconciliation are documentation/governance changes; final post-report PR-head CI must pass separately. Independent mathematical audit and original-domain identities remain inherited premises, not freshly peer-reviewed proofs.
