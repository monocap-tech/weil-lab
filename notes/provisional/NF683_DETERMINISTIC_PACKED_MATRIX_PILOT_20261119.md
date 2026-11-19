# NF683 — deterministic packed integer matrix-product pilot

## Recovered actual kernel results

- NF678 mass/Dy replay on NF680 head, run 44540496957 job 135617199047: SUCCESS, complete strict audit of 1,216 literal and aggregate declarations, including all 242 original column/row masses, Dy, shared scalar numerators, global total and w binding. The generic mass projection also passed. Global full input projection and other product gates remain separate.
- NF681 repaired physical Gram/Schur audit, run 44548002861 job 135643723260: SUCCESS, genuine source-bound strict whitelist of all 42 targets. The full original physical Gram and cofinite Schur nonnegativity are now supported by a complete audit job, not just module-scope prints. This does not assert signed Weil positivity or NF672 strict positivity.
- NF681 matrix frontier, run 44548003290: shards 0–60 and 61–120 SUCCESS, 242 of 484 actual local product coordinates independently audited; remaining two shards still in progress at inspection.
- NF682 run 44549764213: emitter SUCCESS. Generic maximum-degree coverage/transport and actual source representative map domination gate compiled with only standard axioms (jobs 135653861788 and 135653861835). These jobs later received runner shutdown (exit 143) before the literal group audit finished. Other shards still active/queued. No complete original metadata coverage is asserted.

## Exact packing architecture

For integer vectors, write P_B(v)=sum_j v_j B^j. If |u_j-v_j|<B at every digit and P_B(u)=P_B(v), then u=v. Proof: first digit difference has absolute value < B and equals minus B times the packed tail. A nonzero integer tail makes its absolute value >=B; contradiction. Induct on the exact finite width. This is deterministic bounded encoding, not a modular hash or probabilistic Freivalds test.

Linearity yields P_B(j ↦ sum_k x_k Y_kj) = sum_k x_k P_B(Y_k). If sum_k |x_k|≤X, |Y_kj|≤M and |z_j|≤Z, then |sum_k x_k Y_kj-z_j|≤XM+Z. Choose B>XM+Z. Thus one exact packed integer dot equality and independent magnitude bounds imply every local product coordinate. The bound does not assume any actual product identity.

The new generic Lean source proposes the exact signed-digit uniqueness, linearity, uniform bound and coordinate recovery theorems. All are compiler pending.

## Actual source pilot

SHA-pin retained NF681 original frontier proposal ZIP artifact 14541229354 (SHA256 13c2c0e296633ab5368b6e1be09c4e9b69d527001e0f3969ffc2f0af0c611ef5). Authenticate Common.lean and first four original column files against the original manifest. Copy only the literal declarations (no prior direct product proof). Use original H row 0 and cached HD column 0 as the two length-242 vectors, and the first four genuine original D columns as the common operand block. The target is 4 HD row-zero and 4 A column-zero identities (eight coordinate identities), with A using commutativity of integer multiplication in the reverse order. The full cache HD column still needs its own authentic matrix-product attachment.

Compute X,M,Z,B externally as untrusted proposals, independently verify original input bounds and packed equalities in Lean by decide +kernel, and conclude the four coordinates by the generic theorem. Each base is a power of two strictly larger than the actual uniform error bound. The matched direct proof uses identical operands/targets. Record separate build elapsed, CPU and peak RSS measurements for direct, bounds, packed cases, and strict standard-axiom audit of all generic and literal proof declarations. Timing includes Lake/build overhead and will not establish a universal or asymptotic speedup. Long integers and larger packed multiplications can eliminate any savings: stop using packing if measurements disfavor it.

This is a pilot of an alternative exact certificate architecture, not a new full 87,967-coordinate proof or a guaranteed faster algorithm. Full global matrix projection, complete analytic moment bank, actual H/V entry and metadata coverage/shape, complete hcache/hpay attachment, unconditional Phase III signed-carrier closure, global signed Weil positivity and RH remain open.
