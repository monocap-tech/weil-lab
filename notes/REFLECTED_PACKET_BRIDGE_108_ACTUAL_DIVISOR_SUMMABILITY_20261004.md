# RPB-108 — actual divisor summability (2026-10-04 UTC)

Parent research head: `8484eb637658018265937901869fbc8af64f7b9f`.

## Definitions before use

The actual divisor coordinate records an actual open-strip zeta zero and
one of its analytic multiplicity copies. The unit band numbered n contains
exactly coordinates with floor(abs(Im rho))=n, so its absolute heights lie
in [n,n+1). Every actual coordinate lies in a unique band.

The quartic height weight is w(q)=1/(1+abs(Im rho(q)))^4.
It counts every multiplicity copy, including critical-line copies.
It is a summability weight, not a replacement for the logarithmic-domain
norm or a spectral operator-domain witness.

## Proof

Each band is finite because it is contained in the already-certified
height window n+1. The actual cumulative logarithmic bound, followed by
log(n+3)<=n+3, gives band cardinality <=A(n+1)^2 for one fixed A>0.
This is a coarse bound, not the sharp local O(log n) theorem.

On the nth band, w(q)<=1/(n+1)^4. Its finite total is therefore
at most A/(n+1)^2. The shifted p-series converges. The nonnegative
partition theorem then gives unconditional summability of w over the
full actual multiplicity divisor, without choosing an enumeration.

Any complex samples with norm bounded by M*w consequently form an
absolutely convergent family. The sample-decay hypothesis is explicit;
the unconditional new witness is the actual full-divisor summable weight.

## Status and next cursor

Exact candidate `57cedf4573225a2eb2d993ca7a4b93ff02dd926b` passed [run 37166971973](https://github.com/monocap-tech/weil-lab/actions/runs/37166971973), job `111331807032`. The isolated module and full `lake build WeilDefect` passed (9,009 and 9,053 jobs). All eight theorem audits report only `[propext, Classical.choice, Quot.sound]`; the unfinished/project-axiom gate passed. Certified source and imports are promoted separately from the validation workflow and dependency manifest.
Next: attach concrete window-test decay and mixed sample/form convergence.
Sharp local unit-height logarithmic counts and bounded sampling on the
entire canonical logarithmic form domain remain open. The coarse weight
does not establish either of these claims.

WD-T38 source/null attachment, enlarged central cancellation, background
completion and F-4 remain open. Earlier residue is retained. SOURCE stays
off the critical path; threshold remains closed; spectral L2 is unproved
and unassumed. RH remains open.
