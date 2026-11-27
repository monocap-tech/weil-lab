# IV106-E18Y — Explicit native operator reserve (analytic derivation, pending Lean)

## Frozen source and dependencies

- Native operator and norm conventions: research commit 018f7e59f4129ce521cd3ae86d1afd59d3b64b5f, `WeilDefect/Arithmetic/ActualZetaNativeFormOperator.lean`, `WeilDefect/Morphology/NeutralLogPoleSourceAttachment.lean`, `WeilDefect/Morphology/NeutralLogHilbertCarrier.lean`.
- Existing Stirling bound: `neutralActualZetaDigamma_log_error` in `ActualZetaNativeLogBounds.lean`.
- Existing convergent series: `Zeta23.DigammaSeries.hasSum_digamma_series`.
- E17A candidate `neutralIV106E17ASymbol_shift` supplies lower bound w <= S+20; `neutralIV106E17APrime_bound` supplies absolute prime bound 8. Their native status must be verified separately.
- w(xi)=log(exp(1)+abs(xi)) >= 1. S is the actual signed compact-window Weil symbol at a=11/10. The native operator is the compression of multiplication by S/w plus the two rank-one cross-pole terms.

## 1. Explicit upper gamma bound

For z=1/4+i*pi*xi and abs(xi)>=1, the source Stirling lemma gives
Re psi(z) <= log|z|+4. The triangle bound gives
|z|/pi <= abs(xi)+1/(4*pi) <= abs(xi)+exp(1).
Therefore the archimedean symbol A(xi)=Re psi(z)-log(pi) <= w(xi)+4.

For abs(xi)<=1, the convergent partial-fraction series implies that Re psi(1/4+iy) is nondecreasing in abs(y). In detail, for r>0 the quantity Re(1/(r+iy))=r/(r*r+y*y) is nonincreasing in abs(y). Apply this termwise to the negative reciprocal at r=1/4 and all negative reciprocal terms at r=n+5/4; pass to the convergent sum. Hence A(xi)<=A(1). At xi=1 the same Stirling estimate and triangle inequality give A(1)<=4+log(1+1/(4*pi))<5. Since w>=1, A(xi)<=w(xi)+4 on the remaining compact interval too. No numerical digamma sampling is needed.

With the absolute prime bound 8, S<=w+12. The E17A lower candidate gives S>=w-20. Consequently -19*w<=S<=13*w since w>=1. In particular |S/w|<=19, so the weighted L2 multiplier and its orthogonal compression have operator norm <=19.

## 2. Pole reserve

The physical map is contractive: Fourier inversion is an isometry and multiplication by 1/sqrt(w) is contractive. Its restriction to the supported carrier is contractive, as is its adjoint.

The two physical moment columns are 1_[-a,a](x)*exp(±x/2). Their squared L2 norms both equal exp(a)-exp(-a). At a=11/10 this is less than 4. An exact rational proof of exp(11/10)<4 follows by bounding the exponential series after degree 3: each consecutive term from degree 4 has ratio <=11/50, so the tail is bounded by (11/10)^4/4!/(1-11/50). The sum through degree 3 plus this tail is <4.

Therefore both log moment source vectors have norm <2. Each of the two rank-one operators has norm <= the product of source norms, <4. The full cross-pole operator has norm <8.

## 3. Receiver

The conservative candidate bound for the full native operator is K=27 (19+8). This is a mathematically derived bound conditional on the E17A estimates and formal attachment of the monotonicity, compression and pole norm inequalities. It is NOT yet a native certificate.

If the second argument has both source moments exactly zero, the mixed pole form is exactly zero by the existing native pole mixed identity. In particular, on the receiving bank and its approximation errors, if all these vectors are moment-neutral, the restricted mixed continuity reserve can use K=19 without paying the pole bound. This must not be substituted for the full operator norm in an unrestricted theorem.

With the exact rational rough-bank calculation M=7, the uniform entrywise error candidate is K*(14*delta+delta^2). E18V gives delta<=2*epsilon. The corresponding bound is K*(28*epsilon+4*epsilon^2). These are local perturbation reserves, not terminal E16 Schur certificates.

## 4. Verification boundary

The installer-only E18X repair does not change the 35-blob dependency manifest. This analytic note is outside the workflow path filter and does not activate another runner. The first native compilation must finish before declarations are admitted. No RH assertion follows.
