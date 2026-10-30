# NF396 — Compute the actual original selected odd-pole correction without native Gram replay

**2026-10-29 PT.** Canonical `W-ODD-NEG` **OPEN**. This is a new *original object* source-only mathematical certificate, NOT a completed signed selected moment or an RH result. Stacked above the NF395 execution-observability draft. The NF395 telemetry and original selected native receipt files were still NOT_FOUND at the start of NF396; absence cannot prove failure.

## Recover and differentiate original from shadow

Fix the unchanged original physical interval `I=[-B,B]`, `B=11/10`, original odd pole `s(x)=sinh(x/2)`, fourth matched source `u4=F*T*e4-E*(I+Y0)*T*e4`, original `E⊥J242` and `s∈J242`. Hence the **exact** old NF393 identity

`<u4,s>=<F*T*e4,s>`.

The frozen original selected `j387(x)=alpha*(121-100x²)*sin(2π*(37/64)*x)`, `alpha=-88873/2^48`, belongs to unchanged J242. The whole **mandatory** source-selected pole correction in the true Fourier-multiplier moment is exactly

`P387=2*<F*T*e4,s>*<j387,s>`.

Crucially the old n512/n513 exterior observations see no pole. This **selected** moment does, so it must not be dropped.

## Original 32 sine frequencies collapse to one closed-form source sum

The unchanged actual PR355 physical sine frequencies are `c_n=5n/11`, `n=1..32`. Therefore `ω_n=2π c_n` and **exactly** `ω_n B=nπ`. Direct integration gives

`I(ω)=int_-B^B sin(ωx)sinh(x/2) dx = 2*[(1/2)cosh(B/2)sin(ω B)-ω sinh(B/2)cos(ω B)]/[(1/2)^2+ω²]`.

Consequently at each original sine `ω_n`,

`I(ω_n)=(-1)^(n+1)*2ω_n*sinh(B/2)/(ω_n²+1/4)`.

The retained original pole self-overlap is likewise **exact**:

`<s,s>=sinh(B)-B`.

Write the unchanged PR355 fourth-source coordinates `g_n=Σ_(k=1)^4 (T_(k,4) C_(n,k))`, including its 33rd pole source coefficient, with original dyadic `T e4=(-2271087,-1621433,1115405,1048576)/2^20`. Then no J242 Gram and no huge raw `Y0*T` are needed:

`<FTe4,s>=Σ_(n=1)^32 g_n I(ω_n)+g_33*(sinh(B)-B)`.

For the actual original j387, differentiation with respect to the frequency yields `I''(ω)=-int_-B^B x²sin(ωx)sinh(x/2)dx`. Thus another exact scalar formula is

`<j387,s>=alpha*[121 I(ω_*)+100 I''(ω_*)]`, with `ω_*=2π*(37/64)`.

No numerical integration and no new signed Weil kernel cells enter either identity.

## Independent rigorous rational evaluation

The source-authentic replay `scripts/local_replay/nf396_original_odd_pole_exact_interval.py` verifies the exact PR355 original Git blob `d87cf3cb9972bed42db4c54e89a05d742499d2d0` and the frozen original NF387 selected vector Git blob `d705ae312be5324bff64f3a9540e30e8b8bd34dc`. It rebuilds all 33 original source coordinates from the four actual source probes and original dyadic T column. It encloses π by Machin's `π=16atan(1/5)-4atan(1/239)` alternating rational series, paying its exact first omitted terms. It evaluates sin/cos/sinh/cosh by **rational interval Taylor sums**, with explicit twice-first-omitted tail payments for bounded arguments. All source-provenance, interval and positivity comparisons use exact `Fraction`, not IEEE floats.

An independent **local** exact Fraction replay of the 33 original aggregated rational fourth-source coefficients (cross-checked against the unchanged PR355 source) passed all three strict enclosures:

`723/1000 < <FTe4,s> < 725/1000`

`-65/10^10 < <j387,s> < -64/10^10`

`-95/10^10 < P387 < -92/10^10`.

Numerical values for orientation only: `<FTe4,s>≈0.723960442102327`; `<j387,s>≈-6.457191448937619e-9`; `P387≈-9.349502352224488e-9`. The **certification** is the rational strict enclosure, not these displayed decimal approximations. The bounds are frozen separately at `notes/data/provisional/NF396_original_j387_pole_interval.json`. The original signed remainder itself remains unmeasured; remote replay completion has not been asserted.

## New exact remaining cancellation obligation

The original candidate-sensitive multiplier moment must be

`A387=Wodd(u4,j387)+P387`.

NF392 gives the fixed-source sufficient low-band candidate rejection test

`|A387-||j387||²| > 1.31e-20 => this single frozen j387 CANNOT satisfy NF375 fourth low-band target at cutoff 2^24`.

The pole magnitude is provably `>9.2e-9>7e11*(1.31e-20)`. **Therefore**, a necessary (not sufficient) condition for this j387 to *pass* the original NF375 criterion is:

`|Wodd(u4,j387)+P387-||j387||²| <= 1.31e-20`.

This isolates the exact missing **one signed selected scalar** and shows that a large negative pole correction must be offset by a corresponding signed Wodd contribution to extremely high precision. It does **NOT** rule out such cancellation: the original archived signed `WJJ/WJF` source remainder has not been accepted for this fixed j387.

**Previous NF395:** native job-state unobservable; j387 undecided. **Current NF396:** fully certified actual original odd-pole correction separated from the open signed remainder. **Next NF397:** recover or compute the genuine `Wodd(u4,j387)` signed archived scalar with source/hash/rounding audit, combine with the now independently certified pole interval and physical norm², apply the existing NF391/NF392 test, and stop only j387 if justified.

The general original signed lowband **UPPER**, infinite complement inverse, operator/source domain, `W-ODD-NEG`, even/whole Weil positivity, RH **OPEN**. No historical overwrite or main merge.
