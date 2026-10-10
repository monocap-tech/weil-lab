# RPB108 RC31 — certified trial Riesz solves and full residual envelopes

Date 2026-10-10. Independent research/rpb108-route-consolidation.
Parent: 5fb1bfe6e05746820a6bf855dec0752c9cb17b14 (RC30).
No other research branch changed.

## Result

Eight polynomial trial Riesz vectors have been computed by exact rational
linear algebra against the enclosed physical metric. They approximate
the physical Legendre moment functionals. Full canonical residuals have
a proved conservative collective envelope

    ||sum_j a_j(r_j-v_j)||_D^2 <= (51/100) a^*D a.

This is a whole-space bound, not a finite-test residual. It is too coarse
to claim a small canonical inverse error for the native head gate.
The finite solve error is small; omitted trial-space response remains
the dominant uncertified-to-small quantity.

## Exact construction and finite uncertainty

Use RC30's rational center Ghat, diagonal physical mass D, and error E,
with -ED<=Gtrue-Ghat<=ED, E<1/2000.
Because the canonical Fourier metric dominates physical L2,
Gtrue>=D and Ghat>=(1-E)D.

Let V=Ghat^(-1)D, and define v_j=sum_i V_ij p_i, with
p_i=P_i(x/B). This targets physical Legendre moments; it does not
target all 8600 RC22 Chebyshev features.

The script computes V exactly and verifies Ghat V=D. Put

    J=D V, H=V^*D V.

For input coefficients a, the uncertainty in its true finite Galerkin
equation has canonical trial-dual norm <=E sqrt(a^*H a).
Therefore the difference between the computed v_a and the exact
finite Galerkin vector has canonical norm <=E sqrt(a^*H a).
In particular it is <=E/(1-E) sqrt(a^*D a).
This follows from Gtrue>=D and Ghat>=(1-E)D; it makes no assertion
about the omitted full canonical response.

## Full Riesz response and residual bound

Let r_j be the FULL canonical Riesz representative of
ell_j(h)=<p_j,i h>_2. Existence follows from ||i||<=1.
Define its full response matrix C_ij=<r_i,r_j>_D. The same inclusion
bound implies 0<=C<=D.

RC24 attaches the physical metric source to every polynomial v_j,
so all mixed pairings below are lawful on the complete form space.
Even without evaluating the physical source residual, variational
completion of the square gives

    C >= 2J - V^*Gtrue V >= J-EH.

Let Z be the Gram matrix of the ACTUAL full canonical errors r_j-v_j.
By the exact mixed Riesz identities,

    Z=C-2J+V^*Gtrue V <= D-J+EH=:U.

Thus 0<=Z<=U is a rigorous whole-space residual Gram bound.
It includes omitted modes through C<=D, rather than silently replacing
C by a finite inverse.

The executed exact rational certificate checks
J-EH>=0, U>=0, and

    U <= (51/100) D.

The per-column canonical error upper displays are approximately

    0.40280, 0.34370, 0.31022, 0.28596,
    0.26939, 0.25480, 0.24757, 0.23708.

Proof data are rational squared bounds in the certificate; the displayed
square roots are not used for certification.
These are upper bounds, not measurements or lower bounds on true error.

## Executed data and validation

Run:
python scripts/validate_rpb108_rc31_trial_riesz.py

The default input is certificates/rpb108_rc30_interval_trial_metric.json.
Local execution passed. The output certificate contains exact V,
the full response lower bound J-EH, full residual Gram upper bound U,
and all per-column squared bounds.

The validator verifies the solve identity, symmetry, and exact positive
semidefiniteness by rational Schur elimination. For zero pivots it
requires the remaining pivot row to vanish. No floating eigenvalue
test is used. Its input operator enclosure is RC30's interval
certificate; the analytic all-space inequalities are proved above.

## Next obligation and evidence boundary

This supplies actual trial coefficients and lawful whole canonical
residual upper bounds. It does not supply small physical residuals
p_j-L_B v_j, and it does not evaluate the true errors or full inverse.

The route can now improve the envelopes by evaluating the attached
physical residuals with both endpoint logs retained, by a sharper
response upper bound C, or by enlarging the trial space. The coarse
51/100 bound must not be advertised as satisfying RC23's head gate.

No native original Weil head/source matrix or aperture extension is
certified. RH/F4 and Lean closure remain open.
