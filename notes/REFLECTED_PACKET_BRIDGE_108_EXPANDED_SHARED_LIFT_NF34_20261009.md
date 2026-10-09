# RPB108 — NF34: expanded shared remaining lift

2026-10-09 UTC. Phase Geometry parent NF33 is
`6aea8f9a887db70fc56bfa6de6af691d9a8997f6`. Coupled CC76 was read only
at `938913512b851edfe14eb41fec23b5a7c472351c`. Definitions precede use
in the additive [NF34 terminology entry](../docs/TERMINOLOGY_RPB108_EXPANDED_SHARED_LIFT_NF34.md).
No other or paused branch is modified.

## Result

The shared rank-one expanded-shell extensions preserve positive original
finite energy on all 54 remaining columns per parity. Both previously
failing inherited witnesses now pass the complete-source floor test.

| Strict certified quantity | Even | Odd |
| --- | ---: | ---: |
| Physical expanded finite-frame gap | >5.2406e-22 | >3.5221e-19 |
| Additional correction norm | <2.1004e-12 | <4.3397e-11 |
| Expanded witness native energy | (5.2856349400,5.2856349401)e-22 | (3.5262578147,3.5262578148)e-19 |
| Complete projected source square | (7.5307195021,7.5307195046)e-23 | (4.8536889260,4.8536889261)e-20 |
| Source square / native energy | (0.1424752104,0.1424752105) | (0.13764418772,0.13764418773) |
| Inherited floor budget | 0.207 | 0.207 |
| Positive witness floor score | (1.6476061938,1.6476061951)e-22 | (1.1814805557,1.1814805558)e-19 |

The complete physical residual reconstruction error is below 6.812e-22
in both parities. The ratios improve from NF33's approximately 0.256075
and 0.209261, which both rejected the unchanged two-mode family.

Completing the original high square proves positivity on each
span(u32)+F, since u34 has the same retained component and differs only
by a high polynomial. The true directional retained Schur value is at
least the displayed positive floor score. Exact parity allows these two
new retained directions to combine with the entire original F. This is
a separate two-direction restriction. It is not a simultaneous
six-retained-direction certificate: the same-parity crosses with the
previous successful pair have not been certified for these new lifts.
Nor is it a complete remaining source-Gram certificate.

## A larger map shared by all remaining columns

The NF33 shared graph U33 has 54 independent retained columns in each
parity. Its two-mode shell is nearly suppressed, but its inherited
complete-source witnesses reject the scalar floor. NF34 retains that
entire graph and extends it through the expanded shell e116 through
e180 even and e117 through e179 odd, with step two.

Let a32 be the exact NF32 constraint vector and u32=T a32 its original
retained polynomial. The exact physical functional

\[
\ell(a)=\frac{\langle u_{32},Ta\rangle}{\|u_{32}\|^2}
\]

acts on every remaining column and satisfies ell(a32)=1. A single
expanded-shell polynomial z defines U34=U33-z ell. The inherited witness
is u34=U34 a32=u33-z. The retained range is unchanged and still exactly
orthogonal to the authenticated x and w. This is a shared rank-one
extension targeted at one retained direction per parity, not an optimal
lift on the entire remaining space.

The complete original source of u33 is paired with each expanded-shell
mode. The measured shell contains a fraction in (0.5012725214,
0.5012725223) even and (0.3983733753,0.3983733754) odd of its complete
projected source square. Physical source-error payments are included.
The coefficients of z are these midpoint source coordinates divided by
four, rounded downward to denominator 10^100. Selection is frozen before
the subsequent sign proof. There are 33 even and 32 odd added modes.

## Full finite-frame certificate

The complete original source of the small correction z gives its signed
couplings to every retained and NF33 high coordinate. If ez is its
physical source error, each original Q(U33_j,z) is enclosed by its
reconstructed pairing plus or minus ez times the exact column's norm
upper bound. The original Q(z,z) payment is ez times ||z||. All
archimedean, prime and pole terms are present in these pairings.

With b=Q(U33,z), the full finite energy and physical mass matrices are

\[
L_{34}=L_{33}-b\ell-\ell^{\mathsf T}b^{\mathsf T}
+Q(z,z)\ell^{\mathsf T}\ell,
\qquad
G_{34}=G_{33}+\|z\|^2\ell^{\mathsf T}\ell.
\]

The mass identity uses the disjoint retained, two-mode and expanded
shells. All 54-by-54 energy entries include the paid correction
couplings. A rational congruence/Gershgorin proof and inverse residual
row norm below one certify positive definiteness. The reciprocal of an
outward upper bound on trace(L34-inverse G34) gives a physical finite
frame gap. A separate validator reconstructs the full 58-coordinate
native graph before the rank-one update and verifies positivity with
an independent arithmetic order. No numerical eigenvalue is a proof.

## Complete source and directional high test

The new witness's original energy is the authenticated NF33 native
energy minus twice Q(u33,z), plus Q(z,z). The correction-source pairing
and reverse old-source pairing agree after physical error payment. Thus
a unit-mass approximate source is never used to establish the tiny
native energy directly.

The residual source is reconstructed as the old source minus the
correction source, subtracting the retained native midpoint coordinates
and the retained approximate correction coordinates. Projection
contraction pays the correction's source error once. The physical error
eta also includes the old source's uniform error and both retained
midpoint balls. For reconstructed projected source square s, the paid
complete square is enclosed by s plus or minus

\[
2\eta\sqrt{s_{\rm upper}}+\eta^2.
\]

The exact endpoint decomposition, regular kernel N320, degree40 pole
tail, all thirteen original prime translation cells, and every
arch/prime/pole source cross are preserved. Exact polynomial/log/log-square
moments use the outward rational grid of 500 decimal digits. Source
sampling and numerical quadrature are not proof inputs.

One reusable monomial source functional computes many normalized
Legendre pairings with outward arithmetic. Independent direct
polynomial-product pairings at both ends of the selected shell and at
retained/boundary coordinates verify overlap. The inherited old source
is also checked against the independent original N720/K620 signed native
pairing at e118 even and e117 odd. This archive check is on u33; the new
correction uses the complete-source symmetry and functional checks.

## Validation and reproduction

Independent validation passed. It checks exact retained membership,
physical masses, the shared functional and its value one on the inherited
constraint vector, every rounded correction coefficient, selected-shell
payments, all correction energy and source-square payments, source
functional overlaps, native bilinear symmetry and the inherited
independent native projection. Its separately assembled 58-coordinate
graph and rank-one update are rigorously positive; the resulting witness
energy overlaps both the producer's frame energy and its independently
paid bilinear energy. Python syntax compilation passed. Every displayed
strict decimal enclosure is checked against the rational certificates.

The exact NF33 trial and its separate complete-source certificates are
hash authenticated, alongside all original native and inherited parent
inputs. The new frozen trials and certificates retain rational endpoints,
correction source coordinates, bilinear payments and inverse proofs.
With the original parent inputs and archives staged, from the repository
root run the following for each parity even and odd (replace PARITY by
its lowercase name and TAG by its uppercase name):

```sh
python3 scripts/certify_native_expanded_shared_lift_nf34_106.py choose --parity PARITY --output notes/data/RPB108_NF34_TAG_FIXED_EXPANDED_SHARED_LIFT_20261009.json
python3 scripts/certify_native_expanded_shared_lift_nf34_106.py certify --trial notes/data/RPB108_NF34_TAG_FIXED_EXPANDED_SHARED_LIFT_20261009.json --output notes/data/RPB108_NF34_TAG_EXPANDED_SHARED_LIFT_CERTIFICATE_20261009.json
python3 scripts/validate_native_expanded_shared_lift_nf34_106.py --output notes/data/RPB108_NF34_EXPANDED_SHARED_LIFT_VALIDATION_20261009.json
```

## Next obligation and preserved boundary

NF35 should certify the new signed complete-source crosses with the
successful pair (v,t) and test the full three-by-three sufficient matrix
per parity. That determines whether the two new directional certificates
can join the previous four retained directions. Passing that test would
still leave the complete remaining shared-frame source Gram and its
collective coupling to certify. A failing matrix would identify a joint
floor obstruction requiring a further shared lift or sharper justified
response bound.

The prior four-direction restriction with all original F remains
certified. A positive finite graph and separately positive directions
cannot simply be adjoined. The full remaining source Gram, its signed
mixed covariance with the successful pair, and the full original retained
infinite-high sign remain open. Highest internally certified whole-domain
aperture remains 21/20=1.05; whole aperture 53/50=1.06, RH, F4 and Lean
remain open. Historical wording and paused fronts remain unchanged.
