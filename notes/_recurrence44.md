# SZ edge recurrence 44 — p-defect relay audit

Date: 2026-09-27
Branch: sz-cross-collar
Status: UNRATIFIED RESIDUE / NF PASS
Canonical parent: SZ-CROSS-COLLAR-3
Immediate residue: series-43
Public promotion: forbidden

## Objective

Carry out the finite causal-path certification promised by series-43.

The certification cannot yet be executed globally because a load-bearing domain audit exposes one omitted boundary state.

The three-sheet K_r recurrence is exact on the P/J common-overlap domain where series-34 derived it. It does not automatically propagate through the full lower defect.

The missing object is the p-defect relay.

The repair is favorable: the relay is triangular and nilpotent, so it introduces no new delay lattice. But it must be included before any globally complete path enumeration can be valid.

No new fixed-L injectivity interval is claimed in this pass.

## 1. Domain of the finite-tap transfer

Series-34 derived

V(x+h)
=
M0 V(x)
+
1_(x<alpha) c_plus S(x+k)
-
1_(x>k-h) c_minus X(x-(k-h))

only on the P/J common-overlap interval

e-h < x < min(u-h,p).

Here

u=p+e.

Therefore:

if 0<e<h,

the overlap starts at the left endpoint and runs to u-h<p;

if e>=h,

the overlap starts only at x=e-h and runs to p.

In particular, when e>h the lower interval

0 < x < e-h

is not governed by the K_r recurrence.

Series 42-43 treated the stacked K_r/causal-lag system as globally complete on the whole head. That extrapolation is not justified by the derivation.

The K_r atom library remains correct on its overlap domain.

The global completeness claim must be repaired.

## 2. Exact lower-defect equations

Use the exact compact equations from series-32/34.

For 0<t<e,

delta S(t)
=
mu X(j+t)
-
G X(t)
-
beta S(k+t),

and

G S(t)
=
mu X(p+t)
-
delta X(t)
+
mu 1_(t<e-h) S(j+t)
-
beta 1_(t>k) X(t-k).

Define the p-defect relay

P(t)=X(p+t),

Q(t)=S(p+t),

0<t<e.

Since

j=p+h,

one has

X(j+t)=P(t+h),

S(j+t)=Q(t+h)

whenever t+h<e.

## 3. Relay propagation strip

For

0<t<e-h,

both shifted relay values remain inside the p-defect strip.

The exact equations become

mu P(t+h)
=
G X(t)
+
delta S(t)
+
beta S(k+t),

and

mu Q(t+h)
=
G S(t)
-
mu P(t)
+
delta X(t)
+
beta 1_(t>k) X(t-k).

Thus

D(t+h)
=
N D(t)
+
F_base(t),

where

D(t)=(P(t),Q(t))^T,

and

N =
[ 0   0 ]
[-1   0 ].

Therefore

N^2=0.

The p-relay has nilpotent internal memory.

P(t+h) is determined directly by the base k-stack.

Q(t+h) sees the current scalar P(t), but Q(t) itself never feeds forward through the relay.

There is no independent p-lattice.

## 4. Relay terminal strip

For

max(0,e-h)<t<e,

the indicator 1_(t<e-h) vanishes.

The second lower-defect equation becomes the terminal p-relay constraint

mu P(t)
=
G S(t)
+
delta X(t)
+
beta 1_(t>k) X(t-k).

Thus the last h-width of the p-relay is not propagated; its P-coordinate is solved directly from the base state.

The first lower-defect equation on the same strip determines the post-defect value

X(j+t)
=
[
G X(t)
+
delta S(t)
+
beta S(k+t)
]/mu.

That value lies outside the p-relay strip and belongs to the next already-reconstructed H-region.

So the relay has an exact entrance/propagation/terminal decomposition.

## 5. Terminal-tail interpretation of Q

Recall

ell=s+u=s+p+e.

Therefore

s+p=ell-e.

Hence

Q(t)
=
S(p+t)
=
H(s+p+t)
=
H(ell-e+t).

So Q is exactly the terminal e-width tail of H.

The relay is therefore not an artificial auxiliary copy.

It is the finite bridge between the lower defect and the physical terminal H-tail.

This explains why omitting it prevents a complete endpoint path certification.

## 6. Memory depth

Because N^2=0, the relay's dependence on free relay data has depth one.

More explicitly:

- P on t>h is determined directly by the base k-stack at t-h;
- Q on t>h depends on P one h-step earlier;
- Q does not propagate onward through the relay.

Thus only the initial relay strip

0<t<min(h,e)

can carry independent P-data before the base forcing takes over.

There is no growth of state dimension as e increases.

## 7. Corrected global state

The globally complete local bookkeeping for the four-delay chamber must contain:

1. the base k-sheet stack
   V(x), V(x+k), V(x+2k)
   when present;

2. the p-defect relay
   P(t)=X(p+t),
   Q(t)=S(p+t)
   on 0<t<e;

3. the P/J overlap transfer K_r on its exact domain;

4. the causal k-predecessor
   X(y-k)
   inside that overlap;

5. the terminal H-tail represented by Q.

At the scalar L2-fiber level this is still finite.

The newly restored relay is triangular/nilpotent, so it adds a finite boundary channel rather than another recurrence lattice.

## 8. Scope correction to series 42-43

The following results remain valid:

- the K_1,K_2,K_3 homogeneous scattering blocks on the P/J overlap;
- det K_r=1;
- the three-sheet support bound;
- the universal factorization K_r^(-1)b_r=-d_r;
- the strict causality of the k-predecessor;
- all determinant audits explicitly performed on valid bulk/scattering subfamilies.

The following claims must not be used globally without the p-relay:

- that K_r plus one causal lag is already a complete head recurrence;
- the 105 bare H/K path count as a complete source certification;
- the statement that series-43 reduced the entire four-delay problem to endpoint path sums involving only K_r and the k-lag.

The correct global certification must incorporate the p-relay entrance and terminal-tail maps.

## 9. Finite certification still survives

The audit does not restore an infinite problem.

The complete system has:

- at most three k-sheets;
- one p-relay of width e;
- nilpotent p-memory N^2=0;
- bounded h-depth;
- bounded k-depth;
- gate-free physical terminal endpoint.

Therefore the global source equation still folds into finitely many constant atom matrices on finitely many parameter chambers.

The missing work is to include the relay atom in that finite graph before performing determinant certification.

## 10. Fixed-L injectivity status

No new injectivity theorem is claimed.

The load-bearing continuous range remains

0 < L <= log(16/3).

The post-log(16/3) determinant audits remain useful positive evidence on the subfamilies they actually cover, but they do not constitute a global completeness proof.

## 11. Quantitative status

No new global singular-value floor is claimed.

Local quantitative facts retained include:

- all previously certified K_r and endpoint margins on their valid domains;
- eta<9/10 for the causal k-lag;
- exact nilpotence N^2=0 for the p-relay.

Nilpotence is stronger than a contraction estimate for the relay itself.

The shrinking-collar drilling interface remains untouched.

## 12. Strategic consequence

The common finite arithmetic-delay mechanism survives the audit.

The correct architecture is now:

base k-sheet scattering
+
one causal k-predecessor
+
one nilpotent p-defect relay
+
finite terminal matching.

This is still naturally extensible to later arithmetic thresholds.

The lesson is that every new overlap must be classified either as:

- a stacked translation sheet;
- a causal predecessor;
- or a finite boundary relay.

Only after all three are accounted for is a global path/determinant certification valid.

## Next frontier

Next target:

SZ-KERNEL-EDGE-GERM-45 / RELAY-ENDPOINT CLOSURE

The next pass should:

1. fold the nilpotent p-relay into the three-sheet atom graph;
2. identify the exact initial P-strip and terminal Q-tail boundary maps;
3. derive the complete entrance-to-terminal matrix including both k-causal paths and relay paths;
4. only then enumerate the finite parameter chambers and certify determinants.

A successful pass would restore a genuinely complete finite certification problem for the full four-delay chamber.

Canonical theorem cursor remains SZ-CROSS-COLLAR-3.

No public promotion and no canonical cursor movement are asserted.
