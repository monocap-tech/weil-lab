# RPB108: 96-vector residual Gram and corrected sign

Additive definitions, 2026-10-07 UTC; extends the 96-moment preflight definitions.

- Q96 is the unchanged actual native form's physical 96-vector restriction on degrees 0 through 95.
- R96 is the Gram of the quantized actual source approximation after orthogonal projection away from those same 96 physical basis vectors. Every endpoint-log, smooth and mixed term is retained.
- delta96=eta96(2M96+eta96) is the operator error allowance for the actual source Gram, where M96 bounds the surrogate residual map norm and eta96 bounds the complete source-map error.
- The corrected finite Schur test uses Q96-(500/477)R96-(500/477)delta96 I. Positive native and complement blocks alone do not establish this test.
- Projection nesting is the exact surrogate identity R84=R96 restricted to the original 84 vectors plus the Gram of the 12 newly projected coordinates, when those original source rows are unchanged. It is not an actual full-native negative witness or a replacement for the corrected sign.
- Whole-domain certification, if obtained from that sign and the physical/logarithmic conversions, applies at aperture 97/100. It supplies no global endpoint exclusion, historical attachment, F4 closure or Lean certification.
