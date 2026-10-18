# PS26 — Partition-independent obstruction to the pole-blind global Z-matrix, and the required even/odd rank-one repair

**W-PHYSICAL-SHIFT · October 17, 2026 · stacked on PS25.** Canonical **W-ODD-NEG**, **W-EVEN-FORM**, native **CC27 D-Riesz** domain/norm bridge, complete original Weil positivity and **RH** remain **OPEN**. This is a substantive negative result about a **proposed proof method**, not a negative direction of the original Weil form. It explains why scaling PS25's highly successful finite-scale **positive-even-pole-dropped** Z-matrix directly to a full physical partition cannot possibly establish global positivity, no matter how many cells are used. The original positive even pole must be retained in a coherent, parity-aware way.

## 1. Recover the actual original signed source, not a model surrogate

On \(I=[-B,B]\), \(B=11/10\), \(R=2B=11/5\), the unchanged zero-extended original signed physical Weil form is
\[
Q[f]=J[f]+c_{\rm arch}\|f\|_2^2
-2\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n)
+\underbrace{2|\langle f,c\rangle|^2}_{\text{POSITIVE EVEN POLE}}
-\underbrace{2|\langle f,s\rangle|^2}_{\text{NEGATIVE ODD POLE}},
\]
with \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\), \(c_{\rm arch}=-\gamma-\pi/2-3\log2-\log\pi\) and
\[
J[f]=\int_0^\infty\frac{e^{-u/2}}{1-e^{-2u}}\|Zf-\tau_u Zf\|_2^2\,du.
\]
The true signed prime shifts and arch kernel, form domains, and original source pins are exactly the same as PS01–PS25.

Let \(P\) be the thirteen-original-source-interval sharp projection from PS15, and \(C=1-P\). Each of those \(13\) intervals has width \(\delta=R-\log9\), and the exact original rational logarithm enclosure proves \(0<\delta<1/350\). The same proof shows the entire sharp source/complement split is **form-domain compatible**. PS16 proves the true original thirteen-source operator \(A_P>323/1000\).

The exact **genuine first Schur complement** on \(C\) is
\[
\mathfrak S_C[h]=Q_C[h]-\langle h,T_Ch\rangle
=\inf_{p\in\mathcal D_P}Q[p+h],
\qquad
T_C=B_{PC}^*A_P^{-1}B_{PC}\ge0.
\]

## 2. Pinned RC315 constant-mode certificate forces the even pole to be essential

The original normalized constant
\[
u_0(x)=R^{-1/2}\qquad(x\in I)
\]
is form-admissible. Its **ACTUAL original signed full Weil** RC315 source-pinned diagonal satisfies
\[
\boxed{0<Q[u_0]<0.040260.}
\]
It is important that this is the original physically normalized *even* low mode, not a synthetic kernel or a later approximation.

Because \(c(x)=\cosh(x/2)\ge1\) everywhere, the **actual positive even pole** obeys
\[
2|\langle c,u_0\rangle|^2
=\frac2R\left(\int_I\cosh(x/2)\,dx\right)^2
\ge2R=\frac{22}{5}=4.4.
\]
Define the *pole-dropped surrogate*, **not the original operator**,
\[
Q^\flat[f]:=Q[f]-2|\langle c,f\rangle|^2.
\]
Its genuine original constant-mode direction is therefore rigorously negative:
\[
\boxed{Q^\flat[u_0]<0.040260-4.4<-4.3.}
\]
This is **NOT a counterexample to Weil positivity**. The original positive pole is precisely the missing positive contribution, and its near-cancellation cannot be replaced by a generic mass lower estimate.

## 3. Stronger no-go *after* the actual source Schur elimination

Take the original sharp source-complement physical projection of the same constant,
\[
h_C=1_Cu_0.
\]
It remains in the original logarithmic form domain by PS15's sharp interval multiplier theorem. The actual source part \(p_0=1_Pu_0\) is also admissible, and \(p_0+h_C=u_0\). The exact source **variational** Schur identity gives the *UPPER* estimate
\[
\boxed{
\mathfrak S_C[h_C]=\inf_{p\in\mathcal D_P}Q[p+h_C]
\le Q[p_0+h_C]=Q[u_0]<0.040260.
}
\]
It does **not** assert that the original \(\mathfrak S_C[h_C]\) is positive or negative.

The original thirteen-source physical measure is \(13\delta<13/350\), so
\[
|C|=R-13\delta>R-\frac{13}{350}.
\]
On \(C\), write \(c_C=1_C c\). Since \(c\ge1\),
\[
\begin{aligned}
2|\langle c_C,h_C\rangle|^2
&=\frac2R\left(\int_Cc(x)\,dx\right)^2\\
&\ge\frac2R|C|^2
>\underbrace{\frac2R\left(R-\frac{13}{350}\right)^2}_{\text{EXACT RATIONAL LOWER}}
>\frac{17}{4}=4.25.
\end{aligned}
\]

Now delete the positive even pole **from the actual already-source-eliminated form**:
\[
\boxed{
\mathfrak B_C[h]
:=\mathfrak S_C[h]-2|\langle c_C,h\rangle|^2.
}
\]
The pinned original constant test proves the **TRUE explicit negative surrogate direction**
\[
\boxed{
\mathfrak B_C[h_C]
<0.040260-4.25<-4.2.
}
\]
Again, \(\mathfrak B_C\) is **not** the original signed Weil form or its exact Schur. It is the deliberate *positive-even-pole-discarded* lower form underpinning the local PS25 Z-majorant.

## 4. UNIVERSAL full-covering obstruction for PS25's current scalar proof architecture

Let \(\{C_j\}\) be **any** finite or suitably convergent countable form-stable physical partition of the **entire source complement \(C\)**. Suppose a symmetric scalar block Z-majorant \(M\) of the same pole-dropped kind as PS25 is claimed to bound the original sign on *every* admissible vector:
\[
t(h)^\top M\,t(h)\le\mathfrak B_C[h],
\qquad
t_j(h)=\|1_{C_j}h\|_2.
\]
This includes arbitrarily fine mesh refinements, optimal choices of physically sized channels, full original seven-prime link checks, sharper Carleman bounds, exact source-energy Schur response and any proposed positive weighted-diagonal-dominance vector.

Evaluate the inequality on the **already source-pinned admissible \(h_C\)**. The negative surrogate certificate forces
\[
\boxed{
t(h_C)^\top M\,t(h_C)
\le \mathfrak B_C[h_C]<-4.2.
}
\]
Therefore **such a globally valid M cannot be positive semidefinite**, regardless of mesh resolution, and no positive weighted diagonal-dominance certificate can exist for it.

This does **not** contradict PS25's local 12-channel \(M>1/4\): those twelve windows occupy less than five percent of the original physical interval, and \(h_C\) is **not supported on that local module**. The no-go applies precisely to extending the same **even-pole-discarding** architecture to the **full** original complement.

### Quantitative information: over 99% even-pole retention is necessary

For a hypothetical *pole-retaining surrogate* on the original whole domain
\[
Q^{(\theta)}=Q-(1-\theta)\,2|\langle c,f\rangle|^2,\quad0\le\theta\le1,
\]
the original constant-mode test shows that **if \(Q^{(\theta)}\ge0\)**, then
\[
\theta>1-\frac{0.040260}{4.4}>0.9908.
\]
After the source elimination, define instead
\[
\mathfrak S_C^{(\theta)}
=\mathfrak S_C-(1-\theta)2|\langle c_C,h\rangle|^2.
\]
The original sharp restricted constant test shows that **if \(\mathfrak S_C^{(\theta)}\ge0\)**, then
\[
\boxed{\theta>0.9905.}
\]
These are **NECESSARY**, not sufficient fractions. The original positive even pole cannot be omitted, and retaining only a modest fraction cannot establish a nonnegative whole-domain surrogate.

## 5. Exact parity- and rank-one-aware repair obligation

The original support, source labels \(r\leftrightarrow9/r\), seven-prime Weil quadratic operator, arch kernel and both poles are invariant under reflection. Consequently the true source, true original signed Schur \(\mathfrak S_C\), and original physical form domain split into **even** and **odd** sectors.

The positive even pole \(2|\langle c_C,h\rangle|^2\) vanishes **identically in the odd sector**. The negative odd pole vanishes **identically in the even sector**. This prevents a sign-blind all-sector scalar Z-matrix from faithfully handling the near cancellation that the even low mode demonstrates.

Let
\[
\phi=\frac{c_C}{\|c_C\|_2},\qquad
K_{\rm even}=\{k\in\mathcal D_C:
k\text{ even},\ \langle c_C,k\rangle=0\}.
\]
The vector \(\phi\) belongs to the original form domain because \(c\) is smooth on \(I\) and sharp projection preserves the logarithmic domain. On even \(h=a\phi+k\),
\[
\boxed{
\mathfrak S_C[a\phi+k]
=\mathfrak B_C[a\phi+k]+2\|c_C\|_2^2|a|^2.
}
\]
This gives an **exact form-theoretic acceptance reduction**, without pretending to have a bounded, evaluated inverse on \(K_{\rm even}\):

1. **Odd:** establish \(\mathfrak S_C[h]\ge0\) for all admissible odd \(h\); this is the native W-ODD-NEG obstruction, with the actual signed odd pole retained.
2. **Even, pole-orthogonal:** establish \(\mathfrak B_C[k]\ge0\) for every \(k\in K_{\rm even}\). If whole true even positivity is possible, this is necessary because the positive even pole vanishes here.
3. **Even, one coherent scalar:** establish
   \[
   \boxed{
   \inf_{k\in K_{\rm even}}
   \Big(\mathfrak B_C[\phi+k]+2\|c_C\|_2^2\Big)\ge0.
   }
   \]
   Together with (2), this is necessary and sufficient for the **entire original true even-sector Schur form** to be nonnegative, by writing \(h=a(\phi+k/a)\) when \(a\neq0\) and treating \(a=0\) separately.

These conditions are an **exact structural reduction**, not a proof that any of them holds. The pinned negative \(\mathfrak B_C[h_C]\) demonstrates that the pole-blind even form already has at least one negative direction, which the true positive rank-one term must repair if whole even positivity is to hold. A rank-one positive correction cannot eliminate a negative subspace of dimension two or higher: any two-dimensional negative subspace intersects \(c_C^\perp\) nontrivially.

## 6. Next mathematical dependency

**PS27** should replace the impossible even-pole-blind global Z-assembly with a **parity-resolved, positive-rank-one-aware global carrier**. Prioritize an exact/coercive bound on \(K_{\rm even}=c_C^\perp\) and the odd sector, then compute the single coherent even variational gate. The original genuine seven-prime and arch interregion couplings and signed odd pole must be retained. A finite coverage algorithm that merely increases PS25's twelve-window Z-majorant while deleting the even pole is ruled out by PS26, irrespective of numerical precision.

**Original full complementary signed Schur positivity, CC27 D-Riesz norm/domain equivalence, W-ODD-NEG, W-EVEN-FORM, full Weil positivity and RH remain OPEN.**

Replay: \`python3 scripts/validate_rpb108_ps26_even_pole_global_no_go.py\` replays PS25→...→original RC315, checks original full RC315 low-mode intervals and source pins, 13-source physical measure, the actual full/schur positive pole lower bounds, explicit negative **surrogate** witnesses, necessary \(>99.08\%\) original/\(>99.05\%\) post-Schur pole retention fractions, exact parity source-label symmetry and fail-closed global no-RH-promotion custody. Passing source-rational CI is not independent formalization or mathematical peer review.
