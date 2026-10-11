# RPB108 RC89 — frequency-weighted archimedean transfer

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: `c15cece46105dec9510a1fd0571802311b5bc588` (RC88).

## Result

RC89 retains the frequency dependence of the archimedean multiplier in
the low-frequency Legendre remainder estimate. Ninety rational Fourier
shells replace the prior use of the full physical multiplier norm on the
entire low band. The infinite Legendre tail is still paid explicitly.
The stronger arch bound is attached to the complete actual-source
covariance with RC88's unchanged canonical complement norm.

| Quantity | RC88 | RC89 |
|---|---:|---:|
| Actual head rank; source inputs; polynomial trial dimension | 38; 22; 64 | 38; 22; 64 |
| Canonical complement norm upper, approximately | 0.715574633375 | unchanged |
| Projected arch norm upper divided by `sqrt(rho)`, approximately | 0.476104236561 | 0.453846973785 |
| Even projected-source relative upper | `63/128` | `251/512 = 0.490234375` |
| Odd projected-source relative upper | `1843/4096` | `459/1024 = 0.4482421875` |
| Retained maximum relative upper | 0.4921875 | 0.490234375 |

The arch upper decreases by approximately **4.674872%**. The retained
source upper factor decreases by **1/252**, approximately **0.396825%**.
The transfer and final source matrices improve RC88 in whole Loewner
order, verified by exact rational PSD tests. These are improvements of
certified upper bounds, not measurements of actual leakage.
Generation and independent replay: **PASS**.

## Physical polynomial subtraction and multiplier envelope

Use aperture half-width `B=11/10`, Fourier convention
`exp(-2*pi*i*xi*x)`, actual canonical Riesz projection `Pi38`, and
`rho=252/257`. RC66/RC74 supply the full physical arch remainder
multiplier bound `K=643/100` and, for `|xi|>0`,

`|m_arch(xi)| <= h(|xi|) = log(1+e/|xi|)+1/(2|xi|)`.

The latter is decreasing. On a shell `a<|xi|<=b`, a valid multiplier
upper is `k(a)=min(K,h(a))`, using `K` when `a=0`.

For each Fourier plane wave restricted to the physical aperture, subtract
its orthogonal physical Legendre projection of degree less than 38. The
corresponding Riesz image lies exactly in the actual head and is killed
by `(I-Pi38)i*`. The polynomial subtraction is therefore exact even
though the original Riesz vectors are only enclosed numerically.

## Complete shell remainder bounds

Let `D_n=(2n+1)!!`, `m=38`, and

`T_n(L)=4B L (2*pi*B*L)^(2n)/D_n^2`.

The RC78 Rodrigues estimate and Legendre Parseval expansion bound the
physical squared plane-wave remainder by

`2B sum_{n>=m}(2n+1)|2*pi*B*xi|^(2n)/D_n^2`.

Integrating this nonnegative bound over the symmetric shell
`a<|xi|<=b` gives

`HS_shell^2 <= sum_{n>=m}[T_n(b)-T_n(a)]`.

The normalization accounts for both frequency signs; the integrated
factor `2n+1` cancels. The right side bounds the physical Hilbert-Schmidt
norm squared of the shell remainder operator.

RC89 keeps the first twelve terms, `38 <= n <= 49`, exactly. For the
remaining terms, dropping the nonnegative subtraction at `a` and using
the ratio of consecutive integrated terms gives

`sum_{n>=50}[T_n(b)-T_n(a)]`
` <= T_50(b)/(1-r_50(b))`,

where `r_50(b)=(2*pi*B*b)^2/103^2 < 1` for every evaluated shell.
Thus every shell upper is

`S(a,b)=sum_{n=38}^{49}[T_n(b)-T_n(a)]`
`       +T_50(b)/(1-r_50(b))`,

rounded upward on the `10^-50` rational grid. The first twelve terms do
not replace the infinite expansion: the geometric term explicitly pays
all omitted degrees. The validator evaluates 90 shells of width `1/20`
from frequency 0 to `9/2` and stores their rounded bounds and weighted
contributions. Only shells up to a selected cutoff enter that candidate.

## Weighted low band and high-band closure

For a cutoff `L` at a shell endpoint, multiplying each shell kernel by
the bounded arch multiplier yields

`HS_low(L)^2 <= sum_{b<=L} k(a)^2 S(a,b)`.

This retains the smaller multiplier where most of the Legendre remainder
mass occurs. It replaces the prior coarser expression `K^2 theta(L)`.
The low-band physical remainder norm is at most `HS_low(L)`. The physical
high-band output norm is at most `h(L)` times the norm of the high-band
input, by the Fourier multiplier bound and contraction under restriction
to the aperture.

For a physical input extended by zero, its low- and high-frequency input
parts are orthogonal on the whole real line. Their output remainders are
not assumed orthogonal. The triangle inequality and scalar
Cauchy–Schwarz nevertheless give the full physical output remainder bound

`beta_phys(L)^2 = HS_low(L)^2+h(L)^2`.

The degree-less-than-38 low-band polynomial output is subtracted before
applying the canonical adjoint complement. RC88 gives its uniform norm
upper `tau=0.7155746333745389...`. Consequently

`||(I-Pi38)i*K_arch|| <= tau beta_phys(L)`.

The finite exact cutoff search covers 21 endpoints from `7/2` to `9/2`
in steps of `1/20`. It selects `L=21/5`, with

`beta_phys <= 0.6280413174427247...`,
`beta_arch = tau beta_phys/sqrt(rho) <= 0.4538469737847650...`.

Both root ceilings are rounded upward on the `10^-30` rational grid.
This is an operator remainder bound after physical polynomial subtraction,
not a bound of this size for the unprojected full arch operator. The
chosen shells and cutoff give a certified improvement; no globally optimal
partition or cutoff is claimed.

## Attachment to the complete actual source

The prime and signed-pole transfer bounds remain exactly those of RC88.
So do the original 22 source inputs, all Riesz trial coefficients, RC81's
complete physical Riesz-error Gram upper `E_phys`, RC68's source operator
approximation error `delta`, the physical trial Gram `T`, and the nominal
source subtraction residual covariance `W` from RC71.

Let `k_p=beta_arch+beta_prime+beta_pole,p`, `s=tau^2/rho`, and
`nu=1/65536`. The complete projected actual-source transfer covariance is
bounded by

`E_can = rho[(1+nu) D_k E_phys D_k`
`                 +(1+1/nu)delta^2 s T]`,

with outward Loewner rounding of the bracket on the `10^-24` grid.
All original Riesz and source approximation uncertainties are still paid.
The strengthened arch constant receives the one adjoint norm appropriate
to its polynomial-subtracted output; no duplicate prime or pole tail
factor is introduced.

The nominal source covariance upper is unchanged, `N=tau^2 W`. A final
paid Young inequality gives

`A(t)=(1+t_p)N+(1+1/t_p)E_can`.

With the old RC88 parameters, exact rational PSD checks already certify
whole Loewner improvement. A nine-value rational search for each parity
again selects `t_even=1/4` and `t_odd=5/16`. The final matrix improves RC88
in whole Loewner order and satisfies

`A_even <= (251/512) M22_even`,
`A_odd <= (459/1024) M22_odd`.

Here `M22` is RC67's actual original 22-input canonical Gram lower matrix.
Parity preservation gives the retained maximum factor `251/512`.
The matrix describes the actual rank-38 projected original source, with
22 inputs; it is not a new 38-input source covariance.

## Independent replay and provenance

Replay independently encloses `e` by a rational Taylor series with a
geometric tail and `pi` by Machin arctangent bounds. It verifies every
odd double factorial using its factorial identity. Every power difference
`b^p-a^p` is independently reconstructed as the positive finite sum
`(b-a) sum_{j=0}^{p-1} b^(p-1-j)a^j`.

The multiplier logarithms use a separate rational positive atanh series,
with exact power-of-two range reduction and an explicit geometric tail.
Those bounds must fit inside the saved directed logarithmic intervals.
The integrated infinite remainder and upward shell/root rounding
conditions are checked with exact fractions.

Replay directly contracts the 64-mode physical trial Gram through mass
sums, rebuilds the actual source attachment in units of `rho`, and verifies
final PSD comparisons after exact native-to-Legendre congruence. It repeats
the complete calculation and requires equality with the saved JSON.

Nine input hashes bind RC88, RC78, RC81, RC71, RC68, RC67, RC70, RC59 and
RC74. Relevant RC88 input links and RC78's link to the physical arch bound
are checked, together with actual head rank, fixed source input count,
matching `e`/`pi` boxes and the unchanged nominal covariance identity.

```bash
python scripts/validate_rpb108_rc89_frequency_weighted_arch_transfer.py --replay certificates/rpb108_rc89_frequency_weighted_arch_transfer.json
```

## Remaining scope

The scalar source budget remains open. No actual rank-38 budget failure,
new original-source input covariance, enlarged Weil or complement floor,
whole-aperture positivity, RH, F4 or Lean formalization is asserted.
The arch transfer has become tighter, while the nominal source residual,
prime transfer and underlying Riesz approximation remain separate targets
for further reduction.
