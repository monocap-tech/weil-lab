# RC177: correlated P0/P2/f0 canonical first and action Gram

Parent: RC176, `cd81bb3848963aed70020e84205a29658ba538a8`.

RC176 completed the actual f0 regular output carrier and the paid canonical first-action trial. RC177 now evaluates the full correlated canonical source and action data on S=(P0,P2,f0). This supplies the missing f0 diagonal and mixed action rows needed before extending RC173's actual canonical inverse response.

The evaluated operator is M=D^-1 L, where L=D+h+R-rI is the actual supported canonical operator and D P_n=(H_n+s)P_n. M is self-adjoint in D energy and RC121 gives aI<=M<=2I, a=32125/230953. The original Weil operator A_Q and augmented Hhat are distinct targets and are not evaluated here.

## 1. Source overlap is retained exactly

Let G=S* D S. The f0 coefficients are eta_n=(2n+1)/[n(n+1)(H_n+s)] on even 2<=n<=988. Therefore

\[
 G_{02}=0,\qquad
 \langle P_2,f0\rangle_D
  =\frac{2B}{5}(H_2+s)\frac5{6(H_2+s)}
  =\frac{2B}{6}=\frac{11}{30}.
\]

The exact source Gram has the form

\[
 G=\begin{pmatrix}
 2Bs&0&0\\
 0&2B(s+3/2)/5&11/30\\
 0&11/30&\|f0\|_D^2
 \end{pmatrix}.
\]

The actual constant and f0 energy enclosures are inherited from RC127/RC129. Their rational lower and upper matrices are positive and retain the off-diagonal 11/30. All relative matrix comparisons below use this full nonorthogonal G.

## 2. Complete action carriers

The first two action columns use RC171 and RC172. The f0 column uses RC176:

\[
 \widehat M f0=f0+w14+\widehat p_{-rD^{-1}f0}
                        +\widehat p_{D^{-1}Rf0}.
\]

The native w14 finite polynomial through degree 4094 is reconstructed by RC128's directed generator. The hash of every coefficient center and radius must match RC128's historical coefficient hash. No revised meaning of w14 is introduced.

Every finite regular term vanishes above degree 512; the f0 and negative-r terms vanish above degree 988. Beyond degree 4094 the three complete represented action columns are exactly

\[
 \widehat M P_0:\ \eta_n,\qquad
 \widehat M P_2:\ \frac{\eta_n}{1-6/z_n},\qquad
 \widehat M f0:\ \eta_n\sum_{k=0}^{14}\mu_k(\lambda/z_n)^k,
 \quad z_n=n(n+1),\quad\lambda=977132.
\]

The positive mu coefficients and lambda are RC128's native analytic tail data. The scaling lambda is retained in every tail moment; the features are not unscaled powers of 1/z_n.

For O=4094, the whole common eta tail satisfies

\[
 T=\sum_{\substack{n>O\\n\text{ even}}}
   \frac{2B}{2n+1}(H_n+s)\eta_n^2
 \le\frac{B}{(H_O+s_-)(O-1)O}
 <5.171\times10^{-9}.
\]

Set z_first=(O+2)(O+3). Each of the three positive tail amplitudes is bounded by

\[
 A_0=1,\quad A_1=(1-6/z_{first})^{-1},\quad
 A_2=\sum_{k=0}^{14}\mu_k(\lambda/z_{first})^k.
\]

Thus every omitted action Gram entry is between zero and A_i A_j T. This is an entry enclosure, not an assumed rank-one Loewner bound. Weighted Young bounds convert the full entry intervals into Loewner matrices and pay all mixed tails.

## 3. Actual first moment and mixed errors

Let V be the three represented action columns and e_i=M S_i-V_i. The inherited full-column D errors are

| Column | Full D error upper bound |
|---|---:|
| P0 | 0.000179348866 |
| P2 | 0.000512542531 |
| f0 | 0.000099881089 |

The validator first evaluates all nine directional pairings S_i* D V_j. Since K=S* L S is symmetric, each actual K_ij belongs to both directional enclosures

\[
 (S_i,DV_j)\pm\sqrt{G_{ii}}\epsilon_j,
 \qquad
 (S_j,DV_i)\pm\sqrt{G_{jj}}\epsilon_i.
\]

Their intersection is retained. The historical RC172 two-source and RC175 f0 mixed rows provide additional independent intersections. All intersections are nonempty. The f0 diagonal and all first-moment mixed entries are now evaluated with full action errors paid.

For w_i=sqrt(G_ii,upper), a correlated action-error upper is the diagonal matrix

\[
 E_{ii}=\epsilon_i w_i\sum_j\epsilon_j/w_j.
\]

For arbitrary real or complex coefficients c, weighted Cauchy-Schwarz gives

\[
 \Big\|\sum_i c_i e_i\Big\|_D^2
 \le(\sum_i|c_i|\epsilon_i)^2\le c^*Ec.
\]

The exact rational PSD check also verifies E-epsilon epsilon* >=0; diagonality makes the same bound valid after taking coefficient absolute values. This is a mixture error bound, not a declaration that error vectors are orthogonal.

Let Qhat=V* D V and b_i=sqrt(Qhat_ii,upper). The actual full action Gram Q=(M S)* D (M S) obeys entry radii

\[
 |Q_{ij}-\widehat Q_{ij}|
 \le b_i\epsilon_j+b_j\epsilon_i+\epsilon_i\epsilon_j.
\]

This pays both mixed carrier/error terms and the error/error term. Weighted Young bounds again give simultaneous Loewner enclosures for all complex source mixtures.

## 4. Certified results

For each matrix, upper-lower <= beta G_lower holds by an exact rational PSD check. The next smaller millionth fails for that selected enclosure.

| Enclosure | Relative width upper beta |
|---|---:|
| Actual canonical first-moment Gram K | 0.011597 |
| Actual full canonical action Gram Q | 0.010509 |
| Full action-error Gram E, relative squared bound | 0.000003 |

Selected new actual entry enclosures, rounded outwards for this table:

| Entry | Lower | Upper |
|---|---:|---:|
| K(P0,f0) | 0.0213380639 | 0.0214339422 |
| K(P2,f0) | 0.0995524978 | 0.0998264981 |
| K(f0,f0) | 0.0222334980 | 0.0222868935 |
| Q(P0,f0) | 0.0137522579 | 0.0139503109 |
| Q(P2,f0) | 0.0293110441 | 0.0294791267 |
| Q(f0,f0) | 0.0077916043 | 0.0078269341 |

The independently evaluated first and second moments also pass the stronger structural checks

\[
 aG\le K\le2G,\qquad aK\le Q\le2K,
 \qquad a^2G\le Q\le4G.
\]

The validator proves these with the adverse enclosure endpoints: for example Q_lower-a K_upper is PSD and 2 K_lower-Q_upper is PSD. The assertions follow from the actual bounded self-adjoint canonical action, and provide independent consistency controls on the realized carriers and Gram arithmetic.

## 5. Validation and scope

All eight inputs are hashed and their checkpoint cross-links checked. Generation and replay reverse both the w14 input summation and the full action-prefix summation. The historical w14 hash and the entire new certificate must reproduce exactly. Every infinite output tail and every mixed action error remains in the enclosures. No finite invariant compression is assumed.

```bash
python scripts/validate_rpb108_rc177_three_source_canonical_action_gram.py \
  --replay --output certificates/rpb108_rc177_three_source_canonical_action_gram.json \
  certificates/rpb108_rc176_f0_regular_output_carrier.json \
  certificates/rpb108_rc172_quadratic_regular_action.json \
  certificates/rpb108_rc171_regular_legendre_projection.json \
  certificates/rpb108_rc129_four_vector_joint_moment.json \
  certificates/rpb108_rc128_collective_second_response.json \
  certificates/rpb108_rc127_enriched_even_endpoint_action.json \
  certificates/rpb108_rc121_diagonal_metric_equivalence.json \
  certificates/rpb108_rc175_f0_regular_physical_source.json
```

The native seven-source frame is unchanged. RC177 completes the canonical first/action Gram on the evaluated P0/P2/f0 family; it does not extend the actual canonical inverse certificate to three sources, identify the original augmentation adjoint range, specify Stage I's required full matrix tolerance, or execute a Riesz iteration.

Next cursor: extend RC173's actual canonical inverse response to P0/P2/f0 using these complete action carriers and paying the full correlated inverse-trial residuals. Stage I, original augmented Weil positivity, whole-aperture original positivity, RH, F4, and Lean remain open/unclaimed.
