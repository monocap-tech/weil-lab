# RPB108 — RC129: four-vector joint Gram and endpoint moment

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Starting checkpoint RC128, commit 56a2955125232c11b5fb27d8dc31bec3714c3f90.

## Result and coverage

RC129 selects RC128's K=14 collective response w_14 and certifies the complete actual D Gram and endpoint pairing matrices on

\[
 U=[P_0,\psi_0,f_0,w_{14}].
\]

The family has dimension four by RC128's paid distance argument. The new vector has a finite polynomial through degree 4094 and fifteen analytic tail features combined into that same vector. It overlaps all three old vectors in D coordinates. Those correlations are retained in the full Gram rather than assigning it a block diagonal structure.

All entry intervals, weighted Loewner matrices, a strictly positive Gram lower and a correlated reference inverse-response sandwich are accepted by exact rational checks. The actual finite/tail and tail/tail endpoint terms are paid. The psi_0/f_0 first pairing is also sharpened using the new response vector and RC128's action error.

| New joint quantity | Lower, outward display | Upper, outward display |
|---|---:|---:|
| G_{w,w} | 0.005995031037544 | 0.005995034800509 |
| G_{psi,w} | 8.149618e-8 | 8.590711e-8 |
| H_{0,w} | 0.022771129322842 | 0.022771133733766 |
| H_{psi,w} | 1.151659e-7 | 1.267630e-7 |
| H_{f,w} | 0.005995031037544 | 0.005995034800509 |
| H_{w,w} | 0.002338074094298 | 0.002338087000505 |

These are outward decimal displays; acceptance uses the exact rational certificate endpoints. They are first moments and pairings, not the complete four-vector covariance or an accurate evaluated inverse.

No new original Weil direction or original positivity extension is claimed. The original count remains 10–639 below 0.01. Global/F4 and RH remain open.

## Definitions and selected representation

Keep D=J+sI, JP_n=H_nP_n, s=c_R+log2+789/125, B=11/10, and h=-1/2 log(1-(x/B)^2). The positive endpoint action C=D^-1 h is a contraction on D energy. Define z_n=n(n+1) and d_n=2H_{2n}-2H_n+1/(2n+1)-log2.

The old finite response f_0 and analytic tail psi_0 are RC126's exact symbolic vectors, supported respectively at even degrees 2..988 and every even degree >=990. Their coefficients are (2n+1)/[(H_n+s)z_n] on the corresponding supports. The exact closure is

\[
 CP_0=aP_0+\psi_0+f_0,\qquad a=(1-\log2)/s.
\tag{1}
\]

Set L=4095 and lambda=z_988. RC128's selected vector is

\[
 w=\hat g+\sum_{k=0}^{14}\hat\mu_k\xi_k,\qquad
 (\xi_k)_n=\frac{(2n+1)\lambda^k}{(H_n+s)z_n^{k+1}}
 \quad(n\ge4096,\ n\text{ even}).
\tag{2}
\]

Other xi_k coefficients vanish. The rational polynomial g_hat occupies even degrees 0..4094. Its generator and center/radius coefficient SHA-256 are independently reconstructed and checked against RC128. All retained moment centers mu_hat_k and every g_hat coefficient are positive. Let epsilon be RC128's full norm upper for ||Cf_0-w||_D; epsilon <6.996019e-26 and includes both rounding and the complete omitted analytic moment series.

Define

\[
 G=U^*DU,\qquad H=U^*hU,\qquad
 \Sigma=U^*D(I+C)^{-1}U.
\tag{3}
\]

These use the actual reference energy and physical vectors, not original canonical Riesz moment vectors or the original Weil augmentation.

## Full overlapping Gram

The old three-vector Gram is diagonal by disjoint coefficient supports. Its entries retain RC127's full infinite enclosures. The new mixed entries are

\[
 G_{0,w}=2Bs\hat g_0,
\]

\[
 G_{f,w}=\sum_{2\le n\le988\atop n\text{ even}}
 \frac{2B}{2n+1}(H_n+s)(f_0)_n\hat g_n,
\]

\[
 G_{\psi,w}=\sum_{990\le n\le4094\atop n\text{ even}}
 \frac{2B}{2n+1}(H_n+s)(\psi_0)_n\hat g_n
 +\langle\psi_{tail},w_{tail}\rangle_D.
\tag{4}
\]

The polynomial and analytic parts of w have disjoint D supports, so G_{w,w} is their sum of squared norms. This last orthogonality does not remove w's overlap with the old family.

Let rho=lambda/z_4096, A=sum_{k=0}^{14} mu_hat_k rho^k, rounded upward, and T be RC128's full D energy upper for the leading tail above L. The coefficientwise inequality

\[
 0\le w_{tail,n}\le A(\psi_0)_n\quad(n\ge4096)
\tag{5}
\]

gives

\[
0\le\langle\psi_{tail},w_{tail}\rangle_D\le AT,
\quad0\le\|w_{tail}\|_D^2\le A^2T.
\tag{6}
\]

Here A <0.853102. Directed finite sums plus (6) enclose every entry of G, including the entire infinite tail.

Entry intervals are converted to correlated Loewner matrices with RC127's weighted Young bound. If the entry radii are e_ij and weights w_i are positive rational square-root uppers for the four source energies, the interval error is bounded by the diagonal with entries sum_j e_ij w_i/w_j. Exact rational LDL acceptance proves

\[
\boxed{G\succeq G_{lower}\succeq
 \frac1{1000}\operatorname{diag}
 (G_{00,entry\ lower},G_{\psi\psi,entry\ lower},
 G_{ff,entry\ lower},G_{ww,entry\ lower})>0.}
\tag{7}
\]

Equation (7) is a conditioning bound for this four-vector Gram. It is not an original Weil complement floor.

## All endpoint correlations and infinite remainders

The same-parity endpoint matrix is

\[
 \langle P_n,hP_m\rangle_2=
 \begin{cases}
 2Bd_n/(2n+1),&n=m,\\
 2B/|z_n-z_m|,&n\ne m.
 \end{cases}
\tag{8}
\]

It is positive entrywise on this family. The finite g_hat/g_hat and psi-prefix/g_hat pairings are computed directly from (8) with directed 70-digit sums. The psi prefix ends at degree 4094.

Write z_* = z_4096 and define two positive finite weighted sums

\[
 S_g=\sum_{n\le4094\atop n\text{ even}}
 \frac{\hat g_n}{1-z_n/z_*},\qquad
 S_\psi=\sum_{990\le n\le4094\atop n\text{ even}}
 \frac{(\psi_0)_n}{1-z_n/z_*}.
\tag{9}
\]

For a finite prefix u, positivity and (8) imply

\[
\langle u,h\psi_{tail}\rangle_2
\le T\sum_n\frac{u_n}{1-z_n/z_*}.
\tag{10}
\]

The factor depends on each actual prefix degree. It is not replaced by a single worst-case degree-4094 denominator. With (5), (10), and h <= D, all omitted endpoint blocks obey

\[
0\le H_{\psi,w}-\langle\psi_{prefix},h\hat g\rangle_2
\le T(AS_\psi+S_g+A),
\tag{11}
\]

\[
0\le H_{w,w}-\langle\hat g,h\hat g\rangle_2
\le T(2AS_g+A^2).
\tag{12}
\]

Equation (11) pays prefix/tail in both orders and tail/tail. The latter term follows from endpoint-form Cauchy-Schwarz and h <= D, giving A T. Equation (12) pays both mixed orders and the full analytic tail energy. Their accepted absolute upper contributions are below 1.159707e-8 and 1.290621e-8, respectively. Thus no omitted mixed block is assigned zero.

The remaining new pairings use exact response identities with paid epsilon:

\[
 H_{0,w}=aG_{0,w}+G_{\psi,w}+G_{f,w},
\tag{13}
\]

\[
 |H_{f,w}-G_{w,w}|\le\epsilon\|w\|_D,
\quad |H_{\psi,f}-G_{\psi,w}|\le\epsilon\|\psi_0\|_D.
\tag{14}
\]

The second identity in (14) tightens RC127's psi_0/f_0 entry interval by intersection. Self-adjointness of C in D energy justifies both comparisons. These are not claims of an exactly invariant rounded vector.

The complete H entry intervals are converted to full weighted Loewner bounds. Exact rational acceptance verifies H_lower >= 0 and G_lower-H_upper >= 0. This certifies the joint first moment and contraction on every linear combination of the four source vectors.

## Correlated reference response

For an arbitrary rational four-by-four coefficient trial Y, the reference variational lower is

\[
\Sigma\succeq G-(I-Y)^*G(I-Y)-Y^*HY.
\tag{15}
\]

The validator takes a 10^-20 rational rounding of (G_mid+H_mid)^-1 G_mid. Using correlated bounds on every term gives the accepted lower

\[
\Sigma\succeq G_{lower}
 -(I-Y)^*G_{upper}(I-Y)-Y^*H_{upper}Y.
\tag{16}
\]

The upper remains the contraction secant

\[
\Sigma\preceq G_{upper}-\tfrac12H_{lower}.
\tag{17}
\]

Exact rational PSD checks accept the lower, the upper-minus-lower matrix, and the lower's Loewner improvement over the elementary 3G_lower/4-H_upper/4 bound. Y is a variational trial, not a claimed inverse of the actual full reference operator.

| Coordinate response / actual D energy | Lower | Upper |
|---|---:|---:|
| P_0 | 0.931327855055 | 0.959641776722 |
| psi_0 | 0.546115679979 | 0.744748832485 |
| f_0 | 0.822558697000 | 0.881014852879 |
| w_14 | 0.721915635146 | 0.805212567498 |

These outward diagonal ratios are valid for the individual coordinates. The actual full matrix Loewner sandwich controls every source combination. Because the Gram is not diagonal, this table must not be read as a generalized spectral interval for arbitrary mixtures. The broad reference response bounds do not approach RC128's 10^-24 one-action accuracy; that accuracy was never an inverse-response guarantee.

## Next cursor and evidence boundary

The enlarged family now has full joint G and H, a paid positive Gram lower, and a reference first-moment sandwich. RC128's tiny f_0 residual can be used alongside these actual correlations. The missing data are the remaining joint action/covariance of C psi_0 and C w_14, or an equivalent signed resolvent estimate on that block.

**RC130 cursor:** control the complete remaining two-column residual block after projection onto U. Compute actual second moments or directly bound those two projected actions with their mixed covariance paid. Use the exact P_0 closure and the paid Cf_0≈w_14 row to avoid spending effort recomputing already controlled residuals. A sufficient stopping condition is a covariance/resolvent bound meeting the intended matrix response budget. If the new response column has substantial leakage, identify its collective structure before adding individual native directions.

RC129 does not compute H_2=U^*DC^2U or R_U(U)=H_2-HG^-1H. RC128's three-input residual upper R_U(V_e) cannot substitute for this four-input matrix. A first-moment PSD result also cannot replace the missing action covariance.

D, C and Sigma remain reference objects. Original completion requires Hhat=A_Q+T_Weil^*T_Weil >= eta I and T_Weil Hhat^-1T_Weil^* <= theta I with theta<1, after paid actual original source actions. The inherited W_639 floor and original count are unchanged; no original floor is transferred to this physical source-family decomposition.

**Certified:** complete four-vector G and H with full infinite output, overlapping-support correlations, positive Gram conditioning, endpoint contraction, sharper psi/f pairing, and correlated variational reference bounds. **Not performed:** remaining C psi_0/C w_14 block, complete four-vector covariance, high-accuracy inverse response, regular multiplier or original augmented actions. **Unsupported:** original positivity from reference PSD, inverse accuracy from Cf_0 approximation alone, or full covariance from the old three-input upper.

## Reproduction

Inputs: RC128, RC127, RC126, RC124, in that order. Byte-level SHA-256 linkage is checked. RC128's polynomial coefficient hash is independently reconstructed before pairing. Directed 70-digit arithmetic encloses all positive finite sums. Exact rational tail bounds, weighted matrix errors, PSD and variational congruences accept the complete certificate. Replay reverses action coefficient, Gram, endpoint and weighted-prefix sums and compares the entire rational output.

```bash
python scripts/validate_rpb108_rc129_four_vector_joint_moment.py \
 --output certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc128_collective_second_response.json \
 certificates/rpb108_rc127_enriched_even_endpoint_action.json \
 certificates/rpb108_rc126_finite_response_variance.json \
 certificates/rpb108_rc124_actual_joint_endpoint_moment.json
```

Repeat with --replay. The validator imports RC127's helpers without changing historical files. Only additive RC129 script, certificate and note files are committed; prior RC, Lean and unrelated branch work is preserved.
