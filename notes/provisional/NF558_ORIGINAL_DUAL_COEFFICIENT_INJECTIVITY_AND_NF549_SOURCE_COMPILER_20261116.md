# NF558 — Recover the ORIGINAL 242 odd-jet coefficients and move physical source compiler gate to NF549

**2026-11-16 PT. Draft stacked on NF557 PR #585. New NF558 source-specific polynomial coefficient lemmas and targeted NF549 compiler repair are COMMITTED but NOT YET LEAN ACCEPTED. Real/complex original generator independence, unconditional canonical Gram positivity and RH OPEN.**

## 1. Verified actual compiler movement

The generic algebraic kernel is not presently blocked:
- NF553 exact Hermite degree obstruction, real positive squared-node separation and genuine negative pole separation: **LEAN PASS**.
- NF554 root-multiplicity lower bound from vanishing derivatives in characteristic zero: **LEAN PASS**.
- NF555 quadratic factorization and nonvanishing cofactor for the positive original oscillator node: **LEAN PASS**.
- NF556 precise `rootMultiplicity ω (X*p.comp (X^2)) = rootMultiplicity (ω^2) p` for `p≠0,ω>0`: **LEAN PASS**, GitHub Actions run #43967237428, job #133649771451.

The *separate* NF556 original physical source-chain run #43967237428, job #133649771908, has **FAILED**, but it passed through the corrected original NF547 smooth weighted columns and NF548 real-even compact two-collar cutoff. Its first remaining failure is now **NF549**:
```
ActualZetaOriginalCanonicalGramPhysicalIntegral.lean:69:2
maximum recursion depth has been reached
```
at the original canonical Schwartz synthesis pointwise identity. The log additionally flags an unused `Pi.basisFun_repr` simplifier on the initial synthesis expansion. NF558 makes a narrow compiler-side repair: scope `maxRecDepth 4096` to precisely the target theorem and remove the ineffective simplifier. This changes no integral, source, cutoff, Gram, mathematical assumption, or physical-window identity. It is a CANDIDATE compiler repair pending the next CI results.

The NF557 new original 242 dual-polynomial source/nodes module is still awaiting its separate Actions compilation as of this stage's construction. None of its uncompiled claims may be described as Lean accepted.

## 2. New source-specific polynomial coefficient injection

NF557 defined, literally over the original odd-initial-jet row indices 0..241,

```
p_a(T) = Σ_(i:Fin 242) (-1)^i a_i T^i
```

without a replaced source, fresh basis, or arbitrary generic 242-dimensional carrier.

NF558 adds `WeilDefect/Arithmetic/ActualZetaOriginalJ242DualPolynomialCoefficient.lean`, importing this exact NF557 polynomial and proving the following *candidate* Lean theorems:

### a. Exact coefficient identity
```
coeff(p_a, i) = (-1)^i a_i             for every i:Fin 242.
```
It is a direct monomial-coefficient and finite-sum calculation in the same source ordering, rather than any determinant, interpolation, numerical approximation, or power series surrogate.

### b. Actual 242-coordinate injectivity
```
p_a=p_b ⇒ a=b.
```
Using the coefficient theorem, `(-1)^i a_i=(-1)^i b_i`, and `(-1)^i≠0` cancels to yield `a_i=b_i` for each original row.

### c. Genuine left-kernel extraction
```
p_a=0 ⇒ a=0.
```
This is the precise last step in the NF553–NF557 dual Hermite finite source argument once the original source derivative identities have forced `p_a=0`.

These are source-specific **implementation candidates pending Lean CI**, not assumed independence of the 242 original physical functions.

## 3. Still-missing exact transfer

The actual matrix is
```
A_(n,j) = d^(2n+1)/dx^(2n+1) [original j_j](0),
                               0≤n<242, 0≤j<242.
```
The original selected `j_j` are 241 exact rational-frequency sine/cosine monomials with fixed parity and one true `sinh(x/2)` at index 241.

To finish the original source theorem in Lean, the following remain open:

1. An actual smooth/analytic derivative computation in Lean expressing `A_(n,(f,k))` by the SHA-audited formula involving factorials, powers, and oscillator parity, with `A_(n,pole)=2^(-2n-1)` for the genuine source pole. The source-only exact NF554 58,564 comparison audit is already **PASS**, but is **not a Lean theorem**.
2. Dualize `a^T A=0` using the actual source to obtain `F_a^{(k)}(ω_f)=0`, where `F_a(X)=X*p_a(X^2)` and `ω_f=2πf>0`, and obtain `p_a(-1/4)=0` from the real pole.
3. Apply accepted NF554 and NF556 polynomial multiplicity theorems at all 67 original distinct positive squared nodes; include the true pole as the 68th node, giving total multiplicity 242.
4. Establish that the product of these coprime factors divides `p_a` (or use polynomial root count), contradict `natDegree p_a <242` from NF557/NF553, and conclude `p_a=0` for every original odd-jet left-kernel vector.
5. Use the NF558 coefficient injection and a real square-matrix kernel/cokernel result to obtain actual original source independence, including complex coefficients separated into real and imaginary parts.
6. Only after NF549–NF551 have compiled and original source global independence is a theorem, remove NF550's outstanding independence premise and certify canonical original strict Gram positivity. A real-valuedness/conjugation-equivariance check for real original data also remains independent.

The original 67 distinct NF407 source frequencies, 241 monomial multiplicities, true negative pole and original terminal E collar must remain unchanged throughout. No 'source theorem' can be inferred from the Python audits alone.

## 4. Verification

`.github/workflows/nf558-original-dual-coefficients.yml` contains independent:
- pinned Lean compilation of source-exact NF557 dual polynomial/nodes and new NF558 coefficient injection, rejecting sorry/axiom/admit;
- pinned genuine original NF546→NF551 source-chain build, including targeted NF549 recursion repair;
- SHA-pinned full original NF554 dual odd-jet coefficient audit.

All are pending a new GitHub Actions result. **Do not merge the draft until the actual compiler jobs pass.**

## 5. NF559 target

First check NF557+NF558 Lean results and repair exact error diagnostics. Separately recover NF549–NF551 without weakening the true source. Then formalize the original 242-source odd-initial-jet derivative identity in Lean, starting with the genuine sine/cosine monomial parity and true sinh-pole row.

**Non-transfer:** NF528 authentic full divisor graph/inward affine mollification convergence, NF527 gamma/prime n9/both poles 1/10 coercivity, NF539 signed Weil source equality, W_ODD_NEG and RH remain **OPEN**.
