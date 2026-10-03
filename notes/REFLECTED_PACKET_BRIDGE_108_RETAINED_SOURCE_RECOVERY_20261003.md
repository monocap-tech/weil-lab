# RPB-108 — retained source recovery
Date: 2026-10-03
Parent: f66fc319b88d3efdde0bfc90d66783a5c04921b5

## Recovered source, not an attached carrier witness

The current task is actual witness attachment. This pass adds no conditional representation layer.

Directly inspected primary source: Xuefeng Zhu, arXiv:2608.24827v2,
https://arxiv.org/html/2608.24827v2.

The inspected passages are §1.6; §2, equation (7); and §6.1, Lemma 6.1 and its proof. The main source convention is real-even outside §6. Equation (2) alone cannot be used as a full-complex nonnegative pole formula.

## Source dictionary on admissible tests

Write
```math
F_+(t)=\int f(x)e^{itx}\,dx,\qquad
\mathcal Ff(\xi)=\int f(x)e^{-2\pi i x\xi}\,dx.
```
Then
```math
F_+(t)=\mathcal Ff(-t/(2\pi)).
```
Since the retained digamma/prime symbol is even, the change of variables gives
```math
\frac1{2\pi}\int\Psi_a(t)|F_+(t)|^2\,dt
=\int\Psi_a(2\pi\xi)|\mathcal Ff(\xi)|^2\,d\xi.
```
This is the normalization used by `rightLimitCompactWeilSymbolMathlib`.
The strict source cutoff and the frozen right-limit cutoff have already been reconciled in the certified threshold work; no new threshold argument is claimed here.

Put
```math
M_\pm(f)=\int f(x)e^{\pm x/2}\,dx.
```
Lemma 6.1 proves the real parity decomposition, with pole
```math
2(c_f^2-s_f^2)
```
for real f, where c_f is its even cosh moment and s_f its odd sinh moment. The same lemma gives the complex decomposition Q(f)=Q(Re f)+Q(Im f). Combining these identities yields the general-complex pole
```math
2\operatorname{Re}\bigl(\overline{M_-(f)}M_+(f)\bigr).
```
Thus the recovered arithmetic diagonal on the source admissible class has the exact multiplier-plus-Hermitian-pole species of `sourceDomainQuadratic`. This calculation is written mathematics; this pass does not certify a new Lean Fourier-change-of-variable theorem or import the external formula as a Lean axiom.

Equation (7) supplies the zero-side/geometric-side identity for admissible tests. It does not identify the independently parameterized scalar density in the WD-T38 Lean output with the actual nonzero physical carrier's Fourier norm-square density.

## What remains to attach

1. Recover the concrete source form Hilbert carrier, its map into physical L2, and the actual realization of the retained synthesis/null vector under that map. Native Dirichlet Green columns alone do not specify that realization.
2. Prove that this actual vector belongs to the canonical supported logarithmic form domain. Retained named-density integrability is insufficient without its actual density identification.
3. Establish the source diagonal identity on one common domain containing the actual vector and every required compact test. A smooth-test explicit formula does not by itself extend the abstract synthesis form to this completed domain: a compatible continuous/closed form realization and a justified core extension are needed.
4. Transport the actual source mixed null law on the enlarged test domain. A scalar equality Q(k)=0 alone is not a mixed null law; polarization identifies forms from all diagonals but does not turn one diagonal zero into B(k,u)=0. Positivity on the same enlarged domain could justify that implication if genuinely available; it is not supplied by the present independent scalar parameters.
5. Use the existing diagonal/polarization and source-window bridges to obtain actual `frozenWeilCompactAction ... u = 0`. Then immediately consume `neutralExteriorIntegralGrowthResidual_realizes_of_central`, which constructs the weak realization through the existing boundary-removal theorem without a separate regularity or spectral-L2 assumption.

These are missing source facts, not new assumptions appended to an attachment theorem.

## Additional repository recovery

Inspected `monocap-tech/weil`, branch `research/reflected-packet-bridge`, at
`d8bd75eda7442ecda12c23d4f6b76a582a336783`,
tree `d750190a5c3442e0eb5e9c4ba7280723a946d991`.
Its 44 Lean files comprise the root and 43 original modules. All original non-root modules other than `Neutral.lean` match the current lab blobs; the latter is the known subsequent arithmetic-energy custody repair. No additional actual source realization was recovered in this inspected tree. This is not a claim about every historical branch or repository.

## Witness standing

| Witness | Standing |
| --- | --- |
| Primary admissible-test explicit formula and general-complex pole | Recovered external source law; written convention dictionary |
| Actual WD-T38 carrier/domain/diagonal identification | OPEN |
| Same-domain source mixed identity and enlarged mixed null law | OPEN |
| Actual enlarged compact central cancellation | OPEN |
| Regularity and whole compact realization from actual central cancellation | Previously Lean-certified; central input not instantiated |
| Spectral product L2 from WD-T38 | Not derived; unproved and unassumed |
| F-4 logarithmic Gaussian coercivity | NOT STARTED |

One-log form energy is not silently upgraded to the squared-symbol L2 condition. This inspection does not prove universal nonderivability of spectral membership under all additional mathematical source hypotheses.

## Validation and disposition

Documentation-only recovery. No Lean modules, imports, pinned manifests, workflow, or historical note changes. The existing whole-root certificate at `e1959d1c6858c092a7cc51511bf667b13812768e` remains the latest Lean validation; no new Lean certificate is claimed. Promotion is based on the fresh live research head and preserves every other tree entry. Threshold bookkeeping remains CLOSED; WD-T40/RH standing is unchanged.
