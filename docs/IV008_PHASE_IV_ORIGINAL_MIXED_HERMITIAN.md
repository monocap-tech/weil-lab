# Weil-Lab — IV008
## Actual original signed mixed Weil Hermitian symmetry and real finite quadratic energies

**Phase IV canonical stage:** IV008, continuing IV007 PR #767 on its own stacked branch.
**New Lean acceptance:** PENDING. Seven new original-source proof candidates and three independent original/upstream axiom receipts must all compile and audit before the kernel result is called PASS.
**Not established:** an all-support Weil positivity theorem, the external Weil criterion, or RH.

## 1. Why this step precedes full physical Schwartz polarization

IV007 defined the complete, literal original mixed zeta arithmetic entry

```text
M_a(i,j) = Zeta23.EF.literatureRHS
  (neutralWindowCorrelation a (s_i.toLp 2 volume) (s_j.toLp 2 volume)).
```

It also defined the exact full-multiplicity divisor-side entry

```text
D_a(i,j) = Σ'_q conj (neutralWindowEvaluation a (conj z_q) s_i)
                    * neutralWindowEvaluation a z_q s_j,
```

and the finite complex energy

```text
Q_a(s,u) = Σ_i Σ_j conj(u_i) M_a(i,j) u_j.
```

IV008 now aims to prove **from the authentic original arithmetic source**, not as an arbitrary assumption on a matrix, that the mixed EF really is Hermitian for EVERY arbitrary finite family of complex Schwartz tests supported in one physical window. This gives the necessary real-valued quadratic structure before proceeding to a physical Schwartz-sum polarization theorem.

## 2. Seven actual-source proof candidates

**(1) Schwartz support → compact support.** A complex Schwartz test supported in `[-a,a]` has `HasCompactSupport`, exactly what the original EF needs.

**(2) Authentic original EF dictionary for each mixed entry.** Use the genuine NF533/NF534 `neutralActualZetaWindowCorrelation_literature_of_ae_smoothSecond`, with IV006's a.e. supported representative and the original two-argument `neutralWindowCorrelation`, to prove

```text
D_a(i,j) = M_a(i,j)
```

for ALL index pairs in an arbitrary finite supported family. Prime, archimedean and pole terms remain in `Zeta23.EF.literatureRHS`. No arithmetic term is dropped or identified with a proxy.

**(3) Actual full-divisor Hermitian symmetry.** Reindex the *same* all-multiplicity zeta zero-side series using the pre-existing genuine divisor conjugation involution `neutralActualZetaDivisorPairEquiv`, with `neutralActualZetaDivisorOrdinate_pair`. The proposed theorem is

```text
conj (D_a(i,j)) = D_a(j,i).
```

The proof follows the already established original constructed-Green-source involution, but now applies to arbitrary complex Schwartz family inputs; no reality or oddness symmetry is invoked.

**(4) Literal arithmetic Weil Hermitian attachment.** Combine (2) and (3):

```text
conj (M_a(i,j)) = M_a(j,i).
```

This concerns the ACTUAL original two-argument zeta Weil EF, not an abstract Hermitian model.

**(5) Real diagonal.** `Im M_a(i,i)=0`, without claiming its sign.

**(6) Real finite coefficient energy.** For arbitrary `u : Fin n → ℂ`, finite-sum index interchange plus the original Hermitian identity gives

```text
Im Q_a(s,u)=0.
```

**(7) Exact real-axis identification.** `Q_a(s,u) = (Re Q_a(s,u) : ℂ)` for every supported family and complex coefficient vector.

None of these declares that the real number is ≥0.

## 3. Verified dependencies versus pending steps

**Accepted genuine original source anchors available in the repository:**
- NF533/NF534: literal mixed zeta EF for C² original window correlations via the actual all-multiplicity divisor.
- Original all-divisor partner-conjugation involution and its ordinate equality.
- NF573: supported Schwartz L² representative and the actual window raw transform.

**Pending formal proof chain:**
- IV006 exact original two-window naturality: PR #766 (kernel pending).
- IV007 exact finite-family mixed transport: PR #767 (kernel pending).
- IV008 original arbitrary-supported-family Hermitian and finite energy reality: NEW, kernel pending.

A green source preflight is not a Lean proof. We require direct compilation and 10 source-specific `#print axioms` receipts for seven new declarations plus the three actual-source/upstream anchors. The audit forbids nonstandard axioms and `sorryAx`; it binds dependency/source SHA-256 values to the actual compiled `.olean` artifact.

Files:
- `WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalMixedHermitian.lean`
- `scripts/iv008_original_mixed_hermitian_audit.py`
- `.github/workflows/iv008-original-mixed-hermitian-source.yml`
- `docs/IV008_PHASE_IV_ORIGINAL_MIXED_HERMITIAN.md`

## 4. The exact limitation and next IV009 gate

The original **zero-side mixed entry** is Hermitian by the authentic divisor involution, and its supported-Schwartz `Zeta23.EF.literatureRHS` representation is therefore Hermitian. This remains logically distinct from showing that its finite mixed coefficient sum equals the *diagonal* signed Weil expression of the physical Schwartz sum:

```text
Σ_i Σ_j conj(u_i) M_a(s_i,s_j) u_j
   ?= Zeta23.EF.literatureRHS
          (neutralWindowCorrelation a
             ((Σ_i u_i • s_i).toLp 2 volume)
             ((Σ_j u_j • s_j).toLp 2 volume)).
```

This next identity requires exactly attached sesquilinearity in the ORIGINAL `Schwartz → L² → window → correlation → EF` chain, or an equivalent proof from the original full-divisor series with justified finite/t-sum interchange. Do not infer it from Hermitian symmetry alone.

Only after that bridge may the frozen-collar NF600/NF738 coercivity be transferred to an original mixed Gram matrix built from an arbitrary family *inside that same collar*. Neither the bridge nor that local result would prove positivity for genuinely enlarged supports, global Weil positivity, or RH.

**Milestone:** authenticate genuine mixed Weil Hermitian symmetry and real-valued finite energies; no positivity claim.
