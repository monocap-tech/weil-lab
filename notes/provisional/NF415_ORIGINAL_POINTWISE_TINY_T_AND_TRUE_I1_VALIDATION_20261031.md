# NF415 — Pointwise original I0 near-zero closure; validated original source I1 experiment

**2026-10-31 PT. Same original NF370 u4; canonical W-ODD-NEG OPEN; no source family expansion.**

## Previous cursor

NF413 original full 242-selected + 4-critical source-correlated second-derivative physical Gram established ||u4''||L2(-B,B)<256 and the omitted t<10^-10 I0 contribution in whole *L2* <4.8e-19. NF414 certified exact source-radii-paid finite regularized original arch multiplier and all seven true signed continuous prime translations at original hotspot points x=7/20 (cell 3), 9/10 (cell 6), 26/25 (cell 7), but neither actual remaining I0 nor I1 at even one point. Their known finite values are not z.

## New rigorous pointwise truncation inequality

For x in (0,B), B=11/10, let a=t/2 and t1=2(B-x). For 0<t<min(h,t1), the full x±t/2 source translates lie within [-B,B]. The original physical symmetric second difference has exact triangular integral identity

D_t u4(x) = u4(x)-[u4(x+a)+u4(x-a)]/2
          = -1/2 int_(-a)^a (a-|s|) u4''(x+s)ds.

By Cauchy-Schwarz on the ORIGINAL physical support,

|D_t u4(x)| <= (1/2) [int_(-a)^a (a-|s|)^2 ds]^(1/2)||u4''||L2(-B,B)
             = t^(3/2)/(4 sqrt3) ||u4''||L2(-B,B).

For original exact K(t)=exp(-t/4)/(1-exp(-t))<2/t on 0<t<=h<=1/2, integrate:

|int_0^min(h,t1) K(t) D_t u4(x)dt|
 <= ||u4''||2 h^(3/2)/(3 sqrt3)
 < 256/(3 sqrt3) h^(3/2) < 50 h^(3/2),

where final rational strict inequality follows from 256²<3*(3*50)², i.e. 65536<67500.

For h=10^-12, this is a **pointwise** original I0 omission bound <5e-17, genuinely stronger in type than NF413's L2 norm bound. It is valid for all positive physical original x (with moving t1 endpoint) without assuming a uniform source curvature or a fictitious global C1 seam on z. It is NOT a bound for the entire I0 or I1 integral.

## Actual original I1 attempt

Original NF408 I1 at x=9/10 (cell 6) has EXACT rational physical t integration limits [2/5,4] and integral:

I1(x) = 1/2 int_(2/5)^4 K(t) [u4(x)-u4(x-t/2)]dt.

A new script reconstructs all 242 selected + four critical original physical source coefficients as exact dyadic rational consolidated polynomials/trigonometric terms and odd sinh pole, then performs **validated complex Arb analytic integration** through python-flint 0.8.0 acb.integral, not a manually weighted Gauss pilot. The source coefficient-radius charge for this I1 term is <5 S0: original source sup error is ≤S0 at each x/t physical source translate and ∫_(2/5)^4 K(t)dt<2 ln 10<5. Native integrator must return a FINITE rigorous enclosure and an acceptable interval width before the full I1 can be promoted.

The precision and evaluation limits of the first focused script are diagnostic; if analytic error evaluation fails due to the unresolved high-order cancellation of enormous coefficients on complex interval boxes, the result must be typed METHOD STOP, not a numeric certificate. There is no claim here of having completed I0, entire z, signed cross, cellwide enclosures, or original NF404 threshold.

**Next:** inspect actual focused native I1 status and if accepted verify full source radius and enclosure width; else use source-correlated Taylor/analytic quadrature that maintains cancellation on validation boxes. Then complete I0 at hotspot rational interiors 6,3,7, one-sided full cell models, all eight and NF404 scalar.

New script: scripts/local_replay/nf415_original_cell6_I1_validated_acb.py.
Focused CI: .github/workflows/nf415-original-cell6-acb-integral.yml.
CI receipt after run: notes/data/provisional/NF415_original_cell6_I1_validated_acb.json.

**Still OPEN** original I0/I1 remainder, exact full z points/cells, signed p-z cross, complete original centered norm and NF404 C, original J242 lowband, domain, infinite inverse, W-ODD-NEG, even/whole Weil, RH. No new signed cells, historical overwrite, main merge, or RH promotion.
