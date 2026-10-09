# CC55 terminology — measured residual phase geometry

* **Original split and data:** at a=53/50, A is the complete original physical E112 retained parity matrix; phi1=e112/e113 and phi2=e114/e115 are the two measured exterior modes. d1=Q(phi1,phi1), c=Q(phi1,phi2), d2=Q(phi2,phi2); bi(x)=Q(x,phii). All original signed channels remain.
* **High C-orthogonal residual mode:** psi=phi2-(c/d1)phi1. Its native high energy is d_delta=d2-c^2/d1>3; the residual source column is b_delta=b2-(c/d1)b1. Physical orthogonality is not asserted.
* **First and residual response:** G1=|b1|^2/d1; T2=|b_delta|^2/d_delta; G2=G1+T2. The relative norms are R1=sup G1/A, R_delta=sup T2/A and R2=sup G2/A. In general R_delta is not R2-R1.
* **A-energy source angle:** between A-Riesz vectors A^{-1}b1/sqrt(d1) and A^{-1}b_delta/sqrt(d_delta), measured in the positive A inner product. Its squared cosine sigma is coordinate-invariant; it is not the physical L2 angle between high modes.
* **Measured source-active plane S:** span{A^{-1}b1,A^{-1}b_delta} in the retained parity space, with the A inner product. A positive lower frame bound here means G2(x)>=lambda_minus A(x) for x in S. This does not identify S with a critical spectral subspace.
* **Measured kernel:** the A-orthogonal complement of S, equivalently ker b1 intersect ker b_delta=ker b1 intersect ker b2. It has dimension54 when the two source columns are independent.
* **Residual response on first-source kernel:** the supremum of T2/A over ker b1; equal to R_delta(1-sigma). A positive supremum is an upper norm attained by some direction, not a positive lower frame bound over that kernel.
* **Scope:** actual two-mode source geometry at one aperture, not the complete F112 inverse response, full critical geometry, CC52 moment-carrier transfer, or an all-cap defect-relative frame bound.
