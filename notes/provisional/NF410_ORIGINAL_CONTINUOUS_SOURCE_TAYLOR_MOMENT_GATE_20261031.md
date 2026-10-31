# NF410 — Original signed continuous-response Taylor gate, with exact principal polynomial moments

**2026-10-31 PT. Original W-ODD-NEG OPEN. RH OPEN.**
Research branch \`research/nf410-original-cell-taylor-moments\`, stacked on NF409 PR #402. Unchanged NF370 fourth \`u4\`, NF407 242+4 coefficient native source, original 7 prime-power terms, NF404 exact dyadic pole, B=11/10. No new signed cells/source family, no merge or theorem promotion.

## Previous / current / next

**Previous NF409.** Source-exact original p=q+r sign and 8 cell zero-degree integrals accepted; original continuous z source expression exactly reduced but not rigorously integrated. Provisional 2/4-node true-source pilots straddle C=1.0950537731184213...e-21. NF409 hotspot cells 6,3,7 carry >80% of absolute resolution-change variation; this ranking is NOT a rigorous error bound.

**Current NF410 mathematical advance.** Explicit exact-polynomial signed principal moments M_(i,k)=∫_(cell i)(x-c_i)^k p(x) dx, k=0,1,2,3, in source-rational interval arithmetic, with all original 7 jumps retained and true physical endpoint log. New pure Fraction source-level replay proves k=0 overlap with prior independently written NF409 cell integral and global half integral. This supplies a correlation-preserving polynomial energy functional and removes the need to perform numerical x-quadrature on p, including signed z*p terms, once an original-z Taylor enclosure has been independently proved.

**Not yet achieved.** No source-validated Taylor coefficients/remainders for continuous original z(x), no certified full original positive scalar upper/lower, hence NF404 gate undecided. A new CI workflow exists for the exact p polynomial moments; do not call it accepted until an actual successful run and durable output are verified.

## A. The moment identity and correlation-preserving norm computation

For x>=0 write original p(x)=q(x)+r(x), with
q(x)=v/2 log(B/(B-x)), v=u4(B)<0;
r(x)=v sum_n c_n 1_(x>x_n),
n∈{2,3,4,5,7,8,9}, c_n=Lambda(n)/sqrt(n)>0, x_n=|B-log n|.

Fix any source seam cell [a_i,b_i] and rational c_i. Set A=B-c_i and
H_j(y)=y^(j+1)/(j+1)*(log(B/y)+1/(j+1)) for 0<y<=B, H_j(0)=0.
Since H'_j(y)=y^j log(B/y)>=0 on [0,B], source-rational seam uncertainty is rigorously enclosed by endpoint evaluation; no numerical singular log quadrature.

Then, for k≥0,
  M_(i,k)^q =
    (v/2) sum_(j=0)^k (-1)^j binom(k,j) A^(k-j)
      * [H_j(B-a_i)-H_j(B-b_i)].

The step contribution from each original n is
  M_(i,k)^(r_n) =
    (v*c_n)/(k+1)*
      [(b_i-c_i)^(k+1)-
       (min(b_i,max(a_i,x_n))-c_i)^(k+1)].

Both formulas are exact elementary identities. In particular k=0 reproduces NF409's signed-cell primitive independently; it is not a newly invented source coefficient. Endpoint x=B is handled via H_j(0)=0, not an ill-defined log.

Let T_i(x)=sum_(k=0)^d a_(i,k)(x-c_i)^k with exact rational a_(i,k) (representing an independently checked approximation to the WHOLE original continuous z). Define T by odd reflection. Then

 E_T := ||p+T||²
     = E_p + 2 sum_i ∫_(a_i)^(b_i) T_i(x)^2 dx
             +4 sum_i sum_k a_(i,k) M_(i,k).

E_p=||q+r||² already comes from the original NF407 accepted exact receipt. Polynomial self-products integrate with exact rational primitives. This computes *all signed correlations before forming the energy*; it is not the sum of independent |q|, |r| and |z| upper bounds. Moment and E_p intervals are genuine outward enclosures, and polynomial candidate coefficients remain exact rationals until a separate original-z certificate attaches.

## B. What is required for a rigorous numerical decision

An independently verified source-native original continuous response encloser must prove for EVERY x in every original physical positive cell
   |z(x)-T_i(x)| <= delta_i
with outward interval arithmetic, and separately account for the accepted NF408 native coefficient action radius <1e-745. For eps²=2 sum_i (b_i-a_i)delta_i² (using upper seam widths) and an exact rational R with E_T.upper<=R², the complete original power satisfies the VALIDATED interval

 max(0,E_T.lower -2 R eps-eps²) <= ||p+z||²
                      <= E_T.upper+2 R eps+eps².

Compare this ENTIRE interval with the exact NF404 cap C. An upper <=C accepts that particular sufficient centered scalar; a lower >C proves that sufficient gate fails for this fixed original fourth source (not that W-ODD-NEG or RH fails). If intervals overlap C, return UNDECIDED. No number of unverified Gauss nodes makes this result rigorous.

NF409's conditional example R=3.32e-11, eps=9e-17 charges 5.9760081e-27 (<gamma²/8). For a rigorous decision also require the verified candidate E_T upper to be <=R²; R and eps are not pre-accepted bounds.

## C. Source-specific regularity: no Taylor polynomial may cross a genuine seam

Write x_n=|B-h|, h=log n. The continuous original prime remainder P_n-r_n is C^0 across x_n but has an explicit possible first-derivative jump (from smooth u4 one-sided endpoint derivative):

- For n=2,3 with h<B, (P_n-r_n)'(x_n+) - (P_n-r_n)'(x_n-) = +c_n u4'(B).
- For n=4,5,7,8,9 with h>B, the jump is -c_n u4'(-B)=-c_n u4'(B), since original u4 is odd.

Thus a Taylor model spanning two different physical cells without a seam-jump correction would be invalid even after subtracting the known step r. For original hotspot cell 3, x runs from log4−B to B−log2; cell 6 from log7−B to log8−B; cell 7 from log8−B to log9−B. Each cell must be enclosed independently with interval source side conditions.

For last cell 8 ending at B, NF408 analytically cancels the divergent endpoint log but only proves bounded/continuous z; it does NOT establish bounded high x derivatives at x=B. Any Taylor-remainder argument using a global max |z^(d+1)| on the closed last cell requires an additional endpoint-regularity proof. Use endpoint-sensitive intervals or a log-enriched local model rather than silently assuming smoothness.

## D. Non-negotiable independent Bessel check

For original pole sheared g=w-a*s, with s∈J242, orthogonal projection gives exact original
  E_true=||g||² >= ||P_J g||² >= E_sel,lower,
where NF404 source-exact selected lower E_sel,lower≈1.0950024763105536e-21. The NF404 sufficient cap is C=E_sel,lower+gamma², gamma²≈5.12968078676143e-26.

The original NF408 2-node E2≈1.0055614488866898e-21 is ~8.9441027423864e-23 BELOW the known rigorous selected lower, so E2 is definitely not the true power. This is a PROVED consistency failure for that provisional numerical value, not an interval error estimate for all cell values. E4≈1.1088870373875423e-21 exceeds the cap by ~1.3833264269121e-23, but it also remains uncertified. Future original full norm intervals must intersect [E_sel,lower,infinity); a claimed entire rigorous interval below E_sel,lower signals a broken evaluation or a source mismatch.

## E. Source/custody standing

- ACCEPTED previously: NF404 selected lower / pole shear / exact C and gamma², NF407 original principal E_p, NF408 source-native action radius, NF409 original exact k=0 signed source moments.
- NEW NF410: exact formula and executable original-source Fraction polynomial moment producer, degree 0..3. Its CI results must be read, not inferred from code presence.
- OPEN: rigorously evaluated ORIGINAL continuous z Taylor coefficients and remainder on 6/3/7 and the other five cells; actual complete centered scalar interval; original fourth lowband J242-perp upper; complete signed infinite odd operator and domain; W-ODD-NEG and RH.

**Next NF411 or continued NF410:** derive and EXECUTE source-native outward interval/Taylor evaluation of z on cells 6/3/7 including nested t integrations, integer-lattice error control and all seven translated prime supports. Never substitute an unverified full Gauss mesh. Reject a result if its certified full-energy interval falls below the NF404 selected lower. No closure promotion before the full original inequality is decided.
