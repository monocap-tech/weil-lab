# EF39 — Original signed arch–prime–pole interaction and one protected-row shorting

2026-10-31. Canonical W-EVEN-FORM OPEN. Parent EF38 draft PR #444, exact first-source/cutoff CI #41258523208 SUCCESS; EF38 genuine one-row original physical projection bound ||P_F g_e||<1 and cofinite energy dual eta<25000/17. The 469 original SI10 even source modes and exact first source e=1_I cos(2pi 37/64 x), seven true prime-power translations with w_n=(ln p)/sqrt n (n=2,3,4,5,7,8,9), genuine positive even cosh pole and entire original quarter-digamma symbol are unchanged.

## Genuine original finite arch cut and all physical signed correlations

The original protected first arch source row a_arch(37/64)e is removed EXACTLY. Let z be the full original 7-prime plus 2u cosh(x/2) physical response on I=[-11/10,11/10], as verified in EF37 and EF38; <z,e> and ||z||² have native original 340-digit outward intervals, and z on each of eight positive-half genuine cutoff cells is P cos(omega x)+Q sin(omega x)+k cosh(x/2).

Keep the signed first N=40 terms of the exact original arch physical Laplace cutoff:

 h_N(x) = sum_(m=0)^(N-1) a_m exp(-lambda_m B) cosh(lambda_m x),
 lambda_m=2m+1/2,
 a_m = 2 Re[e^(i omega B)/(lambda_m-i omega)].

No arch term is silently promoted to a source row. The full original signed response on the compact physical interval is z+h_N+h_tail.

EF39 checks three actual correlated quantities using the native EF24/EF26/EF29 outward interval arithmetic: (1) <z,h_N> with original eight cutoff cells and all seven signed prime channels plus genuine pole, (2) <h_N,e> with the true first protected cosine source, and (3) ||h_N||² as the COMPLETE signed 40x40 Gram, not a sum of separate norms. Stable endpoint antiderivatives avoid overflow at the physical boundary:

 For a lambda>0 define E_+(x)=exp[-lambda(B-x)], E_-(x)=exp[-lambda(B+x)]. Then the primitives of E_B cosh(lambda x) times cos(omega x), sin(omega x) are respectively [lambda(E_+-E_-)cos(omega x)+omega(E_++E_-)sin(omega x)]/[2(lambda²+omega²)] and [lambda(E_+-E_-)sin(omega x)-omega(E_++E_-)cos(omega x)]/[2(lambda²+omega²)]. The cosh(x/2) primitive comes from the two sinh((lambda+/-1/2)x)/(lambda+/-1/2) terms, using the continuous x limit at lambda=1/2.

The signed original complete 40x40 arch Gram is exact:

 G_ij=(1-E_i E_j)/[2(lambda_i+lambda_j)] + (E_j-E_i)/[2(lambda_i-lambda_j)] for i != j, where E_i=exp(-2 lambda_i B).
 For i=j: G_ii=(1-E_i²)/(4lambda_i)+B E_i.

Every contribution includes real signed a_i a_j; no diagonal-only or positive-only proxy.

The true original first-row projected squared response is

 D_N=||z||²+2<z,h_N>+||h_N||²-(<z,e>+<h_N,e>)²/||e||².

**Native entry/acceptance condition:** certify D_40<1/15 with a strict original outward interval. All finite cutoff integrals must be original, not approximated numerically without enclosure.

## Entire infinite half-integer tail paid

For every m>=40, the original arch coefficient and physical cosh norm admit the EF36/EF37 upper
 ||a_m e^-lambda_m B cosh(lambda_m x)|| <= lambda_m^-3/2 + 2 sqrt(B) exp(-lambda_m B)/lambda_m.
The complete algebraic tail is bounded by 1/sqrt(78.5)<57/500, and the native original positive exponential tail <1/10000. Thus ||h_tail|| <57/500+1/10000.

Because the original first source e belongs to V469 and the exact arch constant row was removed, the true original cofinite F subset span(e)^perp. The exact projection inequality is

 ||P_F g_e|| <= sqrt(D_40)+||h_tail||
 <259/1000+57/500+1/10000 <3/8.

The inherited original SI10 complete even cofinite lower mu>17/25000 therefore yields the new true first-source cofinite energy-dual response and EF34 unseen residual upper

 **eta < (3/8)^2/(17/25000) =28125/136 ≈206.8015.**

This is an original conditional analytic/source-custody improvement, provided the strict D_40 interval is verified by the focused native workflow and the original EF26/EF29 physical Fourier/digamma domain identities survive independent audit. The EF34 eta>0 relies on its separately stated jump/pseudolocality and form-core premises.

## Obligations not discharged

This pass is an exact original **one-row** protected source shorting. It does not invert the actual 469-dimensional protected source Gram, nor does it compute the original full inverse cofinite energy Riesz response. The EF33 first-source restricted Schur S2>1/500 remains much smaller than the present eta upper, hence neither sign of the entire original first-source cofinite Schur is decided. The original W-EVEN-FORM, W-ODD-NEG paused, W-WHOLE-FORM and RH remain OPEN. No main merge or historical artifact mutation.

EF40 should decide whether adding a *small, explicitly source-typed stable subset* of the other 468 original modes gives a useful gain over EF39, ideally with original jointly signed physical integrals, certified Gram determinants/conditioning and full infinite arch residual. If no such subset controls the remaining physical projection, identify a genuine conditioning/information STOP; do not claim a full 469D projection from a one-row bound.

Native source: scripts/validate_rpb108_ef39_original_even_full_arch_cross_first_row.py. Focused workflow: .github/workflows/ef39-original-even-signed-arch-cross.yml. Independent original Fourier/cutoff/core review remains distinct from rational CI.
