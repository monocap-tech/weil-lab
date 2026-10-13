# RPB108: exact endpoint-log Gram and regularized coupled pilot

## Terminology and result

The **endpoint-log source component** is v_i(x)L(x), where v_i=sqrt(2i+1)P_i(2x) and L(x)=-(1/2)log[(x+1/2)(1/2-x)]. The **endpoint-log residual Gram** is the physical Gram of these eight components after removing physical Legendre degrees 0..63. It is one component of the actual full-source residual Gram, not the entire Gram.

Every entry of this eight-by-eight residual Gram is now rigorously enclosed by rational intervals with width below 10^(-35). This isolates the singular part responsible for the previous direct quadrature disagreement. A new pilot combines it with regularized mixed quadrature; the latter remains uncertified.

## Exact moment identities

Set t=x+1/2 and write p_i(t)=P_i(2t-1). All coefficients are rational. Put H_n=sum_(j=1)^n 1/j and H_n^(2)=sum_(j=1)^n 1/j^2. For k>=0, n=k+1,

integral_0^1 t^k L(t)dt = (1/2)[1/n^2+H_n/n].

For the squared log component,

integral t^k log^2(t)dt=2/n^3,
integral t^k log^2(1-t)dt=[H_n^2+H_n^(2)]/n,
integral t^k log(t)log(1-t)dt=H_n/n^2-[zeta(2)-H_n^(2)]/n.

The first two follow respectively by differentiating the elementary power integral and the beta integral twice in its second parameter at b=1. The mixed identity follows by differentiating the beta integral once in each parameter at (a,b)=(n,1): the logarithmic first derivatives are -1/n and -H_n, and the mixed second logarithmic derivative is -[zeta(2)-H_n^(2)]. The log factors are integrable and justify differentiation by domination. Zeta(2)=pi^2/6 is enclosed with the existing rational Machin pi enclosure.

Thus if p_i p_j=sum a_k t^k, the full unnormalized log Gram is a rational affine expression in zeta(2). The projection coefficient against degree n is the exact rational

b_ni=integral_0^1 p_n(t)p_i(t)L(t)dt.

The exact unnormalized residual Gram entry is

integral p_i p_j L^2 - sum_(n=0)^63 (2n+1)b_ni b_nj.

Multiply by sqrt[(2i+1)(2j+1)] to obtain the normalized physical entry. Rational interval square roots and outward rounding complete the enclosure. Opposite-parity entries vanish exactly. Polynomial products through degree 70, all harmonic sums and projection subtractions are evaluated rationally before any floating display; this avoids unstable monomial cancellation.

## Certificate and checks

`scripts/certify_native_endpoint_log_gram.py` uses Python's standard library and the existing rational helper functions. Output: `notes/data/RPB108_ENDPOINT_LOG_GRAM_CERTIFICATE_20261005.json`. It checks every entry width below 10^(-35). Its degree-zero diagonal agrees with the previous exact endpoint-log tail and is bounded above by 1/64^2.

Approximate diagonal displays are 0.000123977, 0.000360664, 0.000620809, 0.000843576, 0.001121354, 0.001331394, 0.001628659, 0.001827032. These are displays of enclosed entries, not Schur eigenvalues.

## Improved actual-source pilot

Write the actual source map V=V_L+V_H, with the endpoint-log component just enclosed and the remaining source containing the smooth H(d), regular arch difference integrals, same-vector pole moments and actual prime translates. On each prime-split panel, the latter source is smooth through both panel endpoints.

For the mixed integral integral v_i L(V_H)_j, subtract the linear endpoint interpolant of (V_H)_j on that panel. Integrate the interpolant term using explicit antiderivatives of t^k log t and t^k log(1-t); evaluate the remaining vanishing-endpoint product with Gauss quadrature. Its singularity is weaker than the unregularized source product. The smooth residual Gram is evaluated separately. The full Gram reconstruction retains all cross terms:

R=R_L+R_H+[integral V_L*V_H-C_L* C_H]+its adjoint.

Here C_L and C_H are the first-64 projection matrices. Omitting these mixed terms would change the actual source Gram. C_L comes from the exact rational moments. All slots retain the same physical trial vectors.

`scripts/explore_native_log_separated_residual.py` implements this reconstruction. It is exploratory: the regular and mixed Gauss integrals, elementary antiderivative arithmetic and finite eigenvalue evaluation are floating and have no rigorous error enclosure yet. Output: `notes/data/RPB108_LOG_SEPARATED_RESIDUAL_PILOT_20261005.json`.

| Outer nodes per panel | Source-pairing discrepancy | Smallest lower-pilot eigenvalue |
|---|---:|---:|
| 128 | 4.87943e-14 | 4.9392048e-6 |
| 256 | 4.59632e-14 | 4.9392006e-6 |

The residual Gram repeat-norm display is 2.50463e-8, compared with 1.14217e-4 for the previous direct 512/1024-node pilot. This is a substantial numerical improvement obtained from exact singularity treatment; it is not a remainder estimate. The constant residual squared display tends to approximately 0.001238011, consistent with the previous slower direct pilot.

## Remaining precision input

The endpoint-log Gram itself is closed. The remaining arithmetic consists of rigorous smooth-source approximations and mixed integral/error enclosures, including actual prime panel endpoints and inner arch difference integrals. The established source-map or correlated matrix error criterion then determines whether the positive displayed eight-source margin is certified. Repeat agreement alone still does not provide that error.

The full 64-dimensional Schur sign is not certified; even closing this eight-source corrected restriction would leave 56 coordinates. No full carrier contraction, actual negative/null witness, global endpoint exclusion or signed endpoint-null Gaussian upper estimate is asserted. F4 entry and FULL TRANSPORT CLOSED remain open. The previously certified constant-linear corrected block remains valid. Lean source/checkpoint and CI claims are unchanged.
