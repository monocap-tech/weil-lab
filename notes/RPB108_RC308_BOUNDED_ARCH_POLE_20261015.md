# RC308 — common bounded physical carrier for regular archimedean, pole and nominal prime sources

**Parent:** RC307 merged commit `35c1fb0311f44f23a7eee6830ff60411274b9ec8`.  
**Aperture:** `B=11/10`.  
**Status:** original Weil positivity, complete endpoint action, RC292 signed inverse, Stage I, F4, RH and Lean **OPEN**.

## Research objective

RC307 certified the nominal seven-prime source as a bounded linear operator on physical `L²([-B,B])`, extending to the complete space by density. RC308 audits whether two other parts of the *original* Weil source belong to that same carrier: the regular archimedean convolution and the pole contribution. It distinguishes the bounded **source suboperators** from the still-unproved complete original operator.

## 1. Regular archimedean term

RC46 carries a rational degree-192 Taylor polynomial `r_192(t)` and a uniform exact analytic approximation `|r(t)-r_192(t)|<=epsilon` on `0<=t<=2B`.

The inherited RC237 source polynomial is the sum of left and reflected right physical convolutions. For an even input `q`, it is precisely the physical integral kernel

`(Rq)(x)=int_{-B}^B r(|x-y|) q(y) dy`.

The same symmetric convolution formula acts on odd functions, with the reflected right contribution acquiring a minus sign as enforced by parity. The integral kernel is symmetric and bounded over the compact physical aperture.

The exact rational absolute coefficient bound gives

`sup_{0<=t<=2B}|r(t)| <= sum_{k=0}^{192}|a_k|(2B)^k + epsilon`.

Every monomial term is rounded outwards before summation, avoiding giant-denominator cancellation or floating-point overflow. The Schur integral test then gives the **entire physical L2 operator bound**

`||R||_{L²->L²} <= 2B sup|r|`.

The kernel approximation error is bounded independently of input degree:

`||R-R_192||_{L²->L²} <= 2B epsilon`.

RC308 reconstructs the complete mixed source `q=P4-P6/2+P8/3-P10/5` directly from its single rational polynomial and checks exact coefficient equality with the signed sum of four inherited source profiles. It also derives a second independent physical convolution integral for the first seven Taylor coefficients and checks the resulting low-kernel polynomial exactly.

## 2. The original pole term is rank two

On normalized `x in [-1,1]` with physical measure `B dx`, split the pole analytic source into

`phi_even(x)=cosh(Bx/2)`,
`phi_odd(x)=sinh(Bx/2)`.

The original source formula has opposite signs on the orthogonal even and odd sectors:

`P_pole(q)=2<q,phi_even>phi_even - 2<q,phi_odd>phi_odd`.

This has rank at most two and is bounded on the entire physical L2 carrier. Its exact operator norm is

`||P_pole|| = 2 ||phi_even||² = 2(B+sinh(B))`,

because `||phi_odd||²=sinh(B)-B` is strictly smaller.

A rigorously enclosed rational Taylor series for `sinh(B)` gives a narrow exact interval around this norm. The RC303/RC237 pole source instead uses the degree-40 Taylor truncations of cosh and sinh. If `delta` bounds both omitted exponential tails uniformly, then the rank-one outer-product perturbation inequality gives

`||P_pole-P_pole,40|| <= 8B exp(B/2)_upper delta`.

This is independent of source polynomial degree, and includes both parity sectors. The mixed `q` pole moment is also rebuilt directly and regressed against the independently computed component Legendre moments.

## 3. A common physical source operator

With the signed nominal prime operator of RC307, define the **three-component source**

`S_3 = P_nominal - R + P_pole`

(the sign of R depends on the original Weil source convention; its norm bound is sign-invariant). Each term extends boundedly to `L²([-B,B])`, hence so does `S_3`:

`||S_3||_{L²->L²}
<= C_prime_nominal + C_regular + C_pole`.

On the physical D-energy Hilbert completion, where `D` is diagonal with eigenweights `H_n+s` and `s>=s_lower>0`, we consequently have

`||D^-1 S_3||_{D->D}
<= (C_prime_nominal + C_regular + C_pole)/s_lower`.

This establishes **composability of the three-component operator** on its own common completed carrier, not of the entire original Weil action.

The regular-kernel polynomial and truncated pole approximations also have a direct, degree-independent L2 model-error bound.

## 4. Remaining endpoint/diagonal obstruction

The original Legendre endpoint/singular part contains a nontrivial coupling between arbitrarily high Legendre degrees. RC306 controls its degree-adaptive omitted tail for finite polynomial inputs, but this is not equivalent to a fixed bounded operator on the same completed Hilbert carrier. Neither the endpoint term nor all original diagonal terms are included in `S_3` here.

Therefore RC308 **does not** prove that the full Weil action maps the D-energy completion to itself, and no repeated Chebyshev inverse powers of that full operator are justified.

## RC309

Investigate the singular endpoint/diagonal Legendre matrix using its near-diagonal discrete Hilbert-transform structure and the log-harmonic D weights. Establish a boundedness/closed-domain theorem on the common D carrier or exhibit a precise obstruction. Only then assemble the full original action and attempt repeated RC292 inverse-response operations.

## Reproduce

```bash
python scripts/validate_rpb108_rc308_bounded_arch_pole.py --output certificates/rpb108_rc308_bounded_arch_pole.json
python scripts/validate_rpb108_rc308_bounded_arch_pole.py --output certificates/rpb108_rc308_bounded_arch_pole.json --replay
```

The source identifications and standard L2 Schur/rank-one operator inequalities remain imported mathematical facts; exact replay is computational custody, not independent mathematical peer review or proof of RH.
