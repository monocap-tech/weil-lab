# RPB108 — LF48: uniform physical action budget

## Submitted theorems

Derive an absolute full-line jump budget: the integral of the norm of the actual trial jump is at most 2 B L + M E_B(x), where E_B retains both genuine exterior endpoint tails. The assumptions are measurable trial, cap-interior evaluation point, pointwise Lipschitz cancellation bound L on the cap, and norm bound M at the evaluation point.

A real-valued integrable majorant partitions space into the cap (constant L) and both exterior half-lines (M times the actual jump density). Its integral is computed from the exact exterior-tail identities. In particular, this controls the integral of the norm, which is stronger than a bound on the norm of the integral.

Use cutoff-independent pointwise domination to obtain the same bound for every truncated spatial jump integral. Finally transport the bound through the finite time-action identity: the norm of the trial value plus any positive-lower-cutoff Poisson time-mixture action is at most M + 2 B L + M E_B(x). Cap bounds supply the trial-zero-extension hypotheses. The budget is independent of both time cutoffs. No new definitions are introduced.

## Validation boundary

LF46 run 38156067404, job 114522019567, and LF47 commit ba34eab71ac16212256d7311868d20be303c4e26 run 38157540913, job 114525888683, both passed targeted certificate transport, complete root library, and unfinished-declaration rejection. Thus spatial dominated convergence and limiting physical time-action identification are now checked. LF47 is the latest full-root validated checkpoint. LF48 awaits cumulative CI; no local Lean executable is available.

## Remaining

The endpoint-aware bound prepares an L2 majorant and physical test-pairing convergence. It does not itself assert L2 convergence or a spectral source identity. Physical weak attachment, L2 convergence, and spectral identification remain open. No aperture positivity, F4 closure, or RH claim.
