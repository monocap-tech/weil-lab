# RPB108 DNE14 — Complete compensated constant residual interval certificate

Date: 2026-10-09 UTC / continuation of the 2026-10-08 Pacific session. Independent DNE parent 0dd390a467a887828d83dff030c17d5d6745cf28. [Definitions](../docs/TERMINOLOGY_RPB108_DNE14_SCALAR_SOURCE_CERTIFICATE.md). No other branch modified.

## New arithmetic checkpoint

At a=53/50, fix the DNE13 trial

    w=e0+(7094302/10^9)e112-(5131477/10^9)e114.

The complete ORIGINAL signed native source is integrated before squaring, retaining its archimedean, six prime-power and even pole correlations. All56 retained even Legendre projections e0,e2,...,e110 are removed. Neither remaining high pairing with e112/e114 is replaced by zero.

The executed directed-interval computation establishes the convenient outward bounds

    0.0039512 < P(w)=||(I-P_E)L_Qw||²_2 < 0.0039514,
    0.0399313 < Q(w,w) < 0.0399315.

These are actual-source inequalities after paying the entire regular-kernel and pole truncation error. They are not Gauss convergence estimates. The machine-readable records retain the narrower decimal endpoints from both runs.

With the inherited full ORIGINAL signed high coercivity C_Q >=207/1000 (DNE10 equation2, sourced there to NF16/NF20), completing the whole high square gives

    S_Q(e0,e0)=Q(w,w)-<r,C_Q^-1 r>
             >=Q(w,w)-(1000/207)P(w)
             >0.02084.

The last rational inequality is checked directly from the outward bounds above. Thus the scalar constant low line remains strictly positive after the ENTIRE infinite-dimensional high response. This is a stronger conclusion than positivity of a finite three-mode trial or a numerical residual comparison.

## Construction and analytic error ledger

The DNE11 source formula is used exactly in structure:

    s_Q(p)=U_p(x)-(1/2)p(x)log(a²-x²),

where U is a polynomial on each ORIGINAL prime-translation panel after paid smooth-kernel and pole truncation. The singular polynomial action is D[e_n]=H_n e_n; the identities through n114 were independently checked in DNE13. Every active prime n in {2,3,4,5,7,8} has both original zero-extended translation orientations and coefficient Lambda(n)/sqrt(n). Even parity reduces the original pole source exactly to 2 cosh(x/2) int p(y)cosh(y/2)dy.

The first run uses the rational regular-kernel expansion r_128. The independent higher-order replay uses r_160. Both use the degree64 cosh Taylor polynomial in the output profile AND moment. From DNE11,

    delta_N=(550/19)(106/125)^N,
    epsilon_N=[2a delta_N+3e-99]||w||_2,
    ||s_Q(w)-s_N(w)||_2 <=epsilon_N.

For N128 the source error is below4.195e-8; for N160 it is below2.145e-10. This error is independent of the polynomial degree. No native high-response convergence assumption is used.

For the computed truncated source-square T_N and projected square P_N, orthogonal projection is a contraction, so

    |P(w)-P_N| <=epsilon_N(2 sqrt(T_N^upper)+epsilon_N),
    |Q(w,w)-<w,s_N(w)>| <=epsilon_N ||w||_2.

These payments are explicitly added to the interval endpoints before the gate is compared. T_N is the full physical source norm, not a sum of separate source-sector norms.

The polynomial part is integrated by exact primitive formulas evaluated with directed Decimal intervals. The log cross terms use finite primitives of t^k log t after substituting t=a+-x. The log² term is integrated across the whole interval using beta-derivative moments (DNE11 equations20–21). Every endpoint t=0 uses its exact analytic limiting primitive0; no endpoint strip is discarded.

An EVEN input still has ODD monomials in U on individual prime panels. The computation keeps all those monomials in the U p log cross term. Treating each positive-half panel polynomial as even would be incorrect. Complete-interval log² and p e_j log coefficients themselves remain even.

## Directed constants and cancellation controls

Only the Python standard library is needed. Basic arithmetic uses separate ROUND_FLOOR and ROUND_CEILING Decimal contexts. Decimal ln and sqrt are correctly rounded to nearest; their enclosing endpoints are widened by one representable neighbor in the working precision. Rational coefficients and bounds are converted with directed division.

Pi is enclosed by Machin's formula16 atan(1/5)-4 atan(1/239), with400 exact Fraction alternating-series terms and their exact remainder bounds. Euler's constant is enclosed from H_100-log100-1/200 plus the first80 Bernoulli terms, with a symmetric first-omitted-term remainder |B162|/(162*100^162). The Euler–Maclaurin remainder bound follows by expanding the positive-integral denominator in Binet's digamma formula; the remainder has the first omitted sign and magnitude bounded by its term. The gamma enclosure width is below1.504e-166.

This tighter constant enclosure matters because prime-translated monomial coefficients can be enormous before cancellation. Increasing Decimal precision alone does not cure a fixed transcendental-input uncertainty amplified coefficientwise. Preliminary low-precision/wider-gamma attempts were inconclusive and were corrected before this certificate.

The primary run uses280 Decimal digits, the N160 replay320. Both integrate all seven positive-half panels and reflect the physical integral. Each run checks115 complete half-interval even log moments against independent beta-derivative formulas, plus the odd x log moment against its closed form:116 consistency checks per run.

A separate Fraction validator passed796 assertions: independent split-convolution formulas, transformed log-primitive derivative coefficients including odd degrees, and harmonic moment identities. These finite checks validate the implementation algebra; the infinite source error and complete high inverse conclusions also depend on the analytic arguments and inherited coercivity above. No Lean proof was run.

## Scope and next frontier

This certifies ONLY S_Q(e0,e0), with all other retained low coordinates fixed to zero. It does not say S_Q is positive on the entire56-dimensional retained even space. Cross-couplings with other low coordinates could still matter. It does not certify the odd sector, DNE9's reflected contact matrix, a genuine near-critical direction, the full residual Gram, whole-aperture positivity, global first-contact exclusion, F4, or RH.

DNE15 should recover an authenticated near-critical retained direction, fix a rational approximation and its finite high correction, and apply the complete source moment enclosure against that direction's actual residual budget. The constant-line budget is about0.008266; near-critical budgets may be much smaller. If the physical-norm gate fails there, preserve the correlations in a form-dual estimator rather than extrapolating this scalar success to the whole matrix.

The attached native signed matrix archives were not recovered or replayed here. The frozen rational trial is independently specified, so this scalar result does not require their coefficient authentication. Its full-high inference does retain the published high-coercivity dependency.
