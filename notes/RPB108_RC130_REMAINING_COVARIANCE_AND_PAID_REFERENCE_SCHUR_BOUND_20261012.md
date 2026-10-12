# RPB108 — RC130: remaining covariance and paid reference Schur bound

Date: 2026-10-12 UTC. Aperture a=11/10. Branch research/rpb108-route-consolidation. Starting checkpoint RC129, commit 8e7e6c5004087a24fe9d95be3777576495edcd37.

## Result and decision

RC130 encloses the remaining C psi_0, C w_14 second-moment and projected-covariance block on U=[P_0,psi_0,f_0,w_14]. It pays all omitted input and output tails, the nonorthogonal projection through the actual four-vector Gram, and every residual mixture, including RC128's tiny f_0 row and exact zero P_0 row.

The w_14 residual is genuinely positive after all uncertainties are paid:

\[
\boxed{R_{ww}\ge2.8455721963943\times10^{-5},
\qquad R_{ww}/G_{ww}\ge0.004746548253.}
\]

These are outward lower displays of exact rational acceptance endpoints. The four-vector family cannot meet a whole-family inequality R <= epsilon G below this relative coordinate lower. This is a real remaining response direction, not an enclosure-width artifact. No diagonal Loewner lower is inferred from the coordinate result.

The paid covariance nevertheless permits a positive reference Schur compression and a substantially sharper P_0 reference-response interval:

\[
\boxed{0.931327855055\le\Sigma_{00}/G_{00}
\le0.931339797136.}
\]

RC129's upper was 0.959641776722. The narrowed interval is still a reference inverse-response enclosure, not a high-accuracy evaluated inverse or original Weil response. The remaining psi_0 variance is quantitatively upper-bounded but its lower remains zero in this certificate.

Original coverage remains 10–639 below 0.01. No new positive original direction, original positivity extension, Global/F4 completion or RH result is claimed.

## Definitions and inherited structure

Keep the actual diagonal energy D=J+sI, JP_n=H_nP_n, s=c_R+log2+789/125, B=11/10, endpoint form h=-1/2 log(1-(x/B)^2), and positive D-energy contraction C=D^-1 h. Set z_n=n(n+1) and d_n=2H_{2n}-2H_n+1/(2n+1)-log2.

RC129 supplies complete actual Gram and first-moment enclosures on U. Define

\[
 G=U^*DU,\quad H=U^*hU,\quad H_2=(CU)^*D(CU),
\quad R=H_2-HG^{-1}H.
\tag{1}
\]

R is the residual Gram after D-orthogonal projection onto span(U), hence R >= 0. The exact P_0 action CP_0=((1-log2)/s)P_0+psi_0+f_0 gives an exactly zero residual row and column. RC128's selected w_14 satisfies ||Cf_0-w_14||_D <= epsilon_f, epsilon_f<6.996019e-26. Thus R_ff <= epsilon_f squared. Both facts are for the symbolic f_0 family and RC128's defined w_14; no rounded-vector exact invariance is asserted.

The genuinely remaining columns are psi_0 and w_14. Their joint projection uses all four family vectors and the full nonorthogonal G, not a diagonal replacement.

## Actual actions and paid infinite contributions

Truncate input psi_0 at even degree 4094 and input w_14 to its rational polynomial g_hat on even degrees 0..4094. The omitted w_14 input is its entire analytic part, not zero. The generator and center/radius coefficient SHA-256 of g_hat are independently reconstructed and checked against RC128.

For finite input u, use the actual coefficient action

\[
 (Cu)_n=\frac1{H_n+s}\left[d_nu_n
 +\sum_{m\ne n\atop m\text{ same parity}}
 \frac{(2n+1)u_m}{|z_n-z_m|}\right].
\tag{2}
\]

Directed 70-digit intervals evaluate both columns through even output degree 8190. Rational coefficient centers at 10^-40 define finite action trials q_psi,q_w. Their rounding D energies are summed outward on a 10^-100 grid. The certificate stores their joint coefficient SHA-256, generator and 4,096 coefficients per column for reproducible reconstruction.

Let T bound the leading tail D energy beyond degree 4094, and A be RC129's coefficient domination constant w_tail,n <= A psi_0,n there. Then

\[
\|\psi_{omitted}\|_D\le\sqrt T,
\qquad\|w_{omitted}\|_D\le A\sqrt T.
\tag{3}
\]

Since C is a contraction, (3) pays both omitted source actions. For omitted output n>=8192 and a finite input supported through degree 4094,

\[
 |(Cu)_n|\le
 \frac{2n+1}{(H_n+s)z_n}
 \frac{\sum_m|u_m|}{1-z_{4094}/z_{8192}}.
\tag{4}
\]

The monotone preceding width-two parity cells give a leading output-tail D energy upper

\[
 T_{out}\le\frac{B}
 {(s_{lower}+H_{8190,lower})8189\cdot8190}.
\tag{5}
\]

Equations (3)–(5) and the finite rounding errors combine by the norm triangle inequality. All actual infinite action errors are bounded:

| Actual action versus finite trial | Absolute D norm error upper, outward display |
|---|---:|
| C psi_0 versus q_psi | 7.744094e-5 |
| C w_14 versus q_w | 9.773347e-5 |

These intentionally moderate cutoffs do not certify tiny psi_0 action error. They are sufficient to resolve the positive w_14 covariance direction and obtain the stated Schur response improvement.

## Second-moment lower and upper

All tested input coefficients and same-parity endpoint entries are positive. The full action coefficients therefore dominate those from a positive truncated input, by bounded-action convergence in D energy. Summing the directed finite-action coefficient lower products through degree 8190 gives genuine lower bounds for each remaining H_2 entry. This pays infinite contributions by positivity; it does not identify a finite prefix with the full action.

For upper bounds, if e_i bounds ||Cu_i-q_i||_D, use

\[
 |(H_2)_{ij}-\langle q_i,q_j\rangle_D|
 \le e_i\|q_j\|_D+e_j\|q_i\|_D+e_ie_j.
\tag{6}
\]

Diagonal uppers may also be intersected with H_ii, since C squared <= C. Directed trial Grams, positive action-prefix lowers, (6) and contraction give the full remaining second-moment interval matrix.

## Nonorthogonal projection and complete covariance

Let G_lower <= G <= G_upper be RC129's Loewner bounds. Their positive definiteness permits

\[
 G_{upper}^{-1}\preceq G^{-1}\preceq G_{lower}^{-1}.
\tag{7}
\]

Put J_mid=(G_lower^-1+G_upper^-1)/2 and K_G=(G_lower^-1-G_upper^-1)/2 >=0. Equation (7) implies the signed entry enclosure

\[
 |(G^{-1}-J_{mid})_{ij}|
 \le\sqrt{(K_G)_{ii}(K_G)_{jj}}.
\tag{8}
\]

This is a consequence of -K_G <= G^-1-J_mid <= K_G and contraction in K_G coordinates. It is not obtained by inverting entrywise intervals. Exact rational inversion, directed rational square-root uppers and signed interval products pay every entry of H G^-1 H on the two remaining columns.

Subtract that full projection enclosure from the remaining H_2 enclosure. Intersect diagonal lowers with zero and diagonal uppers with source energy. The psi_0 diagonal upper may additionally be intersected with RC127's old residual upper by projection monotonicity. Residual Cauchy-Schwarz intersects the mixed entry with +/-sqrt(R_psi,psi,upper R_ww,upper).

| Actual remaining covariance | Lower, outward display | Upper, outward display |
|---|---:|---:|
| R_{psi,psi} | 0 | 4.094930e-8 |
| R_{psi,w} | -9.091919e-8 | 1.352452e-6 |
| R_{w,w} | 2.8455721963943e-5 | 4.466802238143e-5 |

The mixed sign is unresolved and retained. A positive w coordinate lower does not imply R >= diag(0,0,0,r_w). The complete matrix upper must pay the mixed term.

To obtain the **full four-input covariance**, embed this block in the psi_0/w_14 rows, insert the exact zero P_0 row, and use R_ff <= epsilon_f squared. Each remaining f mixed term is bounded by sqrt(epsilon_f squared R_ii,upper). Thus every mixture of all four inputs is paid without redundantly recomputing the already controlled columns.

Entry bounds are converted to full weighted Loewner matrices with RC127's weighted Young inequality. Exact rational checks accept the resulting full covariance upper as PSD. The interval Loewner lower need not be PSD; the independent residual-Gram theorem supplies R >= 0. RC130 certifies the complete projected covariance enclosure efficiently, rather than evaluating all sixteen entries of H_2 afresh.

## Paid reference Schur response bound

For the D-orthogonal complement, I <= I+C_complement <= 2I. The Schur subtraction S therefore satisfies R/2 <= S <= R. The exact family response is

\[
 \Sigma=G(G+H-S)^{-1}G.
\tag{9}
\]

Using full correlated bounds, define

\[
 N_{lower}=G_{lower}+H_{lower}-R_{upper}.
\tag{10}
\]

Exact rational acceptance and nonsingular inversion verify N_lower>0. It follows that

\[
 \Sigma\preceq G N_{lower}^{-1}G.
\tag{11}
\]

Gram uncertainty on the two outside factors in (11) is paid; G is not silently replaced by its midpoint. Set K_N=N_lower^-1, G_mid=(G_lower+G_upper)/2, E_G=(G_upper-G_lower)/2, and tau=tr(E_G K_N). RC129's interval construction makes E_G a positive diagonal matrix and -E_G <= G-G_mid <= E_G. Consequently

\[
 (G-G_{mid})K_N(G-G_{mid})\preceq\tau E_G.
\tag{12}
\]

This follows by normalizing the Gram error as a contraction and bounding the largest eigenvalue of E_G^(1/2) K_N E_G^(1/2) by its positive trace. Weighted Young gives the stored full joint upper, with t=1/1000,

\[
 \Sigma\preceq(1+t)G_{mid}K_NG_{mid}
 +(1+1/t)\tau E_G.
\tag{13}
\]

Its difference from RC129's valid response lower passes an exact rational PSD check.

Individual diagonals can be sharper. If a_i=(G_mid K_N G_mid)_ii and b_i=tau(E_G)_ii, the scalar norm triangle inequality gives

\[
 \Sigma_{ii}\le a_i+b_i+2\sqrt{a_ib_i}.
\tag{14}
\]

The certificate pays the square root outward. Equation (14) is a separate coordinate upper, not a joint Loewner matrix assembled from optimized diagonals. For each coordinate, take the best of (14), the diagonal of (13), and RC129's separate secant matrix upper. These coordinate minima do not produce a new full matrix bound.

| Reference response / actual source D energy | Lower | Best paid coordinate upper |
|---|---:|---:|
| P_0 | 0.931327855055 | 0.931339797136 |
| psi_0 | 0.546115679979 | 0.744748832485 |
| f_0 | 0.822558697000 | 0.824115275162 |
| w_14 | 0.721915635146 | 0.740914960159 |

The full joint matrix upper (13), all covariance Loewner bounds and the individual optimized results are stored distinctly. The P_0 interval width is about 1.195e-5 in units of its source D energy. It is substantially smaller than the first-moment-only width, but does not reach a 10^-6, 10^-12 or 10^-24 inverse-response budget.

## Next cursor and evidence boundary

The complete residual covariance is now paid, and its Schur response bound is useful. The remaining w_14 coordinate is genuinely nonzero, so another substantial response must be captured or bounded to improve the prescribed inverse-response gap. The psi_0 block is still broadly enclosed; its required accuracy must be assessed through the joint response budget, not guessed from an independent column norm.

**RC131 cursor:** investigate a collective representation of the residual Cw_14 after projection onto U, paying its correlation with Cpsi_0. Alternatively sharpen the signed remaining Schur block enough to meet an explicit source-response tolerance. Cw_14 has an infinite analytic input; RC128's finite-input geometric expansion cannot be reused for the whole vector without paying the analytic-source action. Keep that distinction explicit. Use the now certified joint matrices and response width as the stopping criterion, rather than adding individual native directions by default.

The covariance and Schur theorem concern C and the positive reference I+C. They are not original Weil source leakage or original augmented responses. Original completion still requires Hhat=A_Q+T_Weil^*T_Weil >= eta I and T_Weil Hhat^-1T_Weil^* <= theta I for theta<1 after actual original actions. The inherited W_639 floor and original count are unchanged; no floor is transferred to this physical response decomposition.

**Certified:** remaining joint actions with full norm errors, second-moment enclosures, nonorthogonal projected covariance, full four-input covariance including all mixed terms, positive w_14 obstruction, positive reference Schur compression, and improved reference response bounds. **Not certified:** a small whole-family variance, high-accuracy inverse, regular multiplier action, original augmented response, original positivity, Global/F4 or RH.

## Reproduction

Inputs: RC129, RC128, RC127, in that order. Byte-level SHA-256 linkage and the reconstructed RC128 polynomial hash are checked. Directed 70-digit coefficients and finite action Grams are combined with exact rational tail bounds, inverse-Gram Loewner-to-entry enclosures, signed interval projection products, covariance PSD acceptance and Schur congruences. Replay reverses finite-source, coefficient-action and output Gram sums and compares the entire rational certificate.

```bash
python scripts/validate_rpb108_rc130_remaining_covariance.py \
 --output certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc128_collective_second_response.json \
 certificates/rpb108_rc127_enriched_even_endpoint_action.json
```

Repeat with --replay. The validator imports immutable RC127/RC129 helpers. Only additive RC130 script, certificate and note files are committed; prior checkpoints, Lean and unrelated branch work are preserved.
