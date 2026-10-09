# DNE16 terminology: native high-source correlations

Use the original physical even or odd carrier on [-a,a], a=53/50, and its canonical form Q with polynomial source L_Q. The normalized physical Legendre modes are e_n. The inherited original high floor is kappa=207/1000; no source-square matrix is substituted for the high form.

| Symbol | Definition |
|---|---|
| E | The 56 retained modes, even 0..110 or odd 1..111 |
| H2 | Measured high modes (112,114) even or (113,115) odd |
| U | Physical orthogonal complement of E+H2 |
| p_star=T x | Exact H2-compensated NF24 retained target |
| sigma | P_U L_Q p_star; its H2 coordinates vanish |
| K_j | P_U L_Q e_hj, j=0,1 |
| P2 | <sigma,sigma> |
| Z_j | <K_j,sigma> |
| H_jk | <K_j,K_k> |
| C2 | Native Q(e_hj,e_hk), inherited authenticated CC60 intervals |
| W0 | C2(C2-kappa I), strictly positive |
| V | W0+H, strictly positive |
| G | Z^* V^-1 Z, optimized correlation gain |
| J(y) | ||sigma-K y||²+y^*W0 y, for a fixed exact rational two-vector y |
| J_min | P2-G, minimum of J over all real two-vectors |
| S2(x) | Q(p_star,p_star), finite compensated target energy |
| T_rest | True remaining reaction <sigma,D_eff^-1 sigma> |

CC59 gives T_rest <= J_min/kappa, and CC60 gives T_rest <= J(y)/kappa. A passing directional certificate requires J(y)<kappa S2(x). If J_min>kappa S2(x), every two-vector trial fails this sufficient estimator on x. Such failure does not determine the actual T_rest or the full Schur sign.

The joint 3-by3 Gram is ordered (sigma,K_0,K_1). It is directional data for one NF24 x per parity. It is neither a full retained 56-by56 matrix nor the full infinite high inverse. The finite source approximation is projected onto U by removing all 58 same-parity coordinates before the operator-tail payment. Source errors are measured in physical L² norm, and projection is a contraction.

The original source is written L_Q p=U_p-(p/2)log(a²-x²), where U_p includes the constant archimedean term, exact harmonic singular action, regular convolution, clipped signed prime translations and signed pole terms. Each sector is added before any source products are formed. A larger regular Taylor order changes only the approximation and paid tail, not the original form.
