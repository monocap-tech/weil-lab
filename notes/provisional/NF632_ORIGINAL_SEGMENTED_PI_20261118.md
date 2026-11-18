# NF632 — segmented high-precision shared Machin computation

Status: new proof candidates and independent exact arithmetic check; CI pending.

## CI recovery

NF621 original matrix-derived payment job 134968354605 and NF631 widened payment run 44359078922 remained queued at inspection. No new payment acceptance. NF628 closure job 134959216515 reported an additional integer-center theorem failure at line 140: unfolding the payment record during simp masks c.A_eq. Use an explicit change for the y coordinate and rewrite c.A_eq without unfolding the A projection. Metadata lexer failures were addressed already in NF631.

## Computational pivot

Two previous concrete high-precision moment trials were interrupted before successful kernel truth. All keys use one expensive shared Machin computation (two 2000-term arctan sums at Q=10^2600). Do not repeat it independently in every key. The exact reference identity is now candidate-proved by segmenting the same rounded terms into prefix chunks of at most 32. Joining uses exact ball-addition equalities, not a fresh reduction of the entire atan sum. The final pi equality directly transports the accepted NF616 analytic containment theorem.

Independent exact BigInt replay in-session (not the committed Python emitter) computed both signed floor sums using incremental powers and separately using direct powers; agreement PASS. Atan rounding radii are 1995 and 2000 units; after the +1 tail fees and directed multiply rounding, pi radius is 39942/10^2600. The 2601-digit scaled integer begins 3141592653589793238462643383279502884197169399375105820974944592307816 and ends 30861792868092087476091782481628. There are 126 segments total at chunk length 32.

New emitter supports complete prefix chain and final pi equality, and a bounded early/late actual segment trial for both denominators. Automatic CI compiles only four genuine segments and emits the full untrusted proposal set; full kernel trial is manual. No claim that this fully resolves computational cost; rational exponent/floor arithmetic may remain a bottleneck. Actual Lean equality to the literal pi receipt and use in endpoint bank checks are open.

No main merge, no full numerical custody or global Weil/RH promotion.
