# RPB108 RC287 — six-source trial invariance and inverse-covariance transfer threshold

Parent: RC286 `023801851ee560e09878e6af2d50faf615dcb439`. Aperture B=11/10.
Original Weil form remains unchanged. **No new original source actions and no
new positive same-parity pivot are claimed.**

## 1. What really transfers to rank 317

All six original RC280 trial polynomials, covering even P0/P2/P4 and
odd P1/P3/P5, have physical Legendre support through degree 64.
Every RC283 reduced positive projection (ranks 301, 317 and 334)
contains that entire support. Both the RC278 rank-371 reference
and the reduced reference use the identical parity-specific
augmentation coefficient lambda=C_b.

Therefore for each trial Z_i and source u_i,

    G_old Z_i = G_new Z_i,
    e_i,old = D^-1 u_i - D^-1 G_old Z_i
            = D^-1 u_i - D^-1 G_new Z_i = e_i,new.

All six trial variational centers AND their full 3x3 even/odd center
Grams are invariant under the reference reduction. This is an exact
algebraic source/action interface. The source residual vectors
are also exactly invariant.

**The inverses are not invariant:** the complete residual covariance
matrix E_new = [<e_i, N_new^-1 e_j>_D] must be recertified against the
changed reference.

## 2. Exact six-mode covariance budget

RC280 certifies a Loewner upper matrix S_old on the residual covariance
and a positive old-native gate lower matrix L_old. It certified old
positive source subsets [P0,P4] in even parity, and [P1,P3,P5] in odd
parity, with rigorous respective native eigenvalue floors

    even gamma_old >= 0.00059192661158
    odd  gamma_old >= 0.00000098600777.

Because the trial centers do not change, a sufficient condition to
preserve the respective *old certified positive-block margin* is

    E_new <= S_old + Delta,
    0 <= Delta < (gamma_old/lambda) I

on each selected source subset. The exact rational validator computes
the strict scalar covariance budget:

| Old positive subset | Native old floor, approximately | Allowable added covariance identity norm |
| --- | ---: | ---: |
| Even P0,P4 | 5.91927e-4 | **< 6.02505e-5** |
| Odd P1,P3,P5 | 9.86008e-7 | **< 9.57687e-8** |

The odd three-source block is extraordinarily sensitive. Even a
small *additional* conservative covariance payment may defeat that
old proof. A new source-family trial optimization may be preferable
to merely transporting the RC280 margins.

## 3. Why the global inverse comparison is insufficient

The inherited bounds G_old<=nu_old D and G_new>=mu_new D yield, by
noncommuting inverse Loewner order,

    G_new^-1 <= (nu_old/mu_new) G_old^-1.

This implies E_new <= kappa S_old, where kappa=nu_old/mu_new, and hence
the actual new gate has a Loewner lower matrix

    L_new >= L_old-lambda*(kappa-1) S_old.

For the preferred rank-317 reference, the conservative kappa factors
are approximately **945.24 even** and **774.42 odd**. Every scalar
diagonal in the originally certified RC280 positive source subsets
becomes negative in this *derived lower matrix*. The exact validator
checks these signs for ranks 301, 317 and 334, with downward-rounded
rational entries and upward-rounded covariance displays.

These are **negative LOWER ENVELOPES, not negative actual gate entries,
negative eigenvalues, or original Weil witnesses**. The failed sufficient
test says the global comparison is much too weak to justify carrying
the six-mode positivity certificate from rank 371 to rank 317.

## 4. Work still open

The separate RC285 positively certified P0/P1 pivots and RC286 full
cross-coupling mass payments in the rank-317 reference remain valid.
They are mathematically different trial and inverse-residual
certificates and are not invalidated by this no-go transfer audit.

RC287 provides a precise computation contract for **RC288**:
reconstruct the complete mixed residual covariance under the new
rank-317 inverse, using RC280's unchanged six polynomial source
actions, degree-resolved original output intervals and tails.
The particularly fragile odd-three-source block may benefit from
stronger trial selection and simultaneous covariance optimization.

The 315-dimensional rank-317 remaining Schur principal form,
Stage I, global F4, RH and Lean remain **OPEN**.

## Replay

```bash
python scripts/validate_rpb108_rc287_six_source_covariance_transfer.py --output certificates/rpb108_rc287_six_source_covariance_transfer.json
python scripts/validate_rpb108_rc287_six_source_covariance_transfer.py --output certificates/rpb108_rc287_six_source_covariance_transfer.json --replay
```

The validator checks immutable RC278, RC280, RC283 and RC286 input Git
blob identities, exact trial parity/support, six-source center
invariance, exact covariance transfer formulas and their insufficient
bounds. Actions replay does not independently prove imported analytic
inequalities and is not a Stage I or RH proof.
