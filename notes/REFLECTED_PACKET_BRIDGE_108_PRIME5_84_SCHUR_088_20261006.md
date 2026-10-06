# RPB108: matched actual 84-source calculation at 22/25

Base input custody: `e307fe186f5b4cb5c908f070171582aed1801cad`.
Definitions: [22/25 registry](../docs/TERMINOLOGY_RPB108_PRIME5_84_SCHUR_088.md).
The immutable [preflight](REFLECTED_PACKET_BRIDGE_108_PRIME5_088_PREFLIGHT_20261006.md) and [matched-input checkpoint](REFLECTED_PACKET_BRIDGE_108_PRIME5_088_MATCHED_INPUTS_20261006.md) record the earlier finite-only stages.

## Lawful matching at the larger aperture

The physical aperture is a=22/25, source length d=44/25 and native correlation length L=88/25. All physical orthonormal Legendre degrees 0–83 are retained. Prime powers 2,3,4,5 contribute, with Lambda(4)=log(2). Exact rational logarithm enclosures verify d<log(6), so every one of the original nine panels remains strictly ordered. This proof does not extend that panel order across the boundary a=log(6)/2.

The native remainder ceilings are exp(L)<34 and L/(1-exp(-L))<5L/4=22/5. The constructor retains exponential order 260, Bernoulli order 230, gamma order 20 and 220-term logarithms on a 400-digit outward grid. The source constructor verifies alternating, decreasing absolute Bernoulli-pair coefficients; half its finite kernel polynomial is bounded by (1+d+d^2/3)/2<11/5. Since d/2<1 and d<3, its existing exponential order 90 and Bernoulli order 100 controls apply, with gamma order 50. Coefficient rounding to denominator 10^40 retains its complete error budget.

The unchanged quarter-window certificate agrees exactly with the recovered earlier helper. Three invalid native and two invalid source dimension/aperture controls reject. Older aperture arithmetic is not changed.

Both fresh native runs reproduce byte for byte and certify finite margin tau_native=1/(2048*10^18). Both outward 80-digit compact exports reproduce byte for byte, including all 7,056 containment checks, exact symmetry, odd parity zeros, and 42 even plus 42 odd shifted positive pivots. The compact certificate records the full original native hashes and the construction hashes; the canonical Git-backed enclosure is the compact certificate. This is not a claim that the original full native blob was uploaded.

Both fresh source runs reproduce byte for byte. The aggregate actual physical source-map error is approximately 1.4875240004297264e-36. No endpoint logarithm, actual translation panel, signed pole or prime term is dropped.

## Actual complement and integrated damping

The proved spherical-Bessel positive-region estimate and its degree-by-degree integrated bound are in [the 17/20 proof](REFLECTED_PACKET_BRIDGE_108_PRIME5_84_SCHUR_085_20261006.md). That proof uses the actual physical plane-wave normalization, not an abstract moment surrogate.

The baseline finite-band split at T=25/2, q=177/200 and N=11 freshly certifies physical complement 1/2 and logarithmic complement 9/100. Its actual pole bound, joint prime-2/4 operator bound and prime-3/5 four-vertex chain norm are all checked at 22/25. The independent positive and negative 4x4 chain comparisons pass; a smaller chain constant rejects.

The integrated certificate uses T=27/2, individual degrees 84–131 and the complete undamped tail from degree 132. Write Y=2*pi*a*T and z_n=Y^2/(2n+3). The analytic inequality log(s)<=(s^2-1)/2 gives exp(-z_n*s^2)<=exp(-z_n)*s^(-2z_n). Thus the integrated degree bound is

\[
\frac{4aT(2n+1)Y^{2n}e^{-z_n}}
{[(2n+1)!!]^2(2n+1-2z_n)}.
\]

Exact pi enclosures verify Y_upper^2<84*85, hence every retained degree has positive rate. The numerator power and reciprocal rate use Y_upper; attenuation uses Y_lower and the reciprocal of a positive 61-term exponential Taylor sum. Every term and the infinite tail is rounded outward on an 80-digit grid.

The complete low-frequency mass upper bound is approximately 0.0007784985184788175. The unrounded physical complement lower bound is approximately 0.6193667796498902. It certifies both the original c=3/5 and the sharper rational c=619/1000, beta=1000/619, without changing the cutoff or mass calculation. The logarithmic complement remains 9/100. The baseline, integrated and refined complement certificates each reproduce exactly, and three invalid integrated-damping controls reject. These are fixed-aperture bounds, not a uniform attenuation claim over varying apertures.

## Complete Gram and exact sign

The fresh residual Gram retains endpoint-log/log, endpoint-log/smooth and smooth/smooth contractions, every mixed entry and all 84 projected coordinates. It uses exact integer Hankel contractions, 500-term endpoint logarithms and a 300-digit outward grid. Every one of the 14,112 residual endpoints is encoded losslessly as a finite-decimal string. Every native/source pairing must pass its actual physical error bound; no sampled pairing check replaces the full 7,056 comparisons.

The independent Hankel validator checks nine power and nine endpoint-log contractions on panels 0,4,8 for source pairs (0,83), (41,83), (83,83). Direct double sums agree exactly, original convolution enclosures are contained, large-integer carry controls pass and mismatched source/projection dimensions reject.

The complete correction is delta=eta(2M+eta), where eta is the actual physical source-map error and M bounds the full surrogate residual-map norm. Both full Gram runs agree byte for byte. At c=3/5, the stored sufficient estimator has a certified negative direction whose actual native energy is positive. The independent stored-vector validator confirms native Rayleigh energy approximately 4.142473728951854e-20 and sufficient-estimator Rayleigh upper bound approximately -1.0532323848542405e-21. Its required complement constant lies in a rational interval displayed near 0.615255122235198. This is not an actual negative full-form witness. The complete original Gram and its negative certificate remain unchanged.

The sharper c=619/1000 therefore uses the same full inputs. The separate 160-digit sign constructor pins all three complete input hashes and checks Q84-(1000/619)Rhat84-((1000/619)delta+tau)I. Its margin search begins at the actually certified native margin, not at an extrapolated larger margin.

Both refined sign runs reproduce byte for byte and certify

\[
\tau=\frac1{16384000000000000000000},\qquad J=9.
\]

All 84 shifted pivot lower bounds are positive. The margin is one eighth of the certified native finite margin. The exact scalar conversion gives

\[
\mu=\frac{619}{831619072000000000000001000},\qquad
\kappa=\frac{619}{191272386560000000000000236190}.
\]

The comparison matrix has nonnegative diagonal entries and determinant mu^2>0; twice the conversion coefficient rejects. The inherited actual Garding inequality gives kappa. Consequently, on the complete actual native domain D_(22/25),

\[
Q_a(h)\ge7\cdot10^{-25}\|h\|_2^2,\qquad
Q_a(h)\ge3\cdot10^{-27}E_{\log}(h).
\]

The full-domain positivity frontier advances from 17/20 to 22/25. Fixed-aperture weak null modes are excluded and the existing WD-T10 full-source unit-domination consequence applies. This is fixed-window control, not all-window domination or global endpoint exclusion.

The full Gram maximum entry width is approximately 3.041949685829048e-114 and its exact actual Gram correction delta is approximately 1.5904977757900004e-35. Displayed decimal values do not decide any proof gate.

## Independent validation and scope

Both independent stored-input validation runs reproduce byte for byte. They verify all four source/native/Gram/complement hashes, exact symmetry, the full Gram correction, lift bound and scalar physical/logarithmic conversions, and recompute all 84 shifted pivots on an 80-digit outward grid. The negative diagonal rejects; the sign constructor also rejects the doubled conversion coefficient.

Four independent rational Bessel-series controls use degrees 84,131 and arguments 60,75. They verify squared damping and 644 differential-equation coefficient identities; an overly strong exponent rejects. In addition, at the actual cutoff, independent even-order-180 Taylor polynomials for exp(-z*s^2) are integrated coefficient by coefficient at degrees 84 and 131. Their rational upper bounds lie below the integrated power majorant, while the next odd term gives positive lower bounds. The report rounds the integral lower bounds down, upper bounds up, and majorant lower bounds down on an 80-digit grid; the displayed enclosures still prove the strict inequality. These checks validate application conventions; the analytic Bessel and integrated inequalities remain proved in the cited note.

Reproduction from the repository root:

```sh
python scripts/certify_native_prime5_matrix84_088.py > /tmp/native088.json
python scripts/compact_native_prime5_matrix84_088.py --input /tmp/native088.json --output notes/data/RPB108_PRIME5_MATRIX84_088_COMPACT80_20261006.json
python scripts/certify_native_prime5_source84_088.py > notes/data/RPB108_PRIME5_SOURCE84_088_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_gram84_088.py > notes/data/RPB108_PRIME5_GRAM84_088_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_integrated_complement84_088.py > notes/data/RPB108_PRIME5_INTEGRATED_COMPLEMENT84_088_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_refined_complement84_088.py > notes/data/RPB108_PRIME5_REFINED_COMPLEMENT84_088_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_integrated_schur84_088.py > notes/data/RPB108_PRIME5_INTEGRATED_SCHUR84_088_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_integrated_schur84_088.py > /tmp/integrated-schur088-repeat.json
python scripts/validate_native_prime5_integrated_088.py /tmp/integrated-schur088-repeat.json
```

Global endpoint exclusion, retained historical selected-packet attachment, F4 and FULL TRANSPORT CLOSED remain open. No Lean, axiom or workflow changes are made. Historical notes and earlier certificate flags retain their original snapshot scope.
