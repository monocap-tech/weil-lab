# NF552 — Original 242 odd initial jets reduce to 68-node Hermite interpolation

**2026-11-16 PT. Draft stacked on NF551 PR #579. Compiler repairs and new source audit are committed; they require CI acceptance. No unconditional Lean independence/Gram certificate is claimed. W_ODD_NEG and RH remain OPEN.**

## 1. Inherited CI: isolate the actual NF546 failures

NF551 head `e571e72dbe336cef5fa61a06483a90b24754efe2`, NF546 job `133605579843` in run `43954566178`, failed on THREE issues after earlier four repairs:

1. Original oscillator continuity: `fun_prop` could not decide the **fixed source node parity conditional** under the opaque original node; NF552 explicitly cases on `Even (nf545OriginalOscillatorNodeAt ...).2`, leaving only continuous power, sine, cosine and complex cast.
2. Compact bound: the primed boundedness lemma was elaborating the wrong implicit compact set; NF552 uses the unprimed `IsCompact.exists_bound_of_continuousOn` with the explicit **original full physical window** as `ContinuousOn` domain.
3. The pole window indicator proof closed after `congr 1`; a trailing `exact` was an extra tactic ("no goals to be solved"). NF552 removes that tactic, retaining the true sinh-pole formula.

These are **candidate repairs**, not verification. Other NF547–NF551 Lean errors may become visible only after this upstream module compiles.

## 2. A smaller original independence certificate than the 136 complex roots

The NF551 order-484 ODE and 136 characteristic-root description remain valid. But **oddness** allows the original 242-dimensional independence problem to be reduced to **68 squared-frequency nodes** (67 original positive frequencies and the genuine pole).

Index the unchanged original selected oscillator functions by original rational `f>0`, order `0<=k<m_f`, and put `omega_f=2*pi*f`. The original convention is

```
j_(f,k)(x) = x^k sin(omega_f*x) when k even
             x^k cos(omega_f*x) when k odd
j_pole(x) = sinh(x/2).
```

Define the **exact 242 x 242 odd-initial-jet matrix**

```
A[n,(f,k)] = d^(2n+1)/dx^(2n+1) j_(f,k)(0),
A[n,pole]  = d^(2n+1)/dx^(2n+1) sinh(x/2) at x=0,
0 <= n < 242.
```

For `k<=2n+1`, elementary Leibniz/differentiation gives

```
A[n,(f,k)] = (-1)^(n+floor(k/2)) * (2n+1)!/(2n+1-k)!
              * omega_f^(2n+1-k),
A[n,(f,k)] = 0 if k>2n+1,
A[n,pole]  = 2^(-(2n+1)).
```

These identities are **exact**, and do not involve collocation or approximating the 242-dimensional weighted Gram.

Multiply row `n` by `(-1)^n`. For the oscillator columns,

```
(-1)^n A[n,(f,k)]
   = (-1)^floor(k/2) (d/domega)^k [omega*(omega^2)^n] at omega=omega_f.
```

For the pole column,

```
(-1)^n A[n,pole] = (1/2)*(-1/4)^n.
```

Thus set

```
t_f=omega_f^2=4*pi^2*f^2  (>0),
t_p=-1/4 (<0).
```

All **68 t-nodes are distinct**: the 67 original rational f are positive and distinct, and the true pole t-node is strictly negative.

## 3. Exact symbolic determinant formula

Let the ordered nodes be the 67 original pairs `(t_f,m_f)`, followed by `(t_p,1)`. Their total multiplicity is `sum_f m_f + 1 = 241+1=242`. Define the standard confluent Vandermonde

```
V[n,(a,k)] = (d/dt)^k t^n at t=t_a,
0<=k<m_a, 0<=n<242.
```

The operator `p(t) -> (d/domega)^k[omega*p(omega^2)]` at a fixed nonzero `omega_f` is a triangular combination of `p^(ell)(t_f)` with `ell<=k`. Its coefficient on the top `ell=k` term is **`omega_f*(2*omega_f)^k`**. Combined with the original sign `(-1)^floor(k/2)`, each oscillator block has an invertible triangular column transformation; the pole column contributes the nonzero scalar `1/2`.

The ordinary confluent Vandermonde determinant is

```
det V = [product over nodes a, k=0..m_a-1 of k!]
        * [product over ordered a<b of (t_b-t_a)^(m_a*m_b)].
```

Consequently the **exact original odd-jet determinant** is

```
det A =
(-1)^(242*241/2) * (1/2)
* [product over original (f,k) of
        (-1)^floor(k/2) * omega_f * (2*omega_f)^k]
* [product over 68 nodes a and k=0..m_a-1 of k!]
* [product over ordered nodes a<b of (t_b-t_a)^(m_a*m_b)].
```

Every factor is nonzero for the **actual** `omega_f=2*pi*f`: `pi>0`, `f>0`, all `t_f` distinct, `t_p<0`. Hence **det A != 0 as a mathematical consequence of the formula**.

If a global original complex linear combination `S_d(x)=0` for all real `x`, all its 242 odd initial derivatives vanish, so `A*d=0` and `d=0`. This supplies a second complete **paper proof** of `NeutralNF551OriginalJ242GlobalIndependence`, independent of the 136-root annihilator argument. Via the NF551 analytic collar equivalence, the **source-specific** canonical positive Gram follows on paper as well. This does NOT assert those implications are Lean compiled.

The 68-node architecture is preferable for formalization: polynomial Hermite interpolation at distinct **real** t-nodes replaces 136 complex exponential roots, and exact positivity/noncollision suffices. An abstract determinant identity followed by the source-specific derivative bridge should be the terminal Lean path.

## 4. Independent full-size original-source audit

New `scripts/local_replay/verify_nf552_original_odd_jet_hermite_factorization.py`:

- Pins the same exact NF407 J242 SHA and NF500 native-raw SHA; confirms all 241 **original** oscillator node orders, all 67 source groups, unchanged Lean source table, and genuine final `sinh(x/2)`.
- Constructs the entire **242 by 242** matrix of odd derivative formulas, not a reduced sample. Performs modular Gaussian elimination at the exact formal specialization `pi=1` over the known prime `2^61-1` and requires a nonzero determinant.
- Independently computes the 68-node Hermite-product determinant at that same specialization; requires exact equality of the two modular values.
- Outputs explicit limits: a modular specialization is a **structural cross-check**, NOT a proof that the determinant is nonzero at the real transcendental `pi`. That conclusion instead uses the displayed symbolic factorization and positive/distinct real nodes.

The modular check can catch a single wrong source parity, missing pole factor, repeated source index, wrong derivative order, or incorrect multiplicity. It is **not a Lean compiler certificate for the generic confluent determinant formula**.

## 5. Formal proof obligations for NF553

1. Obtain actual clean pinned Lean builds of NF546 then NF547, NF548, NF549, NF550, NF551. Repair compiler errors according to job logs; do not count passing SHA-Python as Lean acceptance.
2. Prove the generic confluent Vandermonde determinant and/or injectivity of finite Hermite jets `p↦(p^(k)(t_a))_{a,k}` for distinct real nodes of total multiplicity 242. A divisibility-degree proof is natural: a degree<242 polynomial with the prescribed 242 root multiplicities must be zero.
3. Prove the exact selected-source odd-derivative formula and the real squared-frequency triangular change of basis in Lean, including the genuine sinh pole.
4. Combine into a source-specific `NeutralNF551OriginalJ242GlobalIndependence` **theorem, no new hypothesis**; transfer through the NF551 collar identity and NF550 weighted square to unconditional strict positivity of the **original** canonical 242 Gram.
5. Separately establish REAL-data conjugation-equivariance so odd corrections are not inadvertently complex rather than real.

**Non-transfer:** No finite Gram fact proves the true NF528 original positive/negative divisor graph source convergence, NF527 1/10 gamma+prime+both-poles coercivity, NF539 signed Weil identity, W_ODD_NEG, or RH. All remain OPEN.
