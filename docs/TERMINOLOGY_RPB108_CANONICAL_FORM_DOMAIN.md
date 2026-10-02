# RPB-108 terminology: canonical supported logarithmic form domain

The canonical supported logarithmic form domain is
`neutralCanonicalLogFormDomain a`: all physical complex L2 classes that
vanish almost everywhere outside [-a,a] and have finite normalized Fourier
energy with weight log(e+|xi|). It is a complex submodule, with addition
and scaling closure proved using genuine integrability and a.e. L2 laws.

Canonical here specifies this concrete domain, not identification with an
imported source's chosen domain or form. Every lawful
`NeutralSourceFormDomainAttachment` has its domain contained in this one.
No equality of those domains is asserted.

The canonical carrier attachment constructor uses the actual physical
carrier's support and an explicit finite-log-energy witness. It does not
prove that witness, the source quadratic identity, central cancellation,
or spectral operator-domain membership. Finite form energy and the stronger
spectral-product L2 criterion remain distinct requirements.
