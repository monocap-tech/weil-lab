# Weil-Lab NF382 — exact optimal robust joint signed-information gate

**2026-10-28 Pacific.** Canonical obligation `W-ODD-NEG` OPEN. Stacked on NF381 PR #366. **Actual original n513 signed measurement STILL PENDING:** [Actions 40820718599](https://github.com/monocap-tech/weil-lab/actions/runs/40820718599) and exact-gap [40820718721](https://github.com/monocap-tech/weil-lab/actions/runs/40820718721) remained QUEUED at recovery; no artifacts or successful native verdict were obtained. This is an **exact analytic improvement** to the *acceptance test*, NOT a numerical n513 result, odd negativity/positivity, full inverse, or RH.

## New physical information gate, actual original n512 pinned

For the original two supported sine harmonics `v512,v513` on `[-11/10,11/10]`, `<v512,v513>=0` and `||v512||²=||v513||²=B=11/10`. Fix the same orthogonal projector `P=P_(J242+F4)` as NF380/381 and let `q_i=(I-P)v_i`, `g_i=||q_i||²`, `c=<q512,q513>`. Then

`c=-<Pv512,Pv513>`, and `|c|² <= (B-g512)(B-g513)`.

Consequently, **`g512+g513>B` is a sufficient condition for the actual 2x2 exterior Gram to be strictly positive definite**, since
`g512*g513 - (B-g512)*(B-g513) = B*(g512+g513-B)>0`.
It is sufficient, not necessary. The already certified original n512 native physical enclosure `g512≈1.085542249619544`, frozen SHA256 `9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b`, implies **`g513>0.01446` is conservative sufficient physical information**. This is stronger than the bare NF381 fractional independence requirement in cases where the n513 native mass is near its fail-fast cutoff, but it is NOT an observed n513 mass. The new helper performs SHA-pinned native n512 preflight and checks the rational bracket `0.01445 < B-g512_lower <0.01446`.

## Exact optimal robust signed-information bound

Once actual original n513 native `b513=Wodd(u4,q513)` and `g513` with SHA/overlap checks are obtained, set `a_i=lower(|b_i|)>=0`, `G_i=upper(g_i)>0`, `C>=|c|`, all exact rationals. Require `C²<G1*G2` to use the robust SPD upper envelope. Choose the signs of the known strictly signed intervals so the actual signed pairings add. For any weights `x,y>=0`,

`||Q_J m(D)u4||² >= (a1*x+a2*y)²/(G1*x²+2*C*x*y+G2*y²)`.

This is a valid **lower** on the original strong residual under the inherited analytic realization/domain hypothesis. The best lower from this entire *sign-aligned robust ray family* is computed exactly, with **no arbitrary finite trial grid**. Define
`X=G2*a1-C*a2`, `Y=G1*a2-C*a1`.

- When `X>0,Y>0`, the maximizing ray is `(x,y)=(X,Y)`, and its squared lower is
  `Lopt=(G2*a1²-2*C*a1*a2+G1*a2²)/(G1*G2-C²)`.
- Otherwise the maximizing ray lies on the boundary, and `Lopt=max(a1²/G1,a2²/G2)`.

**Proof:** Fix `K=[[G1,C],[C,G2]]\succ0`. The quotient is homogeneous. An interior maximum obeys `K(x,y)^T\propto(a1,a2)^T`, whose coordinates have signs `X,Y`. If the positive cone excludes this stationary vector, its maximum is attained on a boundary axis. Cauchy and the exact interval orientation protect the numerator; Gram upper bounds protect the denominator. This is the optimum of the declared conservative sign-aligned envelope, **not** an exact measurement of the unknown Gram inverse and **not** an upper bound on any full residual.

The runner also preserves NF381's independent eleven-ray lower and reports `max(Lopt,L381)`, so the previously valid certificate cannot degrade. **Only a strict certified lower above `D=2401/(2*10^28)` stops the *fixed NF370 sufficient* small-strong-residual method.** A smaller lower is inconclusive, not positivity. A different finite ray/grid is not a new theorem.

## Reproduction, standing, and stop

`python3 scripts/local_replay/nf382_optimal_robust_joint_dual.py --self-test --preflight-512 notes/data/provisional/NF380_original_archived_unfitted_signed_dual_native.json`

Pure stdlib `Fraction` proof regression: eight abstract algebra fixtures with rational cross checks, plus SHA-locked **actual original n512** physical gate. Neither generates n513. When and ONLY when the new native n513 file exists, run `--original-512 PATH --native-513 PATH --output PATH`; the runner calls the complete NF381 parent original SHA/16-physical/32-signed checks first.

**Previous:** NF381 exact remaining 17/20 gap; native n513 pending. **Current:** NF382 exact robust optimal ray and physical independence criterion. **Next:** verify actual original n513 CI; run SHA-pinned NF381 and NF382 joint screens, compare with D. If insufficient, method-STOP further blind sine-pair enumeration and return to source-adapted lowband/true inverse orientation. Original lowband H4, whole exterior inverse, 238 selected directions, signed operator domain, `W-ODD-NEG`, even, whole Weil and RH remain OPEN. No historical overwrite or main merge.
