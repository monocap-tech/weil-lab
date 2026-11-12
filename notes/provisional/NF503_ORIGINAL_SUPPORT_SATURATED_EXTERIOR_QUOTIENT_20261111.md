# NF503 — Source-saturated exterior-quotient architecture for the complete supported Weil response

**November 11, 2026 PT. Scope: exact Hilbert-space theorem and source-authenticated verifier. Original physical J8 exterior integrals NOT yet evaluated.** This research draft is stacked on original NF502 [PR #530](https://github.com/monocap-tech/weil-lab/pull/530); original NF501R 4096-bit native all-242 full-support projected logarithmic one-ray failed the frozen selected sufficient gate [native CI #43139106161](https://github.com/monocap-tech/weil-lab/actions/runs/43139106161). The original NF501 independent exact-Fraction follow-up and NF502 cone source-CI have separate verification obligations. No main merge, no RH or global Weil positivity assertion.

## Why NF503 must change the observable

The accepted original log ray has full physical two-collar raw alignment ~34% yet its true \(J_{242}^{\perp}\) capture is **less than 0.0005%** of the whole perpendicular original \(q\). NF501R and NF502 show that preserving the endpoint logarithm alone is not enough. Trying one more arbitrary smooth endpoint ray is therefore not the right next numerical experiment.

A stronger question can be posed without choosing **any** individual trial direction:

> If an unlimited number of arbitrarily shaped legitimate physical \(L^2\) directions supported in a chosen true physical cell region \(S\) were allowed, what is the BEST possible approximation to the complete original perpendicular residual?

If even this physically overgenerous *support-saturated* class cannot meet the fixed original NF404 sufficient residual budget, then no finite or infinite collection of rays supported in \(S\) can do so, regardless of how cleverly selected. This reduces a poorly identified search for witnesses to a canonical **outside-region Schur complement**.

## Exact original physical Hilbert-space theorem

Let \(I=[-B,B]\), \(B=11/10\), and \(J=\mathrm{span}\{j_0,\dots,j_{241}\}\subset L^2(I)\) be the authentic original 242D analytic selected space (including true \(s(x)=\sinh(x/2)\) as index 241). Let \(P=P_J\), \(Q=I-P\) and \(W=m(D)u_4-a s\) be the complete original physical supported response with the unchanged NF404 dyadic center. Put \(q=QW\).

Let \(S\subset I\) be a measurable support region, \(O=I\setminus S\), and assume \(O\) contains a nonempty real open interval. Since the old \(j_i\) are linearly independent analytic functions, their restrictions to \(O\) remain independent. Thus their **actual exterior physical Gram**

\[
G_O=(\langle j_i,j_j\rangle_{L^2(O)})_{i,j=0}^{241}
\]

is strictly positive definite. The original entire-generator basis identity is a theorem from the inherited physical frame, not a new harmonic shadow.

Define the complete-original-source exterior physical data

\[
E_O=\int_O |W(x)|^2\,dx,\qquad
b_O=\left(\int_O j_i(x)W(x)\,dx\right)_{i=0}^{241}.
\]

Here **all** original physical prime seams, critical sine carriers, 273 grouped modes, genuine odd sinh pole and NF404 center remain as in NF407/NF406.

Then the exact support-saturated residual is

\[
\boxed{\displaystyle
\mathcal R(S)
=\inf_{\phi\in L^2(S)}
\|q-Q E_S\phi\|_{L^2(I)}^2
=E_O-b_O^\top G_O^{-1}b_O.
}
\]

\(E_S\) here denotes extension by zero from \(S\) to \(I\). The statement allows **every** \(L^2\) physical ray on \(S\), far more than a particular finite-generator or original Weil-image family. Its numerical closure is not a domain claim.

### Proof via the invisible complement

For \(r\in J^\perp\) and \(\phi\) supported on \(S\),

\[
\langle r,QE_S\phi\rangle_I
=\langle r,E_S\phi\rangle_I
=\langle r|_S,\phi\rangle_S.
\]

Hence the annihilator of \(QE_S L^2(S)\) *inside* \(J^\perp\) consists exactly of

\[
\{r\in L^2(O):r\perp J|_O\}.
\]

The best possible squared residual is the squared orthogonal projection of \(q\) onto this annihilator. Because the difference \(W-q=PW\) belongs to the original \(J\), the exterior projection eliminates it: one can compute using **W itself**, without the (potentially badly cancelled) old full 242D projection \(PW\). The projection of \(W|_O\) perpendicular to the restrictions \(J|_O\) has the exact stated exterior Schur norm \(E_O-b_O^\top G_O^{-1}b_O\). The old pole centering is also immaterial to this final scalar: replacing \(W\mapsto W+\lambda s\) changes only a vector inside \(J|_O\).

Equivalently the **maximal possible energy capture by any supported physical S-local ray family** is

\[
\boxed{\|q\|^2-\mathcal R(S).}
\]

This is **not** an optimization over source-eligible multipliers; it is a universal necessary physical limitation.

### Independent primal identity

Let \(H=\langle J,J\rangle_I\), \(G_S=\langle J,J\rangle_S\), \(J_S:L^2(S)\leftarrow\mathbb R^{242}\). Then the supported physical projector map \(T=QE_S\) has

\[
T^*T=I_S-J_SH^{-1}J_S^*.
\]

Since \(J\) has no nonzero analytic member supported strictly inside \(S\), this is positive/invertible. With \(c_S=J_S^* q|_S\), the Woodbury identity gives

\[
\boxed{\begin{aligned}
\|P_{\mathrm{ran}\,T}q\|^2
&=\langle q|_S,(T^*T)^{-1}q|_S\rangle\\
&=\|q|_S\|^2+c_S^\top G_O^{-1}c_S .
\end{aligned}}
\]

The last equation is the **same** as the exterior Schur formula after using \(q\perp J\), but its derivation is independent of the exterior annihilator argument. Two opposite source evaluation paths are therefore available for eventual numerical cross-checks.

## New exact selected-frame architecture

The original full physical Gram \(H\) and stable dyadic \(D\) were already SHA-pinned by NF401/NF404/NF501R. The **exterior** operator can be evaluated without an ill-conditioned raw inverse:

\[
G_O=H-G_S,\qquad
N_O=D^\top G_O D=N-D^\top G_SD.
\]

For the genuine J8 terminal two-collar \(S\), \(O\) contains the entire central aperture; analytic source rank is secure. A numerical solver must rigorously enclose \(N_O^{-1}\) (or use verified residual bounds), **not** assert that the near-identity full-support \(N\) automatically makes \(N_O\) well conditioned. The source-native recipe is:

1. Obtain \(E_O=E_I-E_S\), using the already genuine original complete centered scalar components \(K+D_7+D_8\) and independent true original whole J8 two-collar positive square \(2E_{w,T}\), but only with outward intervals and cross-correlated source remainder fees.
2. Compute \(b_O=b_I-b_S\) in the original D frame, reusing NF401's source-accepted complete original full 242D multiplier moment column with the original pole adjustment. For genuine \(S\), compute \(b_S\) by integrating **both** the original analytic \(A(d)=H(d)+vC_8\) from native NF494 and the original \(U(B-d)\log(B/d)/2\) from source-accepted NF500. Do not conflate this full physical cross column with only the logarithmic NF500 column.
3. Compute the original \(G_S\) by **actual** source generator products over both genuine terminal collars with explicit physical interval and error control. No exterior signed kernel elements or invented Riesz directions are needed.
4. Contract \(E_O-b_O^\top G_O^{-1}b_O\) with outward source and matrix inverse error fees. The only final decision is whether its strict LOWER bound exceeds original \(\gamma^2\), its strict UPPER bound is below \(\gamma^2\), or the data are insufficient.

This avoids *selecting* an exterior witness and tests the **entire** possible physical terminal-collar source-support class at once. It may show a support-localized universal no-go far more general than NF498–NF502, but such a decision is **NOT** claimed before the actual numeric source integrals are evaluated.

## New source-independent exact verification

The [NF503 exact-Fraction verifier](../../scripts/local_replay/verify_nf503_original_saturated_exterior_Hilbert_quotient_exact.py) verifies all three formulas in an exact nontrivial seven-dimensional model with three independent polynomial prototype selected generators. Its 48 adversarial independently solved controls include: different true original-style orthogonal complements, huge and rational selected shear/recenter terms, 5 true support patterns (including nested supports), primal \(T^*T\) inversion, the exterior Schur scalar, and the direct exterior orthogonal residual. It also SHA-pins the actual original NF501 source and NF404 fixed gamma and calibrates \(S=\varnothing\) against the **source-native** genuine original \(\|QW\|^2\) interval. Exact finite toy model checks test logical algebra, **not** original J8 numeric source integrals.

## Acceptance and current decision

- NF501R source-native original one-ray full projected result: **SUCCESS**; strict failure of original selected sufficient gate for this candidate.
- NF502 geometric perturbation theorem: **mathematically derived**; independent focused GitHub certification remains a separate gate.
- NF503 exterior-quotient identity and explicit source-numeric input architecture: **mathematically derived**; independent GitHub exact Fraction theorem checks pending.
- Whole original J8 \(S\)-saturated \(\mathcal R(S)\): **OPEN — no numerical value yet**.
- Source-to-Weil-multiplier image/graph domain, original whole even/odd form, W-ODD-NEG, RH: **OPEN**.

**Next bold NF504:** genuine original source-native whole J8 two-collar exterior \(G_O,b_O,E_O\), independent rational acceptance of outward Schur scalar, then decide a universal *physical S-local* necessary no-go/pass for unchanged original NF404 budget. Do not infer global Weil positivity or RH from that restricted geometric result.
