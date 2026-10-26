# SI29: all 14 directions survive the full original J470 projection

## Standing and custody

The active obligation is W-ODD-NEG and remains open. This supplies original-operator inverse/rank information needed for its matched SI29 Schur response. It is not another positivity test of a selected source span. No new source direction is proposed.

Parent custody is draft PR #327, commit `d1ad210db31c0fcf50a836f3392d473f6e9eabb6`, successful Actions run `40373098137`, artifact `12672553450`. That result bounds the actual projected energy in the PR #326 Taylor coordinates by 1.02e-111 I, but does not establish a quantitative lower bound. PR #326 had explicitly left independence modulo the full J470 unproved. This note supplies that analytic argument and exact original-geometry witnesses. Historical certificates are not rewritten.

The result is an analytic theorem with exact-rational hypothesis/witness checks, not a Lean proof or independent analytic audit. The original operator realization, domain and Astar coercivity remain inherited assumptions. Rank of the explicit physical functions themselves uses only their stated formulas and standard analytic uniqueness.

## Explicit original objects

The 107 distinct positive SI10 centers c_j have b9 orders p_j summing to 469. Their supported odd physical generators are x^k sin(2*pi*c_j*x) for even k and x^k cos(2*pi*c_j*x) for odd k, 0<=k<p_j. Include the original odd pole s(x)=sinh(x/2). Call this synthesis map J. Exponential-polynomial uniqueness at the distinct exponents +/-2*pi*i*c_j and +/-1/2 proves rank(J)=470, as in SM35.

The true 14 SI29 features have entire formulas

    F_i(x) = integral_(c_i-r_i)^(c_i+r_i) rho_i(eta) sin(2*pi*eta*x) d eta,
    rho_i(eta) = 1/(2*r_i)                         for degree 0,
                3*(eta-c_i)/(2*r_i^2)             for degree 1.

These are the actual normalized means and 3 E[u h] first moments, not their Simpson approximants. The 12 distinct positive bands have disjoint interiors. Ten bands carry a single mean; the other two carry a mean and a first moment.

## Quotient independence without a 484-dimensional solve

Suppose F y=J a on the physical interval [-B,B], as L2 functions. The unsuppressed formulas on both sides are entire in x. Equality almost everywhere on this interval therefore implies equality of their entire continuations.

On these entire continuations, introduce the constant-coefficient differential expression

    L = (D_x^2-1/4) product_j (D_x^2+4*pi^2*c_j^2)^p_j.

It has order 940 and annihilates every original J generator, including the pole. Indeed each sine/cosine generator is a combination of e^(+/-2*pi*i*c_j*x) times a polynomial of degree <p_j, and the corresponding factors kill that polynomial. This argument applies before zero extension. It asserts no derivative identity for zero-extended functions, no bounded L2 functional and no commutation with Astar.

Differentiation under the compact frequency integrals is valid for the entire feature formulas. Hence L F y is the sine transform of the compactly supported integrable density sigma(eta) sum_i y_i rho_i(eta), where

    sigma(eta) = -(4*pi^2*eta^2+1/4) (4*pi^2)^469
                 product_j (c_j^2-eta^2)^p_j.

The identity L F y=0 implies this density is zero almost everywhere. To see this, extend the positive-frequency density oddly onto the reflected negative bands; its ordinary Fourier transform is zero, so uniqueness of the Fourier transform of finite measures gives the zero measure. Positive bands do not meet zero.

Inside any band, sigma is nonzero except at finitely many atomic centers. The remaining density is affine. Consequently the affine density vanishes throughout that band's interior. For a single mean this forces its coefficient to zero; for a mean/first-moment pair, two distinct interior evaluations force both coefficients to zero. Thus y=0 and

    rank(F modulo span(J)) = 14.

The checker supplies 14 rational interior evaluation points, all separated from every original atomic center by an explicit positive neighborhood radius. It records the exact nonzero nodal product at each point, the actual 14x14 density-evaluation matrix D and a rational inverse. Both D D^-1=I and D^-1 D=I are checked. This is an explicit witness for the final density argument; D is not a physical Gram matrix. Its conditioning says nothing about the physical projected Gram.

An independent way to audit the separation is to use real-axis growth first: finite-frequency features are bounded and the trigonometric source terms have polynomial growth, so an entire identity cannot contain a nonzero sinh coefficient. Fourier uniqueness then separates the remaining atomic distributions from the absolutely continuous feature densities. The annihilator proof avoids having to manipulate those atomic derivatives explicitly.

## Consequence for the actual reduced inverse

Let A=Astar be the original supported positive operator with inherited A>=kappa_star I, kappa_star=33621/10^9. Assume the original finite source and feature domain statements. Since J is independent, H=J* A J is strictly positive definite. Define

    W = F - J H^-1 J* A F,
    T_F = W* A W.

Quotient independence implies W y!=0 for every y!=0. Coercivity gives y* T_F y >= kappa_star ||W y||^2>0. Therefore T_F is a strictly positive 14x14 matrix and its ordinary inverse exists. This argument does not assign its minimum eigenvalue a numerical lower bound.

For the actual coordinates G=(F-H106)U from PR #326, H106 takes values in span(J). The exact checked identity M U=diag(scales), with every scale nonzero, proves U invertible. Hence

    T_G=U* T_F U >0,
    h_G=U* h_F for h_F=F*R0 and J*R0=0,
    h_G* T_G^-1 h_G = h_F* T_F^-1 h_F.

The projected L2 residual family also has rank 14, as does the energy-projected family. The full augmented physical span has dimension 484, but neither the proof nor the intended response calculation calls for a raw dense 484x484 inversion. The Schur correction remains 14-dimensional, with the full original J projection retained.

## What is now resolved and what remains

The exact-rank/kernel ambiguity is resolved: all 14 actual feature directions survive the full original J projection, and the reduced energy inverse exists under the inherited original hypotheses. This is separate from numerical usability. No quantitative T lower bound, energy condition number, normalized forcing entries or inverse response value has been computed here. In conjunction with PR #327, the result is 0<T_G<1.02e-111 I, not an order-one normalization.

The next numerical acceptance target is still a rigorously conditioned representation of this same projected 14-dimensional family and matched forcing, with full J projection/action accounted for. Point evaluation witnesses cannot be used as L2 norm bounds. Qualitative invertibility cannot justify a floating inverse, a precision budget or a truncation tolerance relative to the unknown minimum eigenvalue. W-ODD-NEG, original domain review, even-sector obligations, CC27/Weil transfer and RH remain open. No merge or obligation reassignment is implied.
