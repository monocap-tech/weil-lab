# Original archimedean mixed coupling: finite physical-shift target

**W-ODD-NEG remains OPEN.** The new quantitative result bounds the COMPLETE small-shift contribution in the original 470x14 mixed block by 4e-7 in matched normalized coordinates. The remaining finite integral is not computed. A single complete raw-source shift node is retained as an explicit feasibility probe, not as an integrated operator certificate.

## Custody and unchanged coordinates

Base: PR #338 at fa7986b3fd83b8fd93014c886eb26943807e0202, successful Actions 40423854196. The canonical manifest still selects open W-ODD-NEG. Prior prime data and negative mixed budgets remain separate and unchanged.

Use ORIGINAL J470, actual continuous F14, exact physical projection X=(J*J)^-1 J*F and accepted exact dyadic C,D. Set W=(I-P_J)FC and U=JD. Then U*W=0 EXACTLY and the full physical trial frame is Y=[U,W]. The native interval X encloses that exact projection; its midpoint is not silently substituted.

The new workflow pins successful full-frame run 40417043904 at 0e3321350980247f8cba46cdbb45b717e49ad213, artifact 12694539474. Archive SHA256 e2c6017b35cd85ba404efa8013305d9e7c023d916cc1b2f96dbbcf7a7c8f772a. That archive retains BOTH matched inputs:

- si29_full_trial_preconditioner.json, SHA256 87d6f3ae24cde489adaf9ab3ac7efa612bc82bd78c6c9e94866802fdc550052f;
- si29_full_J_L2_normalization.json, SHA256 c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60, copied after the earlier native-custody check in that accepted run.

Run/source/artifact/archive and BOTH JSON hashes are verified before replay. The frame also retains the exact D candidate fingerprint 37c01971e3f63843cc15454172a46cad9079b6b64705e24cd9bb1bb4287c73e0. No native projection or frame factorization is repeated.

## Original digamma form and finite physical support

The original arch multiplier is Harch(xi)=Re psi(1/4+i*pi*xi)-log(pi). Subtracting the digamma integral at z=1/4 from the one at z=1/4+i*pi*xi in [NIST DLMF 5.9.16](https://dlmf.nist.gov/5.9.E16), taking real parts, and substituting t=2s gives

    Harch(xi)=c0+integral_0^infinity k(s)[1-cos(2*pi*xi*s)] ds,
    k(s)=2 exp(-s/2)/(1-exp(-2s)), c0=psi(1/4)-log(pi).

The kernel and factors are those of the ORIGINAL quarter-digamma, not a whole-line inverse approximation. An exact rational Laplace-series regression checks the change-of-variable factor against the original digamma positive summands.

Let Z denote physical zero extension, tau_s whole-line translation, and

    C_s=Z*(tau_s+tau_-s)Z/2,
    A_s=U*C_s W.

The positive form I-C_s permits Tonelli on diagonal forms and polarization for mixed forms. The native trial functions have interior H1 derivatives and finite traces. The explicit translation estimate below controls the small-s integral; exponential decay controls the large-s diagonal integral. These observations justify this form representation on the finite original trial, conditional on its inherited original realization/domain identities.

Since U*W=0, the c0 term and all scalar identity terms have ZERO mixed action. Since the zero-extended physical supports have length 2B, C_s=0 for s>=2B, B=11/10. Therefore

    U* Harch W = -integral_0^(2B) k(s) A_s ds.

For odd original sources this same A_s is the clipped overlap used in the prime calculation, with the appropriate source transformation:

    (J*C_s W)_ij = integral_(-B)^(B-s) W_j(x) J_i(x+s) dx.

This removes any infinite frequency cutoff from this mixed arch component. It does NOT compute the remaining finite integral or prove that a naive node grid is efficient.

## Rigorous cancellation of the singular small-shift kernel

The accepted frame gives exact-rational upper bounds

    E >= ||Y(B)||^2 approximately 50014.52438895423,
    L >= trace(Yprime*Yprime) approximately 6327724199.340357.

For an odd physical f with v=|f(B)| and d=||fprime||, decompose the whole-line translation difference into its interior overlap and TWO boundary strips. Cauchy and the fundamental theorem of calculus give

    ||(tau_s-I)Z f||^2
       <= 2s v^2+(8/3)s^(3/2) v d+2s^2 d^2,   0<s<=2B.

The interior term is at most s^2 d^2. Each boundary value is bounded by v+sqrt(t)d, and the two strip integrals supply the other terms. Thus the COMPLETE coefficient Gram

    G_s=[(tau_s-I)Z Y]*[(tau_s-I)Z Y]

satisfies 0<=G_s<=t(s)I with

    t(s)=2Es+(8/3)s^(3/2)sqrt(E L)+2Ls^2.

Exact U*W=0 implies (G_s)_(U,W)=-2 A_s. Moreover, 0<=G_s<=tI implies ||G_s-tI/2||<=t/2, so its offdiagonal block has norm <=t/2. Consequently

    ||A_s|| <= t(s)/4
            = Es/2+(2/3)s^(3/2)sqrt(E L)+Ls^2/2.

This uses the full 484D frame and pays every mixed source coefficient simultaneously. It is not a sum of entrywise bounds or positive source tests. An exact orthogonal odd-polynomial regression verifies the endpoint cusp and bound; a rank-one PSD Gram regression checks the quarter factor.

Because exp(2s)>=1+2s, k(s)<=1/s+2. Taking any rational R>=sqrt(E L) yields the complete near-zero error bound

    ||integral_0^delta k(s) A_s ds||
       <= E(delta+delta^2)/2
          +R[(4/9)delta^(3/2)+(8/15)delta^(5/2)]
          +L[delta^2/4+delta^3/3].

The checker obtains the INTEGER ceiling R=17789832 from the exact E,L. Choosing the first square-dyadic cutoff that pays a 1e-6 tolerance gives delta=2^-36. Its complete operator error is at most approximately 3.6434279856404313e-7, strictly below 1/2500000=4e-7. All roots of delta and final arithmetic are rational; no floating bound is used.

The remaining exact numerical target is now

    -integral_(2^-36)^(11/5) k(s) U*C_s W ds,

with a proved 4e-7 source-normalized operator allowance for the omitted part. The allowance itself is NOT a quadrature error for the remaining interval. Exact physical orthogonality is essential: an approximately projected or endpoint-aligned replacement cannot simply drop the constant/identity terms.

## Complete midpoint-node feasibility check

At s=B, the right clipped endpoint B-s is exactly ZERO. The prior prime-point evaluator excluded this case because separate Ci/log and 1/x expressions are singular there, even though their regularized primitives are entire and normalized to zero.

A new rational-shift wrapper computes B-s as an EXACT rational before conversion, and returns the exact zero primitive at that endpoint. No ancestral helper is altered. The original primitive-series, translation/odd-reflection and ALL fourteen continuous-feature degree-255 Taylor product checks are run at this node, including actual first moments and the pole.

The probe then computes the COMPLETE 470x14 raw-J value of -k(B) J*C_B W, retaining all 6580 entry balls and a joint exact-Fraction radius. The local node took about 45 seconds. This is an actual node value and implementation-cost diagnostic. It is not an integral lower/upper or proof of a quadrature mesh. The retained raw-J node/error must be transported through the actual D before use with the normalized small-shift allowance.

A separate standard-library replay checks all native entry radii and the coupled operator bound while requiring the status DIAGNOSTIC_COMPLETE_ARCH_SHIFT_NODE_NOT_INTEGRAL and false quadrature/integral flags.

## Work still required

The physical representation and singular-endpoint allowance are quantitative original mixed-operator information. The arch integral over the remaining finite interval, its complete coupled quadrature error, and the actual normalized arch matrix remain uncomputed. A single node costs tens of seconds in this implementation; a many-node run needs a certified error plan and a measured cost estimate first. No full integration campaign is launched from this probe, and no method-class impossibility is claimed.

The prime block is computed and the negative mixed block has its separate budget. A complete Astar mixed block still needs the arch result and matched source-coordinate/error transport. Actual Astar projection, matched forcing, inverse response value, signed odd Schur and infinite-operator transfer remain OPEN. Native enclosure validity, the analytic form/translation proof, exact arithmetic CI and independent original analytic/domain review retain separate standing. W-ODD-NEG, even/CC27/Weil/RH remain OPEN. Draft/unmerged, stacked on PR #338.
