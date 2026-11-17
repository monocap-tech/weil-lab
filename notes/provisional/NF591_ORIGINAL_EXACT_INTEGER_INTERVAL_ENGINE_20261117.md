# NF591 — exact integer-only original full-box interval reconstruction

Stacked on NF590 #621. New Lean proofs and the new CI replay are pending. The exact BigInt replay was executed during NF591 and passed.

## Verified new receipts

- NF590 run 44130300029 job 134205209760 completed SUCCESS: the ungrouped Arb evaluation of all 374 primitive contributions (including the two-exponential genuine sinh pole) satisfies all 400 historical normalized ceilings. This is independent of the grouped NF587 calculation.
- NF589 run 44128563458 job 134199007847 completed with the **literal uncorrected odd seed graph** build step SUCCESS. The actual graph convergence theorem conditional on the half-carrier L1 and strip premises is now accepted. Quantitative twisted panels and terminal C1 attachment failed. The sole panel diagnostic was the last division/multiplication association; NF591 gives the division bound an explicit type and commutes only the outer product.
- NF590 run 44130300029 job 134205211292 failed: generic jet recurrence had three reserved lambda identifier lexer errors and one scalar-series commutativity mismatch; frozen-source regularity had one recursion failure at the selected dyad array size proof (NOT node equality); normalized tail had a doc-comment/set_option ordering parser error. NF591 repairs those exact diagnostics. No new compiler acceptance claimed for repairs.

## Independent exact arithmetic replay (no Arb)

Implemented and executed scripts/local_replay/nf591_exact_fixedpoint_original_jets.js on the actual frozen NF407 coefficient JSON. It uses only BigInt, exact rational input conversion, integer addition/multiplication/division with directed widening. Q=10^250. A ball (m,r) denotes |x-m/Q|<=r/Q. Multiplication uses center floor(m*n/Q), radius ceil((|m|s+|n|r+rs)/Q)+1. Division by positive d uses floor(m/d), ceil(r/d)+1. Complex arithmetic uses separate real and imaginary enclosures. Original dyadic midpoint/radius box is converted outward exactly.

Pi is computed from Machin's identity 16 atan(1/5)-4 atan(1/239) with 200 terms of each finite rational arctan polynomial and an outward remainder of one unit at scale Q for each arctan. The exact rational comparison 1/(p^(401)*401)<=1/Q holds for both p. The phase f B is reduced exactly modulo integer turns to [-1/2,1/2); the reduced argument is divided by four, exp is evaluated in the unit disc with 220 terms and a one-unit remainder (2/220!<=1/Q), and squared twice. The genuine pole uses exp(±11/20) and both actual exponential jet recurrences. The frequency recurrence itself uses full unreduced frequency. All 374 primitive contributions use their actual full coefficient boxes; 273 distinct oscillator computations are cached but the coefficients are not grouped. Every radius propagation is outward.

The BigInt run passed ALL 400 ceilings, and every upward-rounded coefficient ceiling at scale 10^40 is **identical** to NF494/NF587/NF588's. The endpoint upper bound also passes -1e-11. Committed 150376-byte exact receipt with all 400 scaled integer endpoints and ceilings. Independent Node CI verifies the frozen source SHA256 and byte-identical receipt. The live replay used bytes fetched from the previously hash-audited original source; SHA verification is included in the committed standalone script, not asserted to have been newly executed during this isolate run.

## Lean formalization

New candidates for exact rational ball operations (addition, negation, multiplication, positive division, widening, absolute bound), complex rectangle operations, and floor/ceil rounding soundness. New analytic remainder candidates: |exp(z)-sum_{n<N}z^n/n!|<=2/N! for |z|<=1, N>=1, via factorial growth and geometric tail summation; arctan finite polynomial remainder <=x^(2N+1)/(2N+1) for x>=0 via integrating finite geometric identity; Machin approximation. This separates the two small transcendental inputs from all later rational arithmetic.

The exact replay is independent of Arb but is NOT a Lean proof term. The source-specific fixedpoint recurrence/checker must still be implemented in Lean and connected to the sound arithmetic and analytic phase/pole enclosures; periodic phase reduction and all 400 inequality receipts must be checked against the actual canonical jet definition. Full-box exact original solve custody, disc assembly, terminal corrected graph and signed Weil coercivity remain open. No local Lean build, no main merge. RH OPEN.
