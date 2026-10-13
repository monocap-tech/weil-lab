# RC188 terminology: extended centered psi endpoint action

Historical checkpoint wording remains unchanged. The native source psi0 is still eta_n=(2n+1)/(n(n+1)(H_n+s)) on even n>=990. The actual canonical M=D^-1 L, D norm, and native seven-source frame retain their definitions.

- **p188**: an exact rational polynomial on even degrees990..32766. Each coefficient is a nonnegative integer divided by2^42, obtained by rounding the certified eta coefficient midpoint downward on that fixed grid. Its discrepancy from the actual finite psi0 prefix is paid in D energy.
- **Integer endpoint kernel**: the lower fixed-point enclosure of each nonnegative even Legendre h-matrix entry, with scale2^28. Off-diagonal entries are (2n+1)/(|n-m|(n+m+1)); diagonal entries use the certified harmonic and log2 intervals. Kernel rounding and interval width are explicitly paid.
- **Q188(p188)**: the represented complete action Cp188, C=D^-1 h. It consists of32768 finite even output coefficients through65534, stored as integer numerators at scale10^30, and25 analytic eta moments above65534. The next moment pays the full geometric remainder.
- **Extended centered Cpsi trial**: Q188(p188)+(1/2)psi0 restricted to even degrees>=32768. The full omitted input contributes (C-I/2)t and is paid using0<=C<=I. No commutation with the degree cutoff is assumed.
- **RC188 complete canonical psi action trial**: psi0 plus the extended centered Cpsi trial minus rD^-1 psi0, r=789/125, with the regular component represented by zero and bounded on the entire native source by RC181. The identity and negative-r analytic terms retain complete source support.
- **Exact fixed-point output sum**: an integer sum of integer input coefficients times integer lower kernel entries. Every product and partial reduction is proved below2^63; the calculation uses no floating-point arithmetic.

This checkpoint improves one native action certificate. It neither reevaluates the five-source inverse width nor changes its response sources or acceptance status.
