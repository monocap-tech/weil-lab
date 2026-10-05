# RPB108: whole-domain sign at the prime-3 aperture a=11/20

Base: e7de495b5d034e516a04bd0ae222bc5fb3cd35bb.
Definitions: docs/TERMINOLOGY_RPB108_PRIME3_WHOLE_DOMAIN36.md.

## Result

On the actual canonical supported logarithmic form domain at a=11/20,

Q(h) >= (1/4000000000) ||h||_2^2.

This excludes fixed-aperture weak null modes and establishes the corresponding full-source WD-T10 unit domination. The actual prime powers 2 and 3 are included. No retained witness/null identification or global endpoint exclusion is inferred.

## Stronger physical complement bound

The previous full residual Gram certificate showed that the sufficient factor 4 was too large. Even the previous unrounded complement factor approximately 3.847444 failed on its recorded rational vector. That historical obstruction remains valid.

The existing integrated-mass theorem can give a stronger 36-moment bound by moving only its physical frequency cutoff from 7 to 763/100. A rational-grid search identified this useful value, but the proof uses only its exact rational evaluation. No optimal-cutoff theorem is claimed. The actual source or native matrix is not changed.

For a<=11/20, k=36, and T=763/100, set y=2a(22/7)T and q=y^2/(73*75). The same proved low-frequency bound is

rho(T)=4a T y^72 / [(73!!)^2(1-q)].

At the upper aperture rho is below 0.001343, and q<1. The upper-aperture bound dominates all smaller apertures by monotonicity of the positive factors in a. With S=sqrt(2)log(2), A=log(3)/sqrt(3), and c(T)=log(T)-1/(2T)-S, the actual prime-2 background satisfies m_2>=-10 on the low band and m_2>=c(T) on the high band. The latter lower symbol increases with frequency. The prime-3 compressed adjacency has norm at most one on the supported carrier, so its form loss is at most A||h||_2^2. The existing 36-moment pole bound is p=16a(a/2)^72/(36!)^2. Thus

Q(h) >= [c(T)-(10+c(T))rho(T)-p-A] ||h||_2^2

for every lawful complement vector. The exact interval lower bracket exceeds 0.3372633707 and hence 1/3. Prime 3 is conservatively bounded by A throughout the uniform interval [1/2,11/20], including its inactive portion; no continuity premise across its activation threshold is needed.

The logarithmic proof retains its independent cutoff T_log=7 and the original low-mass estimate. Its physical-frequency split is not replaced by 763/100. This preserves logarithmic coercivity 9/100 and lawful form-domain lift existence. The new physical bound 1/3 proves the inverse factor 3.

## Same-source corrected sign

The complete 36-source Gram, all 1296 pairings, source enclosure errors, endpoint log products and five prime panels are taken from the already reproduced certificate. None is recomputed with a different projection or normalization. Input hashes bind the native matrix, source enclosures, full Gram and stronger complement certificate.

Let delta be the recorded actual Gram operator error, below 2.84e-25. Rational outward elimination at grid 10^-200 proves all 36 pivots of

Q_36-3 Rhat_36-(3delta+1/40000000)I

strictly positive. Consequently Q_36-3R_36 >= (1/40000000)I, and the actual corrected form Q_36-K_36 has at least this margin because K_36<=3R_36. This resolves the sufficient-estimator obstruction without asserting that its former negative vector was a negative full-form witness.

## Whole-domain assembly

The actual residual-map norm squared is at most trace(Rhat_36) upper+delta. The lawful physical lift norm squared is therefore at most 9 times this quantity, which is below 43.077<49. Use the integer lift norm bound L=7.

For h=e+u, with e in E_36 and u in its lawful form complement, square completion gives

Q(h) >= tau||e||_2^2+(1/3)||u+lift(e)||_2^2,

while ||h||_2^2<=2(1+L^2)||e||_2^2+2||u+lift(e)||_2^2. Therefore

Q(h) >= min(tau/[2(1+L^2)],1/6)||h||_2^2
       = (1/4000000000)||h||_2^2.

The carrier is the same supported logarithmic form domain; no spectral operator-domain membership is assumed. The strict lower bound excludes actual weak null modes on this aperture.

## Validation and scope

The stronger complement certificate and whole-domain certificate reproduce byte-for-byte. All 36 shifted pivots pass; replacing the first diagonal by -1 is rejected. Source, native and Gram input hashes pass. The previously certified full Gram and all 1296 pairings are reused unchanged. The prior factor-4 obstruction is preserved as historical work.

Artifacts: scripts/certify_native_prime3_complement36_optimized.py, scripts/certify_native_prime3_whole_domain36.py, and notes/data/RPB108_PRIME3_{COMPLEMENT36_OPTIMIZED,WHOLE_DOMAIN36}_CERTIFICATE_20261005.json.

Next: a larger aperture with its actual prime panels and lawful complement, or a proof of global endpoint exclusion. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. Lean code, axioms and earlier CI claims are unchanged; these analytic/rational certificates are not Lean formalized.
