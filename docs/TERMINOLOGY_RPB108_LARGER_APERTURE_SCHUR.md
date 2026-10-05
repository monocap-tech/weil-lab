# RPB108 larger-aperture source and Schur terminology

- **Scaled actual source:** the actual L2 interior source representing Q_a(e_i,f) on the supported logarithmic form domain, using e_i(x)=sqrt((2i+1)/(2a))P_i(x/a). It does not assert physical spectral operator-domain membership or retained WD-T38 membership.
- **Scaled unit coordinate:** t=(x+a)/(2a), with physical measure dx=(2a)dt. It compares form calculations without identifying the analyses of dilated vectors.
- **Scaled endpoint-log split:** L(t)=-(log t+log(1-t))/2 retained exactly, with the physical constant -log(2a) included in the smooth source.
- **Larger-aperture full residual Gram:** the actual Gram of (I-Pi_20)q_i at a=51/100, including all source cross terms and projection products. Its input vectors are the same as the independently certified native matrix vectors.
- **Larger-aperture corrected sign certificate:** a rational enclosure proving Q_20-(5/2)R_20>(1/10000000)I, including the actual Gram operator error. This bounds the exact lift-corrected form from below.
- **Larger-aperture whole-domain coercivity:** Q_a(h)>=(1/520000000)||h||_2^2 for every supported logarithmic form-domain vector at a=51/100. It excludes that aperture's weak kernel and supplies full-source WD-T10 domination there, without global endpoint exclusion or retained witness/null transport.

These definitions extend the half-aperture terminology additively. Historical wording is unchanged. F4 and FULL TRANSPORT CLOSED remain open; no Lean formalization is claimed.
