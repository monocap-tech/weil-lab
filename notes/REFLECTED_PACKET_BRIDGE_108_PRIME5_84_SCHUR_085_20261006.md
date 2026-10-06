# RPB108: matched actual 84-source calculation at 17/20

Base: `2d7cdd44c4e2089c6b76e65067a34b1b798e767a`.
Definitions: [17/20 registry](../docs/TERMINOLOGY_RPB108_PRIME5_84_SCHUR_085.md).

## Lawful constructor extension

The physical aperture is a=17/20 and the matched finite basis and orthogonal moment complement use all Legendre degrees 0–83. Prime powers 2,3,4,5 are active; Lambda(4)=log(2). The nine-panel order remains valid because a<log(6)/2. Every endpoint logarithm, signed pole term, translation panel and mixed Gram term is retained.

The shared native constructor admits the new audited aperture only with degree 83 and matrix return. For its correlation length L=17/5, exact logarithm intervals verify exp(L)<30, exp(L)>5 and L<6. Consequently L/(1-exp(-L))<5L/4=17/4. Exponential order 260, Bernoulli order 230, gamma order 20, logarithm order 220 and the 400-digit outward grid remain adequate under the new checked ceilings.

The source length is d=17/10. Its 100 Bernoulli pairs have alternating, decreasing absolute coefficients. Pairing them bounds the polynomial between 1+ds and 1+ds+d^2s^2/3 on [0,1]; half its absolute value is below 17/8. Also d/2<1 and d<3, so the existing exponential and Bernoulli remainder estimates apply with the new ceiling. The source constructor retains exponential order 90, Bernoulli order 100, gamma order 50 and 220-term logarithms on the 400-digit grid. Coefficients are rounded to denominator 10^40 with the complete rounding budget included in the actual physical source error.

Both fresh native runs agree byte for byte, certifying finite margin 1/(32*10^18). Their outward 80-digit native matrix exports agree byte for byte and check all 7,056 inclusions, exact symmetry and odd parity zeros, and 84 shifted positive parity-block pivots. The full native output is reproducible by its constructor and identified by SHA256 and Git blob hash in the compact enclosure. Both fresh source runs also agree byte for byte, with aggregate physical L2 error approximately 1.4830912497142953*10^-36. The unchanged default quarter-window certificate matches the earlier helper, and three invalid constructor controls reject. Existing aperture formulas remain unchanged.

## Fixed-aperture damped complement

The previously proved spherical-Bessel inequality gives

\[
|j_n(x)|\le\frac{x^n}{(2n+1)!!}
\exp\left(-\frac{x^2}{2(2n+3)}\right)
\]

for n>=1 and |x|<=sqrt(n(n+1)). Its proof and physical plane-wave normalization are in [the 41/50 damping note](REFLECTED_PACKET_BRIDGE_108_DAMPED_COMPLEMENT_082_20261006.md). A rational proposal search selects T=259/20, q=177/200 and N=11; the exact three-part mass bound is then checked independently of the floating proposal. Its displayed mass is approximately 0.0007489047885094212 and physical lower bound approximately 0.5780254429325515, allowing c=23/40 and beta=40/23. No optimality is claimed. Both certificates reproduce byte for byte.

This finite-block split is superseded in the refined sign check by the following stronger integrated estimate. Its original certificate and full matching Gram are preserved.

## Integrating the damping degree by degree

For 0<s<=1, the elementary inequality log(s)<= (s^2-1)/2 gives

\[
e^{-zs^2}\le e^{-z}s^{-2z}\quad(z\ge0).
\]

Write Y=2*pi*a*T and z_n=Y^2/(2n+3). Applying this inequality to the squared Bessel bound, then integrating over s=|t|/T, gives

\[
\int_{-T}^{T}2a(2n+1)j_n(2\pi at)^2\,dt
\le \frac{4aT(2n+1)Y^{2n}e^{-z_n}}
{[(2n+1)!!]^2(2n+1-2z_n)}.
\]

The denominator is positive in the proved positive region: Y^2<n(n+1) implies 2n+1-2Y^2/(2n+3)>0. Thus no unproved Bessel zero estimate or divergent power integral enters the formula.

For exact interval application, use Y_upper in the numerator power and denominator rate, and Y_lower in the damping exponent. The reciprocal of the positive 61-term exponential Taylor sum gives an outward upper bound E_n for e^(-Y_lower^2/(2n+3)). Every integrated degree term is rounded outward and summed on an 80-digit grid.

At T=14, exact pi intervals verify Y_upper^2<84*85. Retain degrees 84 through 131 individually and add the complete undamped tail B(a,132,T). The resulting complete low-frequency mass bound is approximately 0.0009304093559968975, strictly below 1/1000. Although this mass exceeds the split bound at its different cutoff, the higher cutoff improves the physical high-frequency term enough to certify

\[
c_{\rm raw}=\log T-7/(216T^2)
-(27/5+\log T-7/(216T^2))\rho
-\text{pole loss}-\text{joint prime loss}>13/20.
\]

The displayed value is approximately 0.654497381644652. The prime-2/4 and prime-3/5 chain controls, actual pole bound and logarithmic complement bound 9/100 are freshly checked at the new aperture by the original constructor. Three invalid integrated-damping domain controls reject. This is a fixed-aperture certificate; no uniform attenuation over varying apertures is asserted.

## Matching full Gram and refined sign

The full Gram is freshly constructed twice from the actual 17/20 source and native enclosures. Endpoint-log/log, endpoint-log/smooth and smooth/smooth terms, all mixed entries and the complete 84-coordinate projection are retained. All 7,056 native/source comparisons are required to lie within the corresponding actual physical source errors. Every residual Gram entry must have width below 10^-55.

The exact integer Hankel contractions use 500-term endpoint logarithms and a 300-digit outward grid. Every one of the 14,112 endpoints is stored losslessly as a finite-decimal string. Independent direct double sums and original convolution intervals agree for source pairs (0,83), (41,83), (83,83) on panels 0,4,8, for both power and endpoint-log contractions. Large integer carry and mismatched projection controls pass.

The actual operator correction remains delta=eta(2M+eta). Changing the complement bound changes beta, not this correction or the stored source/Gram data. The refined check uses Q84-(20/13)Rhat84-((20/13)delta+tau)I, with all complete inputs pinned by SHA256. Its candidate margin starts at the actually certified native finite margin.

The baseline complement c=23/40 already yields a certified positive actual corrected matrix at the native finite margin tau=1/(32*10^18). With the stronger integrated complement c=13/20, both 160-digit refined sign runs reproduce byte for byte and retain that margin. All 84 shifted pivot lower bounds are strictly positive. The certified lift bound is J=8.

The exact scalar comparison gives

\[
\mu=\frac{13}{27040000000000000000020},\qquad
\kappa=\frac{13}{6219200000000000000004730}.
\]

Its comparison matrix has nonnegative diagonal entries and determinant mu^2>0; twice this conversion coefficient is rejected. The inherited actual Garding inequality gives the displayed kappa. Consequently, on the complete actual native domain D_(17/20),

\[
Q_a(h)\ge4\cdot10^{-22}\|h\|_2^2,\qquad
Q_a(h)\ge2\cdot10^{-24}E_{\log}(h).
\]

The actual whole-domain positivity frontier advances from 41/50 to 17/20. Fixed-aperture weak null modes are excluded and the existing WD-T10 full-source unit-domination consequence applies. Both baseline and refined positive certificates remain recorded. This is fixed-window control, not all-window domination or global endpoint exclusion.

The full Gram maximum entry width is approximately 3.041949685829048e-114. The exact source correction delta is approximately 1.532563211620454e-35. These are displays; every proof decision uses exact rational endpoints.


## Validation, reproduction and remaining scope

The independent refined-sign validator checks all four source/native/Gram/complement hashes, widens the complete matrices to an 80-digit grid and recomputes every corrected pivot. It verifies the exact lift, physical norm and inherited Garding conversions. Four independent exact Bessel-series controls at degrees 84,131 and arguments 60,75 check normalization and squared damping; all 644 differential-equation coefficient identities hold, and an overly strong exponent is rejected. The numerical controls verify application conventions; the analytic inequalities are proved in the notes.

From the repository root:

```sh
python scripts/certify_native_prime5_matrix84_085.py > /tmp/native085.json
python scripts/compact_native_prime5_matrix84_085.py --input /tmp/native085.json --output notes/data/RPB108_PRIME5_MATRIX84_085_COMPACT80_20261006.json
python scripts/certify_native_prime5_source84_085.py > notes/data/RPB108_PRIME5_SOURCE84_085_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_gram84_085.py > notes/data/RPB108_PRIME5_GRAM84_085_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_integrated_complement84_085.py > notes/data/RPB108_PRIME5_INTEGRATED_COMPLEMENT84_085_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_integrated_schur84_085.py > notes/data/RPB108_PRIME5_INTEGRATED_SCHUR84_085_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_integrated_schur84_085.py > /tmp/integrated-schur085-repeat.json
python scripts/validate_native_prime5_integrated_085.py /tmp/integrated-schur085-repeat.json
```

Complete source and Gram files are Git blobs in the commit tree and are read back exactly with the other artifacts. Historical 41/50 notes and certificates remain intact. No Lean, axiom or workflow edits and no requested CI run. Global endpoint exclusion, historical selected-packet attachment, F4 and FULL TRANSPORT CLOSED remain open.
