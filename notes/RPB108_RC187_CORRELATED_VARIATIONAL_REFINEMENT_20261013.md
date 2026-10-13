# RC187: correlated variational bounds shrink the same five-source inverse enclosure

Parent: RC186, `ce8ab73b05de739868149002541b449dd3e34505`.

RC187 reduces the certified canonical inverse-response width from5.513393 to2.576643 on the unchanged response family S=(P0,P2,f0,psi0,w14). It changes the enclosure proof, while retaining RC186's operator, norm, trial directions, rational trial coefficients, and complete represented action carriers. The half-Gram gate still fails.

## Why this refinement helps

RC186 correctly paid many mixed variational terms entry by entry. On a source family with strongly overlapping directions, converting those separate errors into a matrix bound can lose useful correlations. Its new trial reduced the nominal and actual residual bounds, but the selected inverse endpoints remained inherited from RC184.

RC187 retains those residual certificates and pays the combined maps with simultaneous matrix Young inequalities. This preserves the complete source and error Gram geometry rather than assigning independent uncertainty to every mixed entry. No new action accuracy or source coverage is claimed.

## Exact variational decomposition

For U=TY, R=S-MU and represented residual Rhat=S-VY,

\[
 C=\operatorname{Sym}(S^*DU)+\operatorname{Sym}(U^*DR),
 \qquad \Sigma=C+R^*DM^{-1}R.
\]

The complete source/trial cross form satisfies

\[
 \operatorname{Sym}(S^*DU)
 =\frac12\bigl(G_S+G_U-G_{S-U}\bigr).
\]

Every Gram on the right has full finite/analytic source support. The inherited six-trial Gram Loewner endpoints and exact coefficient congruences therefore enclose this entire cross form, including all mixed directions.

The finite cross form Sym(U*D Rhat) is independently accumulated through degree16382. Its arithmetic interval errors are converted to a simultaneous Loewner enclosure. Both its infinite output tail and the difference between Rhat and R remain explicit.

For any complex mixture c and t>0,

\[
 |\operatorname{Re}(Ac,DBc)|
 \le t\|Ac\|_D^2+\frac{1}{4t}\|Bc\|_D^2.
\]

Thus a complete pair of map Gram uppers G_A,G_B pays the whole Hermitian cross form by plus/minus tG_A+G_B/(4t). This holds for arbitrary complex mixtures without error orthogonality.

The actual-action payment uses A=U, B=R-Rhat, the full U Gram upper, and one of RC186's certified transformed error envelopes. The tail payment uses A=U_tail, B=Rhat_tail on disjoint support above16382.

## Complete shared analytic tails

On the omitted support, U has coefficient eta_n times

\[
 Y_{\psi}+A_w(n)Y_w.
\]

With A_w(n)=mu_0+delta_n and |delta_n|<=delta_f, a valid simultaneous trial-tail Gram upper is

\[
 2T_\eta\,\operatorname{outer}(Y_{\psi}+\mu_0Y_w)
 +2T_\eta\delta_f^2\operatorname{outer}(Y_w).
\]

The nominal residual tail upper is retained exactly from RC186. It pays the common leading eta term, the shared w14-source/f0-action moment cancellation, and every variable negative-r factor and higher-moment remainder. The finite q185 represented carrier adds no nominal tail, while its actual omitted action is already included in the action-error envelope.

These two complete tail Gram uppers suffice for the matrix Young tail payment. No cutoff commutation, source independence, or vanishing infinite action is assumed.

## Certified comparison and acceptance

| Same five response sources | Variational width upper | Inverse response width upper | Half-Gram gate |
|---|---:|---:|---|
| RC186 selected inherited inverse enclosure | Not newly narrowed there | 5.513393 | Failed |
| RC187 baseline trial, refined enclosure | 1.427820 | 3.651212 | Failed |
| RC187 q185-enriched trial, selected | 1.657407 | 2.576643 | Failed |

The variational width compares C_upper-C_lower with the same G_lower. It is a separate quantity from the full inverse width. The enriched trial has a smaller inverse width even though its selected variational-width upper is larger than the baseline's; its paid residual contribution is smaller.

The selected variational action parameter is1/30 and its tail parameter is3. The selected actual residual upper uses Young parameter1, while the residual lower is zero. Both selected inverse endpoints come from the refined construction rather than the inherited enclosure.

The actual canonical inverse gate contract remains width<1/2 in this family. The certified acceptance ratio decreases from11.026786 to5.153286. The guaranteed margin bound is1/2-2.576643=-2.076643, hence supplies no positive acceptance margin.

A separate exact check of the stored gate matrix with RC184's rational witness x=(-1/120,3/50,-14/25,-26/25,1) gives x*H*x<-0.00051246845. Thus the selected enclosure fails the gate, beyond merely having an insufficient width upper. This is not an impossibility result or a lower bound on intrinsic inverse uncertainty.

## Replay and remaining scope

The certificate hashes twenty-two inputs: RC186 and its twenty-one historical inputs. RC186's input hashes are checked. Its immutable source/action reconstruction and complete mixed geometry are reused with the same source Gram endpoints. No action generator is changed.

Exact replay reverses finite summation, trial order, error-envelope alternatives, and both variational and residual Young searches. The entire resulting JSON must reproduce exactly. Every selected width is checked by exact PSD comparison against its asserted multiple of G_lower.

Run:

```
python scripts/validate_rpb108_rc187_correlated_variational_refinement.py --output certificates/rpb108_rc187_correlated_variational_refinement.json
python scripts/validate_rpb108_rc187_correlated_variational_refinement.py --replay --output certificates/rpb108_rc187_correlated_variational_refinement.json
```

Next: retain this correlated variational method while tightening the actual psi0 and w14 endpoint-action bounds. Their centered finite-input approximations provide a concrete precision-refinement route; new carriers and all mixed rows must then be reevaluated. No future acceptance or pass count is guaranteed.

The accepted four-source inverse remains intact. Native v10,z_b6,t10 complete action/inverse coverage remains open. Original augmented Weil floor and auxiliary response targets, Stage I, whole-aperture original Weil positivity, RH, F4, and Lean remain open/unclaimed.
