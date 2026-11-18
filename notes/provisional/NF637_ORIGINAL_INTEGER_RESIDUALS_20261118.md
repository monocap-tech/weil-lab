# NF637 — fixed-scale integer moment residual fees

Status: exact independent replay of genuine source-key moment tables PASS; generic reference attachment and literal kernel tests pending.

NF636 #667 latest on inspection. The complete NF623 original moment-derived transformed payment result remains external PASS (242/242); NF631 widened payment job 134995143316 still queued. NF631 metadata focus 134995143198 has moved to in_progress. NF632–636 newest compiler and concrete kernel trials otherwise queued. No new Lean acceptance reported.

## Reduction

Use Q=10^2600. For integer-coordinate residual rectangle A let U(A)=|Re.mid|+Re.rad+|Im.mid|+Im.rad. For denominator lower bound delta=d/e with d,e>0, and proposed current radius R and preceding radius Rprev (integer Q units), the original rational comparison is exactly
  e*(U(A)+n*Rprev) <= d*R.
At degree zero the preceding fee is zero. NF637 checks the same directed-rounded rectangular products via NF636, retaining all reference rounding fees. The proof candidates transport the integer comparison to NF615RectBelow using positive-denominator clearing. The local reference theorem expressly requires exact point and natural-scalar rectangle identities; cache/boundary identities and original row/table composition remain to be attached. No new analytic approximation.

Independent BigInt replay constructed the complete three source-key tables at the original precision from the same source parameters. Pole (1,0): 1 row, maximum radius 86431/Q. Oscillator (0,37/32): 27 rows, maximum 3722396298337/Q. Mixed (1/2,37/64): 14 rows, maximum 2680143396/Q. All 42 exact integer fee checks passed; replacing each current radius by zero failed all 42. This was a separately implemented in-session replay, not a check of the retained shard bytes or a Lean proof.

Committed emitter uses audited eight shards, checks exact equality of the complete three tables to the existing numerical producer, and emits all 42 local integer residual gates and 42 zero-radius negative tests. CI checks source hashes and schedules bounded kernel compilation. The Python emitter and new Lean files were not run in-session. Machin integer-only optimization remains deferred; priority is the full residual comparison and its reference attachment. No main merge, no unconditional physical solve, no global Weil positivity/RH promotion.
