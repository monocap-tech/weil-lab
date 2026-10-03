# RPB-108 — source reconstruction and bounded-L2 type boundary

Recovered research head: e24a611b05389787cf2af61355064aa1640166e7.
Latest certified Lean source: a212c087ae269a27e17f7b715531caaa95b37088.
This is an analytic/type diagnosis, not a Lean theorem certificate.
No actual witness is claimed and no new conditional representation module is added.

## Primary-source reconstruction

Re-read Zhu, arXiv:2608.24827v2:
https://arxiv.org/html/2608.24827v2

The source gives the compact-window geometric quadratic formula in §2,
equations (2), (3), (7), and real/complex parity decomposition in §6.1,
Lemma 6.1. The odd pole contribution is negative; the nonnegative even pole
premise cannot be copied to arbitrary complex vectors. These results identify
the source geometric functional, not the project's abstract selected synthesis
operator with that functional.

The actual remaining project identification is between the selected physical
realization and that source functional on its lawful domain. The independent
density, symbol and scalar-Q parameters in WD-T38's Lean constructor do not
establish it.

## Bounded-L2 boundary

NeutralNullExtensionInterface uses bounded continuous linear operators on H.
NeutralPhysicalFourierCarrier specializes its interface to ordinary physical L2.
This does not mean the full logarithmic Weil operator is bounded on ordinary L2.

In particular, requiring its bounded endpointOperator to represent the concrete
Weil diagonal on the FULL canonical supported logarithmic domain is not a lawful
repair. The following analytic argument explains the obstruction; it is not
formalized in Lean in this pass.

Fix a nonzero smooth function phi with support strictly inside the window, and
set f_R(x) = exp(2*pi*i*R*x) * phi(x). Its L2 norm is independent of R, while its
mathlib Fourier transform is the Fourier transform of phi shifted by R. All
f_R have finite logarithmic energy and belong to the canonical form domain.
Choose a bounded spectral interval carrying positive Fourier mass of phi.
The shifted mass on this interval contributes at least a constant times log R
to the logarithmic energy as R increases.

Under the retained actual EXT5 asymptotic, the actual symbol is bounded below
by a positive multiple of log(e+|xi|) minus a constant. The finite prime
correction is bounded. The pole pairing is uniformly bounded for these
fixed-support, fixed-L2-norm functions by Cauchy-Schwarz against the two
exponential window moments. Hence the concrete quadratic diagonal grows
without bound as R tends to infinity.

For a bounded ordinary-L2 operator W, however,
abs(inner(f_R, W f_R)) <= norm(W) * norm(f_R)^2,
which is uniformly bounded. Thus no such W can represent the concrete
quadratic diagonal on the full canonical domain. A restricted source domain
that does not contain these modulated tests is not excluded by this argument.
Nor does it exclude a bounded representation in a stronger form-space norm.

## Correct reconstruction target

Preserve the original source Hilbert/form-space topology and its explicit map
into physical L2. Carry source membership through that map using the retained
finite-log-energy data. Identify source and geometric quadratic forms on the
lawful SAME source domain. Use the existing polarization bridge there.

Alternatively, formulate the endpoint relation through the source form and its
dual/observation pairing, rather than an equality between a globally bounded
ordinary-L2 operator and the whole-line logarithmic multiplier. The existing
abstract null equation can only be transported once this relation is supplied
by the actual source realization.

The carrier's inclusion in the canonical logarithmic domain does not require
equality of that source domain with the full canonical domain. Existing
sourceFormDomain_le_canonical already expresses the lawful containment.

This assessment does not establish the source realization, carrier energy,
same-domain diagonal identity, or any mixed null column. It rejects an invalid
full-domain bounded-L2 attachment and identifies what must be reconstructed
before endpoint nullity can be consumed.

## Witness status

- Actual carrier/source-domain attachment: not proved.
- Actual source quadratic/mixed identification: not proved.
- WD-T38 source identification: retained mathematical hypothesis; no concrete
  source realization witness found in the current Lean branch.
- Enlarged cancellation: requires translation of strict persistence in the
  contradiction; it is not implied by endpoint nullity.
- Spectral-product L2 membership: not derived; stronger route remains stopped.
- Actual locally integrable defect and whole compact realization: open.
- No new axioms, witness-valued placeholders or conditional representation
  modules were introduced.
- Threshold bookkeeping remains closed; F-4 coercivity has not started.

Next substantive task: reconstruct the actual source form-space-to-L2 map and
its form/observation relation. Adding another field that simply assumes that
relation would not prove the witness requested.
