# NF25 — Original directional source Gram and scoped estimator rejection

This additive registry uses NF24's exact fixed polynomial target p and
CC64's full high-response correlation formula, including nonzero measured
source coordinates. No historical definition is changed.

For one physical parity let E=E112, F=E^perp and let phi1,phi2 be the
measured H2 modes. Define r=P_F Lp and Gj=P_F Lphi_j. The **original
directional source Gram** is the physical L2 Gram of (r,G1,G2). It is a
three-by-three complete-source object for ONE retained seed, not the full
58-column source Gram or the collective retained residual matrix P2.

Its entries are P=<r,r>, z_j=<Gj,r>, and D_jk=<Gj,Gk>. Let C2 be the
original native form on H2 and u_j=Q(p,phi_j), which is retained explicitly.
Set V=D-kappa C2 and zbar=z-kappa u, with kappa=207/1000. The **two-mode
correlated response majorant** is U=(P-zbar*V^-1*zbar)/kappa. It is an
upper bound on the true full high response; it is not that response itself.

The **rational moment Gram** uses the regular arch kernel r_320, preserves
the exact endpoint logarithms, and uses degree40 pole exponentials and
fixed rational retained projection centers. Every coefficient and moment
is enclosed outward. Its physical source approximation errors are paid
entrywise before it is used as the original source Gram.

**Scoped estimator rejection** means that the certified U/Q(p) exceeds
one. It rejects U<Q(p) as a sufficient sign certificate for this fixed p
and these measured modes. It proves neither actual high response >=Q(p)
nor negativity, a null, or nonimplication from all original Weil identities.

CC64's sharpness concerns completions compatible with C2, the measured
high-source tail and kappa. A failed optimal majorant shows that improving
the choice of Y within those two measured sources cannot close this
particular estimator. Additional original high-form information may do so.
