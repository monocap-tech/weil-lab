# RPB108 DNE7 — Arithmetic reflected Hankel sign and prime-two packet control

**Research identity:** DNE7 tests whether the original arithmetic forces a favorable reflected correlation on arbitrary positive-half profiles or only on solutions of the actual pole-free eigenvalue equation.

Let a>0 and f be real and smooth supported in (0,a). Define even/odd extensions `E f(x)=f(|x|)` and `O f(x)=sgn(x) f(|x|)` to (-a,a), zero outside. Both belong to the original canonical domain.

**Reflected arithmetic Hankel form**:
```
C_a(f)=
 int_0^a int_0^a j(x+y) f(x) f(y) dxdy
 +sum_(log n <= 2a) c_n int_(max(0,ell_n-a))^(min(a,ell_n))
             f(x) f(ell_n-x) dx,
 j(t)=exp(-t/2)/(1-exp(-2t)),
 ell_n=log n, c_n=Lambda(n)/sqrt(n).
```

**Parity comparison:** `H_a(Of)-H_a(Ef)=4C_a(f)`, where H is the complete original POLE-FREE native form, preserving all archimedean and prime shifts; this is a form comparison, NOT positivity of either H or original Q.

**Archimedean Gram:** for f supported away from x=0,
```
C_arch(f)=sum_(k>=0) |int_0^a f(x)exp[-(2k+1/2)x]dx|²>=0.
```
The prime terms are reflection/Hankel pairings, each sign indefinite on sign-changing profiles.

**Prime-two negative/positive subspaces:** At any a>(log2)/2, there are disjoint small intervals J and R_2J inside (0,a), where `R_2 f(x)=f(log2-x)`; choose their union so every pairwise sum remains below log3, and so no within-J or within-R_2J sum equals log2. On the antisymmetric subspace `f=g-R_2g` with smooth g in J, `C_2(f)=-c_2||f||²`, while every higher prime-power reflection vanishes. The continuous Gram can be made uniformly as small as desired by shrinking J. Thus `C_a(f)<=-(c_2/2)||f||²` on an INFINITE-dimensional smooth subspace. The symmetric subspace `g+R_2g` has `C_a(f)>=c_2||f||²`. Both signs persist after intersecting with kernels of ANY fixed finite list of continuous linear moment functionals.

**Exact concrete cap:** At a=53/50 choose ell=log2, eps=1/100,
J=(3ell/8-eps,3ell/8+eps), R_2J=(5ell/8-eps,5ell/8+eps). Use 2/3<ell<7/10 and 1<log3 to verify both intervals are disjoint and inside the cap and no higher prime reflections overlap. Every f supported on J union R_2J satisfies x+y>ell/2, so `j(x+y)<2`. Its L1 squared is at most 4eps times its L2 squared. Therefore C_arch<=8eps||f||²=2/25||f||². Since c_2=ell/sqrt2>4/9, antisymmetric f obeys `C_a(f)<-c_2||f||²/2`, strictly. The bound is valid on all smooth subspace vectors, not merely individual approximate delta packets.

**Inherited null-adapted restriction:** If Q_a>=0 and a real odd original null h=Of has sinh pole moment zero, then H_a(Of)=0. The even test Ef obeys
```
0<=Q_a(Ef)=-4 C_a(f)+8 (int_0^a f(x) cosh(x/2)dx)²,
```
so `C_a(f)<=2 (int f cosh)²`. This is a NECESSARY condition for an actual null, not a contradiction. It must be combined with the FULL homogeneous eigenfunction equation, which arbitrary packets do not satisfy.

**Scope:** Infinite negative/positive index of the reflected comparison DOES NOT imply negative original Q, does not disprove the RH criterion, and cannot evaluate the actual pole-free ground state. The new obstruction is to UNCONDITIONAL reflected positivity or finite-moment repairs, not to a null-adapted arithmetic estimate.


**Localized reflected Hankel operator:** On S=J union (log2-J) chosen with all pairwise sums below log3, set B_S(f)=int_S j(x+y)f(y)dy + c_2 f(log2-x), acting on L2(S). Its continuous archimedean part is Hilbert-Schmidt, while reflection is a selfadjoint involution with infinitely dimensional +/- eigenspaces. Thus sigma_ess(B_S)={-c_2,+c_2}. This is the essential spectrum of the FOLDED PARITY COMPARISON, not of the full Weil operator, J_a or the Doob generator. Finite-rank pole-moment corrections do not change it.
