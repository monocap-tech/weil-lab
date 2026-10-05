# RPB108: integrated Bessel bound closes the half-aperture Schur sign

## Domain and definitions

Work at a=1/2 on the existing supported logarithmic form domain H, with Fourier convention exp(-2pi i x xi). Q is the actual native prime, pole and archimedean form. E_20 has orthonormal physical basis sqrt(2n+1)P_n(2x), 0<=n<20; F_20 is its physical L2 complement inside H. All sources and residual Grams retain these same vectors. Definitions are recorded in docs/TERMINOLOGY_RPB108_INTEGRATED_BESSEL_SCHUR.md.

The earlier coercivity Q(f)>(9/100)||f||_H^2 on F_20 already constructs the unique actual form-domain lift z_e, characterized by Q(z_e,f)=Q(e,f) for f in F_20. Set K(e,e')=Q(z_e,z_e') and S_20=Q_20-K. No spectral operator-domain membership is assumed.

## Integrating before taking the maximum

For f in F_k the established plane-wave expansion gives

|fhat(t)|^2 <= ||f||_2^2 sum_(n>=k)(2n+1)|j_n(pi t)|^2,
|j_n(pi t)| <= (pi |t|)^n/(2n+1)!!.

Integrate these nonnegative majorants over [-T,T]; Tonelli is applicable. The factor 2n+1 cancels exactly with integration of |t|^(2n). With y an upper bound for pi T,

integral_(-T)^T |fhat(t)|^2 dt
 <= 2T sum_(n>=k) y^(2n)/[(2n+1)!!]^2 ||f||_2^2
 <= rho^2 ||f||_2^2,
rho^2=2T y^(2k)/[(2k+1)!!]^2 /(1-q),
q=y^2/[(2k+1)(2k+3)].

Indeed the exact ratio of successive integrated terms is y^2/(2n+3)^2, which is bounded by this slightly larger q for n>=k. This is a valid conservative geometric bound. It improves the previous uniform band-maximum bound without altering the carrier or moment conditions.

Choose k=20, T=9/2 and y=(22/7)T. The existing rational arctangent calculation proves pi<22/7. Only prime 2 contributes at this aperture, so its actual amplitude is S=sqrt(2)log 2, enclosed by the existing rational logarithm and square-root algorithms.

The actual native symbol satisfies m(t)>=log |t|-1/(2|t|)-S away from zero and m(t)>-10 everywhere. Therefore with c=log(T)-1/(2T)-S and the established pole bound p=8/[4^40(20!)^2],

Q(f)>=[c-(10+c)rho^2-p]||f||_2^2.

Outward rational bounds certify that this bracket exceeds 2/5 (its enclosure lower bound is approximately 0.40624888). The earlier logarithmic bound remains unchanged. Thus the actual complement inverse obeys K <= (5/2)R_20 instead of the previous coarse K<=5R_20. This constant follows from the native symbol and integrated observation bound; it is not assumed from a desired matrix sign.

## Rigorous full corrected sign

Use the previously certified actual native matrix Q_20, full residual Gram R_20 and its operator enclosure error delta<7.07e-29. Let Rtilde denote the enclosed surrogate matrix. Then

S_20 >= Q_20-(5/2)R_20
 >= Q_20-(5/2)Rtilde-(5/2)delta I.

Rational interval elimination verifies positive pivots after subtracting a further tau I, tau=1/10000000. Every entry, mixed term and source error is included. Consequently

S_20(e,e)>tau ||e||_2^2 for nonzero e in E_20.

Replacing the first diagonal of the checked lower matrix by -1 is rejected. All input hashes are pinned. The prior factor-5 estimator's negative direction remains a true historical result about that estimator; the sharper inverse bound resolves its insufficiency without changing its data.

## Whole-domain conclusion and explicit physical margin

The exact square completion is

Q(e+f)=S_20(e,e)+Q(f+z_e), e in E_20, f in F_20.

From Q(z_e,z_e)=<r_e,z_e> and complement coercivity,

||z_e||_2 <= (5/2)||r_e||_2.

The actual residual-map squared norm is at most trace(Rtilde)+delta. The certificate proves (5/2)^2[trace(Rtilde)+delta]<25, hence ||z_e||_2<=5||e||_2. If v=f+z_e, then

||e+f||_2^2=||e-z_e+v||_2^2
 <=2(1+25)||e||_2^2+2||v||_2^2.

Here e and z_e are physically orthogonal, since z_e belongs to F_20. Combining the two coercivity margins yields

Q(h)>=(1/520000000)||h||_2^2 for every h in H.

Thus Q has no nonzero weak-null vector at a=1/2. The former twelve-coordinate Schur sign obstruction at this aperture is closed. By the already established same-vector energy/factorization criterion, full-source WD-T10 unit domination and its continuous contraction on the positive-energy completion hold at this aperture. No independent retained WD-T38 witness attachment or null transport is inferred.

## Scope and validation

The implementation is scripts/certify_native_integrated_bessel_schur.py; exact rational data and pivots are in notes/data/RPB108_INTEGRATED_BESSEL_SCHUR_CERTIFICATE_20261005.json. The certificate invokes the prior logarithmic complement checks, verifies the improved constants, checks the full matrix with the actual Gram error, proves the lift norm bound and rejects the negative control. It reproduces deterministically. The native and Gram input hashes are pinned and verified.

This closes a fixed-aperture sign problem, not all-window positivity or global endpoint exclusion. Under the already established canonical aperture theorem the first positive endpoint cannot occur at or below a=1/2. No explicit larger-aperture margin is computed. F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and previous CI claims are unchanged; this new analytic/rational certificate is not Lean formalized.
