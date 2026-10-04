# RPB108: translation rigidity obstructs enlarged full weak-null transport

Base: research 556d3c67b1769f1408b72963824ff79c436d5931.

## The obstruction theorem

Let 0<a<b. Let h be a nonzero actual supported logarithmic vector with support in [-a,a]. Then h cannot satisfy
\[
Q_b(g,h)=0\quad\hbox{for every }g\in D_b.
\]
Here Q_b is the full actual native Weil mixed form, already identified with full positive-minus-negative sampling on D_b.

In particular a nonzero endpoint weak-null vector cannot retain full weak-nullity on any strictly larger window while preserving its physical vector. This proves an obstruction to the fresh full-source first-contact transport route. It does not establish RH or apply automatically to selected-background forms.

The proof uses two actual properties already derived: translation covariance of the full native form, proved explicitly below, and finite nullity on every fixed supported logarithmic domain. It assumes neither background positivity nor spectral physical operator-domain membership.

## Window-independent full form and translations

On the union of supported logarithmic domains, the full source mixed form
\[
Q(f,g)=\langle Pf,Pg\rangle-\langle Nf,Ng\rangle
\]
depends only on the physical vectors. Its complete raw samples and partner dictionary are unchanged on support inclusion. Thus Q_c(f,g)=Q_d(f,g) whenever f,g belong to both domains. The preceding full-density theorem identifies this with the native form on each domain.

Define tau_s h(x)=h(x-s). Its support is shifted by s, and
\[
\widehat{\tau_s h}(\xi)=e^{-2\pi i s\xi}\widehat h(\xi).
\]
Hence logarithmic energy is preserved by translation. The translated vectors lie in a sufficiently large supported domain.

The actual native form is invariant under simultaneous translation:
\[
Q(\tau_s f,\tau_s g)=Q(f,g).
\tag{1}
\]
To prove this, compute both forms in one larger window containing all four vectors. The Fourier multiplier pairing is invariant because the two phases cancel. For the native pole moments,
\[
M_-(\tau_s f)=e^{-s/2}M_-(f),\qquad
M_+(\tau_s f)=e^{s/2}M_+(f).
\]
Thus each mixed pole cross term, conjugate(M_-(f))M_+(g) and conjugate(M_+(f))M_-(g), is unchanged: s is real and the factors cancel. The fixed finite prime multiplier in that larger window is included unchanged on both sides. No prime threshold limit is required for this computation.

In particular,
\[
Q(g,\tau_s h)=Q(\tau_{-s}g,h).
\tag{2}
\]
These are full native/source identities on actual logarithmic vectors, not claims about a selected-only multiplier.

## Finite nullity is unconditional at a fixed window

For each c>0 let A_c be the bounded Riesz operator for Q_c on D_c with the canonical logarithmic inner product. The certified symbol differs from w by a bounded multiplier; finite prime terms are bounded physical L2 operators, and the pole term is finite rank.

The supported logarithmic embedding J_c into physical L2 is compact by the earlier Fourier-truncation proof. Therefore the bounded-multiplier correction compressed as J_c^* M J_c is compact, and
\[
A_c=I_{D_c}+K_c,\qquad K_c\ \hbox{compact}.
\]
This operator is self-adjoint, but positivity is not needed for finite nullity. If ker A_c were infinite-dimensional, an orthonormal sequence e_j in it would obey K_c e_j=-e_j, contradicting compactness. Thus ker A_c is finite-dimensional.

This is a fixed-window conclusion with constants depending on c, not a globally finite defect index assumption.

## Independent translates force a contradiction

Suppose the theorem's nonzero h is weak-null on D_b. Choose c with a<c<b and epsilon>0 so that
\[
a+\epsilon<c,\qquad c+\epsilon<b.
\]
For every |s|<epsilon, tau_s h belongs to D_c. For every g in D_c, tau_-s g belongs to D_b. Equation (2) and the assumed enlarged weak-nullity yield
\[
Q_c(g,\tau_s h)=Q_b(\tau_{-s}g,h)=0.
\]
Thus all these small translates belong to ker A_c.

Any finite collection of distinct translates of a nonzero compactly supported L2 vector is linearly independent. Indeed a relation with distinct s_j transforms into
\[
\widehat h(\xi)\sum_j d_j e^{-2\pi i s_j\xi}=0.
\]
Compact support makes Fourier(h) continuous and entire; nonzero h gives a nonempty real interval where its transform is nonzero. The exponential polynomial therefore vanishes on that interval, hence identically. Its derivatives through order m-1 at zero give a Vandermonde system in the distinct s_j, forcing every d_j=0.

Choosing arbitrarily many shifts in (-epsilon,epsilon) now makes ker A_c infinite-dimensional, contradicting finite nullity. This proves the obstruction theorem.

The contradiction requires a strict support margin. It does not exclude a kernel vector at its own endpoint window, so the previous first-contact constructor remains consistent.

## Exact enlarged residual and a negative perturbation

Now suppose h is an actual endpoint-null vector at a:
\[
Q_a(g,h)=0\quad(g\in D_a),\qquad h\ne0.
\]
Fix any b>a and view the same h in D_b. Source custody gives Q_b(h,h)=Q_a(h,h)=0.

Let
\[
r_b=A_b h.
\]
The theorem proves r_b!=0. For g in the old domain,
\[
\langle g,r_b\rangle_{D_b}=Q_b(g,h)=Q_a(g,h)=0.
\]
Thus the residual is orthogonal to the embedded old logarithmic domain. It records precisely the newly admitted mixed pairings, with no loss of the original witness.

Set
\[
s=\|r_b\|_{D_b}^2>0,\quad
d=|Q_b(r_b,r_b)|,\quad
t=\frac{s}{s+d}>0,\quad
v=h-t r_b.
\]
Self-adjointness and the Riesz dictionary give
\[
Q_b(r_b,h)=\langle r_b,A_bh\rangle=s,
\]
and hence
\[
Q_b(v,v)
 =-2ts+t^2Q_b(r_b,r_b)
 \le-2ts+t^2d
 \le-ts<0.
\]
The last inequality uses td<=s. This is a lawful actual logarithmic negative vector in every strictly larger window, constructed from the same endpoint vector and its actual enlarged residual.

Both full source coordinates of v exist by the logarithmic sampling theorem. Their exact actual energy satisfies
\[
\|Nv\|^2>\|Pv\|^2.
\]
Consequently the full-negative factor T_b=N_b P_b^{-1}, which is bounded by the positive carrier theorem, has norm strictly greater than one. Full-negative unit domination fails at every strict enlargement of this endpoint.

The fixed-window smooth-density theorem and continuity of Q_b give compact smooth approximants to v with strictly negative actual native energy. This is an existence consequence with an explicit strict bound on v; no numerical approximation or actual endpoint has been supplied here.

## Consequence for the first-contact route

If the previous constructor's lawful negative input is supplied, it yields a genuine endpoint h_* and a_* with full-source unit contraction and weak-nullity at a_*. The present theorem then gives negative vectors in every window b>a_* and rules out same-vector full weak-null persistence there.

Thus the inability to transport that particular null equation is not an unresolved carrier completion issue. The canonical inclusions exist and preserve coordinates; the larger test space necessarily detects a nonzero actual residual.

This does not derive a contradiction from a lawful negative input. First contact followed by strict negativity in every larger window is mathematically consistent. Any RH conclusion still requires a separate exclusion argument.

It also does not forbid every endpoint witness strategy. A different construction could change the physical vector, but that would require a new custody theorem and would not satisfy the same-vector persistence requested here.

## Selected-background scope

For a fixed selection,
\[
Q_{{\rm bg},s}(f,g)=Q(f,g)+
 \langle N_{{\rm selected},s}f,N_{{\rm selected},s}g\rangle.
\]
This extra selected negative energy generally is not invariant under physical translations: nonreal samples acquire real exponential factors and the pairwise negative coordinate mixes. Therefore equation (1) cannot be imported into the selected-background form without proof.

The obstruction applies to the full actual native weak-null identity. It does not claim that every historical selected null record has been disproved. Recovering its exact mixed identity and selection custody remains necessary. Finite-nullity by itself cannot replace the missing translation covariance.

A frozenWeilCompactAction equation must still be related lawfully to the actual native mixed form, including any separately required symbol premise. If such a relation identifies enlarged frozen-action cancellation with full native weak-nullity for this compactly supported same vector, the obstruction applies. No typed action equivalence is assumed here.

## Validation and cursor

Analytic proof on the already identified actual logarithmic/source domain. It uses the preceding compact-remainder and full-domain source/native theorems; no new external arithmetic result is introduced. No Lean source/workflow changes, new CI claim, asserted actual negative vector, or numerical endpoint. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 556d3c6, physical translations preserve the actual full native Weil mixed form, and identity-plus-compact gives finite nullity at every fixed window. Therefore no nonzero supported actual vector can be weak-null on a strictly larger window: assumed enlarged nullity would generate infinitely many independent small translates in an intermediate-window kernel. For any nonzero endpoint-null h supported in [-a,a] and any b>a, the enlarged Riesz residual r_b=A_b h is nonzero and annihilates the old domain. The same-vector perturbation h-t r_b, t=||r_b||^2/(||r_b||^2+|Q_b(r_b)|), has rigorously negative actual native energy; smooth negative tests follow by logarithmic density. Thus full-negative WD-T10 contraction fails at every strict enlargement of that endpoint. The fresh full-source first-contact route cannot provide the same-vector enlarged weak-null transport needed by the proposed F4 assembly. This is an exact analytic obstruction, not an RH contradiction. Selected-background forms need separate treatment because selected negative energy generally breaks translation covariance. No actual endpoint/negative vector existence is asserted. Lean unchanged; FULL TRANSPORT CLOSED and F4 entry remain open; this full-source persistence route is obstructed.
