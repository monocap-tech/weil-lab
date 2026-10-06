# RPB108 terminology: actual 84-source certificate at 41/50

Introduced with `REFLECTED_PACKET_BRIDGE_108_PRIME5_84_SCHUR_082_20261006.md`. These are the existing native physical conventions at a new explicitly audited aperture; they do not introduce a selected off-line packet.

- **Audited aperture:** a=41/50, physical interval [-a,a], source coordinate x=(u+a)/(2a). Native correlation length L=4a=82/25; source length d=2a=41/25.
- **Matched finite space V84:** the physical orthonormal Legendre degrees 0 through 83, with the same 84 moments annihilated by its L2 orthogonal complement W84.
- **Native enclosure Q84:** the full native restriction, including archimedean, signed pole and prime-power terms 2,3,4,5. Its compact representation stores 3,570 row-major lower-triangle integer endpoint pairs on outward grid 10^-80, with reflection supplying all 7,056 entries. Compact endpoints enclose the original 400-digit endpoints; this is outward widening, not lossless compression.
- **Actual source enclosure:** all 84 physical sources, with endpoint logarithms and nine ordered translation panels. Smooth coefficients are integer numerators over 10^40. Their certified physical L2 errors include coefficient rounding and all analytic remainders.
- **Residual surrogate Gram Rhat84:** the full Gram after subtracting the matching V84 projection. Endpoint-log/log, endpoint-log/smooth and smooth/smooth contractions and every mixed entry remain present. Its 14,112 exact endpoints are finite decimals on grid 10^-300.
- **Actual Gram error delta:** eta(2M+eta), where eta is the aggregate actual source-map L2 error and M is the certified surrogate residual-map norm upper bound. The actual residual Gram differs from Rhat84 in operator norm by at most delta.
- **Complement inverse factor beta:** 2, from the actual physical W84 coercivity c=1/2. The same complement has logarithmic lower bound 9/100.
- **Corrected margin tau:** a positive rational certified by outward pivots of Q84-2Rhat84-(2delta+tau)I. A positive finite Q84 alone does not supply this margin.
- **Lift bound J:** a positive integer with J^2>beta^2(trace_upper(Rhat84)+delta), bounding the energy-completion lift in physical L2.
- **Whole-domain physical coefficient mu:** tau*c/[tau+c(1+J^2)]. The inherited exact two-variable norm conversion gives Q_a(h)>=mu||h||_2^2 for the full native domain D_a.
- **Whole-domain logarithmic coefficient kappa:** mu/[10(mu+23)], obtained with the inherited actual Garding inequality. This bounds the existing logarithmic energy Elog on D_a.

Whole-domain here means every vector of the fixed native domain at this aperture. It does not mean all apertures, global endpoint exclusion, historical retained packet attachment, F4 closure, or a Lean proof.

**Certified outcome at 41/50:** the actual residual Gram is enclosed, but Q84-2R84 has a strictly negative certified direction. The same direction has strictly positive Q84 energy. Thus tau, J, mu and kappa above are conditional conversion definitions, not certified positive values for this pass. A negative sufficient lower estimator is not an actual negative vector for the full form. The established whole-domain frontier remains 81/100.

- **Estimator negative direction v:** the explicit 84-entry rational vector stored in the Gram certificate, with v*(Q84-2R84)v strictly negative after the complete Gram error is added to the quadratic upper bound.
- **Required inverse slack:** the positive lower bound -U, where U is that certified negative quadratic upper bound. A refined actual inverse-complement estimate needs to restore at least this directional energy before this estimator can certify positivity.
