# NF584 — exact logarithmic Fourier split

Stacked on NF583 #614; new Lean scripts compiler-pending.

## New accepted compiler results

NF583-head rechecks: NF582 run 44036588847 job 133880827826 and NF579 run 44036589078 job 133880829535 have both passed the exact affine and complex twisted convolution transform build step. The normalized mollifier module and scalar fixed-frequency limits also passed on the former. This verifies the actual full-complex compression and convolution identities, with their stated integrability hypotheses. The NF582 independent scale sequence remained failed on the previous head; the completed NF582-head job 133871858557 diagnosed its final Tendsto definitional unfolding mismatch. NF584 explicitly changes the statement to the literal lambda before simplification. Other NF583-head recovery jobs were still active; no new terminal Gram or endpoint graph acceptance claimed.

## Exact analytic split (new proof candidates)

Retain B=11/10, delta=1/500, x=B-d and z=t+iy. The actual half transform is

H_U(z)=exp(i t B) * integral_0^delta A_y(d) log(B/d) exp(-i t d) dd,
A_y(d)=U(B-d) exp(-y(B-d))/2.

Let L(d)=log B-log d; this equals log(B/d) for d>0 and is nonnegative for d<=B. NF584 formalizes candidates for its exact interval integrability and primitive
integral_0^a L(d) dd=a(L(a)+1).
For |A|<=C0 the near panel norm is at most C0 a(L(a)+1). A separate generic proper-interval complex integration by parts lemma pays the endpoint traces and integral of the derivative without crossing d=0.

On [a,delta], (A L)'=A' L-A/d. The derivative norm is bounded by C1 L+C0/d. Integrate the latter with the exact log ratio, and bound the former by the full nonnegative log mass. The upper endpoint log and the inverse derivative contribution combine exactly:
L(delta)+log(delta/a)=L(a).
Therefore the high panel has |t| times norm bounded by 2 C0 L(a)+C1 delta(L(delta)+1).
At a=1/|t|, whenever |t|>=500, adding the near panel gives
|t| * |integral_0^delta A L exp(-itd)| <= C0(3 L(a)+1)+C1 delta(L(delta)+1).
This is precisely the historical NF576 high-band expression, with no endpoint regularization. The same near-panel theorem with a=delta gives the low-band bound.

The formal split keeps whole interval integrability and proper derivative interval integrability explicit. The original raw-transform change of variables, source-specific A_y and derivative integrability, and scalar high/low specialization must still be connected. No formal source U attachment claimed. The mathematically weaker assertion of some finite C for convergence needs only C1 regularity and compact collar bounds, not the exact numerical U400 envelope; the quantitative historical estimates must still be preserved for signed-form/source obligations.

## Disposition

New focused CI and three proof-candidate components committed. No local Lean build, no fresh numeric replay, no main merge. Previous verified conditional continuum/discrete graph limit, global independence, raw/window dictionary, normalized mollifier and scalar limit receipts retained. Full unconditional canonical Gram, literal endpoint graph and authenticated U binding are not yet verified; full Weil coercivity, W_ODD_NEG and RH remain open.
