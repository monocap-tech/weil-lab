# RC152: action error on the two uncovered directions

RC151 identified the independent complement `psi0`, `delta=z_b6-v10` to the five paid RC149 sources. This pass combines existing, separately certified action information into one two-column estimate. RC130 constructs a finite polynomial trial for `Cpsi0` with full D-norm error at most 0.00007744094. RC134 bounds the full D-energy of `delta` by 2.37944693e-8. Since the positive endpoint contraction obeys `0 <= C <= I`, the zero polynomial is a valid first trial for `Cdelta` with squared error at most that source energy.

For every rational mixture `a psi0+b delta`, the squared error of these two trials is bounded by

\[2a^2\epsilon_\psi^2+2b^2\|\delta\|_D^2.\]

This is the signed Young inequality; it pays the possible mixed error without assuming orthogonality. The resulting diagonal Loewner error matrix is compared by exact rational PSD checks to RC151's conditional source Gram lower. The certified relative upper factor is **38.055323**. On the RC151 witness mixture the error envelope is about **5.03857e-8**, against conditional source Gram lower **1.32426e-9**, a factor **38.04823**. The delta diagonal error budget alone is **2.04495** times its conditional Gram diagonal, while the psi diagonal budget is **0.12743** times its diagonal.

These are bounds on a trial's possible error, not lower bounds on its actual error or on the true inverse response. They do not rule out a sharper correlated `Cdelta` trial. They show precisely why importing the existing `Cpsi0` polynomial and a contraction bound for `Cdelta` does not certify the seven-source half-Gram matrix precision. The next calculation needs a nonzero correlated difference action trial and paid mixed endpoint pairings with the five existing directions. Original Weil or augmented actions and the required Stage I tolerance are still outside this calculation.

## Reproduction

```bash
python scripts/validate_rpb108_rc152_complement_action_budget.py \
 --output certificates/rpb108_rc152_complement_action_budget.json \
 certificates/rpb108_rc151_complement_schur.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc134_correlated_six_input_covariance.json
python scripts/validate_rpb108_rc152_complement_action_budget.py --replay \
 --output certificates/rpb108_rc152_complement_action_budget.json \
 certificates/rpb108_rc151_complement_schur.json \
 certificates/rpb108_rc130_remaining_covariance.json \
 certificates/rpb108_rc134_correlated_six_input_covariance.json
```

The certificate records hashes of its three predecessor certificates and the RC130 finite action trial hash. Earlier checkpoint files are unchanged. No whole-aperture positivity, F4, RH, or Lean closure follows.
