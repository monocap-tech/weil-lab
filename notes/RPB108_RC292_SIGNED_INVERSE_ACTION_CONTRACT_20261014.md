# RC292 — dual signed-response acceptance thresholds and exact inverse-action budget

**Parent:** canonical RC291 `c14663806869d60a988ecef2214b38bd161dfc7a`.
**Original form:** unchanged.
**Positive reference:** rank 317, even 122 sources.
**Status:** an executable **conditional certificate contract**; the
new native operator iterations and signed source responses are NOT performed.

## Goal

The certified even joint auxiliary pivot from RC288 is positive on
`P0,P4`. RC290 gives its exact lower-matrix congruence

    Gamma_lo' = diag(a,delta),  a>0, delta>0,

in the source basis `P0, P4-tP0`. Write `v_h=P0`,
`v_s=P4-tP0`, and let `R` be the other **120 even**
rank-317 source directions. In the unchanged physical metric, the
*actual* signed reduced-reference solutions are

    Y_h=G_new^-1 v_h,  Y_s=G_new^-1 v_s.

The mathematically valid whole-range Schur cross estimate is

    C*Gamma_actual^-1 C
      <= lambda² [
          ||P_R Y_h||_physical²/a
         +||P_R Y_s||_physical²/delta] Mass_R.

A **sufficient** (not necessary) acceptance condition is

    ||P_R Y_h||_physical² < a/(2 lambda²),
    ||P_R Y_s||_physical² < delta/(2 lambda²).

It would make the complete even joint block-to-rest cross payment
strictly smaller than one physical Mass. This ALONE does not prove the
remaining principal Schur form positive. RC286's different, already
certified single-P0 bound is not conflated with the joint partition.

## Exact residual-to-signed-projection interface

In the actual D Hilbert norm define

    N=D^-1 G_new,    b=D^-1 v,   Y=N^-1 b.

Inherited RC278 and RC283 estimates give the spectral enclosure

    0 < mu I <= N <= nu I.

For any **actually evaluated** approximate source response `Yhat`,
its **actually paid** full D-residual is

    r=b-N Yhat.

By positivity and the retained-rest D floor `d_R=H_2+s_lower>0`,

    ||Y-Yhat||_D <= ||r||_D/mu,
    ||P_R(Y-Yhat)||_physical
       <= ||r||_D/(mu sqrt(d_R)).

For either source with pivot lower `gamma_i=a` or `delta`, set

    T_i=gamma_i/(2lambda²).

The following two strict, testable conditions suffice:

    ||P_R Yhat||_physical² < T_i/4,
    ||r||_D² < mu² d_R T_i/4.

The triangle inequality then gives
`||P_R Y||_physical²<T_i`.

All inequalities are on the **same** physical/original source,
reduced reference and D norm. No change of input source or transfer
of old-reference inverse covariance is permitted.

## An exact Chebyshev action budget (not a performed solve)

For each of `v_h=P0` and `v_s=P4-tP0`, the source right-hand-side
D squared norm has an exact rational upper bound

    ||b||_D² <= sum_{n in supp(v)} m_n v_n²/(H_n+s_lower),
    m_n=2B/(2n+1).

Using the exact rational `mu,nu` bounds from RC283 and RC278,
choose the least integer `t0` such that `t0² mu>=nu`. Set

    q0=(t0-1)/(t0+1) < 1.

For the canonical inverse-Chebyshev polynomial `p_(k-1)`,
the **ideal exact arithmetic** residual has the certified bound

    || b-N p_(k-1)(N)b ||_D² <=4 q0^(2k) ||b||_D².

RC292 derives the smallest sufficient degree `k-1` (relative to
this rational `q0` estimate) that charges at most **one quarter**
of the requested total residual-square threshold.

Another quarter of that threshold is reserved for the combined
real original-operator action, prime, pole, archimedean, endpoint,
rounding and infinite-tail errors. If their **actual residual-space
D squared norm** is certified below the reserved quarter, the sum
of ideal and execution residuals satisfies the strict total
threshold by the triangle inequality.

These bounds are only a priori resources. The Chebyshev action must
actually be evaluated against the **native infinite-dimensional
`G_new`** with rigorously paid input/source, prime and endpoint
faults; doing a nominal finite matrix multiply is not enough.

Even with a flawless residual check, the decisive condition is the
**signed projected approximate response**:
`||P_R Yhat||_physical²<T_i/4`.
No such response has been evaluated yet, and the current global
covariance bound from RC291 cannot supply it.

## Deliverables and next source action

The exact rational JSON records the hard and soft native pivot
floors, mass budgets, full D-residual tolerances, separate
ideal Chebyshev and native action error tolerances, and sufficient
recurrence lengths, with RC129/RC278/RC283/RC290/RC291 source pins.

**RC293:** implement a genuine native operator-action engine for
both sources at this exact reference and aperture, evaluate the
Chebyshev recurrence with full original arithmetic error payments,
and certify the signed 120-coordinate projections. Reject any
claim of a positive full auxiliary gate without separately
establishing the remainder principal form.

No new action, Stage I, F4, RH or Lean result is asserted here.

## Replay

```bash
python scripts/validate_rpb108_rc292_signed_inverse_action_contract.py --output certificates/rpb108_rc292_signed_inverse_action_contract.json
python scripts/validate_rpb108_rc292_signed_inverse_action_contract.py --output certificates/rpb108_rc292_signed_inverse_action_contract.json --replay
```

Reproduction verifies rational identities against pinned inherited
certificates. It does not independently establish their analytic
premises or execute the proposed inverse solve.
