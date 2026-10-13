# RC215 — correlated common carrier and t10 precision target

Parent: RC214 `3bd7243d11cf758c6ec5bc16ff388b7a2ac474fe`.

RC215 supplies a complete canonical carrier for the native common source u = (v10 + z_b6)/2. It uses the pinned v10 carrier plus one half of RC214's difference carrier. Linearity gives e_u = e_v + e_delta/2 and a full D-norm error at most **0.000025947382**. The source includes the unchanged native finite centers and averaged selected analytic tails. RC212's common finite-source hash is checked against RC135. This common source is in the existing span and does not add a ninth independent source.

## Eight-source correlated error test

Keep the eight native-plus-P2 sources and RC213's rigorous source Gram floor unchanged. Replace the z action trial by v trial plus delta trial, as required by RC214. For native coefficients x, the error generator coefficients are

- e_v: x_v + x_z;
- e_delta: x_z;
- every other generator: its original coefficient, including e_t10.

The validator enumerates all 128 signed rank-one controls, fixing the first sign to remove global duplication. Each control uses the exact inverse of the rational source Gram floor. For real coefficients the triangle envelope is the maximum signed quadratic form; for complex coefficients the real and imaginary parts inherit the same bound because all sources, operators, and carriers are real. No error-generator orthogonality is assumed.

The certified relative squared-error factor improves from **304.038475** to **5.269262**, over 57.7 times smaller. It remains above the sufficient half-Gram threshold **0.5**. The certificate includes an exact failed envelope witness. This failure is not a lower bound for the true action error and does not imply an inverse or operator failure.

The t10-only envelope factor is above **4.201389**, so even perfect knowledge of the other errors would not make the current independent t10 radius pass this fixed error model. Setting only the t10 radius to zero would give factor at most **0.319818**. That is a counterfactual diagnostic, not a new t10 certificate.

## Concrete next target

Each of the 128 controls is stored as an exact quadratic in a future t10 radius tau. Exact integer-grid bisection brackets the largest radius accepted by this fixed sufficient envelope and source Gram floor between **0.000075812305** and **0.000075812306**. This is a limit of the current envelope, not an intrinsic limit on the operator or a lower bound on the true error.

A convenient stricter target is one eighth of RC212's complete t10 radius: at most **0.000069481172** (outward decimal; the exact target is stored in the certificate). If that full native t10 action bound is proved, while the other carriers retain their current certified radii, the correlated error factor will be at most **0.478972**, with margin **0.021028** below 0.5. The target itself has not yet been attained for the actual action.

## Validation and remaining work

Normal execution and reversed sign-enumeration replay agree exactly. Immutable input and helper Git blob pins are checked against the live parent tree; a deliberately incorrect input pin is rejected. All 64 updated source/action and represented-action pairing error payments are supplied. Compatible nominal mixed/action/residual centers have not yet been assembled.

The accepted RC210 six-source inverse width stays **0.436100**. The expanded inverse remains untested. Source-range/augmentation obligations, odd coverage, Stage I, RH, F4, and Lean closure remain open.

Next cursor: RC216 — tighten the complete native t10 canonical action to the concrete radius target, then assemble compatible expanded mixed/action/residual centers and test the inverse gate separately.
