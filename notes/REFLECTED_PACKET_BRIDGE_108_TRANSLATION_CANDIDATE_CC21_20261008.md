# RPB108 CC21: arithmetic translation candidate, whole-shell generation and phase obstruction

2026-10-08 UTC. Recovered Coupled CC20
`41ec534960cc1dd5336739193899a352af83097f` and paused Global NF71
`6ed350cb6736993fa9801bce9ab15f096c10c200`. Coupled remains the sole active
integration frontier. [Definitions](../docs/TERMINOLOGY_RPB108_TRANSLATION_CANDIDATE.md)
precede use. This is a stage-two candidate test for CC20's actual forced
covariance, not another independent global investigation.

**A: an actual absolute estimate and a whole-input construction.** The
exact divisor translation law gives a cap-uniform O(r) increment after
common ordinate-phase compensation. A fixed smooth two-window partition
also constructs a bounded right inverse generating the ENTIRE incoming
source shell, with a constant independent of the old signed gap.

**C: the boost-only continuation candidate fails.** A common unitary phase
cannot be removed when comparing an old positive range with its translated
image. It leaves a complete phase/gain commutator. The absolute transverse
bound controls neither its critical defect weight nor the full relative
reaction. A finite pair-law control has a uniformly protected positive
inverse and diverging critical weighted cost. This refutes the proposed
structural inference, not an inequality exploiting the actual infinite
zeta dictionary. No actual zeta critical covariance is evaluated.

## 1. Candidate and the exact actual arithmetic estimate obtained

Use tau_r h(x)=h(x-r) and the normalized complete p_q,n_q from CC20.
The actual divisor identity, already recorded in EXTERNAL_SEVEN_EIGHTHS
and SOURCE_HEIGHT_GRAPH_ERROR, is

    p_q(tau_r h)=exp(i theta_q r)[cosh(beta_q r)p_q(h)
                                      +sinh(beta_q r)n_q(h)],
    n_q(tau_r h)=exp(i theta_q r)[sinh(beta_q r)p_q(h)
                                      +cosh(beta_q r)n_q(h)].

Retain every multiplicity copy. Partner reflection leaves theta unchanged,
changes beta to -beta, keeps p and negates n. Thus U_r preserves the
partner-even positive and partner-odd negative source spaces. C_r preserves
them and S_r maps one into the other. This is an operator statement on
the complete square-summable source carrier, not a finite-height packet.

The accepted external strip gives abs(beta_q)<=b=3/8. It is inherited in
its published scope; no new external proof replay or Lean audit is claimed.
For the joint Gamma=(P,N), the hyperbolic block has norm at most exp(b|r|)
and preserves the signed source metric. Therefore

    ||Gamma(tau_r h)||<=exp(b|r|)||Gamma(h)||,
    ||Gamma(tau_r h)-U_r Gamma(h)||
             <=[exp(b|r|)-1]||Gamma(h)||.          (1)

The second is a genuine OLD-GAP-INDEPENDENT arithmetic absolute bound,
valid on every fixed cap for translated supported vectors that remain
inside it. All mixed entries and both source channels are included.
It applies before any null equation, and it holds for positive eigenmodes.
The per-row identity also gives Q(tau_r h,tau_r f)=Q(h,f).

The tested candidate was to use (1), positive observability and CC20's
protected positive inverse to obtain a relative incoming cost below one
for a fixed shell width independent of the old signed gap. The following
calculation identifies why that inference fails.

## 2. Whole-shell generation, without a trial-span assumption

Let a0=21/20 be the certified anchor, s>=a0, t=s+h<=B and
0<h<=a0/4. On D_t choose a fixed smooth partition chi_-+chi_+=1,
where chi_-=1 for x<=-a0/4 and chi_-=0 for x>=a0/4. It depends on
the anchor, not on s, h, the old defect or a target positive gap.
For the canonical norm estimates multiply these functions by one fixed
smooth compact cutoff equal to one on [-B,B]. The existing logarithmic
weighted convolution bound then gives a finite K_chi,B such that

    ||chi_- f||_D^2+||chi_+ f||_D^2<=K_chi,B||f||_D^2.

Translation is unitary in this full-line Fourier energy norm. Set

    h_-=tau_h(chi_- f), h_+=tau_-h(chi_+ f).

The supports are respectively inside [-s,a0/2] and [-a0/2,s],
so BOTH vectors belong to the entire original D_s. Their sum translates
back EXACTLY to f=tau_-h h_-+tau_h h_+. No boundary regularity or global
H1 requirement is used. Multiplication preserves the canonical domain.

For w in W_st put f=P_t^-1 w and p_-=P_s h_-, p_+=P_s h_+.
Define A_r:V_s->W_st by

    A_r p=(I-Pi_s)P(tau_r P_s^-1 p), r=+h,-h.

Then the bounded linear map R_h w=(p_-,p_+) satisfies

    [A_-h,A_+h] R_h=I_W,
    ||R_h||^2<=kappa_B=C_B^2 K_chi,B/c_B^2.        (2)

Here c_B,C_B are the cap bounds for COMPLETE positive analysis. They
exist in the inherited analytic observability theorem; CC21 does not
claim evaluated optimized values. The construction uses the protected
positive inverse only, and its bound is independent of the old signed
gap. Thus checking a WHOLE translated-old-domain operator can now
control the WHOLE incoming shell. Checking finitely many old trial
vectors still cannot do so.

This resolves the coverage premise for this candidate. It does not
establish any signed arithmetic suppression.

## 3. Exact translation residual and its phase/gain commutator

Let Ttilde=T_s Pi_s on the entire positive source ambient. For p in V_s
the complete negative source of the translated shell increment is

    F_r p=N(tau_r P_s^-1 p)-T_s Pi_s P(tau_r P_s^-1 p)
          =K_st A_r p.

Using the actual pair law, with source parities explicitly typed,

    F_r=U_- S_-+ +U_- C_- Ttilde
                       -Ttilde U_+(C_+ +S_+- Ttilde) on V_s. (3)

Subtract its pure-phase commutator H_r=U_- Ttilde-Ttilde U_+.
The remaining three terms are

    U_- S_-+ -Ttilde U_+ S_+- Ttilde,
    U_-(C_--I)Ttilde-Ttilde U_+(C_+-I).

With g_s=||T_s||<1, the exact absolute estimate is

    ||F_r-H_r||
       <=(1+g_s^2)sinh(b|r|)+2g_s[cosh(b|r|)-1]
       <=2[exp(b|r|)-1].                         (4)

Equation (4) retains the missing phase term; it does not set it to zero.
Although U is the SAME actual ordinate phase in both channels, it acts
before and after Ttilde in different terms. It generally changes V_s
and need not commute with either Pi_s or the gain map. Its unitary norm
does not imply a small commutator on the critical range.

The complete positive ambient already has unbounded actual ordinates.
For a copy with theta_q tending to infinity, choose r_q=pi/abs(theta_q).
On its positive partner block ||U_rq-I||=2 while r_q tends to zero.
Hence no operator-norm O(r) bound on the entire positive phase ambient
follows from actual zero counting and strip width. This is an actual
analytic observation, using the unbounded actual divisor, not invented
numerical zeta ordinates.

This ambient observation does NOT prove the same failure on V_s or on
a critical physical source combination: an isolated coordinate is not
a complete compact physical packet. A sharper arithmetic range estimate
could control H_r there. Its proof is exactly the extra input the tested
candidate lacks. Strong continuity on fixed square-summable packets
supplies no rate uniform over a moving near-critical family.

## 4. Connection to the specified forced covariance and the strict budget

Let F=[F_-h,F_+h]. From the whole-source identity and (2),

    K_st=F R_h,
    L L*=Ecrit F R_h R_h* F* Ecrit.               (5)

All mixed products between the two translated branches remain in (5).
It is the SAME actual covariance as CC20's
Lambda^-1/2 J M_t^-1 J* Lambda^-1/2, not a replacement gain dictionary.
For a critical output y_i, (3) paired with y_i equals
-J_i(tau_r P_s^-1 p)/sqrt(lambda_i).

An independently proved sufficient arithmetic template for this route is

    kappa_B ||G^-1/2 Ecrit F||^2<=q,
    (kappa_B/eta)||Elow F||^2<=ell,
    q+ell<1.                                    (6)

The low-output inverse is protected at eta; the band/rank protection must
remain independently valid. Equation (6) bounds the full direct-sum
operator, including every old vector. It is a sufficient upper template,
which can be stronger than the exact correlated expression (5).
The scalar kappa bound lawfully pays all mixed R_h products; no cross
term is declared zero. The minimal arithmetic target remains CC20's (5).

Replacing the full F by separate norms in (4) produces at best a term
divided by min spectrum G. Even granting an O(r) absolute commutator
would not by itself make that bound independent of the old gap. A step
forced to shrink with that gap supplies no non-stalling exit. The strict
covariance in (6), including its joint cancellations, is not established.

## 5. Exact pair-law control of the failed candidate

This control is a finite source system with the exact pair translation
law. It is NOT actual zeta data, an actual explicit formula, or a complete
physical translation representation. It audits the claimed source-algebra
inference. The genuine differential/logarithmic crossing proofs from CC19
remain the separate physical operator controls.

In two partner-orbit source coordinates set

    p_old=(1,1), n_old=(a,0), 0<a<sqrt(2),
    U=diag(1,-1), R=exp(beta r),
    c=(R+R^-1)/2, sboost=(R-R^-1)/2.

To realize full partner-copy signs, duplicate each positive coordinate
and duplicate each negative coordinate with opposite sign, using the
isometric 1/sqrt(2) embedding. This preserves the complete source norms,
historical parity law and every mixed pairing. It does not invent zeta
locations or multiplicities. Relative phases 1,-1 can represent two
arbitrarily separated heights; their common scalar phase is immaterial
to the cost and can be absorbed into the translated control column.

The old gain eigenvalue and defect are lambda=a^2/2, delta=1-lambda.
The law gives translated sources

    p_new=(c+sboost*a,-c),
    n_new=(sboost+c*a,-sboost).

Both positive source columns are independent. On their two-dimensional
declared coefficient carrier the positive Gram satisfies I<=M<=7I
whenever 1<R<=3/2 and the Pell choices below are used. Its inverse is
uniformly protected as delta decreases. Both original diagonal energies
equal2delta, but their original mixed entry is -c a^2.

Subtract the old positive projection. Put A=c+sboost*a/2. The shell's
positive source is A(1,-1), with norm squared2A^2; its negative source is

    (c*a+sboost*delta,-sboost).

Therefore its exact critical and low-output costs on a unit positive
shell vector are

    critical=(c*a+sboost*delta)^2/(2A^2 delta),
    low=sboost^2/(2A^2).

The full cost exceeds one in the tested family. Choose Pell rationals
a=p_j/q_j, p_j^2-2q_j^2=-1, so delta=1/(2q_j^2), and R=1+2^-j.
The compensated boost tends to zero, the positive metric stays uniformly
protected, and the critical weighted cost tends to infinity. Its pure
phase commutator has squared norm lambda on the old unit source direction.
The exact CC20 forced covariance is independently checked to equal
lambda times the unweighted critical shell leakage.

Thus strip-bounded boost, a small compensated increment and a protected
positive inverse do not supply the proposed relative bound. None of
these controls is said to match the remaining complete zeta correlations,
zero-density theorems or canonical physical carrier. Their role is the
specific algebraic method obstruction; they do not show actual zeta
non-stalling is false.

## 6. Positive-level discrimination and inherited controls

For the original P=I, N=(9/25,12/25) control the original lowest physical
level is mu=16/25>0 and original incoming cost9/34<1. The shifted negative
analysis is (N,sqrt(mu)I), including the ENTIRE physical mass channel.
Its critical eigenvalue and old defect change; its critical and low-output
costs sum to exactly1. The shifted physical Schur block is zero while the
original form is positive.

The mass channel has its own physical translation action; it is not a
divisor pair with an assigned beta. A shifted version of (3) must
recompute Ttilde, Ecrit, G and the entire extra mass residual. Reusing
the unshifted commutator or discarding those rows gives the wrong test.
Equation (1) for actual divisor sources continues to hold on an original
positive eigenmode and therefore cannot distinguish zero from its positive
level by itself. The original mass distinction stays explicit.

The existing CC19 genuine differential and canonical logarithmic controls
still reach original contact with bounded complete sources. The new
candidate supplies no hypothesis that excludes those crossings. Their
inherited analytic proofs are not replaced by the finite pair model.

## 7. Validation, scope and staged exit

**13,996 exact checks pass:** 2,688 new checks and all11,308 CC20 checks
replayed. New checks include2,016 Gaussian-rational complete pair
translation/mixed/sign/norm checks,640 checks of40 approaching-critical
phase controls,27 whole right-inverse/covariance controls and5 full
positive-level mass checks. The mixed covariance is checked directly
against the independently constructed complete coefficient Schur form
and the CC20 forced positive-inverse expression. No floating values enter.

The cap-wide smooth partition, full mixed-series passage and actual phase
ambient observation are analytic. The finite frame tests certify the
right-inverse algebra, not a numerical whole zeta frame constant. No new
Lean proof, effective cap margin, source cutoff, critical zeta vector,
actual phase/gain commutator or arithmetic relative covariance is evaluated.

Stage two now has a CONCRETE tested candidate and a precise rejection:
bounded transverse boost after phase compensation does not close the
critical relative budget. The whole-shell generation premise is resolved
analytically. Any subsequent arithmetic attempt must bound the ACTUAL
whole commutator/residual covariance in (5)-(6) or the equivalent CC20
forced covariance, using a new justified property of the complete divisor
range. Another change of coordinates, strip constant improvement, fixed
source-prefix calculation or generic continuity bound is insufficient.

The phase-compensation shortcut stops here. Its obstruction does not
authorize repeated conditional reformulation as a closure claim. The
certified whole-domain anchor remains21/20, even0 / odd0. No all-cap
gain, accumulated finite-cap loss, non-stalling, RH/F4 or Lean closure.
Coupled publication is additive; Global NF71, the other paused branches
and all historical wording/certificates remain unchanged.
