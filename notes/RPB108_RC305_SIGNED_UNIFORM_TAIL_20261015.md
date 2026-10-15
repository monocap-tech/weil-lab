# RC305 — sign-robust endpoint tail and prime-uncertainty operator bounds by input degree

**Parent:** RC304 merge `93f2a120d09181735c5720b2a86f340d8c27d917`.  
**Scope:** even finite input polynomials in the original Weil aperture `B=11/10`; source intervals and classical endpoint coefficients imported from earlier certified models.  
**Standing:** Stage I, true inverse, global F4, RH and Lean **OPEN**.

## Why this pass matters

RC304 extends the native source action to P10 and the full fixed input
span `V6`. A Chebyshev inverse recurrence, however, generates signed
polynomial combinations with increasing degrees and eventually
infinite outputs. Two inherited analytic estimates must therefore be
reexamined, rather than indefinitely adding precomputed columns.

1. RC252's sophisticated endpoint-tail routine constructs a
   **positive signed-moment bracket**. General signed input polynomials
   need not satisfy that positivity: e.g., `P0-P2` has zeroth
   signed moment 0. We must not apply that routine's positive-bracket
   gate to arbitrary recurrence inputs.
2. RC237's original signed-prime translation-parameter uncertainty
   depends on the actual polynomial's monomial absolute sum and
   derivative majorant. RC305 derives explicit uniform constants
   for these quantities over every even polynomial up to a chosen
   input-degree cap.

## The signed-uniform endpoint tail theorem

Let the even Legendre polynomial input be

`q = sum_{d even,0<=d<=D} a_d P_d`

with physical `||q||_2^2 = sum_d m_d a_d^2` and
`m_d=2B/(2d+1)`.

For any even output `n>=N>D`, the original endpoint formula
requires only `n>d` and reads

`h_n=(2n+1) sum_d a_d/[n(n+1)-d(d+1)]`.

Set `x_n=n(n+1)`, `t_D=D(D+1)`. Without assuming **any**
particular sign or nonvanishing source moment,

`|x_n h_n/(2n+1)| <= [sum_d |a_d|]/[1-t_D/x_N]`.

By weighted Cauchy,

`(sum_d |a_d|)^2 <= S_D ||q||_2^2`,
where the exact finite-degree dual constant is

`S_D = sum_{d even<=D} 1/m_d
      = (D/2+1)(D+1)/(2B)`.

For `N=2050` and the same physical D weighting as RC304, the
positive parity-weight telescope gives

`W_N = (N^-2 + [N^-2-(N+1)^-2])/2`.

The full endpoint high-output D tail satisfies

`sum_{n>=N even} m_n h_n^2/(H_n+s)
  <= C_end(D,N)^2 ||q||_2^2`

uniformly for *every signed coefficient choice*, where

`C_end(D,N)^2 =
  2B S_D W_N /
    [(H_N+s_lower)(1-D(D+1)/(N(N+1)))^2]`.

The validator records exact rational formulas and outward-rounded
square roots for D=10,20,32,64,128,256,512,1024,1536,2048.
It tests direct original endpoint coefficients at output 2050 and
2052 on three explicitly signed sources, including two with
vanishing zeroth moment.

**This is a bound on the endpoint tail suboperator only.**
At D>=N the geometric denominator becomes zero/nonpositive and this
proof does not apply. For growing degree, the output cutoff must grow.

## The uniform finite-degree prime-parameter uncertainty theorem

Let `q(x)=sum_k b_k x^k` with the same even Legendre input and
`A(q)=sum_k |b_k|`,
`T(q)=sum_k k|b_k|/B`.

Define the exact basis constants for each even degree d:

`A_d = sum_k |coefficient_k(P_d)|`;
`T_d = sum_k k|coefficient_k(P_d)|/B`.

The sum and weighted Cauchy inequalities yield

`A(q)^2 <= A_D^2 ||q||_2^2`,
`T(q)^2 <= T_D^2 ||q||_2^2`,

where

`A_D^2=sum_{d even<=D} A_d^2/m_d`,
`T_D^2=sum_{d even<=D} T_d^2/m_d`.

For each of the seven active prime powers, let
`delta_l=(l_upper-l_lower)/2`,
`delta_c=(c_upper-c_lower)/2`,
and `c_upper` be the pinned interval data.

The *existing* original signed-prime interval-parameter formula
now gives the **uniform** physical L2 error bound

`||prime_error(q)||_2 <= C_prime(D)||q||_2`,

`C_prime(D)=
  2 sum_{7 primes}[delta_c+
     c_upper sqrt(2 delta_l A_D^2 +
                  2B delta_l^2 T_D^2)]`.

The certificate uses exact rational monomial sums and outward
square-root intervals, with validated degree caps D=10,20,32,64.
The corresponding D-inverse-norm prime error obeys

`||D^-1 prime_error(q)||_D
   <= C_prime(D)/sqrt(s_lower) ||q||_2`.

The RC303 **independently translated signed mixed polynomial**
`P4-P6/2+P8/3-P10/5` is checked against the new uniform
degree-10 prime bound. No coefficient positivity is assumed.

## Two precise limits identified

* The fixed low original output cutoff 64 and legacy `65>3d+1`
  guard admit only even input degrees through d=20. At d=22 the
  old original cutoff-dependent analytic estimate is no longer
  justified without enlarging its projection cutoff.
* The fixed high endpoint-tail cutoff N=2050 requires D<2050;
  it does not cover a degree-2050 source or arbitrary recurrence
  output. The source-dependent prime majorant constants also
  deteriorate with D, so these are not dimension-free operator
  norm estimates.

Thus this is a genuine **all-signed-input** analytic suboperator
extension, but not a complete high-degree original Weil action.
The regular archimedean, pole, analytic source intervals,
arbitrary-degree prime-projection tails, and repeated-operator
composition remain distinct obligations.

## Next — RC306

Combine this signed-uniform endpoint/prime suboperator interface
with **degree-adaptive source and output cutoffs**; audit all
other analytic error terms before asserting a uniform full
action. Repeated Chebyshev recurrence remains prohibited until
every input generated by a step belongs to the certified domain.

## Reproduction

```bash
python scripts/validate_rpb108_rc305_signed_uniform_tail.py --output certificates/rpb108_rc305_signed_uniform_tail.json
python scripts/validate_rpb108_rc305_signed_uniform_tail.py --output certificates/rpb108_rc305_signed_uniform_tail.json --replay
```

Exact arithmetic custody and replay cannot substitute for
independent review of the imported original Weil endpoint
and prime-source identities.
