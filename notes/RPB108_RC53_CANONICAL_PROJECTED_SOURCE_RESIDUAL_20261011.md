# RPB108 RC53 — canonical projected combined-source residual

2026-10-11 UTC. Parent RC52:
`98b0a36ff5171e972aae6c607040d3bfd095ae33`.
Only `research/rpb108-route-consolidation` is written.

## Result and scope

The complete signed bounded-remainder source now has a paid canonical
orthogonal residual bound outside the actual low-eight native span:

    Gamma_8=sigma_total^*(I-Pi_8)sigma_total
       <=3.2375584720655657... M_8 <(1619/500) M_8.

Here Pi_8 is the canonical orthogonal projector onto the actual native
Riesz representatives 0 through 7. The scalar allowance improves
RC52's unprojected 3.773930291713645... M_8 bound by more than a factor
1.165, or approximately 14.2 percent. This is a certified upper bound,
not an evaluation of the actual residual Gram entries or projector.

All eight source columns are covered. The projector targets an
eight-dimensional actual native span; the complete 1250-feature
projection and source map remain unconstructed. This allowance is
far above RC44's sufficient final source-Gram gate of M/90000, which
concerns the full 1250-feature system. That gate is not met here.

Generation and independent square-completion replay pass. RC52's six
positive individual directions and 1/21 floor on span{r_6,r_7} are
preserved. The full original head floor and whole-aperture positivity
remain open. No RH/F4 or Lean closure is claimed.

## Projection and variational definitions

Use the canonical logarithmic Hilbert space D, its physical inclusion
i with ||i||^2<=rho=252/257, the actual native Riesz map R, and its
Gram M_8=R^*R. Let V be the emitted rounded 32-mode native trial map.
Keep RC52's bounded physical action

    K=K_arch+K_prime+K_pole,
    sigma_total=i^* K iR.

Both signed pole actions are included. Since M_8 is positive definite,

    Pi_8=R M_8^(-1) R^*,
    Gamma_8=sigma_total^*sigma_total
       -(R^*sigma_total)^* M_8^(-1)(R^*sigma_total).

The actual source Gram and exact projection coefficients are not
evaluated. Instead choose a concrete rational coefficient matrix L.
For every coefficient vector a, orthogonal projection minimizes distance:

    ||(I-Pi_8)sigma_total a||_D
       <=||sigma_total a-R L a||_D.

This inequality is valid for any L. Consequently an exact solve of a
rational center can be used without identifying it with the unknown
actual canonical projection solve. All errors in replacing R by V
and the true source by its nominal trial action remain paid.

The original full source also contains the canonical identity column R.
Since (I-Pi_8)R=0, its projected residual is exactly the same Gamma_8.
This does not remove the identity contribution from the original head.

## Concrete rational reconstruction coefficients

Let G_0 be RC40's rational center of the actual native Gram, with its
emitted exact inverse N_0. RC40's actual inverse enclosure and relative
Gram error below 11/5000 are inherited; the validator verifies both
inverse products and the positive physical lower bound for G_0.

Let H_0 be the center of RC52's nominal complete trial remainder head,
and R_h its entry halfwidth matrix. Choose

    L=N_0 H_0,
    G_0 L=H_0 exactly.

L preserves parity. It is a concrete approximate projection coefficient
map into the actual span ran(R). It is not RC41's oblique reconstruction
operator, nor the actual solution of M_8 C=R^*sigma_total. The variational
argument makes a separate exact-solve error estimate unnecessary;
actual metric and Riesz-map discrepancies enter the residual bound.

## Nominal variational residual

RC52 provides a nominal physical source F_nom, its physical Gram upper
envelope U_nom, and the nominal physical pairing

    H_nom=(iV)^*F_nom,
    |H_nom-H_0|<=R_h entrywise.

The true trial action differs from F_nom by at most delta ||iV a||_2,
with the inherited delta<49/200000. Define the nominal canonical vector

    Y_nom=i^*F_nom-V L.

Its squared norm uses the canonical trial Gram, not the physical trial
Gram T. From RC38's directed metric enclosure,

    V^*V <=G_trial,up=V_leg^* G_metric,nom V_leg+E_metric T.

The validator checks T against the exact Legendre physical mass matrix.
The whole canonical trial metric error E_metric T is retained.
Thus the nominal residual Gram is bounded by

    Y_up=rho U_nom-H_0^*L-L^*H_0
          +L^*G_trial,up L+D_round.

To pay nominal head interval rounding, let Z=|L| entrywise and
E_round=Z^* R_h+R_h^* Z. Set D_round to the diagonal of E_round's row
sums. The elementary inequality 2|a_i a_j|<=|a_i|^2+|a_j|^2 proves
that this diagonal majorizes the uncertain Hermitian cross terms.
All arithmetic and rounding allowances are rational.

## Actual source and actual reconstruction errors

Let E=R-V. RC47 provides whole-map canonical and physical bounds

    E^*E<=B_can,
    (iE)^*(iE)<=B_phys.

These correlated matrices are retained. RC52 supplies the complete
physical operator parity bounds k_even and k_odd. Write
S=diag(k_(j mod 2)); opposite-parity errors vanish. Paying both the
actual physical Riesz-map error and archimedean source approximation gives

    D_source=(33/32) S B_phys S+33 delta^2 T,
    (K iR-F_nom)^*(K iR-F_nom)<=D_source.

Now decompose the actual canonical variational residual:

    sigma_total-R L
       =Y_nom+[i^*(K iR-F_nom)-E L].

For any u>0 the bracketed error has Gram bounded by

    D_u=rho(1+u)D_source+(1+1/u)L^*B_can L.

This pays the reconstruction error E L in the canonical norm, while
the physical source error is lifted through i^*. Replacing either norm
by the other without these factors would not give this certificate.
For any t>0, another Young inequality yields

    Gamma_8 <=(sigma_total-R L)^*(sigma_total-R L)
             <=A_(u,t)=(1+t)Y_up+(1+1/t)D_u.

Exact rational PSD bisection verifies A_(u,t)<=lambda_(u,t) P for
42 rational parameter pairs. The selected pair is u=1/16, t=1.
RC39's M_8>=alpha P, alpha=8947777583/17179869184, then proves
Gamma_8<=(lambda_(u,t)/alpha)M_8. No floating eigenvalue or unpaid
trial-to-actual identification is used.

## Independent replay

Generation forms Y_up from its four source/head/metric terms. Replay
instead sets L_opt=G_trial,up^(-1)H_0 and D=L-L_opt, and uses

    Y_up=rho U_nom-H_0^*G_trial,up^(-1)H_0
          +D^*G_trial,up D+D_round.

Exact rational equality verifies this independent square-completion
expression against the emitted envelope. Replay also constructs the
physical error term by full diagonal congruence S B_phys S rather than
entrywise parity scaling. Both paths reproduce the entire certificate,
including the exact coefficient solve, rounding allowance, canonical
metric error, actual transfers and rational residual PSD bounds.

## Evidence boundary and next work

Entrywise subtraction of an uncertain projection is too expensive with
the present bounds. The certified construction instead approximates the
projected source by actual native representatives and pays its full
variational residual. The improvement is modest: it demonstrates a
valid projection attachment, not a nearly closed residual gate.

The remaining tasks include sharper canonical source lifting, stronger
actual-map error control, and enlargement of the projection beyond
eight native features. The complete 1250-column source map, full original
head floor and final projected-source gate are still open. The low-eight
bound cannot be extrapolated to those unevaluated columns. No new
aperture positivity follows. RC44's complement floor and RC45's full
head-conditioning certificate are preserved.

## Reproduction

Inputs, in order: RC39 native Gram, RC40 native inverse, RC47 correlated
transport, RC43 prime head, RC38 metric, and RC52 complete source covariance.
Input hashes and shared dependencies are checked.

    python scripts/validate_rpb108_rc53_projected_source_residual.py
    python scripts/validate_rpb108_rc53_projected_source_residual.py --replay certificates/rpb108_rc53_projected_source_residual.json
