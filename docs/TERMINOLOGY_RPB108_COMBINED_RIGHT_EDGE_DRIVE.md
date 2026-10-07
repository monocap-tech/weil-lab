# RPB108 terminology: combined right-edge drive

Date: 2026-10-07 UTC. Additive definitions.
- f_h(v)=h(a-v), 0<v<2a, is the unchanged physical right-edge profile.
- K_E(s)=exp(-s/2)/(1-exp(-2s)), s>0, is the actual off-support archimedean Euler kernel.
- k_reg(s)=K_E(s)-1/(2s) is its bounded continuous remainder on a fixed compact positive range, extended at zero by k_reg(0)=1/4.
- A_h(u)=p_h(a+u)-sum_(log n<=2a) Lambda(n)/sqrt(n) h(a+u-log n)-integral_0^(2a) k_reg(u+v)f_h(v)dv is the combined edge drive for 0<u<log 2.
- F_pole^edge(t)=Re integral_0^t p_h(a+u) conjugate(f_h(t-u))du is a local collar pairing. It is distinct from the global translation correction (cosh(t/2)-1)Ppole(h).
- This does not supply an injective inverse-boundary scalar, an actual null vector or a same-vector support enlargement.
