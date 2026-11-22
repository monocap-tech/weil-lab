# Weil-Lab — CP-C1(E): the exact CP001 flat profile and corrected prime-channel custody

**Jurisdiction:** Independent CP, source-attached to the original signed Weil pairing. This does not modify Phase III NF or Phase IV IV source. **Status:** exact-rational independent geometry PASS; genuine Lean 4.34 compiler and axiom audit PENDING for 14 new physical Schwartz candidates. CP-C1(B/C/D) are also pending a genuine new compiler run. No RH or global Weil positivity.

## 1. A material correction to the previously prepared local overlap experiment

The canonical [CP001 source specification](docs/CP001_CROSS_PROJECTION_COMPATIBILITY.md) freezes **old-bump radius `h=1/2000`**, not `1/1000`. An earlier *local-only*, not source-committed CP-C1(E) geometry script had used `h=1/1000` as though it were the original CP001 bump. That was incorrect: its old support would touch the strict original collar endpoints. **Do not import its estimates `I9>1/10000`, `kappa*I9>1/30000`, or normalized `>1/60` into CP001.** The present corrected script fails closed if the old radius changes to `1/1000`.

The exact original CP001 profiles, unchanged, are

\[
\phi(u)=\begin{cases}\exp(1-1/(1-u^2)),& |u|<1,\\0,&|u|\ge1,\end{cases}
\quad
f_-(x)=\phi((x+c)/h),\quad f_+(x)=\phi((x-c)/h),\quad t_r(x)=\phi((x-q)/r)
\]

with `c=1099/1000`, `h=1/2000`, `q=1/5` and `r in {1/1000,1/500}`. The old closed support intervals are respectively `[-2199/2000,-2197/2000]` and `[2197/2000,2199/2000]`. Each lies **strictly inside** its genuine original open collar. The three support intervals are disjoint, and the physical window remains `[-11/10,11/10]`.

## 2. Exact Mathlib smoothness connection, no replacement bump

Mathlib's already-defined `expNegInvGlue(z)` is `exp(-1/z)` for positive z, zero otherwise, and has a proved `C∞` theorem `expNegInvGlue.contDiff`. Therefore the exact frozen formula is also

\[
\boxed{\phi(u)=e\cdot\operatorname{expNegInvGlue}(1-u^2).}
\]

This is an **identity of pointwise functions**, not a convenient but different smooth surrogate. Composition with `(x-c)/r`, positive-radius compact support, and the existing `HasCompactSupport.toSchwartzMap` produce the actual complex Schwartz objects. The new candidate file `WeilDefect/Arithmetic/CP_C1E_FrozenFlatSchwartz.lean` supplies all steps as proof candidates: literal piecewise identity, infinite differentiability, support and center value, actual complex `𝓢(ℝ,ℂ)` packaging, frozen `Fin 3` family, original window support, and specialization of CP-C1(C)'s full original arithmetic–complete-divisor matrix equality. **These declarations are not accepted until a real v4.34 Lean kernel/axiom run succeeds.**

## 3. Exact rational classification and nonzero original n=9 prime overlap

The new `scripts/cpc1e_frozen_cp001_prime_geometry.py` uses `Fraction`, order-36 rational exp Taylor partial sums and rigorous geometric tail majorants. No floating-point inequality decides a claim. It classifies every prime shift `log(n)` for all integers `n>=2`: `2<=n<=12` checked directly; `n>=13` excluded by `log 13>5/2`.

For both frozen radii, the sole support-compatible shift is **n=9 between the two OLD bumps**. There are no central/old or self prime channels. The old pair are NOT translates by exactly log 9: `2c=2.198`, whereas `2.19722<log9<2.19723`. The verified strict interval is

\[
\frac{77}{100000}<\delta=2c-\log9<\frac{78}{100000}.
\]

On `|x+log9/2| < 3h/50`, both normalized bump arguments obey `|u|<21/25`, and their exact frozen profile satisfies

\[
\phi(u)>e^{-441/184}>1/11,
\]

because `e^(441/184)<11` has its own exact-rational Taylor certificate. The subinterval length is `2*(3h/50)=3/50000`. Thus

\[
\boxed{I_9=\int f_-(x)f_+(x+\log9)\,dx>\frac3{6050000}>0.}
\]

For the true von Mangoldt weight `kappa=Lambda(9)/sqrt9=log3/3>1/3`, and the original old mass `m=h*a2<=2h=1/1000` (`a2=∫phi²`), this yields

\[
\boxed{\kappa I_9>\frac1{6050000},\qquad 2\kappa I_9>\frac1{3025000},\qquad \frac{\kappa I_9}{m}>\frac1{6050}.}
\]

The coefficient gives a **nonzero true arithmetic prime sector**; the full signed original Weil form includes `-prime` plus both poles and Gamma and has no positivity conclusion from this calculation.

## 4. Mutation controls and custody

Four exact tests deliberately mutate the geometry: setting central coordinate to zero creates an n=3 interaction, widening the central radius to 1/10 creates an n=4 interaction, shifting the right old center by 1/20 removes n=9, and using the erroneous old radius 1/1000 violates the strict old collar inclusion. Each negative control passed.

- `scripts/cpc1e_frozen_cp001_prime_geometry.py`: exact-rational PASS, produces JSON audit (not LEAN).
- `WeilDefect/Arithmetic/CP_C1E_FrozenFlatSchwartz.lean`: 14 actual physical profile and source attachment Lean **candidates**; 16 `#print axioms` requests, including the two upstream C/D names.
- `scripts/cpc1e_frozen_flat_kernel_gate.py`: strict source pins, 16 genuine multiline axiom reports, standard-only trust, actual compiled `.olean`, and a SHA-bound receipt contingent on B/C/D accepted kernel receipts.
- `scripts/cpc1e_frozen_flat_local_kernel_lane.sh`: manual opt-in local B/C/D→E compiler path, **no GitHub Actions launch**.

The independent CP target still lacks a separately constructed complete-root/finitary-zero trace with exact original normalization, robust interval values for all nine readings, a certified tail, and any support-independent positivity proof. The present source can be falsified by a genuine Lean compiler failure or by a rigorous mismatch in the source/target readings; it makes no claim of RH.
