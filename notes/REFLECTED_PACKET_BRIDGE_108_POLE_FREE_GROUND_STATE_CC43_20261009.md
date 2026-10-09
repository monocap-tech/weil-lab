# RPB108 CC43: native pole-free ground state and the higher zero-moment channel

Date: 2026-10-09 UTC. Analytic dependency: CC41 at 4eb3278fc07caaf118166bb86b7093be3f28c095.
Publication base: 7dc863673966b4bd62d8851b4c91cf0418a9da1d, preserving the concurrent CC42 contact-doublet result.
Definitions: [pole-free ground state](../docs/TERMINOLOGY_RPB108_POLE_FREE_GROUND_STATE.md).
Result: H_a has a simple nonnegative even ground state with nonzero cosh
moment. At an original nonnegative contact, a zero-moment pole-free null
therefore requires one negative ground state and a HIGHER zero eigenmode.
This does not exclude that remaining higher mode or prove RH.

## 1. The actual favorable kernel after pole removal

Retain CC27's normalized native form. Once BOTH signed poles are removed,
the continuous off-diagonal kernel is -j(x-y), where

    j(d)=exp(-|d|/2)/(1-exp(-2|d|))>0 for d!=0.

The discrete off-diagonal atoms are -c_n at +/-log n, with
c_n=Lambda(n)/sqrt(n)>0 for every active prime power. Thus the sign
problem noted in the concurrent actual-contact report for the FULL Q
is absent for H: the positive long-range pole kernel has been removed.
No prime term, local diagonal term or physical mass shift is removed.

For a real supported h in D_a, |h| belongs to D_a. One way to verify
this domain fact independently of endpoint regularity is to write

    log(e+|xi|)=1+int_0^infinity exp(-e t)
                              (1-exp(-t|xi|)) dt/t.

The Fourier multipliers exp(-t|xi|) have positive normalized Poisson
kernels. The corresponding difference energies contract under absolute
value, so E_log(|h|)<=E_log(h). The L2 norm is unchanged. Tonelli
justifies the nonnegative integral representation and domain extension.

Canceling local diagonal terms gives the actual pole-free comparison

    H_a(h)-H_a(|h|)
      = int int j(x-y)(|h(x)h(y)|-h(x)h(y)) dx dy
        +2 sum c_n int (|h(x)h(x+log n)|
                              -h(x)h(x+log n)) dx >=0. (1)

The continuous term is finite on the form domain: its integrand is
bounded by one half of j(x-y)|h(x)-h(y)|^2, and the inherited native
archimedean difference-energy representation controls this expression
(with harmless bounded far-tail terms). Core approximation extends
the comparison to the complete supported carrier. The translation
terms are finite by physical L2 Cauchy-Schwarz.

If the positive and negative sets of h both have positive measure,
the continuous term is STRICTLY positive. Restricting to separated
positive-measure subsets gives a strictly positive finite contribution,
since j is positive at every nonzero separation. Hence no lowest
physical eigenvector can change sign.

## 2. Existence, parity and simplicity

CC41 realizes H_a as the supported A_a plus a bounded physical remainder.
The compact physical embedding of D_a implies compact resolvent. Thus
the semibounded H_a attains its least physical eigenvalue lambda_0(a).
Absolute-value comparison gives a nonnegative real ground state phi.

The ground eigenspace is one-dimensional. If two linearly independent
real ground vectors existed, each could have its sign chosen nonnegative
by (1). A linear combination would change sign on two positive-measure
sets: nonproportional nonnegative profiles have different ratios, including
the possibility of disjoint support. This contradicts the strict comparison.
Real conjugation then gives simplicity over the complex field as well.

Reflection commutes with H_a. It takes phi to another nonnegative ground
state of the same norm, so simplicity gives phi(-x)=phi(x). Moreover

    int phi(x)cosh(x/2)dx>0.                            (2)

Only nonnegativity and nonzero physical mass are needed for (2).
Strict positivity at every point, a Hopf lemma, boundary values, H1
regularity and an unrestricted Fourier multiplier domain are NOT claimed.

## 3. Consequence for actual contact classification

Assume Q_a>=0 on the entire original supported domain. Since
Q_a=H_a+2c^2 on even vectors and Q_a=H_a-2s^2 on odd vectors,
H_a has at most one negative eigenvalue: on odd vectors it is nonnegative,
and on the codimension-one even kernel of c it is nonnegative. This is
a min-max consequence of the actual rank-one pole signs.

If a nonzero zero-moment Q_a-null exists, its pole moments vanish and
mixed nullity implies H_a h=0 in the supported operator sense of CC41.
It cannot be the simple ground state: an even ground state has nonzero
cosh moment by (2), and an odd vector cannot be that even ground state.
Therefore lambda_0(a)<0. Combining with the preceding index bound:

    H_a has EXACTLY ONE negative eigenvalue, simple and even,
    while the zero-moment contact lies in a higher zero eigenspace. (3)

In particular, if H_a has no negative eigenvalue, the zero-moment contact
channel is excluded. This is a CONDITIONAL statement; a negative even
pole-free direction is already present in the actual finite native data
near a=53/50. No absence of negative H is established there or globally.

The new sign comparison therefore restores a legitimate ground-state
argument for the pole-free form, but it does not license one for full Q,
nor does it remove a higher zero mode. The original moment-carrying even
threshold -2 and odd susceptibility1 remain separate open arithmetic tests.

## 4. Adversarial higher-null control

For b>0 let H=-b[[1,1],[1,1]], with strictly negative off-diagonal entries,
and let c(x)=sqrt(b)(x_1+x_2). Then Q=H+2c*c=b[[1,1],[1,1]]>=0.
H has a simple positive-profile ground state (1,1), eigenvalue -2b,
and a higher zero eigenvector (1,-1) with c=0. That vector is also a
Q-null. For real (x,y),

    H(x,y)-H(|x|,|y|)=2b(|xy|-xy),

strict for opposite signs. Thus even the favorable kernel, a simple
nonnegative ground state, and rank-one stabilization do not by themselves
eliminate the higher zero-moment class. This is a finite sign-structure
control, not an actual Weil arithmetic countermodel.

The validator checks 27 new exact assertions across three positive b
values and replays CC41's 16 operator-domain/positive-level controls,
43 total in this local chain. Earlier 25,993-check chains are not replayed
or added. The actual infinite-domain sign comparison and simplicity are
analytic deductions, not computed zeta eigenvectors or Lean certificates.

Whole-domain original positivity remains21/20, even0/odd0, physical
margin1/(3*10^63). Native finite E32 and physical F112 complement at53/50
remain read-only dependencies with full mixed sign pending. RH/F4,
contact exclusion, retained attachment and Lean closure remain open.
