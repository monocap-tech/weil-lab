# RPB108: actual eight-source corrected Schur certificate

## Carriers and theorem

Work on the actual supported logarithmic form domain H at aperture a=1/2, with its multiplier-plus-pole form Q. The physical orthonormal vectors are v_i(x)=sqrt(2i+1)P_i(2x), supported on [-1/2,1/2]. Define E=span(v_0,...,v_63) and F=E's physical L2 orthogonal complement inside H. The previously proved complement estimate Q(f)>(1/5)||f||_2^2 and its H coercivity hold on F. The associated canonical lift z_e in F is characterized by Q(z_e,f)=Q(e,f). The exact low Schur form is S(e,e')=Q(e,e')-Q(z_e,z_e').

**Certified theorem.** For every nonzero e in E_8=span(v_0,...,v_7),

S(e,e) > (1/250000)||e||_2^2.

This is the compression of the actual full 64-coordinate Schur form. The lift removes coupling to F, with the same e in the actual source, prime translates, poles and residual. It does not remove coupling to the other 56 low coordinates.

## Exact surrogate Gram

Let Pi be the physical projection onto E. The actual sources q_i represent Q(v_i,f) and lie in L2 by the previously proved interior-source theorem. Write q_i=v_i L+h_i, L(t)=-(log t+log(1-t))/2, t=x+1/2. The preceding constructive source certificate gives rational polynomials p_i on the three exact prime panels, with htilde_i=sqrt(2i+1)p_i and combined source operator error eta<1.30e-30.

Set rtilde_i=(I-Pi)(v_i L+htilde_i). Compute its Gram Rtilde exactly up to outward interval enclosures:

Rtilde=R_L+R_H+R_LH+R_HL.

R_L is the already enclosed endpoint-log residual Gram. Polynomial products give the smooth full Gram. The mixed full Gram uses elementary antiderivatives of t^k log t and the substitution t -> 1-t for log(1-t). Subtract the first 64 physical projection products, retaining every log/smooth cross term. All polynomial products and substitutions are exact rational operations before interval integration.

The integration panels are [0,1-log 2], [1-log 2,log 2], [log 2,1]. Their endpoints are interval enclosures of the exact values. Polynomial primitives are evaluated by interval Horner evaluation. The log primitive vanishes at t=0; interior logs use 220 atanh-series terms after reduction to [1,2], with a uniform rational remainder bound. Intermediate interval rounding uses a 10^-120 grid. Square-root normalization uses the existing rational enclosure. The maximum surrogate Gram entry width is below 1.24e-53.

The displayed surrogate diagonal is approximately

0.00123801103438, 0.00365414298979, 0.00617439809315, 0.00855014103695, 0.01104863399954, 0.01350784479501, 0.01581879705728, 0.01856556642285.

## Source error and matrix proof

Since I-Pi contracts L2, the residual source-map error is at most eta. A certified norm bound is M=sqrt(trace Rtilde), using the interval trace upper bound. Thus

||R_actual-Rtilde|| <= delta=eta(2M+eta) < 7.27e-31.

The actual coercive complement theorem gives S >= Q_8-5R_actual on E_8. In Loewner order,

S >= Q_8-5Rtilde-5delta I.

Q_8 is supplied by the independent rational actual finite-matrix constructor, including the native prime 2 and poles. Normalize its unnormalized polynomial matrix physically. Interval Schur elimination proves

Q_8-5Rtilde-5delta I-(1/250000)I > 0.

The eight pivot lower displays are approximately 0.0818206, 0.2540142, 0.0178490, 0.1321678, 0.0416593, 0.0155467, 0.000741371, 0.5899306. These are elimination pivots, not eigenvalues. Replacing the first diagonal by -1 is rejected as a negative control.

This certifies the actual corrected sign, including source truncation and all integral errors. Agreement with the prior 256-node pilot is only a check: the midpoint Gram differs from it by about 1.73e-9 in operator norm, and no pilot convergence assumption enters the proof.

## Consequence and exact remaining obstruction

The completion-of-square identity gives

Q(e+f)=S(e,e)+Q(f+z_e,f+z_e), e in E_8, f in F.

Therefore Q is strictly positive on U=E_8+F, a closed subspace of H of codimension 56. Closedness follows from the bounded finite physical projection. Any negative subspace intersects U only at zero, so the actual negative index is at most 56. Likewise the global weak kernel (vectors u with Q(u,h)=0 for all h in H) injects under projection into span(v_8,...,v_63), so its dimension is at most 56. With reflection, the corresponding bounds are 28 in each parity sector. These are bounds on negative index and weak nullity; arbitrary vectors with Q(u,u)=0 are not thereby weak-null vectors.

For an exact smaller obstruction, put W=span(v_8,...,v_63), T=S restricted to E_8 (now T>=(1/250000)I), and define the mixed map B by <e,Bw>_2=S(e,w). The remaining finite form is

S_remaining(w,w')=S(w,w')-<Bw,T^-1 Bw'>_2.

Completing the square inside E=E_8+W proves full Q>=0 if and only if S_remaining>=0. Negative index and weak kernel transfer exactly to this 56-dimensional form (28 per reflection parity). T^-1 exists with norm at most 250000. The mixed map and the remaining block have not been enclosed here. Positivity of either raw W block alone would not establish positivity of S_remaining.

This is an exact reduction of the remaining sign obstruction, not a retained-witness membership assumption. The global endpoint exclusion / signed endpoint-null Gaussian input remains independently open. No actual negative witness, nonzero weak null witness, RH conclusion or carrier contraction is asserted. F4 and FULL TRANSPORT CLOSED remain open.

## Artifacts and validation

`scripts/certify_native_coupled_schur.py` and `notes/data/RPB108_COUPLED_SCHUR_CERTIFICATE_20261005.json` contain the reproducible standard-library calculation, all Gram intervals, exact source error and shifted pivots. The source certificate SHA256 is pinned in the output. The existing finite-matrix helper now optionally returns its matrix and allows the interval grid to be selected; default certificate output is preserved. The prior a=1/2 finite certificate was reproduced byte-for-byte. Lean source, axioms and the previously reported CI checkpoint are unchanged; this new certificate has not been formalized in Lean.
