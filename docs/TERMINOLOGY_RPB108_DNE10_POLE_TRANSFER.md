# RPB108 — DNE10 full-source pole transfer

**DNE10:** the exact relation between the complete original signed Weil form Q_a and the genuine original pole-FREE form H_a on a fixed aperture, including the WHOLE infinite high response. This is NOT a finite sampled-high-mode approximation or a new claim that the residual has been evaluated.

At a=53/50, fix a real parity p. Let `E_p` be the physical normalized Legendre degrees <112 of parity p (dimension56), and `F_p=D_a^p intersect E_p^perp`. For even let `m_p(h)=int_I h(x)cosh(x/2)dx` and sign `sigma_p=+1`. For odd let `m_p(h)=int_I h(x)sinh(x/2)dx` and sign `sigma_p=-1`. The complete actual signed form obeys `Q_p=H_p+sigma_p*2 m_p m_p^*`, with no other changes to archimedean or prime terms.

**Pole tail:** `v_p=P_(F_p,L2) psi_p`, where psi_even=cosh(x/2), psi_odd=sinh(x/2). Both satisfy `||v_p||_2<10^-150` at a=53/50, by Taylor polynomials of degrees110 and111, respectively, with explicit uniform remainder and the best-L2 Legendre projection property. This is an ACTUAL pointwise pole-profile estimate, not a bound on any native source/action response.

**Original high operator:** `C_Q=Q_p|F_p` (as closed form), with inherited NF16 physical floor `C_Q>=207/1000 I`. Let `G_Q=C_Q^{-1}` map bounded physical high functionals to the complete high form-Riesz response. Define `beta_Q=<v_p,G_Q v_p>`, so `0<=beta_Q<5*10^-300`. For BOTH parities `1-sigma_p*2 beta_Q>1-10^-299>0`.

**Original signed response:** For low x∈E_p, let `T_Q x∈F_p` be the unique complete high response satisfying `Q(x+T_Q x,z)=0` for every high z. Let `S_Q(x)=Q(x+T_Q x)` and `a_Q(x)=m_p(x+T_Qx)` (the high-corrected pole moment).

**Exact pole-free transfer:**
```
T_H x = T_Q x + [sigma_p*2 a_Q(x)/(1-sigma_p*2 beta_Q)] G_Q v_p,
S_H(x) = S_Q(x) - [sigma_p*2/(1-sigma_p*2 beta_Q)] |a_Q(x)|².
```
These are TRUE full-high Schur identities. The high-response difference satisfies `||T_H x-T_Q x||_2 <=(2/(207/1000)) ||v_p|| |a_Q(x)|/(1-2 beta_Q)`, so it is <`11*10^-150 |a_Q(x)|`.

**Residual transfer:** For any admissible low-plus-finite-high polynomial w=x+y_hat, let `r_Q(z)=Q(w,z)`, `r_H(z)=H(w,z)` on ALL F_p. Then
```
r_H(z)=r_Q(z)-sigma_p*2 m_p(w)<v_p,z>,
||r_H||_(F,D*) <=||r_Q||_(F,D*)+2|m_p(w)|*10^-150.
```
This does NOT estimate `||r_Q||`: NF20 proves that the already measured two high columns cannot establish a useful full residual upper bound. It provides a rigorously small *difference* between Q and H residuals, enabling a common source ledger once a true all-high estimate is obtained.

**DNE10 scope:** no computed full high source Gram, no certified 56x56 reflected LMI, no new whole aperture positivity, no RH/F4 or Lean proof. Concurrent CC/NF branches remain read-only.
