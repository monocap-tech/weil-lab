# RPB108 LF01 — canonical certificate transport and full-root build gate

Recovered RC parent: `261e907ff6b8aed70a1319a86717286406ef7c4f` (RC37).
Work branch: `formalization/rpb108-certificate-transport`.

## Implemented declarations

`WeilDefect/Screening/CanonicalCertificateTransport.lean` formalizes:

1. RC23 metric and head floors under certified whole quadratic errors.
2. RC23 source-residual acceptance under a complete residual error bound.
3. Simultaneous robust gate with explicit metric reserve.
4. Physical-to-canonical residual transport through the inclusion estimate.
5. RC36's exact rational canonical budget and conversion equality.
6. Two-sector Schur coercivity with a positive common reserve.
7. RC22's exact scalar budget giving common reserve `1/10000`, conditional
   on the actual head/tail/mixed quadratic lower estimate.

The variables are quadratic evaluations on arbitrary vectors. They are not
matrix entries. Universal specialization is needed for a Loewner conclusion.
The complete residual error `eE` must include the RC23 error budget; this
pass does not reconstruct it from finite trial tests or matrix JSON.

## Build evidence boundary

The task environment has no Lean/Lake/Elan executable, and direct Git
cloning is blocked. Repository sources are read through the GitHub connector.
Existing cached Mathlib sources do not constitute a usable Lean installation.

This pass updates CI to compile the new exact target first and then
`lake build WeilDefect`, replacing the previous single example build.
Build logs are retained as artifacts even on failure. A successful new-target
build would certify these declarations; a successful root build would certify
the imported source chain at that commit. Source presence alone certifies
neither. Consult the draft PR's actual run result for build evidence.

## Remaining formalization seams

- Reflect rational PSD/LDL witnesses into universal matrix inequalities.
- Prove map-error-to-Gram-error transport and its operator-norm interface.
- Instantiate complete physical residual attachment and inclusion bounds
  for the supported canonical carrier, rather than assuming their evaluations.
- Import analytic endpoint/kernel/interval enclosures with checked proof data.
- Attach the actual CC119 certificate to a full-domain `a=53/50` theorem.
- Bridge the concrete source graph and Green closure with the intended test
  domain while preserving their distinction.
- Global positivity/nonstalling continuation remains unproved mathematics.

This patch formalizes the certificate consumer algebra. It does not certify
RC36's interval input, a new aperture, CC119's local theorem, F4, or RH.
Historical research records and all other branch refs remain untouched.
