# RPB108 terminology: local finite source matrix

Introduced with REFLECTED_PACKET_BRIDGE_108_LOCAL_FINITE_SOURCE_MATRIX_20261006.md.

- **Fixed dilation carrier H:** D_1, with physical realization U_t h at aperture t; it is used to compare varying forms and does not preserve the physical vector across t.
- **Local fixed selection s:** one finite set of actual negative divisor coordinates, selected at a nonnegative null window c and retained for nearby apertures.
- **Effective covariance G_s(t):** A(t)+R_s(t)^*R_s(t), where A(t) is the full native form and R_s(t) is actual selected analysis after dilation.
- **Finite source matrix D_s(t):** I-R_s(t)G_s(t)^(-1)R_s(t)^* on l2(s), defined where G_s(t) is coercive. Its positivity, negative index and nullity match the complete native form.
- **Minimal selection:** r independent actual coordinate rows on ker A(c), with r=dim ker A(c). Copy cardinality alone does not establish independence.
- **Fixed-coordinate positive factor S(t):** G_s(t)^(1/2) on H. It is unitarily related to the actual WD-T10 effective synthesis on its positive coefficient range; it does not assert raw Green coefficients.

The finite matrix still contains an inverse on an infinite Hilbert carrier. Its existence is not a computed numerical certificate, independent arithmetic rigidity, a first-jet estimate, or an identification of the historical fixed packet.
