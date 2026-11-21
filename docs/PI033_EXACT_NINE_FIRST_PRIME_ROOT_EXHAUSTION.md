# PI033 — Exactly nine live transversal first-prime crossings: complete sign-atlas exhaustion

**Weil-Lab / Potential Interface — controlled research reopening, ANALYTIC + EXACT INTEGER-INTERVAL.** Parent: \`research/pi032-explicit-nine-transversal-prime-gamma-crossings\`. Original true signed Weil source (PI027): pole − original von Mangoldt prime + compensated Gamma, unchanged IV011 Git blob \`14d8f01ce34f764900eccc68399d7323b4f4a25c\`; PI registry #792. The present result is a *classical* proof with exact-integer interval subcertificates. **No Lean kernel theorem, CI run, PR, trace identity, global Weil positivity or RH** is claimed. NF original HD/A frontier stays 692/968.

## 1. Statement (a strict strengthening of PI031–PI032)

For the **same** explicitly fixed, real nonnegative \(C_c^\infty\) bump
\[
d=\log(10/9),\qquad
\ell=d/100,\quad\Delta=d/2,\quad x_0=d/5,\quad u=3/2,\quad m=1,
\]
\[
g(y)=\begin{cases}e^{-1/[y(1-y)]},&0<y<1,\\0,&\mathrm{otherwise},\end{cases}
\quad b_\ell(x)=g(x/\ell),\quad
\rho=b_\ell(\cdot-x_0)+\frac32 b_\ell(\cdot-x_0-\Delta),
\quad \phi=D(D^2-\tfrac14)\rho,
\]
define PI027's genuine autocorrelation tests \(h_{\beta,a}\), original signed Weil form \(W\), and relative-phase coefficient \(\Theta(a)=B(a)-P(a)\).

**PI033 theorem (classical, source-preserving):**
\[
\boxed{\#\{a\in(\log3-d,\log3):\Theta(a)=0\}=9.}
\]
Every one of the **exactly nine** roots is *simple/transversal*:
\[
\boxed{\Theta'(a_*)\ne0,\qquad B(a_*)=P(a_*)>0.}
\]
Each makes the full original signed Weil value independent of all unit relative phases:
\(W(h_{\beta,a_*})=W(C)\) and \(W(D_{a_*})=0\). The theorem counts **only this specified first-prime window and test family**, not arbitrary smooth tests, all separations, all original support classes, or the full spectral zero divisor.

## 2. Three normalized correlation channels and source signs

Define \(E(y)=g'''(y)-(\ell^2/4)g'(y)\) and the even compact correlation
\[
\mathcal I(\tau)=\int_\mathbb R E(y)E(y-\tau)\,dy.
\]
It vanishes for \(|\tau|\ge1\). Write \(Q(\ell\tau)=\ell^{-5}\mathcal I(\tau)\) and \(t=\log3-a\in[0,d]\). The exact PI027/PI031 correlation is
\[
\boxed{C(t)=\tfrac{13}{4}Q(t)+\tfrac32 Q(t-\Delta)+\tfrac32 Q(t+\Delta),}
\]
and the translated positive first-prime window contains **only** the genuine \(n=3\) sample:
\[
P(a)=\kappa_3 C(\log3-a),\quad\kappa_3=\log3/\sqrt3>1/3.
\]
On \(0\le t\le d\), only the **central** channel \(t=\ell\tau\) (\(0\le\tau\le1\)) and the **two symmetric satellite** channels \(t=\Delta\pm\ell\tau\) (\(0\le\tau\le1\)) may contribute. Their supports are disjoint because \(\Delta>2\ell\). Outside them \(P=0\) and \(\Theta=B>0\).

Use the previously strict source Gamma bound \(0<B(a)<J/450\) and PI032's exact-enclosed \(J\ell^5=(13/4)\mathcal I(0)<(13/4)21\):
\[
\boxed{0<\ell^5B(a)<\tfrac{13}{4}\tfrac{21}{450}<1/5.}
\]
This is enough to determine the **full signed phase** from the following unambiguous exact conditions on any normalized channel:
\[
\boxed{\mathcal I(\tau)>2/5\ \Rightarrow\ \Theta<0,\qquad
\mathcal I(\tau)<0\ \Rightarrow\ \Theta>0.}
\]
Indeed the weakest live coefficient is the satellite \(\kappa_3(3/2)>1/2\), so \(\ell^5P> (1/2)(2/5)=1/5>\ell^5 B\) on a positive interval. For negative \(\mathcal I\), \(P<0<B\).

Thus **a complete sign atlas** for \(\mathcal I\) outside the PI032 three strict root brackets can certify *no further first-prime roots*, rather than relying on an unproved numerical root scan.

## 3. Four exact adaptive intervals with no roots

PI032 established \(\mathcal I(0)<21\) and \(\int_0^1|E'|^2<9000\) by outward integer bounds, so the convolution Cauchy–Schwarz estimate yields
\[
\boxed{|\mathcal I'(\tau)|\le
\sqrt{\mathcal I(0)\int_0^1|E'|^2}
<\sqrt{21\cdot9000}<435.}
\]
A new standalone script, \`scripts/pi033_exact_nine_exhaustive.py\`, imports the **unchanged actual PI032** function \`eval_integral(tau,N,'I')\`, which provides signed \(10^{40}\)-scale outward-rounded integers containing the true smooth integral value at rational \(\tau\).

For each rational cell \([c-h,c+h]\), if the trusted integer interval is \([L,U]\), the entire smooth integral satisfies
\[
\boxed{\mathcal I([c-h,c+h])\subset[L-435h,U+435h].}
\]
All cell endpoints, rational derivative cushions and final sign comparisons use \`fractions.Fraction\`. Every adaptive bisection is fail-closed at depth 20. Each shard checks exact continuity of its leaf partition and verifies the strict inequality for **every** leaf, with no floating-point sign acceptance.

The local independently reimplemented fixed-point pilot completed the following four exact sign atlas regions:

| Normalized \(\tau\) interval | Exact certified inequality on **entire** interval | Adaptive leaves | Each midpoint integration |
|:--|:--|--:|--:|
| \([0,101/1000]\) | \(\mathcal I>2/5\) | 6 | 2048 cells |
| \([121/1000,477/1000]\) | \(\mathcal I<0\) | 31 | 512 cells |
| \([498/1000,690/1000]\) | \(\mathcal I>2/5\) | 22 | 512 cells |
| \([706/1000,41/50]\) | \(\mathcal I<0\) | 17 | 512 cells |

All four independent local subscripts **PASS** in exact integer/rational arithmetic. Their four intervals cover the complement of three short derivative-controlled bands in \([0,41/50]\). The exact inherited PI032 subcertificates have not been independently reproduced *inside Lean*. The new GitHub-file copy was source-read and should be rerun in the pinned working tree before any independent acceptance promotion.

## 4. Three overlapping strict monotonicity bands

PI032 provided exactly these **strict** derivative samples:
\[
\mathcal I'(111/1000)<-90,\quad
\mathcal I'(484/1000)>65,\quad
\mathcal I'(698/1000)<-75,\quad
\sup|\mathcal I''|<9000.
\]
One additional exact interval calculation for PI033 certifies
\[
\boxed{\mathcal I'(491/1000)>69.}
\]
The \(9000\)-Lipschitz derivative estimate then proves:

| Protected band | Derivative sign and evidence | Root content |
|:--|:--|:--|
| \([101/1000,121/1000]\) | \(\mathcal I'<-90+9000(10/1000)=0\), strictly | Exactly the one root in PI032 bracket \((106/1000,115/1000)\) |
| \([477/1000,491/1000]\) | \(\mathcal I'>65-9000(7/1000)>0\) | First half of unique middle root |
| \([491/1000,498/1000]\) | \(\mathcal I'>69-9000(7/1000)>0\) | Overlapping continuation of the middle band |
| \([690/1000,706/1000]\) | \(\mathcal I'<-75+9000(8/1000)<0\) | Exactly the one root in PI032 bracket \((692/1000,704/1000)\) |

The whole middle band \([477/1000,498/1000]\) has \(\mathcal I'>0\) and exactly its PI032 root \((477/1000,490/1000)\). The boundaries *meet* the four sign atlas regions without gaps. The strict inequality at the first band's endpoints is valid because the original sample is **strictly** \(<-90\), even though \(90=9000(10/1000)\).

For the original phase coefficient \(\Theta=B-P\), PI032 separately proved \(\ell^6|B'|<1/1000\), while the prime term's derivative dominates throughout the original nine PI032 brackets. Thus each of those roots remains **simple as a zero of the full original phase**, not merely of the correlation.

## 5. Analytic sign exclusion for the outer smooth support tails

Only \([41/50,1]\) remains. A direct algebraic simplification **eliminates all numerical integration** there.

For \(0<y<1\) put \(v=y(1-y)\), \(c=1-2y\), \(\delta=\ell^2/4\in(0,1/3240000)\), \(g=e^{-1/v}\). The *exact* differential identity is
\[
\boxed{E(y)=\frac{g(y)c}{v^6}\,p_\delta(v),\qquad
p_\delta(v)=1-10v+24v^2-12v^3-\delta v^4.}
\]
For \(0<y\le9/50\) one has \(0<v\le369/2500\). Here
\[
p_\delta'(v)=-10+48v-36v^2-4\delta v^3
\le-10+48(369/2500)<0,
\]
whereas the exact rational endpoint lower bound satisfies
\[
\boxed{1-10v_0+24v_0^2-12v_0^3-\frac{v_0^4}{3240000}>0,
\quad v_0=369/2500.}
\]
So \(E(y)>0\) for \(0<y\le9/50\). The symmetric flat bump has \(E(1-y)=-E(y)\), hence \(E(y)<0\) for \(41/50\le y<1\).

For \(41/50\le\tau<1\), every \(y\in(\tau,1)\) satisfies \(E(y)<0\) and \(E(y-\tau)>0\), so
\[
\boxed{\mathcal I(\tau)=\int_\tau^1E(y)E(y-\tau)dy<0.}
\]
At \(\tau=1\), the correlation is exactly zero and the Gamma phase is strictly positive. Thus **the entire last tail is root-free**, proven analytically without a quadrature cutoff. The exact rational endpoint polynomial positivity is checked in the PI033 bridge subcertificate.

## 6. Exhaustive count and exact source/spectral boundary

The normalized range \([0,1]\) has now been exhausted without gaps:

1. Four disjoint certified-sign regions exclude additional roots.
2. Three protected monotonicity bands contain exactly one root each, by strict PI032 endpoint signs and derivative bounds.
3. The remaining outer tail \([41/50,1]\) has strictly negative correlation.
4. The two symmetric satellite sectors inherit this exact **three-root** count because \(\mathcal I\) is even, while the original \(B(a)>0\) prevents roots outside the active correlation channels.
5. PI032 guarantees the *full original phase derivative* is nonzero on its nine disjoint brackets.

Therefore **exactly \(3+3+3=9\)** source-exact live \(n=3\) cancellations occur in the specified first-prime window, all simple.

This conclusion is genuinely stronger than PI032's \(\ge9\); it does **not** assert a universal bound over arbitrary bumps (PI029 shows there is none), any new global positivity theorem, or a spectral zero trace identity.

At each root, the PI027 source normalization comparison remains *conditional*: \(W(D)=0\) exactly, printed Ch12 would require \(Z_{12}(D)=0\), printed uncorrected Ch13 would require \(Z_{13,\rm cap}(D)=2B>0\) **only if those distinct trace claims were independently established with a common correct Haar/test/cutoff dictionary**. They have not been. Off-critical complex transformed arguments must be retained in any CP comparison.

## 7. Custody, status and PI034 handoff

New files: **this memo and one exact regression script**, no Lean module, workflow, PR, or Actions dispatch. PI032's original kernel candidate and exact integer verifier remain byte-for-byte inherited. The four sign coverage shards and bridge were run in an independent equivalent local interval implementation and passed; this is **a reproducible exact arithmetic certificate, not a Lean kernel-accepted result**. Independent re-execution of the exact committed PI032+PI033 source pair and manual review of its interval arithmetic remain sensible acceptance gates.

A controlled PR against \`main\` requires re-auditing the entire stacked research diff and all source-scoped workflow triggers; PI033's doc/script by themselves match no inherited PR workflow dependencies. Preserve accepted NF numerical certificates, source identities and strict source-bound \`#print axioms\` requirements. The accepted original HD/A numerical frontier remains **692/968**, regardless of PI033's mathematical result.

**Next — PI034:** develop a small, **source-bound formal Lean certificate architecture** for the interval sign atlas and root-count theorem. Prioritize independent replay of the exact PI032/PI033 integer scripts, verified interval-enclosure API lemmas, a finite partition completeness theorem, the polynomial positive-tail lemma, and explicit source-identified original n=3 prime/Gamma normalization. Stage only minimal compiler proof obligations under an isolated/manual gate after independently checking CI fan-out; do not claim spectral equivalence or RH.
