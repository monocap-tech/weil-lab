# RPB108 — NF31: all remaining native retained couplings

2026-10-09 UTC. Phase Geometry parent NF30:
`2c64055c00350a7b91ead62453b085cd3408da66`. Coupled CC73 was recovered
read-only at `433c32598895a6c23a4be303496939011c59017b`. No other or
paused branch is modified. Additive definitions:
[NF31 terminology](../docs/TERMINOLOGY_RPB108_REMAINING_BACKGROUND_NF31.md).

## Result

NF31 certifies every signed native coupling of the successful lifted pair
to the remaining54 retained directions per parity:216 paid entries in
total. It also certifies the complete two-by-two finite reaction of those
backgrounds, with inverse uncertainty and physical source errors paid.

Both original finite full-retained lifted families are positive. The
previous four-direction retained Schur certificate with all original high
modes is preserved. The two statements are distinct; they do not together
prove the full retained Schur matrix positive.

| Strict certified native quantity | Even | Odd |
| --- | ---: | ---: |
| Remaining physical native gap | >5.5884e-22 | >3.6221e-19 |
| Remaining reaction / seed energy | (0.0052929,0.0052931) | (0.0079417,0.0079419) |
| Remaining reaction / response energy | (0.8434098,0.8434101) | (0.7687532,0.7687534) |
| Finite response energy after remaining elimination | (5.92040,5.92041)e-38 | (4.97592,4.97593)e-34 |
| Finite full-retained lifted family | positive | positive |

Thus the retained couplings are substantial even after the selected
response probes pass their separate complete-source test. The full
collective high response cannot be treated as a small uncoupled addition.
This is a coupling certificate, not a bound on the still missing remaining
complete source Gram or the true inverse-weighted collective reaction.

## Exact remaining frame and physical inverse

In each parity let T=E intersect span(x,w)-perp. Its dimension is54.
Select the largest absolute nonzero two-by-two constraint minor of the
exact rational seed and response coefficients. The remaining basis
columns are e_j plus the two exactly solved pivot coordinates. Pivot
coordinates are (0,3) even and (1,3) odd in the parity-local retained
coordinate list. Every column is exactly physically orthogonal to both
x and w; these basis columns are not assumed orthonormal.

A_T=T* A_E T uses all authenticated original signed native entries.
Decimal200 LDL arithmetic only selects fixed rational preconditioners.
Outward rational congruence and positive Gershgorin margins prove
A_T positive. The rational row-norm inverse residual is strictly below
one; its Neumann bound pays every inverse entry error.

With K=T A_T^-1 T*, the physical inverse trace gives

\[
Q(u,u)\ge\frac{\|u\|_2^2}{\operatorname{tr}(K)_{\rm upper}},\quad u\in T.
\]

The remaining physical gap is much larger than the old55-dimensional
native background's gap, because the certified response direction has
been separated as well as the seed. No high-condensed gap follows.

## Signed native reaction and physical payments

Let B=Q(T,(v,t)) and Q2=Q((v,t),(v,t)). The even pair is NF30's fixed
expanded family; the odd pair is the unchanged NF29 family. Original
retained coordinates of the compensated source and two-high response
come from native entries. NF26 and NF30 enclose the retained correction
coordinates. Their uniform source errors are multiplied by the small
correction norms and paid as physical balls.

For midpoint coordinate vectors b_i and source-coordinate ball radii
delta_i, define Rhat_ij=b_i* K b_j and e_i=delta_i sqrt(trace(K)_upper).
The full original finite reaction R_T=B* A_T^-1 B pays

\[
|(R_T)_{ij}-\widehat R_{ij}|
\le e_i\sqrt{\widehat R_{jj,\rm upper}}
+e_j\sqrt{\widehat R_{ii,\rm upper}}+e_i e_j.
\]

The paid signed matrix Q2-R_T has positive diagonal and determinant in
each parity. Together with A_T>0, this proves positivity on the finite
family span(v,t)+T. It contains all retained degrees of freedom, with
only the selected two lifted retained directions changed. It is not
the entire original retained-plus-high domain.

Two exact rational remaining native response candidates per parity are
frozen through the exact constraint basis. Independent evaluation of
2Q(candidate,input)-Q(candidate,candidate) agrees with the corresponding
finite reaction enclosure after source-error payment. Their complete
sources have not yet been certified. The certificate retains their exact
coefficients for reviewable later use.

## The remaining collective object

Write R=P_F L(v,t), G=P_F LT, and C for the original high form. Eliminating
F changes both the remaining block and its mixed coupling:

\[
A'=A_T-G^*C^{-1}G,\qquad
B'=B-G^*C^{-1}R,\qquad
M'=Q2-R^*C^{-1}R.
\]

The actual collective obligations are A'>0 and
M'-B'^* A'^-1 B'>0. NF31 certifies A_T and B, not A' or B'. The
remaining complete physical Gram G*G and signed cross G*R are still
missing. A collective floor-based sufficient matrix would instead
enclose the full block with these Gram entries divided by kappa.

The certificate deliberately labels U_old-R_T as arithmetic only,
not a collective lower bound. Its response diagonal is negative in
both parities. That fact is not a valid estimator obstruction or an
actual negative original direction: the expression is not a justified
joint Schur bound in the first place.

## Replay and genuine controls

Fresh outward rational replay reproduces the certificate. Original
inputs are SHA256 authenticated;216 explicit signed coupling enclosures,
the exact frame rule, physical inverse proof, full reaction matrix and
frozen response candidates are retained in the compressed certificate.
The compression is lossless base64 of deterministic gzip; the validator
authenticates both encoded and decompressed bytes.
Fresh replay, all four independently evaluated frozen-response gains,
six genuine crossing controls and three positive-level controls passed.
Both proof scripts passed Python syntax compilation.

Exact three-block controls have remaining/high block [[1,1/2],[1/2,1]],
couplings (-1/4,1/2), and critical diagonal q=7/12+s. Their true joint
Schur value is s, while the invalid separate subtraction gives13/48+s.
For s=-1/100,0,1/100, the latter stays positive through a genuine
negative/null/positive crossing. The separate high and finite tests also
remain positive. The same controls at physical scale1e-18 preserve the
near-critical crossing. Whole-mass shifts1/1000,1/10,2 of the exact null
control have those exact positive physical ground levels. These are
algebraic controls, not actual Weil countermodels or a nonimplication
from all original Weil identities.

With the authenticated original NF24 archives at the documented paths:

```sh
python3 scripts/certify_native_remaining_background_nf31_106.py --output /tmp/nf31.json.gz.b64
python3 scripts/validate_native_remaining_background_nf31_106.py /tmp/nf31.json.gz.b64 --output /tmp/nf31-validation.json
```

## Next frontier and scope

NF32 must obtain the remaining collective complete source Gram and its
signed mixed entries, with an appropriate joint high lift or sharper
response bound. The now-certified remaining native frame and inverse
give concrete inputs. The frozen response candidates are additional
probes, not substitutes for all remaining matrix directions.

Whole-domain53/50 positivity, full retained infinite-high Schur sign,
all-aperture continuation, RH, F4 and Lean remain open. Highest internally
certified whole-domain aperture remains21/20. Historical wording and
paused branches remain unchanged.
