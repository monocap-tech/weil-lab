# RPB108 DNE46: improved original high floor and 87 retained directions

Parent DNE45: `a9eda40b874163be980da517d3dda87942f83533`.
Branch: `research/rpb108-direct-null-exclusion`. Terminology was registered
before load-bearing computation in
`docs/TERMINOLOGY_RPB108_DNE46_REFINED_ARCH_SHELL.md`.
Historical results and certificates remain immutable.

DNE46 raises the original infinite F112 lower floor from 603/1000 to
**647/1000**, and certifies **87 retained directions**, up from 85,
coupled to the entire infinite high space at aperture a=53/50. The complete
44-column odd packet now passes. The even packet has 43 positive comparison
directions and one remaining negative comparison direction. No original
negative vector or null mode is established.

## 1. Change the arch input, not just the prime weight

DNE45 proved that the fixed arch input 2.772351243732, minus any valid
GLOBAL prime norm upper estimate, could not exceed 0.613456223732.
That theorem remains valid for its stated fixed input. DNE46 changes the
arch input using the inherited original high-frequency Bessel and
archimedean multiplier estimates, with freshly checked rational cutoffs
and a finer shell partition.

For n>=112, the inherited depth-six positive-region Legendre/Bessel
comparator is valid while (2 a pi T)^2 < 112*113. Its polynomial
logarithmic-derivative coefficients are positive and decrease with n by
induction on the positive convolution and increasing denominators.
The associated envelope's integration rate is bounded below by

    225 - 2 sum_{j=0}^{63} c_j(112) y^(2j+2),

where y is an outward upper enclosure of 2 a pi T_max. DNE46 sets
T_max=67/4=16.75, obtains y<=111.55795513, checks y^2<112*113, and
computes a fresh rate >54.8293136579. The conservative rate **50** is
used throughout. The old T<=16 rate 75 is not reused beyond its scope.

The complete physical low-frequency mass upper bounds for F112 are:

| Cutoff T | Mass upper, decimal display |
| --- | ---: |
| 14 | 1.237339987e-9 |
| 15 | 4.778877750449e-6 |
| 16 | 0.002571270623643016 |
| 65/4 | 0.009014914485972449 |
| 33/2 | 0.02773342589322749 |
| 67/4 | 0.0746962951087725 |

Exact rational endpoints are stored in the certificate. Each bound sums
48 independently enclosed degrees 112 through 159, uses the first 12
positive damping coefficients and a 155-term positive exponential lower
series, and pays the entire remaining undamped geometric tail. Neither
frequency nor high degree is truncated without its error allowance.
The mass bounds below 16 are deliberately weaker than the old bounds,
since they use rate 50; the extra shells provide the improvement.

For b(T)=log T-7/(216 T^2), and these increasing cutoffs T_0,...,T_5,
the original archimedean lower is

    b(T_5)_lo - (b(T_0)_hi+27/5) rho(T_0)
      - sum_{i=1}^5 (b(T_i)_hi-b(T_{i-1})_lo) rho(T_i).

This is a telescoping step-function lower bound: each adjacent multiplier
increment pays a complete cumulative mass upper. All interval endpoints
are directed outward. The total shell payment is about 0.001853193196.
After the inherited signed two-cross-pole absolute allowance
16 a (a/2)^224/(112!)^2, the arch-minus-pole lower is approximately
**2.8164295563832886**.

Authenticate DNE43's independently audited complete prime operator norm
bound ||P||<43387/20000=2.16935. Subtracting it gives a strict original
infinite high lower >0.6470795563832887, certified down to

    Q_original(h) >= (647/1000) ||h||_physical^2,  h in F112.

This bound applies to the complete original form with all active prime
powers 2,3,4,5,7,8, both orientations, archimedean term, and original pole
allowance. The analytic inequalities are inherited from NF10 and its
CC18 comparator; see `notes/RPB108_NF10_COMPLEMENT106_HANDOFF_20261008.md`.
DNE46 independently evaluates the new cutoffs, admissibility, rates,
masses, logarithms, and shell arithmetic. It adds no new source integrals.

## 2. Preserve the old positive space and add two directions

The original DNE44 native N44 and projected source Gram G44 are reused
with their decoded hashes and passing source/subspace audit authenticated.
Set H=(647/1000)N44-G44. Start in the exact invertible chart formed by
DNE44's positive columns B_old and negative comparison columns D_old.
The new positive embedding begins with **exactly B_old**, followed by a
new rationally chosen direction. All mixed terms are paid by the fresh
congruence certificate. This proves inclusion of the full previous
85-direction space, rather than proximity between numerical eigenspaces.

| Parity | Old positive rank | New positive rank | Remaining comparison rank | Full comparison inertia |
| --- | ---: | ---: | ---: | --- |
| Even | 42 | 43 | 1 | (43,1,0) |
| Odd | 43 | 44 | 0 | (44,0,0) |

Positive and negative restrictions have independent interval-congruence
sign certificates. The combined embedding has exact rank 44. By inertia,
these positive dimensions are maximal for this particular sufficient
uniform-floor comparison. A remaining negative comparison does not imply
an original negative vector, and a basis change alone cannot remove it.

Exact physical coefficient columns, masses, full projected source trace,
and the infinite response allowance G/k are paid. The new physical gap
lowers are approximately 1.4042044025715023e-37 even and
1.8069395448934553e-33 odd. A common physical guard of **1e-37** applies to
the 87-direction span plus the entire infinite F112 space.

## 3. Validation and scope

The independent high audit passes **3,975** new exact rational checks.
It reconstructs coefficients independently, proves coefficient monotonicity
through the individually integrated degrees (the all-degree induction is
analytic), checks the fresh positive region and rate, rebuilds each mass,
uses an independent longer logarithm series, and authenticates the inherited
prime certificates. The independent positive-subspace audit passes **27,488** new
sign/rank/physical checks; the combined new count is **31,463**. It rechecks original native signs,
exact span inclusion, all compressed mixed entries, complete comparison
inertia, retained rank, physical coefficients, and the all-high gap.
Inherited audit counts are not counted as newly executed.

Reproduce from the repository root:

```sh
python scripts/certify_dne46_refined_arch_shell.py --output notes/data/RPB108_DNE46_REFINED_ARCH_SHELL_20261010.json
python scripts/validate_dne46_refined_arch_shell.py notes/data/RPB108_DNE46_REFINED_ARCH_SHELL_20261010.json --output notes/data/RPB108_DNE46_HIGH_FLOOR_VALIDATION_20261010.json
python scripts/certify_dne46_positive_subspace.py even --output notes/data/RPB108_DNE46_EVEN_POSITIVE_SUBSPACE_20261010.json.gz.b64
python scripts/certify_dne46_positive_subspace.py odd --output notes/data/RPB108_DNE46_ODD_POSITIVE_SUBSPACE_20261010.json.gz.b64
python scripts/validate_dne46_positive_subspace.py notes/data/RPB108_DNE46_EVEN_POSITIVE_SUBSPACE_20261010.json.gz.b64 notes/data/RPB108_DNE46_ODD_POSITIVE_SUBSPACE_20261010.json.gz.b64 --output notes/data/RPB108_DNE46_POSITIVE_SUBSPACE_VALIDATION_20261010.json
```

There remain **25 uncovered retained dimensions**: 24 outside the computed
packet (12 per parity) and one inside the even packet. The actual high
inverse has not been evaluated. Whole-aperture positivity, first-contact
exclusion, RH, and Lean remain open. The remaining packet direction still
requires a substantively stronger estimate; the 24 exterior directions
still require their complete original source correlations or another
certified collective bound.
