# RPB-108 — logarithmic actual-divisor growth (2026-10-04 UTC)

Recovery anchor: research/reflected-packet-bridge at
`0a2bc0f0ba3cde964a0d622965f7318113f92110`.
Parent analytic result: the actual reflected Mellin identity, factorial
entire/circle envelope, and multiplicity-weighted Jensen count bound.
Validation continues on draft PR #35, validation/rpb108-mellin-growth.

## Definitions and claim

The actual height-window divisor repeats each actual nontrivial zero
according to its vanishing order. Its cardinality is the cumulative
multiplicity count. The established majorant is
A_n = n(n+1) C n! q^(-n) exp(-q)/q + 1, q=p/2>0.

The scalar logarithmic estimate is log(A_n) <= K(n+1)log(n+2).
Choosing n=ceil(2(|T|+2)) gives
N_div(T) <= K'(|T|+1)log(|T|+2).
The constants are obtained from the positive actual theta-kernel constants.
No zero-count premise, RH premise, or spectral operator-domain membership
is introduced.

Proof: bound n! by (n+1)^n; choose
B=max(1,C exp(-q)/q), b=max(1,1/q).
Then A_n <= (B+1)(n+1)^(n+2)b^n.
Take logarithms, bound the constant and linear terms using log(n+2)>=log2,
and use n+2<=2(n+1). For the natural ceiling order,
n+1<=6(|T|+1), n+2<=7(|T|+2).
The latter yields log(n+2)<=(1+log7/log2)log(|T|+2).

## Residue custody

The earlier local checkout at 542d00a contains staged and untracked
native/logarithmic source-domain and actual-divisor modules. It is older
than the promoted research head and was left intact; its dirty state is
not a new certified frontier. The four analytic continuation files
recovered from the later scratch directory agree with the promoted
analytic stage.

Still open: local unit-height multiplicity estimates and bounded
logarithmic-domain sampling; infinite full-divisor sampling and full
zero-side to Weil-form transport; WD-T38 source/null witness attachment,
enlarged central cancellation, background completion, and F-4.
Cumulative O(T log T) alone does not prove local O(log T) density,
sampling conditioning, or the missing null witness.
SOURCE traversal is off the critical path; threshold remains closed;
spectral L2 membership remains unproved and unassumed. RH remains open.

## Validation

Pending exact-candidate Lean build, full-project build, and axiom audit.
No new theorem is certified until those checks pass.

## Next cursor

After certification: local multiplicity/sampling estimate, with the global
cumulative bound available for sufficiently decaying full-divisor tails.
