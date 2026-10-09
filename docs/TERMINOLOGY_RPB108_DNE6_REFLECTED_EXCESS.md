# RPB108 — DNE6 reflected half-interval excess

**DNE6** studies an exact same-parity reformulation of DNE4's complete original pole-free weighted jump form. It does NOT import Coupled's signed source-Schur response or promote finite Aperture certificates to a full original sign.

Let a>0, phi=phi_a be the normalized, positive-a.e., bounded, even pole-free ground state of H_a with eigenvalue lambda0(a). When investigating a possible non-ground H-null, lambda0(a)<0; put d_a=-lambda0(a)>0.

For 0<x<a define the **reflected pointwise potential**
`V_a(x)=2 [int_0^a j(x+y)phi(y)dy]/phi(x)` wherever phi(x)>0. It is defined a.e., can be unbounded, and is not assigned a numerical value without the ACTUAL ground state.

Let `u` be real odd in DNE4's complete weighted form domain. Its positive-half restriction is also denoted u.

**Exact reflected excess:** `W_phi(u)=int_-a^a V_a(|x|)phi(x)^2 u(x)^2 dx + X_a(u)`, where
```
X_a(u)=
 int_(0,a)^2 phi(x)phi(y)[j(|x-y|)-j(x+y)](u(x)-u(y))² dxdy
 +2 sum_(ell_n<a) c_n int_0^(a-ell_n)
       phi(x)phi(x+ell_n)(u(x)-u(x+ell_n))² dx
 +sum_(ell_n<2a)c_n int_(max(0,ell_n-a))^(min(a,ell_n))
       phi(z)phi(ell_n-z)(u(z)+u(ell_n-z))² dz.
```
All original prime powers with ell_n=log n<=2a and both shift orientations are represented. Empty interiors contribute zero. Every summand is nonnegative, because j is strictly decreasing and |x-y|<x+y on (0,a)^2.

**Null-deficit identity:** If H_a h=0 with odd h and u=h/phi, then
`X_a(u)=2 int_0^a [d_a-V_a(x)] phi(x)^2 u(x)^2 dx`.
This is a necessary identity; it does not assert that any such null exists.

**Non-strict reflected-floor exclusion:** If `2a>log2` and `V_a(x)>=d_a` almost everywhere on (0,a), then there is NO nonzero odd pole-free H_a-null. Equality is excluded by the strictly positive continuous same-side difference kernel, which forces u constant on positive half if X=0, followed by the strictly positive original prime2 cross-origin bridge, which rules out a nonzero constant.

**Deficit-set necessary condition:** Any odd H-null for 2a>log2 forces the set `{x in (0,a):V_a(x)<d_a}` to have positive measure. Thus the actual spectral obstruction must live in a REFLECTED-LOW-POTENTIAL region.

**Interior oscillation bound:** For 0<delta<a, `alpha_(a,delta)=j(a-delta)-j(a+delta)>0`. Set `S_delta=int_delta^a phi` and `m_delta=[int_delta^a phi*u]/S_delta`. Every odd null satisfies
```
alpha_(a,delta)*S_delta*int_delta^a phi(x)(u(x)-m_delta)^2 dx
 <=int_0^a (d_a-V_a(x))_+ phi(x)^2 u(x)^2 dx.
```
This constrains shape on interior collars, but supplies NO full arithmetic deficit estimate, since phi and V remain unevaluated.

**Falsifier:** A positive cross-origin prime bridge increases excess energy but does not alone forbid a higher odd zero: finite reflected graph models can be tuned so a higher zero survives with V<d on some nodes. The non-strict V>=d condition is sufficient, NOT necessary.
