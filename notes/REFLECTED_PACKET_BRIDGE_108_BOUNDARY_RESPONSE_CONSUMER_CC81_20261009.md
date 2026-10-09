# CC81 — positive original response consumed, residual deficit retained

Integration parent CC80: e54ff7bc65914a73b8dbd29c408eabd55f6a50d2. Read-only source NF42: f2c49f8d2ff95374d3ee2c3b1836ec772e4817dc. Read [CC81 definitions](../docs/TERMINOLOGY_RPB108_RESIDUAL_RESPONSE_CC81.md) before the residual-column criterion. This checkpoint writes Coupled only.

## Original response has advanced beyond CC80

NF42 constructs all original signed boundary source covariances, pays their physical errors and encloses the full two-source Woodbury credit. Its four-high-column minorant A1 agrees with the actual high operator on Z and Y under the explicit floor hypothesis A>=(207/1000)I. This hypothesis is not newly proved. The source-backed response is strictly positive on both frozen NF38 witnesses, excluding the zero-response possibility for this expanded original source packet under that hypothesis.

The independent CC81 consumer authenticates the two full source certificates against the original validator hashes and authenticates the validator manifest. It reconstructs the two-by-two inverse denominator with separate rational interval arithmetic, checks all nine Woodbury entries overlap the published intervals, and computes the witness credit by first forming g h. It separately verifies positive leading joined minors, a strictly negative complete determinant and a negative joined witness value. These are independent certificate-level matrix checks, not a replay of the original endpoint/prime source integration.

| Conditional response quantity | Even | Odd |
| --- | ---: | ---: |
| Published source-backed witness improvement | [1.68013122983,1.78712561456]e-24 | [1.98181339342,1.98435969486]e-22 |
| Independently enclosed fraction of baseline witness deficit | (0.01678,0.01867) | (0.11883,0.11980) |
| Necessary additional actual response after A1 | >9.39362146648e-23 | >1.45753955024e-21 |

The fractions use the interval baseline witness deficit, not a physical norm or the old whole-domain gap. They describe this frozen witness only. Neither improved full joined lower matrix is positive. A negative lower certificate is not negative actual original Weil energy: the unknown residual matrix T1 remains positive semidefinite and may supply further credit.

## Quantitative next-column target

Keep D1=A-A1>=0 and freeze a genuinely independent original high polynomial y. After establishing its operator-domain/source attachment and d1=<y,D1y>>0, completion of its defect square gives

    D1 >= f1 f1*/d1,  f1=D1y.

Inverse order and scalar Woodbury then give

    T1 >= p1*p1/b1,
    p1=f1*A1^-1R,  b1=d1+f1*A1^-1f1.

The first useful rejection screen for each parity is |p1 h|^2/b1 exceeding the corresponding necessary additional-response bound above. Nonzero response alone no longer suffices: its magnitude must pay this measured deficit. Rescaling y cannot improve the quotient, because numerator and denominator both scale quadratically. The full signed, error-paid matrix K1+p1*p1/b1 must pass before a simultaneous six-direction restriction is claimed. Passing only the witness quotient remains insufficient.

The appropriate source deliverable comprises original Ay, its native attachment to all four H columns, and every signed physical covariance needed for f1,f1*A1^-1R and f1*A1^-1f1. Physical orthogonality to H may fix a selection but cannot delete source covariances. The trial must be frozen before its response sign proof. A larger independent source span is allowed if one column cannot pay the full matrix deficit; the existing packet supplies no guarantee that one column will suffice.

## Verification and custody

The original NF42 terminology, note, two certificates and validator manifest are frozen unchanged under notes/cc81-source/. Run:

    python scripts/certify_cc81_boundary_response_consumer.py notes/cc81-source --output notes/data/RPB108_CC81_BOUNDARY_RESPONSE_CONSUMER_20261009.json

The consumer uses only Python exact fractions. New six rank-one full-matrix credit controls cross positive/null/negative at two scales with nonzero mixed entries. Direct determinant and updated leading-block condensation agree; nonzero rescaling leaves credit invariant. Existing CC80 controls remain preserved. Consumer result: PASS. Source integrations and the original NF42 validator are not replayed here; their published verification is separately identified.

The complete remaining background transport and actual residual response remain open. CC74's four-direction and CC78's separate two-direction full-high restrictions are preserved; no simultaneous six-direction certificate follows. Whole-domain positivity stays 21/20, not 53/50. RH, F4, full transport, uniform all-cap continuation and Lean remain open. Historical wording, DNE and paused branches are unchanged.
