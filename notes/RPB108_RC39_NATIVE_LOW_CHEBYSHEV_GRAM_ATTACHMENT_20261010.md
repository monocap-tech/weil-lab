# RPB108 RC39 — actual native low Chebyshev Gram attachment

2026-10-10. Branch `research/rpb108-route-consolidation`.
Recovered parent: `4f30e64e6add2458a0f429780dc455fffcddfd4e` (RC38).

## Result

The first eight features of RC22's actual 8600-feature head are now
attached to certified rational trial vectors and actual canonical Gram
enclosures. The native functionals are

    ell_k(h)=integral_-B^B T_k(x/B) h(x) dx,  0<=k<8,
    B=11/10.

Their actual canonical Riesz representatives are r_k^T. This is the
same supported logarithmic carrier as RC22 and RC38, rather than a
physical polynomial projection being substituted for the canonical head.

Let M_native be their actual canonical Gram, and M_phys their exact
physical Chebyshev polynomial Gram. The certificate proves

    (8947777583/17179869184) M_phys <= M_native
      <=(252/257) M_phys.

The lower factor is approximately 0.520829203480389 and the upper
factor approximately 0.980544747081712. Thus the first eight actual
native features are quantitatively independent in this physical metric.
This does not give a conditioning estimate for all 8600 features.

For the transformed thirty-two-mode trial map V_native and the actual
native Riesz map R_native, the all-coefficient approximation bound is

    ||(R_native-V_native)a||_canonical^2
      <= (1531371999127928832/561420614948974609375)
           a* M_native a.

This native-metric squared bound is approximately 0.002727673261,
with norm upper below 0.052228. It uses the actual canonical feature
metric, rather than only the physical input mass of RC38. The change
of metric is why this number is not directly comparable to RC38's
0.001420651892 physical-input squared bound.

The certificate also encloses all 36 upper-triangle entries of the
actual M_native: twenty same-parity intervals and sixteen exact
opposite-parity zeros. The diagonal displays below round lower bounds
down and upper bounds up; the certificate contains rational endpoints.

| Native feature | Actual canonical squared norm lower | Upper |
|---|---:|---:|
| 0 | 2.038929 | 2.043975 |
| 1 | 0.616036 | 0.617719 |
| 2 | 0.886824 | 0.889179 |
| 3 | 0.889226 | 0.891677 |
| 4 | 0.864218 | 0.866701 |
| 5 | 0.834661 | 0.837159 |
| 6 | 0.806038 | 0.808544 |
| 7 | 0.779601 | 0.782112 |

Only native features 0–7 are certified in this pass. The other 8592
features, the original Weil head matrix A, and the native bounded
remainder source Gram remain unevaluated. No head-floor or source-cross
acceptance condition from RC22 is discharged by this Gram certificate.

## Exact target conversion

RC22 defines T_0(t)=1, T_1(t)=t,
T_(k+1)(t)=2t T_k(t)-T_(k-1)(t). Expand each degree <=7 Chebyshev
polynomial in the exact Legendre basis:

    T_j(t)=sum_(i=0)^7 C_ij P_i(t).

The validator computes C using rational polynomial subtraction and
checks every reconstructed remainder is exactly zero. C is triangular
with positive diagonal, and respects parity. Therefore

    R_native=R_Legendre C,   V_native=V_RC38 C,
    M_phys=C* D C,

where D=diag(2B/(2i+1)), 0<=i<8, and * denotes conjugate transpose.
The conversion is exact: there is no target truncation, target sampling,
or additional target-approximation error. Every emitted V_native column
is a degree <=31 rational polynomial. It remains an approximation to
the native canonical Riesz representative, not its exact realization.

## Actual Gram brackets from the error identity

For the Legendre targets, write R for the exact Riesz map and V for the
RC38 emitted trials. Define

    M_L=R*R,
    J_ij=ell_i(v_j)=D_ii V_ij,
    H_actual=V* G_actual V,
    H_hat=V* G_hat V,
    T=V* M_32 V.

Here J is not assumed symmetric: RC38's emitted coefficients were
explicitly rounded. The exact Hilbert-space identity is

    (R-V)*(R-V)=M_L-J-J*+H_actual.

RC38 certifies 0<=(R-V)*(R-V)<=beta D, where
beta=91276884027/64250000000000. Its enlarged metric error E gives

    -E T <= H_actual-H_hat <= E T.

Thus, with K=J+J*-H_hat,

    L:=K-E T <= M_L <= U:=K+E T+beta D.

This uses the positive whole canonical Riesz-error Gram. It does not
replace the actual canonical Gram by a nominal finite trial Gram or
subtract approximate matrices without an error budget.

Exact rational LDL and bisection certify L>=alpha D for
alpha=8947777583/17179869184. Congruence by C yields the stored native
Loewner brackets C*L C and C*U C, and M_native>=alpha M_phys.
RC32's supported inclusion bound gives the independent upper
M_native<=(252/257)M_phys. Positive definiteness of the physical Gram
follows from the Legendre mass and invertible exact C.

The error conversion is now lawful:

    (R_native-V_native)*(R_native-V_native)
      <=beta M_phys <=(beta/alpha) M_native.

All finite matrix inequalities are verified with exact rational
arithmetic. Actual Riesz vectors are not assumed to be polynomials.

## Actual entry enclosures and reflection

RC38 also gives T<=t_V D. Center the Legendre Gram enclosure at
K+(beta/2)D. Its normalized operator error is at most

    tau=E t_V+beta/2,

approximately 0.001146546710. After conversion, center
N=C*[K+(beta/2)D]C satisfies

    -tau M_phys <= M_native-N <=tau M_phys.

The Hermitian operator bound implies, for individual entries,

    |(M_native-N)_ij|
      <=tau sqrt(M_phys,ii M_phys,jj).

Use directed interval square roots and round the resulting entry
endpoints outward to denominator 10^12. The stored Loewner brackets
are matrix inequalities, not entrywise inequalities; the separate
entry enclosures above are the valid entrywise claims.

Reflection x->-x is unitary for the supported canonical metric because
its Fourier weight log(e+|xi|) is even. The Riesz representative of
ell_j inherits the parity of T_j. Consequently opposite-parity actual
Gram entries vanish exactly. These zeros are not inferred just from
nominal trial coefficients.

## Reproduction, execution and scope

Run from the repository root:

    python scripts/validate_rpb108_rc39_native_low_chebyshev_gram.py > /tmp/rc39.json

Default inputs are the committed RC38 metric and residual certificates;
explicit paths are also accepted. Proof data are in
`certificates/rpb108_rc39_native_low_chebyshev_gram.json`, including
the input digest, exact conversion and native trial coefficients,
physical Gram, canonical Loewner brackets and actual entry enclosures.

Execution: PASS. Exact polynomial conversion, parity, native physical
Gram positivity, quantitative canonical Gram lower bound, trial Gram,
native-metric error bound and all entry enclosure budgets passed.
A separate saved-certificate replay checked these matrices and bounds.
The analytic attachment is the Hilbert/Riesz error identity and exact
RC22 target equality; its input whole error and metric budgets remain
RC38's analytic plus interval certificates. Decimal assumptions remain
RC30's documented correctly rounded arithmetic behavior.

Next: attach additional native feature ranges or certify the actual
bounded remainder sources for this low native block. Canonical feature
Gram conditioning is distinct from the original Weil head floor
A>=m M_native and the source-residual acceptance condition. Neither
is proved here. No full 8600-feature canonical projection, new aperture
positivity, RH/F4 result or Lean closure is claimed. Only this research
branch receives new files; previous artifacts are preserved.
