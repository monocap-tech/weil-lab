# Weil-Lab — Original-operator proof-obligation audit and critical-path reset (2026-10-23)

**Research governance audit, NOT another MG checkpoint or a claim of RH progress.**
**Canonical active mathematical obligation remains `W-ODD-NEG` OPEN.**
**Caution on custody:** the repository default `main` HEAD observed on 2026-10-23 was `f7570c26b0d3835eb45f7cfd989d1529267ef7eb` (October 15); this audit branch is based on research PR #316 / `d292f520d0363a29176ab5f57cbab92e69eb0fe1`, whose SI/SM/MG evidence is largely unmerged. Do not describe research-branch acceptance as integrated main proof. The manifest `research/obligations.json` is the canonical priority authority, not the latest checkpoint number.

## A. Immediate mathematical correction: qualitative strong-action positivity is already implied

[SI29](../notes/RPB108_SI29_POLE_THRESHOLD_20261016.md) gives the original 14-feature physical pole-only Birman–Schwinger certificate. [SM19](../notes/RPB108_SM19_ORIGINAL_WOODBURY_RESIDUAL_20261017.md) records the *actual original* operator minorant on the supported odd carrier
```
C14 = (1/1000)I + G Gamma G* <= Ao,
B14 = C14 - 2|s><s| <= Astar := Ao - 2|s><s|,
2<s,C14^-1 s> <= 966379/10^6 < 1,
B14 >= kappa_star I,  kappa_star=33621/10^9.
```
The SI29-only pole threshold is NOT a bound on the additional signed negative-frequency operator Kminus. These estimates require the inherited self-adjoint original physical Fourier/form realization, which has NOT received the independent analytic form/domain identification claimed at the RH end.

**Decisive consequence:** for EVERY finite source synthesis `F` with columns actually in `Dom(Astar)`, with positive definite physical Gram `H=F*F`, exact operator functional calculus gives
```
Sstar=(Astar F)*(Astar F) >= kappa_star^2 H,
kappa_star^2 = 1130371641/10^18 = 1.130371641e-9.
```
In particular, for MG11's 23 boundary-adapted original odd sources plus genuine supported sinh pole, physical injectivity [MG21](../notes/RPB108_MG21_FINITE_SOURCE_ANALYTIC_POSITIVITY_AND_RESIDUAL_20261019.md) and strong-domain membership where established already yield full **24-dimensional** strict strong-action positivity. An explicit Euclidean coefficient constant additionally needs a certified lower `H >= h0 I`, but *qualitative rank 24* does not await a new MG67/MG68 computation. The full-original `Sstar` is not the signed Weil form. This analytic implication is conditional on original operator/domain identification being valid; it is NOT an independent revalidation of those premises.

[MG21](../notes/RPB108_MG21_FINITE_SOURCE_ANALYTIC_POSITIVITY_AND_RESIDUAL_20261019.md) separately proves strict positivity of any fixed finite positive-frequency source moment through compact support, entire Fourier transforms and linear independence. It does NOT certify a useful explicit smallest generalized eigenvalue.

**Decision:** MG57–MG67 finite source-strong-action sign/cell/trace/dimension improvements are valid *constructive local quantitative certificates*, but absent a theorem connecting a specific bound to the full ORIGINAL signed residual they do not close a new required qualitative positivity obligation. Do NOT promote a new 3D/4D/24D moment result as critical-path progress merely because the previous conservative Fourier lower matrix was indefinite.

## B. Minimal justified proof dependency graph — ORIGINAL supported Weil route

```
[PROVED conditional-on-original-realization]
 SI29 exact original Ao positive 14-feature supported reference
   + SM19 pole correction: Astar >= kappa_star I
   + MG21 compact-source Fourier analytic finite-moment SPD
                     |
                     v
[PROVED analytic reduction, numerical acceptance OPEN]
 SI10 all-real original signed seven-prime negative-frequency
    Kminus >=0, SM10/SM37 exact finite-source 890-cap + infinite eta
 SM32 original odd E0 rank 470, complement F=E0^perp
    Wodd|F >= mu I, mu=17/25000
 SM33 original negative leakage on F: epsilon<1/15000
 SM34 full-original energy-dual E_A=Astar^-1 E0:
    full positive mixed cross CANCELS exactly,
    signed residual mixed cross is only -Kminus
        |
        +--> SM34 exact corrected finite Schur S_A>=0 on E_A
        |       NECESSARY + SUFFICIENT for Wodd>=0,
        |       given domain, F>0 and Schur hypotheses;
        |       ENTIRE corrected 470D Schur UNCLASSIFIED.
        |
        +--> SUFFICIENT quantitative simplification:
              N=J*Astar^-1 Kminus Astar^-1 J
                    <= theta G=theta J*Astar^-1 J
              theta=51/56, on ALL original 470 coefficients.
              STILL OPEN. This is NOT a necessary condition for
              positivity of original Wodd.
                      |
                      v
[MG07/SM35 conditional computational acceptance, OPEN]
 Original strong-domain 470-trial Galerkin Z,
 R=J-Astar Z, Z*R=0,
 G0=Z*Astar Z, N0cap=Z*Kcap Z,
 DB=R*B14^-1 R, entire original frequency/source matrix:
 (1+t) N0cap+(1+1/t)(Hminus/kappa_star) DB
                    <= (51/56) G0 for some SAME t>0,
 ALL 470 original source coefficient combinations.
 Neither the complete matched matrices nor the inequality
 has been certified for the original source.
                      |
                      v
[OPEN even after the odd inequality]
 W-ODD-NEG original whole odd (PS36 O1/O2) + original
 W-EVEN-FORM (EF01–EF07 no full global even PSD; EF07
 overlapping Rayleigh enclosures) + independent physical
 Fourier / quadratic-form closure and operator-domain transfer
                      |
                      v
[OPEN] W-WHOLE-FORM / original global Weil positivity
                      |
                      v
[OPEN] original CC27 complete native generalized-critical
      defect-relative cross covariance / D-Riesz and F4/global
      source/zero transfer, not supplied by finite signed forms
                      |
                      v
[OPEN] W-GLOBAL-BRIDGE -> actual zeta Weil criterion -> W-RH
```

The SM34 reduction is the simplest *operator-structural* route in evidence: it already removes an entire class of previously uncontrolled unbounded positive/archimedean mixed blocks and prices the infinite negative leakage by the relative factor `epsilon/mu<5/51`. Therefore future positive-only source mixing campaigns must provide new information relevant to `N/G`, `DB`, an original signed cap, or the exact corrected Schur before claiming critical-path significance.

Separate mathematically incomplete requirements remain: [EF07](../notes/RPB108_EF07_GLOBAL_EVEN_WITNESS_20261017.md) original even bounds, [CC27](../notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md) original native full 16-block residual coupling and defect-relative covariance, independent Fourier/form domain identification, and the actual zeta global bridge. Neither odd sign alone nor a finite positive source witness implies RH.

## C. Quantitative gap table — what is actually known

| Obligation / exact gate | Strongest accepted input, within explicitly stated scope | Quantified deficit / obstruction | Missing information |
|---|---|---|---|
| Positive pole-corrected original odd `Astar >= kappa_star I` | SM19: `kappa_star=33621/10^9`; inverse pole reference `2<s,C14^-1 s><=0.966379<1` | **CLOSED** under inherited original-realization assumptions. Pole Schur clearance `1-0.966379=0.033621` and `Sstar>=kappa_star^2 H` | Independent original operator/form/domain attachment for RH-facing transfer, not another finite SPD check |
| Entire odd complement | SM32 `Wodd|F>=17/25000 I`, SM33 `epsilon<1/15000` | `epsilon/mu < 5/51≈0.0980392`, enough for SM34 **conditional** `theta=51/56≈0.9107143` | Actual full 470D finite signed energy-dual `N<=theta G` or exact 470D corrected Schur |
| Complete finite negative-response `N<=theta G` | Exact SM34 operator identity and criterion; G,N actual original 470D **unmeasured** | No certified global 470D generalized eigenvalue interval: **numerical deficit undefined**, not 0 | Complete original `Astar^-1 J` response and all Kminus cross moments; possibly sharper direct signed Schur |
| MG07 full matrix gate with `DB=R*B14^-1R` | Exact SM19/MG07 Woodbury and Galerkin identities; no physically accepted 470x470 `G0,N0cap,DB` jointly assembled | With `Hminus=82.71043570625`, `Hminus/kappa_star≈2.4600826e6`. For t=1, the DB coefficient is **≈4.9201651e6**. If `N0cap<=theta G0/4`, residual budget `DB<=theta*kappa_star/(4Hminus) G0≈9.254916e-8 G0` is a **conditional tolerance**, not an achieved bound | Matched 470-source original Galerkin Z, physical/cross negative cap, and whole-frequency residual D,F,pole Gram |
| SM35 scalar residual alternative | Hminus/kappa_star² ≈7.3171011e10 (t=1 factor ≈1.4634202e11). Under SM35 stated cap assumption, `D=R*R <= theta*kappa_star²/(4Hminus)G0≈3.1115953e-12 G0` | Huge conditional required contraction, **not** an observed residual | Directional preconditioning or directly bounded Kminus-weighted error; no inference from Sstar positivity |
| Existing full negative cap feasibility | SM10/37 actual 890-source/infinite PSD cap; SM36–SM38 **noncertifying 25-source floating pilots** yield cap generalized ratios ~9.8–10 vs direct sampled ~0.96–1; target theta≈0.91 | This is a warning of cap inflation, **NOT a certified 470-source deficit**. SM29 true 13-positive-band reference with remote negative packet is a restricted-method no-go; neither proves failure of original Wodd | A matched **exact original** 470-source cap-vs-Galerkin energy comparison; if failed, new original Kminus enclosure or trial geometry |
| MG43–MG55 original 24D residual *certificate method* | MG43 source-bound blending did not close contraction. MG53 optimistic zero-[0,8] full measured-band Rayleigh remains negative ~−0.77 to −0.87 on four fixed source cases; MG54 symmetric inherited source budget threshold `h/(d+r)` ≈0.288–0.295. MG55 convex changed-response family has a common exact negative source-coordinate witness | **Proved method-family ceiling for fixed response/remainder and tested convex hull**; hypothetical zeroed bands are NOT valid physical residual uppers, only no-go comparators | Genuine new complete whole-frequency coupled G/S residual architecture, source/trial geometry, or different cap; additional same-cell refinements cannot repair this fixed family |
| MG57–MG67 positive strong-action source restrictions | MG57 1D; MG62–63 independently positive 2D restricted planes; MG64/65 finite 3D scalar method 0/252; MG66 global source-error sign 7/24 SPD, MG67 cone improvement 18/24 strict source orthants with 6 failed conservative envelope cones | Qualitative full24 Sstar SPD follows already from `Astar>=kappa_star I` and F independence; **no proof that these source-local lower estimates improve N0cap, DB, theta or G0**. MG64 best scalar L/E≈0.10199 is a **method-specific** 3D deficiency, not a signed spectral deficit | A precise Loewner implication to original `DB` or negative cap on the SAME 470-source response, not another source rank test |
| Original even | EF07 same-vector original negative-cap enclosure `[0.802331,1.019889]` vs positive-even enclosure `[0.462976,2.639461]` | Overlap; signed difference interval `[-1.837130,0.556913]` includes 0, so **INCONCLUSIVE** | Tighter original even complete signed operator comparison or structural parity transfer |
| Original native CC27 / global bridge | CC27 exact arithmetic native kernel, mixed signs and existing critical-equation cancellation; no defect-relative residual bound `J M_t^-1 J* <=(1-delta) Lambda G` with cap-only reserve | Existing cap-only bound behaves as `1/m` as minimum critical defect `m->0`, so **no uniform reserve established**; simple fixed-sign and only-new-prime forcing methods eliminated | Actual critical-row joint defect-relative covariance including ALL arch/prime/pole cross terms, then original form-domain/zero-side transfer |

**Quantitative discipline:** the MG07 target is a matrix **Loewner** comparison on the entire 470-dimensional original source space; a diagonal, 24D isolated source lower, matrix TRACE decrease, one Rayleigh direction, or a scalar residual constant on another source family is not a substitute. In particular, the true 470D signed deficit cannot be numerically computed while `G0,N0cap,DB` on the SAME original trial are missing.

### Newly isolated source-domain sublemma (conditional; no signed gate)

The original SM35 470 generator functions are zero-extended compactly supported odd polynomial sine/cosine sources and the genuine supported sinh(x/2) pole. [The October 23 domain lemma](../notes/RPB108_ODD470_STRONG_DOMAIN_20261023.md) explicitly pays the endpoint jumps and proves an exact whole-470 scalar high-frequency multiplier-action bound S_(o,|xi|>=1) <= 650 sum(C_j^2) I470 using SM41's original a_o(xi)<=17+log|xi|. Together with bounded low frequencies, this establishes strong-domain source membership **under the claimed supported Fourier-form realization**, not independent identification of that realization with the actual original Weil form. The bound is extremely coarse and does not improve the required MG07 same-trial negative-cap or residual slack. An exact-rational geometry/envelope replay is included in critical-path CI. No theorem-status changes.

## D. Why dimensional strong-action expansion does not enter the controlling inequality

With an original strong-domain physical source F and any rational matrix B of compatible dimensions:
```
H=F*F, G=F*Astar F, S=(Astar F)*(Astar F),
R=F-Astar F B,
R*R=H-G B-B*G+B*S B.
```
For a FIXED B, a certified `S >= L` yields a **lower**, not upper, estimate for `B*S B`, so it cannot reduce the needed `R*R` upper. A nonzero positive spectral subspace of S also does not bound `Astar^-1 R` in the original B14 metric or improve the complete 470D negative response. An improved *upper* for S, improved correlations among G,S on the same original trial, or explicitly certified residual geometry could enter. A source positivity lower could aid numerical conditioning of least squares, but a usable Galerkin residual upper STILL requires a complete, independently evaluated `R`.

Even taking optimal formal least-squares `B=S^-1G`, the minimized residual `H-GS^-1G` is not bounded **above** from `S>=L`: inversion reverses the order, giving `S^-1<=L^-1`, hence `H-GS^-1G >= H-GL^-1G`. This is the wrong inequality orientation. Also, positive `S` does NOT imply source-subspace invariance or a full inverse of Astar.

The only source-to-critical-path implication available from SI29 is its already-used GLOBAL operator coercivity/inverse order `Astar^-1<=B14^-1<=kappa_star^-1 I`. Further local Sstar positivity does not strengthen this global inverse statement without proved full-domain range/complement control.

## E. Research-front decision

**SUSPEND** dimensional-strong-action positivity expansion as an active RH critical-path front. **RETAIN** MG57–67 artifacts as verified constructive finite-frequency data and method-specific obstructions. Continue them only upon an explicit matched-residual or signed-cap dependency showing a quantitative source-bound effect.

**REDIRECT** the active original odd effort to the SM34 energy-dual 470-source inequality with an MG07 matched Galerkin/cap feasibility **preflight**. This uses the established full positive cross cancellation and certified infinite complement rather than attempting to reconstruct them through ever-larger local positive source matrices.

Comparison:
1. Full-spectrum original `R=J-Astar Z` and `DB`: **necessary for MG07 computational route**; candidate if feasible matched negative cap. Strong-domain and actual high log-frequency tails mandatory.
2. Better original 470-source approximation geometry: valuable ONLY if it materially increases `G0` relative to the negative cap and/or decreases verified complete `DB`; not automatically from extra source dimensions.
3. Joint original positive/negative-frequency control: promising when the 890-column cap is too conservative. A directly certified `J*Astar^-1 Kminus Astar^-1 J` or exact signed Schur may bypass the MG07 source-cap failure, with all finite/infinite terms included.
4. Inverse-resolvent/positive-energy-dual structural method: **SM34 already removes the entire positive mixed cross**, so prioritize its finite acceptance over reproducing another componentwise positive proof.
5. Native CC27/Weil transfer and even sector remain parallel genuine theorem obligations; neither is a consequence of the odd finite matrix alone.

## F. SINGLE next mathematical obligation — matched full-odd 470-source cap-only feasibility preflight

**Precise statement (method-specific necessary gate, not a necessary condition for Wodd itself).** On the exact original SM35 exceptional 470-source synthesis J, construct ONE genuine finite strong-domain `Astar`-Galerkin trial Z and the complete original certified
```
G0=Z*Astar Z >0,
N0cap=Z*Kcap Z   (includes SM10/37 full negative-frequency
                 890 Taylor columns, all cross terms and infinite eta).
```
Certify via complete exact rational Loewner data that
```
                  Delta0 := (51/56)G0-N0cap >0.
```
This is a **necessary preliminary feasibility condition for the fixed Z/cap MG07 route** because for any t>0 and any DB>=0 the left side of the target is at least N0cap. It is NOT necessary for the true original signed operator to be positive; the upper cap may be much too loose or Z poorly chosen.

**Proposed implementation:** Before computing a prohibitively precise full 470-column residual, choose an original physically supported trial family V including J; certify the complete original 470×470 Astar stiffness G0 (whole archimedean/high-frequency logarithmic tail and true pole). Independently build the matching `N0cap` with all original 973 negative leaves, 890 source moments and eta correction, on the EXACT same Z. Compute an exact generalized eigenvalue upper `x=lambda_max(G0^-1/2 N0cap G0^-1/2)` by rational Loewner/LDL tests, reporting the full cross terms. An exact rational source vector v with `v*(theta G0-N0cap)v<=0` is a **stopping witness for this fixed cap/trial** even without DB; it is not a negative witness for Wodd itself.

**Acceptance:** complete, independently replayed original physical `G0,N0cap`, source domain and full-frequency accounted; exact rational strictly positive `Delta0` and a **quantified normalized slack** `Delta0>=delta G0`, `delta>0`. Then, and only then, begin a complete `DB` construction on the SAME Z and search a SINGLE rational t>0 satisfying MG07 in Loewner order. On each normalized coefficient ray with `x=N0cap/G0` and `y=(Hminus/kappa_star)DB/G0`, optimizing t separately gives the necessary (NOT sufficient for uniform t) condition
```
                   (sqrt(x)+sqrt(y))^2 <= theta.
```
Thus if `x>=theta` on a certified ray, no residual improvement alone can rescue the present method. If `x<theta`, even the best raywise t requires `y<=(sqrt(theta)-sqrt(x))^2`; a common t must still exist for all rays.

**Failure criterion:** An exact negative/zero `Delta0` witness after valid physical matrix assembly means abandon further MG57–67-style local source-strong lower refinements as a way to rescue THAT fixed cap and Z. Move to sharper true-original negative cap, different original trial geometry, or direct actual finite energy-dual signed Schur. If `Delta0>0` but feasible DB margin is not within measured reach, quantify the relative residual deficit and change inverse/resolvent or joint-source geometry rather than iterating Fourier subcell counts.

### Exact SI10 negative-support mass tightens independent original signed-ray high tail >20x

The exact-rational refinement now also integrates 1/xi² over the true original support leaves individually, producing S32=2Σ(h+κ)(1/max(32,a)−1/b) with 0<S32<M32/1024<M_SI10/1024. The true signed-ray high negative tail is now β32²*S32, strictly sharper than the global support mass bound, and is exact on the inherited frequency cover. The standalone original SI10 973-leaf/107-component negative-frequency complement already establishes the true complete signed-frequency Knegative upper mass M=1204033883/32000000<38. For the TRUE physical two-source rays with previous exact Fourier |T_f(xi)|<=beta32/|xi| at |xi|>=32 and (-m)_+<=Knegative, the entire high negative contribution to original Wodd=m(D)-2ss* is at most M beta32²/1024. Old all-real uniform SI06 bound charged M0*2beta32²/32. The new exact support-weighted bound is >20 times sharper WITHOUT changing the 2240-cell low32 method-stop criterion or 470 original source dimensions. This is a separately verified original signed-ray positivity *input*, not universal odd-operator positivity. [Exact independent replayer](../scripts/validate_rpb108_mg07_original_signed_supported_tail.py) is now a required input to the low32 CI. No strict original signed-ray lower or method STOP is accepted until the actual 2240-cell rational run passes.

### Oct 24 implementation: full-original exact low32 integrated signed method-stop attempt (CI not yet passed)

A dedicated complete-original strict scalar test now exists at scripts/validate_rpb108_mg07_two_source_original_low32_affine_stop.py. Retains full original SI10 cluster0 rational sine+true sinh pole rays, every original signed seven-prime and quarter-digamma point via rational Euler gamma H1024-log1025/H1024-log1024 with 64-term positive digamma series and integral tail; each real cell signed m interpolated affinely with entire SM40/SM43A curvature fee. Exact SM42 true sine-pole Fourier T(mid),T'(mid) and full physical second-moment cap enclose squared Fourier on each entire real cell. Signed w97(m) is 1-Lipschitz, affine on sign-stable cells; all kink-ambiguous cells use separate rigorous floor. Exact integrated affine multiplier x squared affine source with interval errors pays every term; 2240 full cells [0,1]/256 and [1,32]/64, then original pole+high-log tail. Strict positive lower would prove Knegative(f)>97/100 Astar(f), thus obstruct ONLY the J-only Ritz/SM40-cap sufficient method because verified original theta_SM40<97/100 and SM40 Kcap>=Knegative. No proof status unless the dedicated 90min focused Actions workflow passes (rigorous fail-closed); preliminary float evaluation of same conservative error formulas positive ≈+3.5m direct and +0.22m cap is NONCERTIFYING. No full original signed odd/even/Weil/RH promotion. [Derivation and CI](../notes/RPB108_MG07_TRUE_LOW32_AFFINE_METHOD_STOP_20261024.md).

### New EXACT original 2-source pole/high-tail input reduces remaining method STOP to low-frequency [0,32]

Preserve two different archived original rational J470 source candidates: SI10 cluster0 physical sin(2π(37/64)x) combined with genuine sinh pole s, direct Knegative ray (a,b)=(12001,16384) and separate SM40 cap ray (3013,4096). Original SI18 complete true physical two-source Gram and SI12 sinh pole Taylor interval prove exact ||f||², <f,s>, 2|<f,s>|² (including every sine-pole cross). SI14 phase-reduced **signed** sin(2πcB)+sinh(B/2) cancellation gives |f_direct(B)|<425 and |f_cap(B)|<97, with endpoint derivatives rigorously bounded. Two real supported physical IBPs, second derivative L1, and original SM41 ENTIRE high-log a_o<=17+ln|xi| certify the original whole-frequency positive FORM tail above cutoff **32** <264000 direct / <15700 cap, relative <11/10000 true ray L² energy. At cutoff2048, <500 and <26 and squared-strong tails <1/20000 of true ray norm. This reduces the required original whole-real rigorous low-band scalar integral to [0,32] instead of [0,2048], a 64× shorter coverage. SM40 exact sharp theta now asserted theta<97/100. Since Kcap_SM40>=Kneg, a strict original scalar 0..32 cell certification Kneg_low_LO−(97/100)Ao_low_HI>(97/100)(Tpositive_hi−2|<f,s>|²_LO) on ONE ray is enough to STOP the fixed J-only Ritz+SM40 sufficient method, not enriched Galerkin or true signed positivity. Implement that with SM43A crossing-safe affine signed multiplier and SM42 true sin/sinh Fourier transforms. Low band BOTH energies OPEN. [Proof and exact Fraction scripts](../notes/RPB108_MG07_TWO_SOURCE_EXACT_PHYSICAL_POLE_AND_LOW32_20261024.md).

### Oct 24 returned exact SM40 theta and actual rational two-source feasibility probe

The 107-cluster/3892-cell fully paid original SM40 sharpened complement CI has completed SUCCESS (40071136137), giving **theta_SM40=0.9699135819561749** on the unchanged original 470 source map and complete original signed negative frequency subcells. Original MG07 finite residual algebra regression SUCCESS (40071136586) is NOT the full 470-source operator certificate. The original 25-source numerical SM40 cap-ray CI SUCCESS (40071136256, discovery ONLY) selected f=12001*sin(2pi*(37/64)x)+16384*sinh(x/2), Kneg/Astar~0.996..0.9997 (<1, >theta). First true continuous SI29 14-feature pole-aligned augmented MG07 local numerical solve (rank truncated SVD 10–13 out of nominal 16 for this 2source+14 setup, NOT the actual full 484D trial) finds Kneg/G~0.9964..0.9991 and squared strong residual/G~4.4e-4..5.9e-4, while theta*kappastar*kappa/Hinf≈2.618e-9. Therefore pursue a **rigorous one-ray method stopping certificate** instead of more formal scalar-tail sharpening: certify the same rational source f under complete original Astar and SM40 cap, both with original real-frequency interval payments. J-only Ritz can be rejected by exact Ccap(f)>theta Astar(f); AUGMENTED Ritz requires its full true trial response, not the truncated numerical one. Never infer negative original odd direction or RH failure. Original critical-path audit initially failed schema on 34 custom active role values; canonical roles repaired without altering research scope. [Oct24 numerical/noncertifying audit](../notes/RPB108_MG07_AUGMENTED_TRUE_SI29_TWO_SOURCE_FEASIBILITY_20261024.md).

### Pole-aligned true SI29 Jensen trial preconditioning: remove boundary jumps without changing original span

The 14 TRUE continuous SI29 augmented-trial features g_j are odd and generally nonzero at support endpoints x=±B, causing an O(1/|xi|) Fourier tail. Since s=sinh(x/2) is a true original column of J470, define h_j=g_j−(g_j(B)/s(B))s. Every h_j vanishes EXACTLY at both endpoints and span(J470,G14)=span(J470,h1..h14). A full Astar-Galerkin response and residual are invariant under this change of finite trial basis; 4D Fraction toy explicitly checks the equality, while leaving true SI29 reference B14 unchanged. Two exact physical IBPs give O(1/|xi|^2) with all derivative boundary, interior g'' and sinh-pole payments. Exact center-phase distance bound |g0(B)|<=min(1,pi_up dist(2cB,Z)) for original Jensen means and |g1(B)|<=2pi_up r B for the true odd moments produce complete 14D high-frequency squared Ao-action Loewner upper <7.5e-5 at Λ2048 and <1.4e-6 at 8192 (conditional on SM41). This is ~1.9 million times smaller than the old coordinate tail bound 143, but is NOT the actual MG07 strong residual or its Loewner margin. Build 484-trial original cross/action covariances in this endpoint-zero basis, retaining all 470 source cross directions. [Exact original proof](../notes/RPB108_MG07_SI29_AUGMENTED_TRIAL_20261023.md).

### Young discriminant before any 484-column full-original interval build

After SI29-feature trial enrichment makes D_B=κ^-1 R*R, the original MG07 loss Hinf/(κstar κ)≈3.7047e8 remains. For an actual rational original 470-source ray, set n=Z*Kcap_SM40 Z, d=(Hinf/(κstar κ))R*R, g=Z*Astar Z. A single t>0 must satisfy (1+t)n+(1+t^-1)d<=θg. Its *per-ray* inf over t is (√n+√d)². Exact strict feasibility is Δ=θg−n−d>0 and Δ²>4nd. A rigorously failing ray rejects the selected enriched Galerkin/cap sufficiency route even after optimal t; it does not rule out original signed positivity, a different cap, or a different trial. At paid θ≈0.933564 the necessary D/G0 is <2.5200e-9 (before negative cap); this should be the first numerical/interval feasibility diagnostic. No original source ray n,d,g has been enclosed yet. [Exact-regression implementation](../scripts/validate_rpb108_mg07_augmented_young_ray_gate.py).

### Source dimension 470 vs Galerkin trial dimension up to 484 — a NEW exact option

The 470 original sources E0=ran(J) **must not change** in the SM34 exact signed-energy-dual criterion. But the separate Galerkin approximation of Astar^-1 J need not use only V=ran(J). With actual 14 SI29 reference features G, choose V=ran(J)+ran(G), dimension at most 484 after independent basis reduction. Galerkin gives J*R=G*R=s*R=0; thus exact entire SI29 B14 R=κR and R*B14^-1 R=κ^-1 R*R. This removes *all* positive-reference Woodbury and pole-inverse residual terms by enforcing residual orthogonality rather than estimating them. The full 470-source MG07 bound becomes (1+t)Z*Kcap_SM40 Z + (1+t^-1)Hinf/(κstar κ)R*R <=theta Z*Astar Z. The larger κ^-1 residual factor need NOT be smaller for arbitrary old R, and the enriched full physical strong Gram has not been built. The original SI29 14 features are TRUE CONTINUOUS frequency Jensen means (12) and first moments (2); finite rational Simpson-node sums are QUADRATURE approximations, not the positive-reference vectors. A first strong-tail validator mistakenly substituted these surrogates and was repaired. The corrected exact variation bound uses continuous |w| masses 1 and 3/2 and |frequency| moments c and 3c/2, proving finite whole high-frequency strong-action tail for all 14 true SI29 vectors conditional on SM41/SI06 original domains. The 14D tail upper 143<ΣU_j<144 at Λ2048 is only domain-admissibility, NOT a practical MG07 residual bound. This makes SI29-feature-enriched Ritz a live alternative even if the original J-only SM40 cap-ray test fails. [Exact algebra, domain handoff and open gates](../notes/RPB108_MG07_SI29_AUGMENTED_TRIAL_20261023.md).

### A whole-real supremum replaces the obsolete negative trace norm in MG07

Use the SI06 **all-seven-prime-powers** uniform m(xi)>-CONST_UP-TWOC, CONST_UP=4707/875 and TWOC<70751/10000, to obtain **the exact original whole-frequency multiplier bound** Kminus <= Hinf I with Hinf=871887/70000≈12.455529. The original Fourier zero-extension is isometric, so its compression does not increase this norm. The accepted original MG07 noncommutative inequality now uses (1+t^-1)(Hinf/kstar)R*B14^-1 R, replacing even the repaired coarse 82.77732945625 global mass estimate and decreasing the reference-residual coefficient by factor >6.64. No sampled frequency input, new exceptional dimension or 890-cap perturbation is involved. This *does not* certify R, N0cap or theta*G0. [Whole-negative uniform certificate](../notes/RPB108_MG07_GLOBAL_NEGATIVE_SUP_20261023.md).

### Required correction to the inherited SI10-to-Kminus transfer

A critical audit found the old SM33 QKminusQ leakage and whole Hminus global norm missing the +kappa cost when passing from SI10's h>=(-m)+ to Kminus=(kappa-m)+. The canonical original 107 b9 cluster moment mass must be Mj_full=Mj_h+2*kappa*cluster width, including all original reflected unresolved leaves. The corrected original SM33 arithmetic now enforces its OLD legacy epsilon_h<66247/1e9 and corrects epsilon_full by adding strictly positive kappa weights, still below 1/15000 (using 2B*kappa*W*2^-18), with global Hminus=82.77732945625<83. Sharper e_max<16813/1e7 additionally bounds Hminus*epsilon_full<11/2000 and its inverse correction <81/10. SM34/SI29/SM35/MG07 downstream acceptance depends on REPLAY of these amended exact validators, not historical green CI. See [proof-accounting erratum](../notes/RPB108_SM33_KAPPA_LEAKAGE_REPAIR_20261023.md).

### Newly available full-infinite Schur threshold, no extra source dimension

The old `51/56` threshold is NOT an intrinsic stopping barrier: on F=E0^perp the true pole is orthogonal, Ao>=kappa=1/1000 and the certified entire Q Kminus Q<=epsilon imply the stronger full signed complement D_F>=kappa-epsilon. SM34's **same** exact energy-dual Schur then admits theta=1-epsilon/kappa, strictly above 14/15 from epsilon<1/15000; no new Taylor/source generators needed. The exact original SM40 refined cell weights may further reduce epsilon via h_eff=min(h_SI10,w_SM40), preserving all original 3892 subcells and source b9 cluster errors. A focused exact rational validator was added; its theta_eff decimal is NOT accepted before PASS and independent domain audit. The canonical J-Ritz cap and complete residual source gates should use the strongest actually certified theta, rather than forever assuming the superseded 51/56. [Detailed derivation](../notes/RPB108_SM40_SHARP_ODD_COMPLEMENT_THRESHOLD_20261023.md).

### Method obstruction hierarchy for the canonical J-Ritz trial

First seek a valid SM40 cap-only source ray, but simultaneously inspect the stronger real negative operator Kminus: if a rigorously certified original physical v has v*[(51/56)AJ-J*Kminus J]v<=0, **no valid negative upper cap** can rescue this particular J-Ritz threshold even if its cap conservatism vanished. The SM38/SM40 25-source direct noncertifying ratios ~0.965-0.973 exceed theta~0.9107 but remain below 1. This is compatible with positive signed Wodd: the obstruction may be the conservative 51/56 sufficient threshold rather than actual signed negativity. Prioritize exact physical ray enclosures and investigate sharpening the SM34 complement leakage/Schur threshold if direct obstruction is confirmed. Both numerical searches are NONCERTIFYING and no true original ray has passed the test.

### Correct original cap for stopping tests: SM40, not SM10

SM10's original 25-source numerical ratio around 10.86 was a superseded cap-inflation diagnostic. Reusing the SAME original 25 source trial, the certified operator upper caps SM37, SM39 and SM40 were progressively tighter, with NONCERTIFYING SM40 numerical max cap/Astar ratios 1.003132 (4096×4) and 1.012044 (8192×8), versus theta=51/56~0.910714. These values are too high for that sampled Ritz sufficient gate, but DO NOT certify a source ray or any original signed operator sign. Every initial original physical ray and full MG07 gate must now use the SAME refined **SM40 exact entire signed-real 3892-subcell/107-block/890-Taylor-column negative cap and eta** as the data named in its test; negative results on old SM10 do not rule out SM40. See [SM40 certified negative cap note](../notes/RPB108_SM40_ENDPOINT_CURVATURE_SEVEN_PRIME_20261018.md) and [new SM40 ray-scout note](../notes/RPB108_ODD_CAP_RAY_SCOUT_20261023.md).

### Historical data: full SM36 pilot already warns of cap obstruction

The successful SM36 noncertifying 25-source original physical pilot (PR #217, Actions 39167260822) reported largest 890-cap-to-Galerkin-energy generalized eigenvalues 10.688198, 10.688195 and 10.863858 on three sample grids, versus the required theta=51/56~0.910714. By invertible Galerkin congruence, the EXACT counterpart would be the same generalized raw original source-stiffness/cap ratio. No rigorous original-ray obstruction is inferred from these float Fourier and Hankel observations, and no actual signed-odd witness is asserted. The current NF response is to search *small* rational original physical source combinations on the **same** cap with repeated samples, then rigorously bound upper whole Astar action and lower cap action on one specific rational direction before more residual work. See [pilot-ray discovery note](../notes/RPB108_ODD_CAP_RAY_SCOUT_20261023.md).

### Cap-only inverse elimination on the canonical source Ritz space

The source-space result extends to the entire MG07 residual: with P_J=J H^-1 J*, define E=(I-P_J)Astar J. Then J*E=0, R=J-Astar Z=-E(AJ^-1H), and E*E=SJ-AJ H^-1 AJ>=0, where SJ=(Astar J)*(Astar J) is the COMPLETE strong-action source Gram. Consequently, the FULL MG07 inequality for this SAME Ritz space is equivalent to (1+t)CJ+(1+t^-1)(Hminus/kappa_star) E*B14^-1 E <= (51/56)AJ, all in raw original source coordinates. This avoids AJ inverse in the decision but **not** the need for true entire-frequency SJ and correlated B14 feature/pole residual data. Source-positivity LOWER estimates alone do not bound E*E from above. 

The first natural 470D trial can be taken as the exact Astar-Galerkin response within V=ran(J), where J is the original SM35 exceptional physical source synthesis, H=J*J, AJ=J*Astar J>0 and CJ=J*Kcap J>=0. Since Z=J AJ^-1 H and Q=AJ^-1 H is invertible, the entire cap-only matrix is exactly Delta0=Q*[(51/56)AJ-CJ]Q. Thus the first same-trial cap-only positivity decision requires NO original inverse/residual computation: check (51/56)AJ-CJ>0 in the raw original source coordinates. A rational physical source v with v*[(51/56)AJ-CJ]v<=0 is a rigorous STOP witness for this **specific** original J-Ritz geometry and chosen negative cap; it is not a negative witness for true Wodd and does not exclude enriched trial spaces or a sharper cap. Full spectrum positive certification still requires all 470 coupled source coefficients and a normalized Loewner margin, and successful cap-only certification still requires matched DB and one uniform t.

See [the exact algebra and fail-closed ray analysis](../notes/RPB108_MG07_CAP_ONLY_J_RITZ_20261023.md). The new validator checks a noncommuting rational 3D toy and original 470/890 geometry, not the uncomputed original 470D stiffness or cap.

## G. Acceptance doctrine and stopping rules

A new calculation is a critical-path advance **only if** it (i) discharges an OPEN original theorem, (ii) improves an explicit term of the complete acceptance Loewner inequality on its exact shared 470D source/response, (iii) proves a precisely scoped method-class impossibility, or (iv) supplies concrete original-operator domain/inverse/covariance data indispensable to one of those gates. Otherwise archive it as exploratory.

1. **Stop qualitative source rank work.** Under SI29/SM19 and the actual strong domain, the full finite original source Sstar positivity is already analytic. No new source dimension or favorable trace is an acceptance event.
2. **Stop at cap-only obstruction.** If `Delta0` is not strictly positive on an exact original source vector, do NOT pay for finer `DB` under fixed Z and original cap.
3. **Stop at method-family ceiling.** MG53–55 already block fixing a frozen response/remainder by separately perfecting local original direct-frequency/remaining-frequency covariances. Any restart must CHANGE the response or whole-source coupling and prove which old no-go premise is broken.
4. **Stop at uncoupled full-frequency loss.** If source energy and negative envelope are not evaluated on identical original physical sources, or pole/high-frequency/domain terms are not all paid, reject the result rather than extrapolating from 24D or 25D pilot data.
5. **Stop if the inverse-conditioning reserve is not useful.** Compare `DB` against the exact `(sqrt(theta)-sqrt(x))^2` raywise allowance. If best physically justified coupling fails to improve the controlling witness, pivot to a sharper original Kminus cap or direct SM34 finite Schur.
6. **Stop incorrect theorem promotion.** Never infer full original Wodd or RH from source positivity, one-vector signed Rayleigh, 3D cone success, CI, or an unverified formal/domain interface. Independent physical source/domain checks, complete even operator, global Weil transfer and CC27 remain separate.

No new numbered MG checkpoint is authorized or created by this audit. This document is an evidence-linked proposed governance reset; final mathematical acceptance still requires independently replayed original-operator certificates and human proof review.
