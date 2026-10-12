# RC161 terminology additions

Definitions are additive; historical terminology remains unchanged.

**Combined endpoint approximation.** For the RC158 inverse trial matrix Y and its paid action approximation q(Y), H_approx=Sym<q(Y),y(Y)>_D approximates the complete symmetric endpoint functional H_Y=<Cy(Y),y(Y)>_D. The old action part is a correlated source-Gram polarization; the new action part uses RC156-157's directed trial-source pairing blocks.

**Joint endpoint deviation.** If e=Cy-q(Y), E bounds e^*e, and G_y bounds y^*y, then for gamma>0 the symmetric deviation obeys -K<=H_Y-H_approx<=K, K=(gamma E+G_y/gamma)/2. This bound pays the whole conditioned functional for every mixture without independent entrywise error charging or mixed-error orthogonality.

**Weighted action-column Cauchy bound.** With paid column errors epsilon_i and positive weights w_i, (sum_i epsilon_i|c_i|)^2<=[sum_i epsilon_i w_i]sum_i (epsilon_i/w_i)|c_i|^2. RC161 uses rational upper square roots of the inverse source-Gram diagonal as weights, then transports this bound to the inverse trial coefficients. It preserves the small errors of accurately paid old columns.

**Positive variational lower with a retained sharper enclosure.** Passing a PSD check on the combined-action variational lower certifies positivity of that lower. It does not imply that this lower and its paired upper improve the previously retained inverse enclosure. RC161 retains RC160's narrower valid enclosure when the new candidate is wider.
