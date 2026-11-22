# Weil-Lab — CP-C1(A) nine-probe phase-complete finite-form reconstruction

**Independent cross-projection structural gate | 2026-11-22.** Based on current CP034 source head `c6eb36832beed0974000371296360b92e76e36ad`, including CP001–CP004's frozen three-bump family, and source-aware phase negative controls in IV030/PI027–PI034. The new mathematical result is elementary exact Hermitian linear algebra. **NO original Weil-source Lean proof, no independent arithmetic/zeta spectral equality, no exhaustive spectral zero certificate, no general Weil positivity, and no RH.** Do not modify NF/IV/PI proof or acceptance records or call source-independent Fraction checks a compiler receipt.

## 1. The frozen test space and the convention that must be proved

Preserve CP001's **actual** smooth compactly supported real tests:

- `f_- = b_(-1099/1000, 1/2000)` and `f_+ = b_(1099/1000, 1/2000)`;
- `t_r = b_(1/5, r)` with `r` in `{1/1000,1/500}`;
- `b_(c,h)(x) = exp(1-h^2/(h^2-(x-c)^2))` for `|x-c|<h` and zero otherwise;
- `V_r=span_C{f_-,f_+,t_r}`; `G_r=diag(m_0,m_0,m_r)>0`, where `m_0=h*a_2`, `m_r=r*a_2`, and `a_2=integral_{-1}^1 phi^2>0`.

The original IV011 mixed correlation convention is `C(s,t;u)=integral t(x)*conj(s(x-u)) dx`, i.e. **conjugate-linear in its first test, linear in its second**. Consequently the following algebra applies to the *full* original Weil form only **once** its Hermitian mixed-form laws and polarization/source identification have actually been proved. It applies separately and unconditionally to any abstract 3x3 Hermitian matrix with this convention.

Define the true original source diagonal, not an abstract PSD surrogate, as `q_A(v) = Re(neutralIV010Diagonal (11/10) v)`. Define the independent complete explicit-formula arithmetic diagonal `q_E` and centered zero-side `q_Z,T` only with matching signs, Fourier normalization, reflected off-line factors, domain and admissibility. No identification of those three functions is assumed here.

## 2. Nine real probe evaluations recover every complex mixed entry

Let `B` be a **Hermitian sesquilinear** form on `V_r`, with `B(u,v)` conjugate-linear in `u`, linear in `v`; let `q(v)=B(v,v)`. For the ordered basis `e_0=f_-`, `e_1=f_+`, `e_2=t_r`, evaluate exactly the following **nine scalar diagonals**:

1. Three single-source energies `d_i=q(e_i)`, `i=0,1,2`.
2. Three real-phase pair energies `p_ij=q(e_i+e_j)`, `i<j`.
3. Three quadrature-phase pair energies `s_ij=q(e_i+i e_j)`, `i<j`.

All nine probes remain authentic compactly supported Schwartz tests in the same physical source support window. For the true mixed matrix `A_ij=B(e_i,e_j)`, sesquilinearity gives exactly

```
A_ii = d_i,
Re A_ij = (p_ij-d_i-d_j)/2,
Im A_ij = -(s_ij-d_i-d_j)/2,         i<j,
A_ji = conj(A_ij).
```

The **minus sign** in the imaginary reconstruction follows from the original `C(s,t)` conjugation orientation. Under a linear-first convention it would be reversed. Applying an unsupported switch of convention is a falsifiable mathematical error.

**Exact finite equality criterion:** for two genuine Hermitian forms on the same frozen space and with the same convention, equality of their nine indicated real diagonal evaluations is **equivalent** to equality of their entire 3x3 complex mixed matrices. There are nine independent real entries in a 3x3 Hermitian matrix (three diagonal, three complex offdiagonal); without additional structural laws, fewer than nine independent real linear observations cannot determine the whole matrix.

This is a proposed small *acceptance architecture for CP-C1(A)*, not a proof that the original signed Weil or independently constructed zero-side pairings satisfy the necessary Hermitian/source hypotheses.

## 3. Phase and support negative controls

CP002/CP003's source-conditional prime-only matrix on these frozen tests is

```
A_prime = [[0, -alpha, 0],[-alpha, 0, 0],[0, 0, 0]],
alpha = (log 3/3)*I_9 > 0,
I_9 = integral f_+(x+log 9)*f_-(x) dx > 0.
```

Therefore the signed **prime-only**, not full Weil, diagonal satisfies

```
q_prime(f_-+f_+) = -2 alpha,
q_prime(f_--f_+) = +2 alpha,
q_prime(f_-+i f_+) = 0.
```

These three tests have identical physical supports and physical L2 mass because the old bumps have disjoint support. The prime-interaction **support graph is also identical**. Thus graph/mass/support-only observations cannot preserve the signed arithmetic contribution. In particular, one cannot infer equality of the full forms from an active-prime graph, separate diagonal positivity, or an even-real-only sample.

For the original two real bump shapes, the true prime-only imaginary mixed entry is zero, so the `+i` probe is a symmetry negative control rather than evidence that every conceivable complex-phase interface has been tested. The **full** Weil mixed entries still contain original poles and Gamma; do not set them to zero on the ground that the central prime interactions vanish. IV030 and PI027–PI034 supply separate, non-graph phase challenges which should remain independent adversarial inputs.

For the two radii, the old-old `2x2` block must be identical, since `f_-/f_+` are unchanged. If two independently produced source/comparison matrices have different old-old blocks, reject before comparing tail bounds.

## 4. How certified probe errors imply an operator-norm error

Let `D=A_r-Z_(T,r)` (or `A_r-E_r`), assuming **both** sides are valid Hermitian matrices in the *same* convention. Suppose independent, source-audited, outward-certified real errors give

```
|q_D(e_i)| <= delta_i,
|q_D(e_i+e_j)| <= delta_plus_ij,
|q_D(e_i+i e_j)| <= delta_iplus_ij,
```

where all nine `delta` are nonnegative. Put

```
P_ij = delta_plus_ij + delta_i + delta_j,
S_ij = delta_iplus_ij + delta_i + delta_j.
```

Then `|Re D_ij| <= P_ij/2`, `|Im D_ij|<=S_ij/2` for `i<j`. Hence, writing `G=diag(m_i)>0`,

```
||G^(-1/2) D G^(-1/2)||_op^2
  <= ||G^(-1/2) D G^(-1/2)||_F^2
  <= sum_i delta_i^2/m_i^2
       + 2*sum_(i<j) (P_ij^2+S_ij^2)/(4*m_i*m_j).
```

The right-hand side is an **exact rational expression** if the admitted masses and nine error budgets have exact rational bounds. It can be compared with `epsilon^2` without evaluating square roots. To certify `epsilon<1/500`, one must first obtain valid source-audited probe enclosures and certified physical mass lower bounds. A raw generated error budget, floating-point match or external JSON assertion does not itself supply these hypotheses.

The operator inequality is a finite linear-algebra consequence; it does not provide the missing zero enumeration, off-line zero tail, original arithmetic/zero-side equality, Hardy-Z root proof, or spectral-model injection.

## 5. Reproducible exact negative-control self-test

The companion `scripts/cpc1a_nine_probe_algebra.py` uses only Python `fractions.Fraction` to check three nontrivial 3x3 rational Hermitian examples, including purely imaginary entries. It reconstructs all nine real degrees of freedom; it **rejects** the incorrect imaginary polarization sign, checks `+1/-1/i` prime-phase examples, and instantiates the mass-normalized Frobenius-budget algebra on a small illustrative rational mass/error tuple. The sample masses/errors are **not certified original physical masses or actual zeta/Weil comparison errors**.

Local execution of the complete script: **PASS**. This checks exact algebra, not the genuine Lean proof language, Fourier kernel, real smooth bump integrals, zero completeness or any CP-C1(A) source statement.

## 6. Next source-bound gate

1. On the original Phase IV v4.34 source branch, prove that the literal `neutralIV010Diagonal` induces a Hermitian mixed form on the frozen span with the original IV011 convention. Do not import the v4.35 external Zeta `.olean` into this toolchain without an explicit compatibility port.
2. Source-bind the actual nine frozen test vectors and the true `Pole - Prime + Gamma` diagonal to the independently calculated nine explicit-formula diagonals, retaining n=9 and all original constants. The prime-only first/second phase controls are immediate falsifiers, not full-form identities.
3. Keep the finite-height complete zero roster, even-real cosine-moment evaluations, off-line reflected upper tail and normalized mass error budget as **independent** CP-C1(B) proof legs. Use the nine-probe error formula if/when all nine separate source/bounded-zero evaluations have been admitted.
4. Preserve the CP034 four-theorem successful Lean receipt and CP029 pointwise-Borwein / the remaining 524 complex source cells as a separate numerical formalization queue. Do not label a pending n=2 original `cpow` interval certificate as CP-C1(A) success.

**Stop conditions:** missing Hermitian or source-polarization law; imaginary-sign mismatch; source-diagonal vs independently derived complete explicit-formula probe inconsistency; two-radius old-block inconsistency; true zero count/interval completeness failure; or a lower proved discrepancy exceeding the admitted operator norm budget. No favorable numerical output can override one of these conditions.