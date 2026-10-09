# RPB108 DNE15 — Near-critical native residual gate definitions

Definitions registered with their first load-bearing use, 2026-10-09 UTC.

- Native NF24 targets: the exact rational retained vectors x_e,x_o and frozen two-high corrections in the byte-authenticated NF24 target ledger, SHA256 6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00. Their independent source branch is read-only.
- Frozen compensated p: x plus the ledger's exact rational correction on H2, degrees112/114 even or113/115 odd. Its tiny remaining H2 pairings are retained.
- Exact H2-compensated p_star: x-C2^-1 Q(H2,x). This is a finite two-high-mode minimizer, not the complete infinite high response.
- S2(x): Q(p_star,p_star), the native two-high-mode Schur energy.
- P2(x): ||P_U L_Q p_star||², U=F112 intersect H2-perp. Exact H2 source coordinates vanish, so P_U L_Q p_star=P_F112 L_Q p_star.
- Compensated leakage ratio R: P2(x)/S2(x), for these positive-energy nonzero targets only. It is a physical-source ratio, not an inverse-weighted reaction or eigenvalue.
- Scalar-floor gate: P2<kappa S2 with kappa=207/1000, sufficient for positivity after paying the unmeasured inverse by its uniform floor. Its failure does not imply failure of positivity.
- Required correlated gain fraction: 1-kappa/R. In CC59's bound, the correlation subtraction G=Z*V^-1 Z must exceed this fraction of P2 to pass on the target. The actual G is not evaluated in DNE15.

Historical terminology is unchanged. All source actions are ORIGINAL signed Weil actions at a=53/50.
