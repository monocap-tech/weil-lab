# RC197 terminology

**Native v10 source** is the unchanged RC131 order10 vector used in RC133: the degree-8190 rational Cg midpoint polynomial plus eta_n sum_{k=0}^{10} nu_k (lambda/n(n+1))^k at even n>=8192. Its finite prefix is materialized in RC183's Cg array. It is distinct from the actual action Cw14.

**Centered v10 endpoint carrier** represents C on a finite degree-512 input, retains its degree-1536 output and25 exact output moments, and adds one half of the omitted actual native v10 input. The full-domain contraction bounds the error on that omitted input by half its D norm. It assumes no commutation of C with a degree cutoff.

**Complete v10 canonical-action carrier** adds the native identity, the centered endpoint carrier, a finite negative-r D^-1 correction with coefficient intervals, the exact negative-r correction on the native source tail, and a regular degree-1536 polynomial. Its absolute D-norm error pays all input/output tails. It is not an expanded inverse-acceptance certificate.
