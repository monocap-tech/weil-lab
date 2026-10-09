# RPB108 CC47 — Exact moment-zero gate with complete high response

Date: 2026-10-09 UTC. Publication base b57e217cf6f01381bf8a33d5335a84aeef7081f0.
[Definitions](../docs/TERMINOLOGY_RPB108_CONSTRAINED_SCHUR_CC47.md).
This supplies a finite-dimensional certificate target for the invisible
channel, NOT a evaluated new native certificate or an all-cap theorem.

## 1. Lawful form-domain high elimination

Work in either real parity sector and retain the complete original Q,
including both poles, all prime shifts and the archimedean form. Let E
be a finite physical-orthonormal trial space in D, and F=D intersect E-perp.
Assume C=Q|F satisfies C(y)>=kappa||y||_2^2 with kappa>0. The inherited
identity Q=E_log+R, ||R||<=r_B, implies

    ||y||_D^2<=C(y)+r_B||y||_2^2
               <=(1+r_B/kappa)C(y).                 (1)

Conversely C is bounded in the D norm. Thus C defines an equivalent
Hilbert form norm on the closed high carrier. The full mixed functional
Q(x,.) and the physical moment m(.) are continuous in it. Their form
Riesz vectors Wx and r exist uniquely, with

    C(Wx,z)=Q(x,z), C(r,z)=m(z), beta=C(r,r).         (2)

No claim is made that Q(x,.) has a physical L2 source representative,
or that the full logarithmic Weil operator is bounded on physical L2.
This distinction matters for the pending source/action Gram.

Write h=x+y=x-Wx+z. Completing the full high form square gives

    Q(h)=S(x)+C(z), S(x)=Q(x)-C(Wx),
    m(h)=a(x)+m(z), a(x)=m(x)-m(Wx).                (3)

Every cross term is included in W. It cannot be replaced by a diagonal
source envelope or by the raw low moment m(x).

## 2. Exact constrained rank-one correction

If beta>0, the moment-zero constraint m(h)=0 is equivalent to

    z=-a(x)r/beta+z0, m(z0)=0.

The two high components are C-orthogonal by (2), giving

    Q(h)=K_m(x)+C(z0),
    K_m(x)=S(x)+a(x)^2/beta.                       (4)

Consequently Q is strictly physically coercive on ker m if and only if
the finite gate K_m is positive definite, given the coercive high sector.
Necessity follows by taking z0=0; sufficiency follows by norm control.
For a quantitative bound, assume K_m(x)>=sigma||x||_2^2, sigma>0,
let w=||W||_(E,L2->F,L2) and A=||a||_(E,L2)*. Since ||r||_2<=sqrt(beta/kappa),
put L=1+w+A/sqrt(kappa beta). Then

    ||h||_2<=L||x||_2+||z0||_2,
    Q(h)>=gamma||h||_2^2,
    gamma=min(sigma/(2L^2),kappa/2)>0.             (5)

The formula is conservative; it is not a numerical defect or collective
source-frame reserve. When E is zero-dimensional the high bound alone
applies and no artificial finite eigenvalue is introduced.

If beta=0, (2) forces r=0 and m|F=0. Then a=m|E and the constraint is
m(x)=0. The exact gate is S restricted to that finite kernel, with z
unrestricted in F. Use the same norm argument with L=1+w. If the finite
kernel is {0}, all constrained vectors lie in F and kappa suffices.

On ker m the native pole terms vanish, so Q=H. A successful gate therefore
provides the physical moment-zero floor sought in CC44, whether or not
Q is positive on moment-carrying vectors. Scalar threshold contacts and
the collective defect-relative source-shell estimate remain separate.

## 3. Controls: constraint can help, but only with its actual response

Take physical Q=[[1,2],[2,1]], E=span e1,F=span e2. Here kappa=1,
W=2, S=-3. For m(x,y)=x-y, beta=1, a=3 and K_m=6>0; indeed the
constrained vectors (x,x) have Q=6x^2 although Q has a negative eigenvalue.
Using the raw low moment1 instead of the corrected moment3 gives a
wrong gate -2. For m(x,y)=x+y instead, a=-1 and K_m=-2: the constraint
does NOT save positivity. For Q=[[1,1],[1,1]], m=x-y, the computed gate
is4>0 and excludes the physical null (1,-1), which has nonzero moment;
for m=x+y the gate is0 and retains that moment-zero null.

If m|F=0, beta=0 and there is no rank-one correction. This singular case
is checked explicitly; taking a limit of a division by beta is unlawful.

Full physical mass-shift check: starting from Q=[[1,2],[2,1]] and m=x-y,
shift by mu=1/2. C_mu=1/2, W_mu=4, S_mu=-15/2, beta_mu=2,
a_mu=5 and K_mu=5. On the same constrained vectors the exact shifted
energy is5x^2. High response, beta and corrected moment ALL change.
Keeping their unshifted values would give the wrong answer.

Genuine positive-eigenlevel control: original Q=[[2,1],[1,2]] is strictly
positive with eigenvalues1 and3. For m=x+y its gate is2. Shifting by
mu=1 gives [[1,1],[1,1]] and gate0, retaining the moment-zero shifted
null (1,-1). The gate correctly classifies a shifted positive eigenmode
as a shifted null, not an original null. Its high block remains positive.

The genuine differential crossing remains a lawful Schur application
whenever its chosen high sector is coercive. A full original null with
nonzero chosen moment is outside ker m; a moment-zero null makes the
gate singular. The constrained theorem cannot turn a restriction-only
certificate into an all-cap continuation theorem.

## 4. Current native data do not yet evaluate this gate

All54 new exact control checks pass. No historical chain total is added;
these checks do not evaluate an actual native gate or a zeta null vector.

The read-only NF15 handoff certifies original E80 at53/50 with physical
lower9e-34 and NF10 certifies F112 at the same cap with lower17/100.
E80 and F112 are not complementary: 32 intervening physical directions
remain. Taking E=E112 would make the known F112 bound a lawful kappa,
but the full E112 native matrix and complete high response are not
established by the handoff. Taking E=E80 requires a certified high bound
on all of F80, which is not supplied by F112 positivity alone.

Even after a complementary split is certified, the needed quantities
are the FULL response Gram C(Wx,Wx'), mixed moment m(Wx), and beta,
with rigorous errors and original normalization. An approximate scalar
susceptibility, separate finite/complement signs or unsigned norm alone
does not evaluate (4). No native gate is made to pass here.

This theorem identifies a falsifiable target-specific path to exclude
invisible nulls: certify the constrained gate, not necessarily the stronger
unconstrained full Schur sign. It does not prove the needed all-cap
arithmetic estimate, eliminate moment-carrying contact, or close RH/F4.
Whole-domain original positivity remains21/20; Lean closure remains open.
