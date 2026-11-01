# EF40 — Two genuinely protected SI10 even source rows, signed original physical response

2026-10-31. Canonical active W-EVEN-FORM OPEN, odd W-ODD-NEG paused/OPEN, whole Weil and RH OPEN. Parent EF39 [draft PR #447](https://github.com/monocap-tech/weil-lab/pull/447), original focused final-head [Actions #41262941734](https://github.com/monocap-tech/weil-lab/actions/runs/41262941734) SUCCESS.

## Original source identity and improvement over EF39

The actual first SI10 even protected Fourier cluster has center c0=37/64 and original real-even Taylor order p0 at least TWO (certified by the genuine original SI10 107-cluster/469-order inventory). The physical support I=[-11/10,11/10] yields two genuine distinct protected even source rows:

e(x)=cos(omega*x), v(x)=x sin(omega*x), omega=2*pi*(37/64), x in I.

The actual k=1 real-even Fourier jet is -x sin(omega*x), so replacing v by -v does not alter their protected span. This is NOT an arbitrary extra probe added to the protected source space: both rows belong to the unchanged original 469-dimensional SI10 span V469. Their physical L2 Gram is well-conditioned: G_ee=||e||² about 1.2363494; G_ev=<e,v> about +0.0395; G_vv=||v||² about 0.2896. The exact Schur q=G_vv-G_ev²/G_ee is certified STRICTLY >1/4 by the source-native directed interval validator. The two-row matrix is therefore positive definite without float-SVD or conjectural conditioning.

Retain EF39's actual fully signed original physical first-source response H40=z+h40, where z includes EVERY original prime/power n=2,3,4,5,7,8,9 translated cutoff, true signed weights (ln p)/sqrt n, and the true positive cosh pole. h40 includes all 40 original quarter-digamma physical cutoff half-integer modes with the genuine signed complete 40×40 Gram. EF39's original native 340-digit source L2 interval certified

 D1=||H40||² - <H40,e>²/||e||² ≈0.06232001255 <1/15.

EF40 now computes the two new ORIGINAL signed pairings

 b_v = <H40,v>=<z,v>+<h40,v>,

with full physical translation support and signed arch terms, not a surrogate Fourier window. On the exact original eight positive-half arithmetic cutoff cells, each prime/pole piece is P cos(omega x)+Q sin(omega x)+k cosh(x/2), so multiplication by x sin(omega x) has elementary exact antiderivatives. The true full 40-mode arch pairing uses stable e^[-lambda(B-x)], e^[-lambda(B+x)] endpoint primitives; nothing in the original cutoff is dropped.

The exact L2 source Gram entries are

 <e,v>= -B cos(2 omega B)/(2 omega)+sin(2 omega B)/(4 omega²),

 ||v||²=B³/3-B² sin(2 omega B)/(2 omega)-B cos(2 omega B)/(2 omega²)+sin(2 omega B)/(4 omega³).

Let G_vv|e =||v||² - <e,v>²/||e||² >1/4 and b_v|e =<H40,v>-(<H40,e>/||e||²)<e,v>. Then **exact original source-space Schur transitivity** (for physical L2) gives

 D2 = D1 - b_v|e² / G_vv|e.

The acceptance inequality is strictly D2<29/500=0.058, expected around 0.05708 from the noncertifying pilot. This is a genuine source-projection acceptance only after the exact native source validator passes; a pilot cannot establish it.

## Complete original infinite arch tail and energy dual scope

The original quarter-digamma cutoff h_tail with modes m>=40 remains fully bounded by the EF39 certified

 ||h_tail||<57/500+1/10000.

Since span{e,v} is a genuine TWO-dimensional subspace of the original SI10 protected V469, the complete original even physical cofinite projection P_F kills both e and v and contracts residuals. From D2<29/500< (241/1000)^2, the entire original first-source gradient after the protected arch constant row obeys

 ||P_F g_e|| < 241/1000+57/500+1/10000 < 9/25=0.36.

The inherited original signed even SI10 cofinite floor mu>17/25000 gives a true full first-source energy-dual response bound, including the EF34 unseen residual

 **eta < (9/25)^2 / (17/25000)=3240/17 ≈190.588.**

EF39's upper was eta<28125/136≈206.801; EF40 reduces that upper by roughly 7.8%. It is a **real additional original source-projection step**, not a proof that the full 469-source projector has been computed.

The actual q-even inverse-energy response, original remaining 467 protected source rows and their cross-couplings, and the entire 469x469 signed exceptional Schur remain UNCOMPUTED. The new upper remains far above EF33 restricted first-source/kernel Schur lower S2>1/500, so the original first-source full-cofinite signed scalar Schur is still undecided. Independent original Fourier/logarithmic digamma, physical-domain and form-core audit remains OPEN.

## EF41 entry and custody

EF41 should check whether a small, source-valid set of higher first-cluster protected even jets (x²cos, x³sin, etc.) produces a decisive projection improvement with the original signed 40-mode physical response and entire arch tail fully paid. The stable two-row Gram establishes a concrete path; it does NOT imply global conditioning of all original 469 modes. Avoid global unverified numerical inverse or whole form positivity promotion.

Native validator: scripts/validate_rpb108_ef40_original_even_two_row_jet_projection.py. Workflow: .github/workflows/ef40-original-even-two-rows.yml. Exact source validation and final-head CI must pass separately from independent analytic source identity/physical form audit. No main merge.
