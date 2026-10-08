# CC18 original odd closure terminology

All statements concern the original unshifted Weil form at `a=21/20`.
The [CC17 terminal definitions](TERMINOLOGY_RPB108_TERMINAL_ODD.md) remain in
force. Historical status statements in earlier files are not rewritten.

| Term | Definition |
| --- | --- |
| Original odd source frame72 | The sources of the physically normalized odd Legendre vectors of degrees3,5,...,111, CC17's precise weak vector, and the16 original complementary vectors of degrees113,115,...,143. Every source and source Gram product includes the original endpoint, prime and pole terms. |
| Weak source chart | The retained basis consisting of degrees3,5,...,111 and `w=10^-14 q`, where `q` is CC17's finite original odd trial. Its degree-one coefficient is nonzero, so it spans the entire original odd retained space. The weak vector has physical mass approximately3.888; it is not assigned unit mass. |
| `C` | The original positive compression to F112, with physical lower bound `c=699/1000`. It may be unbounded. Only its bounded inverse and finite operator-domain action columns are used. |
| `Z16` | The fixed original odd operator-domain trial columns of degrees113 through143. They are physically orthogonal to every retained degree0 through111. |
| `G_B`, `G_Z`, mixed source Gram | The actual physical L2 Gram matrices of the original retained F112 source columns, the original complementary actions `CZ`, and their complete mixed products. They are distinct from the native trial form matrix. |
| Native trial matrix `T` | `Z* C Z`, the original mixed Weil form on the sixteen trials. It is not `(CZ)*(CZ)`. |
| Matrix defect envelope | With `J=G_Z/c-T` and `H=(CZ)*B/c-Z*B`, the original retained Schur matrix dominates `A-G_B/c+H*L+L*H-L*J*L` for a rational full16-by56 lift `L`. All mixed terms and physical source errors remain. |
| Deterministic lower `K` | A rational matrix dominated by the complete interval matrix envelope after paying every interval uncertainty with a weighted diagonal and paying coefficient/endpoint rounding. Positivity is checked on the whole matrix. |
| Fixed-aperture closure | Strict coercivity on the entire original even and odd form domains at `a=21/20`. It is a theorem about this aperture, not a reusable continuation or non-stalling theorem. |
| Complete compression reaction | `<r_s,D_o^-1 r_s>` for CC17's original source `r_s=P_D L(10^-14 q)`, with the entire original positive odd `e111`-perpendicular compression `D_o`. The reaction retains odd55 and the infinite complement. |
| Reaction enclosure | Bounds on the actual complete reaction obtained from a native original trial lower and the certified original terminal Schur scalar lower. Such bounds can settle the sign without evaluating the infinite inverse exactly. |

Passing a fixed odd matrix test requires attachment through the original
positive infinite complement before it proves whole odd positivity. Joining
that result to CC16's inherited whole even closure yields fixed-aperture
whole-domain positivity. Source construction, native integration, full Gram
integration, independent matrix assembly, original infinite attachment and
Lean formalization are different verification scopes and must be labeled.
