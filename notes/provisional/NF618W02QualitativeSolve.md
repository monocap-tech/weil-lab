# W02-NF-04 — Qualitative intrinsic original physical solve without the numerical bank

Authority: continuation amendment canonical-return@d4e482f2f616112dca11f6d8fd803a3dffb5a80c. Parent 2eb85b38ccd811b9603e53cb019bc09c938ab051. Named Batch25–39 and universal-dispatch holds retained. Mathematical head Batch24R1 unchanged.

## Mathematical result (deductive argument; native candidate not compiled)
Let J_i be the unchanged 242 real generators nf545OriginalSelectedRealGenerator, I=[-11/10,11/10], H=neutralNF606PhysicalH. For any real coefficient z≠0, define F_z(t)=sum_i z_i J_i(t). The original global independence and collar separation theorem neutralNF569OriginalCollarSeparatesJ242 gives a nonzero observation of F_z within the fixed positive collar (2197/2000,2199/2000) inside I, by exact complexification. The J_i are analytic and hence continuous. The exact continuous-source Gram square identity implies z^T H z=integral_I F_z(t)^2 dt>0: continuity supplies an interval of positive measure on which the square is strictly positive. No explicit lower eigenvalue, numerical enclosure or reference frame is needed.

If Hx=Hy, write z=x-y. Then Hz=0, so z^T H z=0. Strict positivity forces z=0. Thus the real 242-dimensional endomorphism H is injective, hence surjective. Every RHS b has a unique real solution; in particular the actual RHS neutralNF612RHS=Vw, with V the literal full-interval mixed matrix and w the frozen physical weight vector. This is an existence/uniqueness statement about the exact intrinsic system, not proof that its unique solution lies in the historical frozen box.

Projection interpretation: let q=sum_j w_j C_j (the actual four critical functions) and p_a=sum_i a_i J_i. The equation Ha=Vw says integral_I J_i(p_a-q)=0 for each i. Thus p_a is the orthogonal projection of q onto the real span of the original 242 generators under unweighted L2 on I. This is a mathematical interpretation, not a new Lean declaration; it is not the signed Weil form or the collar-weighted canonical correction. The original source has separate critical coefficients, so this does not assert that the full historical NF407 source has vanishing selected moments.

## Why this reduces the active dependency
Historical NF671/NF672 source bundled the qualitative full H strict theorem with the numerical 15+227 Riesz/Schur reconstruction. NF676's full chain previously stopped at continuity; NF678 records a repair. We do not consume or claim the current status of those bundled generated endpoints. The direct route reuses only original analytic separation, generic integral-square/strict-witness arguments and elementary finite-dimensional row action. NF671 generic job 135364375635 at 2bb6c1553f31a87de4c70194dbc3846c5fce5129 printed standard axioms for the integral-square identity; containing run 44466173424 failed, so do not promote full NF671 from that job. Current-source dependencies are pinned below; not all transitive named audits were independently repeated. The existing NF614 audit is documented in W02-NF-03.

| Objective | Existing full numerical receiver | Direct route |
|---|---|---|
| Exact H strict positivity | Bundled with generated physical Schur chain | Analytic independence and interval square |
| Exact Ha=Vw existence/uniqueness | Near-identity and numeric entry/payment gates | Strict H and finite dimensionality |
| Historical frozen-box containment | Required | Still required; not supplied |
| Global signed Weil positivity | Not proved | Not proved |

The qualitative argument uses zero NF618 numerical moment slots. This does not establish a computable positive lower eigenvalue, residual tolerance, numerical source identity, box membership, historical signed action or RH.

## Native verification candidate
NF618W02QualitativeSolveCandidate.lean.txt contains eight proposed Lean declarations and named axiom prints. Extracted source witness/continuity from NF671/672 (without generated imports), new generic strict row-action injectivity, then bijectivity and exact RHS uniqueness. This is stored as a nonactivated text candidate, not an admitted module. To verify: place as a .lean file in a pinned checkout, build the four listed imports, run lake env lean on it, and require success and an exact named audit of all eight declarations with only propext, Classical.choice, Quot.sound (or no axioms). No sorry or untrusted numeric premise. Source reviewed, not executed; local Lean/lake unavailable and the connector has no scoped workflow_dispatch action. Existing PR/push triggers are not used for speculative broad CI. No assertion of native acceptance. Only a new native PASS may promote these declarations.

## Remaining quantitative target
For the actual unique solution a*, establish neutralNF587SourceInFrozenBox a* neutralNF604OriginalCritical. The existing residual/payment route remains sufficient but its proof of existence no longer needs to be an active objective. A narrower possible target is an explicit bound on the inverse action and a directly enclosed combined physical residual Vw-Ha0 for an exact proposed center a0; this is a proposal, not a verified alternative receipt. Invertibility by itself supplies no explicit norm estimate. Do not expand the held bank for counts. No verified cross-lineage demand, no binary producer closure or hold release.

## Immutable input blobs at parent
- WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGramStrictWitness.lean bbd7d6c68e54730e885dd80d0479c5f2b155b1cb
- WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGramIntegralSquare.lean a148ba7bc736644137bdfe623188cac525383aac
- WeilDefect/Arithmetic/ActualZetaOriginalJ242CanonicalGramPositivity.lean 57326dabdae0c8509531aa1a91d5f5b0a8302a8f
- WeilDefect/Arithmetic/ActualZetaOriginalJ242AnalyticIdentity.lean e68bdbf0dd554942eb044032c7a648af46ecc188
- WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGramPositiveDefinite.lean dfbf7b14080b23c9c09cc392ae687919f9c85bca
- WeilDefect/Arithmetic/ActualZetaOriginalPhysicalSystemEquiv.lean 112f1ee93ab54104581b6a73df6efda9dd98fb19
- WeilDefect/Arithmetic/ActualZetaOriginalPhysicalSolveResidual.lean 2cf06688dc7e63bbb0c797102260559884325855
- WeilDefect/Arithmetic/ActualZetaOriginalSolveResidualCustody.lean ea037cfc025670efe53b1379af1197510f7cbabf
- WeilDefect/Arithmetic/ActualZetaOriginalJ242SourceFunctions.lean 53935773feb3bba3c10e699cd8f862f9dd590b76
- WeilDefect/Generated/NF671/OriginalPhysicalFullGramPSD.lean 9c182ab52e5800ed1a63bd119603328a1c2bcf53
- WeilDefect/Generated/NF672/OriginalPhysicalFullGramStrict.lean ff3417e30553a3b250cc323c22cbec4feff9eb95
- lean-toolchain 664e12dc06fe1ec82414cccb8e8f8e34d33d9f3f
- lakefile.toml e567c529fc39eff8a175b3361a2831763e5dcc2c

Execution: deductive mathematical analysis and staged Lean source. Mathematical: proof argument, native candidate pending. Custody: text deliverables committed on existing branch; raw archive custody unchanged. Adoption: not native admitted; no dependent activation.
