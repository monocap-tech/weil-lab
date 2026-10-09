# RPB108 NF40 terminology

This note adds terminology to NF39 without changing earlier reports.

**Boundary energy defect compression** means the physical 2 by 2 matrix
`D_Y = Y*(A-A0)Y`, for orthonormal boundary Legendre columns Y,
where `A0 = kappa I + V C^-1 V*`, `V = AZ-kappa Z`,
and `C = Z*AZ-kappa Z*Z`. A positive compression is a statement about
these two physical boundary directions. It is not a whole-high spectral gap.

**Joined inverse improvement** means the signed 3 by 3 response matrix
`T = R*(A0^-1-A^-1)R`. Under the NF39 hypothesis `A >= kappa I`,
`A >= A0` and `T >= 0`. Strict positivity of the boundary energy defect
compression does not imply strict positivity, or a usable lower bound,
for T on the joined sources.

**Enclosure-compatible extension** means an exact finite Hilbert model
whose selected rational moments lie in the original certified enclosures.
It does not mean the exact unknown Weil moments, the complete Weil
identities, or the full polynomial-coordinate source geometry are matched.
NF40 leaves Y*R free; its selected values are explicitly synthetic.

**Zero-response extension** is the enclosure-compatible nine-vector
model in NF40 with a positive boundary defect but T=0 on all three
joined source columns. It is an information-sufficiency test, not a
negative original Weil-form certificate.
