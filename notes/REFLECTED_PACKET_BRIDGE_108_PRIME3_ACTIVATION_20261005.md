# RPB108: prime 3 activated; 36-moment complement certified

Base: 3362c62b580a0fc40addcbdfb6bb0d6140ed4bc7.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_ACTIVATION.md.

## Results and scope

At a=11/20, the actual prime set is {2,3}. The newly computed native twenty-vector restriction is strictly positive with physical margin 1/32000000. The actual twenty interior sources use five exact prime panels; all 400 source/native pairings agree within the certified source error. This is finite source custody, not whole-domain positivity at this aperture.

The old twenty-moment complement sufficient estimate becomes inconclusive after prime 3 is included. Increasing the number of annihilated physical moments to 36 restores actual complement coercivity:

Q_a(f)>=(1/4)||f||_2^2,
Q_a(f)>=(9/100)||f||_(H_a)^2,

uniformly for 1/2<=a<=11/20 and f physically orthogonal to sqrt((2n+1)/(2a))P_n(x/a), 0<=n<36. Thus the actual sign at 11/20 reduces exactly to the corrected 36-coordinate form. It has not been decided. The certified whole-domain endpoint exclusion remains through 27/50.

## Actual prime matrix and source panels

Rational logarithm enclosures establish log(3)<11/10<log(4). The native matrix adds both actual correlations with shift y=log(n)/(2a) and coefficient 2log(n)/sqrt(n), for n=2,3. Native archimedean and pole terms are recomputed at a=11/20 in the same orthonormal physical basis.

Here L=4a=11/5 is slightly above log(9), so the previous exponential remainder multiplier 9 is not valid. The constructor uses 10 and checks L<log(10). The existing kernel multiplier 3 is retained using log(4)<L<9/4. Exponential order 80, Bernoulli pairs 60, gamma order 12 and outward grid 10^-120 remain sufficient. All twenty unshifted and shifted interval pivots pass after certifying the raw margin 1/32000000. The negative diagonal control is rejected.

For the source construction, d=2a=11/10 and t=(x+a)/d. Kernel A_d, endpoint H terms, constant -gamma-log(2pi)-log(d), actual pole exponentials and physical pole moments retain the established scaled analytic construction, evaluated with the new d. The source normalization is sqrt((2i+1)/d), and the JSON errors are physical L2 errors. The source-map error is below 1.114e-26.

Writing ell_n=log(n)/d, the panels are cut at 0,1-ell_3,1-ell_2,ell_2,ell_3,1. On the first panel both positive translates are active; on the second only prime 2's positive translate is active; on the middle neither is active; on the fourth only prime 2's negative translate is active; on the fifth both negative translates are active. Each source contribution is -(log(n)/sqrt(n))p_i(t plus or minus ell_n). This retains the actual prime-2/prime-3 coexistence and avoids rounding the narrow edge-panel widths.

Exact primitive integration of the sources against the twenty native trial vectors checks all 400 mixed entries. The largest discrepancy is below 9.716e-34 and lies within every source row's error. Dropping prime 3 would change the normalized constant-vector pairing by at least 0.0016003695, far beyond the source error, and is rejected by the omission control.

## Why shrinking overlap does not give a small physical norm

Let d=11/10 and s=log(3). Since d/2<s<d, the supported translation by s pairs a left edge strip of length d-s with a disjoint right edge strip of the same length. On their union C_3 is the swap operator; on the middle it vanishes. Hence ||C_3||_(L2->L2)=1. Equal normalized functions on the paired strips attain this norm. For example the two-strip indicator is in the supported logarithmic form domain, since its Fourier transform decays as O(1/|xi|).

The prime-3 form therefore has absolute value at most A||f||_2^2, A=log(3)/sqrt(3), approximately 0.6342841006. This bound is sharp on physical L2 regardless of how short the nonzero overlap is. A different estimate may exploit logarithmic energy or the moment conditions; small overlap by itself does not justify a smaller uniform physical L2 bound. This does not contradict the existing norm continuity on the logarithmic carrier.

With k=20 and T=43/10, the prime-2-only physical complement bracket at a=11/20 is approximately 0.3117827381. Subtracting A leaves approximately -0.3225013625. This is an inconclusive lower bound, not an actual negative witness and not a universal impossibility theorem for twenty moments. In particular the old inverse factor 3 cannot simply be reused on that basis.

## Restored coercivity with 36 moments

Use k=36 and T=7. The established integrated-Bessel majorant is

rho(a,T)=4aT [2a(22/7)T]^(2k)/[((2k+1)!!)^2(1-q)],
q=[2a(22/7)T]^2/[(2k+1)(2k+3)].

The pole bound is p(a)=16a(a/2)^(2k)/(k!)^2. Both majorants increase with a where q<1, so evaluating at 11/20 bounds all apertures in [1/2,11/20]. Prime 2 remains active throughout. Prime 3 is zero below its activation and otherwise obeys the same compressed bound A, since s>a on this entire interval.

For the prime-2-only symbol m_2, the established actual estimates are m_2(t)>=log|t|-1/(2|t|)-S_2 and m_2(t)>-10, with S_2=sqrt(2)log(2). At T=7 put c=log(T)-1/(2T)-S_2. Subtracting the compressed prime-3 penalty globally gives

Q_a(f)>=[c-(10+c)rho-p-A]||f||_2^2.

The certified bracket is greater than 0.2599128395, hence greater than 1/4.

For w(t)=log(e+|t|), w(t)<=log|t|+3/|t|. The rational check

(9/10)log(7)-(4/5)/7-S_2-A>0

shows m_2(t)-A>=w(t)/10 for |t|>=7, because the left side increases with |t|. On the low band w<3 (e<3 and e^3>10). Therefore

Q_a(f)>=[1/10-(10+A+3/10)rho-p]||f||_(H_a)^2.

The certified bracket exceeds 0.0999734085, hence exceeds 9/100. The same physical moment conditions control the Fourier low band and the pole moments. No spectral operator-domain membership is assumed.

The bounded physical projection onto E_36 and the logarithmic gap construct the exact form-domain lift z_e on F_36, as in the prior finite-complement theorem. Its physical inverse estimate is K_36<=4R_36. Exact square completion reduces all actual negative and weak-null directions to S_36=Q_36-K_36. This is a proved reduction with actual coercivity, not a sign certificate for S_36.

## Validation and next obligation

The native matrix and five-panel source certificates reproduce exactly. At 27/50 the extended native matrix constructor reproduces the preceding matrix certificate exactly. All 400 source/native pairings pass and reproduce exactly; omission of prime 3 is rejected. The scalar complement-limit and 36-moment complement certificates reproduce exactly. The matrix negative diagonal control is rejected. The scalar scripts check the constants in the analytic proofs above; arithmetic checks alone do not prove the compressed-translation norm statement.

Artifacts: scripts/certify_native_prime3_{matrix,source,pairings,complement_limit,complement36}.py and notes/data/RPB108_PRIME3_{MATRIX,SOURCE,PAIRING,COMPLEMENT_LIMIT,COMPLEMENT36}_CERTIFICATE_20261005.json.

Next: extend the actual matrix/source construction through degrees 20..35, build the full 36-source residual Gram retaining all cross terms on the five panels, then bound Q_36-4R_36 or construct sharper actual lifts. No full residual Gram at 11/20 is claimed here, and a twenty-coordinate estimator cannot replace the missing sixteen Schur coordinates.

Whole-domain positivity at 11/20, global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Whole-domain positivity through 27/50 remains intact. Lean source, axioms and prior CI claims are unchanged; this extension is not Lean formalized.
