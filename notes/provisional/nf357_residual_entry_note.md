# Weil-Lab — NF357: complete strong-residual entry conditions (read-only)

**Inputs:** PR #355 artifact `12776684037`, archive SHA256 `f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0`; diagnostic JSON SHA256 `d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9`; local NF356 floor >499/50000 under inherited original realization/domain assumptions. Repo unchanged.

**Unchanged objects:** physical original odd space H=L²_odd(-B,B), B=11/10. Selected J_242 contains the actual pole s. Q is the physical orthogonal projection onto J_242^perp. U is the selected finite source frame, Phi=UP are the four original exact signed-energy source directions, E=QF are the four exact physical probe residuals. Let C_Q be the operator associated with the **restricted** positive signed form on QH, with C_Q >=mu I and mu>499/50000; B_cpl=QW Phi is the strong mixed map, when the inherited realization supports it. The 4x4 physical and signed probes are S=E*E, C_E=E*W E, Z=E*W Phi. Y_C is the exact dyadic trial supplied by #355.

## 1. Exact matched residual identity (under strong-domain assumptions)

Put T=E Y_C and R=B_cpl-C_Q T. Then R=QW(Phi-EY_C), provided all these inputs lie in the strong operator domain, and

```
B_cpl* C_Q^-1 B_cpl
 = Y_C* Z + Z* Y_C - Y_C* C_E Y_C + R* C_Q^-1 R.
```

This is the **full infinite exterior Schur correction** on four selected source directions. The first three terms are the measured finite variational term; the last is the *complete* untested strong residual, not a Galerkin inverse upper bound. Because C_Q>=mu I,

```
Full_Schur <= S_trial + mu^-1 R*R.
```

The accepted #355 matched finite-probe calculation gives `S_trial<=G_E<(.002) H_phi` in Loewner sense, where H_phi=Phi*W Phi and H_phi>=.99 I. Thus a sufficient FOUR-DIRECTION completion test is

```
||R||_F^2 < (499/50000)*(99/100)*(499/500)
           = 24651099/2500000000
           = 0.0098604396.
```

The corresponding Frobenius norm threshold is approximately **0.0992997462**. This is **not yet measured**, so no sign/Schur conclusion follows. This gate would close only these four source directions, not the other 238 selected directions and hence not `W-ODD-NEG`.

## 2. Original-pole cancellation in the strong residual

Under the inherited original Fourier-operator realization `W=T_m - 2|s><s|` where `T_m` is the physical compression of the original signed frequency multiplier and `s` the true sinh pole, the identity `Qs=0` gives

```
R = Q T_m (Phi-E Y_C).
```

Therefore the **pole output vanishes exactly** from the exterior residual. It may not be dropped from construction of source Phi, E, physical/energy Grams, or original multiplier analysis. This cancellation avoids any separate pole-output norm payment in the complete strong-residual test.

For h=Phi-EY_C and any physical selected frame U with Gram G=U*U, a projected strong-action identity is

```
R*R=(T_m h)*(T_m h) - (U*T_m h)*G^-1*(U*T_m h),
```

with both terms taken on the physical support. The first term can be upper bounded by whole-line `integral |m(xi)|^2 |hhat(xi)|^2 dxi` by Plancherel. The second (nonnegative) projection term can be **lower** bounded from certified original source-form couplings. Cancellation is essential: simply bounding the whole-line norm alone may be far too coarse. A complete interval proof must combine correlated terms *before* independent enclosure boxing. No numerical value for `R*R` is claimed here.

## 3. Finite-span strong-domain membership is analytically accessible

Every individual selected original function is a compactly supported piecewise-smooth function, with smooth interior and possibly a jump at +-B. Its Fourier transform has `|hat f(xi)| = O(1/|xi|)` by integration by parts. Since the original arch multiplier grows at most logarithmically and the prime cosine part is bounded, `m(xi) hat f(xi) in L²(R)`. So Phi, E and h lie in the **strong Fourier multiplier domain** under the inherited multiplier realization. This does not itself establish identification of the original canonical Weil form/operator with that Fourier realization, or graph/form-core density for the full canonical domain. The latter remains separately OPEN.

## 4. Exact conditioning result and numerical risk

From the retained **exact dyadic** 242x4 signed-energy source coefficients P and the accepted selected physical Gram `.99 I < G <1.01 I`, the physical L² squared norms satisfy, for source directions 0,1,2,3 respectively,

```
||Phi_j||² > 1e16, 1e22, 1e29, 1e34.
```

Yet the complete signed-energy Gram is normalized to `.99 I < H_phi <1.01 I`. The last direction has `||Phi_3|| > 1e17` with signed energy near one. These are certified from dyadic fractions and the accepted Gram; they do not prove the residual is large. They do show that any proposed `R` bound based on uncorrelated raw source entries is likely to face severe cancellation and must explicitly budget its physical-coordinate transport. The exact finite-probe Y_C coefficients are also retained; do not round them or replace the exact projected E with an independent approximation.

## 5. Stop/next cursor

The new stronger exterior floor removes the retained #355 *lower-witness* contradiction but does not upper-bound `R`. A finite 4x4 inverse/Schur computation alone is insufficient.

**Current:** a rigorous **conditional four-direction completion budget** and exact residual formula have been established, with pole-output cancellation and finite strong-domain argument.

**Next:** calculate and certify `||Q T_m(Phi-EY_C)||_F²` including the complete Fourier tail, original support compression, and physical projection. Demand it be `< 24651099/2500000000` before any four-direction positivity transfer. If this fails, retype into a tighter energy-resolved inverse scheme rather than inflating source dimensions. Even a pass leaves 238 selected source directions and the canonical original-domain identification open.

`W-ODD-NEG=OPEN`. No GitHub write or new PR.
