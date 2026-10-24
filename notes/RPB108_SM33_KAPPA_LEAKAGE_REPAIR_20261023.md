## October 23, 2026 audit erratum — mandatory \(\kappa\)-payment in \(K_-\)

**Status:** The original SM33 arithmetic was *not* a valid upper for the operator named \(K_-=(\kappa-m)_+\), because it integrated the SI10 envelope \(h=\max(0,-m_{\rm lower})\) without the additional \(\kappa=1/1000\). A simple adverse cell \(m=\kappa/2>0\) has \(h=0\) but \((\kappa-m)_+=\kappa/2>0\). The complete original SM10 890-column cap already uses \(h+\kappa\) correctly; the leakage/norm and subsequent SM34/MG07 reuse had not consistently carried that payment.

The corrected SAME source-space cluster mass is
\[
 M_j^{\rm repaired}=M_j^{\rm legacy}+2\kappa(b_j-a_j).
\]
For original b9 errors \(e_j<2^{-9}\), complete reflected unresolved width \(W=973/32\), and \(B=11/10\),
\[
 \varepsilon_{\rm repaired}
 =2B\sum_{j=1}^{107}M_j^{\rm repaired}e_j^2,\qquad
 \varepsilon_{\rm repaired}-\varepsilon_{\rm legacy}
 =4B\kappa\sum_j (b_j-a_j)e_j^2
 <2B\kappa W\,2^{-18}.
\]
This exact rational maximum payment is
\[
 2B\kappa W\,2^{-18}=\frac{10703}{41943040000}
 \approx2.5517940521240\times10^{-7}.
\]
The historical exact SI10 h-only leakage is below \(66247/10^9\), as enforced in the amended original SM33 validator. Consequently the **conservative fully paid leakage upper** satisfies
\[
 \varepsilon_{\rm repaired}<
 \frac{66247}{10^9}+\frac{10703}{41943040000}
 =\frac{8716573659}{131072000000000}
 <\frac1{15000}.
\]
The last strict inequality has been independently checked by exact Python \`Fraction\` arithmetic. Historical SM33 floating displays of \(\varepsilon=0.00006624610913\), \(H_-=82.71043570625\), \(\Gamma_-^2\) and its inverse correction are **LEGACY UNDERPAID VALUES** and must not be cited as complete certified \(K_-\) quantities. The corrected globally valid norm upper is
\[
 H_-^{\rm repaired}=2B(M_{\rm SI10}+\kappa W)
 =82.77732945625<83.
\]
The same conservative paid epsilon bound gives a **more explicit conditional SM34-style complement threshold**, without even using SM40:
\[
 \theta_{\rm paid}=1-\frac{\varepsilon_{\rm repaired}}{\kappa}
 >1-\frac{8716573659/131072000000000}{1/1000}
 =\frac{122355426341}{131072000000}
 \approx0.9334978205947876.
\]
This improves the old \(51/56\) sufficient numerical acceptance threshold and is based only on original SM33 b9 estimates plus the paid \(\kappa\). The numerical threshold is not accepted as a completed certified replay until the amended SM33 exact Fraction assertion has executed successfully and the inherited operator/domain identity has been independently reviewed.

SM35 now consumes this corrected value and propagates it into MG07. The SM34 **qualitative** \(51/56\) sufficient criterion survives because the fully paid \(\varepsilon<1/15000\) is preserved; its exact nonorthogonal Schur algebra is not otherwise changed. The sharper same-470 source-space \(\theta=1-\varepsilon/\kappa>14/15\) also remains logically available, conditional on the original physical/Fourier realization. No original \(470\times470\) signed gate is thereby evaluated.

For the refined SM40 leak computation use \(h_{\rm eff}=\min(h_{\rm SI10}+\kappa,w_{\rm SM40})\), **not** the invalid \(\min(h_{\rm SI10},w_{\rm SM40})\). This pays all original 3,892 real subcells and the complete 107 b9 remainder errors.

**Verification distinction:** the displayed rational ceiling and norm arithmetic have been checked independently; new full cluster-by-cluster corrected SM33 and SM40 replay, and dependent original MG07 workflows, await successful execution. The draft PR does not promote W-ODD-NEG, even, CC27 or RH.
