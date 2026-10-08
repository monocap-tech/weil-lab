# RPB108 — Native dilation virial audit for the boundary-contact alternative

Date: 2026-10-08. Active Coupled branch. Follows [boundary-contact alternative](REFLECTED_PACKET_BRIDGE_108_BOUNDARY_CONTACT_ALTERNATIVE_20261008.md) and CC27's exact native formula. **Classification: exact smooth-core identity and sign discrimination, not exclusion of a zeta null mode.** Original signed poles, every prime-power coefficient and both translations are retained.

## 1. Dilation without an old-gap denominator

Let nonzero f in C_c^infinity(-1,1) and h_s(x)=s^(-1/2) f(x/s). Set ell_n=log n, c_n=Lambda(n)/sqrt(n), a_arch(xi)=Re psi(1/4+i*pi*xi)-log pi. With the repository's unitary Plancherel convention, CC27's complete original form gives

    Q_s(h_s,h_s)=A_f(s)+P_f(s)+H_f(s),
    A_f(s)=integral_R a_arch(eta/s) |F f(eta)|² d eta,
    C_f(d)=Re integral_R conjugate(f(u)) f(u+d) du,
    P_f(s)=-2 sum_{ell_n<=2s} c_n C_f(ell_n/s),
    M_+(s)=sqrt(s) integral f(u) exp(+su/2) du,
    M_-(s)=sqrt(s) integral f(u) exp(-su/2) du,
    H_f(s)=2 Re(conjugate(M_-(s)) M_+(s)).             (1)

For any finite s this is a FINITE prime sum. Because f is compactly supported, a term with ell_n>=2s vanishes exactly. No tail of active primes is omitted. The f-specific positive test norm is constant: ||h_s||_physical=||f||_physical. Equation (1) is an identity of the actual native form on this smooth template; it does not assume Q_s>=0.

## 2. Rigorous archimedean dilation sign

The trigamma series for Re z>0 yields, for xi>0,

    a_arch'(xi)= 2*pi²*xi sum_{k>=0}
       (k+1/4) / [((k+1/4)^2+pi²*xi²)^2] > 0.     (2)

The symbol is even, hence xi*a_arch'(xi)>0 for every xi!=0. Differentiation under the integral in (1) is justified for smooth compact f by rapid Fourier decay and the bounded logarithmic symbol derivative. Therefore

    A_f'(s)= -1/s² integral_R eta*a_arch'(eta/s)
                              |F f(eta)|² d eta < 0.   (3)

Strictness follows because a nonzero f has nonzero Fourier mass away from eta=0. Thus the full original archimedean term always **decreases under outward dilation**; it does not provide a positive virial obstruction to contact by itself. This is an exact all-s statement, not a sampled numerical derivative.

## 3. Prime translation derivative: no universal sign

Away from, and by smooth flat extension across, prime-support thresholds, differentiating each active term gives

    P_f'(s)=(2/s²) sum_{ell_n<=2s} c_n ell_n C_f'(ell_n/s). (4)

For real even, nonnegative, symmetric unimodal f, its autocorrelation C_f is nonincreasing for positive d, so P_f'(s)<=0. A concrete admissible H_0^1 template (approximable on the logarithmic core) is f(u)=cos(pi*u/2) for |u|<1 and zero otherwise. Here for 0<=d<=2,

    C_f(d)=(1-d/2)cos(pi*d/2)+sin(pi*d/2)/pi,
    C_f'(d)=-(pi/2)(1-d/2)sin(pi*d/2)<0 (0<d<2). (5)

Every active prime term consequently drives this particular test's energy downward as support expands. This is a genuine arithmetic-coefficient example, but the template is **not** an actual contact eigenfunction. Oscillatory/complex templates have no fixed autocorrelation derivative sign, and the argument cannot be applied to unknown native critical vectors.

## 4. Pole virial has opposite parity tendencies

For real even nonnegative f, M_+=M_->0 and both grow in absolute value with s, since their common integral is sqrt(s) integral f(u)cosh(su/2)du. Hence H_f(s)>0 and H_f'(s)>0. The original **even pole opposes** the negative arch and monotone-bump prime dilation signs.

For real odd f positive on (0,1), M_-=-M_+ and M_+(s)=2sqrt(s) integral_0^1 f(u)sinh(su/2)du>0 strictly increases. Hence H_f(s)=-2 M_+(s)^2<0 and H_f'(s)<0. The original **odd pole reinforces** the negative archimedean dilation tendency for such templates. These are the CC35 signed CROSS poles, not two positive squares.

The even cosine example has M_+=M_-=sqrt(s)*4*pi*cosh(s/2)/(pi²+s²), so its pole diagonal equals 2s[4*pi*cosh(s/2)/(pi²+s²)]² and its derivative is strictly positive by the integral argument. Odd f may be chosen smooth, e.g. u*exp(-1/(1-u²)) in |u|<1, zero outside.

## 5. Contact target and falsification rule

The boundary-saturation lemma says any nonzero null mode at a nonnegative cap touches BOTH physical endpoints. It does **not** guarantee that the mode is smooth enough for (1)-(4), nor that its prime autocorrelations are unimodal. To use this alternative one must (a) justify a smooth-core limit of complete signed first differences uniformly on contact candidates, (b) use their exact Q_a(h,.)=0 equation, and (c) prove an arithmetic-specific sign relation strong enough to contradict strictly positive prior apertures.

At a hypothetical first contact a*, an inward dilation of a null h satisfies Q_s(U_{s/a*}h)>0 for every s<a* by strict old-cap positivity. Thus any proved original-zeta contact equation forcing the same signed quantity negative for some inward s would exclude that contact. This is a DIFFERENT sufficient route from CC19's inverse old-gap covariance, but no such arithmetic relation has been proved. A sign estimate only on arbitrary smooth f, or a claim of smoothness without domain proof, is insufficient.

**Decision from (3)-(5):** Reject a universal favorable-sign virial shortcut. The actual archimedean term is strictly decreasing in aperture; prime shifts can reinforce it; the pole sign depends on parity. A viable direct-contact theorem must estimate their **joint** correlation on contact solutions, preserving zero-level vs shifted-positive discrimination. Compare the genuine H_0^1 differential crossing, which has a boundary-saturated null at a=pi/2 and an inward-dilation positive margin: it defeats a structural argument based only on dilation and endpoint saturation.

No new aperture certificate, old-gap-independent shell estimate, global contact exclusion, RH/F4 or Lean result follows. No numerical validator is asserted; formulas above are analytic core identities and exact test calculations. The highest internally whole-positive original aperture remains 21/20; NF10's 53/50 complement and NF11's prime-only low8 handoff are not whole-aperture positivity.
