# RPB108: matched Carleman quadratic identity

Registered 2026-10-07 before first load-bearing use.

- Fix the unchanged actual h in K_a intersect Xcrit. On a right collar write f(v)=h(a-v), C(u)=integral_0^(2a) f(v)/(u+v)dv, r(u)=A_h(u)-C(u)/2, A0=A_h(0), and M=2A0. The pinned signed matching theorem proves C(u)->M and the signed inverse moment equals M. This does not define an absolute inverse integral.
- For u>0 the ordinary derivative C'(u)=-integral_0^(2a) f(v)/(u+v)^2 dv is well defined. Each fixed u has a nonsingular integrable kernel. No physical derivative h' is used to define C'.
- d(u)=A_h(u)-A0 is the actual drive variation. It is not an independent comparison drive. Its squared Hardy budget with weight 1/[u log(1/u)] is finite by the pinned matching theorem.
- J_delta=Re integral_0^delta r(u) integral_0^(2a) conjugate(f(v))/(u+v)^2 dv du is the rectangular residual pairing. The two-variable integral is absolutely convergent by the pinned absolute-collar proof plus its separated outer region. It differs from the triangular native translation flux integral because v spans the entire source support independently of u.
- The matched Carleman quadratic identity is J_delta=(1/4)|C(delta)-M|^2-Re integral_0^delta d(u) conjugate(C'(u))du. Its last integral is absolutely convergent. The combined identity is justified by fixed positive cutoffs followed by the lawful signed boundary limit, without requiring absolute integrability of C C' or A0 C'.

Scope: a boundary identity conditional on already proved critical membership/matching properties of actual null vectors. It is not a scalar injectivity statement, a derivative estimate, an arithmetic bound, enlarged null transport, or F4 closure.
