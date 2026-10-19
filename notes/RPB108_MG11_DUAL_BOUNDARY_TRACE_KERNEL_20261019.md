# MG11 — Dual endpoint traces: original odd rank TWO and 23-dimensional cancellation

October 19, 2026 — Method Gate. The original signed Fourier/closed-domain identification and full odd/even/Weil/CC27/RH remain OPEN. Stacks on fully passing MG10 (#259).

## Why MG10 does not finish strong residual certification

MG10 successfully paid the full original 25-source leading endpoint jump, exhibiting a complete signed-source-independent rank-one plus scalar strong positive high-tail upper bound and an exact 24-dimensional jump-vanishing source subspace. Its original Fourier asymptotic rate on that kernel is 1/xi^2 amplitude, strong squared tail O((log Lambda)^2/Lambda^3). The full source MG10 bound is sharply conservative at cutoff 4096: 96902.63 versus original SM41 2.73869, though it improves at 2^20 and 2^24. That is a valid method gate and does not imply the full original operator can be certified cheaply.

MG11 asks whether the SAME physical common boundary support and parity makes a second cancellation possible. All 25 SI10 original odd physical pilot sources are smooth INSIDE the common [-B,B], B=11/10, and satisfy f(-B)=-f(B), f'(-B)=f'(B). Thus both leading endpoint Fourier jumps lie in the span of only TWO original source boundary functionals, b_j=f_j(B) and d_j=f_j'(B).

## Exact two-trace original Fourier identity

For each zero-extended original odd physical source and omega=2*pi*xi, integrate by parts THREE times:

T_f(xi)=
 - J0_f(xi)/(i omega)
 - J1_f(xi)/(i omega)^2
 - J2_f(xi)/(i omega)^3
 + (i omega)^-3 * integral[-B,B] f'''(x) exp(-i omega x) dx,

Jr_f(xi)=f^(r)(B) exp(-i omega B)-f^(r)(-B) exp(i omega B).

Because f is odd and f' even, J0=2 f(B) cos(omega B) and J1=-2i f'(B) sin(omega B). The ENTIRE second-order-peeled remainder E2 starts with J2 and is bounded by

 |E2_f(xi)| <= D3_f/(2*pi*|xi|)^3,

 D3_f = |f''(B)|+|f''(-B)|+integral[-B,B]|f'''|.

Actual original rational derivative majorants for all selected sources use SM42 certified phase intervals, true rational SI10 centers, pi upper and genuine B:
- sin(w x): D3<=2w^2+2B w^3;
- x cos(w x): D3<=4w+8B w^2+2B^2 w^3;
- odd sinh(x/2) pole: D3<=sinh(B/2) exactly, upper-rounded by the true SM42 sinh interval.

No boundary term is silently erased, no numerical Fourier values are accepted, and no high-degree 470-source majorant is claimed.

## Independent original derivative-trace rank certificate

Use SM42 exact rational Taylor phase/sinh/cosh intervals for b_j and d_j for all 25 generators:
  b_sin=sin(wB),        d_sin=w cos(wB)
  b_xcos=B cos(wB),    d_xcos=cos(wB)-B w sin(wB)
  b_pole=sinh(B/2)>0, d_pole=(1/2)cosh(B/2)>0.

Choose a genuine nonpole pivot q with SM42 rational interval

 Δ = b_pole d_q - b_q d_pole

strictly separated from zero. Consequently the original 2×25 boundary trace map [b;d] has EXACT rank TWO, and its 23-dimensional coefficient kernel admits explicit original supported functions

 h_i=f_i-a_i s-c_i f_q, for i distinct from q and pole,

 a_i=(b_i d_q-b_q d_i)/Δ,
 c_i=(b_pole d_i-b_i d_pole)/Δ.

These coefficients are the **true analytic endpoints**, not interval midpoints. Exact rational upper bounds on |a_i| and |c_i| follow from strict interval determinant gap, giving D3'_i = D3_i+|a_i|_upper D3_pole+|c_i|_upper D3_q. All 23 h_i satisfy h_i(±B)=h_i'(±B)=0. Physical independence is inherited from SM42's strictly positive complete physical 25-source Gram.

## Rigorous COMPLETE source25 high tail

SM41 original positive multiplier a_o(xi)<=17+ln|xi| for |xi|>=1. Let Lambda=2^k and v=17+k(347/500). Exact whole-real integral bounds give:

* the original MG10 endpoint VALUE covariance weight mu0(Lambda), multiplied by (b·z)^2;
* the endpoint DERIVATIVE covariance weight
  mu1(Lambda)=[v^2/3+2v/9+2/27]/[162 Lambda^3], multiplied by (d·z)^2;
* the complete THIRD-REMAINDER positive strong squared-tail bound
  C3(Lambda)=[2 sum_j D3_j^2 /(6^6 Lambda^5)]
              [v^2/5+2v/25+2/125], multiplied by ||z||^2.

By the *complete source* three-term Cauchy inequality and two exact rational endpoint interval enclosures b=bmid+be, d=dmid+de, eta=1/64, the original high positive action satisfies a fully paid **rank-two-plus-diagonal whole-25D Loewner upper**:

 Q_tail <= 3(1+eta)mu0 bmid bmid^T
         +3(1+eta)mu1 dmid dmid^T
         +3[(1+1/eta)(mu0||be||²+mu1||de||²)+C3] I_25.

Every original physical mixed source cross survives in the two rank-one matrices. Exact-rational outward bounds control sine/cos/omega and pole endpoints. There is no lower-band, original full strong Galerkin residual, source470 or RH promotion.

On the EXACT true 23D dual trace kernel, both jumps vanish, so the ENTIRE original strong Fourier source action has a valid scalar upper C3'(Lambda)=O((ln Lambda)^2/Lambda^5), in the basis of the 23 explicit h_i and with D3'^2=sum (D3'_i)^2. The entire 23D positive source Gram is not the identity; the coefficient-basis upper cannot be silently treated as a physical L2 normalized eigenvalue estimate.

Formally, because the original 470 odd SI10 generator family includes these two independent physical original pilot traces and shares the same support, the whole source470 trace map also has rank two and a 468-dimensional kernel. Only source25 derivative norm bounds are established here.

## MG11 method acceptance

Dedicated exact-rational GitHub Actions must check all actual source centers, 25 endpoint pairs, pole strict positivity, strict q-pole two-trace determinant interval, exact 23-dimensional kernel, all 25 rational third-derivative majorants, positive whole-25 rank2-plus-I Loewner terms, original SM41 direct full-tail comparisons, and 11 cutoff checkpoints. Critically an asymptotic O(Lambda^-5) gain **does not guarantee** improvement at Lambda=4096; record exact comparisons with old SM41, never assume them. The finite-cutoff numerical result determines whether to continue direct endpoint cancellation or first reduce the third-derivative constants by source-adapted exact analytic transforms.

The next theorem-level acceptance remains certified *original* low-frequency strong action and coupled Galerkin residual, complete physical Gram and SI29 reference, full 470-source negative cap and inverse, and complete even/Weil transfer. Neither this finite tail nor an indefinite signed lower reference is an RH proof.

Reproduce: python scripts/validate_rpb108_mg11_dual_boundary_trace_kernel.py.
