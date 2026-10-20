# MG25 — Exact mixed source-response residual criterion with adverse uncertainty refusal

October 19–20, 2026. Stacked on MG24 #273, whose calculation-bearing true-original 24D matrix enclosure CI is independently in progress. **This MG25 PR is a finite-dimensional algebra acceptance tool, not a verified application to the original Fourier operator.** It must never be described as a signed odd/even or RH result.

## The genuine source-aware trial identity

For any genuine finite source map F with columns in the strong domain of the complete self-adjoint Astar, take

```
H=F*F,  G=F*Astar F, S=(Astar F)*(Astar F), Y=F B.
R=F-Astar Y = F-Astar F B.
```

Then for an arbitrary matrix B, **without** falsely assuming B commutes with G,

```
R*R=H-G B-B* G+B* S B.
```

For strictly positive S, the unconstrained least-squares finite-source choice is `B_ls=S^{-1}G`. This minimizes the sum of squared source residuals and gives `R*R=H-G S^{-1}G` (or the appropriate projected response identity); it is **NOT** a proof that the finite span is invariant or an inverse of the full operator.

MG24 returns true-operator Loewner *enclosures* rather than actual G/S matrices. For

```
Hlo <= H <= Hup;
Lg <= G <= Ug;
S <= Sup;
Gc=(Lg+Ug)/2,  E=(Ug-Lg)/2 >=0,
```

the unknown G error W=G-Gc obeys `-E<=W<=E`. Therefore `||W||_op<=||E||_op<=max_i sum_j |E_ij|` (the last is an exact rational bound for symmetric E). For exact rational B, `||B||_op<=max(||B||_1,||B||_infty)`. The **true ambient strong residual** has the rigorous matrix upper

```
R*R <= Hup-Gc B-B*Gc+B*Sup B
        + 2||E||_upper ||B||_upper I.
```

This pays the entire unknown mixed G response, rather than incorrectly inserting Lg in both noncommuting mixed terms. Every matrix is exact rational. This formula is valid only when the supplied source Loewner brackets have been proved for the same full-original operator and basis.

A strict positive Gershgorin margin `m` for `Hlo-Rupper` proves `R*R<=H-m I`. With a certified `H<=K I`, it follows `R*R <= (1-m/K)H`, a genuine finite-source one-step contraction in the physical norm. If the margin is nonpositive, reject.

## Independent nontrivial pole test and adverse case

The MG25 validator operates on an **explicit three-dimensional rational surrogate**, with a noncommuting positive diagonal pole-free operator and a genuine rank-one pole. It independently expands

```
Sstar=So-2(cb*+bc*)+4 sigma bb*
```

and checks the actual matrix identity, including nonzero mixed pole terms, against direct multiplication. A nonscalar least-squares source response passes a *tight* rational interval residual gate; an intentionally much wider but still mathematically valid interval is REJECTED. This is a test of the method's refusal logic, not a claim that the true original source bracket has useful conditioning.

## Immediate next original acceptance

1. **Wait for actual MG24 acceptance before consuming its matrices.** MG24's 24D arrays must be validated with original full-frequency and genuine pole response included; do not infer that MG24 passed from the existence of its source file or PR.
2. Construct candidate rational source-aware B from the validated MG24 source G/S *centers*, with rounding performed outward in a subsequent exact arithmetic verification. The numerical solver may only propose B.
3. Evaluate the full complete-original 24D `Rupper` using the matrix G error charge above, with the real reconstructed physical Gram H.
4. Accept only if the exact H-relative residual margin is strictly positive and quantitatively useful. If not, report its precise defect and improve the poorly controlled omitted-frequency source moments, instead of inventing a scalar inverse.
5. Even a passing 24D source gate is not invariant under `I-Astar FB`, cannot be iterated to a global Neumann inverse, and does not prove MG07 470D negative 51/56 cap. The independent original Fourier/domain identification, complete odd, even, Weil/CC27, and RH obligations stay OPEN.

MG25's first Actions only verifies its **finite surrogate algebra** and fail-closed criteria. Full-original numerical acceptance requires a *separate* run on verified MG24 inputs.
