# Weil-Lab — NF359: Retype the unprobed Schur remainder in the correct form-dual topology

**Standing:** Read-only local analysis and exact-rational replay of pinned PR #355 data. No repository or obligation changes. `W-ODD-NEG=OPEN`. The exterior floor `mu>499/50000` is locally replayed under inherited Fourier/form realization, not an accepted native GitHub CI certificate. The original canonical-domain identification remains open.

## 1. Avoid an unnecessarily strong gate

NF357-358 considered the complete strong residual `R=QW(Phi-EY_C)` with an L² Frobenius target `||R||_F²<0.0098613159...`. This is sufficient under the inherited strong-operator hypotheses but **not logically necessary** to bound the Schur penalty. The positivity question is intrinsically one of the continuous dual of the restricted closed form. Bounding `||R||_L2` pays a potentially severe high-frequency graph-norm cost that the desired inverse-energy penalty does not demand.

Let `H=L²_odd(-B,B)`, `J=J_242`, `Q=I-P_J`, and retain the original semibounded form `w=a_star-k_minus` with its original pole included in `a_star`. On `QH`, write `c(z,t)=w(z,t)` and assume (conditional on the inherited form realization) it is a **closed** positive form with `c(z,z)>=mu||z||²`. Set `K_c = D(c)` completed with `||z||_c²=c(z,z)`, `mu>499/50000`. Let `E=[e_1,...,e_4]` be the same physical projected F4 probes and `Phi` the same four original finite signed-energy directions. `H_phi=Phi*W Phi`, `C_E=[c(e_i,e_j)]`, and `Z=[w(e_i,Phi_j)]` are the retained accepted PR355 form matrices. `H_phi>=.99 I`, and the PR355 matched four-probe inverse certificate gives `0<=G_E=Z* C_E^-1 Z <=g H_phi` with the exact retained rational `g≈0.00191130015923938334`.

The source coupling functionals `L_j(z)=w(z,Phi_j)` are continuous on `K_c` **at the form level**, requiring `Phi_j∈D(a_star)`, not `Phi_j∈Dom(W)` of a strong operator. Indeed, on `QH`, `k_minus(z,z)<=eps||z||²` where the accepted original pruned-complement leakage bound is `eps≈1.67678731571420945e-5`. Therefore

    0 < c(z,z) <= a_star(z,z) = c(z,z)+k_minus(z,z)
                          <= (1+eps/mu)c(z,z).

With the local `mu>0.00998`, the equivalence factor is strictly below `1.001680147611`. Cauchy–Schwarz for the positive forms `a_star` and `k_minus` shows `L_j` is bounded on `K_c`, since

    |L_j(z)| <= sqrt(a_star(Phi_j,Phi_j))*sqrt(a_star(z,z))
              + sqrt(k_minus(Phi_j,Phi_j))*sqrt(k_minus(z,z)).

The numerical upper from this naive bound is not claimed useful; the argument establishes the correct jurisdiction of the dual functional.

## 2. Exact form-orthogonal Schur identity — no strong action

Let `P_E^c` be the orthogonal projector **in the c-form Hilbert space** onto the retained span of `E`, and let `V=(span E)^{perp_c}`. By Riesz, every source functional `L_j` has a representer in `K_c`. Orthogonally decomposing those representers gives the **exact** positive-semidefinite 4x4 identity

    S_full = G_E + D,
    D[x,x] = sup_{z in V, c(z,z)>0} |w(z,Phi x)|² / c(z,z).

This defines the unprobed energy-dual remainder `D` directly on the form domain. It is **independent** of the rounded dyadic trial solution `Y_C` and does not require defining `QW Phi` as an L² vector or integrating `|m|² |hhat|²`. The accepted finite-probe matrix gives `G_E`, not an upper bound for `S_full`. The missing `D` is an upper-bound obligation, not calculated here.

Since `H_phi-G_E >=(1-g)H_phi>=.99(1-g)I`, a sufficient four-critical-direction gate is

    ||D||_op < .99(1-g) = 0.98810781284235301049247927... .

A convenient alternative, if bounding the functional in the **positive a_star energy dual** on the *same c-form-orthogonal subspace V*, is

    sup_{||x||=1, z in V} |w(z,Phi x)|²/a_star(z,z)
      < .99(1-g)/(1+eps/mu)
      = 0.98645043050822774245... .

The explicit multiplicative factor is less than 1.001681. In contrast, the prior strong residual L² squared bound is approximately 0.009861315972: a stricter sufficient condition obtained by paying `mu^-1` globally. The two quantities live in different norms and must not be confused as directly comparable measurements.

## 3. Form-core transfer, with its conditional premise

Suppose the fixed-window supported logarithmic Fourier form-core theorem applies to the **same identified original signed form domain** `D(a_star)`. Finite-dimensional `J subset D(a_star)` and `a_star>=kappa_star||.||²` make `P_J` bounded on the positive form space. Hence `Q` preserves and continuously maps that form domain, and `Q C_c^infty(-B,B)_odd` is dense in `Q D(a_star)` in the positive form topology. Since `c` and `a_star` are equivalent on `Q` by the preceding inequality, this is also a core for `K_c`. Applying the bounded `c`-orthogonal projection `I-P_E^c` yields a core for `V`.

Therefore the supremum defining `D` can be tested on **explicit projected form-core functions**, not on arbitrary unspecified domain objects. However a succession of finite tests supplies only **lower** approximations to that supremum. A valid **upper** certificate must supply a uniform inequality over that entire core, then extend it by continuity in the correct form topology. Mere L² density, or a finite Schur sign, is insufficient.

This is conditional on identification of the full original odd form/domain with the Fourier logarithmic carrier; the separate canonical-domain audit remains open. It does not invent a completed form core for an unproved canonical realization.

## 4. Independent scale check

From the pinned PR355 exact dyadic `Y_C`, and **all** interval entries of the retained original physical quotient `S=E*E`, the correction `EY_C` has squared physical norms (columns 0–3) respectively

    0.0000837344570623885114...
    0.0001615428402891901158...
    0.0001528610266650072005...
    0.0000444368636191992677...

Each exact interval uncertainty is below `5e-747`, and every norm squared is `<1/5000`. Thus the dyadic `Y_C` coefficients of order `1e103` are compensated by the tiny physical quotient geometry; they do **not** make the physical correction enormous. The source `Phi` physical norms are still enormous by earlier certified Gram bounds. This measurement is a conditioning diagnostic only; it bounds neither the unprobed dual remainder nor the full strong residual.

## 5. Counterexample to strong-residual necessity

In `ell²`, consider the positive diagonal operator `C e_n=n e_n` and a residual functional represented as an L² vector `r_n=sqrt(n)/log(n) e_n`, for `n>=3`. Its L² norm diverges but the inverse-form-dual norm satisfies `||C^-1/2 r_n||²=1/log(n)² ->0`. Hence asking for a small L² strong residual may fail while the **actual** inverse-energy remainder tends to zero. This is a negative control of the method, not an assertion about original Weil data.

## 6. Stop and next cursor

**New necessary proof target:** a uniform dual bound for the original **four** couplings on the complete form-orthogonal complement `V`, preferably using the nearly identical `a_star` energy metric. A finite witness or additional finite Galerkin probes **cannot** supply this upper bound. Candidate routes: an analytic relative bound on `L|_V` in the original positive log-energy metric, or an exhaustive energy-weighted spectral tail estimate. Keep the original `J_242`, F4, and pole unchanged. Do not repeat the four-probe computation; do not automatically launch a 242-source inverse/strong-action campaign.

Closing four directions would still leave the other 238 selected source directions, the full infinite signed Schur, and canonical-domain realization open. `W-ODD-NEG=OPEN`, RH unchanged.

**Reproducibility:** `nf359_energy_dual_entry.py` verifies pinned ZIP `f7b64ce...1a1d0` and diagnostic JSON `d853e2ec...d60ab9`, recomputes both acceptance thresholds and the exact native-box physical correction. Output: `nf359_energy_dual_entry.json`. No GitHub writes.
