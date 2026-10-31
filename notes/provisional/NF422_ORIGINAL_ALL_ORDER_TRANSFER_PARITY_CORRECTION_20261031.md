# NF422 — Original physical all-order arch transfer, NF421 parity correction, and certified coverage cost

**2026-10-31 PT; canonical W-ODD-NEG OPEN.** This pass reuses exactly the NF370 supported fourth u4, NF407 original full 242 selected + four critical source (32 critical sines plus odd pole), B=11/10, original seven signed prime-power translations, and NF404 dyadic centered pole. This note is a **mathematical source/proof reconciliation**, not another finite Gauss refinement or a new source.

## Previous → current → next

**NF421 accepted, subject to explicit correction here:** The full original 4096-bit fourth-derivative source Gram and complete original second x-jet at x=9/10 were independently source audited; true original z(x)>0 on [0.899994530369,0.900005469631], with a source-paid cubic remainder on the true physical macro interval [899/1000,901/1000]. The existing NF421 formula for z''' has one **wrong endpoint parity sign**, corrected below. Its *numerical global upper bound on the macro interval* remains valid, because the original proof charged the absolute endpoint contribution by the sum of both positive kernel bounds.

### Exact original source operator: the general moving-interface commutator

Let d=B-x, t1=2(B-x), t2=2(B+x), K(t)=exp(-t/4)/(1-exp(-t)), and

I0[g](x)=integral_0^t1 K(t){g(x)-[g(x+t/2)+g(x-t/2)]/2} dt,

I1[g](x)=integral_t1^t2 (K(t)/2){g(x)-g(x-t/2)} dt.

Define the original common finite arch multiplier A(x)=c(x)+log(B/d)/2, with **A'(x)=K(t1)-K(t2)**, and the linear physical response operator S[g](x)=A(x)g(x)+I0[g](x)+I1[g](x).

Differentiate both original moving support endpoints using t1'=-2 and t2'=+2. The shared internal translated source g(2x-B) cancels EXACTLY. The A' g(x) contribution cancels the remaining internal g(x) terms. For arbitrary sufficiently smooth g (no parity assumption needed yet),

**(d/dx) S[g](x)=S[g'](x)+K(t1)g(B)-K(t2)g(-B).**

The original supported full u4 is odd: every selected x^even*sin, x^odd*cos, all critical sines, and sinh(x/2) are odd on the actual physical support. Thus u4^(j)(-B)=(-1)^(j+1)u4^(j)(B). The original finite continuous arch is S[u4](x) - u4(B) log(B/d)/2.

Therefore for **every n>=1** on an original seam-free positive physical cell, with v_j=u4^(j)(B), K1^(m)=d^mK/dt^m(t1), K2^(m)=d^mK/dt^m(t2),

d^n/dx^n [ original finite arch + actual I0/I1 ]
=
S[u4^(n)](x)
+ sum_(j=0)^(n-1) v_j [ (-2)^(n-1-j) K1^(n-1-j)
                       + (-1)^j 2^(n-1-j) K2^(n-1-j)]
- (n-1)! v_0/(2 d^n).

**There are NO binomial coefficients** in this boundary sum: a new endpoint jet appears once at each differentiation level and is subsequently differentiated, while S[u4^(n)] transfers to the next derivative. It retains all genuine t1/t2 interfaces, not infinite-support/surrogate convolution.

To recover COMPLETE original z^(n), add the actual derivative P_reg^(n)(x) of the original seven signed prime terms on the same physical seam branch and derivative of original -a sinh(x/2) centered pole. The all-order arch identity alone does **not** eliminate prime seams or end-of-support singular behavior.

### Precise NF421 historical correction

The accepted NF421 prose and source-script comment represented the endpoint term in z''' as

u4''(B) [K(t1)-K(t2)]   (**INCORRECT**).

Because u4'' is ODD, the correct term is

**u4''(B) [K(t1)+K(t2)].**

The complete corrected original third derivative also has -2 u4'(B)[K'(t1)+K'(t2)], u4(B)[4K''(t1)+4K''(t2)-1/d^3], S[u4'''] and the genuine seven-prime and centered contributions. The NF421 signed local interval is not automatically invalidated by this analytical notation mistake: its prior quantitative third-derivative bound used the padded absolute endpoint cost **|K(t1)|+|K(t2)|<7**, valid for either sign on the genuine [899/1000,901/1000] interval, and the correct conservative total remains

|z'''| < 58*24580+7*16384+10 = **1540338**.

The NF422 script checks the formal source-parity correction and the exact independent moving-boundary atom balance through all derivative orders 1–12; historical NF421 artifacts are **not silently overwritten**. The correction is explicitly annotated on the predecessor draft PR and here.

### Rigorous quantitative cell-coverage gate

On original positive cell 6, NF406 exactly brackets the true physical endpoints -B+log7, -B+log8; the cell length is STRICTLY greater than 1/8. But NF421's |z'''|<1540338 is certified ONLY on [899/1000,901/1000], whose width is **1/500**, not across the complete cell 6.

At the true NF421 Taylor anchor x0=9/10, the cubic remainder bound at the edge of this original certified macro interval is

1540338*(1/1000)^3/6 = **0.000256723**.

The actual source z(9/10) is ~4.202e-11. Thus an unrefined **single-center cubic bound does not come close to NF404 decision-quality on the whole macro interval**. Extrapolating this |z'''| bound to the other original physical cell-6 locations is NOT permitted.

A mathematically sufficient *conditional* transfer recipe **inside the certified macro interval only** is to subdivide it into 10,000 equal Taylor panels, each with halfwidth r=1/10^7, and independently certify the complete original z, z', and z'' interval at the center of **EACH panel**. The uniform cubic remainder alone then contributes a rigorous macro L² error less than

1540338*r^3/(6*20) = 1540338/(120*10^21)
≈ **1.283615×10^-17**,

because sqrt(1/500)<1/20. This is less than the prior NF409 tentative 9e-17 L² entry budget. The 10,000 **additional center jets are NOT YET certified**, and that error budget would also need allocation to the center-jet interval widths. Accordingly, this is a **feasible finite panel error design, NOT a computed cellwise scalar or completed local enclosure**. In contrast, NF418's unrefined first-derivative global grid would have needed >5e19 subintervals over three cells. Neither cost is a lower bound against better source-correlated x-Taylor/Chebyshev compression.

### Disposition

**ACCEPTED if focused exact-source CI passes:** universal source-valid moving-boundary transfer formula (including correct source parity), historical NF421 exact-sign correction with numerical bound preservation, and finite conditional 10,000-panel error architecture over the original macro cell6 interval.

**STILL OPEN:** certifying the 10,000 center jets or a compressed analytic x-Taylor basis; actual full source-correlated cellwise z on the complete original cell6 and hotspots 3/7, other five positive physical cells; prime one-sided seam evaluation and endpoint dlogd; original NF410 signed p-z and z²; NF404 complete centered original scalar against C≈1.095e-21; fourth J242 complement, domain/infinite inverse, W-ODD-NEG, even/whole Weil, RH.

**NEXT NF423:** Construct a high-order original `S[u^(n)]` source-analytic jet evaluator or an interval Chebyshev model using the exact all-order transfer so each x-panel carries the *complete* original source correlation. Prefer reusing the 246-consolidated original source coefficient structure and evaluating multiple jet coefficients together; avoid separate costly 38+360 t integrations for every one of 10,000 panel centers. Certify original x-panel interpolation errors before signed NF410 integration. No new source, merge, historical rewrite or theorem promotion.
