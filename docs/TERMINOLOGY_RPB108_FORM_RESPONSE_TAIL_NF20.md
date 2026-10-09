# RPB108 terminology — genuine high form-response tail (NF20)

Date 2026-10-09 UTC. Additive definitions; historical CC33, CC47–CC54, IP4, NF17–NF19 unchanged.

**Physical source on finite polynomial test space.** On fixed support [-a,a], a=53/50, the canonical original Weil form decomposes as E_log+R with R bounded in physical L2. For each zero-extended normalized Legendre polynomial e_j, its Fourier transform decays O_j(1/|xi|) and log(e+|xi|) times its Fourier transform lies in L2. Hence the original Q(e_j,.) is represented by a physical L2 source function s_j, though Q is NOT a bounded operator on the full physical L2 or all of its canonical form domain. This source-domain assertion is restricted to finite polynomial combinations.

**True complete high C-Riesz response.** With E=E112 and physical complement F=F112 inside the canonical supported log form domain, let C=Q|F, where C>=207/1000 I physically. For x in E, W x in F is the unique C-form Riesz solution C(Wx,y)=Q(x,y) for all y in F.

**Finite high Galerkin response.** For each parity p and m>=1 set H_m,p=span of the first m exterior Legendre modes of that parity. Let Y_m x be the C-orthogonal projection of Wx onto H_m,p. Set G_m(x,z)=C(Y_m x,Y_m z), G_full(x,z)=C(Wx,Wz). The true residual response T_m=G_full-G_m is positive semidefinite and equals C((W-Y_m)x,(W-Y_m)z). It is not the scalar difference of maxima R_full-R_m. The Galerkin sequence converges to G_full in A-relative finite-dimensional operator norm, but this theorem supplies NO effective rate.

**Form-dual residual source.** Define r_m,x(y)=Q(x-Y_mx,y), y in F. Its squared C-dual norm is EXACTLY T_m(x,x). If the finite-polynomial physical source is s(x-Y_mx), its physical high projection sigma_m(x)=P_F s(x-Y_mx) represents this residual, so
T_m(x,x)<=kappa^(-1)||sigma_m(x)||_physical^2, kappa=207/1000.
The norm on the right is a sufficient estimator, not an equality with the C-inverse reaction or a guarantee of decay.

**Relative residual gate.** The whole original positive-cap Schur condition is A-G_full>0. Once G_m is known, it is equivalent to T_m<A-G_m. A verified matrix upper P_m for the full physical residual Gram gives the SUFFICIENT source certificate P_m<kappa(A-G_m), with all native/finite projection/source errors paid. It is not a proved actual estimate and cannot be inferred from a finite number of observed exterior columns.
