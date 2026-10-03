# RPB-108 terminology — logarithmic energy graph

The energy coordinate of a vector in neutralCanonicalLogFormDomain is
sqrt(log(e+|xi|)) times its normalized L2 Fourier transform, represented as an
actual L2 class. Its existence follows from that domain's one-logarithm energy.

The energy graph embeds the vector as (physical L2 class, energy L2 class).
The graph norm is the product L2 norm, hence the maximum of the two coordinate
norms. It is a concrete norm function stronger than the physical L2 norm.
This pass does not replace the subtype's inherited L2 topology or assert
completeness of the graph.

This construction contains no source quadratic identity, endpoint operator
identification, spectral-product L2 assumption, or actual carrier membership
witness. It reconstructs the topology candidate needed to keep the source form
space distinct from ordinary L2. The source realization remains to be attached.
