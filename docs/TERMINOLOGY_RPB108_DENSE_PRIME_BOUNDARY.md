# RPB108: dense prime paths and the full-line inversion boundary

- Physical interval: I_a=(-a,a), with unchanged zero extension of the physical vector.
- Prime path graph: vertices in [-a,a]; an edge joins x to x+/-log n when both vertices remain in that closed interval and n is an active prime power. This is an admissible translation graph, NOT the singular support of a solution.
- Boundary-generated reachable set: vertices reached from a by a finite admissible word. Endpoint seeds are geometric; all noninitial vertices in the rotation construction lie in the open interval.
- Rotation strip: alpha=log 2, beta=log 3, L=alpha+beta=log 6, J=[a-L,a]. In coordinate y=a-x, rotation is y -> y+alpha for y<beta, and y -> y-beta for y>=beta.
- Full-line prime operator: T_full=sum_(log n<=2a) w_n(tau_(log n)+tau_(-log n)), w_n=Lambda(n)/sqrt(n). Its restriction to I_a agrees with the frozen native prime action on supported vectors. Its full-line Fourier multiplier is t_a(xi)=2 sum w_n cos(2 pi xi log n).
- Tau bound: tau_a=2 sum w_n, a finite full-line operator bound on every Fourier-weighted Sobolev space. It is not a sharp supported prime norm.
- High-frequency carrier: H_R^s={u in H^s(R): Fourier(u)=0 on |xi|<R}. P_R is its Fourier projection; w(xi)=log(e+|xi|). Choose R with ell_R=log(e+R)-C0>tau_a, using the pinned bound |m0-w|<=C0.
- Compact pole extension: eta in C_c^infinity equals one on a neighborhood of [-a,a], and eta p_h is the unchanged actual pole on I_a. F_h=(m0(D)-T_full)h+eta p_h is the full residual with this explicitly chosen compact extension. Exact full-nullity implies F_h vanishes on I_a. No enlarged physical nullity is claimed.
- Failed finite closure premise: a finite frozen prime list implies finitely many boundary-generated profile locations. This premise is false at every possible first-contact aperture in the current lane.
- Failed full-line inversion step: high-frequency invertibility of m0-T_full implies supported critical nullity promotes to H1. The missing exterior residual estimate, not a high-frequency zero of the joint multiplier, blocks this step.
