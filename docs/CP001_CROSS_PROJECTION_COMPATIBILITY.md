# CP001 — Cross-projection compatibility of the original signed Weil form

**Independent research track:** CP###. **Do not renumber or edit either** the Phase IV IV### Lean support-extension chain (current observed stage IV020, PR #788, stacked on IV019 #787) **or** the Phase III NF### numerical-custody chain. This is a hypothesis/dictionary document, not a replacement positivity certificate.

**Status:** mathematical interface specification and independently falsifiable finite-test program. NO new Lean kernel-accepted result, NO spectral-model identification, NO unconditional support-extension theorem and NO claim about RH.

## 1. Fixed source, coordinates and the certification boundary

Use the literal original signed arithmetic zeta Weil source from Phase IV, with unchanged physical window [-11/10,11/10], poles, digamma/Gamma integral and complete von Mangoldt prime term:
- `neutralIV011OriginalMixedPole (11/10) f g`
- `neutralIV011OriginalMixedPrime (11/10) f g`
- `neutralIV011OriginalMixedArch (11/10) f g`
- `neutralIV010Diagonal (11/10) f`

For an admissible complex Schwartz f, set `M(f)=neutralNF600Mass f = ||f||_2^2`, and `q_A(f)=Re(neutralIV010Diagonal (11/10) f)`. Write `B_A` for the Hermitian polarization of q_A *once* its Hermitian quadratic-form laws and source conventions are proved. DO NOT define a complex Hermitian pairing merely by taking `Re` of a complex mixed entry.

The historical original strict collar support is
E_old = Ioo(-11/10,-11/10+1/500) union Ioo(11/10-1/500,11/10).
The new central interval E_r=[1/5-r,1/5+r]. At r=1/1000 the union has measure 3/500; at r=1/500 it has measure 1/125. IV020 proposes the complete original source coercivity `q_A(S+v t) >= (1/10)M(S+v t)` for the widened interval; its new modules are **Lean candidates**, not yet a kernel theorem. The original old-old n=9 prime term survives. Old/new and new/new active prime correlations are *proposed* to vanish by exact relative support gaps, NOT by replacing the original Weil source.

## 2. Candidate invariants and provenance

Let U be a complex linear subspace of genuine physical tests, with the fixed original source and the physical L2 norm.

| Quantity | Exact definition | Invariance and limitations |
|---|---|---|
| Hermitian inertia and nullity of q_A on finite U | positive/zero/negative indices of a matrix of B_A on U | invariant under invertible complex basis congruence, once B_A exists and is proved Hermitian; does NOT require a favorable coordinate metric |
| Intrinsic relative bottom `lambda_A(U)` | inf { q_A(f)/M(f) : f in U, M(f)>0 } | basis-independent **relative to physical L2**; changes if the physical inner product is replaced; decreases under inclusions U subset V |
| L1 embedding capacity `kappa(U)` | sup { ||f||_1^2 / M(f) : f in U, M(f)>0 } | independent of basis of U; depends on chosen physical embedding/measure, not an invariant of the abstract signed form; nondecreasing under U subset V |
| Genuine arithmetic prime burden `pi_A(U)` | sup { |Re P_A(f,f)|/M(f) : f in U, M(f)>0 } | basis-independent once the true prime form and L2 norm are fixed; nondecreasing under inclusion; the *bound* 2/5 is an estimate, not the value of pi_A |
| Mixed interaction `R_A(f,g)` | |B_A(f,g)| / sqrt(q_A(f) q_A(g)) when both diagonal terms are >0 | invariant under nonzero independent scalar rescalings of f and g and changes of representation; not defined at zero/negative diagonal; R<=1 is a genuine 2x2 PSD condition, not a 3x3 theorem |
| Active-prime graph of support cells | edge E_i--E_j for an actual prime-power shift +/-log n in E_i-E_j with Lambda(n) nonzero | invariant under common translation of both cells in the unrestricted centered source, but dependent on logarithmic physical coordinates and relative support, not an abstract quadratic-form invariant |
| Admissible extension | q_A >=0 (or >=c M) on U+T, with all source tests in domain | intrinsic to the pair of subspaces, source form and chosen norm; new support disjointness alone is insufficient |
| A chosen numerical budget `m_cert(r)` | 2/5-150r from IV019's particular Gamma/pole/prime estimates | neither an optimal Rayleigh quotient nor coordinate-free spectral invariant; its zero at 1/375 only marks this certificate's loss of positivity |

The reusable source-level inequality, subject to its original hypotheses, is
`lambda_A(U) >= 11/10 - 75*kappa(U) - pi_A(U)`.
It follows by combining the actual signed Gamma/pole estimate `q_A(f) >= (11/10)M(f) -75||f||_1^2 - Re P_A(f,f)`.
For an authentic old-plus-new class with `pi_A(U)<=2/5` and `kappa(U)<=1/250+2r`, it yields `lambda_A(U)>=2/5-150r`. The latter two estimates require SOURCE proofs on U. In particular, the prime estimate cannot be silently carried to arbitrary enlarged supports.

On a finite basis `F=(f_1,...,f_d)` write the Hermitian arithmetic matrix A_F and the L2 Gram matrix G_F, `G_F>0` for linearly independent tests. The generalized eigenvalues of `(A_F,G_F)`, equivalently eigenvalues of `G_F^{-1/2} A_F G_F^{-1/2}`, are basis-independent. Individual entries, unnormalized eigenvalues of A_F, Cholesky margins and floating-point intervals are not. The complete 3x3 inertia must be checked: the rational Hermitian matrix with diagonal 1 and every off-diagonal -4/5 has positive 2x2 principal blocks but has eigenvalue -3/5 on (1,1,1), hence is negative on the full triple.

## 3. Exact arithmetic-to-zero-side dictionary to check

Fix a convention **explicitly**:
`H_f(z) = integral_R f(x) exp(z*x) dx`,
`z_rho = rho-1/2`,
`k_(f,g)(u) = integral_R f(x+u) conj(g(x)) dx`,
and unitary angular-frequency Fourier transform
`fhat(y) = (2*pi)^(-1/2) integral_R f(x) exp(-i*y*x) dx`.

The centered zeros-side candidate is the convergent test-family pairing
`B_Z(f,g) = sum_(rho nontrivial zeros, with multiplicities) H_f(z_rho)*conj(H_g(-conj(z_rho)))`.
This is a Hermitian form by the zero-reflection symmetry. It is NOT asserted positive: off-line zeros do NOT yield a sum of ordinary squared norms.

In this convention the classical additive Guinand--Weil arithmetic formula, on each smooth compactly supported diagonal test f, reads
`
q_EF(f) =
  2 Re[H_f(1/2)*conj(H_f(-1/2))]
  + integral_R Omega(y)*|fhat(y)|^2 dy
  - 2 Re sum_(n>=2) [Lambda(n)/sqrt(n)] k_(f,f)(log n),
Omega(y)=Re digamma(1/4+i*y/2)-log(pi).
`
The finite prime sum follows from compact support. The full *signed* poles and archimedean term are retained. A three-way source dictionary should prove `q_A=q_EF=B_Z(diagonal)` for the selected tests, matching:
1. Physical cutoff and test-class inclusion, real/complex scalar convention, polarization and the original finite-correlation formula;
2. Fourier normalization `y=-2*pi*xi` for Phase IV's `gammaBracket(-2*pi*xi)`, including Plancherel and the exact Gamma/digamma constant;
3. Both half-pole evaluations and their real cross term, not an even-real specialization `2F(i/2)^2`;
4. The literal original `Lambda(n)/sqrt(n)` multiplicities, both signed shifts and the n>=10 cutoff on this original window;
5. Absolute convergence/termwise passage on the zeros side and a rigorous truncation tail bound for the *specific* smooth tests;
6. Equality of the full Hermitian mixed forms by polarization, not merely diagonal entries on one basis.

The first identity is a **known mathematical explicit-formula relation in compatible conventions**, but is not thereby a certified Lean theorem about this repository's literal source. The zeros-side interface has additional analytical formalization obligations. NO argument may use RH to replace the reflected factor by a modulus square.

## 4. Independent comparands and their actual reach

**Arithmetic / compact-window multiplier.** Marcus Chuk, *Weil positivity in compact windows* (arXiv:2608.24827v2, September 2026), uses the full geometric explicit formula with a frequency multiplier and a Legendre finite-matrix reduction; it reports a certified lower bound at the symmetric window [-0.8,0.8]. Its basis, window, parity reduction and numerical certification are NOT identical to Phase IV's disconnected collar class inside [-1.1,1.1]; in particular the paper's tiny lower constant cannot be compared numerically with IV019's 1/10 without a source convention and domain transfer. Its prime-comb cancellation and spectral-edge sensitivity are pertinent to error budgets, not independent proof of the current Phase IV theorem.

**Two-separated-interval arithmetic versus zero side.** Payam Danesh, *A quantitative two-interval criterion* (arXiv:2611.10726v1, 7 November 2026), defines the same centered zero pairing above and an invariant normalized interaction R. For far-separated shrinking intervals, an off-critical zero forces arbitrarily large normalized cross interactions. This makes R a useful cross-projection observable. However that result concerns separation tending to infinity and widths shrinking subexponentially, NOT the fixed 11/10 window or its three cells. The finite prime supports are in moving multiplicative intervals, unlike IV020's fixed n<10 cutoff.

**Spectral/de Branges.** Masatoshi Suzuki, *On the Hilbert space derived from the Weil distribution* (Canadian Journal of Mathematics), describes a Hilbert-space/de Branges isomorphism under RH and unconditionally built auxiliary spaces. A positive Hilbert realization for the entire original Weil form cannot be imported from the RH-conditional identification. Missing: a concrete operator or reproducing kernel, its domain, a fixed isometric map of source tests, and form preservation on mixed pairs.

**Noncommutative trace/spectral.** Connes's adelic trace formula interprets critical zeros as an absorption spectrum and potential off-line zeros as resonances. Missing: an explicit map from these source Schwartz tests to an operator trace domain, trace class/regularization conditions, sign and normalization matching, and a **proved** equality of the compressed Hermitian forms. Merely observing the same zeros or a formally analogous trace formula is not an isometry or a positivity theorem.

**Li-coefficient arithmetic.** Bombieri--Lagarias connect Li's coefficients through the Guinand--Weil formula. The Li sequence uses a different test/limit family, not the finite disconnected-support class. Missing: explicit Mellin test realization or regularized limit, uniform control, and preservation of mixed Gram data; a match between scalar moments would not determine the full form.

## 5. CP-C1 — Falsifiable finite-compression compatibility conjecture

Specify concrete bump functions rather than arbitrary numerical vectors. For rational center c and radius h>0 let
`
b_(c,h)(x)=exp(1-h^2/(h^2-(x-c)^2)) if |x-c|<h, else 0.
`
This is smooth, nonzero, supported on [c-h,c+h], and b(c)=1. Set
`
f_minus=b_(-1099/1000,1/2000)
f_plus =b_( 1099/1000,1/2000)
t_r    =b_(1/5,r), r in {1/1000,1/500}
V_r    =span_C{f_minus,f_plus,t_r}.
`
All old bump supports lie strictly inside the original open NF543 collars. The new test is outside them; G_r is positive definite by disjoint support.

Let `A_r` be the **full polarized original** `q_A` 3x3 matrix and `G_r` the physical L2 Gram matrix. Let `E_r` be the independently calculated complete pole+Gamma+von-Mangoldt 3x3 matrix with exactly the Fourier/pole/prime convention above; let `Z_(T,r)` be the Hermitian matrix from the centered zero sum, truncated to zeros with |Im rho|<=T, retaining multiplicities and reflection pairs.

**CP-C1 (precise, unproved repository interface target).** For each indicated radius:
(A) `A_r=E_r` entrywise by an exact source/form-dictionary proof, and
(B) there exist independently justified certified error bounds `eps_(T,r)->0` such that
`
||G_r^(-1/2) (A_r-Z_(T,r)) G_r^(-1/2)||_op <= eps_(T,r).
`
No assumption of nonnegative spectral terms, RH, or global extension is permitted. The corresponding generalized eigenvalues differ by at most `eps_(T,r)` (Hermitian eigenvalue perturbation). Any positive coercivity asserted by IV020 can be transferred to the independently enclosed finite zero-side compression **only after IV020 passes Lean AND eps_(T,r)<1/10**; even then, this is only on V_r.

Falsifier: freeze the two support radii, the three bump formulas, normalization, zero enumeration method and T; produce mutually incompatible rigorous interval enclosures for one polarized matrix entry or an operator-norm lower bound greater than the proposed certified error. A numeric disagreement alone is an audit trigger, not a disproof, until normalizations, tail bounds and source integrals are independently certified. If the exact classical source dictionary is wrong in the implementation, the conjecture fails for that implementation. CP-C1 is deliberately much weaker than global positivity and is not advertised as a novel criterion for RH.

Optional later **CP-C2** (NOT assumed): for a specifically identified independent de Branges, trace or operator model, construct an explicit mass-preserving injection `J_r:V_r -> H_spec` and prove both mass and mixed Weil pairing identities. Without `J_r`, no claimed equivalence of the arithmetic and operator projections is meaningful.

## 6. Preservation laws and adversarial tests

- **Congruence:** a change of basis f' = fC sends `A -> C* A C` and `G -> C* G C`; inertia and generalized eigenvalues persist; raw numerical centers need not.
- **Extension:** if U subset U', `lambda_A(U')<=lambda_A(U)`, `kappa(U')>=kappa(U)`, `pi_A(U')>=pi_A(U)`; the bound is monotone but a negative bound is inconclusive.
- **Prime-support exclusion:** if for all active Lambda(n) the support differences of new/old and new/new miss +/-log n, their literal mixed and new prime correlations vanish; old/old n=9 remains. This alone does NOT eliminate mixed Gamma/pole contributions.
- **Positive extension Schur test:** for a finite old/new decomposition with old A>0, positivity of the full block is equivalent to the Schur complement `D-B* A^-1 B >=0`; positive separate diagonals or pairwise 2x2 tests are insufficient for 3+ dimensions.
- **Phase/covariance:** scaling a test by a nonzero complex scalar does not alter its Rayleigh quotient; normalized |mixed| is scalar-invariant when diagonal energies are positive. A common translation preserves relative prime-gap geometry and, in the unrestricted centered classical form, the full zero-side B, but the fixed-window repository theorem cannot be translated beyond its admitted domain.

## 7. Research custody and next gates

1. **Phase IV remains primary:** recover actual IV009 through IV020 compiler logs, repair the earliest failed import, preserve strict source-bound standard-only axiom audits, complete IV020's true n9 transfer, measure and 1/10 theorem before claiming them accepted.
2. **CP001 is independent:** freeze the three bumps, complete exact prime-overlap and support arithmetic preflight, construct `A_r,G_r,E_r`; identify every unformalized normalization map.
3. Build complex polarization and interval-enclosed 3x3 arithmetic entries; test CP-C1(A) first. Only then add verified zero data and nontrivial tails for CP-C1(B).
4. Do not transport Chuk's symmetric-window lower constant, Danesh's large-separation criterion, a conditional de Branges isometry, or Li-coefficient positivity into an original restricted support theorem without explicit interface proof.
5. Stop or revise CP-C1 on a verified mismatch; do not widen it into RH or global Weil positivity.

**Source correction (2026-11-20):** arXiv:2608.24827 is authored by Marcus Chuk, verified against the primary arXiv record; no identification with Xuefeng Zhu is justified.\n\n**Sources / audit anchors:** IV019 PR #787; IV020 PR #788; Danesh https://arxiv.org/html/2611.10726 ; Zhu https://arxiv.org/html/2608.24827 ; Suzuki https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-the-hilbert-space-derived-from-the-weil-distribution/FD33EBD117A6B448053450DD8D62ADB6 ; Connes https://arxiv.org/abs/math/9811068 ; Bombieri--Lagarias https://doi.org/10.1006/jnth.1999.2392 .
