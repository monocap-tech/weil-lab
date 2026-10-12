# RPB108 — RC139: two-sided direct reference response

Date: 2026-10-12 UTC. Aperture a=11/10. Branch `research/rpb108-route-consolidation`. Parent RC138, `5c368d73a5e640092db7ef6285b126abd58fc826`.

## Certified result

The normalized full-carrier reference inverse response satisfies

\[
\boxed{0.931329483032\le\Sigma_{00}/G_{00}\le0.931329517607.}
\]

The width is 3.4575e-8, a 1.377932-fold tightening over RC138's 4.7642e-8. The lower and upper endpoints both improve. The seven-vector source family is unchanged. Both selected trials use only the first four combinations in RC138's source frame, but their rational coefficients differ: one optimizes the accepted lower bound and the other the upper bound. Four candidate trials, including an exact replay of RC138's four-combination trial, are retained in the certificate.

## Two-sided residual correction

Let `A=I+C`, where the global D-energy operator satisfies `0<=C<=I`, and let `r=Ay-P_0`. RC138 established the exact identity

\[
\Sigma_{00}=L(y)+\langle r,A^{-1}r\rangle_D,
\qquad L(y)=2\langle P_0,y\rangle_D-\langle y,Ay\rangle_D.
\]

The global spectral bounds `I<=A<=2I` give

\[
L(y)+\tfrac12\|r\|_D^2\le\Sigma_{00}\le L(y)+\|r\|_D^2.
\]

RC138 used a full residual upper bound for the right side and discarded the nonnegative correction on the left. Here the actual residual receives a positive lower bound as well. With RC138's rational source and action matrices `S,T`, a trial coefficient vector `c` has nominal residual `r_0=(S+T)c-e_0`, and the true residual differs from it by at most `e=sum_j |c_j| epsilon_j` in full D norm. The certified Loewner Gram bounds yield

\[
\sqrt{r_0^*G_{Lo}r_0}-e\le\|r\|_D
\le\sqrt{r_0^*G_{Hi}r_0}+e.
\]

The implementation clips the left side at zero, rounds its square root down on a 10^-40 grid, and rounds the resulting lower residual energy down on a 10^-100 grid. For each accepted four-combination trial, the lower energy is strictly positive. The selected lower trial has a certified residual D-energy floor greater than 1.8700867711e-7. It contributes at least half that energy to the absolute response lower bound. The actual `P_0-y` pairing, trial Gram, and endpoint energy keep the signed interval acceptance from RC138. Division by the actual positive `G_00` interval and outward 10^-12 rounding produce the displayed normalized bounds.

The tentative coefficients were selected numerically, but every submitted coefficient is a fixed rational decimal and is accepted by exact rational calculations. No optimizer result, center inverse, or uncertain matrix positivity is used as a proof premise. Both signed accumulation orders and the entire RC138 predecessor certificate are rechecked in replay. Twelve exact scalar controls test both spectral endpoints, intermediate eigenvalues, and signed trials.

## Evidence boundary and next cursor

This certifies only the single `P_0` reference response. It neither supplies a uniformly accurate inverse matrix nor evaluates the original Weil or augmented actions. The required response tolerance for Stage I has not been established here. RC140 should tighten the common-source/t endpoint energy uncertainty or obtain sharper global spectral information, and explicitly test the needed tolerance before transporting to original sources. Whole-aperture positivity, F4, RH, and Lean remain open.

## Reproduction

```bash
python scripts/validate_rpb108_rc139_two_sided_variational_response.py \
  --output certificates/rpb108_rc139_two_sided_variational_response.json \
  certificates/rpb108_rc138_reference_variational_response.json \
  certificates/rpb108_rc137_seven_input_covariance.json \
  certificates/rpb108_rc136_seven_vector_joint_matrices.json \
  certificates/rpb108_rc135_common_response_capture.json \
  certificates/rpb108_rc132_balanced_action_shared_covariance.json \
  certificates/rpb108_rc128_collective_second_response.json \
  certificates/rpb108_rc130_remaining_covariance.json
```

Repeat with `--replay` to compare the complete rational certificate after reversing signed sums and independently rebuilding RC138. The three RC139 files are additive; historical certificates and wording remain unchanged.
