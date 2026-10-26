# Same normalized SI29 energy Schur: logarithmic split

Parent custody is PR #330, fd077f602b7e5762e85660e66fcc8d69e7a3b210, successful run 40391210597, artifact 12684320650. The workflow verifies the exact accepted run/source/archive/JSON before replay. W-ODD-NEG and inherited original domain review remain open.

For the actual full-J normalized residual W=(I-P_J470)FC, the accepted witness provides ||Wy||^2 <= (101/100)||y||^2 and a whole zero-extension variation ceiling V(Wy)^2<=V2||y||^2. V2 is recomputed exactly from the retained endpoint vector and derivative Gram using 8||W(B)||^2+4B tr(W'*W'). At cutoff 1 the previous certificate bounded Astar energy by 36*(101/100)+V2 and rounded to 2^33.

Retain the logarithmic original Ao multiplier majorant instead. For R=2^k>=1, the entire low-frequency symbol is <=L=max(36,17+log R). Above R, integration by parts gives |hat w(xi)|<=V(w)/(2*pi*|xi|), and the two tails satisfy

    integral_(|xi|>R) a_o(xi)|hat w(xi)|^2
       <= V(w)^2 (18+log R)/(18R),

using 2*pi>6 and integral_R^infinity (17+log xi)/xi^2=(18+log R)/R. Low and high frequency regions are disjoint; Parseval bounds the low mass by the entire physical norm. Therefore the actual energy-projected Schur, minimized over the full original J470 family, obeys

    T_A(FC) <= [(101/100) max(36,17+log R)
                + V2(18+log R)/(18R)] I.

Astar<=Ao makes this an upper bound including the original pole correction. It makes no claim about Astar-Kminus. The inherited whole-original multiplier/domain assumptions remain explicit.

The strict rational inequality exp(7/10)>1+7/10+(7/10)^2/2+(7/10)^3/6>2 proves log 2<7/10. The checker evaluates k=0..80 using exact Fractions and chooses k=34. The resulting rational bound is below 64. Combined with the accepted same-coordinate lower 3328479/10^11, this gives condition number <=6400000000000/3328479 <1.93e6. The power-of-two upper improves by 2^27. No continuum optimization or global optimality is claimed.

This is a sharper complete energy Loewner upper on the SAME normalized 14-dimensional full-J quotient. It changes neither features nor coordinates. It performs no frequency integration, physical solve or new strong-action calculation. Large source-coefficient cancellation still requires certified high precision. Actual Astar projection/entries, matched forcing and the response value remain open, as do W-ODD-NEG, independent analytic/domain review, even/CC27/Weil/RH. Draft/unmerged status and CI acceptance are separate.
