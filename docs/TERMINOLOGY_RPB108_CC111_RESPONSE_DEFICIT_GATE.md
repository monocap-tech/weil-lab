# CC111 response deficit gate

Use the original CC110 Z44 packet, F112 high space and k=603/1000. Q and G are its complete native and high-source matrices; H=kQ-G. J=(B,D) is the exact invertible packet-coordinate frame with 42/43 positive columns and 2/1 negative comparison columns in even/odd parity.

The plain blocks are A=B^t H B, E=B^t H D and F=D^t H D. Its paid deficit gate is S=F-E^t A^-1 E. A certified negative S rejects the full uniform comparison, while leaving original form positivity unresolved.

The Schur response correction in form units is Delta=k^-2 W N^-1 W^t, with N=G_Y/k-Q_Y and W=S_ZY-k Q_ZY for physical high columns Y. Its comparison-unit correction is K=k Delta. All response data must refer to the original Z44/Y frame. The full response gate is F+K_DD-(E+K_BD)^t(A+K_BB)^-1(E+K_BD), assuming the positive block is certified. Scalar directional gains alone do not certify this gate.

For a hypothetical correction with zero B block and crosses, a deficit credit t I in comparison units passes if t exceeds a paid row-norm bound for -S. This is a design threshold, not an available original response certificate. Any positive semidefinite correction that rescues H must have rank at least the negative inertia (2 even, 1 odd).
