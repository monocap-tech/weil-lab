# RPB108 — DNE35 joint signed original source comparison

Parent: DNE34, `75f212e021c28be1094bdcd5b13e084b7f9cb320`, on `research/rpb108-direct-null-exclusion`.
Terminology: `docs/TERMINOLOGY_RPB108_DNE35_JOINT_SIGNED_SOURCE.md`.

DNE35 certifies both complete 12-by-12 joint signed source comparisons. The original high floor kappa=11/25 suffices when all actual source correlations are retained. Original all-high positivity extends from thirteen to twenty-four retained directions, twelve in each parity. The common physical guard is 1e-37. The other 88 retained directions and whole 1.06 positivity remain open.

The packet combines the four scaled tested columns and first eight frozen normalized remainder columns in each parity. All 288 complete source entries and every mixed original native entry are certified. No actual infinite inverse is evaluated, and no original high floor is sharpened. DNE34's separate scalar-credit target remains disproved; it is replaced here by the passing joint signed comparison.

| Certified quantity | Even | Odd |
|---|---:|---:|
| Complete joint source Gram | 12-by-12 | 12-by-12 |
| Original high floor kappa | 11/25 | 11/25 |
| Signed matrix kappa N12-G12 | positive | positive |
| Paid congruence minimum row margin, decimal display | approximately 0.99999999633 | approximately 0.99999999995 |
| Original Schur coefficient floor, decimal display | approximately 0.01121844689 | approximately 0.02545669483 |
| All-high physical gap, decimal display | approximately 2.80459279e-37 | approximately 6.36410979e-33 |
| All-high positive retained rank | 12 | 12 |

Every load-bearing inequality uses exact rational endpoints and the stored congruence. Decimal displays are summaries, not the certificate. Independent validation passes 9,229 exact rational checks. Historical guards remain unchanged on their original subspaces.

## Fixed physical trial frame and native border

The joint frame is Z12=(T4 S, X_[0,8)), where X=hatY U is DNE32's exact native-normalized remainder and S is DNE31's diagonal scaling. No physical high correction, native projection K, or selected polynomial is reoptimized. The exact masses and rational outward norms are recomputed for all twelve columns; native normalization is not used as a physical norm claim.

The original joint native matrix has blocks

    N12 = [ A_s                   (P_s-A_s J) U_8 ]
          [ U_8* (P_s-A_s J)*      C_8              ].

A_s and P_s are the authenticated refined original tested matrix and T4/W52 border. J is the frozen scaled native projection. C_8 is the DNE32 original native remainder congruence block. Every nonzero native mixed term is retained. The independent validator reconstructs this formula using exact rational interval arithmetic, independent of the producer's directed-grid matrix helper.

A separate rational congruence certifies N12 positive. This controls the distinction between a signed source-budget failure and a negative original finite native vector.

## Coherent complete original source Gram

The authenticated original source helper remains `dne23_dne16_source_input.py`, SHA256 `e4539b941f3768f177a469c68f58d34b11d3ea863247c14c1a6a59d81b2f91d8`. Primary regular order/precision is 360/600 and replay is 400/620. All twelve source polynomials share the exact translation-cell geometry, source order and common rational coefficient grid 10^-250.

The sources include harmonic terms, exact endpoint logarithms, regular archimedean convolution, the correctly signed pole and six prime powers {2,3,4,5,7,8} in both orientations. Every positive half-interval cell is integrated analytically, with reflection parity supplying the full physical aperture. Products use DNE34's exact signed integer convolution, whose coefficient bound is asserted for every product. Polynomial-log and log-squared moments retain the singular endpoint contributions. No sampled quadrature, endpoint deletion or partial prime list is used.

For every i,j, complete source integration and all 56 same-parity retained coordinates give

    G_N,ij = <s_N,i,s_N,j>
             - sum_(n<112) <s_N,i,e_n><s_N,j,e_n>.

The unmeasured high tail is included by the whole-source integral, not discarded. All 672 retained source-coordinate intervals per packet and every whole-source Gram entry are stored. The validator reconstructs every projection subtraction. The eight-column remainder principal block reproduces DNE34's source intervals.

Coefficient-rounding errors are bounded in physical L2 and added to

    eta_N ||Z_i||, eta_N=2a(550/19)(106/125)^N+3e-99, a=53/50.

If e_i is the total source L2 error and R_i the projected approximate-source norm upper, entry i,j receives the full error payment e_i R_j+e_j R_i+e_i e_j. Final interval storage rounds outward. Every replay original-source interval must lie inside its primary interval. The large physical norms of scaled tested columns are explicitly included.

## Signed high-floor comparison

The DNE34 scalar-credit allocation is already disproved on the frozen remainder. DNE35 tests the less conservative signed target

    H12 = kappa N12-G12, kappa=11/25.

It includes actual tested/remainder source correlations. A positive congruence for H12 implies positivity of the original Schur form after adding every original high vector. There is no separate remainder allocation r<c.

Floating-point generalized eigenvectors only select a nonzero rational trial. The stored paid intervals for its native energy, complete source energy and signed quadratic prove any failure. A negative H12 trial is a failure of replacing the actual high inverse by the uniform floor bound; it is not a negative Q vector and does not prove an original null exists.

For a positive principal prefix, midpoint Decimal LDL only selects a rational upper-triangular congruence V. Outward interval evaluation of V*H V must have strictly positive Gershgorin row margins. All entries, margins and retained-rank minors are independently checked. The certified prefix contains the four tested directions and an initial remainder prefix, so it contains DNE34's established prefix theorem rather than replacing it by a different positive subspace.

## Physical all-high gap

If V*H V>=m I, then H>=d I with d=m/||V||_F^2. Therefore the original high-eliminated form satisfies

    Q(f)-<Bf,H_F112^-1 Bf> >= Q(f)-||Bf||^2/kappa
                           >= (d/kappa)||coeff(f)||^2.

This uses the existence and boundedness supplied by the original positive high restriction. The true inverse is not evaluated. The source identity and physical L2 ledger attach Bf=P_F112 L_original f to the original mixed form.

Let M be the sum of exact physical masses of the prefix columns and T an outward upper trace of its original projected source Gram. Then ||f||^2<=M||coeff(f)||^2 and the high response z has ||z||^2<=T||coeff(f)||^2/kappa^2. Completing the original high square gives

    ||f+h||^2 <= 4(M+T/kappa^2)||coeff(f)||^2 + 2||h+z||^2,
    Q(f+h) >= (d/kappa)||coeff(f)||^2 + kappa||h+z||^2.

Thus the paid physical gap is

    min{ (d/kappa)/[4(M+T/kappa^2)], kappa/2 }.

The validator records each exact gap and a common rational guard below both parity gaps. Historical gaps remain unchanged on their original subspaces.

## Reproduction and standing

`materialize_dne35_joint_sources.py DNE32_CERTIFICATE OUTPUT.json` reconstructs the exact twelve-column physical frame and full original native matrix. `certify_dne35_joint_source_Gram.py PARITY --count 12 --output OUTPUT.json` computes its complete source Gram. Use DNE16_ORDER=360 / DNE16_PRECISION=600 for primary and 400/620 for replay. Encode exact JSON with deterministic gzip mtime=0 and base64.

Run `certify_dne35_signed_comparison.py PRIMARY REPLAY --output COMPARISON.json` in each parity. Run `validate_dne35_signed_source.py EVEN_PRIMARY EVEN_REPLAY EVEN_COMPARISON ODD_PRIMARY ODD_REPLAY ODD_COMPARISON --output VALIDATION.json` for independent rational validation. Custody authenticates all inputs, scripts and deliverables.

These are analytical original-source interval certificates and rational replay checks. They are not a Lean formalization. Whole 1.06 positivity, complete direct-null exclusion, all-aperture continuation, RH/F4/full transport and Lean remain open.

## Frontier decision

The signed original source comparison passes on the entire requested joint packet in both parities. Actual mixed source correlations resolve the obstruction created by separating the remainder into a scalar budget below the tested credit. This does not reverse DNE34's negative scalar-budget witnesses: both conclusions hold on the same frozen physical trial frame.

The twenty-four-direction retained span contains DNE34's thirteen-direction span and DNE33's ten-direction span. Its positivity includes every original infinite high vector. It is not the raw first twenty-four Legendre modes, and it is not whole E112 positivity: the exact retained projections are specified by the frozen joint packet.

The next immediate source obligation is to expand the complete signed comparison beyond the first eight remainder columns per parity while retaining all mixed entries and physical error payments. The full joint packet would contain four tested and fifty-two remainder directions in each parity. This stage establishes that an evaluated true high inverse is not necessary for the certified twenty-four-direction extension. Whether the original uniform floor suffices for the complete packet remains open; a sharper directional response remains available if a larger signed block fails.
