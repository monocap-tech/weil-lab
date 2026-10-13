# RPB108: physical collar negative-witness constructor

Base: research 583f3a2f6cc6a1b3b5622ce43af10d969a21ec91.

## The constructor theorem

Suppose h!=0 is an actual full-native endpoint weak-null vector in D_a. For every b>a, there is a compact smooth g supported in the newly admitted collars
\[
\Omega_{a,b}=(-b,-a)\cup(a,b)
\]
such that
\[
s:=\Re Q_b(g,h)>0.
\]
With d=|Q_b(g,g)| and t=s/(s+d), the actual physical vector
\[
v=h-tg\in D_b
\]
satisfies
\[
Q_b(v,v)\le-ts<0.
\tag{1}
\]

The construction uses the explicit same-vector residual, a finite prime-shell correction, a collar cutoff and mollification. It requires no inverse of a logarithmic Riesz operator or raw Green-synthesis preimage.

Since h and g have disjoint physical supports,
\[
\|v\|_2^2=\|h\|_2^2+t^2\|g\|_2^2.
\tag{2}
\]
Full actual source custody is exact:
\[
P_bv=P_bh-tP_bg,\qquad N_bv=N_bh-tN_bg.
\tag{3}
\]
Thus ||N_bv||^2-||P_bv||^2>=ts>0.

Compact smooth strictly negative actual tests in (-b,b) are also constructed by one final mollification of v. No actual endpoint h is asserted to exist.

## Terminology before use

**Newly admitted collars:** Omega_a,b, the physical open region added by support enlargement.

**Prime-shell-corrected residual:** the actual residual q_b of the unchanged h at multiplier cutoff b, obtained from q_a by subtracting exactly the newly activated finite physical translations.

**Physical collar negative witness:** v=h-tg above; h is preserved as the original physical component and g is an explicitly constructed smooth outer-collar correction. Its source coordinates are changed by the stated linear formula, not silently retained under a new name.

## Exact prime-shell custody

The preceding residual theorem constructs
\[
q_a=T_a h+p_h,
\]
locally L2 and zero on (-a,a), with the genuine multiplier core T_a h globally L2. Here T_a in this formula denotes the physical Fourier multiplier; it is distinct from the induced positive-range gain map, which will be denoted G_b in this note.

Let
\[
\mathcal S_{a,b}
=\{n:\ n\text{ is a prime power},\ 2a<\log n\le2b\}.
\]
The actual native symbols satisfy
\[
m_b=m_a-\sum_{n\in\mathcal S_{a,b}}
 \frac{2\Lambda(n)}{\sqrt n}\cos(2\pi\xi\log n).
\]
Fourier translation gives the genuine physical shell
\[
H_{a,b}h(x)=
\sum_{n\in\mathcal S_{a,b}}\frac{\Lambda(n)}{\sqrt n}
 \bigl(h(x-\log n)+h(x+\log n)\bigr).
\]
Consequently
\[
q_b=q_a-H_{a,b}h.
\tag{4}
\]
The pole is unchanged. Equality-threshold primes at 2a already belong to the old cutoff and are not in the shell; primes at 2b are included.

The shell is a finite bounded L2 translation operator. Hence
\[
\mathcal F^{-1}(m_b\widehat h)
=\mathcal F^{-1}(m_a\widehat h)-H_{a,b}h
\]
is globally L2, and q_b is locally L2.

For |x|<a, every shell shift exceeds 2a, so both shifted h values vanish a.e. Therefore q_b=0 in the old interior. One cannot identify q_b with q_a in the outer collars; their exact difference there is load-bearing.

## Every enlargement detects genuine collar mass

The derived L2 multiplier-domain result gives, for every g in D_b,
\[
Q_b(g,h)=\int_{-b}^b\overline{g(x)}q_b(x)\,dx.
\tag{5}
\]
The spectral term is an ordinary L2 Plancherel pairing because m_b Fourier(h) is L2. The pole term is integrable on this bounded interval. Thus no unproved graph-density premise is needed to extend (5) to the entire supported logarithmic domain.

If q_b vanished a.e. on (-b,b), (5) would make h weak-null on D_b. The proved strict-enlargement theorem forbids this nonzero h. Since q_b is already zero on (-a,a) and endpoints have measure zero,
\[
\int_{\Omega_{a,b}}|q_b(x)|^2dx>0.
\tag{6}
\]

This proves observability of the combined, shell-corrected collar residual. It does not claim an individual archimedean, prime or pole summand is nonzero independently, or that one selected coordinate detects it.

## Constructing a smooth detecting test

Choose a real chi in C_c^\infty(Omega_a,b), 0<=chi<=1, with
\[
m:=\int\chi(x)^2|q_b(x)|^2dx>0.
\]
Such a cutoff exists by (6), for example by taking a member of a compact collar exhaustion whose weighted mass is positive.

Let f=chi^2 q_b, extended by zero outside the collars. It is compactly supported L2. Choose a nonnegative compact smooth unit-mass mollifier rho and set
\[
g_\epsilon=\rho_\epsilon*f.
\]
For epsilon smaller than the distance from supp chi to the complement of Omega_a,b, g_epsilon is compact smooth and still supported in the newly admitted collars. Standard L2 approximate-identity convergence gives g_epsilon->f in L2. From (5),
\[
Q_b(g_\epsilon,h)\longrightarrow
 \int\overline{\chi^2q_b}q_b=m.
\]

A quantitative sufficient choice is
\[
\|g_\epsilon-f\|_2
 \le\frac{m}{2\|q_b\|_{L^2(\Omega_{a,b})}}.
\]
It ensures s=Re Q_b(g_epsilon,h)>=m/2>0. Take such a g_epsilon as g. No even-real restriction on h or g is imposed, and no phase rotation is necessary.

This is a conditional analytic construction from the supplied actual h. It is not a numerical certificate for an unknown endpoint mode.

## Strict negative energy

Endpoint nullity and unchanged source inclusion give
\[
Q_b(h,h)=Q_a(h,h)=0.
\]
Hermitian expansion for real t>0 yields
\[
Q_b(h-tg,h-tg)
=-2t\,\Re Q_b(g,h)+t^2Q_b(g,g).
\]
Set s=Re Q_b(g,h)>0, d=|Q_b(g,g)| and t=s/(s+d). Then td<=s, so
\[
Q_b(h-tg,h-tg)\le-2ts+t^2d\le-ts<0.
\]
This proves (1). Disjoint physical support proves (2). Bounded actual full analyses and their linearity prove (3), while full source/native equality gives its strict energy defect.

The induced full-negative positive-range map G_b=N_bP_b^{-1} therefore has norm strictly greater than one. A selected-background B can have different energy after removal; no selected unit-bound failure is inferred automatically.

## Producing an actual smooth negative witness

Both h and the compact g are supported a positive distance inside (-b,b), since a<b. Thus v has a strict outer support margin.

For a sufficiently small mollifier scale delta, v_delta=rho_delta*v belongs to C_c^\infty(-b,b). Its Fourier multiplier tends pointwise to one and has modulus at most one. Dominated convergence with the integrable weight w|Fourier(v)|^2 proves
\[
v_\delta\longrightarrow v\quad\text{in }D_b.
\]
The bounded native form therefore gives Q_b(v_delta)->Q_b(v)<0. Eventually v_delta is a compact smooth actual negative test.

Actual source coordinates converge by the already proved bounded logarithmic sampling maps. This is a direct weighted-Fourier construction, not an assumed full graph-density statement.

The final smoothing produces a new negative witness; it does not claim that v_delta is the original endpoint-null vector or that its old source coordinates are unchanged. Their custody is the actual sampling of v_delta.

## What is closed and what remains

At a hypothetical finite positive aperture, the attained endpoint h now gives physical negative witnesses in every larger window through the explicit exterior digamma residual and exact finite prime shell. The earlier abstract form-residual perturbation is no longer the only constructor.

This closes a concrete physical-witness consequence of endpoint nullity. It does not exclude the endpoint, prove that actual negativity exists, or supply exponential boundary-collar smallness. That independent null-exclusion issue remains unchanged.

No residual regularity or physical operator-domain assumption has been added: both were derived in the preceding theorem. No raw-copy observations, retained membership or background positivity are used. FULL TRANSPORT CLOSED remains open.

## Validation and cursor

Analytic proof using the actual gapless residual theorem, exact Fourier translation normalization, finite prime-cutoff custody, the strict-enlargement obstruction, L2 mollification and logarithmic Fourier convergence. No new external input, Lean source/workflow changes or CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf; Actions run 37236113125/job 111535430775.

At 583f3a2, the actual endpoint residual gives a direct physical negative-witness constructor for every b>a. The enlarged residual is q_b=q_a minus the finite prime-shell translations with exactly 2a<log n<=2b; the pole and physical h are unchanged. Its core is L2 by the derived endpoint domain result plus bounded shell translations. It vanishes in the old interior, while strict-enlargement rigidity forces positive L2 mass in the newly admitted collars. A compact collar cutoff and L2 mollification produce an actual smooth g supported outside [-a,a] but inside (-b,b), with Re Q_b(g,h)>0. With s=Re Q_b(g,h), d=|Q_b(g)| and t=s/(s+d), the physical vector v=h-tg satisfies Q_b(v)<=-ts<0 and exact disjoint-support norm custody. Smooth negative witnesses follow by convolution within the strict outer support margin, using direct weighted Fourier convergence rather than an assumed graph-density premise. Actual full analyses obey P v=P h-tP g and N v=N h-tN g, giving strict full-negative gain. No Riesz inverse, raw synthesis preimage or selected-background positivity is used. This makes the conditional finite-endpoint failure physically constructive; it does not assert an actual endpoint/negative input exists or exclude that endpoint. Boundary-collar null exclusion remains independent; Lean/CI unchanged and FULL TRANSPORT CLOSED open.
