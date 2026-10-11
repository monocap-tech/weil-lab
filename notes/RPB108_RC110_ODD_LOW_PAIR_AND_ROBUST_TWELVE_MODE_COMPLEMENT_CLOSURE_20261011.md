# RC110 — odd low pair and robust twelve-mode complement closure

Date: 2026-10-11. Aperture a=11/10. Branch: `research/rpb108-route-consolidation`.

RC110 admits two additional low-energy odd native candidates, RC107 indices 3 and 4, with their coupling to the certified infinite complement paid. The corrected selected native span now has dimension twelve: five even directions inherited from RC109 and seven odd directions certified jointly here. The original nonpositive spectral dimension upper improves from 1,240 to 1,238.

The odd certificate retains the three RC63 weak/control directions and RC107 candidates 9 and 10, then adds candidates 3 and 4. It therefore contains RC109's five-dimensional odd corrected span. The even five-dimensional certificate is inherited unchanged. Actual canonical metric lower bounds prove independence.

These fixed candidate spans are not identified with exact spectral projections of the full original operator. The remaining head directions are not certified positive. The full exceptional spectral coverage problem and whole-aperture positivity remain open.

## The source-tail calculation

Only three new weighted-derivative Gram entries are integrated for the new odd pair. The derivative is that of the complete signed nominal source, including its archimedean terms, exact prime translations and signed odd pole source. The existing physical Riesz trials, native targets and original source approximation are unchanged.

Every odd trial has opposite endpoint values. Its prime jumps share the same odd profile J_o supplied by RC101. If e_j is the exact right endpoint value, the physical source has the decomposition

\[
F_j=g_j-e_jJ_o.
\]

The sign is shared by the two inputs. Its covariance is therefore the positive rank-one matrix j_tail times e e*. Removing the profile cancels the prime support jumps, while leaving the derivative inside each open prime segment unchanged.

On y in [0,1], the continuous remainder derivative Gram is

\[
D_{ij}=\int_0^1 y(1-y)g_i'(y)g_j'(y)\,dy.
\]

The new directed intervals have approximate centers

\[
D\approx
\begin{pmatrix}
0.935689238806&0.408255203430\\
0.408255203430&3.070263430206
\end{pmatrix}.
\]

The signed mixed entry is retained in a common Loewner upper. An explicit uniform pole-derivative Taylor remainder is attached before the continuous-tail theorem is applied. The actual source correction and actual Riesz error are paid separately.

The calculation uses the original odd pole sign. Its differentiated pole polynomial has coefficients -R times the trial exponential moment times (B/2)^k/k! for even k, with R=11/5 and B=11/10. The odd logarithmic reflection terms also retain their signs. This is not an even-source formula with a parity label changed.

Primary integration uses directed 800-digit contexts. Replay uses 600-digit contexts, reflected logarithmic moments and affine prime-segment integration, and checks containment inside the stored primary intervals. Precision is a working choice; exact interval containment and rational matrix inequalities decide acceptance.

## Same complete head and complement

Let H be the original complete sufficient 1,250-feature canonical Riesz head, E=H perpendicular, and D_E=P_EA_QP_E|_E. The inherited original floor remains

\[
D_E\succeq\alpha I,\qquad\alpha=247/2500.
\]

No positivity of a smaller canonical-head complement is assumed. The new physical tail theorem subtracts polynomials that map by i* into this same H.

RC95's rank-1250 canonical adjoint tail factor tau and RC101's odd jump-profile tail upper give

\[
N_{\rm low}=\tau^2\left[
\frac{2R D_{\rm up}}{1250\cdot1251}
+2j_{\rm tail}e e^*\right].
\]

This bounds the nominal original coupling to E for the new odd pair. The actual Riesz residual covariance is contracted directly from RC81 in the matching new-pair coordinates. The original source error is transported with the inherited projected archimedean, prime and pole estimates, yielding E_source. With the accepted source Young parameter t=1,

\[
\Gamma_{\rm low}\preceq G_{\rm low}=2N_{\rm low}+2E_{\rm source}.
\]

The retained high pair uses RC109's accepted actual coupling upper G_high unchanged.

## Joint covariance without assumed independence

First combine the new low pair and retained high pair. With u=1/2, vector Young gives

\[
\Gamma_{\rm new}\preceq
\mathrm{diag}((3/2)G_{\rm low},3G_{\rm high}).
\]

Then combine these four directions with the retained weak triple. With s=1/2,

\[
\boxed{\Gamma_{\rm selected}\preceq
\mathrm{diag}((3/2)G_{\rm weak},3G_{\rm new}).}
\]

Both estimates hold for all joint coefficient vectors. They pay unknown mixed source covariance and retain the signed correlations within the already certified two- and three-column blocks. Source independence and covariance-entry signs are not assumed.

The original head entries are reconstructed directly in the seven selected coordinates through RC107/109's source-response alignment identity. The retained weak original head lower is inherited from RC101. The new four-direction original head lower is formed from matching direct signed intervals. Subtracting the joint covariance upper divided by alpha gives fixed corrected diagonal lowers W for the weak triple and H_n for the new four directions. Their original mixed Weil entries have a center C_0 and halfwidth matrix r.

The actual corrected selected head dominates the matrix family

\[
\begin{pmatrix}
W&C_0+\Delta\\
(C_0+\Delta)^*&H_n
\end{pmatrix},\qquad |\Delta_{ij}|\le r_{ij}.
\]

The off-diagonal entries here are the original mixed Weil entries in a sufficient lower family. They are not asserted to equal the off-diagonal entries of the exact complement-eliminated head. The common covariance domination already pays the unknown mixed complement contribution in Loewner order.

## Replacing 4,096 vertex checks by one robust Schur inequality

There are twelve uncertain mixed entries: three weak rows and four new columns. Direct independent-endpoint enumeration would require 2^12=4096 matrix checks. RC110 supplies an analytic upper for their complete inverse penalty instead.

Suppose H_n is positive definite. For every allowable Delta,

\[
|\left(\Delta H_n^{-1}\Delta^*\right)_{ik}|
\le B_{ik}:=\sum_{j,l}r_{ij}|(H_n^{-1})_{jl}|r_{kl}.
\]

Choose positive rational scales d_i and form the diagonal matrix

\[
U_{ii}=\sum_k B_{ik}d_k/d_i.
\]

Then Delta H_n inverse Delta* is at most U in Loewner order. Congruence by diag(d_i) proves the difference is diagonally dominant with nonnegative diagonal: the diagonal allowance includes the error Gram's own diagonal bound and every absolute off-diagonal bound. This argument controls the entire interval box, including correlated errors.

For any positive v, the matrix Young inequality gives

\[
(C_0+\Delta)H_n^{-1}(C_0+\Delta)^*
\preceq(1+v)C_0H_n^{-1}C_0^*+(1+1/v)U.
\]

Hence

\[
\boxed{W-(1+v)C_0H_n^{-1}C_0^*-(1+1/v)U\succ0}
\]

is sufficient for positivity of every member of the corrected lower family. This retains the signed nominal mixed response and pays only the remaining mixed-entry uncertainty through an error Gram. The accepted mixed-error Young parameter is v=1.

The test is sufficient, not necessary. Failure would not prove a negative or null original direction. No actual mixed-entry independence is required.

## Actual canonical floor

Let M_hi be the selected actual canonical metric upper, obtained as rho times the exact physical native-target Gram, rho=252/257. To certify a floor beta, apply the robust Schur test to the lower family minus beta M_hi. This subtracts the metric's weak, strong and mixed blocks before inverse elimination; an unknown actual metric is not silently substituted for M_hi.

Exact inversion and independent determinant-ratio checks certify the odd selected floor

\[
\beta_{\rm odd}=10^{-16}.
\]

The inherited even selected floor remains 10^-19. For the complete selected-native-plus-E positive subspace, the source norm bound and square completion give

\[
\mu=\frac{\min(\beta,\alpha)}{\max(2,1+2g/\alpha^2)}.
\]

The odd whole-subspace floor is approximately 7.08037e-18. The inherited even whole-subspace floor is approximately 1.14223e-20 and sets the shared floor. The exact shared value is 3998285824/350042833722523441314697265625.

The selected dimensions are five even plus seven odd. Their direct sum with E has codimension 1250-12=1238. A nonpositive original spectral space intersects this explicit uniformly positive space only at zero; projection onto its finite orthogonal complement is injective. This proves the nonpositive spectral dimension upper 1238, without asserting that any nonpositive modes exist.

## Validation and remaining work

The validator binds eighteen input byte hashes, including RC109 and its full source/metric dependencies. It integrates the three new odd derivative entries, validates exact frame changes and actual metric independence, pays both covariance-combination steps, reconstructs the signed mixed original entries, checks exact new-block inverses, and verifies the robust Schur lower and canonical floor.

Independent replay changes the integral formulas, reverses signed contractions, verifies weighted error-row identities, and uses determinant-ratio positivity checks. The entire mixed interval family is controlled analytically; no 4096-vertex list is needed. Separate illustrative rational controls check a positive four-dimensional interval family against all sixteen corners, reject a genuine negative matrix, and show a positive matrix that the sufficient bound rejects at fixed Young parameter one. These controls are not original arithmetic operators and demonstrate the stated sufficiency boundary.

Repository reproduction:

```sh
python scripts/validate_rpb108_rc110_odd_exceptional_pair_closure.py > /tmp/rc110.json
python scripts/validate_rpb108_rc110_odd_exceptional_pair_closure.py --replay /tmp/rc110.json
```

Published artifacts are the validator, `certificates/rpb108_rc110_odd_exceptional_pair_closure.json`, and this note.

The corrected native span grew from ten to twelve dimensions and retained the previously certified directions. Two further low-energy odd candidates are now admitted with their E coupling. The complete corrected native 22-space, spectral coverage beyond that native space, and a positive floor on the remaining full finite-head strong space are still open. Whole-aperture positivity at 1.10, RH and Global/F4 are not proved.
