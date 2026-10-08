# CC6 retained logarithmic Euler tail

Definitions precede first load-bearing use; CC4/CC5 and NF63/NF64 remain unchanged.

- Tail parameter: q=N+1/4, x=pi|xi|, f_x(t)=x^2/[t(t^2+x^2)]. N counts original Euler terms, not divisor rows.
- Retained tail model: M_(N,K)(x)=1/2 log(1+x^2/q^2)+f_x(q)/2+sum_(k=1)^K B_(2k)/(2k)[q^(-2k)-Re(q+ix)^(-2k)]. This retains an UNBOUNDED logarithmic principal multiplier.
- Uniform tail correction budget: epsilon_(N,K)=8(2K-1)!/[6q]^(2K). The exact omitted tail differs from M by at most epsilon on the ENTIRE real Fourier line. This is an upper absolute error bound, unlike CC5's lower omitted-energy bound.
- Tail-retaining lower comparison: Qminus=Q_N+integral M|hhat|^2-epsilon mass. Qplus is defined with +epsilon mass. Both live on the original canonical domain, not all supported L2; no bounded NF63 background gain is assigned to them.
- Mass-small defect: R=Q-Qminus satisfies 0<=R<=delta mass, delta=2epsilon. R is bounded in physical L2 even though Qminus itself is unbounded there.
- Comparison Schur block: Sminus is the EXACT completion of Qminus in the same fixed physical E and nested complement as CC4. It is not the finite restriction of Qminus.
- Relative comparison tolerance: theta=delta c Mgraph^2/[(c-delta)m], where original complement >=c mass, ||W||_(coeff->mass)<=Mgraph, and original exact Schur >=m I. It is a comparison accuracy test, not an arithmetic aperture-loss bound.
