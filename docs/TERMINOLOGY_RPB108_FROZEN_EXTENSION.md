# Terminology registry — RPB-108 frozen-extension supplement

This is an additive companion to [Terminology](TERMINOLOGY.md). These names describe project-local constructions; they do not claim new conventional terminology or a reconstructed EXT-4 witness.

## Frozen compact-test action

The action `frozenWeilCompactAction` holds the selected cutoff radius `a` fixed while its compact Schwartz test `u` varies. It evaluates the normalized tempered core plus the named two-exponential pole:

```math
E_a(h;u)=T_a(h)(u)+\int_{\mathbb R}u(x)p_h(x)\,dx.
```

The test's compact support is an explicit argument, and pole-product integrability is proved. This compact-test action is not claimed to be a tempered distribution, because its pole can grow exponentially. Defining it does not establish that a supplied residual represents it or that its compression equals an imported source form.

## Prime shell between cutoff radii

For selected radii `a <= b`, the prime shell is the finite difference

```math
S_{a,b}=S_b\setminus S_a,
\qquad S_a=\{n:\ n\text{ is a prime power},\ \log n\le 2a\}.
```

It retains the project's strict-right equality-threshold convention. Its mathlib-frequency symbol is

```math
D_{a,b}(\xi)=\sum_{n\in S_{a,b}}\frac{2\Lambda(n)}{\sqrt n}
\cos(2\pi\xi\log n)=\Psi_a^{ml}(\xi)-\Psi_b^{ml}(\xi).
```

The corresponding explicitly defined physical finite-shift expression is

```math
P_{a,b}h(x)=\sum_{n\in S_{a,b}}\frac{\Lambda(n)}{\sqrt n}
\bigl(h(x-\log n)+h(x+\log n)\bigr).
```

The source defines both expressions separately. Their Fourier compatibility is a theorem obligation, not something inferred from these names. The physical expression vanishes on `(-a,a)` when `supp h` is contained in `[-c,c]` and `c <= a`, since each new shift has `log n > 2a`.

## Residual attachment

Residual attachment means proving that the chosen actual residual represents `E_a(h;u)` for every compact Schwartz test. The theorem `frozenWeilCompactAction_represents_iff` characterizes exactly this obligation by the existing `RightLimitWeilWeakRealizationPremise`; it does not discharge it.

**Registration:** RPB-108 frozen-extension continuation, September 30, 2026 (America/Los_Angeles).
