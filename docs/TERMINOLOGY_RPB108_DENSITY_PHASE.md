# RPB108 density phase modulus (CC22)

Use the complete original normalized source decomposition Q=P*P-N*N, with all reflected, conjugate and multiplicity copies. For |x|<=B, the negative coordinate is n_q(h)=integral h(x) exp(i theta_q x) sinh(beta_q x) dx. The accepted external strip is |beta_q|<=3/8.

- Z2(T)=sum_{|theta_q|<=T} beta_q^2 is the cumulative second transverse count.
- W_eta(q)=(1+|theta_q|) log(e+|theta_q|)^eta, eta>0.
- N_eta=W_eta^(-1/2)N denotes the complete weighted negative analysis on physical L2(-B,B).
- U_r is coordinate multiplication by exp(i theta_q r). The phase modulus here is ||(U_r-I)N_eta||_HS. It is not the full translation/gain commutator.
- For the old gain A_s=T_s T_s*, D_s=I-A_s, let E select near-critical output and G=E D_s E. Incoming K has critical leakage L=E K.
- The original whole-shell criterion is ||K*D_s^(-1)K||<1. Its critical covariance requirement is L L*<=q G; a low-output budget ell with q+ell<1 suffices.
- A separated weight-transfer estimator bounds the weighted increment first, then multiplies by ||G^(-1/2) E W_eta^(1/2)||. That factor is at least delta_min^(-1/2) when finite; it may be unbounded.

An actual arithmetic weighted modulus does not certify the original unweighted relative covariance. Joint cancellation must be established before splitting its norm into unrelated factors. Finite controls below certify estimator limitations, not logical independence of the full Weil identities.
