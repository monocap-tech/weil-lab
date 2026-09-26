# SZ-CROSS-COLLAR ratification record — 2026-09-26

**Branch:** `sz-cross-collar`  
**Operation:** audit ratification only; no new traversal  
**Public promotion:** forbidden

## 1. Scope

This record ratifies the previously audited unratified movement
SZ-CROSS-COLLAR-1 through SZ-CROSS-COLLAR-4.

Later branch residue, including SZ-CROSS-COLLAR-5 and
SZ-CROSS-COLLAR-6, is outside this ratification pass and has no effect on the
canonical cursor.

## 2. Decisions

| Pass | Ratification | Canonical role |
| --- | --- | --- |
| SZ-CROSS-COLLAR-1 | RATIFIED | regular $G_a$-carrier realization of the collar residual and quantitative spectral-drop implication |
| SZ-CROSS-COLLAR-2 | PARTIAL / AUXILIARY | $C^1$ screw-potential lemma, first-order collar flatness, and distributional exterior identity accepted; endpoint-trace jet retained only under its explicit extra hypotheses |
| SZ-CROSS-COLLAR-3 | RATIFIED / CANONICAL HEAD | full closed-form-domain cross-collar theorem |
| SZ-CROSS-COLLAR-4 | NOT RATIFIED | abstract factorization lemma retained as residue; selected-coordinate preservation is not selected custody |

## 3. Ratified regular-carrier statement

For $0<c<b$, $u\in\ker G_c\setminus\{0\}$, and zero extension
$J_{c,b}u$, the enlarged residual

```math
\Delta_{c,b}(u):=\|G_bJ_{c,b}u\|
```

is the exact regular-carrier measure of failure of null persistence.

The ratified implication is

```math
\boxed{
\Delta_{c,b}(u)>0
\Longrightarrow
\lambda_b<0.
}
```

The explicit trial vector and non-optimized quantitative Rayleigh bound in
SZ-CROSS-COLLAR-1 are accepted.

## 4. Ratified auxiliary collar regularity

From Suzuki's local screw-kernel regularity and compact support of
$u\in L^2(-c,c)$, the project derives

```math
F_u\in C^1_{\mathrm{loc}}.
```

If $u\in\ker G_c$, then $F_u$ is constant on the old interval and hence

```math
F_u'(\pm c)=0,
\qquad
\Delta_{c,c+\varepsilon}(u)=o(\varepsilon^{3/2}).
```

The exterior second-derivative identity is accepted in the stated
distributional sense.

The stronger asymptotic

```math
F_u(c+\delta)-C_u
=
\frac{u(c-)}4\delta^2\log\frac1\delta
+
O(\delta^2)
```

and its collar-norm consequence are retained only under the explicit endpoint
trace and translated-sample regularity hypotheses of SZ-CROSS-COLLAR-2. They
are auxiliary and non-load-bearing.

## 5. Canonical full-domain theorem

Let

```math
q_a=Q_W^a,
\qquad
\mathcal F_a=\mathfrak D(q_a),
```

be Suzuki's localized closed form and its form domain.

For $0<c<b$, zero extension gives

```math
E_{c,b}\mathcal F_c\subseteq\mathcal F_b.
```

If

```math
0\ne k\in\ker A_c,
```

then the zero extension $\widetilde k=E_{c,b}k$ annihilates every old form
direction. Therefore the cross functional

```math
\Lambda_{c,b;k}([h])
:=
q_b(\widetilde k,h)
```

is well-defined on

```math
\mathcal F_b/E_{c,b}\mathcal F_c.
```

The ratified equivalence is

```math
\boxed{
\widetilde k\in\ker A_b
\iff
\Lambda_{c,b;k}\equiv0.
}
```

Moreover,

```math
\boxed{
\Lambda_{c,b;k}\ne0
\Longrightarrow
\lambda_b<0,
}
```

while

```math
\boxed{
\lambda_b=0
\Longrightarrow
\widetilde k\in\ker A_b.
}
```

Since $q_b(\widetilde k)=0$, one also has

```math
\boxed{
\lambda_b\le0
}
```

for every strict enlargement after this endpoint null mode has formed.

This is the canonical sharpening of
`AZ-FIN-WEIL-NULL-EXTENSION` supplied by the Suzuki bridge.

## 6. Rejected custody inference

The following inference is **not** canonical:

```text
same selected coordinate + negative full Weil value
=> selected packet owns the negativity.
```

Horizon 1 explicitly forbids that converse.

SZ-CROSS-COLLAR-4 proves only an abstract factorization alternative for the
cross functional relative to a selected-coordinate map. A future custody pass
must establish negativity of the selected defect itself, or an equivalent
typed ownership statement, before reconnecting the collar crossing to the
selected negative morphology.

## 7. Canonical head

```text
SZ-CROSS-COLLAR-3
FULL FORM-DOMAIN CROSS-COLLAR THEOREM
RATIFIED
```

No later SZ pass is canonical as a consequence of this ratification.

Further work requires a new individual NF order.
