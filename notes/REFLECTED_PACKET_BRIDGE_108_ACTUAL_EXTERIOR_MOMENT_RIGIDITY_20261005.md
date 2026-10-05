# RPB108: actual exterior moment rigidity and its stability obstruction

Base: research 73e900c04f549fe139341b4b29fe78cd351ffbb5.

## Theorem

For the actual frozen native residual of a physical L2 vector h supported in [-a,a], its restriction to any open interval in (3a,infinity) uniquely determines h.

For L>3a and sigma>1/2, the weighted tail map
\[
W_{L,\sigma}h=e^{-\sigma x}q_h(x),\quad x>L,
\]
is bounded, compact and injective from L2([-a,a]) to L2((L,infinity)). It is also compact and injective on the logarithmic carrier D_a, and on the canonically equivalent actual positive carrier.

There is no positive lower bound for W on any of those infinite-dimensional carriers. On any fixed finite-dimensional endpoint kernel, however, it is bounded below and r independent exterior point observations suffice when the kernel has dimension r.

This is actual prime/pole/archimedean rigidity, absent from the preceding comparison model. It does not prove an endpoint kernel vanishes, since its interior null equation does not force this exterior tail to vanish.

## Terminology before use

**Exterior moment generating function:** H_h(z) below, whose coefficients are actual Laplace moments of the unchanged h.

**Weighted tail observation:** the actual residual restricted to x>L and weighted by exp(-sigma x), not a multiplicity-copy coordinate.

**Exterior moment rigidity:** uniqueness of h from vanishing of its actual far residual on an open interval.

These observations use the same physical h throughout. No raw synthesis preimage or physical spectral-domain membership is assumed.

## Exact native tail, including the pole cancellation

The previously derived actual off-support residual is
\[
q_h(x)=M_-(h)e^{x/2}+M_+(h)e^{-x/2}
-\int_{-a}^a\frac{e^{-|x-y|/2}}{1-e^{-2|x-y|}}h(y)\,dy
-\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
\bigl(h(x-\log n)+h(x+\log n)\bigr).
\tag{1}
\]
Here M_s(h)=integral exp(sy)h(y)dy and M_-=M_(-1/2), M_+=M_(1/2). The prime cutoff is the actual right-limit cutoff at the frozen window a.

For x>3a, every prime translate in (1) is zero: log n<=2a implies x-log n>a, while x+log n>a. Also x-y>0, and the geometric archimedean expansion converges absolutely:
\[
\int\frac{e^{-(x-y)/2}}{1-e^{-2(x-y)}}h(y)\,dy
=\sum_{n\ge0}e^{-(2n+1/2)x}M_{2n+1/2}(h).
\]
The n=0 term is exactly M_+ exp(-x/2), cancelling that pole term. Therefore
\[
q_h(x)=e^{x/2}M_-(h)
-\sum_{n\ge1}e^{-(2n+1/2)x}M_{2n+1/2}(h)
=e^{x/2}M_-(h)-e^{-5x/2}H_h(e^{-2x}),
\tag{2}
\]
where
\[
H_h(z)=\int_{-a}^a
\frac{e^{5y/2}h(y)}{1-ze^{2y}}\,dy,
\qquad |z|<e^{-2a}.
\tag{3}
\]
Supported L2 implies L1. On compact subdisks the geometric series is uniformly dominated, so H_h is holomorphic and its coefficients are M_(2j+5/2), j>=0.

This cancellation uses the exact native normalization. It is not an adjustable representation field.

## Injectivity from any open exterior interval

Equation (2) makes q_h real analytic on (3a,infinity). If it vanishes on any nonempty open interval there, analytic uniqueness makes it zero on the whole right tail. Multiplying (2) by exp(-x/2) and sending x to infinity gives M_-=0.

It follows that H_h(e^(-2x))=0 for every x>3a. Holomorphic uniqueness gives H_h=0, hence
\[
\int_{-a}^a e^{5y/2}h(y)(e^{2y})^j\,dy=0
\quad(j=0,1,2,\ldots).
\tag{4}
\]
The change of variable u=e^(2y) is a homeomorphism of the compact support interval onto [e^(-2a),e^(2a)]. Polynomials in u approximate every continuous function of y uniformly. Multiplication by the continuous nowhere-zero factor exp(5y/2) is invertible. Equation (4) therefore makes h pair to zero with every continuous test on [-a,a], and hence h=0 in L2.

This argument works for complex h and uses no zero-simplicity or background-positivity assumption.

In particular a nonzero actual endpoint-null vector cannot have a compactly supported residual, or a residual vanishing on an open far interval. The endpoint-null equation only vanishes on the old interior; that is consistent with a nonzero analytic exterior tail.

## Compact weighted observation

Separate (2) into the rank-one growing pole term and the remainder integral
\[
-\int_{-a}^a
\frac{e^{-5(x-y)/2}}{1-e^{-2(x-y)}}h(y)\,dy.
\tag{5}
\]
For x>L>3a,
\[
1-e^{-2(x-y)}\ge d_L:=1-e^{-2(L-a)}>0.
\]
After the weight exp(-sigma x), the integral kernel in (5) is bounded in absolute value by
\[
d_L^{-1}e^{5a/2}e^{-(\sigma+5/2)x}.
\]
It is square integrable on (L,infinity) times [-a,a], so the remainder operator is Hilbert-Schmidt. The weighted growing pole is a bounded rank-one map because sigma>1/2. Thus W is compact.

For example, with c_-=||exp(-y/2)||_(L2[-a,a]),
\[
\|W_{L,\sigma}\|\le
\frac{c_-e^{-(\sigma-1/2)L}}{\sqrt{2\sigma-1}}
+\frac{\sqrt{2a}e^{5a/2}e^{-(\sigma+5/2)L}}
{d_L\sqrt{2\sigma+5}}.
\tag{6}
\]
For fixed a and sigma the right side tends to zero as L tends to infinity.

If Wh=0 in L2, continuity of the analytic tail makes q_h zero there pointwise. The preceding uniqueness proof gives h=0. Hence W is injective.

Its restriction to D_a is compact because D_a -> physical L2 is bounded. Transport through the actual bounded positive-carrier isomorphism preserves compactness and injectivity; it does not invent a raw divisor-copy preimage.

## Rigidity is not a uniform observability bound

A compact map on an infinite-dimensional Hilbert space cannot be bounded below. For an orthonormal sequence, weak convergence to zero and compactness force the image norms to tend to zero. Thus neither
\[
\|h\|_2\le C\|Wh\|_2
\quad\text{nor}\quad
\|h\|_{\log}\le C\|Wh\|_2
\]
holds on the respective full carrier.

On a fixed finite-dimensional kernel K_a, injectivity and compactness of its unit sphere give a positive lower bound, provided K_a is nonzero. Exterior point evaluations are bounded physical L2 functionals by (2)-(5). Their restrictions to K_a separate every nonzero vector. Their linear span therefore equals K_a^*, so r distinct exterior points can be chosen with an invertible r-by-r observation matrix in any chosen open far interval.

These are independent spatial observations, not identical equal-ordinate multiplicity copies. Their finite-dimensional condition bound depends on the kernel and observation interval. Equation (6) also shows that the weighted tail lower bound cannot remain uniform as the observation threshold L moves to infinity.

## What this contributes to the remaining attack

There is genuine exact native rigidity: the exterior residual encodes all the Laplace moments in (4), and vanishing there forces the physical vector to be zero.

But the tail map is compact, so injectivity does not furnish stable full-carrier recovery. It also does not give the signed endpoint-to-Gaussian upper estimate. A nonzero endpoint mode has a nonzero tail, while the genuine moving-Gaussian pairing may involve cancellations across the full exterior and boundary collars; no upper bound on that pairing follows from tail injectivity.

Thus an argument that truncates the actual residual to a finite collar, assumes its far tail zero, or obtains a global inverse merely from its moment uniqueness would add independent content. The missing stable estimate or signed cancellation still needs proof.

No endpoint existence or RH conclusion is asserted. This theorem does not restore same-vector enlarged weak-null transport and does not transfer automatically to selected-background forms.

## Validation and cursor

Analytic proof from the previously derived exact actual off-support kernel and pole normalization, with geometric series, polynomial moment density and Hilbert-Schmidt estimates. No new external input, Lean source/workflow change or CI claim. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 73e900c, the actual exact prime/pole/archimedean residual supplies exterior moment rigidity. For h supported in [-a,a] and x>3a, all frozen native prime translates vanish; the n=0 archimedean term cancels the decaying pole term exactly. Thus q_h(x)=e^(x/2)M_-(h)-e^(-5x/2)H_h(e^(-2x)), where H_h(z)=integral e^(5y/2)h(y)/(1-z e^(2y))dy is holomorphic for |z|<e^(-2a). Vanishing on any open right exterior interval forces M_-=0 and all moments M_(2n+1/2)=0 for n>=1; density of polynomials in e^(2y) gives h=0. The weighted tail observation W_(L,sigma):h->e^(-sigma x)q_h on x>L, L>3a,sigma>1/2, is bounded, compact and injective on physical L2 and compact on D_a. It has no uniform inverse on the infinite-dimensional physical or positive carrier, though any fixed finite endpoint kernel has stable observation and r independent exterior point observations. Its operator norm tends to zero as L grows. Thus exact actual exterior rigidity exists but does not supply stable global recovery or endpoint-null Gaussian upper cancellation. Nonzero endpoint modes, if any, have nonvanishing tails; the interior null equation does not force tail vanishing. No raw-copy observations, retained membership, assumed physical operator domain, actual endpoint/RH conclusion or new Lean/CI result; FULL TRANSPORT CLOSED remains open.
