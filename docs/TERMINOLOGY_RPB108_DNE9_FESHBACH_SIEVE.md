# RPB108 DNE9 — Actual pole-free finite spectral Feshbach gate

**Parent:** DNE8 at `2f23fd3a2ad504e9c228d61395a48726c382558d`. DNE9 is independent of the active CC/NF numerical heads.

Fix a=53/50, let D_a be the supported logarithmic canonical form domain and H_a be the complete original pole-FREE archimedean-plus-prime form (signed original poles removed ONLY from H). Its physical operator equals J_a-kappa_a I, with every original prime-power translation and boundary killing retained in J_a.

**Physical trial blocks:** E_even and E_odd are the spans of normalized physical Legendre degrees 0,2,...,110 and 1,3,...,111 respectively (each dimension 56). F_p=D_a^p intersect (E_p)^perp in physical L2. The inherited actual pole-free complement bounds are H_even|F_even >=4/25 physical mass and H_odd|F_odd >=17/100 physical mass. The complete pole-free bounded remainder has norm strictly less than 16 on this cap (original archimedean remainder <8 and six active von Mangoldt translation pairs with coefficient sum <4). Therefore H_p|F_p >=1/101 in the canonical D norm for both parities.

**High response T_p(lambda):** For lambda<c_p, c_even=4/25, c_odd=17/100, the unique bounded form-response E_p->F_p solving
```
H_a(T_p(lambda)v,z)-lambda<T_p(lambda)v,z>
    =-[H_a(v,z)-lambda<v,z>] =-H_a(v,z)
```
for all z in F_p. Physical orthogonality kills the lambda cross term. The response lies in the actual infinite high carrier, not in a truncated physical polynomial space.

**Finite Feshbach gate S_p(lambda):** For v,w in E_p,
```
S_p(lambda)(v,w)=H_a(v,w)-lambda<v,w>
       + H_a(v,T_p(lambda)w).
```
The sign agrees with T solving the negative high forcing. The low eigenproblem H_a h=lambda h is equivalent to S_p(lambda)v=0 with h=v+T_p(lambda)v, and v necessarily nonzero. Conversely every such finite-kernel vector gives a supported physical eigenfunction by the closed form/operator representation.

**Finite inertia/rank:** The number of eigenvalues of J_a^p below kappa_a+c_p is at most dim E_p=56, including multiplicity; for lambda<c_p, H_a-lambda is form-congruent to S_p(lambda) plus the positive high block. In particular a genuine null at lambda=0 has multiplicity at most 56 in its parity. The Schur pencil decreases strictly with lambda: d/dlambda<S_p(lambda)v,v>=-||v+T_p(lambda)v||²_2<0 for v!=0.

**Form-dual residual:** For any approximate high response T_hat, define R_v(z)=H_a(v+T_hat v,z), z in F_p, with dual norm in the supported canonical D norm. Then
```
H_a(v+T_hat v)-101||R_v||_(F_p,D*)² <= <S_p(0)v,v>
                                              <= H_a(v+T_hat v).
```
Both bounds are exact consequences of the full infinite-dimensional high coercivity and are VALID only when the residual is paid on ALL F_p, not a finite source prefix.

**Reflected contact matrix:** On odd physical space the normalized odd half-line map U_- identifies odd vectors with L2(0,a). Let B_a be DNE7's bounded reflected original arithmetic Hankel operator, c(x)=cosh(x/2), and M_a=B_a-2|c><c|. DNE8 gives ||B_a||<13. Because a<log3 and sinh a<3/2, ||M_a||<16.

The finite contact sign target is W* M_a W where W=U_-^*(I+T_odd(0)):E_odd->L2(0,a). An original ODD moment-zero null must have v in ker S_odd(0), s(v+T v)=0, and <Wv,M_a Wv><=0. A STRICT positive lower on that finite joint kernel excludes the odd moment-zero first-contact case; it is NOT certified numerically.

**Scope:** DNE9 is a rigorous reduction to a 56-dimensional exact operator pencil plus an infinite high-response residual which remains unmeasured. It is neither an evaluated 56x56 sign certificate nor RH.
