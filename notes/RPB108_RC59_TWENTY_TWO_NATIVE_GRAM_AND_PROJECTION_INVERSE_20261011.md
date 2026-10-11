# RPB108 RC59 — 22-feature native Gram and projection inverse

RC59 extends the certified actual canonical native Gram interface from eight to **22 features**, at cap B=11/10. It supplies a validated inverse enclosure, 22 target trial columns in the existing 32-mode space, and a whole-map Riesz error upper bound. The original eight trial columns are preserved exactly.

For the actual native Gram M22 and exact physical native Gram P22,

\[
\boxed{\frac3{10}P_{22}\preceq M_{22}\preceq\frac{252}{257}P_{22}.}
\]

Thus the actual metric has condition number at most **840/257 < 3.269 after physical-Gram preconditioning**. This is a canonical metric certificate, not an original Weil-form positivity certificate.

RC58 proves that at least 22 consecutive native features are necessary for the revised source threshold. RC59 constructs the Gram/inverse interface for that first eligible head size. It does not establish that 22 features meet the source threshold or retain a positive original head floor.

## The enlarged native space

The physical features are q_j(x)=Chebyshev_j(x/B), j=0,...,21. Their actual canonical representatives R_j are defined by the Riesz identity

\[
\langle R_j,u\rangle_{\rm can}=\langle q_j,iu\rangle_{\rm phys}.
\]

Write R22 for the column map, M22=R22*R22, and P22 for the physical Gram of the q_j. The exact Chebyshev-to-Legendre conversion matrix C22 is computed by polynomial recurrence and rational triangular elimination. Its diagonal is positive, so the features are independent. The physical Gram is C22* D22 C22, with Legendre mass D_nn=2B/(2n+1).

The actual canonical Gram lower bound is positive definite; consequently the native representatives are also independent, and their actual orthogonal projection has rank 22.

## Variational Gram attachment

Let Gnom be the existing certified 32-mode canonical Legendre trial-metric center, D32 its physical mass matrix, and Gactual the actual canonical metric on that trial space. RC56's attached constant correction yields the corrected mass-relative metric error delta_G < 1e-7. RC59 pays the rounded budget epsilon=1e-7:

\[
G_{\rm actual}\preceq G_{\rm nom}+\epsilon D_{32}.
\]

An exact rational PSD check verifies Gnom>=D32, hence Gactual<=(1+epsilon)Gnom. Let X be the exact 32-by-22 physical Legendre/native pairing matrix, X_nj=D_nn C_nj for n<22 and zero otherwise. Projection of the actual native representatives onto the 32-mode trial space gives the Ritz bound

\[
M_{22}\succeq X^*G_{\rm actual}^{-1}X
\succeq\frac1{1+\epsilon}X^*G_{\rm nom}^{-1}X.
\]

The exact rational inverse of Gnom is checked on both sides. The final Ritz matrix is rounded downward with diagonal row-sum Loewner transport, producing the stored Mlo. Exact rational PSD checks prove Mlo>=0.3 P22.

The inherited global canonical embedding bound supplies M22<=rho P22, rho=252/257. The resulting Mup=rho P22 is checked above Mlo. The argument does not identify the finite trial solve with the unknown actual Riesz inverse.

## Validated actual inverse envelope

The midpoint of Mlo and Mup is rounded entrywise to denominator 10^18, producing a rational SPD center C0. Rounding is paid by a diagonal row-sum allowance. The stored error majorant E obeys

\[
-E\preceq M_{22}-C_0\preceq E,\qquad
E\preceq\frac{11}{20}C_0.
\]

Replay also checks the equivalent direct endpoint inequalities

\[
\frac9{20}C_0\preceq M_{\rm lo},\qquad
M_{\rm up}\preceq\frac{31}{20}C_0.
\]

The exact rational center inverse C0_inverse is verified by multiplication in both orders. Matrix-order inversion therefore gives the certified actual enclosure

\[
\boxed{\frac{20}{31}C_0^{-1}\preceq M_{22}^{-1}
\preceq\frac{20}{9}C_0^{-1}.}
\]

After preconditioning by this center, the actual metric condition number is at most 31/9. These factors describe a validated enclosure; C0_inverse is not asserted to equal the actual inverse.

All 253 upper-triangle actual Gram entries are enclosed, including exact zero opposite-parity entries. The first eight features' entries are intersected with their finer RC56 enclosures. The coarser new whole-matrix interval does not replace those previously established low-eight certificates.

## Trial responses and error interface

The exact nominal 32-mode solve is performed for all 22 Legendre targets, then rounded by the same denominator-10^30 rule used in RC38. After conversion by C22, it supplies the 32-by-22 native trial matrix V22. Its first eight columns equal the previously certified native trial matrix exactly.

Let J=R22*V22=X*V22, computed by exact physical pairing; T=V22*V22 in the physical metric; and GTnom=V22*Gnom V22. For the actual Riesz error E22=R22-V22, the exact identity is

\[
M_{22}=J+J^*-G_{\rm trial,actual}+E_{22}^*E_{22}.
\]

It gives the safe whole-map upper bound

\[
E_{22}^*E_{22}\preceq
M_{\rm up}-J-J^*+G_{T,\rm nom}+\epsilon T.
\]

The emitted upper matrix is checked PSD. The actual physical Riesz-error Gram is at most rho times that canonical upper matrix. This is an initial broad error interface derived from energy identities. It is not a fine evaluation of all 22 physical residual covariances. The tighter previously certified low-eight error bounds remain available separately.

## Actual projection characterization

With the actual inverse enclosed above, the enlarged actual canonical projection is characterized by

\[
\Pi_{22}u=R_{22}M_{22}^{-1}R_{22}^*u.
\]

Its kernel consists of vectors whose first 22 physical native moments vanish. The construction certifies the Gram, rank, inverse enclosure, trial responses, and exact projection interface. It does not evaluate the actual projection coefficients for the complete original source; that requires its attached mixed-source data.

## Verification and remaining obligations

Generation and independent replay pass. Replay independently reconstructs P22 by direct rational integration of the Chebyshev polynomials and the Ritz entries by scalar double sums. It checks both metric inverse identities, PSD transport of rounding, the actual inverse envelope endpoints, coefficient rounding, and exact preservation of the original eight trial columns. No floating eigensolver enters the accepted certificate.

From the repository root:

```sh
python scripts/validate_rpb108_rc59_twenty_two_native_projection.py > certificates/rpb108_rc59_twenty_two_native_projection.json
python scripts/validate_rpb108_rc59_twenty_two_native_projection.py --replay certificates/rpb108_rc59_twenty_two_native_projection.json
```

The enlarged original Weil head floor and enlarged projected-source threshold are both open. The existing actual low-eight floor Q8>=M8/2,900,000 remains valid. RC59 supplies no complement floor for the 22-feature complement; the inherited RC44 floor still belongs to the 1250-feature complement. No full 1250 projection, whole-aperture positivity, aperture extension, RH, or F4 completion is claimed.

The next frontier is a sharper 22-feature Riesz residual covariance and the enlarged signed head/source attachment. Those calculations can now use the exact native conversion, fixed trial coefficients, and validated inverse interface established here.
