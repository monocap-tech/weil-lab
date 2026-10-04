# Terminology: RPB108 native absolute-envelope obstruction

Additive register; historical language is unchanged.

| Term | Definition | Certified consequence / limitation |
| --- | --- | --- |
| Uniform absolute native logarithmic envelope | A real C with abs(M_a(ξ)-w(ξ)) ≤ C for every real ξ | C ≥ w(0)-M_a(0) > 1; independent of the choice of C |
| Zero-frequency envelope deficit | w(0)-M_a(0) | Exceeds one; scalar information, not a supported packet |
| Gårding mass-error coefficient | K_a = NativeLogError a + neutralPhysicalPoleEnergyConstant a | Strictly greater than one |
| Direct absolute-error absorption | Use L ≤ Q_native + K_a m and m ≤ L to infer Q_native ≥ (1-K_a)L | The coefficient is negative; this does not certify positivity or negativity |
| Supported absorption budget | A proved same-domain m ≤ θ_a L together with a sufficient bound K_a θ_a ≤ 1 | A possible independent analytic input, not currently established |
