# RC153: nonzero correlated difference action

Resume from RC152, commit `76cda833f81684183b55a656878436cb8510fa81`, on `research/rpb108-route-consolidation`. The aperture remains 11/10. Write delta = z_b6-v10, with the RC132 and RC131 selected six- and ten-feature collective vectors. C is the inherited positive endpoint contraction on the D Hilbert carrier; 0 <= C <= I.

RC153 constructs a nonzero finite polynomial q_delta approximating Cdelta. It reconstructs the two stored rational center polynomials through degree 8190, verifies their separate predecessor coefficient/radius hashes, and subtracts their coefficients before applying C. The finite difference energy also agrees exactly with RC134. The action trial uses the signed difference source through degree 4094 and outputs through degree 8190. All subsequent signed mixtures retain a paid error budget.

The source tail consists of the omitted finite difference coefficients plus the common analytic tail. The latter is bounded using RC134's combined moment polynomial, taking absolute values only after combining the moments. The omitted source energy is at most 9.792009e-11. For the infinite output from the retained finite source, the geometric denominator estimate pays energy at most 9.740696e-12. Directed interval arithmetic pays finite coefficient rounding. The contraction pays the entire omitted input. By the triangle inequality,

\[\|C\delta-q_\delta\|_D\le\sqrt{E_{round}}+\sqrt{E_{out}}+\sqrt{E_{in}}<0.000013016467.\]

The squared error upper bound improves over RC152's zero trial by a factor greater than 140.43967. This is an improvement of certified upper bounds; no lower bound on actual error is asserted.

Together with RC130's inherited q_psi trial, every mixture a psi0+b delta has error energy bounded by the diagonal matrix

\[E=\operatorname{diag}(2\epsilon_\psi^2,2\epsilon_\delta^2).\]

This is Young's inequality with no assumption about the mixed error sign. Against RC151's conditional source Gram lower G, exact rational PSD bisection establishes E <= 2.482091 G. The previous factor was 38.055323. On RC151's witness the new ratio is approximately 2.367799. The half-Gram action-envelope gate remains unproved.

There is a second, precise limitation: even setting epsilon_delta to zero in this particular diagonal envelope leaves the required relative factor at least

\[\frac{2\epsilon_\psi^2}{G_{00}-G_{01}^2/G_{11}}=2.23934356\ldots>1/2.\]

Thus further difference-column improvement alone cannot make this inherited diagonal envelope pass. A sharper Cpsi0 trial or a correlated joint error estimate is required. This statement concerns this explicit envelope, not the uncertainty of the true inverse response. Mixed response rows with the five paid directions are still unevaluated. Passing an action-error gate would itself not certify the inverse-response matrix width.

Next: refine Cpsi0 and the joint error correlation, evaluate mixed endpoint pairings of q_delta with the paid five-source frame and psi0, then assemble the seven-source inverse-response enclosure. Original Weil/augmented transport and a stated Stage I tolerance remain separate obligations. No whole-aperture positivity, Stage I closure, F4, RH, or Lean closure follows.

## Reproduction

```bash
python scripts/validate_rpb108_rc153_correlated_difference_action.py \
 --output certificates/rpb108_rc153_correlated_difference_action.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc134_correlated_six_input_covariance.json \
 certificates/rpb108_rc151_complement_schur.json \
 certificates/rpb108_rc152_complement_action_budget.json
```

Add `--replay` to reconstruct in reversed inner summation order and check exact certificate equality. Inputs are hashed; historical files remain unchanged.
