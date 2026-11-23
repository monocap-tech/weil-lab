# F08-008 — independent original physical-window Fourier source/ZIP/axiom custody

**STAGED, NONPROMOTING.** Producer [F08-007 PR #944](https://github.com/monocap-tech/weil-lab/pull/944), actual source head `35db6076439e24751bab335a1d1250ff3c6a8b77`. Candidate compiler [run 45232969334](https://github.com/monocap-tech/weil-lab/actions/runs/45232969334). Do not claim a mathematical certificate until that run completes genuine `.olean` build, strict 3/3 named standard-only axioms, and this separate independent archive succeeds.

Original research fixed at `614ba879f7389fdb620c474adaee273b00eac71c`; source `ActualZetaCorrelationFourierAgreement.lean` Git blob `60453bd214c43feedb0fa64d74a15bd452e48998`, upstream source `ActualZetaCorrelationTransform.lean` Git blob `d5aa1095b2fe64933ad8db64732d232631d3d3b7`; source-actual additive generated Lean `OriginalWindowMollifierFourier.lean` Git blob `606d324ca9fcfd53d059efe1b57d1b0e30349476`. The built source must preserve `neutralWindowRepresentative`, `neutralWindowEvaluation a (-2πξ)`, `neutralRawTransform` and the correct `ContinuousLinearMap.mul ℂ ℂ` convolution.

After a successful producer run, bind real artifact ID/digest and independently verify GitHub producer head/run/job, full ZIP SHA256 and CRC, exact generated Lean source SHA, actual direct Lean build transcript, and three named axiom reports with four adversarial refusals. **Placeholders deliberately block acceptance now.**

On PASS the only accepted new lemmas are: L¹ compact-window representative; ordinary pointwise Fourier of its convolution with any integrable complex `rho` = original `neutralWindowEvaluation a (-2πξ)` times `𝓕rho`; the original positive-exponent raw-transform version.

Not established by this audit: existence/normalization of smooth unit-mass mollifier, `|𝓕rho|≤1`, `𝓕rho→1`, physical support gap or weighted L² Fourier equivalence, `C_c^∞((-a,a))` density, original full mixed `Zeta23.EF.literatureRHS`↔native operator, arbitrary support positivity, F42 or RH.

**Producer preflight finding:** original run 45231015520 fully built the 9,032-job Lean module and printed three standard-only axioms but the *workflow's* single-line parser rejected Lean's legitimate multiline pretty-printing of two names. Source-theorem statements and original mathematics were unchanged. New workflow head `35db6076439e24751bab335a1d1250ff3c6a8b77` uses a strict multiline-aware parser; independent F08-008 likewise accepts line wraps, still refusing extra names, `sorryAx`, duplicates, and unexpected output.
