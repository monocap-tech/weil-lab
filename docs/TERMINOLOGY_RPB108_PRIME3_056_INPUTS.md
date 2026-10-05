# RPB108 aperture 14/25 native inputs terminology

- Aperture a=14/25=0.56: actual physical support [-a,a], coordinate t=(x+a)/(2a), width d=28/25.
- Q_36(a): actual native form restricted to the physical orthonormal Legendre vectors sqrt((2n+1)/(2a))P_n(x/a), degrees 0..35. This is the raw restriction before the complement lift correction.
- Five actual prime panels: cuts 0,1-log(3)/d,1-log(2)/d,log(2)/d,log(3)/d,1. Only prime powers 2 and 3 are active because log(3)<d<log(4).
- Source enclosure: exact endpoint logarithm plus the certified rounded panel polynomials, with physical L2 errors retained. The endpoint logarithm is not rounded.
- Physical cutoff 15/2: selected rational frequency split proving 36-moment physical complement coercivity 31/100 uniformly through a=14/25. No optimal-cutoff claim is made.
- Logarithmic cutoff 7: independent split retaining logarithmic complement coercivity 9/100.
- Inverse factor 100/31: the sufficient lawful complement inverse bound implied by physical coercivity 31/100.
- R_36(a): full actual residual Gram after removing exactly the same 36 physical Legendre coordinates. It must be computed from the sources at this aperture.
- Corrected form: Q_36(a)-K_36(a), with K_36(a)<=(100/31)R_36(a). Raw matrix positivity and complement coercivity alone do not certify its sign.

The source/native pairings, full residual Gram and corrected sign at 14/25 remain separate obligations. Whole-domain sign is certified at 11/20 by the earlier certificate. Global endpoint exclusion, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open. These rational/analytic inputs are not Lean formalized.
