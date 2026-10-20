# MG31 — Exact rational coordinate-independent original source residual gate

October 20, 2026. Stacked on [MG30 PR #279](https://github.com/monocap-tech/weil-lab/pull/279). The last accepted original complete-frequency MG30 nonscalar source trial verified 36 exact Fraction candidate residual upper bounds for genuine 23 dual-trace-kernel source vectors plus the original sinh pole. All tested **coordinate-dependent Gershgorin margins were negative** (best -9.1488244e-8), so no strict original source contraction passed. A negative Gershgorin margin is NOT evidence of negative inertia. MG31 tests that ambiguity.

## What the matrix is

Given true complete-original-frequency interval Gstar/Sstar source brackets and the same original physical 24-channel H, MG30 proved

```
R*R <= R_upper(Hup,LG,UG,US;B=tI+D).
A := Hlo-R_upper.
```

This is an **exact rational matrix lower bound** for the physical source residual-contraction difference H-R*R. It is NOT the actual original signed operator, nor the original true spectral Schur complement. The method must never confuse a negative direction in A with a negative direction in the true operator: a nonsharp lower bound can be indefinite while the true difference is positive.

## Exact rational congruence strategy

For the accepted MG30 scalar baseline, best Gershgorin trial, and best nonscalar trial in each of the four original 16-/32-cell k=12/16 scenarios, deterministically reconstruct the **same accepted MG30 rational B** and verify the EXACT stored MG30 margin. Explicitly rebuild A (including all complete original pole Gstar/Sstar mixed terms).

At grid denominator d=10^18, or if needed 10^24, round each symmetric exact A_ij to a rational grid value A0_ij, with independent exact Fraction check

```
|A_ij - A0_ij| <= 1/(2d).
```

The symmetric error matrix has spectral norm at most 24/(2d)=12/d by maximum absolute row sum. Thus **with proof**

```
A0 - (12/d)I <= A <= A0 +(12/d)I.
```

A floating eigensolver can only propose an approximate eigenvector basis. Convert it to an exact rational matrix Q using fixed denominator 2^20, then evaluate `Q^T[A0-(12/d)I]Q` in exact rational arithmetic. If its EXACT Gershgorin lower margin is strictly positive, this is a rigorous positive-definiteness certificate for A; strictly positive transformed Gram implies Q is automatically invertible. This may recover a source one-step contraction rejected by unconditioned Gershgorin, although quantitative H-relative margin requires its own proof.

Alternatively, if a rationalized candidate vector v has

```
v^T[A0+(12/d)I]v < 0,
```

then v is an exact **negative quadratic witness for A**, the *certification bound itself*. No change of coordinates can make that particular A positive definite. This does not establish a negative direction for the actual R residual, original operator, or Riemann zeros.

If neither witness succeeds, status is INCONCLUSIVE; no positivity or negativity is inferred. All decisive signs are proven from **exact rational inequalities**, not from floating eigensolver output.

## Acceptance

Require pinned independently accepted Actions artifacts: MG24 #39378465438, MG29 #39440914565, MG30 #39442984941; true original SI10 physical Gram and MG11 23+pole source basis; exact source-residual algebra replay; exact grid enclosure inequalities and rational congruence/Rayleigh witness. Compare all four original source cases, report accepted/inconclusive/negative-bound count without pretending this exhausts all B trial matrices.

Do NOT infer a 470D invariant range/strong inverse from finite 24D contraction. W-ODD-NEG, original signed 51/56 cap, independent Fourier/form/domain identification, complete odd/even/Weil/CC27/RH remain OPEN.

**CI: PENDING.**
