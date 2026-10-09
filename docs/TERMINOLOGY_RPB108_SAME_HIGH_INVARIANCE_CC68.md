# CC68 terminology: same-high estimator invariance and native rejection

These definitions extend CC64 and precede the CC68 report.

H2 is the original two measured high Legendre modes. A **same-high trial**
is p_beta=p+H2 beta for any finite real or complex two-vector beta, with
the retained NF18 seed unchanged.

For r=P_F Lp, G=P_F LH2, u=H2*r, C2=H2*C_full H2, set
P=r*r, D=G*G, V=D-kappa C2 and zbar=G*r-kappa u, kappa=207/1000.
The **optimal two-mode upper estimator** is
U=(P-zbar*V^-1 zbar)/kappa. It is an upper bound on the true high response.

The **estimator sign margin** is M=Q(p)-U. A **same-high invariant margin**
is this exact scalar, unchanged by p_beta. It is not the true Schur sign.

A **native estimator rejection** proves M<0 using complete original
signed source Gram intervals. It rejects this sufficient estimator;
it does not prove that the actual inverse response exceeds Q(p).

An **all-H2 rejection** says that no same-high trial can make either the
coarse physical-source scalar gate or the optimal two-mode correlated
gate pass with the unchanged high floor. New high-form information can
still improve the true inverse response.

A **Gram transport** evaluates the source Gram under the exact change
r_beta=r+G beta. It keeps all original physical errors and signed sectors,
and does not require rerunning the source moment producer.

An **additional response credit** is U-<r,C_full^-1 r> >=0. It is not
the previously measured two-mode correlation credit, which is already
subtracted in U. To certify this seed's sign, additional information must
reduce the true response below Q(p).
