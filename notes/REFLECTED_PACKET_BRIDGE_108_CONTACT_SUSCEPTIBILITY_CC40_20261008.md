# RPB108 CC40 — Direct-null parity susceptibilities and exact low-mode contact diagnostics

Date: 2026-10-08. Branch: `research/rpb108-coupled-continuation`. Continue the [actual null equation and pole thresholds](REFLECTED_PACKET_BRIDGE_108_ACTUAL_NULL_PARITY_THRESHOLDS_20261008.md) after recovering Coupled's NF13 read-only handoff `e678c00433f9a9ca4812a2aa84ea53eeca53b08e`. **Classification:** valid rank-one reductions, rigorous low2-per-parity inequalities from pinned NF12 enclosures, explicit open arithmetic obstruction. No whole-a=53/50, all-cap or RH/F4 closure.

New deterministic provenance: [pinned NF12 low4 input](data/RPB108_CC40_NATIVE_PARITY_LOW2_INPUT_20261008.json); [exact Fraction validator](../scripts/validate_native_contact_parity_cc40.py). Original complete signed NF12 source at `research/rpb108-phase-geometry-localization`, commit `33d2b6bbd233d09e8c401b086545d0647b283817`; NF13 finite E24/E32 is independent read-only supporting progress, not silently imported as a source matrix. No other branch modified.

## 1. Parity form and exact moment constraints

Let H_a be the complete ACTUAL pole-free form: archimedean digamma symbol plus all active original prime-power translations in both orientations, omitting ONLY the original Hermitian pole cross terms. Let c(h)=int h(x) cosh(x/2)dx on real even supported h, and s(h)=int h(x)sinh(x/2)dx on real odd supported h. Then

    Q_a^e(h)=H_a^e(h)+2c(h)^2,
    Q_a^o(h)=H_a^o(h)-2s(h)^2.                       (1)

These are the original pole signs, not a shifted positive-level test. On any old cap where Q_a is strictly positive in the canonical form norm, H_a^o=Q_a^o+2s² is coercive. Hence define its pole susceptibility

    R_o(a)=2 sup_{0 !=h odd in D_a} s(h)^2/H_a^o(h). (2)

It is finite and nondecreasing as a grows through old-positive caps. Exactly:

    Q_a^o>0 in canonical form norm iff R_o(a)<1; 
    Q_a^o>=0 iff R_o(a)<=1                          (3)

on caps where H_a^o is coercive. This rank-one statement follows from Cauchy-Schwarz in the positive H-inner product and the Riesz representation of s; no source-shell inverse or old-gap denominator appears in its DEFINITION.

At a hypothesized first-contact a*, if H_a*^o remains coercive, an odd nonzero contact null h satisfies

    H_a*^o(h,f)=2s(h)s(f) for all odd f,
    R_o(a*)=1, and h proportional to (H_a*^o)^(-1) s. (4)

Here the inverse is only invoked under the stated positive-coercivity hypothesis. If H loses coercivity, a zero-moment pole-free null can instead occur: Q>=0 forces s(k)=0 on ker H. The latter MUST be addressed separately.

On the even side, define

    beta_e(a)=inf_{even c(h)=1} H_a^e(h).            (5)

If Q_a^e is canonically coercive, H_a^e is coercive on ker c, the constrained infimum is attained and beta_e(a)>-2. At a nonnegative contact, if its null h is even and c(h)!=0, the exact homogeneous equation gives beta_e(a*)=-2 and h/c(h) is a constrained minimizer. If c(h)=0, h instead belongs to a pole-free moment-zero null class, without forcing beta_e=-2. Under absence of such a class the even moment-carrying null space has dimension at most one. The odd case is analogous. The moment-zero obstruction cannot be discarded by manipulating an inverse.

Both extended-real constrained beta values are nonincreasing by support inclusion. These are variational reductions of positivity, NOT unconditional quantitative bounds on their full-cap values.

## 2. Actual low2-per-parity rank-one calculations, no square roots needed

At a=53/50, restrict to Legendre modes E_e=span(degrees0,2) and E_o=span(degrees1,3). NF12 pins exact outward 10^-25 rational enclosures for full signed Q, archimedean, primes and poles. Subtract only signed poles to obtain the pole-free 2x2 matrices H_e,H_o. Define the four exact determinants

    d_e=det(H_e)<0, d_o=det(H_o)>0,
    D_e=det(Q_e)>0, D_o=det(Q_o)>0.                (6)

These FOUR strict signs pass rational interval arithmetic. In particular H_e has precisely one negative and one positive direction, while H_o is positive definite. Also all four signed Q diagonal entries are strictly positive. Put B_e=D_e-d_e>0.

The determinant lemma for Q_e=H_e+2cc^T and Q_o=H_o-2ss^T, followed by constrained minimization, gives EXACT finite-Ritz scalar identities

    beta_e^(2)=2d_e/(D_e-d_e),
    beta_e^(2)+2=2D_e/(D_e-d_e),                 (7)

    R_o^(2)=1-D_o/d_o,
    beta_o^(2)=2d_o/(d_o-D_o),
    beta_o^(2)-2=2D_o/(d_o-D_o).                 (8)

The minima beta^(2) are on the indicated two-dimensional parity subspaces, and R_o^(2) is the corresponding finite positive-H Rayleigh supremum. No unproved infinite inverse or root of an interval pole moment is used: the determinants come directly from the SOURCE-PINNED rational intervals.

For display only, the determinant midpoints are approximately

    d_e=-0.846209689842261, D_e=0.000126775189252,
    d_o=+0.150920193131248, D_o=0.000963070155759.

The strict exact rational comparisons certify

    0 < beta_e^(2)+2 < 1/3000,
    0 < beta_o^(2)-2 < 1/75,
    149/150 < R_o^(2) < 1.                      (9)

The inequalities reduce respectively to

    6000 D_e < D_e-d_e,
    151 D_o < d_o,
    150 D_o < d_o,                             (10)

which hold using UPPER determinant interval endpoints on the left and LOWER denominator endpoints on the right. The independent direct-integer replay of these interval inequalities and source component overlaps passed 19 checks; the checked Python validator has been published for external execution, but no new CI/Lean run is claimed here.

For orientation only, the moment-one finite minimizers in Legendre coordinates are approximately

    even: (degree0, degree2)=(0.6681259,-0.3053484),
    odd:  (degree1, degree3)=(2.1991825,-1.3728591). (11)

They are finite constrained trial profiles, NOT generalized null vectors or solutions to Q(h,f)=0 for all f. These decimal coordinates are not used by the rigorous comparisons.

## 3. Interpretation and strict limits

Enlarging E_e or E_o can only DECREASE the corresponding constrained minima. Therefore

    beta_e(full,a) <= beta_e^(2)(a)<-2+1/3000,
    beta_o(full,a) <= beta_o^(2)(a)<2+1/75.      (12)

These are **upper bounds on the full infima**, not the lower estimates that would prove positivity. For an entire full positive cap, they would constrain the true reserves to very small intervals, but a whole cap at a=1.06 is NOT certified. R_o(full,a) is defined as a positive-H susceptibility only when H_o(full,a) is coercive, and cannot be inferred from a finite H_o>0.

The new NF13 E32 original SIGNED Q certificate adds finite positive directions, but does not give the complete original 112 retained native/source cross form, infinite mixed Schur positivity or global sign. NF10's genuine F112 positive floor and CC40's pole-free F112 consequence remain available, while the 80 remaining retained directions and their couplings cannot be suppressed.

The closeness of finite scalar trials to contact is NOT evidence of an actual zero off the critical line or imminent crossing. The harmless one-dimensional models

    H_e=-2+epsilon, c=1, Q_e=epsilon,
    H_o=+2+epsilon, s=1, Q_o=epsilon,

have arbitrarily small reserves with no null or negative vector. A genuine differential first contact and a full positive-level shifted contact likewise defeat any inference from rank-one susceptibility alone. RH and the precise arithmetic still must be distinguished by an independent inequality.

## 4. What the global Direct Null office now needs to prove

**Odd moment-carrying scenario:** Prove R_o(a)<1 for every finite original positive-H cap by a genuine original-prime/gamma/pole relation, not merely by assuming Q_o>=0. An alternative would show the rank-one Riesz vector cannot satisfy boundary saturation and the full native null equation at R_o=1.

**Even moment-carrying scenario:** Prove beta_e(a)>-2 for every finite cap by an independent constrained form bound; a local Ritz beta_e^(k)>-2 is only a finite statement. Test the special shape of the constrained minimizer against exact native mixed (not just diagonal) arithmetic.

**Zero-moment scenario:** Prove the pole-free constrained null equation has no nonzero compact-supported solution, for both parities, without assuming full original Q positivity on a larger cap. The preceding boundary-saturation lemma and native cutoff IMS identity are necessary inputs but not yet exclusions.

All three scenarios retain CC35's full positive-level control and CC19's genuine differential crossing as adversarial tests. These are **alternative proof obligations**, not the existing source-shell leakage estimate in disguise, though their all-cap conjunction is RH-strength.

## 5. Next measurable checkpoint

Extend the determinant/susceptibility audit to NF13's E32 **complete signed parity matrices**, using fresh locally validated native mixed entries or a source-pinned matrix archive. Evaluate the even pole-free inertia and conditional constrained beta_e^(16), the odd positive-H susceptibility R_o^(16), and whether any moment-zero Ritz channel approaches zero. Crucially compare the FULL signed Q to these quantities; do not infer whole-aperture positivity from them. If the E32 witness vectors concentrate in the same low Legendre modes, quantify that *without* assuming their full null equations.

The global counterpart must seek a signed arithmetic obstruction to the exact R_o=1 / beta_e=-2 contact equations, or prove the zero-moment class absent. Without a new independent arithmetic inequality these reductions remain equivalences, not a proof of RH.

## 6. Custody

New branch files are additive: pinned NF12 interval subset, exact Fraction validator, this report. CC39 and previous Direct Null reports remain unmodified; NF10/NF12/NF13 producer branches remain unchanged. No new all-cap positivity, zero exclusion, finite spectral gap beyond the actual low-mode statements, F4 transport, or Lean closure is claimed.
