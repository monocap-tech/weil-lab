# RPB108 terminology: actual pole resonance compatibility

Introduced 2026-10-07 UTC, global/F4 lane; historical notation retained.

- A=H+P: complete physical native operator and its pole-free part, as defined in POLE_STRIPPED_CHAIN. This H is not the bounded correction in ACTUAL_LOG_OPERATOR_ATTACHMENT.
- H_e,H_o: restrictions of H to physical even and odd functions on the same window. Their physical operator and form domains are the parity restrictions of the canonical domains.
- H_p^#: inverse on (ker H_p)-perpendicular, extended by zero on ker H_p, for p=e,o. Compact resolvent makes this bounded physical inverse well-defined even when H_p is singular. It is not an inverse of the entire operator.
- E=<c,H_e^#c>, O=<s,H_o^#s>: even and odd pole responses. The even scalar E is used only in the negative-H branch, where c is proved orthogonal to ker H_e. The odd scalar is used at nonnegative contact, where s is proved orthogonal to ker H_o.
- x=H_e^#c, y=H_o^#s: actual response vectors on the same supported physical domain, not retained packets or arbitrary Green preimages.
- Even pole resonance: E=-1/2 in the negative-H branch. Odd pole resonance: O=1/2. These refer to full actual pole normalization, not selected actual negative-source matrices.
- Z=K intersect ker C intersect ker S from POLE_STRIPPED_CHAIN. A negative-H contact forces ker H=Z; no such identity is assumed in the nonnegative-H branch.
