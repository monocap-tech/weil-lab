# NF660 — verified NF659 closure; generic original-Gram diagonal-dominance bridge

## Verified prior stages

- NF659 workflow run **44430374282**, job **135245914796**, **SUCCESS** throughout, including the generic congruence interval theorem, the off-diagonal energy/row exchange lemmas, all **225 exact integer transformed centers**, all **225 exact integer transformed radii**, all 15 integer margin gates, the exact integer coercivity gate, and an explicit standard axiom audit.
- NF658 corrected run **44427400456**, job **135241499793**, passed all mathematical and computational build stages: 120 source entry containments, both transformed pilot centers/radii, and generic cross-term bounds. It failed **only** at the final audit script, because literal `\\n` sequences were embedded in two `import` and `#print` source lines. This is a YAML here-document formatting defect, not a Lean theorem failure. The earlier NF658 run **44426966066** had an obsolete mis-transcribed pilot; the corrected pilot passed in 44427400456.

## New proposed Lean work (compiler pending)

`ActualZetaOriginalPhysicalGramDominanceTransfer.lean` develops the reusable mathematical step:

1. For a **symmetric actual real matrix**, bound its quadratic energy below by the sum of actual diagonal entries less the absolute off-diagonal row payments, using the already verified NF659 nonnegative pair energy and row/column payment exchange.
2. From a uniform Gershgorin row margin, deduce a concrete quadratic lower bound.
3. Transfer a computed *center-minus-radius* margin to the **actual** real entries using the hypotheses `|a_ij-c_ij|≤r_ij` and triangle inequalities.
4. Compose these into an interval-coercivity theorem, with **no numerical assumptions and no new axioms**. The CI build must still accept these proofs.

## Remaining physical attachment

The generic result must then be specialized to
`H_I(p,q) = neutralNF606PhysicalH (source p) (source q)`,
where the source enumeration is the original fourteen oscillators plus pole index 241, with `B = K H_I Kᵀ`.
The accepted NF658 source bounds and NF659 congruence interval theorem, together with all 450 source-derived integer identities, must establish the actual 225 real transformed entry bounds. The exact 15 row margins then imply
`yᵀBy ≥ (min_margin/10^192)‖y‖²`.

The witness K is integer scaled by `10^64`, so the physical conclusion requires the actual change of variables `x=Kᵀy/10^64`, an explicit proof of K's triangular invertibility, a Frobenius norm inequality, and the certified integer gate `min_margin * 10^60 > 10^64 * K_norm_squared`.

**The original 15-source physical coercivity theorem is still OPEN until that specialization and basis change pass Lean.** The complete 242-source system, global Weil positivity and RH remain OPEN. This PR is a draft against NF659, not main.
