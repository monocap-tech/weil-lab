# NF37 — a fixed high polynomial with an arbitrary correction functional

These definitions are additive; historical NF31–NF36 wording remains unchanged.

**Free correction functional:** for the NF35 ordered family M=(v,t,u34) and the exact NF36 high polynomial z, let lambda be any real three-vector. The corrected family is M_lambda=M-z lambda^T. Thus all three columns may change independently along z. The retained components remain (x,w,u32) because z lies in the original high space F. This includes NF36's lambda=(0,0,tau), but uses only one high polynomial, not three independent high directions.

**Correction floor data:** kappa=207/1000, U=Q-Gamma/kappa, e=beta-zeta/kappa, and d=qz-gamma_z/kappa, using NF36's complete original signed responses and physical error payments. The corrected floor is U_lambda=U-e lambda^T-lambda e^T+d lambda lambda^T. Native energy and source covariance are updated separately by the same bilinear expansion.

**Loewner ceiling:** when the true d is negative, V=U-e e^T/d satisfies U_lambda=V+d(lambda-e/d)(lambda-e/d)^T and U_lambda <= V for every real lambda. The ordering refers to quadratic forms. A midpoint functional selects a rational diagnostic candidate; it does not prove that candidate's sign or identify the exact real maximizer.

**Universal fixed witness:** a frozen rational vector h gives a=h^T U h and b=h^T e. With x=lambda^T h, h^T U_lambda h=a-2bx+dx^2. The outward rational upper bound a_upper+|b|_upper^2/(-d_upper), if negative, rejects every free correction functional using this fixed z. It is independent of the interval enclosure of the ceiling matrix and does not require a sampled search over lambda.

**Moved obstruction:** a correction may make NF35's original mixed witness positive while a different fixed witness remains negative. Positivity of the old witness is not positivity of the complete joined matrix.

**Scope of rejection:** a universal negative floor witness rejects this named scalar-floor certificate family. It does not prove a negative original Weil form, reject another high polynomial, rule out independent high directions, or rule out a sharper actual inverse-response estimate. The prior four-direction restriction and separate two-direction restriction with all F remain valid. Whole-domain 53/50, RH, F4 and Lean remain open; the whole-domain anchor stays 21/20.
