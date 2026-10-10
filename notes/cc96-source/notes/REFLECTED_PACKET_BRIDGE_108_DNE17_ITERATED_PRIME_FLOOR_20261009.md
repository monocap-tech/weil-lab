# RPB108 DNE17 — Iterated prime weight raises the infinite high floor and closes both directional gates

Date: 2026-10-09 UTC (October 8 America/Los_Angeles). DNE parent b788896e08619c0b42c7404fefd63e7d4a24637a. [Definitions](../docs/TERMINOLOGY_RPB108_DNE17_ITERATED_PRIME_FLOOR.md).

## New original-arithmetic theorem

At a=53/50, let P be the complete selfadjoint clipped six-prime translation operator with its original positive coefficients, so its contribution to the Weil form is -<h,Ph>. DNE17 constructs the exact step weight w=P^2 1 and certifies every row of P w/w. The resulting full physical operator estimate is

    ||P|| <233/100=2.33.

This improves NF16's inherited allowance 2.565346230069. Together with the SAME original NF10 archimedean and signed-pole estimate on F112, the physical complement of the first112 Legendre modes, it proves

    Q(h,h) >[2.772351243732-2.33] ||h||_2^2
           =0.442351243732 ||h||_2^2,
    Q(h,h) >=(11/25)||h||_2^2       for every h in F112.

This is a new infinite-dimensional original high-form floor **0.44**, valid in both parities. It is not a finite high-mode Rayleigh trial. It requires no old-aperture gap, retained near-critical energy denominator, or sign premise at the entire 1.06 aperture.

## Both original near-critical directions now close

Keep the authenticated NF24 retained x in each parity, its exact two-high compensated p_star, measured finite energy S2=Q(p_star,p_star), and complete physical high source square P2 from DNE16. Since the measured-high source coordinates of p_star vanish, DNE16's U-projected source equals the whole F112 source. Original high square completion with the new floor gives

    S_Q(x)=inf_{y in F112} Q(x+y,x+y)
          >=S2(x)-P2(x)/0.44 >0.

| Paid complete-high result | Even NF24 target | Odd NF24 target |
|---|---:|---:|
| Complete source ratio P2/S2, approximate display | 0.35007481524 | 0.28028204450 |
| New sufficient ratio allowance | 0.44 | 0.44 |
| Full-high Schur lower, widened downward | 1.8916e-35 | 1.2004e-31 |
| Certified retained fraction of S2 | >0.20437 | >0.36299 |
| Complete infinite-high directional gate | **Passes** | **Passes** |

All interval source and exact-H2 transfer errors were already paid in the immutable DNE16 replay inputs. The new gate validator uses their exact rational decimal endpoints, not the approximate displays in this table.

DNE15 and DNE16 remain correct for their inherited floor 0.207. DNE16 showed that even the exact two-high correlation optimizer could not close those sufficient gates. DNE17 supplies additional original information: a stronger uniform high-form inequality. The coarse norm-only estimate now succeeds on both directions. No old result is edited and no hypothetical least-high completion is identified with the actual native form.

## Why a short iterated weight improves the prime estimate

For n in {2,3,4,5,7,8}, put c_n=Lambda(n)/sqrt(n) and extend all functions by zero outside I. Then

    (P f)(x)=sum_n c_n [f(x+log n)+f(x-log n)].

NF10 used a quadratic weight in a 6000-cell interval cover. The new weight follows the actual clipped translations: start with 1_I, apply P twice, and certify the next iterate. The power functions 1, P1, P^2 1 and P^3 1 have respectively 1,13,39 and81 constant bands on I. The weight is strictly positive everywhere except immaterial cut choices; its certified essential minimum is above 2.14749. The rigorously enclosed maximum Schur row is below 2.314596, leaving a strict margin below the chosen 2.33 allowance.

For any physical f, the elementary weighted product inequality and selfadjointness of the two-orientation translations give

    |<f,Pf>| <= integral_I |f(x)|^2 [(Pw)(x)/w(x)] dx
              <= max_row ||f||_2^2.

Thus ||P||<=max_row<2.33. This is an operator-norm theorem on ALL physical L2 functions, with no smoothness or finite Legendre assumption. The estimate is an absolute prime bound; it retains all six original coefficients and both orientations.

## Exact symbolic support cuts, not an unverified spatial grid

Every cut is stored as s*a+log(q), where s=+-1 and q is an exact positive Fraction. Translation by +-log(n) multiplies q by n or1/n. Identical cuts arising through log4=2log2 and log8=3log2 are merged by their exact rational keys. Support clipping against +-a is accepted only after rational logarithm intervals certify the comparison.

Floating values propose a cut order; each adjacent pair must then have strictly separated exact rational intervals. No floating order, midpoint lookup or sampled maximum enters the proof. The union of the weight and next-power cuts is checked, so a denominator discontinuity is never crossed inside a tested row. All 81 union bands receive a lower weight interval and upper next-power interval.

Coefficient logs use a positive arctanh series and its geometric remainder; square roots use integer square-root brackets. All value operations round outwards on a Fraction grid. Primary settings are 60 grid digits and220 log terms. The independent higher-order run uses80 digits and320 terms. Exact cut ordering, clipping, positive weight and every row inequality pass in both runs. The full per-band intervals are published.

## Independent word enumeration and archimedean replay

A separate validator expands all words of length2 and3 in the twelve signed prime steps. For a word with partial products q_j, its entire support is the intersection

    -a-log(q_j) <x<a-log(q_j)

over every prefix including the empty word. Its positive coefficient is the product of its original c_n values. There are82 surviving length-two and464 surviving length-three words. This independently reconstructs the weight and next-power values on every certified band, checks both producer enclosures against the word sums, and independently verifies the2.33 row bound. It does not reuse the producer's event-sweep recurrence.

The same validator freshly executes NF10's depth-six Bessel mass formulas at cutoffs14,15,16, checks the uniform rate above80, and replays the archimedean-minus-pole arithmetic above2.772351243732. The analytic depth-six Bessel inequality and original archimedean lower symbol remain explicitly inherited NF10 theorems. The original 6000-cell prime estimate is not needed for the new floor, and is not claimed as freshly replayed.

The copied NF10 source and certificate are authenticated at read-only Aperture head b7fa4461ab4cca2ebc9383ae4b9407c03a580826. DNE16's source/energy certificates are immutable inputs at parent b788896e08619c0b42c7404fefd63e7d4a24637a. No raw NF17/NF19 matrix archive is newly replayed.

## Controls, reproduction and remaining work

The exact validator passes **81,197 rational assertions**, including symbolic ordering guards, both source reconstructions, every Schur row, fresh arch/pole arithmetic and both full-high directional gates. Six abstract rational controls test the response inequality: three genuine crossings pass only at positive Schur sign, while three positive ground levels retain their actual whole-mass-shift null. These are algebraic controls, not original Weil crossings. Python compilation checks pass; no Lean or GitHub Actions execution is claimed.

Run the producer twice with default settings and then DNE17_GRID_DIGITS=80 DNE17_LOG_TERMS=320. It takes the output path as its sole argument. The standalone word/gate validator takes primary certificate, replay certificate, a directory containing DNE16's even_replay_certificate.json and odd_replay_certificate.json, and its output path. Place the copied helper dne17_nf10_complement_input.py alongside it. Published DNE16 source files can be copied under those two short filenames for replay.

The collective frontier is now sharper: certify the full retained source Gram or a rigorous bound on the remaining low-energy retained subspace against the new0.44 budget. The two actual near-critical directions and DNE14's constant line pass complete high elimination, but they do not span all56 retained directions in either parity. This turn does not prove whole-domain positivity at1.06, actual null exclusion, a cap-uniform defect-relative lower frame, RH/F4, full transport or Lean closure. All other branches receive no writes.
