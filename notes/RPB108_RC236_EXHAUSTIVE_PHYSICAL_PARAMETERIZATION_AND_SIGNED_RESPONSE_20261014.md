# RPB108 — RC236: exhaustive physical parameterization and signed response

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC235: `22904e21740833c773c7caa984fc80158d15ba2a`. Branch: research/rpb108-route-consolidation.

RC236 proves an exhaustive physical polynomial parameterization of the chosen rational augmentation's complete frequency range. It then derives a signed original-action inverse criterion equivalent to the **full** auxiliary norm below one. This criterion does not require inversion of the full frequency Gram or numerical construction of canonical Riesz images.

The criterion is proved; its full signed positivity is **not** numerically certified. Only the two-input instance is evaluated. Its enclosures remain too broad to prove positivity, and no negative original direction is established. Stage I, original whole-space positivity, F4, Lean and RH remain open.

## Exhaustive parameter spaces

Use the unchanged RC115 rational Fhat, its parity bandwidths and separate augmentation coefficients. Define

\[
 V_e=\operatorname{span}\{P_0,P_2,\ldots,P_{494}\},
 \quad V_o=\operatorname{span}\{P_1,P_3,\ldots,P_{781}\}.
\]

These physical polynomial spaces have dimensions 248 and 391. By RC121 they are contained in the common canonical/D-energy form domain. They are input parameter spaces, not assumed invariant spectral subspaces or a census of dangerous eigenvectors.

RC230 proves that all retained rational frequency polynomials psi_j are linearly independent. The physical kernel factors as

\[
 \widehat F q=\sum_j\widehat\psi_j\ell_j(q),
 \quad\ell_j(q)=\int_{-B}^B T_j(x/B)q(x)dx.
\]

On the ordered Legendre input basis, the moment matrix has entries integral T_i P_j. Orthogonality of P_j to every polynomial of degree below j makes the entries with j>i zero. Its diagonal is strictly positive:

\[
 \int_{-B}^B T_n(x/B)P_n(x/B)dx
 =\frac{2B}{2n+1}\begin{cases}
 1&n=0,\\
 2^{2n-1}/\binom{2n}{n}&n>0.
 \end{cases}
\]

The formula follows by comparing the leading coefficients of T_n and P_n. The validator checks every one of the 639 diagonals exactly and records its bit lengths and unambiguous numerator/denominator SHA256. Direct rational polynomial integration verifies the triangular structure and diagonal formula through degree 12.

Thus the moment map from either V parity space to its retained coefficient space is invertible. Together with independence of the psi_j this proves

\[
 \boxed{\widehat F|_{V_p}:V_p\longrightarrow
        \operatorname{range}\widehat F_p
        \text{ is a bijection}.}
\]

Every physical input's finite moment vector has a representative in V_p, so the image is the **entire** frequency range, not just the images of two test polynomials. Because V_p is in the canonical carrier, this is also the complete range of the chosen canonical augmentation Xhat=Fhat i. The total dimension is exactly 639.

This proves coverage of the parameterization. It does not execute 639 augmented actions, responses, or Gram entries. Neither a dense solve nor 639 separate solves is mandated by the argument.

## Exact full-range signed identity

Let N0 be the original Weil form's D-Riesz representative, N the positive augmented D-Riesz representative, and A=D^-1 Fhat*Fhat. On the complete common form domain,

\[
 N=N_0+\lambda A.
\]

Both N and N0 are selfadjoint in D energy. N is positive with the actual inherited mu and nu endpoints; positivity or invertibility of N0 is not assumed. Let V denote the map from one parity's finite coefficients to its full polynomial parameter space and put

\[
 Y=\widehat F V,\quad O=N_0V,
 \quad T_V=O^*DN^{-1}O,
 \quad F_{0,V}=V^*DN_0V,
 \quad\Delta_V=F_{0,V}-T_V.
\]

T_V is a response of **original-action sources through the positive augmented inverse**. It never uses an inverse of the original operator. The canonical version of O is A_Q V, since N0=M A_Q and M is the canonical metric's D-Riesz representative. This is another source for which the bridge avoids separately realizing a canonical Riesz image.

For Bhat=lambda Fhat N^-1 D^-1 Fhat*, the exact identity is

\[
 \boxed{Y^*(I-\widehat{\mathcal B})Y
       =\lambda^{-1}\Delta_V.}
\]

Proof. The D source of Y is AV=(N-N0)V/lambda. Expanding the response gives

\[
 Y^*\widehat{\mathcal B}Y
 =\lambda(AV)^*DN^{-1}(AV)
 =\lambda^{-1}V^*D
   [N-2N_0+N_0N^{-1}N_0]V.
\]

Also Y*Y=V*DAV=lambda^-1 V*D(N-N0)V. Subtracting proves the identity. The two mixed terms cancel by N N^-1=N^-1 N=I; **N0 and N need not commute**. Physical unbounded compositions are not used: these are bounded form operators in the common D space and finite source maps.

The validator verifies this full matrix identity in a nonidentity D metric with noncommuting original and augmented operators. It checks a positive original form, an indefinite original form with a positive augmentation, and a singular nonnegative original form. The indefinite case is an abstract control, not a negative Weil example. The singular case has a nonnegative but singular signed gap and frequency norm equal to one, demonstrating why strict positivity is required. These checks prevent silently assuming original positivity or treating a zero gap as a passed strict gate.

## Why the criterion covers the full norm

The positive finite-rank Bhat maps into range(Fhat) and annihilates its frequency-orthogonal complement. The parameter map Y=Fhat V bijects onto that entire range. Therefore, separately in the two parity blocks,

\[
 \boxed{\|\widehat{\mathcal B}\|<1
 \quad\Longleftrightarrow\quad
 \Delta_{V_e}\succ0\ \text{and}\ \Delta_{V_o}\succ0.}
\]

Strict positivity of the two full finite matrices implies a positive frequency gap by finite dimensionality. Conversely a full frequency gap makes each signed matrix strictly positive. This is a statement about all 248+391 channels, not the two-dimensional compression from RC235.

There is also an explicit route to a quantitative gap without a full frequency Gram inverse. The exact input D Gram is diagonal with entries m_n(H_n+s). If a validated full signed matrix or uniform form estimate proves

\[
 \Delta_{V_p}\succeq c_p V_p^*DV_p,
 \qquad c_p>0,
\]

and f_p^2 bounds the actual physical Fhat norm squared, then

\[
 Y_p^*Y_p\preceq(f_p^2/s_{\rm lower})V_p^*DV_p,
\]

so the full frequency gap on that parity is at least

\[
 \boxed{\zeta_p\ge c_p\frac{s_{\rm lower}}{\lambda_p f_p^2}.}
\]

Take the minimum of both parity gaps for the full auxiliary operator. Under a consistent positive signed-floor hypothesis this gap is at most one because Bhat is positive. The certificate computes conservative gap multipliers greater than 0.2925582015 even and 0.2784881697 odd per unit of a proved signed D floor. These are conversion factors, **not certified signed floors or actual positive frequency gaps**.

A full positive signed enclosure can be verified in the input metric without numerically conditioning the frequency basis. This is an alternative certification interface, not a proof that it is cheaper or well conditioned in implementation. A full signed matrix or an equivalent uniform bound still needs actual original-action and augmented-inverse error certification.

Combined with the already positive Hhat, a full frequency gap would give the original canonical floor through the established augmentation criterion. No such signed floor or full frequency gap is obtained in this pass.

## Evaluated two-input instance

For P0 and P1, RC231 supplies full original actions O_j=N0 P_j and RC234 supplies complete augmented actions NP_j. Their actual original forms f_j are already sharply enclosed. RC236 encloses

\[
 T_j=\langle O_j,N^{-1}O_j\rangle_D,
 \qquad\Delta_j=f_j-T_j.
\]

For a trial Z=zP_j, its residual is O_j-zNP_j. Source and action share the same original piece. If E0 and Eaug are the inherited squared action errors, the complete residual fault norm is bounded by

\[
 |1-z|\sqrt{E_0}+|z|\sqrt{E_{\rm aug}}.
\]

The signed variational center for T_j is

\[
 C_z=(2z-z^2)f_j-\lambda z^2 g_j,
 \quad g_j=\|\widehat F P_j\|_{\rm freq}^2.
\]

The correction to C_z is added and bounded by the actual mu/nu residual sandwich. Negative trial coefficients are handled with their correct signs. For the signed gap, the common original form can be coupled before rounding:

\[
 \Delta_j=(1-z)^2f_j+\lambda z^2g_j
           -\langle O_j-zNP_j,
                    N^{-1}(O_j-zNP_j)\rangle_D.
\]

Here the correction is subtracted **from the gap** because the gap itself is the original form minus a response. The inverse response still uses its added correction; its sign has not been reversed. The validator retains both direct and coupled signed-gap bounds.

Exact trial candidates include z=k/1000, k=-50,...,50, and two variational proposals. Deterministic rational selection gives:

| Input | Original-action inverse response enclosure, outward | Signed gap enclosure, outward |
|---|---|---|
| P0, even | [0.0004595597, 33.1650731551] | [-33.0765139591, 0.0880996363] |
| P1, odd | [0.0011563242, 42.5102481230] | [-42.4131653073, 0.0959264916] |

These broad intervals do not certify signed positivity even on the two-input test space. Their negative lower endpoints are uncertainty bounds, not actual negative directions: both upper endpoints are positive. Opposite parity pairings vanish exactly, so the diagonal enclosures cover all complex combinations of the two tested inputs.

The full inverse-response matrix on the exhaustive 639-dimensional parameter space has not been evaluated. Original test-form positivity alone cannot replace the missing T_V upper bound. The new equivalence locates the full remaining numerical target; it does not discharge it.

## Verification and next work

Generation verifies all input Git blob pins, every positive moment diagonal, low-degree exact moment controls, coupled original-action response bounds, and noncommuting positive/indefinite structural controls. Replay reverses input and residual accumulation order and requires exact equality of the complete certificate.

```bash
python scripts/validate_rpb108_rc236_full_range_signed_response.py --output certificates/rpb108_rc236_full_range_signed_response.json
python scripts/validate_rpb108_rc236_full_range_signed_response.py --output certificates/rpb108_rc236_full_range_signed_response.json --replay
```

Publication adds only this note, validator and certificate. Expected-head non-force update and remote comparison/tree readback verify existing blob preservation. Conflict checks apply to additions, not all historical contents.

The next focused work is richer certified augmented responses to original-action sources N0 V and a full signed-gap lower enclosure. RC228's canonical inverse gate remains preserved. Full original augmentation norm below one and Stage I assembly remain open; no mandatory solve count or completion time is asserted.
