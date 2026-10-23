# MG61 — Original strong-action source-plane conditioning and exact rational orthogonal gauges

**Status: implemented, independent GitHub Actions numerical acceptance pending.** Parent [MG60 PR #309](https://github.com/monocap-tech/weil-lab/pull/309) independently verified 50 genuine original source projected 2D moment matrices using MG58's 47/55 physical Fourier subcells plus MG59's correlation-preserving project-before-error architecture: **0/50 strictly positive-definite 2D lower matrices**, despite full exact rational producer and independent replay passing [Actions #39959456013](https://github.com/monocap-tech/weil-lab/actions/runs/39959456013).

## A new obstruction in the certificate: the chosen 2D source basis can make a valid moment bound unusually loose

MG60's tests used a physically valid but highly UNBALANCED basis `[v, e_i]`, where the accepted MG57 mixed integer source vector

```
v=(-3,0,-2,2,2,0,1,2,1,2,2,2,1,-2,-2,2,0,2,2,2,2,1,-3,-2), ||v||²=82.
```

The second vector `e_i` is a unit original source coordinate. This makes the initial 2D affine Young error charge dominated by the first coordinate; because the accepted Young bound subtracts a diagonal error fee proportional to `(rho_1+rho_2)rho_i`, it is NOT invariant under a change of source-plane basis, even though the TRUE physical source moment is covariant under such a basis change. No certificate failure here proves negativity of the genuine physical `S_*=(A_*F)^*(A_*F)>=0`.

For each original coordinate `i=0..23`, form the exact rational source-plane orthogonal complement

```
w_i = e_i - (v_i/82)v,qquad v^T w_i=0,qquad ||w_i||² = 1-v_i²/82>0.
```

Then use the same physical original source plane `span(v,e_i) = span(v,w_i)` but produce NEW exact Young certificates for TWO BALANCED rational source-plane bases:

```
W_{i,1}=[v/9,w_i],qquad W_{i,2}=[v/18,w_i].
```

This changes neither the physical source nor the underlying original operator, only the *basis in which the physically valid 2D projected-source error budget is enclosed*. The selected 55-cell original physical Fourier source archive is exactly the independently accepted MG58 original pole-corrected signed seven-prime/digamma action source; physical MG57's genuine 12 source subcells remain unchanged. The original [5/8,7/8] new source cells are unchanged, and the strong action energy in all unmeasured original real frequencies is still positive semidefinite. No reweighting of the original operator or discarded physical frequencies is allowed.

## Acceptance: exact 2D Gram, restricted source coefficient norm

For each of **48 new original physical source-plane gauge certificates**, independently reconstruct all 55 genuine original Fourier source cells from accepted MG57/MG58 source generators, project onto `[v/9,w_i]` and `[v/18,w_i]` BEFORE charging MG59's true shared multiplier scalar, same original sinh pole/source Taylor, or interval errors, and calculate complete exact rational original source 2D affine Young lower `L_i`. Each is valid only for its exact projected physical 2-plane:

```
W_i^T S_* W_i \succeq W_i^T S_{*,[0,4]}W_i \succeq L_i.
```

A strict 2D original physical source-action positivity claim is accepted **only** on exact conditions
```
a=(L_i)_{11}>0,\quad c=(L_i)_{22}>0,\quad ac-(L_i)_{12}²>0,
```
then with `u=v/9` or `u=v/18`, `w=w_i` the bound
```
x^T S_* x \ge
\frac{ac-(L_i)_{12}²}{(a+c)(||u||²+||w||²)}
||x||²,qquad x\in span(u,w).
```

This produces a restriction **only on the chosen genuine original two-dimensional source subspace**, NOT a global original `S_*>=c W W^T` Loewner lower. If all 48 tests fail, it is a new *finite accepted basis-gauge no-go*, not a proof that no better original 2D source restriction exists.

## Independent replay

Producer uses accepted physical original 55-cell MG57/MG58 records and MG59's project-before-error 2D cell moment to calculate 48 rational upper/lower matrices, with normalized source Gram and exact 2D determinant signs. The independently authored verifier does NOT import MG61's producer: it recreates the original 55 physical cells from separately independently authored MG58 physical interval generator and MG59 accepted original baseline builder, builds exact original physical pole Gram via MG24, and computes EVERY 2D matrix through MG59's separately implemented independent projected-source moment accumulator, including the rational `v\perp w_i` identities. All 48 exact rational 2D positivity outcomes and any positive coefficient constant are checked without relying on floating eigenvalues.

Even if 2D coercivity is achieved, the original 24D source residual contraction, 470D inverse, odd signed 51/56 spectral cap, independent Fourier/form/domain and complete even/Weil/CC27/RH remain OPEN.
