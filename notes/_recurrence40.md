# SZ edge recurrence 40 — endpoint subspace closure

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-39
Public promotion: forbidden

## Objective

Replace the artificial identity-carried sheet in series-39 by the true endpoint graph subspaces supplied by the boundary transfer equations.

The main result is positive for every gate-free endpoint atom:

- the n=0 unmatched-shear bookkeeping zero disappears;
- pure bulk propagation between the true endpoint lines is nonresonant for every admissible length;
- matched k-scattering between the true endpoint lines is nonresonant, with or without admissible bulk propagation.

The remaining endpoint obstruction is now exactly the gated endpoint graph, together with the simultaneous two-cycle closure in the paired-defect geometry.

No new global fixed-L injectivity interval is claimed.

## 1. Gate-free endpoint graph lines

Use the exact transfer coefficient

R = G delta / (mu^2-G^2).

The entrance P-relation in a gate-free endpoint atom is

S = R X.

The terminal relation in a gate-free endpoint atom is

S = R^(-1) X.

Therefore define

v_in =
(1,R)^T,

v_out =
(1,R^(-1))^T.

The corresponding endpoint graph lines are

L_in = span(v_in),

L_out = span(v_out).

They are registered in the terminology file.

A row annihilating L_out is

ell_out = (R^(-1), -1).

## 2. Pure bulk line-to-line closure

The true gate-free endpoint closure for n bulk steps is

ell_out M0^n v_in = 0.

Equivalently, with columns M0^n v_in and v_out, resonance would require their 2-by-2 determinant to vanish.

Using the exact outward rational enclosures

1.5849625 < log3/log2 < 1.5849626,

2.3219280 < log5/log2 < 2.3219281,

and outward square-root arithmetic, the line-to-line determinants are nonzero for every admissible

0 <= n <= 15.

The closest case is n=2:

0.496884
<
det( M0^2 v_in , v_out )
<
0.496895.

For comparison,

n=0 gives a determinant less than -2.19318,

n=1 gives a determinant less than -0.85680,

and every n>=3 has absolute determinant greater than 1.84.

Thus

|det( M0^n v_in , v_out )| > 0.4968

for every admissible n.

So the true endpoint graph lines never align under admissible pure bulk propagation.

## 3. Unmatched zero-bulk closure

Series-39 found

det(I-E_plus)=det(I-E_minus)=0

at zero doubled bulk advance.

That zero came from the identity-carried companion sheet.

Impose the true endpoint graph lines instead.

For E_plus, take

V_low = a v_in,

V_high = b v_out.

The fixed lower-sheet equation is

(M0-I)V_low
+
c_plus e2^T V_high
=
0.

Thus the endpoint closure matrix on the amplitudes (a,b) is

C_plus =
[ (M0-I)v_in , c_plus (e2^T v_out) ].

For E_minus, the corresponding equation is

-c_minus (e1^T V_low)
+
(M0-I)V_high
=
0,

giving

C_minus =
[ -c_minus (e1^T v_in), (M0-I)v_out ].

A direct symbolic simplification gives the same determinant in both orientations:

det C_plus
=
det C_minus
=
beta (mu^2-G^2)/(G delta^2).

This is strictly positive.

Using

beta>1,

mu^2-G^2>1/4,

G<3/2,

delta^2<98/45,

one gets the explicit exact bound

det C_plus
=
det C_minus
>
15/196.

Numerically,

det C_plus
=
det C_minus
=
0.3414753471....

Therefore the n=0 unmatched-shear zero in series-39 is a bookkeeping artifact, not a physical endpoint resonance.

## 4. Doubled endpoint-line closure

For a doubled state W=(V_1,V_2), define the incoming injection

J_in =
diag(v_in,v_in),

viewed as a 4-by-2 matrix.

Define the outgoing endpoint test

L_out =
diag(ell_out,ell_out),

viewed as a 2-by-4 matrix.

For any doubled transfer A, the true gate-free endpoint closure matrix is

C_end(A) = L_out A J_in.

Resonance requires

det C_end(A)=0.

This replaces the artificial condition det(I-A)=0 whenever the doubled state is closed by endpoint graph lines rather than literal equality of the two carried sheets.

## 5. Matched defect endpoint closure

Take A=K, the matched defect scattering insertion from series-38.

Outward interval arithmetic gives

-0.042475
<
det C_end(K)
<
-0.042458.

Hence the matched defect insertion remains nonresonant after imposing the actual endpoint graph subspaces.

This is stronger than the earlier det(I-K) test because it uses the physical gate-free endpoint closure.

## 6. Matched defect plus bulk propagation

Take

A_n = K B4^n,

where

B4=diag(M0,M0).

For every admissible

0 <= n <= 15,

outward interval arithmetic gives

det C_end(A_n) != 0.

The smallest absolute margin occurs at n=0 and is greater than

0.04245.

Representative certified intervals are:

n=0:
-0.042475 < det C_end(A_n) < -0.042458;

n=1:
-0.72061 < det C_end(A_n) < -0.72059;

n=2:
2.83018 < det C_end(A_n) < 2.83026.

For n>=3 the absolute determinant is greater than 10.

Thus no admissible amount of pure bulk propagation can tune a matched k-scattering event into gate-free endpoint-line resonance.

## 7. Gated terminal endpoint graph

The true remaining endpoint condition appears when the terminal k-gate is active.

Series-34 gives

S(x)
=
R^(-1) X(x)
-
(beta/delta) S(x+k).

Therefore, on the doubled state

W =
(X(x),S(x),X(x+k),S(x+k)),

the terminal condition is

S(x)
-
R^(-1) X(x)
+
(beta/delta) S(x+k)
=
0.

Equivalently the endpoint row is

(-R^(-1), 1, 0, beta/delta).

This is the gated endpoint graph registered in the terminology file.

The gate-free line L_out is recovered exactly when the translated-sheet term is absent.

## 8. Meaning for endpoint closure

The endpoint problem is no longer an unspecified carried identity sheet.

There are now two explicit closure types:

1. gate-free endpoint graph line:
   S=R^(-1)X;

2. gated endpoint graph:
   S-R^(-1)X+(beta/delta)S_k=0.

All gate-free endpoint closures in the currently extracted bulk/matched-scattering library are nonresonant with explicit margins.

Therefore any remaining endpoint failure must use the gated endpoint graph or the simultaneous two-cycle case-B closure.

## 9. Scope of the result

This pass repairs the specific n=0 bookkeeping degeneracy left by series-39.

It also proves gate-free endpoint-line nonresonance for:

- pure bulk words M0^n;
- one matched k-scattering insertion K;
- K followed by any admissible doubled bulk power.

It does not yet enumerate every separated E_plus/E_minus word with endpoint graph rows, because the actual endpoint gate may switch on between the two shears.

It also does not close the case-B two-cycle system.

## 10. Quantitative status

The gate-free endpoint library has explicit fixed-scale margins:

pure bulk endpoint-line closure:
absolute determinant > 0.4968;

zero-bulk unmatched endpoint closure:
determinant > 15/196;

matched endpoint closure:
absolute determinant > 0.04245.

Thus no gate-free endpoint atom is close to singular for the exact Weil weights.

No uniform estimate for gated endpoint closure is yet proved.

No shrinking-collar estimate follows.

## 11. Fixed-L injectivity status

The globally load-bearing experimental injectivity range remains

0 < L <= log(16/3).

Post-log(16/3), the following failure modes have now been excluded:

- local defect/overlap singularity;
- pure bulk monodromy;
- matched one-k scattering resonance;
- separated one-k scattering resonance without endpoint gating;
- zero-bulk unmatched identity-sheet artifact;
- gate-free endpoint-line resonance.

The remaining obstruction is:

gated endpoint graph closure
and simultaneous two-cycle closure.

## 12. General prime-channel architecture

The transfer architecture can now be stated with endpoint data included:

- bulk state V=(X,S);
- bulk transfer M0;
- unmatched gate shears E_plus,E_minus;
- matched insertion K;
- local defect solves D0,D1,P0,J0,T0;
- entrance graph L_in;
- gate-free terminal graph L_out;
- gated terminal graph in the doubled state.

Fixed-L injectivity is therefore a finite endpoint-subspace transversality theorem.

No new source-level threshold proof is needed.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-41 / GATED ENDPOINT CLOSURE

The next pass should:

1. compute the closure determinant when the terminal row
   (-R^(-1),1,0,beta/delta)
   is active;
2. propagate that row through E_plus, E_minus, K and bounded powers of B4;
3. enumerate the finite gated endpoint word family;
4. then assemble the simultaneous case-B two-cycle closure matrix.

A successful pass would leave only the coupled two-cycle determinant, or possibly finish the fixed-L four-delay prime-channel injectivity theorem.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
