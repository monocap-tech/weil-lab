# RPB108: full-domain positivity at aperture 51/100

Base: de27a603637822527757aebffb379b62065d00c7.

## Definitions and result

At a=51/100, H_a is the actual supported logarithmic form domain, E_20 is the physical span of e_n(x)=sqrt((2n+1)/(2a))P_n(x/a) for 0<=n<20, and F_20 is its physical L2 complement in H_a. Q_a is the actual native mixed form. The scaled interior source q_e represents Q_a(e,f)=<q_e,f>_2 on H_a. The full residual Gram R_20 is the Gram of (I-Pi_20)q_e for the physical orthogonal projection Pi_20 onto E_20. These are the same vectors used in the native matrix certificate.

The corrected Schur form S_20 is Q_20 minus the actual F_20 lift energy K_20, constructed using the previously certified logarithmic complement coercivity. The new actual-source certificate and full mixed residual Gram certify

S_20 > (1/10000000)I,
Q_a(h) >= (1/520000000)||h||_2^2 for every h in H_a.

The weak kernel is therefore zero at this larger aperture, and the established same-vector energy factorization gives full-source WD-T10 unit domination there. Under the established canonical positivity-aperture theorem, the first positive endpoint is strictly above 51/100 or absent. This is a fixed-aperture result; global endpoint exclusion and all-window domination are not inferred.

## Scaled actual source construction

Set d=2a=51/50 and t=(x+a)/d. Retain L(t)=-(log(t)+log(1-t))/2 exactly. The physical endpoint logarithm is L(t)-log(d); the term -log(d)p(t) is included in the smooth source. It is not omitted under dilation.

The scaled regular archimedean kernel is

A_d(s)=(ds)exp(-ds/2)/(1-exp(-2ds))=(1/2)B(2ds)exp(-ds/2),
B(z)=z/(1-exp(-z)).

Expand B through 64 and the exponential through 60. With N=60 and K=32, the existing Bernoulli and alternating-exponential arguments give

|A_d(s)-Atilde_d(s)| <= ce s^(N+1)+cb s^(2K+2),
ce=(3/2)(d/2)^(N+1)/(N+1)!,
cb=4(d/3)^(2K+2)/(1-(d/3)^2).

The rational checks give exp(d/2)<2 and B(2ds)<3 for 0<=s<=1. The latter follows from 2d>log(4) and 2d<9/4. These are the same kernel bounds with scaled arguments, not an assumption that the half-aperture kernel is unchanged. Integrating (1/2-Atilde_d(s))/s gives the nonconstant endpoint H polynomial. Its error is he=ce/(N+1)+cb/(2K+2); the regular difference-integral error uses ae=ce/(N+2)+cb/(2K+3).

The constant is -gamma-log(2pi)-log(d). The regular left polynomial is constructed from the same p_i(t) and Atilde_d; Legendre reflection constructs the right polynomial. The pole exponentials are exp(plus or minus d(t-1/2)/2). Their moments include the physical measure factor d. Their exponential remainder is ee=2(d/4)^(N+1)/(N+1)!, and both moment/output errors are enclosed by 10d*ee. Thus each unnormalized smooth-source error is bounded by 2he+2i(i+1)ae+10d*ee plus its coefficient radii.

Only prime 2 is active. Its coefficient remains log(2)/sqrt(2), while its coordinate shift is log(2)/d. The three exact panels are [0,1-log(2)/d], [1-log(2)/d,log(2)/d], [log(2)/d,1]. Their endpoints are interval enclosed; they are not rounded cutoffs.

The physical source normalization is sqrt((2i+1)/d). Multiplying a uniform unnormalized source error by this factor and then by sqrt(d) for its L2 norm yields sqrt(2i+1) times that error. The JSON row error fields and source-map error are these physical L2 bounds. The combined error eta is below 7.48e-29.

## Full mixed residual Gram and source custody

After changing variables, the physical measure d cancels the two source normalization denominators. The Gram and mixed pairing formulas therefore retain the factor sqrt((2i+1)(2j+1)), while all smooth functions and prime cutoffs are newly computed. The exact L(t) residual Gram and projection moments are aperture-independent in this normalized coordinate; the constant -log(d)p_i lies in E_20 and its residual projection is zero. It is nevertheless included in the full source and pairing computation.

The calculation retains log/log, smooth/smooth, both log/smooth cross terms and every projection product, for all twenty coordinates. Polynomial and logarithmic primitive integrals are evaluated rationally on the exact prime panels at outward grid 10^-120. The source/native mixed pairing comparison covers all 400 entries. Its maximum discrepancy is below 7.03e-36 and within every source row's certified error.

The source approximation contributes an operator error delta=eta(2M+eta), where M bounds the surrogate residual-map norm by the square root of its trace. The certified delta is below 2.62e-28. The maximum residual Gram entry enclosure width is below 1.59e-52. Native and source JSON byte hashes are pinned in the Gram certificate.

## Corrected sign and whole-domain coercivity

The previous uniform complement theorem gives Q_a(f)>=(2/5)||f||_2^2 and Q_a(f)>=(9/100)||f||_(H_a)^2 on F_20. The latter constructs the lawful form-domain lift z_e; no physical spectral operator-domain membership is assumed. The former gives K_20 <= (5/2)R_20.

Rational interval elimination of Q_20-(5/2)Rtilde_20-(5/2)delta I-(1/10000000)I yields twenty strictly positive pivots. Therefore S_20>(1/10000000)I. Replacing the first diagonal of the checked lower matrix by -1 is rejected.

The certified lift norm satisfies ||z_e||_2<=5||e||_2: its squared bound (5/2)^2[trace(Rtilde_20)+delta] is below 19.075, hence below 25. Write h=e+f and v=f+z_e. Exact square completion gives Q_a(h)=S_20(e,e)+Q_a(v). Since e and z_e are physically orthogonal,

||h||_2^2 <= 52||e||_2^2+2||v||_2^2.

Combining the Schur and complement margins proves the stated whole-domain bound 1/520000000. The existing aperture inclusion and canonical endpoint results transfer this to exclusion of a first positive endpoint at or below 51/100; this turn supplies no explicit additional aperture beyond 51/100.

## Validation and cursor

The new source JSON reproduces exactly. At a=1/2 all twenty source coefficient/error rows and the source-map error agree exactly with the earlier source constructor. The full larger-aperture Gram certificate reproduces byte-for-byte. All mixed source/native pairings satisfy their errors; all twenty shifted pivots are positive; the negative diagonal control is rejected. These validate the arithmetic certificate together with the analytic scaling proof above. They are not a new Lean theorem or CI result.

Artifacts: scripts/certify_native_larger_aperture_source.py, scripts/certify_native_larger_aperture_gram.py, notes/data/RPB108_LARGER_APERTURE_SOURCE_CERTIFICATE_20261005.json, and notes/data/RPB108_LARGER_APERTURE_GRAM_CERTIFICATE_20261005.json.

Next: larger apertures or an independent global endpoint exclusion. Prime 3 first activates at log(3)/2; it is not present here. Global endpoint exclusion, all-window unit domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean source, axioms and prior CI claims are unchanged; this new analytic/rational certificate is not Lean formalized. Historical half-aperture claims remain unchanged.
