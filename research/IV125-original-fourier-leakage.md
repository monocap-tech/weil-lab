# IV125 — Original Fourier leakage attachment

Five Lean proof candidates on the IV124 branch. Exact cell-mean cancellation and cell payment are implemented for a restricted measure and a supplied a.e. phase-difference bound. The actual Fourier L2 pointwise squared majorant C xi² is integrated on (-T,T] with constant 2 C T³/3. The low-band mass bound is connected by Plancherel, complementary integration and monotonicity of the native logarithmic weight to IV124's response-corrected Schur receiver.

Still missing: the exponential phase Lipschitz proof, a genuine equal-cell partition and recombination lemma, physical L1/L2 Cauchy–Schwarz on the window, and a.e. transport of the resulting Schwartz Fourier pointwise estimate to the L2 representative (the current pointwise receiver is stronger than necessary; an a.e. receiver is preferable). No unconditional finite-codimension coercivity yet. The sharper primitive/Poincare alternative remains unimplemented. No new source normalization or global sign claim.

Native verification: compile IV124 and IV125 together, audit all ten exact named declarations, preserve source hashes, compiled objects and logs. Static source preflight only; not a kernel receipt. Parallel IV123 custody run was active when staged; no new workflow activated here.
