# NF661 — actual original physical 15-source target and quantitative basis transfer

## Recovered runner truth

- NF659 run **44430374282**: **SUCCESS** for all 450 transformed integer identities, generic two-index interval congruence, diagonal-pair nonnegativity, and standard axiom audit.
- NF660 initial run **44433932382**, job **135257932201**: **FAIL** in new generic finite dominance module, with three precise Lean elaboration failures: diagonal multiplication parenthesization at line 70, an `abs` ring rewrite on the wrong expression at line 149, and incorrect orientation of `add_le_add_right` at line 151. Its failed compile printed `sorryAx` because of those unfinished proof goals; therefore **NO Lean pass may be claimed**.
- NF661 repairs all three observed elaboration errors on its own branch; fresh verification is pending.
- NF658 rerun **44427400456** built original entry widenings, all corrected transformed pilots, and analytic cross-term inequalities, but the separate audit script failed on literal `\\n` sequences in the generated Lean command. That workflow was repaired and resubmitted as **44434056814**; do not claim the repaired audit passed until its run reports success.

## New physical system construction

The new module `ActualZetaOriginalPhysicalGramCoercivityClosure.lean` defines:
- `neutralNF661Source (i : Fin 15) : Fin 242`: fourteen actual oscillator source indices **0 through 13**, plus original pole index **241**.
- `neutralNF661PhysicalH`: the submatrix of the authentic unweighted original physical integral matrix `neutralNF606PhysicalH`, with re-used original symmetry theorem.
- `neutralNF661Quadratic`, `neutralNF661SqNorm`: real finite quadratic and Euclidean-square norm expressions.

The proposed general coercivity transfer theorem concludes
`target * ||x||² ≤ xᵀ H x`
when supplied:
1. (m ||y||² ≤ yᵀ B y), for all real (y);
2. exact congruence identity (yᵀ B y = (T y)ᵀ H (T y));
3. quantitative norm (||T y||² ≤ N ||y||²);
4. surjectivity of the basis map (T);
5. nonnegative target and (target*N ≤ m).

This closure theorem is deliberately **source-independent** and **assumption-transparent**; it does **not** assert any unverified original matrix positivity. Fresh Lean build and axiom audit are pending.

## Numerical scaling obligation (exact)

Let `S=10^64`, `k = K_scaled` (integer), `C=H_center_scaled` (integer), `E=H_radius_scaled` (integer).
Then
`|H_pq-C_pq/S|≤E_pq/S`
and (B=(k/S)H(k/S)^T).

The integer transformed centers (T_{ij}=sum_{p,q}k_{ip}k_{jq}C_{pq}) and error radii (U_{ij}=sum_{p,q}|k_{ip}k_{jq}|E_{pq}) imply
`|B_ij-T_ij/S^3| ≤ U_ij/S^3`.

The integer minimal transformed row margin `m_int` proves (yᵀ B y≥(m_int/S^3)||y||²).

Take the basis map (x=(k/S)^T y), which is surjective because (k) is triangular with all diagonal entries (S\ne0). With integer Frobenius bound `kn = sum k_ij^2`,
`||x||²≤(kn/S²)||y||²`.
The previously certified gate `m_int * 10^60 > S * kn` is exactly sufficient for (xᵀH x≥10^{-60}||x||²).

## Still open

The NF658 lower-triangular source balls must be converted into 225 real physical (H_I) bounds (including symmetric upper entries). The 450 NF659 integer arithmetic identities must be attached through the accepted double-sum interval theorem to actual (B), with proof of interval row margins. The quantitative (k/S) norm and inverse/surjective map must be made explicit in Lean. **Do not claim the original 15-source physical (10^{-60}) coercivity theorem has closed.**

Complete 242-generator physical certification, global Weil positivity, and RH remain OPEN. All changes are on a draft branch based on NF660, not main.
