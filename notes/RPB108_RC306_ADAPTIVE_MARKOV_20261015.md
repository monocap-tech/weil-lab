# RC306 — Polynomial-growth signed-prime error and universal adaptive endpoint-tail bound

**Parent:** RC305 merged at `540e46d0bde48589bbcee25c6f291e02b08b16cd`.  
**Carrier:** original Weil aperture `B=11/10`.  
**Status:** conditional analytic **suboperator** improvements; original Weil positivity, RC292 inverse, Stage I, F4, RH and Lean remain OPEN.

## Core discovery

RC305 made the signed prime-parameter uncertainty bound valid on all finite-degree coefficient vectors, but it did so using a monomial-coefficient absolute-sum majorant. That estimate became enormous around degree 64, despite the original translation intervals being only about 10^-40 wide.

RC306 replaces **monomial coefficient growth** with the physical polynomial's sup norm and its derivative. The improvement is structural; it does not require new prime digits or a larger precision budget.

### 1. Signed-prime interval uncertainty without monomial explosion

For every signed even Legendre polynomial `q(x)=sum_{d even<=D} a_d P_d(x/B)` on `[-B,B]`, put

`||q||_2^2 = sum_d m_d a_d^2,   m_d=2B/(2d+1)`.

The classical Legendre inequality `|P_d(t)|<=1` on `[-1,1]`, combined with Cauchy–Schwarz, gives

`||q||_infty <= sqrt(S_D) ||q||_2`,

`S_D=sum_{d even<=D}1/m_d=(D/2+1)(D+1)/(2B)`.

On the physical interval, the classical Markov inequality gives

`||q'||_infty <= (D^2/B)||q||_infty <= (D^2/B) sqrt(S_D)||q||_2`.

For an uncertainty `delta_l` in each of seven prime translation positions, the L2 discrepancy between compactly supported translated sources is controlled by two disjoint regions:

- the symmetric difference of their support intervals, of length at most `2 delta_l`; this costs `2 delta_l ||q||_infty^2` in squared L2;
- their common overlap, of length at most `2B`; the mean-value theorem bounds their pointwise difference by `delta_l ||q'||_infty`, costing `2B delta_l^2 ||q'||_infty^2`.

Hence, retaining RC237's paired signs, for each prime coefficient enclosure `c<=c_high` and coefficient error `delta_c`,

`C_prime(D)=2 sum_{seven prime powers} [delta_c + c_high sqrt(2 delta_l S_D + 2B delta_l^2 (D^4/B^2) S_D)]`

gives `||prime_error(q)||_2 <= C_prime(D)||q||_2`, and after inverse D weighting,

`||D^-1 prime_error(q)||_D <= C_prime(D)/sqrt(s_lower) ||q||_2`.

**This covers arbitrary signed coefficient vectors** in any fixed finite even-degree cap D. The constants grow at most polynomially, not exponentially, with D; they are not uniformly bounded as D tends to infinity.

The proof invokes the standard Legendre bound and the classical Markov theorem. Actions validates their exact algebraic consequences, native parameter interval enclosures, and representative Legendre endpoint identities. It does **not** independently formalize Markov or the original Weil/prime translations.

### 2. A dimension-independent endpoint-tail bound, with adaptive cutoff

RC305's endpoint tail estimate is valid when the first omitted even output N strictly exceeds D. Keeping N=2050 forces its spectral gap to zero as D approaches 2050.

Instead choose

`N(D)=max(2050, 2D+2)`, for even D.

Now for *every* even nonnegative D,

`1-D(D+1)/(N(N+1)) > 3/4`.

The exact input sup-norm dual constant is again `S_D`, while the even-parity telescoping weight is

`W_N = (N^-2 + (N^-2-(N+1)^-2))/2 < N^-2`.

Since `2B S_D/N^2 <=1/4` and `H_N>=H_2050`, the RC252 absolute Cauchy endpoint argument yields the **dimension-free adaptive endpoint suboperator tail bound**

`||D^-1 endpoint_omitted_{n>=N(D)}(q)||_D^2
  <= [4/(9(H_2050+s_lower))] ||q||_2^2`.

The assertion is valid for arbitrary finite even D **only with the moving cutoff**. It does not mean that a fixed 2048-output truncation controls every-degree input. The finer certificate also evaluates the sharper rational D-specific estimate at D=10,20,32,64,128,256,512,1024,1536,2048,4096,8192.

### 3. Regressions and the mixed signed source

The exact validator verifies:

- all seven pinned native prime-translation and coefficient intervals;
- the new signed-prime bound is strictly smaller than RC305's monomial bound at D=10,20,32,64;
- the adaptive endpoint energy matches the prior fixed-cutoff expression whenever N remains 2050;
- the adaptive bound is strictly smaller once N must grow beyond 2050;
- the exact polynomial identities behind the global N(D) spectral gap and sup-norm ratio;
- the physical squared L2 norm of the independent RC303 signed input `P4-P6/2+P8/3-P10/5`;
- independent Legendre identities `P_d(1)=1` and `P'_d(1)=d(d+1)/2` for selected degrees.

Importantly, RC303's *previous upper bound* on the mixed source's prime arithmetic error may exceed the sharper new analytic bound. That is **not a contradiction**: the two are different upper bounds on the same underlying uncertainty. We do not compare them as though the prior upper estimate were the true realized error.

### 4. Still missing before RC292 can run

This checkpoint solves two specific pieces of the error problem:

1. Prime **parameter uncertainty** on any fixed polynomial degree cap.
2. Endpoint **omitted-output tail**, with an output cutoff increasing with the input degree.

It does not bound every degree's **nominal prime output** or its projection tail, regular archimedean source, pole term, finite-output interval uncertainty, or the action on the full infinite-output vector. No full signed inverse, remaining Schur positivity, Stage I or RH is inferred.

A numerical issue also remains: even polynomially growing C_prime(D) eventually becomes too large for a dimension-free operator norm as D grows without bound. A weighted/smoothing argument or more natural source space may be necessary.

## RC307

Integrate the improved suboperator constants with a degree-adaptive **direct prime projection**, regular archimedean and pole bounds. Before implementing Chebyshev powers, specify an invariant/common Banach or Hilbert-domain completion and show stability under the full original action.

## Reproduce

```bash
python scripts/validate_rpb108_rc306_adaptive_markov.py --output certificates/rpb108_rc306_adaptive_markov.json
python scripts/validate_rpb108_rc306_adaptive_markov.py --output certificates/rpb108_rc306_adaptive_markov.json --replay
```

The exact replay verifies the supplied computational implications; it is not independent peer review of the imported functional inequalities or the original Weil identity.
