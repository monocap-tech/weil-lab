/* Exact unsigned binary multiplication for carry-free moment convolutions.
 * No floating arithmetic or sign decision occurs here. GMP is optional;
 * the Python caller has an exact-integer fallback. */
#include <gmp.h>
#include <stdlib.h>
#include <stddef.h>

void *nf49_multiply(const unsigned char *a, size_t na,
                   const unsigned char *b, size_t nb, size_t *length) {
    mpz_t x, y, z;
    mpz_inits(x, y, z, NULL);
    mpz_import(x, na, -1, 1, 0, 0, a);
    mpz_import(y, nb, -1, 1, 0, 0, b);
    mpz_mul(z, x, y);
    void *result = mpz_export(NULL, length, -1, 1, 0, 0, z);
    mpz_clears(x, y, z, NULL);
    return result;
}
void nf49_free(void *p) { free(p); }
