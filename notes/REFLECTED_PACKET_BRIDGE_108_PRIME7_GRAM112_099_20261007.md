# RPB108: whole-domain positivity at aperture 99/100

2026-10-07 UTC. Continuation of the complete 99/100 native/source construction published at `1abf19e7abe8e85c7b899503bac6eaaa43239231`. Concurrent global/F4 work and historical certificates are preserved.

The full eleven-panel matched 112-source residual Gram and the actual source-error corrected Schur sign pass at aperture 99/100. Whole-domain actual positivity is certified through **0.99**, with the conservative published bounds

\[
 Q(h)\ge10^{-31}\|h\|_{\mathrm{mass}}^2,
 \qquad Q(h)\ge8\times10^{-34}E_{\log}(h).
\]

## Complete matched Gram

The retained and projected-away physical degrees are 0 through 111. Two fresh complete constructions start with separate initially absent checkpoints. They integrate all eleven panels and retain the complete 90/110 source polynomials, of maximum degree **421**, through product integration degree **842**. All endpoint-log, smooth, mixed and 112 projection terms are present; no 49/50 Gram is transferred to this target.

The complete outputs and panel checkpoints repeat byte for byte. All three 112-by-112 CS, smooth and cross contraction matrices are retained, giving **37632 saved interval entries**. The largest residual entry width is about **2.421135114108674e-80** on a 300-digit outward grid. Endpoint-log construction uses 160 Machin terms. Independent reconstruction uses closed binomial Legendre coefficients, endpoint-log squared Hankel moments, 320 Machin terms and a finer 400-digit grid.

Independent exact rational endpoint projections validate all **12544 native/source pairings**, including both enclosure widths and actual source allowances. No source allowance is increased. Every displaced pairing control is rejected. All **12544 residual entries** reconstruct independently inside their saved enclosures, with every displaced residual control rejected. Complete error aggregation and normalization are rechecked from the source input.

## Actual corrected sign

The complete source allowance remains eta about **6.529425981605490e-36**, below 6.54e-36. The full residual trace gives map norm bound M about **6.876391040899991**, with actual operator correction

\[
 \delta=\eta(2M+\eta)\approx8.979777264426324\times10^{-35}.
\]

The matched complement is the independently proved **193/200**, strictly below its unrounded lower bound about 0.9655228660957642. The actual corrected matrix

\[
 Q_{112}-(200/193)(R_{112}+\delta I)-1.25\times10^{-29}I
\]

passes all **112 outward pivots at 160 digits**. The full corrected sign certificate repeats byte for byte. A separate audit widens the saved native and residual inputs to 80 digits and passes all 112 corrected pivots with the same shift. Negative diagonal controls are rejected. This uses the actual source correction and the proved target complement, without an assumed larger complement or uncorrected sign.

## Full physical and logarithmic conversion

An integer lift norm bound **L = 8** gives

\[
 \mu=\frac{\tau c}{\tau+c(1+8^2)},\quad
 \tau=1.25\times10^{-29},\quad c=193/200,
 \qquad \kappa=\frac{\mu}{10(\mu+24)}.
\]

The exact conversion determinant equals mu squared and is strictly positive. Oversized conversion controls are rejected. Mu is about **1.923076923076923e-31** and kappa about **8.012820512820513e-34**, supporting the rounded published bounds above. The fresh Gårding-24 audit includes the actual target prime/pole budgets and the published multiplier estimate m0 >= w/10 - 6.

## Custody and remaining scope

`notes/data/RPB108_PRIME7_GRAM112_099_CUSTODY_20261007.json` pins every new file and archive part, unchanged arithmetic dependencies, the matched preflight and prior native/source custody. Complete Gram and panel checkpoints use deterministic gzip/base64 transport with compressed and decoded SHA256 checks and verified Git blob hashes. File and dependency hashes are checked on the provisional publication tree, and the published custody bytes are checked again.

Restore the complete archives with `python scripts/restore_native_prime7_gram112_099_archives.py`; restore the native/source inputs with their prior published restoration script. The complete Gram auditor accepts primary/repeat Gram and checkpoint paths; pairing and residual auditors accept restored contractions; the pinned corrected sign constructor and separate widened whole-domain auditor reproduce the scalar result.

The original full Gram extraction keeps its pre-sign false flags; the separate final Schur and whole-domain audit records supply the positive corrected sign. Historical 49/50 certificates, native/source finite-only records and concurrent global/F4 evidence remain intact. Global endpoint exclusion, F4, full transport and Lean formalization remain open. Further aperture work requires fresh target parameters and matched coupling checks.
