# RPB108: the actual prime bulk is sublogarithmic on the closed weak-critical class

Date: 2026-10-07 UTC. Recovered live head a293e9c3fa7745af5001b6ff7e8511b49c45de4b and the canonical cursor.
Definitions: [sublogarithmic prime bulk](../docs/TERMINOLOGY_RPB108_SUBLOG_PRIME_BULK.md).
Category: actual sharp-head arithmetic / precise contour-oscillation obstruction. Analytic, not Lean-certified.

## Result

For any finite canonical supported family F with the already closed weak translation bound D_w(t;h)=O(|t|),

    Omega_F(T)=O(1/T),
    integral_(t0)^T t q_F(t)dt=O(1+log log T),
    B_prime,F(T)=O(1+log log T),
    B_F(T)=C_gamma,F(T)+O(1+log log T).

This holds for ALL large T, not just an averaged bound. On the previously constructed actual good-height sequence,

    S_F(T_n)=C_gamma,F(T_n)+O(1+log log T_n).

For a hypothetical nonzero actual contact kernel, its established sharp/log limit therefore forces C_gamma,K(T_n)/log T_n -> (2/pi)Lambda_K>0. The actual rough positive eigenmode has the same conclusion. Thus direct oscillation of the prime term in THIS contour representation cannot supply a bounded/sublogarithmic sharp return by cancelling the positive leading term: its entire contribution is already o(log T).

This is a candidate-specific obstruction with an actual quantitative bound, not a claim that primes are irrelevant to existence of K. Their exact physical null equation determines which h are possible. A zero-specific compatibility/range theorem could still exclude those h. The smallest global arithmetic theorem remains nonpositive sharp/log liminf, and the global dependency graph does not shorten.

## 1. Consume the established actual weak translation estimate

The actual sharp/log note already proved D_w(t;h)=O(t) from the exact full-null equation and its translated correlation. Its eigenmode extension obtains the same bound after keeping the mu mass residual. We use those results unchanged, without reopening endpoint regularity or Abel transfer.

For lambda in [-1,1], let g_lambda(x)=exp(lambda x)h(x) on the fixed support. Choose a smooth compact cutoff equal to one on a fixed enlargement containing all sufficiently small translates. Multiplication by cutoff times exp(lambda x), and by its first derivative, is uniformly bounded on the canonical logarithmic Fourier space. The Schwartz-convolution proof in the preceding contour note gives this directly.

Decompose the translated difference into a multiplier times (tau_t h-h) and a multiplier difference times tau_t h. The second multiplier has logarithmic operator norm O(|t|), uniformly in lambda. Squaring the triangle bound gives

    ||tau_t g_lambda-g_lambda||_D^2
       <= C||tau_t h-h||_D^2+C t^2||h||_D^2=O(|t|).

Thus the same weak translation bound holds uniformly for both exponential modulations lambda=+1,-1. These changed physical vectors are used only for Fourier estimates; they are never asserted null. The original h and its actual coefficients in S_F remain unchanged. This step is important: form membership alone only gives a finite log-weighted strip integral; it does not give the weak-critical tail used below.

## 2. Physical weak tail and a log-log first-height estimate

In the H-transform frequency normalization, average the nonnegative log-weighted cosine defect over 0<t<1/T. Tonelli gives the factor

    1-sin(u/T)/(u/T).

On |u|>T this is at least 1/24, as already proved in the actual tail note. The O(t) defect average is O(1/T), so each modulated physical Fourier tail satisfies

    integral_(|u|>T) log(e+|u|)|F_(g_lambda)(u)|^2du<=C/T.

Fourier normalization rescales constants only. Summing lambda=+1,-1, both signs and the finite family gives Omega_F(T)<=C_F/T. This is a continuous physical Fourier estimate, not a claim that the discrete prime or zero packets are freely realizable.

Let dmu(t)=log(e+t)q_F(t)dt and f(t)=t/log(e+t). On t>=t0>2, f is positive, increasing and f'(t)<=1/log(e+t). Positive layer cake, retaining the initial interval as a fixed constant, gives

    integral_(t0)^T t q_F(t)dt
       <= f(t0)Omega_F(t0)+integral_(t0)^T f'(u)Omega_F(u)du
       <= C_0+C_F integral_(t0)^T du/[u log(e+u)]
       =O(1+log log T).

All measures here are nonnegative. No cancellation or signed Tauberian inference is needed. Cauchy-Schwarz pointwise gives

    |W_F(c+it)|+|W_F(c-it)|<=q_F(t)/2.

Therefore the absolute integral of t times both W weights is also O(1+log log T). Their log-weighted base integral is finite by canonical energy.

## 3. Bound the COMPLETE actual prime term before taking limits

On c=3/2,

    Z(c+it)=-sum_(n>=2) Lambda(n)n^(-c-it),
    |Z(c+it)|<=sum_(n>=2) (log n)n^(-3/2)<infinity,

and the same holds at -it. This includes all prime powers, not a finite prime deletion. The classical Euler log-derivative series is recorded in the author-hosted [Kedlaya chapter 9, equation (9.1.1)](https://kskedlaya.org/ant/chap-von-mangoldt.html); its absolute convergence here follows by comparison with the displayed convergent elementary series.

The registered r(c+/-it) has magnitude <=t+1. Consequently

    |B_prime,F(T)|
       <=C integral_(t0)^T (t+1)(|W_F(c+it)|+|W_F(c-it)|)dt
       =O(1+log log T).

For every finite T the prime series can be integrated term by term. The absolute budget above is uniform in finite prime truncations and includes the whole infinite series. No exchange of divergent first-height moments or hypothetical signed cancellation occurs.

This estimate rules out even a logarithmically large negative prime contribution on an unbounded sequence. Prime oscillation remains possible at smaller scales, but cannot cancel a positive c log T term for fixed c>0.

## 4. Isolate the gamma coefficient with the correct two-sided signs

The exact completed log derivative is

    A(s)=Z(s)+1/s+1/(s-1)-(log pi)/2+psi(s/2)/2.

The standard digamma asymptotic in [NIST DLMF 5.11.2](https://dlmf.nist.gov/5.11) implies, at fixed c=3/2 and t->infinity,

    A(c+/-it)=(1/2)log t+O(1).

The O(1) includes the absolutely bounded actual prime term and the gamma imaginary constants. The two rays stay in a closed sector away from the negative real axis, as required by the asymptotic. The rational terms are O(1/t); no zero-free or RH assumption beyond c>1 is needed here.

Write r(c+it)=t-i and r(c-it)=-t-i in the EXACT two-sided B_F definition. The leading real log term contributes

    (1/(2pi)) integral_(t0)^T t log t Re[W_F(c+it)+W_F(c-it)]dt

plus a correction bounded by the finite integral of log t times both |W|. The O(1) remainder multiplied by r contributes O(1+log log T) by section 2. Hence the result B_F=C_gamma,F+O(1+log log T), with the stated coefficient and signs. C_gamma is a cross-modulated quadratic integral, not a pointwise nonnegative Fourier density.

Combining with the previously proved good-height contour relation adds only a convergent constant. Thus the complete actual prime contribution and all lower-order completed factors are sublogarithmic, and the sharp/log coefficient on that sequence comes wholly from the leading gamma term. This does not newly identify or recompute kappa_R; its existing coefficient is consumed as an input.

## 5. Lawful null testing and the precise failed mechanism

Neither the vertical holomorphic weight nor its leading gamma integral is automatically a supported physical null test. Full mixed-nullity annihilates Q(h,u) for u in the same supported canonical carrier. It does not annihilate each separately split prime/gamma integral or a height-multiplied analytic sample packet. The existing complete source-graph obstruction remains the domain safeguard; no enlarged null equation or historical selected witness is used.

The failed implication is now quantitative:

    actual prime oscillation in B_prime,K
       -> cancellation of the positive sharp/log coefficient.

The left contribution has absolute size O(log log T); the coefficient needing cancellation is c log T, c=(2/pi)Lambda_K>0. Their normalized limits are incompatible. A successful arithmetic theorem must instead use the actual UNshifted null/source compatibility to exclude the fixed physical profile or force its leading gamma coefficient to vanish. That is not supplied by the decomposition and is not silently inferred from Q(h)=0.

This conclusion is representation-specific. It does not preclude a different oscillation theorem for the complete sharp zero head, a nonlocal source-range theorem, or an identity that rules out the profile before evaluating the contour. It does exclude treating bounded Euler-series oscillation on this right line as the missing leading cancellation.

## 6. Four controls and validations

| Control | Audit |
|---|---|
| Actual rough positive eigenmode | Its pinned D_w=O(t) proof retains mu h. Every estimate above therefore applies to the SAME actual source range; its positive sharp/log slope persists entirely in the leading gamma term. This is the decisive actual distinction test. |
| Artificial compact-good-row logarithmic control | No actual xi/Euler-series contour identity is attached to its artificial rows. It remains a compactness/density countercontrol, not a counterexample to this actual prime estimate. |
| Fixed finite actual restoration | Changes sharp/log normalization by o(1). Its bounded correction cannot erase the leading term, and the prime estimate already includes ALL actual prime powers. |
| Two-row comparison contact | Auxiliary negative rows remain outside the actual xi divisor. Comparison zero-nullity is not substituted for actual unshifted nullity; no source-range exclusion follows from its geometry. |

The JSON records four internal source blob pins and primary external locations. Exact rational controls check weak-tail-to-first-moment budgets with dyadic atoms and rational logarithm enclosures, absolute complete-prime envelopes, and the two-sided gamma algebra. They verify the quantitative obstruction; the continuous modulation, Tonelli and asymptotic arguments above remain analytic. No Lean compilation or axiom closure is claimed.

No actual bounded-return mechanism was found. The global graph is unchanged and the implication actual source-range full unshifted nullity -> bounded/sublogarithmic sharp subsequence remains unproved. Certified 99/100 positivity, historical certificates and cursor wording are preserved. No aperture marching, attachment restart, new endpoint criterion, global exclusion or F4 claim occurs.
