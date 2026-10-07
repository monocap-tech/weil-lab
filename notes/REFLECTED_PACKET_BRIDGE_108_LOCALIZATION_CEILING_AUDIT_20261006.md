# RPB108: the universal localization margin ceiling is impossible

Date: 2026-10-06 (America/Los_Angeles). Live recovery d898db2aabc6e3dc57450a72e7dff72ba57f94ae.
Definitions: [localization ceiling audit](../docs/TERMINOLOGY_RPB108_LOCALIZATION_CEILING_AUDIT.md).
Analytic audit with actual source custody and the classical Weil criterion; not Lean certified.

## Disposition of the preceding target

The exact localization identity and termwise controls in AVERAGED_NATIVE_LOCALIZATION remain valid. Its equation (6), however, proposed the universal sufficient target
\[
E_\chi(h)\le\delta\|h\|_2^2
\quad\text{for every supported logarithmic }h,
\qquad \delta=3\cdot10^{-29}.
\tag{1}
\]
**This target is retired.** It is not merely an unproved stronger route: for the actual native Weil form it is analytically incompatible with the discrete zero-side spectrum.

The proof is by contradiction. Equation (1) and the already established L_chi>=delta mass would imply Q>=0 on all compact smooth tests. The classical Weil criterion then implies RH. Under that consequence, the actual literal formula is a positive discrete sum over critical-line ordinates. The long packets constructed below make (1) fail. No truth value for RH is assumed outside this contradiction, and no actual negative or null vector is constructed.

The external primary source used for the classical criterion is Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, July 4, 2021, introductory equation (4) and Appendix C, Proposition C.1:
https://alainconnes.org/wp-content/uploads/Selecta.pdf .
Their sign convention uses the negative prime/archimedean distribution on tests with vanishing pole moments. Our Q includes the pole terms; restricting to that pole-annihilating smooth subspace gives exactly the criterion's nonnegative zero-side form. The logarithmic-coordinate change is the usual multiplicative-to-additive transform. Thus Q>=0 on the full compact smooth class implies its required restricted positivity.

This is a written analytic application of that criterion, not a new Lean RH equivalence declaration.

## Long packets between actual zero ordinates under RH

Inside the contradiction, all actual zero ordinates theta_rho=Im(rho)/(2 pi) are real. The existing literal formula and source extension give
\[
Q(h)=\sum_\rho \nu_\rho|\widehat h(\theta_\rho)|^2,
\tag{2}
\]
where nu_rho are the exact positive weights proportional to analytic multiplicity in the fixed source normalization. The harmless fixed normalization factor does not affect any estimate below.

Choose any real omega outside this locally finite ordinate set. There is d>0 with |theta_rho-omega|>=d for every rho: local finiteness handles a bounded neighborhood, and the far ordinates are separated automatically. Let eta be a smooth compact function of physical mass one supported in (-1,1). Define
\[
h_L(x)=L^{-1/2}\eta(x/L)e^{2\pi i\omega x},\qquad
\widehat h_L(\xi)=\sqrt L\,\widehat\eta(L(\xi-\omega)).
\tag{3}
\]
Every h_L is an admissible compact smooth actual carrier vector and has mass one. The already certified quartic full-divisor weight implies
\[
\sum_\rho \nu_\rho|\theta_\rho-\omega|^{-4}<\infty.
\tag{4}
\]
Indeed, the finitely many near ordinates have a positive gap, and the far shifted quartic tail is bounded by a constant times the existing height weight. No new local zero-count or spacing theorem is needed.

For N>=2, Schwartz decay and (2)-(4) yield
\[
0\le Q(h_L)
\le C_{N,\eta}L^{1-2N}
\sum_\rho \nu_\rho|\theta_\rho-\omega|^{-2N}
\longrightarrow0.
\tag{5}
\]
Thus global positivity is compatible with arbitrarily small native energy on these **varying** mass-one packets. Each finite window can still be strictly coercive with its own window-dependent constant. There is no contradiction with any certified fixed-aperture margin.

## Averaged local energy retains a positive limit

For the fixed compact chi of the localization identity, put chi_omega=chi exp(2 pi i omega x). The correlations obey
\[
I_s(h_L)=e^{2\pi i\omega s}I_{s/L}(\eta)
\longrightarrow e^{2\pi i\omega s}.
\tag{6}
\]
In the averaged form they are multiplied by c_chi(s). The finite local prime terms and compact pole integral therefore converge immediately. For the archimedean energy,
\[
L_{\chi,\rm arch}(h_L)
=m_0(0)+2\int_0^\infty k(s)
\left[1-c_\chi(s)\Re I_s(h_L)\right]ds.
\tag{7}
\]
Near zero the bracket is O(s^2) uniformly for L>=1: the translation derivative norms of chi and eta control their autocorrelation defects, and 1-cos(2 pi omega s)=O(s^2). For complex eta the imaginary autocorrelation term is O(s/L) and its product with sin(2 pi omega s) is also O(s^2); equivalently take eta real to avoid it. We choose eta real. Beyond the compact c_chi support the bracket is exactly one, and k has an integrable tail. Dominated convergence proves
\[
\boxed{L_\chi(h_L)\longrightarrow Q(\chi_\omega).}
\tag{8}
\]

The native logarithmic envelope on the fixed chi support gives Q(chi_omega)->+infinity as |omega|->infinity. One proof retains a fixed bounded Fourier band of chi with positive mass; its shifted logarithmic weight tends to infinity. The bounded prime symbol and physical pole budget cannot prevent this divergence.

Consequently choose omega outside the discrete ordinate set with Q(chi_omega)>delta. Equations (5) and (8) imply
\[
E_\chi(h_L)=L_\chi(h_L)-Q(h_L)
\longrightarrow Q(\chi_\omega)>\delta.
\tag{9}
\]
This contradicts (1). More strongly, under RH the full localization defect has no finite uniform physical-mass upper bound over all compact supported h: choose omega to make the limit in (9) arbitrarily large.

## What failed and what survives

The prior pass correctly said its target was stronger than global positivity and did not prove it. The present audit identifies a decisive obstruction: a fixed local patch averages positive energy into Fourier gaps of the global discrete spectrum. Even perfectly nonnegative global Weil energy cannot absorb that artificial local energy by a fixed mass-only ceiling.

The failed proposed route is
\[
\text{local certificate}+\text{universal mass-only defect ceiling}
\ \longrightarrow\ \text{global closure}.
\]
The implication itself is valid, but its second premise is impossible for the actual form. This distinction matters: the exact localization identity is not defective, and no existing sign certificate or source dictionary is reopened.

The identity Q=L_chi-E_chi still says that E_chi<=L_chi is equivalent to global positivity. Merely renaming that inequality would provide no independent theorem. No corrected independent global cancellation estimate has been obtained here. A source-sensitive comparison could remain possible, but it must permit the spectral-gap packets and their positive local-energy limits.

The active global priority therefore returns to the actual zero-eigenvalue endpoint equation and its existing full-kernel lower-flux or Gaussian-moment gates. Those are kernel-specific and do not demand a false estimate on every physical vector. Their arithmetic bounds remain unproved. Retained one-vector attachment and prescribed whole-packet custody remain separate.

Remaining category: **global endpoint exclusion**. No endpoint is excluded by retiring this route, and no same-vector enlarged cancellation or F4 obligation is discharged.

## Transport, provenance and validation

The physical vectors h_L vary with L; their supports enlarge and their Fourier bandwidth contracts. Equation (3) explicitly changes the physical vector. It is not a dilation proving same-vector null transport. None is a finite-window null mode in this argument.

Pinned repository sources and the retrieved primary criterion are recorded in notes/data/RPB108_LOCALIZATION_CEILING_AUDIT_20261006.json. The proof uses actual full-divisor quartic summability, the literal formula and full-domain source custody, plus the previous localization identity. Historical wording and certificates are preserved; this audit supersedes only the proposed universal target's viability.

160 scaling, 128 ceiling and 152 shifted-tail controls repeat. They check exponents and comparison signs, not the analytic zero-gap limit or Weil criterion. No new Lean build, axiom audit or CI result is claimed. Newer complete 19/20 Gram/scalar-obstruction custody is preserved; whole-domain frontier remains 47/50. F4 and FULL TRANSPORT CLOSED remain open.
