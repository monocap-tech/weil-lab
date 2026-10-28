# NF370 — Original-source shear and unprobed signed exterior residual

**Scope:** canonical original W-ODD-NEG; unchanged J242, original four PR348 critical source functions, true signed seven-prime symbol and odd pole. Exact form-level reduction with independent original-data SHA-pinned rational replay; **not** global Schur closure, native-Arb recomputation, or an original-operator-domain audit.

## Full Feshbach shear before another inverse

Let J=J242 be the physical selected space, Fext=J^perp with positive complete original signed restricted form c and associated operator C >= mu I. Let f=(f1,...,f4) be the unchanged four original critical functions, p=Pf and q=Qf. Let E: R4 -> Fext have columns q_i, and CE=E* C E >0 (already certified in original PR355).

Define the original-source exterior functional d(v)=w(f,v) on Fext and selected-source functional b(v)=w(p,v). Then

    b = d-C E,      E* b = E* d - CE.

For the **exact** E-Galerkin response associated with b,

    Y_b = E CE^-1 E* b,

the residual is independent of the physical quotient shear:

    R=b-C Y_b
     =d-C E CE^-1 E* d,                (1)
    E* R=0.

The source representation has Galerkin response

    Y_d=E CE^-1 E* d = E+Y_b.

The original signed source Gram H=f* W f, selected four-mode Gram P4=p* W p, and finite Schur corrections obey

    H=P4+B+B*+CE,    B=p* W E,
    H-(E*d)* CE^-1 (E*d) = P4-(E*b)*CE^-1(E*b).  (2)

The true complete infinite Schur is congruence-invariant:

    P4-b* C^-1 b = H-d* C^-1 d.         (3)

The entire missing unprobed term is exactly

    R* C^-1 R
      = d* C^-1 d - (E*d)* CE^-1 (E*d). (4)

Every inverse here is the inverse of the positive **exterior form operator** on the specified carrier, not Q W^-1 Q. The identities (1)-(4) follow by expanding q∈range(E) and positive-form Galerkin orthogonality. The exact finite replayer checks the source/selected shear against the original archived NF369 complete 4x4 signed matrices, and verifies that the exact dyadic candidate Y_source=I_4+Y_projected preserves the same finite residual and finite Schur. It does NOT calculate C^-1 on the unprobed infinite space.

## One smooth signed original multiplier, no source-count expansion

Under the inherited original SI10/SM41 Fourier realization, A_o has whole-real symbol a_o=max(1/1000,m), and Kminus has kminus=(1/1000-m)_+. Therefore the original complete odd signed form is

    W=Astar-Kminus=P_I m(D) P_I -2|s><s|,

where s=sinh(x/2) belongs to J242 and m is the uncut seven-prime signed digamma multiplier. For every exterior test v, <s,v>=0, hence

    d(v)=<m(D) f,v>,                         (5)
    d_strong=Q P_I F^-1 [m(xi) fhat(xi)]      (when strong action exists).

The critical original f consists of exactly the already accepted 32 sine frequencies c_n=5n/11 and a small common supported sinh coefficient. Its Fourier transform is explicit (NF363/364). The multiplier m is smooth in xi on the real axis; unlike max(kappa,m), there are **no nonsmooth crossover points** m=kappa to pay in this forcing integration. No seven-prime, pole or high-frequency action is discarded: the pole vanishes **only in the exterior functional**, not from W on the selected sector.

The original source strong-domain requirement is supported analytically on these finite explicit physical functions: piecewise smooth supported boundary traces imply fhat(xi)=O(1/|xi|), the original logarithmic symbol obeys |m(xi)|<=17+log|xi| for |xi|>=1 (SM41 plus full negative norm bound), and int_1^infty (17+log t)^2/t^2 dt<infinity. Thus m fhat is L2, under the inherited compressed multiplier/operator identification. This finite-source observation does **not** resolve the independent general original-domain audit.

## Correct computational entry, not a scalar detour

A legitimate sufficient four-mode full signed test is the **matrix** inequality

    d* C^-1 d <= H,

or, after the certified q-probe, the equivalent

    R* C^-1 R <= H-(E*d)* CE^-1(E*d) = P4-D_E.

The target is anisotropic and retains the already accepted original positive 4x4 margin. A strong-domain sufficient upper would use (QWf)^* (QWf)/mu, but a direct scalar norm of unprojected Wf is not enough: the physically correlated Q subtraction must be retained. A selected-space trial j_i∈J242 can upper-bound the full source forcing via ||QWf_i||<=||Wf_i-j_i||, with **complete** low-frequency correlated response plus the already analytic high tail. No selected 242-dimensional inverse or source enrichment follows automatically.

**STOP:** This pass certifies exact original-source retyping and a SHA-pinned finite matrix consistency replay, not a new sign of the whole infinite exterior. PR355/NF369 q-probe correction remains a Galerkin lower slice; the full R* C^-1 R is OPEN. Do not promote O1/O2, even, F4, CC27, Weil or RH.

**Evidence:** original NF369 run 40762984235, artifact 12849890537, archive SHA256 1bacc7ae7967d1282eb28fd9d8566204eb21ba93246f6e81b174a18cc2ab1e96, JSON SHA256 1b22cd77dd555749b8dcc41f92ddd91d982f2eca23ebf3a7638e512147b39d18. Exact replay script scripts/local_replay/nf370_original_source_shear_replay.py. Next: evaluate/bound the genuinely correlated 4x4 full signed original-source forcing and its exterior form-dual response; no raw 242 solve.
