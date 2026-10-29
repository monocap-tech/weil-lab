# NF380 — quantitative population guarantee for original annular out-of-fit candidates

**Date:** 2026-10-28 Pacific. **Type:** rigorous exact Hilbert-space/rational preflight for external sign-box witness selection; **NOT** a native indexed annulus certificate, signed lowband observation, source import, NF375 method stop, or W-ODD-NEG closure. Historical source and selected carrier unchanged. Remains within draft PR #361.

## Previous / current / next

**Previous NF379:** fixed original u4 lowband response is nonzero outside J242+E4, by analytic continuation and an NF376 certified nonzero signed Fourier knot. This is qualitative. The original NF377 4096-bit annular selector and exact fullband threshold workflows remained QUEUED during this pass, with no accepted index; the container lacked python-flint 0.8.0 so native replay was not possible. GitHub Actions has a large unrelated PR-check backlog (about 993 queued at inspection); do not promote queued checks or add a 492-integral campaign.

**Current:** strengthen the 492-annulus Bessel guarantee into a rigorous **population lower bound**: at least ten existing candidate annuli clear the current strict >49% physical-outfit fraction. This makes the exact/native selector acceptance robust, not a one-off edge-equality event.

**Next:** resolve GitHub Actions native run or independently obtain the same 4096-bit outward Gram certificate for one identified annulus. Then evaluate ONE original signed continuum pairing, compare to NF375 lowband h4=1.5e-13 or the separately highband-paid full-frequency threshold beta+h4≈3.3122287474e-13; stop the original sufficient method only on an accepted outward obstruction.

## Exact survivor-count theorem

Let B=11/10, n=492, h=B/n=11/4920. Let delta_i be the n mutually orthogonal normalized odd annuli, each ||delta_i||²=h. Let S=J242+span(E4), of rank d<=246, and let

r_i = ||(I-P_S)delta_i||² / h in [0,1].

The Hilbert-Schmidt/Bessel projection trace bound yields sum_i r_i >= n-d >=246.

For any rational t in (0,1), if k candidates satisfy r_i>t, then

sum_i r_i <= k+(n-k)t.

For t=49/100, k<=9 would imply sum<=9+483*(49/100)=24567/100=245.67 <246, contradiction. Therefore at least **TEN distinct** original rational annuli satisfy

r_i>49/100,

or equivalently ||(I-P_S)delta_i||² > (49/100)*(11/4920)=539/492000.

For t=1/3, k<=122 would yield sum<=122+370/3=736/3<246; therefore at least **123 distinct** original annuli satisfy r_i>1/3. The ten-candidate result is the one relevant to the native 49% acceptance condition. The theorem DOES NOT identify indices or prove that any corresponding signed response is nonzero.

The above is exact mathematics with no dependence on RH, on a numerical Gram inverse, or on Mittermeier's finite positivity margin. `scripts/local_replay/nf380_annulus_survivor_preflight.py` replays all rational thresholds with stdlib Fraction.

## Time-bandwidth scale: diagnostic only

The physical full interval has length 2B=2.2 and the NF375 Fourier cutoff is ±Lambda with Lambda=2^20. The classical time-frequency area (2B)*(2Lambda)=4B Lambda = 23068672/5 ≈4,613,734.4. Dividing by the 492 annulus dimensions gives 5767168/615≈9,377.51. This is **not** an exact rank assertion, a universal sampling lower bound for our fixed source, or a theorem that the projected u4 contains millions of independent modes; bandlimited functions on a finite interval still form an infinite-dimensional restriction space. It is diagnostic support for why 492 unregularized cell averages cannot replace the missing direction-resolved residual upper. Exact NF378 finite-rank noninjectivity and the derivative-paid NF377 Poincare upper govern any rigorous claim.

## Acceptance and two gates

- **PASS analytic and local exact rational:** at least ten admissible 49%-outfit indices exist; at least 123 clear one-third. Preflight code arithmetic executed locally.
- **NOT PASSED:** a named original annulus with outward original physical Gram; actual signed annular dual integral; original lowband full residual, fitted E4 payment, quantitative derivative budget, full original exterior inverse.
- **External method PROMOTION:** requires an independently replayable original signed pairing or strong bound that actually changes a current NF375/376 accept/STOP, not merely better candidate counting.
- **Original theorem CLOSURE:** complete W-ODD-NEG O1/O2 with source/cross/infinite/domain; even/whole/RH separate OPEN.

**Operational stop:** do not launch further duplicate native workflows while the existing annulus and exact-threshold runs are queued. Repo custody here is additive and non-load-bearing; no changes to research/obligations.json or imported theorem pins. 
