#!/usr/bin/env python3
"""NF381: use original NF380 archived native signed kernel to measure only n513.

Selected J242, four fixed original critical probes, NF369 Y0, NF370 T, archived
full WJJ/WJF and the historic signed multiplier are UNCHANGED. The outer
original sine n513 is a diagnostic only, not an added generator.
"""
import json,sys,hashlib
from pathlib import Path
import verify_nf380_original_archived_signed_dual as parent

ORIGINAL_512_SHA='9d4b07fb2ca42c14ed995ddcd69811201eacb6f13f9f795a70c4b64889e9f83b'

def main():
    if '--original-512' not in sys.argv:
        raise ValueError('original NF380 native n512 report mandatory')
    idx=sys.argv.index('--original-512')
    filename=sys.argv[idx+1]
    original=Path(filename).read_bytes()
    assert hashlib.sha256(original).hexdigest()==ORIGINAL_512_SHA
    first=json.loads(original)
    assert first['unfitted_n']==512 and first['original_signed_32_CE_BP_overlaps'] is True
    del sys.argv[idx:idx+2]
    parent.INDEX=513
    parent.main()
    ix=sys.argv.index('--output')
    dest=Path(sys.argv[ix+1]);j=json.loads(dest.read_text())
    assert j.get('unfitted_n',513)==513
    if 'FULL SIGNED ONE-WITNESS RESPONSE' in j['standing']:
        assert j['original_signed_32_CE_BP_overlaps'] is True
        j['standing']='NF381 N513 ORIGINAL ARCHIVAL REUSE FULL SIGNED ONE-WITNESS RESPONSE; JOINT REPLAY REQUIRED'
        j['original_512_native_source_sha256']=ORIGINAL_512_SHA
        j['original_candidate_513_is_not_a_new_selected_source']=True
        j['complete_joint_512_513_dual_computed']=False
        j['W_ODD_NEG']=j['RH']='OPEN'
    else:
        j['standing']='NF381 FIXED N513 PHYSICAL CANDIDATE METHOD STOP; JOINT NOT COMPUTED'
        j['original_512_native_source_sha256']=ORIGINAL_512_SHA
        j['complete_joint_512_513_dual_computed']=False
        j['W_ODD_NEG']=j['RH']='OPEN'
    dest.write_text(json.dumps(j,indent=2)+'\n')
    print('NF381 inherited original signed operator n513 native:',j['standing'],flush=True)

if __name__=='__main__':main()
