# RPB-108 — native coefficient dictionary and background form completion
Date: 2026-10-03
Parent: b382eecec14866087fc2760f65757d9838947a80

## Scope and terminology

This is a written deduction from the actual-zeta logarithmic construction and the retained RPB-24 background model. It constructs a form-space adjoint realization of the SAME reduced compensator coordinate, rather than postulating a new representation field. It is not Lean-certified and does not identify the independently parameterized current WD-T38 carrier.

- Linear analysis means an adjoint of complex-linear synthesis, with the inner product antilinear in its first argument.
- Multiplicity quotient means removal of duplicate-frequency coefficient directions with zero sum, using the inherited quotient Hilbert norm.
- Background form carrier means D(Q_B) with inner product Q_B(v,f), using the strictly positive closed background form already retained in RPB-24.
- Form completion means completion in this background norm, not completion in native ordinary L2.

Retained inputs are RPB-24's actual background realization, strict positivity A_B >= eta I on its stated window, its Green core, and signed reduced factor S=-TC. This pass does not establish those inputs for the present generic WD-T38 fields. The canonical logarithmic topology and explicit-formula extension are the written construction at b382eec.

## 1. Exact multiplicity and conjugation dictionary

Let F_f(z)=integral f(x) exp(i z x) dx and e_gamma(x)=exp(-i gamma x). For the first-antilinear L2 inner product, the complex-linear raw analysis coordinate is

    <e_gamma,f>_2 = F_f(conj gamma).

The order <f,e_gamma> instead gives its complex conjugate and is antilinear in f. RPB-24 section 2 writes the latter pairing; it is lawful as a scalar pairing but must be conjugated when interpreted as a linear analysis operator. This clarification does not change its diagonal Green congruence.

At an ordinate of multiplicity m, start with m orthonormal duplicate coefficient directions. Their normalized surviving vector is m^(-1/2)(1,...,1). Synthesis sends it to sqrt(m) e_gamma; adjoint analysis is sqrt(m) F_f(conj gamma). The other m-1 directions have zero sum and synthesize to zero. Therefore sqrt(m) is exactly the quotient-Hilbert normalization; m is the squared analysis weight. Conjugate ordinates have equal multiplicity.

For a nonreal pair gamma, conj gamma, use p=(e_gamma+e_conjgamma)/sqrt(2) and n=(e_gamma-e_conjgamma)/sqrt(2). Compared with the evaluation convention sqrt(m) F_f(gamma), conjugation swaps the two raw entries. After pair diagonalization this is the fixed unitary

    D = identity on positive channels, minus identity on negative channels.

D commutes with the coefficient signature, preserves selected/background projections, and preserves the signed diagonal and its polarized form. A real ordinate is fixed. Thus both linear conventions have exactly the same coefficient norms and closures, with the negative-coordinate sign recorded. If a signed compensator is expressed using raw evaluation instead of adjoint analysis, its negative input coordinates must also be changed: C_eval=C_adjoint D_-=-C_adjoint. Unit gain and reducedness are preserved. One may not change the analysis convention and retain an untransformed negative coordinate u.

This is direct quotient and pair algebra in the retained raw-column model. The retained source pin is Bombieri Lemma 10, printed p.210 and proof continuation p.213, recorded in docs/IMPORTED_SOURCE_PINS.md. The publisher PDF could not be retrieved in this pass; no claim of a newly verified primary-source normalization beyond that retained pin is made.

## 2. Green preconditioning has no extra diagonal weight

Write R=G^(1/2), where G is the self-adjoint Dirichlet Green inverse. For h in the dense native L2 copy,

    <e_gamma,h>_-1 = <e_gamma,Gh>_2
                  = F_(Gh)(conj gamma).

Hence native analysis is the above multiplicity/pair analysis of J h=G h; after unitary transport k=U h, the physical function is Rk. This is a physical Green map, not multiplication of the coefficient by q_gamma.

The concrete column dirichletProblemOneColumn is G e_gamma: its q_gamma exponential term plus endpoint-homogeneous corrections has zero endpoint values and satisfies L column=e_gamma. Self-adjoint Green transfer moves this whole column, including the corrections, onto the physical function. The scalar q_gamma alone is not an admissible replacement.

Consequently, in RPB-24's stated raw-column realization, native analysis has image E(H_0^1). The smooth core is contained in H_0^1 and dense in H_log; E is bounded in that topology by b382eec. Therefore

    closure E(H_0^1) = closure E(H_log)

in the SAME multiplicity-normalized coefficient Hilbert metric, with D inserted if changing the linear convention. This closes the raw multiplicity/conjugation/Green dictionary in that model. It does not identify an arbitrary generic synthesis P with those columns, nor turn the complex-symmetric Bombieri finite matrix into an ordinary Hermitian Gram.

## 3. Effective background analysis must use the background form

Raw positive analysis and effective background analysis are different. The latter includes all unselected negative channels. Keep RPB-24's notation

    Q_B = Q_full + ||Phi f||^2,
    D_B = T T* = R A_B R,
    S = R Phi* = -T C,
    C u perpendicular to ker T.

Here Phi is the fixed selected negative analysis in the same linear convention. The actual full multiplier-plus-pole form, its same-domain polarization, and the finite selected analysis determine Q_B. No unselected-negative term is discarded.

The retained strict positivity and the logarithmic Garding estimate make Q_B's norm equivalent to the logarithmic norm. Indeed Q_B >= eta ||f||_2^2, and

    ||f||_Hlog^2 <= K (Q_full[f] + K' ||f||_2^2)
                 <= K'' Q_B[f].

Conversely the actual symbol bound, pole bound and finite selected moments give Q_B[f] <= K''' ||f||_Hlog^2. Thus this complete background carrier has exactly the canonical supported logarithmic domain. These bounds use RPB-24's retained strict background positivity, not an assertion that Q_full is strictly positive at a unit-gain endpoint.

## 4. Construct the effective adjoint realization by completion

On the Green core Ran R define

    V(Rk) = T* k.

R is injective, so this is well-defined. Polarizing the retained form congruence gives

    <V(Rv), V(Rk)> = <v, T T* k> = Q_B(Rv,Rk).

Therefore V is an isometry from the Green core with its actual background form norm into coefficient space. Core density extends it uniquely to an isometry

    V : D(Q_B) -> (ker T)^perp.

It is onto: the range of an isometry from a complete space is closed, and its core image is Ran T*, whose closure is (ker T)^perp. This constructs the effective analysis from the retained concrete quadratic; it is not a new assumed source-identification field.

Reducedness now supplies a unique actual physical form vector

    f_u = V^(-1)(C u).

No premise Cu in Ran T*, H_0^1 membership, or spectral-product L2 is used. If a native adjoint preimage k with T*k=Cu is already available in this SAME model, uniqueness gives f_u=Rk. Thus this reconstruction agrees with an existing identified native witness; it cannot certify equality with an unidentified WD-T38 physical function.

The signed selected law is exact on the core:

    Phi(Rk) = S* k = -C* T* k.

Both sides are continuous in the same background/logarithmic norm, hence

    Phi f = -C* V f

on the whole form domain. The SAME C is transported. In particular unit gain C*Cu=u yields Phi f_u=-u, and u nonzero implies f_u nonzero.

## 5. Attach the endpoint mixed source identity in the retained model

For every v in D(Q_B), the full signed form satisfies

    Q_full(v,f_u)
      = Q_B(v,f_u) - <Phi v, Phi f_u>
      = <Vv,Cu> - <-C*Vv,-u>
      = 0.

This is a mixed null identity for every vector of the actual canonical endpoint logarithmic domain. The same-domain source diagonal and multiplier-plus-pole polarization from b382eec identify this with the actual endpoint arithmetic form. It uses the effective background carrier, rather than selected-only neutrality of raw positive synthesis. It is a written actual-model endpoint witness, conditional only on the already retained RPB-24 realization and positivity, not an attachment of the present generic Lean fields.

The weak background equation also identifies the constructed vector:

    Q_B(v,f_u) = -<Phi v,u>,

so f_u=-A_B^(-1) Phi* u. This is a consequence of the construction, not a substitution of a newly chosen vector for the current carrier.

## 6. Precise remaining attachment and enlarged-window boundary

The dictionary is settled for RPB-24's raw columns, and the background completion constructs an endpoint logarithmic adjoint witness with the unchanged signed reduced C. The current WD-T38 source H,P,C,k, physical carrier h, and extension map remain independently parameterized. No actual instance proving that they are this retained model has been located. Their identification is still necessary.

An endpoint identity on (-c,c) does not imply the requested frozen action vanishes for every test supported in (-a,a), a>c. The fixed physical zero extension must be shown to obey the enlarged same-domain mixed law with the retained enlarged compensator/extension. The form completion supplies no such persistence law automatically. Do not call endpoint mixed nullity enlarged central cancellation.

For the CURRENT carrier, spectral L2 remains unproved and unassumed. A vector reconstructed solely in the form completion has logarithmic energy; this does not supply log-squared Fourier energy. An independently identified native preimage would give H_0^1 and the stronger spectral route, as previously recorded, but is not required for endpoint attachment.

Once the actual enlarged central law is attached, consume neutralExteriorIntegralGrowthResidual_realizes_of_central immediately. It provides the locally integrable regular defect and certified boundary-removal/whole compact weak realization without spectral membership. Exterior, digamma and boundary work stay closed.

## Validation and next witness

Documentation-only, five additive/current file changes. No Lean declarations, manifests, workflows or historical notes changed; no new Lean certificate is claimed. Prior root certificate e1959d1c6858c092a7cc51511bf667b13812768e remains the unchanged-code certificate.

Next witness: identify the retained effective background realization and its form-completed vector with the actual WD-T38/current physical carrier; then attach fixed physical enlarged mixed nullity. Actual enlarged central cancellation OPEN; current-carrier spectral L2 OPEN; threshold bookkeeping CLOSED; F-4 NOT STARTED; WD-T40/RH unchanged.
