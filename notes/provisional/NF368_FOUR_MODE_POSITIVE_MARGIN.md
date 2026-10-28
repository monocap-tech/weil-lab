# NF368 — Quantified four-mode positive margin and matched exterior acceptance budget

**Standing:** exact-rational replay of the SHA-pinned, already native-certified PR348 original four-mode signed Gram and PR355 physical/signed exterior quotient; original form/domain assumptions inherited. No new Arb integration, no full 242D or global sign theorem. Active W-ODD-NEG OPEN.

## Accepted inputs
- PR348 original_four_mode_critical_block.json SHA256 a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922, embedded in the original PR355 ZIP.
- PR355 original_exterior_scalar_floor_stop.json SHA256 d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9; parent ZIP SHA256 f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0.
- The unchanged four real original critical physical vectors F and original J242 physical projection P; Q=I-P. Complete signed original W=Astar-Kminus, positive exterior signed floor mu=1/1000-epsilon (old accepted #350), epsilon=1.6767873157142093e-5, mu>0.00098.

## First actual quantitative positive margin
Reconstruct each PR348 signed Gram interval [lo_ij,hi_ij] as exact Fractions. Form midpoint M and radius R. The maximum absolute row radius is ~2.75e-40. The checker proves by a full exact-rational 4×4 LDL factorization:

    M-(5e-23 + max_i sum_j R_ij) I is positive definite.

Consequently the complete original *coupled* four-mode signed form has

    w(Fz,Fz) > 5e-23 ||z||²           for all real z∈R4.

This is a certificate of positivity ONLY on the particular fixed four-dimensional trial plane. It does not assert global W≥0 or RH.

NF367 uses the PR355 exact signed/physical quotient Grams to give

    |w(PFz,PFz)-w(Fz,Fz)| <= delta ||z||²,
    delta=9*2^-290 + tr(C_exterior) < 2^-286.

Therefore the *physically projected* four independent modes obey the rigorous finite selected inequality

    w(PFz,PFz) > 4.9e-23 ||z||².

The accepted parent also gives the upper operator bound on this selected four-plane <1.1e-16 relative to physical L². Neither endpoint alone controls the infinite signed Schur.

## Matched whole-exterior gate, no interpolation of missing data

Let C=QWQ be the self-adjoint positive signed form on F=J242^perp, with c(v,v)>=mu||v||² under the inherited exterior theorem. Let Bp=w(p,·)|F, p=PFz. The complete signed Schur penalty is the squared C-dual norm:

    D[p]=||Bp||²_{(F,c)*} = sup_(v∈F)[2Re w(p,v)-c(v,v)].

To certify positivity on this **four-plane only**, it would suffice to prove D[PFz]<=4.9e-23||z||². If Bp has an independently verified strong L² representative QW p, a stronger (sufficient, not necessary) scalar-floor acceptance test is

    ||QW(PFz)||² <= mu * 4.9e-23 ||z||²,

with old accepted mu≈0.000983232126842858; RHS≈4.81784e-26||z||². Thus the strong forcing norm must be <=2.19496e-13||z||, *if strong realization is available*. The previous NF355 failed global mu-only bound on DIFFERENT energy-normalized selected directions; that does not decide this four-plane threshold.

For a trial exterior response y and form-dual residual r=Bp-Cy, an exact identity gives

    D[p] = 2Re Bp[y]-c(y,y) + ||r||²_{(F,c)*}.

A certified upper can be obtained using the full residual norm (or ||r_strong||²/mu with a proven strong representative). A finite Galerkin lower correction is NOT an upper bound. No such y/r has been computed here. Full selected matrix positivity and whole infinite Schur remain OPEN.

**Next stop/gate:** Construct ONE declared matched exterior trial on the original four-plane and certify the entire weak form residual, or prove a no-go on its feasible error budget. Do not start a raw 242D inversion or source/dimension campaign.
