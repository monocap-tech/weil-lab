# RPB108: constructive actual smooth-source enclosure

## Statement and custody

At aperture a=1/2 put t=x+1/2 and v_i(x)=sqrt(2i+1)P_i(2x), 0<=i<=7. Let q_i be the previously proved actual interior source representing Q(v_i,f) on the supported logarithmic form domain. Set L(t)=-(log t+log(1-t))/2 and h_i=q_i-v_i L. No operator-domain, retained membership, simplicity, positivity or density hypothesis is added.

There are explicit rational polynomials p_i on each of the three panels [0,1-log 2], [1-log 2,log 2], [log 2,1], with degrees at most 131, such that

|| h_i-sqrt(2i+1)p_i ||_infinity <= epsilon_i.

For the map from the eight physical coordinates to L2, the combined error eta=(sum epsilon_i^2)^(1/2) is bounded above by 1.2955294230763636e-30 (display only; the JSON stores an exact rational upper bound). Values at the two prime cutoffs can be assigned either one-sided convention without affecting L2 custody. The polynomial surrogate uses the exact actual prime panels, not rounded cutoff locations.

## Kernel construction and error proof

Let K(s)=exp(-s/2)/(1-exp(-2s)) and A(s)=sK(s). Define B(z)=z/(1-exp(-z)). Approximate B(2s) by its Bernoulli polynomial through 64 and exp(-s/2) by its Taylor polynomial through 60; their product divided by two is Atilde. Both constant terms are exact and Atilde(0)=1/2.

For 0<=s<=1, the standard Bernoulli bound |B_(2k)|/(2k)! <=4/(2pi)^(2k), with pi>3, gives a tail bounded by 4(s/3)^66/(1-1/9). The exponential alternating-series remainder is at most (s/2)^61/61!. Also B(2s)<=3 and the absolute exponential polynomial sum is below 2. Consequently

|A-Atilde| <= ce s^61+cb s^66,

ce=3/(2^62 61!), cb=(4/3^66)(9/8).

The removable endpoint function H(d)=J(d)+(log d)/2, J(d)=atanh(exp(-d/2))+atan(exp(-d/2)), satisfies H(0)=log 2+pi/4 and H'(d)=(1/2-A(d))/d. Its nonconstant polynomial approximation is obtained by integrating -[Atilde(d)-1/2]/d. The uniform H remainder is at most he=ce/61+cb/66.

For a trial polynomial p=P_i(2x), |p|<=1 and |p'|<=i(i+1). Expanding p(x+/-s)-p(x) makes each regular arch integral an explicit polynomial after integration to d_-=t or d_+=1-t. The error of the two regular integrals is bounded by 2i(i+1)ae, ae=ce/62+cb/67. The two H terms contribute at most 2he.

The endpoint constants combine exactly: psi(1/4)-log pi+2H(0)=-gamma-log(2pi). Constants are enclosed with rational intervals: Machin pi, atanh-series log 2, and Euler--Maclaurin gamma at n=100 through order 12 with the next-term remainder. The two actual pole terms are M_-(p)exp(x/2)+M_+(p)exp(-x/2), with no extra factor 1/2. Taylor approximations of exponentials and their same-vector moments contribute at most 10ee, ee=2/(4^61 61!). Reflection gives M_-=(-1)^i M_+.

On the exterior panels the prime contribution is exactly -(log 2)/sqrt 2 times the appropriate shifted polynomial; on the middle panel it vanishes. Interval coefficients enclose log 2 shifts and all constants. The midpoint of each coefficient interval is rational. For t in [0,1], the sum of coefficient radii bounds its uniform arithmetic error. Multiplication by an outward bound for sqrt(2i+1) completes each epsilon_i. The endpoint logarithm is retained exactly rather than approximated.

## Consequence for the remaining Gram calculation

Let Pi be the physical projection onto degrees 0..63, r_i=(I-Pi)q_i and rtilde_i=(I-Pi)(v_i L+sqrt(2i+1)p_i). Since I-Pi is an L2 contraction, ||r-rtilde||<=eta. If M is a certified bound for ||rtilde||, then

||r* r-rtilde* rtilde|| <= eta(2M+eta).

This preserves all log/smooth mixed terms and the same trial vectors. The polynomial source remainder is now independently certified. Enclosure of rtilde* rtilde, its projection subtraction, and the exact prime endpoint integrals is still required. The existing floating pilot is not assigned this error bound automatically. High-degree monomial cancellation requires adequate precision or a better conditioned integration basis.

## Reproducible evidence and limits

`scripts/certify_native_smooth_source.py` uses standard-library rational arithmetic and outward interval rounding. `notes/data/RPB108_SMOOTH_SOURCE_CERTIFICATE_20261005.json` contains all three polynomial coefficient lists for all eight sources and exact errors. Repeated execution reproduces the certificate. An independent floating source check at t=1/10,2/5,3/5,9/10 agrees within 1.07e-14; that check verifies conventions but does not establish the theorem's error bound.

No full residual Gram or corrected eight-source sign is certified here. The other 56 low Schur coordinates remain outside this eight-source calculation. The full carrier contraction, global endpoint exclusion and signed endpoint-null Gaussian upper estimate remain independent open inputs. F4 and FULL TRANSPORT CLOSED remain open. Lean code and its previously recorded CI/axiom checkpoint are unchanged.
