# RC196 terminology

**Response-adapted triangle weights** are positive rational weights t_k selected using the row dual energy Y_k G_lower^-1 Y_k*. The selection t_k approximately1/sqrt(dual energy) optimizes a trace surrogate for the certified triangle bound. It is not a claim that the actual action errors are correlated or independent.

**Adaptive response action-error Gram** means E=(sum_k epsilon_k/t_k) sum_k epsilon_k t_k Y_k*Y_k. Each epsilon_k is a full absolute D-norm error bound on one represented raw trial action. Cauchy–Schwarz proves E bounds the squared action error of every complex response mixture. Weight selection changes the bound, not the operator, source family, trial vectors or action carriers.

**Retained RC195 matrix interface** means that all complete source/trial Grams, mixed cross entries, nominal residual Grams and infinite-tail payments are used from the SHA-256-bound RC195 certificate. This is a proof refinement on already reconstructed data, not a new finite projection or nominal-residual calculation.
