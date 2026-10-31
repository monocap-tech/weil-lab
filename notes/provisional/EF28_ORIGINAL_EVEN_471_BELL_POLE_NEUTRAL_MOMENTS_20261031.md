# EF28 — Source-adaptive even pole-neutral finite moment kernel, avoiding universal FIR

**2026-10-31. Canonical W-EVEN-FORM OPEN.** Parent EF27 [draft PR #414](https://github.com/monocap-tech/weil-lab/pull/414) restricted physical positive-pole Schur A−M²/E+Δ. Its first focused Actions #41229142104 failed because it attempted to convert the exact integer 10^372 into Python float for printing; mathematical source quantities printed before that point. EF27 code fixed this harmless reporting overflow on parent branch; revised CI requires an explicit receipt, not an inferred success. Parent EF26 expanded signed source and tiny R>10^-193 passed [Actions #41227759868](https://github.com/monocap-tech/weil-lab/actions/runs/41227759868) under independent analytic source/digamma attachment conditions.

## 1. Return to the source itself, not another 469-fold universal FIR

Actual original protected SI10 even source family: 107 positive rational frequencies c_j, positive Taylor orders p_j summing exactly to **469 real-even source constraints**. The even source functions on the physical symmetric aperture I=[−11/10,11/10] are

u_{jk}(x)=x^k cos(2π c_j x) for k even,
u_{jk}(x)=x^k sin(2π c_j x) for k odd,
with 0≤k<p_j.

Their orthogonal real-even complement is the exact native F469. The ORIGINAL positive even-pole vector is c(x)=cosh(x/2), not a surrogate.

Define **471 explicitly fixed real-even compact C5 test functions** (l=0,...,470):

x_l=(l+1)/512, r=1/8192,
b_r(t)=cos^6(πt/(2r)) for |t|<r, zero otherwise,
φ_l(x)=½[b_r(x−x_l)+b_r(x+x_l)].

All 942 bell supports are disjoint: nearest positive center spacing 1/512>2r, opposite sign pair separation ≥2/512>2r, and 471/512+r<B. Every φ_l is in the strong logarithmic original Fourier-multiplier domain; any real finite linear combination is physically compact even C5. This does not require a universal 938-root annihilator.

Construct the ACTUAL, exact finite real moment matrix Htilde∈R^(470×471):
- 469 rows H_{(j,k),l}=∫_I u_{jk}(x)φ_l(x)dx;
- one *separate* pole row h_{pole,l}=cosh(x_l/2), since <cosh(x/2),φ_l>=J_r(1/2) cosh(x_l/2) with common nonzero positive bell Laplace J_r.

These are explicit original values, not independent free random entries. They admit exact evaluation by derivatives of the closed cosine-six Fourier kernel:

F_l(ω)=H_r(ω/(2π))cos(ω x_l),
∫φ_l(x)x^k e^{iωx}dx=i^(−k)∂_ω^k F_l(ω),

with real-even parity selecting cos for even k, sin for odd k. No source reassignment or "Taylor approximation to V" is introduced.

Since 470 homogeneous real constraints act on 471 real columns, **dim ker Htilde≥1 regardless of matrix rank**. There exists a NONZERO true original real-even compact cofinite f=Σ a_lφ_l satisfying *all 469 native exceptional source orthogonalities AND* the exact genuine positive-pole orthogonality <c,f>=0. This is an actual elementary existence theorem for the original source data; it is NOT yet an explicit interval coefficient vector or a mixed source sign.

## 2. Exact physical normalization without gigantic FIR coefficients

Disjoint translates and native cosine-six beta integrals give **for every coefficient vector a**, exactly

||f||²=d Σ_l a_l², d=231r/1024=231/8388608,
||f'||²/||f||²=(9/11)π²/r² (when f≠0).

Thus the physical basis is orthogonal with identical L2 norms; its physical Gram condition number is **exactly 1**, independent of 469 exponentials. This does NOT imply the native 470×471 original moment matrix is numerically well-conditioned; its smallest nonzero singular value and the mixed residual still need interval verification. Do not confuse these different matrices.

The original EF25 digamma envelope −8<a_arch(ξ)<8+ln(1+|ξ|), Parseval and Jensen yield for any f in this physical span

q_arch(f,f) < [8+ln2+ln(1+9/(44r²))]||f||² <26||f||²,

because X=1+9/(44r²)=150994955/11 and the exact rational 41-term exp(17) sum exceeds X. The original full seven-prime signed multiplier is **retained**, with magnitude ≤TWOC<8, so

**q0(f,f)<34||f||²** for every f in the 471-bell span, rather than incorrectly claiming prime self-energy zero.

On the cofinite kernel of the first 469 exact native rows, the original inherited SI10 bound supplies **q0(f,f)≥μ||f||²**, μ=17/25000, under its stated analytic form/core closure conditions. Therefore the original true complement energy for any such nonzero f lies in [μ d||a||², 34d||a||²). Its positive even-pole self energy is EXACTLY zero on the further kernel of the pole row.

## 3. Reduction of inverse-Schur and positivity to one finite ORIGINAL residual

Let e(x)=1_I cos(2π(37/64)x) be the actual first SI10 even source, and set the finite signed source gradient g_l=q0(e,φ_l) using the COMPLETE original seven-prime/digamma form. Define the true Euclidean residual

δ = dist(g,range Htildeᵀ) = ||P_{ker Htilde}g||_2.

This definition is unambiguous even if Htilde lacks full row rank; the projector is the orthogonal Euclidean projector. If δ>0, choose the exact source-adapted coefficient vector a=Pker g, so f=Σ a_lφ_l is nonzero, exactly SI10 cofinite and pole neutral. Then

M=q0(e,f)=g·a=δ²,
||f||²=dδ²,
E=q0(f,f)<34dδ²,

and hence the TRUE original one-source/cofinite inverse correction satisfies

**R_original(e)≥|M|²/E>δ²/(34d).**

Moreover since <c,f>=0, the positive pole contributes ONLY to the first source diagonal under minimization over this f:

min_t q_even(e+t f) = A+2u²−M²/E,
A=q0(e,e), u=<c,e>.

A genuine NEGATIVE original even Weil-form direction would be proved if the finite source-specific residual and first source diagonal meet the strict criterion

**δ²>34d(A+2u²).**

If δ=0 on this particular 471-bell space, the test is inconclusive; this does NOT mean the full original mixed form vanishes. If δ>0 but the strict inequality fails, we obtain nonzero coupling but not a negative even direction. This is a sufficient negativity/witness criterion, not necessary for PSD and not sufficient for whole Weil/RH.

EF28 does NOT evaluate actual Htilde, g, δ, A, any singular values, or the full 469D corrected Schur. An independent exact rational 3×4 toy matrix checks the projection identities and all factors in the variational quotient, but is never used as an original source certificate.

## 4. Stopping point and next admissible move

The EF27 scalar Schur bounds on the universal FIR detector are too wide to establish a sign despite the original mixed sign and R>10^-193. EF28 **retypes the remaining problem as a finite, pole-neutral original moment residual with exact physical norm and a 34 upper energy**, removing the universal 469-factor spectral scaling from the entry. The source-moment system may still be very ill-conditioned; EF28 does not claim otherwise or generate 220,000 unverifiable 340-digit coefficients.

**EF29 acceptance:** independently compute source-conditioned interval enclosures for the original 470×471 Htilde entries (or certify a compressed exact equivalent), and the corresponding complete signed g vector. Report numerical rank/conditioning and outward lower δ (not merely a floating Gram inverse); separately compute original source A so the strict original corrected negativity criterion can actually be evaluated. If no robust residual remains, document a finite-grid METHOD STOP, or vary this physical test family without opening an unbounded new route. Full original 469D Schur and even/odd/whole Weil/RH remain OPEN.

All research additive GitHub-first custody. No main merge.

**EF28 original source verification receipt — 2026-10-31:** [Actions #41231565079](https://github.com/monocap-tech/weil-lab/actions/runs/41231565079), job `124626681315`, **SUCCESS**. Native source 107 clusters, 469 source-even real rows plus one genuine positive pole row, 471 rational bell centers/942 physically disjoint C5 lobes, exact real physical Gram `dI` with `d=231/8388608`, source Fourier second-moment and exp17 Jensen, all seven original prime power norm retained, and exact `q0(f,f)<34||f||²` finite proof conditions PASS. Independent Fraction projection toy and canonical obligation/governance PASS. This regression does not materialize or enclose the actual original 470×471 moment coefficients nor signed source g, residual δ, first-source diagonal A, original domain proof or full corrected Schur. Those remain OPEN. The regular rational center lattice may also induce frequency aliasing or singular-value weakness; physical Gram condition 1 alone does not establish source moment-system conditioning. This is EF29's verification gate.
