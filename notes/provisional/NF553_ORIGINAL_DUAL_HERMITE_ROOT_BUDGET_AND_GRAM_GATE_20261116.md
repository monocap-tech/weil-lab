# NF553 — Original 242 independence from the dual 68-node polynomial root budget

**2026-11-16 PT. Draft stacked on NF552 PR #580. Independent source audit of NF552 full 242×242 original odd-jet determinant has now returned CI SUCCESS (run 43958541368, job 133619443020); corresponding NF552 and NF546–NF551 Lean compilation remains separately pending. New NF553 standalone Lean lemmas are source implementations until compiler acceptance. RH OPEN.**

## 1. The substantial change: no 242×242 determinant theorem is necessary

NF552 proved on paper that the original 242 odd-derivative matrix has nonzero determinant by reducing it to a 68-node *confluent Vandermonde*. A smaller, cleaner route to formalization uses the **dual** of that matrix.

Let
```
A[n,(f,k)] = j_(f,k)^(2n+1)(0),   A[n,pole] = (sinh(x/2))^(2n+1)(0),
                         0 <= n < 242.
```
For an arbitrary real row coefficient vector `a=(a_0,...,a_241)`, define
```
p(t) = sum_(n=0)^241 (-1)^n a_n t^n.
```
The sign is chosen to absorb the exact oscillator derivative parity. Then

```
sum_n a_n A[n,(f,k)]
   = (-1)^floor(k/2)
     (d/domega)^k [omega p(omega^2)] at omega=omega_f,
sum_n a_n A[n,pole] = (1/2) p(-1/4).
```

Therefore if `a^T A=0`, we know for every original positive oscillator frequency `omega_f=2*pi*f`:

```
(d/domega)^k [omega p(omega^2)]_(omega=omega_f) = 0
                         for 0 <= k < m_f,
p(-1/4) = 0.
```

The first condition says that `F(omega)=omega*p(omega^2)` has a root of multiplicity at least `m_f` at the **nonzero** `omega_f`. Since `omega -> omega^2` has derivative `2*omega_f ≠ 0`, this transfers to a root of `p(t)` of multiplicity at least `m_f` at `t_f=omega_f^2` (for polynomials this may be proved algebraically from factorization rather than by invoking an analytic inverse-function theorem).

Together with `p(-1/4)=0`, this yields the divisibility statement

```
H(t) = (t+1/4) * product_(f original) (t-4*pi^2*f^2)^(m_f)
H | p.
```

All 68 nodes are distinct, with original multiplicities totaling `1+sum_f m_f=242`, so `H` is monic of degree **242**. But by construction `degree p <=241`. Hence **p=0**. Its monomial coefficients are exactly `(-1)^n*a_n`, so `a=0`. Thus `A^T` is injective, hence for the finite square original matrix `A` is invertible and `A*d=0 ⇒ d=0`.

Finally, if an arbitrary **complex** original generator combination `S_d≡0`, all its 242 odd derivatives at the origin vanish. The real matrix `A` annihilates the real and imaginary parts separately, giving `d=0`. This discharges the original **complex** global independence on paper without ever computing an enormous determinant or invoking distinct complex-root exponential-polynomial uniqueness.

### Why this is a better Lean architecture

Only the following mathematical components need to be formalized, in this order:

1. One **generic** polynomial root-multiplicity transfer for `omega * p(omega^2)` at nonzero `omega`.
2. The standard algebraic fact that distinct root factors of the prescribed multiplicities produce their entire product as a divisor.
3. A **degree contradiction** between `deg H=242` and `deg p<=241`.
4. A real finite-dimensional square-matrix injective/surjective transfer, then complex real/imag decomposition.
5. The exact 242 source odd-derivative identity, preserving the NF407 oscillator parity and genuine sinh pole.

No generic 242×242 determinant expansion or polynomial Hermite-interpolation *formula* is required.

## 2. Standalone candidate Lean lemmas

`WeilDefect/Arithmetic/ActualZetaOriginalJ242HermiteDegreeObstruction.lean` implements:

- `neutralNF553HermiteDegreeObstruction`: a degree-242 polynomial divisor cannot divide a nonzero degree-<242 real polynomial;
- `neutralNF553PositiveSquareNode`: oscillator square nodes strictly positive;
- `neutralNF553PositiveSquareNodeInjective`: squaring is injective on positive reals;
- `neutralNF553GenuinePoleNodeSeparated`: the original pole squared node -1/4 cannot equal any real square.

This file is intentionally independent of the pending NF546 source dependencies, so its **compiler acceptance can be tested in isolation**. It does NOT use an axiom or silently assume the hard source derivative-to-polynomial bridge. Further source-specific Lean wiring is required.

## 3. Exact signed orientation of the original matrix

In the **unchanged** NF407 order, the 67 rational frequencies are strictly increasing. Every oscillator square node difference `t_b-t_a` for `a<b` is therefore positive; the genuine pole, appended last, contributes precisely **241 negative pairwise factors counted with multiplicity**.

The 242 row signs have exponent `242*241/2=29161` (odd). The original source parity transformations contribute

```
sum_(f original) sum_(0<=k<m_f) floor(k/2) = 165 (odd).
```

The total determinant sign exponent is `29161+165+241=29567`, so

```
sign(det A) = -1
```

in that precise original row/column order. **This is stronger than merely proving nonzero** and offers another independent source-order consistency check. The sign is analytically forced for genuine `pi>0`; it is not inferred from the modular specialization.

## 4. Verification boundary

NF552 source audit CI on inherited commit `78c761ee4e021a9a5a50e761905e8b2c99c644d0`: **PASS**. It constructed the full original 242×242 odd-jet matrix at the *structural test specialization* `pi=1` and matched its nonzero modular determinant against the exact 68-node Hermite product over prime `2^61-1`.

**Still open:** source-specific Lean odd-jet differentiation, root-multiplicity transfer, finite-matrix rank transfer, real-to-complex linear independence, upstream NF546-551 compilation, unconditional canonical Gram positivity in Lean, genuine NF528 positive/negative all-divisor source-graph convergence, NF527 1/10 coercivity, NF539 signed Weil identity, W_ODD_NEG and RH.

## 5. Next NF554

Obtain compiler acceptance of the isolated new NF553 polynomial-degree/root-separation lemmas, and recover the upstream NF546→NF551 Lean chain. Then formalize the derivative-to-polynomial identity and root-multiplicity transfer **without** introducing a source-independence premise. Once the genuine original global `NeutralNF551OriginalJ242GlobalIndependence` is proved, use the existing NF551 local↔global theorem and NF550 source-positive weighted square to establish canonical original Gram positivity without assumptions.
