# 2026-11-21 — Eight GitHub Actions YAML colon repairs

Branch ancestry: `research/iv026-single-lane-iv009-kernel-recovery` at `e11839ca94e3244c9c31b74a07ca00ab10dfbc54`.

**Diagnosis:** eight still-installed historical workflows have one unquoted YAML mapping scalar each, e.g. `run: pip install --only-binary=:all: python-flint==0.8.0`. The `: ` in the pip argument is rejected by a YAML parser (`mapping values are not allowed here`). A minimal local PyYAML negative control fails, and the identical quoted command passes. Each affected file was verified to contain exactly one such line.

**Fix:** quote the entire existing `pip install --only-binary=:all: ...` scalar with single quotes. Quoting is YAML syntax only; the shell receives the same command. No source code, mathematical input, protected certificates, workflow events, job definitions, pinned dependencies, or original proof artifacts are otherwise modified.

**Files with one-line fixes:**
- `.github/workflows/nf390-original-selected-moment.yml` — original Git blob `4bb2685f5cd881415fc47c7eb1fa12c6862e331a` — command `run: pip install --only-binary=:all: python-flint==0.8.0 numpy scipy`
- `.github/workflows/nf392-original-j387-norm-and-native.yml` — original Git blob `d2c4975d17a42655f899c0c3e8627de5f8d74cfe` — command `run: pip install --only-binary=:all: python-flint==0.8.0 numpy scipy`
- `.github/workflows/nf393-original-direct-pole-native.yml` — original Git blob `5db9588a231ab3dfc16f58443175dc359d2024a5` — command `run: pip install --only-binary=:all: python-flint==0.8.0 numpy scipy`
- `.github/workflows/nf394-original-native-selected-receipt.yml` — original Git blob `8422320acbd9f935eb32424215a0fd13b0839650` — command `run: pip install --only-binary=:all: python-flint==0.8.0 numpy scipy`
- `.github/workflows/nf506-original-J8-independent-posterior-schur.yml` — original Git blob `6eaf62379a60c99a3ce3ce9becce8483675e67ea` — command `- run: pip install --only-binary=:all: numpy==2.3.5`
- `.github/workflows/nf509-original-microcell-leverage-source-focused.yml` — original Git blob `3bdf25f4bceba2408c656130323bd3bb99f283a2` — command `- run: pip install --only-binary=:all: python-flint==0.8.0`
- `.github/workflows/nf512-original-H4095-direct-J242-residual-focused.yml` — original Git blob `5c2db47c308c12fe1dc844fb0637c949d16bb4d8` — command `- run: pip install --only-binary=:all: python-flint==0.8.0`
- `.github/workflows/nf626-original-integer-centers.yml` — original Git blob `7cac97fb233b21c41380a9b8b86da9a1c9ef0e12` — command `- run: pip install --only-binary=:all: python-flint==0.8.0`

**Evidence scope:** GitHub run IDs from the preceding maintenance diagnostic (e.g. 44947285688, 44947284730, 44947282197, 44947279036) were instantaneous failure with zero jobs; this repeated YAML syntax defect is a concrete candidate explanation, not retrospective proof of GitHub's server-side message. Real GitHub Actions validation and actual fresh Lean kernel/axiom audits are still required.

**Acceptance:** verify every changed YAML diff replaces only its single unquoted scalar with the identical quoted scalar, ensure no extra paths changed, compare run behavior after guarded promotion, and retain strict evidence distinctions (source verification != Lean PASS).

Do not open an unrestricted PR or launch heavy CI until effective lineage and CI capacity are controlled.
