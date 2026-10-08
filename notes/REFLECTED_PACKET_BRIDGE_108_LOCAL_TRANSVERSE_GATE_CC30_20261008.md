# RPB108 CC30: the local transverse density shortcut contains Lindelof

Date: 2026-10-08 UTC. Parent: 3fe64929ae5030f3fe8fbdc2f181c3c15b3db408.
Definitions: [local transverse gate](../docs/TERMINOLOGY_RPB108_LOCAL_TRANSVERSE_GATE.md).
Scope: arithmetic premise audit. No actual shell covariance upper bound,
new aperture, new independent frontier, or Lean proof.

## Finding

The proposed upgrade of the existing cumulative transverse density bound
to an every-height local sampling bound conceals an open hypothesis.
For the complete actual zeta location measure,

    S2(T)=o(log T) as real T->infinity

is equivalent to the Lindelof hypothesis. The proof below identifies the
cost of this particular premise; it does not prove that every possible
arithmetic shell estimate must first establish Lindelof.

Even granting that premise supplies no old-defect factor in the surviving
finite-height correlations. The CC29 target remains

    E_s(A_t-A_s)E_s <= C_B omega_B(G_s),  omega_B(x)->0,

with cap-only fixed band and positive step. A local location estimate is
not an evaluation of this complete adaptive covariance.

## 1. External theorem and unconditional count

Backlund's criterion is that, for EVERY fixed epsilon>0, the number of
zeros with Re(rho)>1/2+epsilon in [T,T+1] is o(log T), with multiplicities.
It is equivalent to Lindelof. Sources read in this pass:

- Terence Tao, 254A Supplement 7, 2015-03-01, Theorem 2 and its proof:
  https://terrytao.wordpress.com/2015/03/01/254a-supplement-7-normalised-limit-profiles-of-the-log-magnitude-of-the-riemann-zeta-function-optional/
- Jorn Steuding, Sampling the Lindelof hypothesis with an ergodic
  transformation, RIMS Bessatsu B34, section 5, printed page 372;
  it attributes the criterion to Backlund, 1918/19:
  https://www.kurims.kyoto-u.ac.jp/~kenkyubu/bessatsu/open/B34/pdf/B34_021.pdf
- The Analytic Number Theory Exponent Database, growth chapter,
  Lemma 6.15, states the corresponding growth-exponent version:
  https://teorth.github.io/expdb/blueprint/zeta-growth-chapter.html

Only the criterion is imported. No proof of Lindelof or independent
reformalization of Backlund is claimed. Tao's original proof exposition
and Steuding's research article were checked, not only a search snippet.

The unconditional total unit-height count is O(log T). For example,
Trudgian, arXiv:1208.5846v2, Corollary 1, bounds the error in N(T) by
0.111 log T+0.275 log log T+2.450+0.2/T0. Subtract its bounds at two
endpoints and the differentiable main term to obtain O(log T).
Endpoints containing zeros can be enclosed in a slightly larger interval;
the same order holds, including multiplicity. We do not use the incorrect
unconditional unit-height asymptotic sometimes inferred by subtracting
an O(log T) error term.

https://arxiv.org/pdf/1208.5846

## 2. Exact equivalence for the second transverse mass

Write beta=Re(rho)-1/2. The classical critical strip gives |beta|<=1/2,
so this argument does not require the separately accepted narrower strip.
The inherited normalized source dictionary may repeat reflected channels
by a fixed factor; keep all copies, and absorb only that fixed factor in
the counting constants. At positive heights functional symmetry preserves
the ordinate and multiplicity while replacing beta by -beta.

If S2(T)=o(log T), every fixed epsilon>0 obeys

    epsilon^2 R_epsilon(T) <= S2(T).

Thus all the far-right local counts are o(log T), and Backlund gives
Lindelof. Strict versus non-strict horizontal thresholds are immaterial:
one can replace epsilon by epsilon/2. For ordinate endpoints, cover the
closed window with two half-open unit windows. All statements here hold
as the REAL height tends to infinity, not merely along selected heights.

Conversely assume Lindelof and fix epsilon>0. Split the same complete
unit-height sum into |beta|<=epsilon and |beta|>epsilon. The unconditional
total count bounds the first part by C epsilon^2 log T. Reflection and
Backlund bound the second part by (1/4) times o(log T). Hence

    limsup_(T->infinity) S2(T)/log T <= C epsilon^2.

Let epsilon decrease to zero AFTER taking the limsup. This proves local
transverse vanishing. No uniform-in-epsilon Backlund rate is assumed,
and the result provides no effective decay rate by itself.

This is a classification of an arithmetic premise, not another reformulation
of the shell target. Neither implication from Lindelof to the shell target
nor implication from the shell target to this local statistic is asserted.

## 3. Cumulative density does not furnish the local premise

CC22 retains the actual cumulative bound

    Z2(T) << T (log log T)^2/log T.

Its primary input, Chourasiya--Simonic arXiv:2507.15184v2, Corollary 1,
was checked again. That is a count up to height T, not a bound on its
increment in every unit interval. Subtracting two cumulative UPPER
bounds does not bound the increment by their difference.

For an exact location-only control, choose b=1/8, T_j=2^(2^j), and
m_j=2^j for j>=J. At each positive height T_j put m_j copies at each
of beta=+b and -b, and include their conjugates at negative height.
J can be chosen beyond any prescribed finite verification height.

Through T_j the complete transverse mass is

    4 b^2 sum_(k=J..j) 2^k < 8 b^2 2^j = O(log T_j).

Between clusters it remains O(log T). This is much smaller than the
CC22 cumulative allowance for sufficiently large T. The far-right
cumulative count is likewise O(log T), so it fits the displayed Ingham
upper bounds asymptotically. The local total count is O(log T) too.
But the unit window containing T_j has transverse mass 2 b^2 m_j,
and therefore

    S2(T_j)/log T_j = 2 b^2/log 2 > 0.

The local premise fails. These artificial locations are NOT an actual
zeta divisor, a native-form countermodel, or an independence theorem.
CC25's rigidity audit remains in force: one may not attach an artificial
dictionary to the unchanged complete actual explicit formula.

## 4. Genuine crossing and positive-level tests

Granting a local tail premise still leaves every finite source prefix.
Any finite off-line dictionary satisfies the local asymptotic premise
trivially, with no constraint on its finite critical correlations. This
observation is about information content, not an actual zeta example.

The inherited genuine H01 differential form has compact negative
observation H01->L2 on each finite cap, yet crosses at pi/2. Its exact
critical leakage is 2u(v-u). At fixed v=1+1/16 it tends to 1/8 as u->1,
while the old defect 1-u^2 tends to zero. Thus even uniform finite-rank
approximation of negative observations would not by itself imply a
vanishing-defect shell bound. This is a control against the proposed
transfer, not a counterexample to the complete arithmetic Weil identities.

The full positive-level control is also retained: P=I,
N=(9/25,12/25), mu=16/25. Original shell cost is 9/34<1. Adding the
ENTIRE physical mass channel sqrt(mu)I for Q-mu I gives old gain
481/625, defect 144/625, and critical plus low cost exactly one.
No tail statement distinguishes that original positive level from zero.

The unchanged minimal input for CC29 is still the complete joint
forced-source covariance estimate, tested on ALL critical coefficient
combinations in the protected positive metric. Height-local sparsity
neither supplies its defect dependence nor controls the changed positive
projection in the phase/gain commutator.

## 5. Validation, custody, and decision

All 24,987 exact checks pass: 115 new and 24,872 inherited from CC29.
The validator replays CC29 and adds exact finite split, sparse-cluster,
finite-prefix, genuine-crossing, and full-mass controls. These are rational
checks of the stated inequalities, not data about actual critical zeta
vectors. The equivalence in section 2 is an analytic argument conditional
only on the imported classical counting criterion and unconditional count.

Decision: do not promote an every-height local sampling premise to an
available arithmetic input, and do not start another generic compactness
front. This targeted shortcut has now been priced as Lindelof, with a
remaining independent finite-correlation gap even if it were granted.

Original whole-domain positivity stays internally certified through
21/20, even0/odd0, physical margin 1/(3*10^63). RH/F4, reusable
continuation, retained attachment and Lean closure remain open. Global
stays paused at NF71; Aperture and Pre-Contact Shadow stay paused.
