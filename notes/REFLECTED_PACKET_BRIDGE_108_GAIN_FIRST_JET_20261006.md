# RPB108: actual subcritical gain rate and the first-derivative obstruction

Date: 2026-10-06 (America/Los_Angeles). Source `874ebbe767021d5e26f1d32ce034bec70d6115e8`.
Definitions: [subcritical gain registry](../docs/TERMINOLOGY_RPB108_GAIN_FIRST_JET.md).
Global/F4 lane; no aperture computation or actual contact existence assertion.

## Recovered stronger input and new gain consequence

FRACTIONAL_NULL_REGULARITY already proves, for every fixed 0<alpha<1/2, the actual full exterior residual bound
\[
M_s(h)\le C_{c,\alpha}s^{2\alpha}\|h\|_2^2.
\tag{1}
\]
This is a full mixed-null result, not a general logarithmic-carrier estimate. It retains the prescribed primes and pole and is uniform on the fixed null space. Its physical collar rates were already stronger than the inverse-log estimates; they are reused rather than claimed anew here.

Combining (1) with the new logarithmic dual collar estimate gives the actual gain consequence
\[
e_s(h)\le\frac{10C_{c,\alpha}}{\beta\log(1/s)}
s^{2\alpha}\|h\|_2^2.
\tag{2}
\]
For any fixed 0<epsilon<1, choose 2alpha=1-epsilon/2. Dividing (1)-(2) by the weaker power s^(1-epsilon) leaves s^(epsilon/2) tending to zero. Therefore
\[
\boxed{M_s(h)=o(s^{1-\varepsilon}),\qquad
e_s(h)=o\left(\frac{s^{1-\varepsilon}}{\log(1/s)}\right).}
\tag{3}
\]
The little-o is uniform for mass-one vectors in the fixed actual kernel, using the existing fixed-alpha constants. No limit alpha=1/2 or epsilon=0 is taken. In particular no O(s), finite first derivative, or quadratic estimate follows.

For an orthonormal basis of the finite null coefficient space E, reconstruction B_c is bounded into physical L2. Summing (2)-(3) over that basis proves
\[
f(s)=o\left(\frac{s^{1-\varepsilon}}{\log(1/s)}\right)
\quad\hbox{for every fixed }\varepsilon>0.
\tag{4}
\]
Thus the available actual total trace upper rate is nearly linear with an arbitrary fixed power loss, while the sufficient sequencewise exclusion theorem requires finite liminf of f(s)/s^2. This is the remaining quantitative separation. The existing spectral split proves f(s)/s^2 tends to infinity at any nonzero contact; (4) is consistent with that conditional conclusion.

## Finite variation cannot supply quadratic boundedness

On a fixed nearby support interval, strict Loewner monotonicity makes f positive and increasing, and norm continuity gives f(s) tending to zero. It has finite total variation on that compact interval. These facts give no bound on f(s)/s^2. The smooth scalar response Lambda(c+s)=1+s has f(s)=s, finite variation and bounded derivative, while f(s)/s^2=1/s tends to infinity. It also obeys every rate in (4).

Differentiability almost everywhere from monotonicity cannot impose a second-order estimate at the particular contact endpoint. Even a finite right derivative there is insufficient, because it can be positive. A zero right derivative remains insufficient, as the next controls show. These are failures of functional implications, not constructions of an actual arithmetic contact.

## Even a zero first derivative does not close the target

For sufficiently small s>0, set L=log(1/s). The following positive increasing scalar gains all satisfy f(s)/s^2 tending to infinity, all finite inverse-log decay rates, and (4):

| Gain f(s) | Right derivative at zero | Quadratic ratio |
| --- | --- | --- |
| s | 1; response is smooth | 1/s |
| s^(3/2) | 0; response is C1 | 1/sqrt(s) |
| s L | infinite; continuous and finite variation | L/s |
| s/L | 0; response is C1 | 1/(s L) |

For the logarithmic controls, derivatives on (0,s0) are L-1 and 1/L+1/L^2, respectively; choose s0<exp(-2). Each is increasing there and has finite endpoint variation because f tends to zero. Their first derivative limits are as displayed. For each fixed epsilon>0, dividing any of these f by s^(1-epsilon)/L gives a quantity tending to zero, since a positive power of s dominates every fixed logarithmic power.

Setting the scalar response to 1+f(s) gives a strictly increasing local response and a contact defect -f(s). It has a one-dimensional rough normalized gain spectrum consistent with GAIN_SPECTRAL_SPLIT. Assigning the scalar mass-control M(s)=L f(s) makes the dual collar inequality e<=10M/L hold and preserves every subcritical collar power rate. No physical residual function, prescribed zeta rows, or source synthesis is claimed for these assigned rates.

The exact failed implication is:

    norm continuity + finite Loewner variation + all actual subcritical power rates
    + a finite, or even vanishing, right first derivative of response
    -> finite sequencewise quadratic gain trace.

The s^(3/2) and s/L controls reject the zero-first-derivative version; s rejects the inference from smoothness alone. This belongs to endpoint exclusion. It does not reject a theorem with an additional genuine arithmetic second-order or compensator estimate.

## The operator distinction behind the obstruction

The exact compensator identity on E is
\[
\Pi_E[\Lambda(c+s)-\Lambda(c)]\Pi_E
=\big((C_{c+s}-C_c)|_E\big)^*
\big((C_{c+s}-C_c)|_E\big).
\tag{5}
\]
Hence a right Lipschitz bound for the compensator increment in the fixed positive Hilbert carrier gives O(s^2) gain and would exclude contact. A right Lipschitz bound or a vanishing first derivative for the **response** gives only O(s) or o(s) gain; it does not give (5)'s needed compensator regularity. In the s^(3/2) rate control the increment norm is s^(3/4), despite the response's zero first derivative.

Likewise response C2 regularity with a zero first derivative would give a quadratic upper bound by Taylor's theorem, but C2 regularity alone permits a linear crossing. The actual aperture family and local response have not been proved C1 or C2 here, and no derivative at a prime threshold is silently introduced.

The smallest sufficient targets remain the sequencewise finite quadratic trace liminf, the basiswise sequencewise full residual collar bound, or a right Lipschitz compensator estimate on the full actual contact space. Their actual arithmetic proofs are absent. The recovered fractional estimate supplies a real quantitative upper bound but does not bridge the gap from subcritical powers to quadratic scale.

## Validation and custody

Pinned sources and repeat rational controls: notes/data/RPB108_GAIN_FIRST_JET_20261006.json. At s=4^-n the script checks the four rate controls with the base-4 logarithm n, differing from the natural logarithm by a fixed positive factor. It verifies increasing quadratic ratios, positive finite-variation increments and the response/compensator square relation. Infinite asymptotics and derivative statements are proved analytically above; sampled controls are not their proof. No actual arithmetic contact or Lean certification is asserted. Historical statements are preserved. No Lean/compiler/workflow changes or new axiom/CI claim. Publication recovered the newer aperture-lane head d8d086c7882ea80026ecccf6d86eaff14eb78442: whole-domain positivity at 93/100 is certified there. This global-lane pass performs no aperture calculation. F4 and FULL TRANSPORT CLOSED remain open.
