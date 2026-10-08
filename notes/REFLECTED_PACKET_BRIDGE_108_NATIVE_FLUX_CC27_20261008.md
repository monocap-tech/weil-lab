# RPB108 CC27: native exterior forcing and sign mechanism test

2026-10-08 UTC. Parent Coupled CC26
`d2a5b46dd5454fe2f214caa31f98ba6ba881f564`; paused Global NF71
`6ed350cb6736993fa9801bce9ab15f096c10c200`.
[Definitions](../docs/TERMINOLOGY_RPB108_NATIVE_FLUX.md).

The specific mechanism tested here is whether the OLD generalized
critical equation makes the native prime, archimedean and pole forcing
small through support localization or a common sign of its interactions.
This pass uses their actual coefficients. It rejects both the claim that
only newly admitted prime powers force the residual and the fixed-sign
premise of a direct sign-based cancellation argument. It does not reject
an unknown estimate exploiting the actual critical vectors jointly.
No new defect-relative arithmetic covariance bound is proved.

## 1. The exact arithmetic operator being tested

In the pinned mathlib Fourier coordinate, let

    a_arch(xi)=Re psi(1/4+i*pi*xi)-log pi,
    c_n=Lambda(n)/sqrt(n), ell_n=log n,
    m_+(h)=integral h(x) exp(x/2) dx,
    m_-(h)=integral h(x) exp(-x/2) dx.

On a supported cap t the original native mixed form is

    Q(h,f)=integral conjugate(Fourier h) a_arch Fourier f
      -sum_{log n<=2t} c_n integral conjugate(h(x))
                             [f(x+ell_n)+f(x-ell_n)] dx
      +conjugate(m_-(h)) m_+(f)+conjugate(m_+(h)) m_-(f).       (1)

The sum runs over prime powers. The factor is c_n, not 2c_n: the
2Lambda(n)/sqrt(n) cosine multiplier has two translations with half
its coefficient. The two pole moments are cross-paired; their diagonal
is not generally a nonnegative square. The established canonical-domain
extension of (1) is inherited. The local Lean native theorem is on its
specified Green carriers; CC27 does not extend its Lean statement.

For an actual old critical lift h_i, lambda_i=1-delta_i,

    J_i=A_i-Pi_i+C_i-delta_i M_i,
    J_i|D_s=0.                                                 (2)

The old equation imposes cancellation among the four full rows on D_s.
It neither sets their separate exterior values to zero nor gives a
bound on their exterior norm. For the full positive metric M_t,

    J M_t^-1 J* = sum_{r,u} X_r M_t^-1 X_u*,
    (X_1,X_2,X_3,X_4)=(A,-Pi,C,-Delta M).                     (3)

Thus all sixteen blocks, including native/source and prime/pole cross
blocks, participate in the required estimate. Computing just the four
diagonal blocks cannot test collective phase cancellation.

## 2. What the actual exterior kernel says

For smooth h,f with positively separated compact supports, local
archimedean renormalization and the -log pi multiplier have zero mixed
pairing. DLMF 5.9.16 with z=1/4+i*pi*xi and the substitution v=2u gives
Re psi(z) as a local renormalized constant minus

    2 integral_{u>0} exp(-u/2)/(1-exp(-2u))*cos(2*pi*xi*u) du.

Take the integral first with a positive lower cutoff. The cosine
translation formula then applies lawfully. Below the support separation
both translated mixed pairings vanish, so the cutoff can be removed;
the tail is integrable. This proves the off-diagonal archimedean density
is -exp(-|d|/2)/(1-exp(-2|d|)), with the stated normalization.
The pole cross pairing has kernel exp(d/2)+exp(-d/2).
Consequently the continuous part of the FULL native exterior kernel is

    C_off(d)=2 cosh(d/2)-exp(-d/2)/(1-exp(-2d)), d>0.           (4)

The remaining part consists of negative translation atoms -c_n at
+/-log n. Formula (4) is not a pointwise representation of the entire
singular archimedean kernel and is not used at d=0.

If y=exp(d), exact simplification gives

    C_off(d)=(y^3-y-1)/(sqrt(y)*(y^2-1)).                     (5)

The polynomial y^3-y-1 is strictly increasing for y>1 and has a unique
root there. Hence (4) changes sign exactly once. Its derivative is
strictly positive: the derivative of 2cosh(d/2) is positive, and that
of exp(-d/2)/(1-exp(-2d)) is negative. For exact rational evaluation
set r=exp(d/2)>1:

    C_off(2 log r)=r+1/r-r^3/(r^4-1).                        (6)

For example r=11/10 gives a negative value and r=3/2 a positive value.
Their displacement exponentials 121/100 and 9/4 are not integers;
sufficiently narrow bumps at those separations avoid every prime atom.
Continuity makes the corresponding full native mixed pairings have
these signs for nonnegative smooth bumps. These are actual native
arithmetic coefficients, not modified zero dictionaries.

## 3. The sign obstruction persists in both parity charts

Let g_epsilon be an even, nonnegative C-infinity bump supported in
(-epsilon,epsilon), normalized in L2. Write g_x(u)=g_epsilon(u-x).
For 0<x<y define even tests h=g_x+g_-x, f=g_y+g_-y and odd tests
h=g_x-g_-x, f=g_y-g_-y. Their supports are disjoint for small epsilon.
In the absence of atoms at either separation, their mixed pairings
have the signs of, respectively,

    2[C_off(y-x)+C_off(y+x)],
    2[C_off(y-x)-C_off(y+x)].                               (7)

For even positive pairing choose x=2log(11/10), y=2log(13/10).
Both C_off values are positive by (6), with r=13/11 and 143/100.
For even negative pairing choose x=2log(21/20), y=2log(11/10).
The sum in (7) is negative by exact rational evaluation at r=22/21
and 231/200. Both pairs fit in the original anchor cap 21/20; their
separation exponentials are nonintegers, so narrow supports avoid atoms.
For odd tests at either of these atom-free pairs, strict increase of
C_off gives a negative pairing.

For a POSITIVE odd pairing choose x=log(5/4), y=log(8/5), so x+y=log2
and y-x=log(32/25). The direct separation is not a prime displacement.
The two opposite-sign reflected bump pairs align with the n=2 atom.
Their contribution to Q(h,f) is +2log2/sqrt2. All continuous cross
pairings are O(epsilon), since their supports stay separated and the
L1 product is O(epsilon). Other prime atoms are avoided. Thus Q(h,f)>0
for sufficiently small epsilon. The positive image atom is essential;
it cannot be removed by keeping just the positive half-window shifts.

These tests disprove a fixed off-diagonal sign, in either natural
parity cone of tests nonnegative on the positive half-window. They do
NOT disprove positive definiteness: a positive matrix may have mixed
entries of both signs. They are not critical eigenvectors, and (7)
is not an evaluation of J or its defect-relative covariance. A more
specific constraint on actual critical vectors could still supply
cancellation. Such a constraint has not been derived from (2).

## 4. Already-active prime powers can force the new strip

Consider s=21/20, t=53/50. The entire right-limit prime set is identical
at these two caps: {2,3,4,5,7,8}. Exact Taylor upper and lower bounds
for exp(2s) and exp(2t) place both between8 and9. Thus the newly admitted
prime shell is empty, without any threshold ambiguity.

Choose epsilon=1/200 and a much narrower smooth nonnegative bump h
centered at s+epsilon-log2, and f its translate by +log2, centered at
s+epsilon. The old h fits strictly in (-s,s), while f lies strictly
in (s,t). Normalize h,f in L2. The n=2 old prime term in (1) is
EXACTLY -log2/sqrt2; its reverse orientation has disjoint supports.
No other prime shift aligns if the bump is sufficiently narrow.
The archimedean-plus-pole pairing is O(bump width), so the full native
mixed pairing is nonzero for small width. Both orientations and the
full native pole remain included in this computation.

This is a counterexample to a proposed SUPPORT IDENTITY saying old-to-new
native forcing consists only of newly admitted prime powers. It is not
a counterexample to the critical covariance estimate. A critical h_i
is selected by the old equation, and f is not asserted to be a source-shell
lift; that lift has an interior correction. Already-active translations
must nevertheless remain in any lawful estimate of the actual row (2).
The old annihilation J_i|D_s=0 cannot be applied to this exterior f.

## 5. What the available boundedness estimate actually gives

Let U_B bound the full native form on the canonical logarithmic domain,
and c_B,C_B be the inherited positive observability constants. The
positive images P h_i are orthonormal. For every coefficient vector a,

    ||sum_i a_i h_i||_D <= ||a||/c_B,
    ||sum_i a_i J_i||_{D_t*}
           <= (U_B/c_B+delta_max C_B)||a||.                 (8)

The separate archimedean logarithmic form, finite prime translations and
bounded pole moments supply such a cap-only U_B. Inserting the protected
M_t^-1<=c_B^-2 I yields only a cap-only bound on unweighted covariance.
With m=min_i(lambda_i delta_i)>0, (8) gives

    ||(Lambda G)^(-1/2) J M_t^-1 J* (Lambda G)^(-1/2)||
       <= (U_B/c_B+delta_max C_B)^2/(c_B^2 m).              (9)

This estimate loses the old defect. Its right side grows as the defect
collapses; the ACTUAL covariance is not asserted to grow. The sign and
support tests above establish precisely why two proposed simplifications
of the native terms are invalid. They do not establish that every use of
the exact arithmetic identities must incur (9).

The missing result remains a joint estimate of the actual generalized
critical residuals, in the full M_t^-1 metric, with a lambda_i delta_i
factor and a strict cap-only reserve. The complete identities fix the
arithmetic but the current proved estimates do not quantify that transfer.
No formal logical independence or impossibility theorem about the full
Weil identities is claimed.

## 6. Required discrimination controls and scope

The genuine differential crossing from CC19/20 has u=2s/pi,
lambda=u^2, delta=1-u^2. At enlarged v,

    J M_t^-1 J* =lambda*2u(v-u).

At genuine contact v=1 its defect-relative critical cost is2u/(1+u),
which tends to1. For a fixed step v-u>0 that cost diverges as u tends
to1. Therefore a generic cancellation argument using only an old weak
eigen-equation, protected positive metric and support growth cannot
provide the desired uniform reserve. This differential control does
not reproduce the native prime/archimedean/pole coefficients.

For the full positive-level control P=I, N=(9/25,12/25), the original
lowest physical level is16/25. The original whole budget is9/34<1.
Shifting by that level adds the entire (4/5)I mass channel. The shifted
old gain is481/625, its defect144/625; critical plus low budget is1.
A shift changes the diagonal physical mass term, so the off-diagonal
kernel tests alone cannot distinguish original positivity from shifted
contact. The full diagonal, low output and full physical mass must be
retained. The validators replay these genuine crossing/full-mass controls.

24,604 exact checks pass: 50 new checks and 24,554 inherited CC26 checks.
The new rational checks verify (5)-(7), the empty new-prime-shell support
certificate, both image-atom signs, and all sixteen covariance blocks.
Smooth-bump limiting arguments and the digamma off-diagonal derivation
are analytic proofs in this note, not Lean-certified or proved by samples.
No actual critical vector or complete J covariance is numerically evaluated.
The new positive-source frame bound sought by the user is not certified.

Original whole-domain anchor stays21/20 even0/odd0, joined PHYSICAL margin
1/(3*10^63), not a numerical source defect. No new aperture. RH/F4,
retained attachment, reusable continuation, accumulated finite-cap loss
and Lean closure remain open. Coupled alone advances; Global, Aperture
and Pre-Contact Shadow stay paused. Further work needs a specific theorem
on mode-dependent covariance, rather than a sign or new-prime-shell shortcut.

## Source custody

Native source files: `ActualZetaNativeWeilForm.lean`,
`ActualZetaPrimeTransport.lean`, `ActualZetaCorrelationPoles.lean`,
`NeutralWeilMultiplier.lean`, `NeutralWeilPrimeShellTranslation.lean`.
`NeutralArchimedeanExterior.lean` explicitly labels its kernel definition
as not itself proving distribution attachment; CC27 supplies only the
separated-support analytic derivation above. No unattested attachment
is borrowed from that definition.

External formula: [NIST DLMF 5.9.16](https://dlmf.nist.gov/5.9.E16),
checked2026-10-08, Re z>0. This is the only new special-function input.
The arithmetic sign conclusions and residual estimates are our derivations.
No new zero-density or pair-correlation theorem is imported.
