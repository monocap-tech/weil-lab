# SZ kernel edge — pre-GERM-65 refold and integrated handoff

**Date:** 2026-09-27 (America/Los_Angeles)  
**Destination:** `monocap-tech/weil-lab`, branch `sz-cross-collar`  
**Operation:** source reconciliation and research handoff only  
**Standing:** UNRATIFIED RESEARCH INTEGRATION / NO NEW MATHEMATICAL PASS  
**Canonical theorem cursor:** `SZ-CROSS-COLLAR-3`, unchanged  
**Last completed experimental pass:** `SZ-KERNEL-EDGE-GERM-64`  
**Next mathematical target:** `SZ-KERNEL-EDGE-GERM-65 / MIXED-RETURN CONE TRANSFER` — NOT EXECUTED HERE  
**Public promotion:** forbidden

## 1. Refold decision and source custody

This record folds the parallel return-cocycle investigation through **RETURN-COCYCLE-5**, not merely its initial Chebyshev observation, into the entry package for GERM-65. It also carries forward the screw-family audit's valid representation algebra and explicit stop conditions. The imports retain their original hypotheses and unratified standing. Recording an import is not ratifying its mathematical dependencies. [GOV, RC0, RC1, RC3, RC4, RC5, SF]

The frozen source repositories and commits are:

| Alias | Repository and branch at inspection | Pinned commit |
| --- | --- | --- |
| LAB | `monocap-tech/weil-lab`, `sz-cross-collar` | `9d795ddad56d7d884276119343194ac51f7184d9` |
| RC | `monocap-tech/weil`, `research/sz-return-cocycle-0` | `307446bc46c07056fc32eb63f0e366face06ac76` |
| SF | `monocap-tech/weil`, `research/sz-screw-family-0` | `ee6adf776cd996731762a602a335a8bff5adc409` |

All file references below mean the named file at its pinned commit, not a moving branch tip. This is a selective source-level refold into the private lab, not a merge of either public research branch and not a publication operation.

### Source manifest

| ID | Pinned source | Role in this refold |
| --- | --- | --- |
| GOV | LAB:`notes/SZ_CROSS_COLLAR_RATIFICATION_20260926.md` | Ratified cursor and separation of residue, custody, and promotion |
| G63 | LAB:`notes/_recurrence63.md` | Existing five-template coverage through `e <= lambda_ret` |
| G64 | LAB:`notes/_recurrence64.md` | Partial-return geometry, full-cocycle threshold, and original GERM-65 target |
| G62V | LAB:`tools/sz_parity_first_return_audit.py` | Existing 124-variable assembler and coefficient audit helper |
| G63V | LAB:`tools/sz_parity_multikappa_audit.py` | Existing 124/186/248/310/372 assembler and coefficient audit helper |
| RC0 | RC:`notes/SZ_RETURN_COCYCLE_0_TRANSFER_GROUP_AUDIT_20260927.md` | Delay lattice, bulk compression, adjoint telescope, two-tap obstruction |
| RC1 | RC:`notes/SZ_RETURN_COCYCLE_1_PROJECTIVE_COMPRESSION_20260927.md` | Distinction between bulk steps and return attachments; proposed scattering interface |
| RC3 | RC:`notes/SZ_RETURN_COCYCLE_3_BLOCK_SYMBOL_EXTRACTION_20260927.md` | Exact double-tail Schur block and boundary constraint rows |
| RC4 | RC:`notes/SZ_RETURN_COCYCLE_4_BASE_ORBIT_ASSEMBLER_20260927.md` | Source-level 124 reconstruction, reflection sectors, affine compiler correction |
| RC4V | RC:`experiments/sz_return_cocycle_4_base_orbit_verify.py` | Companion symbolic/rational base verifier |
| RC5 | RC:`notes/SZ_RETURN_COCYCLE_5_FIRST_EXTRA_LAYER_20260927.md` | Source-level first extra layer, exact parity gauge, 186 certificate |
| RC5V | RC:`experiments/sz_return_cocycle_5_first_extra_layer_verify.py` | Companion affine-geometry and rational perturbation verifier |
| SF | SF:`notes/SZ_SCREW_FAMILY_REGROUP_AUDIT_20260927.md` | Same-form factorization, kernel-only rank, rejected intertwiner, trace/flux guards |

Verified blob identifiers for the executable sources are:

```text
G62V e19f99c2ba93928016bce9fd8bd19a5cdc495500
G63V 36598d5495433a708ed24297220b058cb5ea2ef8
RC4V 5ed42a069024b85022c5cd5b3381fc06dec7595b
RC5V 495cc9fd30379deec08f622a8e8164b4a17c813f
```

The source notes and relevant script interfaces were inspected for this refold. **The determinant programs were not rerun here.** Their results below are source-contained certificates or inherited residue statements, not newly issued certificates. No historical byte identity between the separate assemblers is asserted.

## 2. Preserve the latest experimental coverage

Use the constants and parameter convention from G63/G64:

```math
e=L-\log(16/3),\quad
h=\log(81/80),\quad k=\log(16/15),\quad
p=\log(10/9),\quad j=\log(9/8),
```

```math
\kappa=k-5h,\qquad
\lambda_{\rm ret}=h-\kappa=6h-k,\qquad
\tau=\lambda_{\rm ret}-4\kappa.
```

The recorded exact inequalities are `4 kappa < lambda_ret < 5 kappa` and `0 < tau < kappa`. G64, not the older parallel snapshot, supplies the working chamber architecture. [G63, G64]

| Parameter range | Geometry | Standing retained after refold |
| --- | --- | --- |
| `0 < e <= kappa` | Base finite parity system | GERM-62 residue; independently reconstructed by RC4 |
| `kappa < e <= lambda_ret` | Single-scale kappa chains; five templates including the base | GERM-63 residue coverage retained in full |
| `lambda_ret < e < h` | Partial irrational-return paths, finite for each fixed e | Open injectivity target; G64 supplies geometry only |
| `h <= e <= j` | Full irrational return graph occurs; further returns may be active | Open injectivity target; coefficient change at e=p remains to be respected |

GERM-63 records nonzero determinants for the 124, 186, 248, 310, and 372 templates for both external parities. RC4/RC5 add independent source-level structure on the base and first extra layer; they do not reduce this inherited coverage to their narrower domains. Conversely, their fresh certificates do not independently re-certify the 248/310/372 templates in this refold. [G63, RC4, RC5]

The retained experimental endpoint is therefore still

```math
0<L\le L_{\rm ret}
=\log\!\left(\frac{3^{24}}{2^{24}5^5}\right),
\qquad
K_c^{\rm ps}=\{0\}
```

in the regular-kernel scope recorded by G63. No new endpoint, no uniform-in-L lower bound, and no full-form-domain persistence exclusion are claimed by this operation. [G63, GOV]

## 3. Integrated imports and their exact scope

### 3.1 Bulk compression and adjoint data

For the retained P/J state `V=(X,S)^T`, RC0's gate-free matrix `M_0` has determinant one and trace `Theta`. Define `B(0)=I`. For integer `r >= 1`,

```math
\mathcal B(r)=M_0^r
=U_{r-1}(\Theta/2)M_0-U_{r-2}(\Theta/2)I,
\qquad U_{-1}=0,\quad U_0=1.
```

This is an exact algebraic compression **where the gate-free P/J recurrence has been established**. The integer r counts homogeneous h-steps, not kappa attachments or rotation returns. It is not legitimate to replace an entire `124+62n` constraint system by `M_0^n`. [RC0, RC1]

RC0 also supplies the general adjoint identity

```math
V_{n+1}=A_nV_n+b_n,\quad
\ell_n=\ell_{n+1}A_n
\ \Longrightarrow\ 
\ell_{n+1}V_{n+1}-\ell_nV_n=\ell_{n+1}b_n.
```

It does not require determinant one. However, the two post-p tap directions span the two-dimensional state space under the stated nonzero-tap hypotheses, so no nonzero constant covector annihilates both pointwise. A scheduler-dependent adjoint or telescoping mechanism remains a question, not an imported solution. [RC0]

### 3.2 Exact tail elimination and source-row interface

Adopt the coefficient dictionary

```math
\beta=\sqrt{2/3}\,\frac{\log3}{\log2},\quad
\gamma=\frac1{\sqrt2},\quad
\delta=\sqrt{2/5}\,\frac{\log5}{\log2},\quad
\mu=\beta\gamma.
```

Thus G63's `c` equals RC3-5's `mu`, and G63's `d0` equals RC4-5's `d=delta gamma`. RC3 proves `0 < mu < 1`, so the paired tail block

```math
\begin{pmatrix}1&-\varepsilon\mu\\-\varepsilon\mu&1\end{pmatrix}
```

has the strict Schur denominator `1-mu^2 > 0`. Its base-chamber source consequences include

```math
x(p+k+z)+\frac{\beta^2\gamma}{1-\mu^2}
\bigl[\mu x(z)+\varepsilon x(e-z)\bigr]=0,
```

```math
x(k+z)+\varepsilon\beta^2\gamma x(p+e-z)
+\frac{\delta}{\beta^2}x(p+k+z)=0.
```

Retain these rows in the **proved base scope `0<e<=kappa`, `0<z<e`**. In particular, the dead-strip substitution used to derive the second row must be rechecked before a wider use. These are exact constraints among scalar x-values; they are not yet an invertible two-port scattering map, and no identification of this x-state with the P/J state `(X,S)` is imported for free. [RC3]

### 3.3 Source-level base compiler and reflection reduction

RC4 gives a 31-site skeleton, its two kappa offsets, and the two reflected seed orientations: `31 x 2 x 2 = 124`. For

```math
Y_C=\begin{pmatrix}x(C+z)\\x(C+e-z)\end{pmatrix},\qquad
\mathsf S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
```

the source block rows on the base chamber are

```math
\begin{array}{ll}
A:&Y_C+\beta Y_{C+r}+\delta\gamma Y_{C+s}
-\varepsilon\delta\gamma\mathsf S Y_{k-C}=0,\\
B:&Y_C+\beta Y_{C+r}=0,\\
D:&Y_C=0,\\
T:&Y_C+\mu Y_{C-q}-\varepsilon\mu\mathsf S Y_{2q-C}=0,
\end{array}
```

where `q=log(4/3)`, `r=log(3/2)`, and `s=log(5/4)`. This is the source-level regression specification, not merely a target matrix dimension. Since all two-component blocks lie in `span{I,S}`, the base system splits into two 62-variable reflection sectors. Changing external parity swaps the sectors, and its full determinant is their product. RC4 contains exact rational sign enclosures for the two sector polynomials. [RC4, RC4V]

The compiler has **translations and reflections**. Carry forward RC4's additive correction to RC2: it is a finite affine Toeplitz-Hankel system, not an already-proved pure Laurent-symbol model. No doubling/reindexing theorem is silently inserted. [RC4, section 8]

### 3.4 First extra layer and parity gauge

RC5 treats `e=kappa+eta`, strictly `0<eta<kappa`. Its exact seed split is

```text
0 < z < eta       : 186-variable edge system
eta < z < kappa   : 124-variable base system after exact relabeling
kappa < z < e     : reflected 186-variable edge system
```

The 186 system has 93 coordinates in each orientation. Its source matrices satisfy the exact external-parity gauge `M_- = G M_+ G`, where G is the orientation sign matrix. RC5's rational midpoint certificate has inverse infinity norm below 63 and physical coefficient perturbation norm below `10^-12`; its Neumann bound proves invertibility in the stated source scope. The rational midpoint matrix called `M_0` there is **not** RC0's two-dimensional bulk `M_0`. [RC5, RC5V]

These results strengthen the inputs to shell elimination. They do **not** prove that the same sign conjugacy survives any proposed reduced ports or that a two-dimensional transfer exists. The seed seams and parameter equalities excluded by RC5 remain explicit: a null seed set for an L2 argument is not the same as an omitted parameter endpoint. [RC5]

### 3.5 Screw-family disposition

The screw-family audit contributes alternative Green representations of the same Weil form on their stated common core, not an independent collar equation. Ambient spectral diversity and raw kernel boundary rank must not be promoted to rank on the retained neutral carrier. The Green Cauchy-jet to GERM-state intertwiner was not established; that shortcut remains stopped. A Stieltjes trace available only after persistence is established remains a conditional terminal condition, not a free local coordinate of every candidate. [SF]

## 4. Reconcile the two scheduler descriptions

RC0 proves that `h,k,p` form an integral basis of the rank-three prime-log lattice. After quotienting the bulk h-step, the retained full translation action has two independent residual generators on the h-circle. This does not conflict with G64's different, narrower construction. [RC0, G64]

G64 quotients the single-scale kappa shells and follows the specific second return `lambda_ret=4kappa+tau`. On the kappa-circle its action is `y -> y+tau mod kappa`, with a four- or five-level carry. For `lambda_ret<e<h` it is active only for `y in (0,e-lambda_ret)`. At `e=h` the generic full irrational rotation graph appears. Above h, G64 guarantees that graph as a subgraph; additional higher-level returns can occur. [G64]

Accordingly, **neither description replaces the other wholesale**. Every proposed shell/link compiler must specify the quotient, source interval, level carry, omitted constraints, and coefficient chamber it represents. In particular, existence of the base rotation subgraph does not prove that two fixed matrices already encode all of `h<=e<=j`, including the change at e=p. [G64; integration requirement]

The finite-path bound is uniform only after fixing e<h. Do not infer a bound uniform as e approaches h, and do not reopen a flat enumeration of all path lengths to approximate such a bound. [G64]

## 5. Additive corrections to stale branch statements

| Earlier wording or direction | Refolded determination |
| --- | --- |
| Only the 124 template is certified; 186/248/310/372 are future targets | Superseded as a status statement by G63; RC4/5 additionally reconstruct the first two sizes from source equations |
| The old assembler cannot be found | G62V and G63V are now located and pinned in the private lab; historical byte identity with the artifact formerly sought is not asserted |
| Mixed returns immediately mean infinite components for every e>lambda_ret | G64 distinguishes finite partial-return paths below h from generic full infinite components at h |
| The screw audit rejected a circle model, so G64's rotation is disallowed | The rejected model was an unsupported complete one-generator scheduler; G64 derives a specific domain-restricted quotient/subgraph |
| The return compiler already has a pure Laurent symbol | Retain RC4's affine Toeplitz-Hankel correction |
| RC5's next cursor RC6 requires a fresh unrelated 248 determinant before GERM-65 | Not adopted as a duplicate traversal obligation; use existing G63 coverage and RC4/5 as source-level regression inputs |
| Numerical shell/link hyperbolicity is a transfer theorem | G64 labels it reconnaissance; exact reduction, coefficient bounds, and admissible-word control remain open |

The original notes remain historical records. This table supersedes their stale status/routing statements for the integrated GERM-65 handoff; it does not erase their mathematics or advance either source branch.

## 6. Integrated GERM-65 execution contract — pending

The next individual mathematical pass remains **GERM-65 / MIXED-RETURN CONE TRANSFER**. Read this refold together with G63/G64 and the pinned source records. Do not restart threshold-by-threshold injectivity, run an unrelated second-extra-layer traversal, or open another screw-family pass.

1. **Establish the exact retained interface.** Start from the scalar source equations and the existing finite assemblers. Specify incoming/outgoing ports for a kappa shell and a lambda-return link. Prove that the proposed elimination preserves the relevant kernel and reconstructs discarded coordinates. Certify every required pivot. Two retained coordinates are a target, not an assumption; retain any additional state that cannot be lawfully eliminated.

2. **Use the imported regression cases.** Recover the RC4 base block rows and reflection split, and the RC5 first-extra-layer coupling and parity gauge, under an explicit relabeling or reduction. Use the existing G63 templates as further consistency checks where needed. Matching dimensions or approximate determinant signs alone is not a proof of row equivalence. A fresh replay must report its source pins and actual execution results.

3. **Derive actual event maps and their domain coverage.** Determine determinants, inverses where needed, parity action, and coefficient intervals for the reduced shell/link maps. Register their precise source/target domains and carry cases. Only after proving an interface to the P/J bulk state may the proposed factorization

   ```math
   \mathcal E_j=\mathcal S_{\sigma_j}\mathcal B(r_j)
   ```

   be used. At this entry state it remains a proposed normal form, not a complete-system identity. A kernel-preserving direct scalar-source reduction is also admissible; do not force a P/J identification merely to use Chebyshev notation.

4. **Test cones on the legal directed products.** Seek a certified invariant cone or cone field and expansion for the actual admissible shell/link words. Individual hyperbolic eigenvalues, determinant one, or nearly aligned eigenvectors do not establish this. Do not demand expansion simultaneously for a map and its arbitrary inverse; respect the directed return structure. The inherited elliptic-type bulk and the hypothesized hyperbolic reduced shell are distinct objects.

5. **Close finite paths only with endpoint control.** For `lambda_ret<e<h`, prove that the incoming and outgoing boundary constraints exclude every nonzero finite-path solution, uniformly over the legal path types needed. Cone expansion without the required boundary transversality is not finite-path nonresonance. Handle the exceptional seed set in the actual L2 formulation rather than by an unproved pointwise trace assertion.

6. **Treat the infinite problem separately.** At and above h, establish a measurable, norm-controlled correspondence between the original candidate and the cocycle section. Prove the precise stable/unstable or spectral statement that excludes a nonzero L2 invariant section. A positive numerical Lyapunov exponent, or expansion only on one cone, is not by itself that conclusion. Reconcile extra upper-chamber returns and the coefficient threshold e=p before claiming coverage through e=j.

Each item is an **open obligation**, not an output of this refold. A failure of two-port reduction, a missing coefficient chamber, or an unresolved L2 implication must be recorded at its exact interface. No determinant, cone, or new interval certificate is issued here.

## 7. Exit state

```text
REFOLD: recorded, source-pinned, and scoped
GERM-64: last completed experimental mathematical pass
GERM-65: next target; NOT EXECUTED BY THIS OPERATION
RETURN-COCYCLE-0..5: selectively integrated with original scope/standing
RETURN-COCYCLE-6: not launched as a duplicate finite-layer traversal
SCREW SHORTCUT: stopped; valid representation algebra retained
EXPERIMENTAL RANGE: unchanged, L <= log(3^24/(2^24 5^5))
CANONICAL THEOREM CURSOR: SZ-CROSS-COLLAR-3, unchanged
RATIFICATION / PUBLIC PROMOTION: none
```

The next pass inherits one reconciled package: existing finite coverage, exact bulk compression, source-level tail and reflection algebra, fresh base/first-layer regression certificates, and two distinct remaining return regimes. It does not inherit an already-proved shell transfer, cone theorem, or L2 exclusion.
