# RPB108 — RC127: joint endpoint action on the enriched even family

Date: 2026-10-12 UTC. Aperture: a=11/10. Branch: research/rpb108-route-consolidation. Starting checkpoint: RC126, commit c72b672465a8172f9f04cb98ceaf3669e495fc0b.

## Result

RC127 certifies the complete joint D Gram and endpoint pairing matrices for

\[
V_e=[P_0,\psi_0,f_0],
\]

where f_0 is RC126's **exact symbolic** collective finite-response polynomial and psi_0 is the **full infinite** even tail above degree 989. It constructs rational finite trials for all three endpoint actions, pays their omitted input and output tails, and encloses the full second moment and projected covariance. The RC126 rounded polynomial is retained as an implemented approximation with its separate paid error; it is not assigned exact invariance.

The exact P_0 covariance row and column vanish. However the new f_0 row does not close:

\[
\boxed{R_{ff}\ge 0.001327614390662,
\qquad R_{ff}/\|f_0\|_D^2\ge 0.018581889237.}
\]

These are outward decimal lower displays of exact rational acceptance bounds. Consequently a whole-family inequality R <= epsilon G is impossible on this enriched family for epsilon below 0.018581889237. Adding f_0 captures CP_0 collectively but exposes a further response of f_0 outside the family. This is actual endpoint covariance, not a certificate-width artifact or a negative Weil direction.

The analytic-tail covariance now has a paid enclosure but no useful smallness certificate. High-accuracy inverse response, regular multiplier action and original Weil/augmented responses remain open. The original spectral count remains 10–639 below 0.01; original positivity, Global/F4 and RH are not established.

## Definitions and exact joint structure

Use RC121's diagonal energy D=J+sI, with JP_n=H_n P_n, H_n the harmonic numbers, and s=c_R+log2+789/125. The actual endpoint multiplication form is h=-1/2 log(1-(x/B)^2), B=11/10. Define C=D^-1 h as the bounded positive contraction on D energy using the endpoint form: 0 <= C <= I. This form definition is sufficient even when a pointwise h psi_0 is not asserted to be physical L2.

Write z_n=n(n+1) and

\[
d_n=2H_{2n}-2H_n+\frac1{2n+1}-\log2.
\]

The physical Legendre mass is 2B/(2n+1). For same-parity indices, the exact endpoint matrix is

\[
\langle P_n,hP_m\rangle_2=
\begin{cases}
\dfrac{2B}{2n+1}d_n,&n=m,\\
\dfrac{2B}{|n-m|(n+m+1)},&n\ne m.
\end{cases}
\tag{1}
\]

All these entries are positive. The two response coefficient families are

\[
(f_0)_n=\frac{2n+1}{(H_n+s)z_n}
\quad(2\le n\le988,\ n\text{ even}),
\]

\[
(\psi_0)_n=\frac{2n+1}{(H_n+s)z_n}
\quad(n\ge990,\ n\text{ even}),
\tag{2}
\]

with other coefficients zero. Their supports and that of P_0 are disjoint in D coordinates. Define

\[
G=V_e^*DV_e,\quad H=V_e^*hV_e,\quad
H_2=(CV_e)^*D(CV_e),\quad
R=H_2-HG^{-1}H.
\tag{3}
\]

Thus G is diagonal, while H is not. R is the D Gram of the action residual outside span(V_e), hence R >= 0. The exact response identity is

\[
CP_0=\frac{1-\log2}{s}P_0+\psi_0+f_0.
\tag{4}
\]

In particular H_{0,psi}=G_{psi,psi}, H_{0,f}=G_{f,f}, and the P_0 row and column of R are exactly zero. Equation (4) also supplies every first-row entry of H_2 from H. It does not assert that C psi_0 or C f_0 lies in the same family.

## Complete first moment and finite–tail correlation

RC124's full infinite psi_0 D Gram and endpoint diagonal enclosures are inherited with SHA-256 linkage through RC126. RC126's exact symbolic finite D norm is inherited similarly. The finite f_0/f_0 endpoint pairing is evaluated directly from (1), with all 494 coefficients enclosed using the actual s interval.

The new mixed pairing is

\[
H_{f,psi}=2B\sum_{\substack{2\le m\le988\\m\text{ even}}}(f_0)_m
\sum_{\substack{n\ge990\\n\text{ even}}}
\frac{(\psi_0)_n}{z_n-z_m}.
\tag{5}
\]

Its prefix is evaluated through n=2046. Let T(r) denote an upper for the D norm squared of the leading analytic coefficient sequence at even degrees n>r. The positive decreasing weight (2x+1)/[x^2(x+1)^2], whose primitive is -1/[x(x+1)], gives

\[
T(r)\le\frac{B}{(s_{lower}+H_{r,lower})(r-1)r}
\quad(r\text{ even}).
\tag{6}
\]

The preceding width-two cells prove the parity-sum upper in (6). The first omitted index is r+2; using the lower harmonic value at r is conservative. There is no sampled or silently discarded infinite tail.

For (5), the omitted contribution is at most

\[
T(2046)\,
\frac{\sum_m(f_0)_{m,upper}}{1-z_{988}/z_{2048}}.
\tag{7}
\]

The accepted mixed interval is approximately [6.77371e-8,9.20152e-8] (outward display). The f/f endpoint diagonal is approximately 0.01700409875790757. The certificate contains exact rational lower and upper matrices for every joint entry.

Entrywise bounds are converted to full Loewner bounds. With midpoint H_mid, symmetric interval radii e_ij and positive rational weights w_i, weighted Young's inequality gives

\[
-E\preceq H-H_{mid}\preceq E,
\quad E_{ii}=\sum_j e_{ij}w_i/w_j.
\tag{8}
\]

Weights are rational upward square-root bounds for the three D energies. Exact rational LDL checks accept H_lower >= 0 and G_lower-H_upper >= 0. These are joint matrix checks, not independent diagonal positivity assertions. The correlated reference sandwich

\[
\frac34G_{lower}-\frac14H_{upper}
\preceq\Sigma\preceq G_{upper}-\frac12H_{lower},
\quad\Sigma=V_e^*D(I+C)^{-1}V_e,
\tag{9}
\]

is also accepted. Equation (9) is a reference first-moment bound, not an accurate evaluated inverse or an original augmented response.

## Paid joint action, including infinite outputs

The exact coefficient action on a finite input u is

\[
(Cu)_n=\frac1{H_n+s}\left[
d_nu_n+\sum_{\substack{m\ne n\\m\text{ same parity}}}
\frac{(2n+1)u_m}{|z_n-z_m|}\right].
\tag{10}
\]

RC127 applies (10) to P_0, f_0 and the psi_0 prefix through degree 2046. It encloses every output coefficient through even degree 4094, then constructs rational center trials q_0,q_psi,q_f. The validator reconstructs every coefficient and stores their joint SHA-256, coefficient count and generator rather than a redundant coefficient table. The rounding error is summed with the actual D mass, including constant uncertainty.

For a finite source u with largest degree t and output beyond degree 4094,

\[
|(Cu)_n|\le(\psi_0)_n
\frac{\sum_m|u_m|}{1-z_t/z_{4096}},\quad n\ge4096.
\tag{11}
\]

Thus (6) pays its entire omitted output D energy. For the psi_0 source, C's contraction additionally pays the omitted input by sqrt(T(2046)). Input, output and rounding contributions are combined by the norm triangle inequality, not by assuming orthogonality of their images.

| Action | Full D norm error upper, outward display |
|---|---:|
| CP_0 versus q_0 | 0.000071906 |
| C psi_0 versus q_psi | 0.000153987 |
| C f_0 versus q_f | 0.000064923 |

These are absolute action errors at the deliberately modest cutoffs, not relative inverse-response tolerances. The psi action error is large relative to its source norm; no small analytic-tail covariance conclusion is drawn from it. All three infinite action outputs are enclosed nevertheless.

The finite trial action Gram is evaluated with directed arithmetic. If epsilon_i bounds ||Cv_i-q_i||_D, then

\[
| (H_2)_{ij}-\langle q_i,q_j\rangle_D |
\le\epsilon_i\|q_j\|_D+\epsilon_j\|q_i\|_D
       +\epsilon_i\epsilon_j.
\tag{12}
\]

The exact identity (4) tightens the first row. The positive coefficient structure permits intersecting lower H_2 entries with zero. No finite action trial is identified with the full action.

## Full projected covariance and the new obstruction

Because G is diagonal and the H entries are positive, interval arithmetic encloses each entry of HG^-1H directly:

\[
\sum_k H_{ik,lower}H_{kj,lower}/G_{kk,upper}
\le(HG^{-1}H)_{ij}\le
\sum_k H_{ik,upper}H_{kj,upper}/G_{kk,lower}.
\tag{13}
\]

Subtracting (13) from (12), and setting the exact zero P_0 row from (4), encloses the entire R matrix. Diagonal lower bounds may be intersected with zero; diagonal uppers may be intersected with source D energy since C is a contraction.

| Actual covariance quantity | Lower, outward display | Upper, outward display |
|---|---:|---:|
| R_{psi,psi} | 0 | 6.805270e-8 |
| R_{psi,f} | -9.646925e-8 | 1.198524e-5 |
| R_{f,f} | 0.001327614390662 | 0.001347770985438 |
| R_{f,f}/G_{f,f} | 0.018581889237 | 0.018864010021 |

The certificate stores the exact entry intervals, their correlated Loewner enclosure using (8), and a separate positive diagonal upper diag(0,2 R_{psi,psi,upper},2 R_{f,f,upper}) obtained by residual Cauchy-Schwarz. The general interval Loewner lower need not be PSD; the independent residual-Gram theorem gives R >= 0. A coordinate lower is not promoted to a diagonal Loewner lower.

The f_0 coordinate lower is strictly positive after all action-tail errors and projection uncertainty are paid. Therefore the current three-vector family does not satisfy a high-accuracy whole-family small-variance hypothesis. The finite source's original covariance has been captured, but subsequent action of its response vector reaches a new complement. This is the next actual operator datum to address.

For the RC126 rational polynomial f_hat, exact symbolic closure is replaced by the paid ||f_0-f_hat||_D squared upper below 6.050e-64. A family containing P_0,psi_0,f_hat can use (4) with that residual. RC127's numerical matrices and exact covariance zero row are explicitly for the symbolic f_0 family; they are not silently reused as exact matrices for f_hat.

## Next cursor and evidence boundary

RC128 should target the remaining two response columns jointly. One concrete route is a collective approximation to C f_0 with its analytic output tail paid, together with sharper C psi_0 correlations and their mixed covariance. A larger reducing family or signed resolvent estimate must pay the complete remaining block. More precision on the exact zero P_0 row cannot remove the certified f_0 obstruction. Whether the next response is cheaply compressible is still an investigation.

The endpoint contraction C, D energy, reference response Sigma and its covariance R are not the original Weil operator A_Q, its effective head F, or its augmentation Hhat. Original completion still requires Hhat=A_Q+T_Weil^*T_Weil >= eta I and T_Weil Hhat^-1 T_Weil^* <= theta I with theta<1. RC112's W_639 complement floor and spectral count are inherited unchanged; no floor is transferred to this physical response-family decomposition.

**Certified:** full three-vector G and H, finite–tail correlation with its infinite remainder, all three joint endpoint actions with paid norm errors, full H_2 and R enclosures, exact symbolic zero P_0 covariance row, and a positive f_0 covariance obstruction. **Conditional:** tighter reference response after paid remaining coupling. **Not performed:** high-accuracy inverse solve, all 39 analytic columns, regular multiplier or original augmented action. **Unsupported:** complete reference response from the zero P_0 row, small tail variance from these broad intervals, or original positivity from endpoint PSD.

## Reproduction

The standalone validator uses only Python standard-library modules. Inputs are RC126 and RC124, in that order, read byte-for-byte with SHA-256 linkage. Its harmonic, coefficient, pairing and action sums use 70-digit directed Decimal contexts; final acceptance uses exact rational interval, norm and PSD bounds. Replay reverses the finite pairing, input action and trial Gram sum orders and compares the entire rational certificate.

```bash
python scripts/validate_rpb108_rc127_enriched_even_endpoint_action.py \
 --output certificates/rpb108_rc127_enriched_even_endpoint_action.json \
 certificates/rpb108_rc126_finite_response_variance.json \
 certificates/rpb108_rc124_actual_joint_endpoint_moment.json
```

Repeat with --replay. Only the additive RC127 validator, certificate and note are committed. Lean and unrelated branch work are unchanged.
