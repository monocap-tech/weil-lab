# RPB108 LF02 — exact matrix witnesses and the native certificate consumer

Continues LF01 on `formalization/rpb108-certificate-transport`.
RC37 remains the isolated research base. No RC branch ref is changed.

## New source

- `ExactMatrixWitness.lean`: an exact diagonal-factor equality and
  nonnegative diagonal imply Mathlib matrix PSD and the universal quadratic
  inequality. Singular PSD is allowed. Rational entries may be represented
  by exact real casts, but their equality and signs must be checked by Lean.
- `PhysicalResidualTransport.lean`: the whole physical weak-residual identity
  bounds the canonical Riesz error, then transports the squared inclusion
  budget. The proof uses the error vector itself as a test, so finite trial
  stationarity cannot satisfy the premise.
- `ActualZetaCertificateConsumer.lean`: proves that the already-defined actual
  physical inclusion is a contraction using the existing energy comparison;
  instantiates whole weak-residual error transport; pins Schur coercivity to
  the actual native operator; transfers its floor to every member of the full
  canonical form domain through the existing inverse maps; transfers full
  canonical positivity to the attached actual-zeta Green zero form.

The actual carrier instance proves the unit inclusion budget. The sharper
RC32 supported budget `252/257` still needs an analytic Lean specialization.
No unsupported identification of the source graph with Green closure occurs.

## Validation boundary

LF01's ten certificate-transport declarations compiled successfully in run
`38081711674`, job `114299805937`, at commit
`cecfa2973489b5097423b9c4af1875490ccf9bfe`. This is target-specific evidence.
The full-root audit and LF02 declarations require their own completed build
results. The workflow now checks the three small certificate modules before
the root. New pushes queue rather than cancel an in-progress root audit.

## Next proof data

Export RC36's nominal rational Gram inequalities to explicit checked matrix
factorizations. This will certify the finite rational inequalities only.
The interval enclosures, exact-source discrepancy, improved inclusion budget,
and original native feature attachment remain separate analytic obligations.

Neither this witness consumer nor an uninstantiated native Schur theorem
establishes new aperture positivity, the CC119 certificate import, F4, or RH.
