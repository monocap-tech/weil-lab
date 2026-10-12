# RC154: complementary action-error half-Gram gate

Resume from RC153 (`4822bd2a711b713811d36dc5ef0905df81816e8a`) on `research/rpb108-route-consolidation`, aperture 11/10. The additive definitions in `docs/TERMINOLOGY_RPB108_RC154_CENTERED_TAIL_ACTION.md` specify the centered analytic input-tail trial, the output-tail moment trial, and the two-column action-error half-Gram gate.

RC153 paid a nonzero Cdelta trial for delta=z_b6-v10, but its inherited Cpsi0 error prevented the diagonal joint envelope from passing. RC154 replaces the Cpsi0 trial. It extends the exact source prefix to even degree 8190 and the finite action outputs to degree 16382. A 25-term moment expansion pays the entire infinite output tail of this finite source. The remaining infinite input tail is approximated by its midpoint under the positive endpoint contraction.

Write psi0=p+t and define q_psi=Q(p)+(1/2)t. The trial is an explicit finite polynomial plus two prescribed analytic tails. Since 0<=C<=I on the full D carrier,

\[\|(C-I/2)t\|_D\le\tfrac12\|t\|_D.\]

This does not assume that C commutes with the degree cutoff. For even n>=16384, the retained finite source action equals eta_n times a positive geometric moment series. The 25th-order moment interval pays the remainder, while all retained moment radii pay rounding. Here eta_n=(2n+1)/(n(n+1)D_n), D_n=s+H_n, and the moment scale is 8190*8191. The input and output tails are treated separately even where their supports overlap.

The certified input-tail energy is below 1.224933e-9, and its centered error energy is one quarter of that bound. The output geometric remainder energy is below 9.048791e-46. Including finite action rounding and moment rounding,

\[\|C\psi_0-q_\psi\|_D<0.000017499518.\]

The squared-error upper bound improves over RC130 by more than 19.58344 times. RC153's paid Cdelta trial is retained. Young's inequality supplies, for every real or complex mixture a psi0+b delta, a two-column squared-error envelope

\[E=\operatorname{diag}(2\epsilon_\psi^2,2\epsilon_\delta^2).\]

Exact rational PSD bisection, with a 1e-6 grid and rejection of the preceding grid point, certifies

\[\boxed{E\preceq 0.365680\,G_{conditional}\prec\tfrac12G_{conditional}.}\]

On RC151's fixed witness mixture, the envelope-to-conditional-Gram ratio is approximately 0.36372617. The psi-only envelope factor that remained above 2.2393 at RC153 now falls to approximately 0.11434882. No sign of the mixed action error is assumed and no lower bound on actual error is inferred.

This closes the two complementary action-approximation precision gate. It does not evaluate mixed response rows, certify the seven-source inverse-response matrix width, specify a Stage I numerical tolerance, or transport the result to original Weil/augmented actions. Stage I, whole-aperture positivity, F4, RH, and Lean closure remain open.

The next calculation is concrete: evaluate the new psi trial and RC153 delta trial against the five paid source directions and each other, pay their analytic tail mixed pairings, and assemble a seven-source variational inverse-response enclosure. Test the resulting matrix width against an explicit Stage I tolerance; an action-error gate alone cannot substitute for that test.

## Reproduction

```bash
python scripts/validate_rpb108_rc154_centered_analytic_tail_action.py \
 --output certificates/rpb108_rc154_centered_analytic_tail_action.json \
 certificates/rpb108_rc129_four_vector_joint_moment.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc151_complement_schur.json \
 certificates/rpb108_rc153_correlated_difference_action.json
```

Add `--replay` to reverse every inner source summation and check exact certificate equality, including the finite coefficient/radius hash. The certificate hashes all four inputs and retains explicit analytic moment intervals. Historical checkpoint files are unchanged.
