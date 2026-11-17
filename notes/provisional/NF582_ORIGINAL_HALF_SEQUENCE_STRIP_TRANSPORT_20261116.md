# NF582 — actual one-collar sequence: transform, uniform envelope, pointwise limit

Stacked on NF581 #612. All new Lean code is compiler-pending.

## Recovery

NF579 job 133861153155 (run 44030545789) completed with failure. Its now-accessible mollifier diagnostics begin with the lexer token |* in the product of two absolute values; the remaining reported unsolved goals in that theorem are downstream of the parse break. Fixed this in the actual mollifier module and proactively in NF580 scalar-limit module. The earlier mollifier definitions and smoothness proofs did not report independent errors in that log; this is not a PASS for the full module. NF580 job 133865519805 still running, Gram and scalar-limit steps failed; final logs not yet available at inspection. No additional verified terminal theorem is claimed.

## Literal sequence

Define s_n = 1 - (1/(n+1))/2, exactly the historical contraction. Independent ScaleSequence module implements s_n >= 1/2, s_n > 0, s_n < 1, s_n -> 1. Use the same positive half support (549/500,11/10), c=1099/1000, and epsilon=(1-s)/2000. No additional choice of an approximating family.

New HalfSequence module connects the prior twisted-integrability theorem with the actual affine compressed and mollifier factors. For any real integrable h supported in that positive collar, the actual transform satisfies the candidate identity

V_s(z)=R_s(z) [s exp(i z (1-s)c) H(sz)].

Assuming the source half has the retained strip envelope |H(z)| <= C E(Re z), uniform on |Im z|<=1/2, then for every 1/2<=s<1 the actual convolution has |V_s(z)| <= exp(1) C E(Re z). The loss exp(1) is a consciously relaxed bound, rather than the tighter NF577 factor 2, because the graph limit only needs a common finite constant. The underlying estimate is exp(epsilon/2+(1-s)c/2) and the dilation scalar satisfies s E(st)<=E(t). For the explicit s_n the scalar limits of R, affine phase and H imply V_{s_n}(t)->H(t) for every real t. No physical L2 dilation theorem or log-energy convergence premise.

Mathematically reflection then gives the real-odd approximation transform G_s(z)=V_s(z)-V_s(-z), majorant 2 exp(1) C E(Re z) and pointwise convergence. The remaining formal attachment of this reflection, actual Schwartz samples, and endpoint h_U integrability/strip bound is not part of the new HalfSequence theorem. The exact source U binding and source-specific integration by parts remain open. The relaxed envelope is sufficient for graph dominated convergence, not a new quantitative signed Weil-form certificate.

Focused workflow added. No local Lean executable, no main merge, no fresh numerical replay. The earlier accepted original global independence, multiplicity divisor majorant, continuum log admission and collar/scalar geometry receipts stand. Full unconditional Gram, continuum and divisor norm/graph convergence and full Weil coercivity remain compiler-pending or open; W_ODD_NEG and RH OPEN.
