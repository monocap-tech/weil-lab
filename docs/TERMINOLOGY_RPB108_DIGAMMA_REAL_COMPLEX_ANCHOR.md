# RPB-108 terminology — full complex positive-real digamma anchor

- Actual derivative comparison: deriv Complex.Gamma(x)=ofReal(deriv Real.Gamma(x))
  for x>0, proved by restricting complex Gamma and comparing real derivatives.
- Actual positive-real digamma real-valuedness: ψ(x) equals the real Gamma
  derivative divided by real Gamma, so Im ψ(x)=0.
- Full complex positive-real Euler anchor: a complex HasSum and equality
  ψ(x)=-γ+∑' n,[1/(n+1)-1/(x+n)] at every real x>0.

The equality is full complex equality on the real axis. Identification on the
right half-plane and source-line residual cancellation remain separate.
Historical wording is immutable; no Gauss representation is assumed.
