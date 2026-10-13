# RPB108: explicit actual theta/count constant

Base: research 3dcdf03409f92a4ce4f36f5e008538e7c7c94976.

## Explicit theta bound

The pinned mathlib revision 5ed2965256430c3649e86755f9576b54eca72435, Mathlib/NumberTheory/LSeries/HurwitzZetaEven.lean, provides evenKernel_eq_cosKernel_of_zero and hasSum_nat_cosKernel₀. At parameter zero these identify the actual remainder as
\[
R(t)=\operatorname{evenKernel}(0,t)-1
 =2\sum_{j=0}^\infty e^{-\pi(j+1)^2t},\qquad t>0.
\]
This is the exact normalization used by neutralActualZetaThetaRemainder.

For j>=0, (j+1)^2>=1+3j, because the difference is j(j-1)>=0 for integer j. Since pi>3 and t>=1, termwise nonnegative comparison and the geometric series give
\[
0\le R(t)\le\frac{2e^{-\pi t}}{1-e^{-3\pi t}}
 \le 4e^{-3t}.
\]
Indeed 3pi t>=9 and exp(9)>=1+9>2, so exp(-3pi t)<1/2. This proves concrete decay parameters p=3,C=4 without the existing asymptotic Big-O witness or compact-interval supremum.

## Replay of the certified count derivation

This is an analytic replay of the existing proof steps with these parameters. The Lean APIs currently package their parameters existentially; no specialization in Lean is claimed.

ActualZetaThetaGrowth.lean polynomial/moment estimates retain p,C. ActualZetaMellinGrowth.lean and ActualZetaMellinRepresentation.lean retain them through the two-tail half-sum. ActualZetaFactorialEnvelope.lean gives the same factorial majorant, whose logarithmic conversion in ActualZetaLogGrowth.lean uses
\[
q=p/2=3/2,\quad
B=\max(1,Ce^{-q}/q),\quad b=\max(1,1/q).
\]
Here B=b=1: exp(3/2)>=1+3/2+(3/2)^2/2=29/8>8/3, so (8/3)exp(-3/2)<1. The scalar logarithmic conversion constant is therefore
\[
D=\log(B+1)/\log2+2+\log b/\log2=3.
\]
The Jensen/moment count constant is D/log2=3/log2. The cumulative height count proof multiplies this by 6(log7/log2+1), and the dyadic band count proof multiplies the result by 6. Thus its admissible constant is
\[
A_0=\frac{108}{\log2}\left(\frac{\log7}{\log2}+1\right).
\]
Since log2>=1/2 (integrate 1/t>=1/2 on [1,2]) and log7<log8=3log2, A_0<864. Hence the explicit integer choice
\[
\boxed{A=864}
\]
is valid for every actual raw-copy dyadic band:
\[
\#\{q:b(q)=n\}\le864(n+2)2^n.
\]
This counts multiplicities and needs no simplicity or lower distinct-point density. The result follows from the actual theta/Mellin/Jensen proof, not an imported numerical zero table or RH assumption.

Source references:
- Pinned mathlib kernel identity: https://github.com/leanprover-community/mathlib4/blob/5ed2965256430c3649e86755f9576b54eca72435/Mathlib/NumberTheory/LSeries/HurwitzZetaEven.lean
- Actual project sources at the base commit: ActualZetaThetaGrowth.lean, ActualZetaMellinGrowth.lean, ActualZetaMellinRepresentation.lean, ActualZetaFactorialEnvelope.lean, ActualZetaLogGrowth.lean, ActualZetaDyadicSummability.lean, all under WeilDefect/Arithmetic.

## Numerical constant in the fixed-packet cutoff

For N>=1 and one unchanged lawful finite Green packet w with physical coordinate h,
\[
|Q_{B,s}(w)-Q_N(w)|
 \le\boxed{6912\,a e^a\|h'\|_2^2(2N+6)2^{-N}}.
\]
This substitutes 864 into the preceding fixed-packet sign theorem. The bound is conservative. The unspecified count constant is now eliminated at the analytic level.

Complete verified actual zero data in the finite prefix, selection/multiplicity data, and rigorous packet/gradient evaluation remain necessary for a numerical sign certificate. In particular, the two-column candidate needs a supplied actual off-line orbit; none is known or supplied here. No signed sample computation is claimed.

## Validation boundary

The explicit theta decay and numerical count specialization are analytic proofs, not Lean formalizations. The pinned kernel source was read to check normalization. A floating-point evaluation of A_0 was used only as a sanity check; the integer bound 864 is proved above by exact inequalities.

No Lean source or workflow changed; no new CI claim. Latest certified Lean head remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775. Existing existential proofs remain unchanged.

No actual off-line existence, background positivity, full graph density, retained source/null membership, simplicity or spectral operator-domain membership is assumed. WD-T38 remains independent; FULL TRANSPORT CLOSED is open.

## Cursor/residue

At 3dcdf03, the actual theta series supplies explicit decay parameters p=3,C=4 analytically. Replaying the pinned Mellin/factorial/Jensen/log-growth proof gives actual raw-copy dyadic count <=864(n+2)2^n, without an unspecified constant. Thus fixed-packet signed cutoff error is at most 6912 a exp(a)||h'||^2(2N+6)2^-N. New theta/count arithmetic is analytic, not Lean-certified; no source/workflow changes. The next concrete input is complete certified finite actual zero data and rigorous sample/gradient evaluation for a fixed lawful packet. No actual off-line orbit, signed prefix, negative certificate or global positivity is produced. Retained source/null attachment or fresh WD-T38 remains independent; FULL TRANSPORT CLOSED is open; SOURCE stays off the critical path.
