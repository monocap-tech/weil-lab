# RPB108: local positivity has an exact global localization defect

Date: 2026-10-06 (America/Los_Angeles). Live recovery e003124e6bcb086c5ffb2f11d6e55c26916dea49.
Definitions: [averaged native localization](../docs/TERMINOLOGY_RPB108_AVERAGED_NATIVE_LOCALIZATION.md).
Global/F4 lane. No aperture march or new sign certificate.

## A different lawful global route

Fix a certified window a=47/50 and its physical mass margin delta=3e-29. Choose a nonnegative real smooth chi supported in (-a,a), with L2 norm one. For any actual compact supported logarithmic h on any larger window, set h_z(x)=chi(x-z)h(x).

Every h_z is in the same logarithmic domain species and is supported in a translated certified window. Multiplication is lawful: the elementary submultiplicative logarithmic weight and weighted L1 decay of the Schwartz Fourier transform of chi bound multiplication on the log Hilbert domain. Translation invariance of the full native diagonal includes the opposite-slot pole moments; their exponential translation factors cancel. The local active prime cutoff agrees with the global one on h_z because larger shifts have zero correlation.

Therefore
\[
L_\chi(h):=\int_{\mathbb R}Q(h_z)\,dz
\ge\delta\int_{\mathbb R}\|h_z\|_2^2dz
=\delta\|h\|_2^2.
\tag{1}
\]
This is an actual use of the existing local certificate on every translated patch. It is not global positivity of Q(h).

## Exact full arithmetic defect

Let c(s)=integral chi(x+s)chi(x)dx. It satisfies c(0)=1, 0<=c<=1, c(s)=0 for |s|>=2a. The actual native dictionary, with every relevant prime power retained, is
\[
Q(h)=E_0(h)-2\sum_n b_n\Re I_{\ell_n}(h)
 +4\int_0^\infty\cosh(s/2)\Re I_s(h)\,ds.
\tag{2}
\]
The pole integral is exactly the original Hermitian cross-pole term, not two independent positive squares. For compact supported h, correlations vanish at large separations, so the active prime sum and pole integrals are finite.

The averaged correlation is
\[
\int_{\mathbb R} I_s(h_z)\,dz=c(s)I_s(h).
\tag{3}
\]
The mass term is unchanged. The recovered Euler/Laplace archimedean energy gives, by expansion of the translated squared difference,
\[
E_\chi(h):=L_\chi(h)-Q(h)
=E_{\rm arch}(h)+E_{\rm prime}(h)+E_{\rm pole}(h),
\tag{4}
\]
where
\[
\begin{aligned}
E_{\rm arch}(h)&=2\int_0^\infty k(s)(1-c(s))\Re I_s(h)\,ds,\\
E_{\rm prime}(h)&=2\sum_n b_n(1-c(\ell_n))\Re I_{\ell_n}(h),\\
E_{\rm pole}(h)&=-4\int_0^\infty\cosh(s/2)(1-c(s))\Re I_s(h)\,ds.
\end{aligned}
\tag{5}
\]
Fubini is lawful here. Near zero, 1-c(s)=||tau_s chi-chi||_2^2/2=O(s^2), while k(s)=O(1/s). At infinity k decays, and the compact source correlations truncate the prime and pole terms. The nonnegative archimedean energy integrals can first be truncated and then passed through Tonelli/monotone convergence.

A sufficient independent global theorem is
\[
\boxed{E_\chi(h)\le\delta\|h\|_2^2
\quad\text{for every actual compact supported logarithmic }h.}
\tag{6}
\]
Equations (1), (4) then give all-window Q>=0. The established contact dichotomy and strict-margin rigidity upgrade this to zero kernel and fixed-window coercivity everywhere. No endpoint witness, Gaussian upper sum or prescribed packet is needed for this implication.

**Equation (6) is unproved.** It is a sufficient cancellation target, not asserted necessary for global positivity. Even if Q>=0, L_chi(h) can exceed delta mass by much more, so (6) may be stronger than needed.

## Why the available margin cannot pay a termwise archimedean budget

The standalone archimedean defect has the sharp bound
\[
|E_{\rm arch}(h)|\le C_{\rm arch}(\chi)\|h\|_2^2,\qquad
C_{\rm arch}=2\int_0^\infty k(s)(1-c(s))ds.
\tag{7}
\]
Sharpness follows from h_L=1_[-L,L]/sqrt(2L): it is an actual logarithmic carrier vector, I_s(h_L)=(1-s/(2L))_+, and dominated convergence gives E_arch(h_L) -> C_arch with mass one.

Because c=0 beyond 2a and k(s)>=exp(-s/2),
\[
C_{\rm arch}\ge2\int_{2a}^\infty e^{-s/2}ds
=4e^{-a}>4/e>4/3\quad(a=47/50<1).
\tag{8}
\]
The currently supplied delta=3e-29 cannot absorb that standalone sharp upper cost. This compares the **available certified margin**, not an asserted upper bound for the unknown optimal local margin. No conclusion about the sign of Q(h_L) is made, because its prime and pole defects remain present.

A signed cancellation in (5) could still make (6) true. Merely optimizing the local Gram/complement constants does not supply that cancellation.

## Actual pole defect has unbounded positive values

Choose a nonnegative real mass-one interval bump f of width eta<2a, for example eta^(-1/2) times the indicator of [-eta/2,eta/2]. Put
\[
h_L=(\tau_L f-\tau_{-L}f)/\sqrt2,\qquad 2L-\eta>2a.
\]
The two supports are disjoint, h_L is real odd, and its physical mass is one. It is an actual supported logarithmic carrier vector. Its correlation for s>0 is I_s(f)-I_(s-2L)(f)/2. The cross-bump correlations have c(s)=0. Let A_f=M_-(f)M_+(f)>0. Directly from (5),
\[
E_{\rm pole}(h_L)=2\cosh(L)A_f
-4\int_0^\infty\cosh(s/2)(1-c(s))I_s(f)\,ds.
\tag{9}
\]
The last term is independent of L and between zero and 2A_f. Hence
\[
E_{\rm pole}(h_L)\ge2A_f(\cosh L-1)\longrightarrow+\infty.
\tag{10}
\]
This is an actual pole-defect control, not a null vector or a negative-energy claim. The prime defect can be negative on these same cross correlations and cancel the growth; ignoring it would be unlawful. It shows why an aperture-independent bound for each defect separately cannot establish (6).

The formula also explains the missing arithmetic scale: all prime shifts ell_n>=2a disappear from the averaged local energies but remain in E_prime, together with the long-separation pole defect. At the certified frontier only 2,3,4,5 occur locally; the larger-window prime correlations cannot be recovered by translating that same local certificate.

## Failed implication, remaining theorem and F4 scope

Failed implication: strict fixed-window positivity + translation invariance + smooth partition localization -> all-window positivity with no new global arithmetic estimate. The exact missing term is (5). The sharp archimedean budget and unbounded positive pole control reject the attempted termwise proof; they do not reject a lawful **combined signed** prime/pole/archimedean estimate.

The smallest stated sufficient theorem on this route is the combined defect upper bound (6), or another bound comparing E_chi to the actual averaged local energy closely enough to keep Q nonnegative. It belongs to **global endpoint exclusion/all-window domination**, not retained attachment or null transport. No such bound has been obtained.

The localized physical vectors h_z differ from h. Their positivity is a test/partition construction, not same-vector enlarged nullity, coefficient transport or a replacement for prescribed WD-T38 fields. If global domination were proved, the contact dichotomy would exclude all nonzero finite endpoint kernels; it would not construct a surviving retained null witness for the historical F4 stack.

This route supplies an independent candidate global inequality, but the accumulated structural identities do not prove it. No new aperture certificate is requested: the missing term is global signed arithmetic cancellation, not another decimal frontier.

## Custody and checks

Pinned inputs and exact repeated controls: notes/data/RPB108_AVERAGED_NATIVE_LOCALIZATION_20261006.json. The actual Euler energy, correlation/pole dictionary, certified 47/50 margin and global dichotomy are reused; historical files remain unchanged.

100 correlation-pair algebra controls, 72 separated-pole budget controls and the rational archimedean-tail comparison repeat. They verify normalization and signs, not the analytic integral passage or (6). No Lean build, new axiom audit or CI claim. Newer 19/20 finite/source custody is preserved; certified whole-domain frontier remains 47/50. Global closure, retained attachment, F4 and FULL TRANSPORT CLOSED remain open.
