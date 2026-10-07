# RPB108: physical source graph and critical height projection error

Date: 2026-10-07 UTC. Additive definitions.

- Gamma_a h=(P0 h,N0 h) is the COMPLETE actual source graph analysis on the supported logarithmic domain D_a. It is not the selected negative map R, its source image W=N0(K), or an effective synthesis.
- Hsrc=ell2(actual positive copies) direct-sum ell2(actual negative copies), with its positive Hilbert metric. Jsrc=diag(I,-I) is its signature operator; Q_a(h,v)=<Jsrc Gamma_a h,Gamma_a v>.
- V_a=Ran Gamma_a is closed by the existing positive observability lower bound. Pi_a is its orthogonal projection in the COMPLETE positive source metric.
- Pi_T cuts BOTH channels to |theta_q|<=T, retaining all corresponding actual copies. M_T multiplies these retained coordinates by |theta_q| and kills the rest. M_T is bounded self-adjoint at each T and commutes with Jsrc. It is not a native operator or a new aperture.
- E_T(h)=(I-Pi_a)M_T Gamma_a h is the weighted off-graph source error. The commutator [M_T,Pi_a]Gamma_a h equals E_T(h).
- Delta_K(T)=sum_basis sum_(|theta_q|>T)(|p_q(h_j)|^2-|n_q(h_j)|^2) is the signed UNWEIGHTED tail trace. It is finite at each T; neither sign nor critical integral is assumed.
- Finite complete source support means BOTH complete channels vanish off one finite actual-coordinate set. This is stronger than finite-dimensional negative compression or a finite selection observing a vector with infinite complete sources.
