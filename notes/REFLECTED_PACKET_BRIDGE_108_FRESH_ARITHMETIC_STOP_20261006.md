# RPB108: actual arithmetic and bounded weak stop witnesses for the fresh morphology

Date: 2026-10-06. Source base: `682cf563c4ffd6bebbd635799db0b8fdac42ac0c`.
Definitions: [fresh arithmetic and stop interface](../docs/TERMINOLOGY_RPB108_FRESH_ARITHMETIC_STOP.md).
Lane: global/F4. No aperture computations.

## Result and exact scope

Conditional on an actual nonnegative null window c, the preceding fresh fixed right packet now has concrete analytic witnesses for every field of the existing NeutralDefectMorphology record. The actual physical Fourier density, actual full quadratic value, signed cross-pole identity, and threshold-aware bounded weak operator interface are specified. No unrelated density, Q, operator or extension vector is substituted.

This is an analytic record instantiation, not a compiled Lean constructor application. Its geometric fields were closed in FRESH_FIXED_RIGHT_PACKET; this note supplies the arithmetic and null-extension fields. The prescribed historical P,C,k remain separate named objects. The newly attached persistenceGoal is false for this fresh nonzero actual vector, exactly as expected from strict-margin translation rigidity.

Thus the actual contact -> fresh attained WD-T38-style morphology path is closed analytically. Contact -> same-vector enlarged full cancellation remains obstructed, so this does not exclude contact or close F4. The remaining decisive global theorem is actual nonnegative-contact exclusion (or an independent genuine endpoint-action bound implying it).

## Actual density and signed form before comparison

Use the unchanged normalized endpoint vector k from FRESH_FIXED_RIGHT_PACKET, Fourier convention exp(-2 pi i x xi), and the canonical weight w=log(e+|xi|). Set
\[
\rho(\xi)=|\widehat k(\xi)|^2,\quad
M=\int\rho=\|k\|_2^2,\quad E=\int w\rho.
\]
L2 Plancherel and the canonical logarithmic domain give integrability of rho and w rho. A measurable Fourier representative defines the density; it is not an independent arbitrary record parameter. Choose m_c with the strict endpoint prime cutoff. The equality-threshold terms have zero mixed compression on D_c, as proved below, so this gives the same actual native form there. Its symbol satisfies |m_c-w|<=C_c for some finite C_c>=0, including the frozen finite prime correction; removing or adding a finite threshold term changes only the finite error constant. Thus m_c rho is absolutely integrable.

The exact actual form is
\[
Q=Q_c(k,k)=p+\int m_c\rho=0,\qquad
p=2\Re\bigl(\overline{M_-(k)}M_+(k)\bigr).
\tag{1}
\]
The original pole is signed on the unrestricted complex carrier. The certified opposite-slot pole dictionary is retained. Cauchy-Schwarz on [-c,c] gives
\[
|p|\le LM,\qquad L=4ce^c>0.
\tag{2}
\]
No H1 or spectral physical operator-domain assumption is used for (1)-(2).

## Exact inputs to the existing arithmetic constructor

Define mu=m_c-L, pi=p+LM and sigma=C_c+L. Then
\[
0\le\pi\le2LM,\qquad
w\le\mu+\sigma=m_c+C_c\le w+2C_c\le(1+2C_c)w,
\tag{3}
\]
using w>=1. Moreover
\[
Q+\sigma M=\pi+\int(\mu+\sigma)\rho.
\tag{4}
\]
Every integral is absolutely convergent by the original density/log-domain bounds. These are concrete inputs to wd_t38_neutral_arithmetic_morphology with:

| Parameter | Actual supplied value |
| --- | --- |
| density | rho=|Fourier(k)|^2 |
| Q | the same actual Q_c(k,k)=0 |
| symbol | mu=m_c-L, only in the scalar comparison constructor |
| pole | pi=p+LM, explicitly a comparison remainder |
| shift | sigma=C_c+L |
| lowerC | 1 |
| upperC | 1+2C_c |
| poleC | 2L |
| primeCoeff | the prescribed actual prime coefficient table in the project's finite-prime convention |

The resulting logarithmicOrder field is
\[
E\le Q+\sigma M\le(1+2C_c+2L)E.
\tag{5}
\]
The existing finite right prime support, threshold subsingleton, finite-prime no-free-Sobolev theorem and global-cancellation scope theorem supply the other arithmetic fields. Those generic scope fields do not themselves identify the physical source; (1)-(4) provide the actual density/form custody here.

This is a lawful use of the existing record because its arithmetic output retains the density, Q, shift and order bounds; it does not retain an assertion that the input scalar named pole is the original physical rank-two pole. No historical formula is edited. The reallocated remainder is generally not finite rank: it includes a physical mass form. It is used only in the scalar order comparison. The actual physical source action and every Gaussian pairing continue to use the original m_c and original exponential pole. Importing pi as neutralWeilSourcePole would be an incorrect substitution.

The cancellation of the two mass terms holds on the entire same-domain mixed form as well: subtract L times the physical L2 pairing from the multiplier part and add it to the pole/remainder part. Hence (4) is not a new source equation or a new physical vector. It cannot create enlarged central cancellation or stronger regularity.

## A common bounded carrier with the actual threshold correction

Shrink the radius b used for the fresh packet if necessary, before choosing its fixed coefficient carrier, so that b>c is inside the local coercive-background neighborhood and no prime power satisfies 2c<log n<=2b. Such a b exists: in any fixed larger bounded interval there are finitely many prime powers, so the finite set of strictly larger threshold distances has a positive minimum (or is empty).

On Hext=D_b, let W_le be the Riesz operator of the actual frozen right-limit-c multiplier plus original pole. Because there is no new threshold, W_le is exactly the full actual native operator A_b. Let T_eq be the Riesz operator of
\[
\sum_{\log n=2c}\frac{\Lambda(n)}{\sqrt n}
 (\tau_{\log n}+\tau_{-\log n})
\]
in physical L2 pairings compressed to D_b. It is bounded, since it is a finite sum of bounded physical translations and physical inclusion is bounded. Define the strict-cutoff operator W_lt=W_le+T_eq; in subscript notation,
\[
W_{<}=A_b+T_{eq},\qquad W_{\le}=A_b.
\tag{6}
\]
W_lt is exactly the frozen endpoint strict-c operator: removal of a negative prime term adds its translation correction. At a threshold these operators can differ on D_b. If primePowerThreshold c is empty they are equal.

The equality-threshold translates have disjoint overlap on endpoint-supported inputs and tests, except on measure-zero endpoints. Thus for J:D_c->D_b,
\[
J^*T_{eq}J=0,\qquad
J^*W_{<}J=J^*W_{\le}J=A_c.
\tag{7}
\]
These are logarithmic Riesz operators on the named form carriers. No logarithmic multiplier is misrepresented as a bounded operator on unrestricted physical L2.

## Null-extension record, with no hidden persistence premise

Supply the existing NeutralNullExtensionInterface at parameter c with:

| Field | Concrete actual witness |
| --- | --- |
| Hext | D_b with its logarithmic Hilbert norm |
| EndpointObs | D_c |
| RightObs | D_b |
| extend | J, preserving the global physical zero extension of k |
| kExt | Jk, nonzero by physical inclusion |
| endpointOperator | W_lt |
| rightLimitOperator | W_le=A_b |
| endpointRestriction | J*, the compression of weak test observations |
| rightRestriction | identity on D_b, observing all enlarged weak tests |
| endpointInteriorNull | J*W_lt Jk=A_c k=0 |
| right_eq_endpoint_of_no_threshold | from T_eq=0 away from equality thresholds |
| prime support fields | the certified strict-right finite support and subsingleton results |

The nullExtensionVector field is exactly kExt=extend k=Jk. Hext is a bounded supported logarithmic carrier for the whole-line physical zero extension, not the entire global physical L2 space. For compact smooth tests in (-b,b), its Riesz pairings equal the actual frozen multiplier-plus-pole action. Endpoint compression therefore means the actual central equation on (-c,c), rather than an abstract operator merely named endpoint.

The resulting persistenceGoal is precisely
\[
W_{\le}Jk=A_bJk=0.
\tag{8}
\]
It is false: nonzero k is supported in [-c,c] with strict margin in b, and the existing translation-rigidity theorem excludes full mixed nullity at b. No theorem here converts endpoint observation into enlarged observation. At a threshold the correction in (6) is kept explicit; away from thresholds equality of the two frozen operators still does not equate J* with the identity.

## Full fresh record and smallest remaining theorem

All geometric fields, sequence fields, actual selected source/synthesis identities and the physicalNull field use the fresh packet previously constructed. Equations (1)-(5) now supply its arithmetic field with the actual Fourier density and actual Q. Equations (6)-(8) supply the exact nullExtension and nullExtensionVector fields. Thus every field of NeutralDefectMorphology has a concrete analytic actual witness conditional on the contact hypothesis. A corresponding Lean proof must still formalize the fixed support filtration, compressed synthesis, scalar reallocation, and weak operator identities; this note is not that compiled proof.

The endpoint actual central cancellation follows on (-c,c) from A_c k=0 and the existing action/form dictionary. Its supported-L2/logarithmic domain promotion is lawful. The enlarged central cancellation required by the strict-gap F4 chain is (8), already obstructed on this fresh realization. A right-limit coefficient vector is retained, but the physical mixed equation is not transported to the larger test domain.

The dependency is now:
 actual nonnegative contact -> fresh actual morphology -> false same-vector full persistence.
The last conclusion does not negate contact. First contact followed by enlarged negative directions remains consistent. To close the global lane, the smallest decisive independent theorem is still absence of a nonzero kernel at every actual nonnegative window, or a genuine endpoint-action decay/H1 theorem that implies it. Prescribed historical attachment is an additional named-object comparison if that old packet is required; it is not needed to construct this fresh option-2 morphology.

## Custody and validation

Pinned inputs: FRESH_FIXED_RIGHT_PACKET_20261006; ACTUAL_CORRELATION_POLES_20261004; ACTUAL_MOVING_GAUSSIAN_COERCIVITY_20261004 (symbol and pole bounds); TRANSLATION_NULL_EXTENSION_OBSTRUCTION_20261004; L2_NULL_DOMAIN_PROMOTION_20261006; WeilDefect/Morphology/Neutral.lean; Arithmetic/LogarithmicForm.lean; Arithmetic/PrimeSupport.lean; Morphology/NeutralInnerCollarRegularity.lean; NeutralGaussianAssembly.lean. Blob custody is in the manifest.

The rational script checks signed-pole mass reallocation, both symbol bounds, exact total-form preservation, threshold-correction sign, endpoint compression and failure of enlarged observation. The analytic work proves the actual integration, finite threshold gap and weak operator dictionaries; rational controls are not an actual null computation or Lean certification. Lean and workflows unchanged; no new build/axiom audit. Historical records preserved. F4 and FULL TRANSPORT CLOSED remain open.
