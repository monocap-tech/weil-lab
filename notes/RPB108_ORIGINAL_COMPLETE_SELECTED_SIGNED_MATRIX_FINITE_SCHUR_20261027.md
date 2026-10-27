# Complete original selected signed matrix and a matched finite Schur split

Bounded continuation of draft PR #353. The selected original source space
is fixed at 242 dimensions, including the true sinh pole. This does not
add source directions, change the original signed form, or promote an
acceptance/RH status. W-ODD-NEG and original domain/realization review stay OPEN.

## GitHub-first inputs

Require successful run 40590794034 at
bb244109b37c599ed21ee6e40016060b4aba90f5, artifact 12773198729,
`original-signed-joint-frame-budget`, archive SHA256
`bb2669985194888b2e2f7e76403be754d1a2ee631d1950c761bf15dc233cb449`.
The workflow hashes TEN exact retained JSONs, replays accepted rank,
signed-block validation and joint frame budget, then executes this native
matrix construction, independent mixed Cauchy validation, and rational
matched-forcing Schur replay. There is no original low-frequency quadrature.

## Two-variable analytic kernel, including coincidence

Use the same complete original complex-bilinear sine kernel as #351/#353.
Write S_c(z)=sin(c z)/z with its entire value c at zero, and
G(nu,mu)=S_B(nu-mu)-S_B(nu+mu). For the inherited analytic Laplace function I,
let D_I(nu,mu)=(I(nu)-I(mu))/(nu-mu). The complete arch component is

    G (A(nu)+A(mu))/2
    + cos((nu-mu)B) D_I(nu,mu)/2
    - cos((nu+mu)B) D_I(nu,-mu)/2.

I is odd. At a coincident exact center nu0=mu0, if I_n denotes its Taylor
coefficient there, the coefficient of h^a k^b in D_I(nu0+h,nu0+k) is
EXACTLY I_(a+b+1), with no binomial factor. Distinct centers use the formal
coefficient recurrence for division by d+h-k (or d+h+k). Entire sine/cosine
jets of the sum/difference arguments include binomial(a+b,a) and the sign
on the second argument. Products are rectangular Taylor convolutions.
Exact rational center identity determines coincidence; subtraction of two
interval copies is never used to infer an exact zero denominator.

The complete seven-prime shift correlation uses the same entire S_c
kernels. The pole overlap is -i G(nu,i/2), an entire expression also at
the true pole. The pole term is -2 H(nu)H(mu). Apply BOTH angular derivative
factors (-1)^floor(a/2) a! and (-1)^floor(b/2) b!, and a factor -i for each
true pole generator. There are no extra 2pi derivative factors.

All 29,403 upper-triangle entries (58,564 full matrix entries) are computed.
Every prime AND pole upper-triangle component is independently checked
against the original clipped polynomial/trigonometric physical primitives.
Every coincident block has symmetry and original diagonal checks, and all
distinct blocks have original one-variable jet slice checks. The largest
required I Taylor coefficient is order 27. A separate rigorous 256-point
Cauchy check verifies the coincident mixed (13,13) derivative using only
the original one-variable kernel; its alias bound is about 1.50814e-34.
That cross-check does not independently establish all refined digits.

## Double-frame error budget and fixed coordinate candidate

The full raw calculation uses 3072-bit native arithmetic and N=384 Laplace
terms. The same elementary strip/Cauchy proof gives a clean function tail
2^-2420 and coefficient tail 2^-2420*4^k on radius 1/4. Add this tail before
jet operations. The upper term limit of the inherited parameterized helper
is extended to 384; existing parameter values and formulas are unchanged.

Rebuild the same actual physical frame D at 4096 bits, verify .99 I<=D*H D
<=1.01 I against the ORIGINAL physical Gram and match its accepted complete
coefficient fingerprint. If rho bounds each raw signed entry radius, then

    ||D*Delta W D||_F^2 <= (2^496)^4 * 242^2 * rho^2.

Both this uniform bound and all actual transported native radii must pass
the diagnostic 2^-80 error target. This remains a diagnostic, not an assumed
Schur reserve. This is a separate two-frame budget; #353's one-frame budget
was not reused as sufficient.

The fixed candidate file contains FOUR exact dyadic coordinate vectors
inside the SAME selected span, proposed by a floating eigensolver. NO
numerical eigenvalue enters any proof. Deterministic midpoint Householder
choices give four nonzero exact dyadic reflection vectors; each exact
rational H_v=I-2vv*/(v*v) is orthogonal identically. Native arithmetic also
checks the full product's orthogonality. Thus Q is an invertible coordinate
change; it introduces no additional physical direction. Reconstruct the
complete finite signed matrix M=Q*D*W_selected D Q. Retain every upper
triangle native ball, outward-rounded at 1536 bits for storage.

## The ACTUAL finite matched Schur calculation

Partition the retained finite matrix as M=[[C,B*],[B,H]], with dimensions
4 and 238. A midpoint Cholesky candidate D_H is accepted ONLY after verifying
.99 I<=D_H*H D_H<=1.01 I against the original interval H. With an upper bound
V on ||D_H||_F^2, H>=gamma I for gamma=.99/V. This is a FINITE block floor.
It is not a floor on a larger infinite complementary space.

Choose an exact dyadic inverse-action candidate Y. Compute the MATCHED
residual R=H Y-B and rho_S=||R||_F^2/gamma. The exact finite Schur matrix
obeys

    S_up-rho_S I <= C-B*H^-1 B <= S_up,
    S_up=C-B*Y-Y*B+Y*H Y.

This pays the full inverse-action residual with the actual matched forcing;
it neither holds forcing fixed during inverse perturbations nor adds
unmatched component inverse charges. Native interval LDL examines the four
lower-bound pivots. The rational replayer independently recomposes H Y,
R, S_up and its lower matrix from ALL retained finite matrix entries and
exact Y, then performs interval LDL anew if native positivity is claimed.
Native physical/kernel congruences and the 238-block positive normalization
are separately rebuilt in CI; the rational ledger is not a substitute for
those native verifications. Their coefficient/error bounds remain explicit.

The output's finite_selected_signed_positive_definite_certified flag is
asserted only when all four lower-Schur pivots are strictly positive. An
unresolved sign is recorded as unresolved, never inferred from floating
coordinates or source positivity for Astar.

## Runtime guard and stopping point

A first validation implementation hit the 150-second raw/check guard because
it rebuilt the same one-variable jets for many pairs. Reusing those jets
keeps every independent prime/pole check. The raw/check guard is unchanged;
the complete finite calculation has a separate 300-second guard. The true
pole returns a scalar in one reference slice; the validation wrapper treats
that scalar consistently with its order-zero source.

Stop at the complete finite signed block and its checked finite Schur
result. The global physical complement from #351 still has its inherited
signed-form floor >.00098, but its mixed action with the selected span is
UNCOMPUTED. Neither the finite 238-block floor nor a positive finite Schur
matrix controls that missing mixed term. No finite BS block, global inverse
response, full infinite Schur sign, global W positivity or RH closure is
claimed. Further work must budget that actual complementary coupling before
any additional matrix/source/precision campaign.

## Local finite result before GitHub replay

The complete native run took about 186 seconds. The verified 238-block
coefficient floor is about 1.88904e-12. All four finite lower-Schur pivots
are strictly positive, approximately 1.23336e-17, 3.14456e-23, 1.20542e-29,
and 1.79058e-32. These certify positive definiteness of the complete signed
restriction to the FIXED selected physical span. They are LDL pivots, not
eigenvalues or a global coercivity constant. The full infinite mixed Schur
obligation remains open.
