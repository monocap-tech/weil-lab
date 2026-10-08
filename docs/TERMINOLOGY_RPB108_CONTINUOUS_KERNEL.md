# RPB108 continuous-kernel dictionary

Introduced with NF61, 2026-10-08.

- **Mean-zero derivative carrier**: U_a={u in L2(-a,a): integral u=0}. On H0^1(-a,a), D=i d/dx maps bijectively to U_a; its inverse is J_a u(x)=-i integral_-a^x u(t)dt. This is not the full canonical logarithmic carrier.
- **Integrated original kernel**: the continuous even function k defined in the NF61 note, with -k'' equal to the ORIGINAL physical Weil distribution. Its compressed integral operator is denoted C_a, avoiding collision with the positive source map P_a and the source gain T_a.
- **Primitive mass operator**: M_a=J_a*J_a on U_a, equivalently the inverse mean-zero Neumann Laplacian. Its quadratic form is the ORIGINAL physical mass of the primitive, not a new negative source dictionary.
- **Relative kernel margin**: a bound C_a>=gamma M_a, gamma>0, on all U_a. This transfers to an original physical lower bound. An absolute operator-norm approximation to C_a alone is not such a bound.

“Integrated” means exact double integration of the original distribution, not prime smearing. No prime halo or modified pole occurs.
