import re,sys
from pathlib import Path
expected=set(sys.argv[2:]);found={}
for m in re.finditer(r"'(?:WeilDefect\.)?(\w+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)",Path(sys.argv[1]).read_text()):
    n=m.group(1)
    if n not in expected: continue
    assert n not in found
    found[n]=[x.strip() for x in (m.group(2) or '').split(',') if x.strip()]
    assert set(found[n])<={'propext','Classical.choice','Quot.sound'}
assert set(found)==expected,(expected,found)
print('Strict audit PASS',sorted(found))
