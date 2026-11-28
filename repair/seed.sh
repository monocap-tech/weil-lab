set -euo pipefail
root="$PWD/research"
e="$PWD/evidence"
mkdir -p "$e"
cd "$root"
test "$(git rev-parse HEAD)" = 5801507d416e4a699c002920b2441f5aa0c19aef
s=notes/provisional/NF618W02RootAttachment
a=WeilDefect/Arithmetic
test "$(git hash-object "$s/RootAttachmentCandidate.lean.txt")" = bed8b192f3741c88f27f877ce82a3e8952e82bf9
test "$(git hash-object "$s/ActualZetaOriginalPhysicalSemanticEndpointCache.lean.txt")" = 66273c57a9dac69913c72f7826aaf0e6c3860eeb
test "$(git hash-object "$s/ActualZetaOriginalPhysicalHybridEndpoint.lean.txt")" = ffc05cf064b4db7e355bf6624c5463545ac02f65
test "$(git hash-object "$s/FrequencyDecomposition.json")" = 1558a62fe99f3a10e34eb75106cab6028b3997ad
for name in ActualZetaOriginalPhysicalSemanticEndpointCache ActualZetaOriginalPhysicalHybridEndpoint; do cp "$s/$name.lean.txt" "$a/$name.lean"; done
cp "$s/RootAttachmentCandidate.lean.txt" "$a/NF618W02RootAttachmentCandidate.lean"
cp ../next/NF618W02Seeds.lean "$a/"
cp "$a/NF618W02Seeds.lean" "$e/"
lean --version | tee "$e/lean-version.txt"
lake update 2>&1 | tee "$e/lake-update.log"
test "$(git -C .lake/packages/mathlib rev-parse HEAD)" = 5ed2965256430c3649e86755f9576b54eca72435
cp lean-toolchain lake-manifest.json "$e/"
lake exe cache get 2>&1 | tee "$e/cache.log"
lake build WeilDefect.Arithmetic.NF618W02Seeds 2>&1 | tee "$e/seed-build.log"
lake env lean "$a/NF618W02Seeds.lean" 2>&1 | tee "$e/seed-axioms.log"
python3 ../next/audit.py "$e/seed-axioms.log" nf618W02Pi_sound nf618W02Seed_sound nf618W02Quarter_sound nf618W02Real_sound
