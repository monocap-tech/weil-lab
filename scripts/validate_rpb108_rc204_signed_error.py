"""RC204: exact eight-column signed marginal error bound after RC203."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import argparse,hashlib,json

RC203_BLOB="5d321b659367ba459682b557b12ef63451f63e49"
GRID=10**20
BETA=F(473,200000)           # 0.002365
OLD=F(313,125000)           # 0.002504
REJECT=F(591,250000)        # 0.002364

def determinant(m):
    a=[list(r) for r in m]
    prior=1
    for k in range(len(a)-1):
        p=a[k][k]
        if not p:return 0
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                q,rem=divmod(a[i][j]*p-a[i][k]*a[k][j],prior)
                assert rem==0,"Bareiss division not exact"
                a[i][j]=q
        for i in range(k+1,len(a)):a[i][k]=0
        prior=p
    return a[-1][-1]

def failed_minor(m):
    for n in range(1,len(m)+1):
        if determinant([r[:n] for r in m[:n]])<=0:return n
    return None

def certify(path,reverse=False):
    raw=path.read_bytes()
    blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
    assert blob==RC203_BLOB,"RC203 blob mismatch"
    d=json.loads(raw)
    assert d["milestone"]=="RC203" and d["selected_trial"]=="least_residual"
    assert d["relative_inverse_width_upper"]=="743003/1000000"
    assert not d["canonical_half_Gram_inverse_width_gate_passed"]
    G=[[F(s) for s in row] for row in d["source_D_Gram_lower"]]
    assert len(G)==6 and all(len(r)==6 for r in G)
    assert all(G[i][j]==G[j][i] for i in range(6) for j in range(6))
    # Positive diagonal dominance verifies Gfloor <= G:
    # diag rounding discrepancy >= 6/GRID; each offdiagonal < 1/GRID.
    g=[[x.numerator*GRID//x.denominator-(6 if i==j else 0)
        for j,x in enumerate(row)] for i,row in enumerate(G)]
    assert all(G[i][i]-F(g[i][i],GRID)>=F(6,GRID) for i in range(6))
    assert all(abs(G[i][j]-F(g[i][j],GRID))<F(1,GRID)
               for i in range(6) for j in range(6) if i!=j)
    Y=[[F(s) for s in row] for row in d["selected_enclosure"]["trial_basis_coefficients"]]
    eps=[F(s) for s in d["individual_raw_trial_action_error_norm_upper"]]
    assert len(Y)==len(eps)==8 and all(len(y)==6 for y in Y)
    assert all(e>=0 for e in eps)
    weighted=[[eps[i]*Y[i][j] for j in range(6)] for i in range(8)]
    scale=1
    for row in weighted:
        for x in row:scale=scale*x.denominator//gcd(scale,x.denominator)
    assert scale==10**70
    w=[[int(x*scale) for x in row] for row in weighted]
    assert all(F(w[i][j],scale)==weighted[i][j] for i in range(8) for j in range(6))
    def check(beta,mask):
        # Fix first sign positive: simultaneous reversal is redundant.
        z=[sum((1 if i==0 or ((mask>>(i-1))&1) else -1)*w[i][j]
               for i in range(8)) for j in range(6)]
        a=[[beta.numerator*g[i][j]*scale**2-
             beta.denominator*GRID*z[i]*z[j]
             for j in range(6)] for i in range(6)]
        assert all(a[i][j]==a[j][i] for i in range(6) for j in range(6))
        return failed_minor(a)
    order=list(range(128))
    if reverse:order.reverse()
    assert all(check(BETA,mask) is None for mask in order)
    assert check(REJECT,12)==6
    assert BETA<OLD
    return dict(milestone="RC204",starting_commit="a390010cf32cb2f0d773c7f5b7c8d5ec37540880",
      input_rc203_git_blob_sha=RC203_BLOB,
      source_family=["P0","P2","f0","psi0","w14","v10"],
      trial_family=d["raw_trial_basis_order"],
      source_D_Gram_lower_floor_scale=GRID,diagonal_floor_allowance_grid_units=6,
      common_exact_weighted_row_denominator=str(scale),
      distinct_signed_rank_one_controls_verified=128,
      positive_integer_leading_principal_minor_tests=768,
      selected_uniform_squared_error_factor=str(BETA),
      previous_uniform_squared_error_factor=str(OLD),
      certified_relative_bound_reduction=str((OLD-BETA)/OLD),
      failed_previous_grid_factor=str(REJECT),
      failed_previous_grid_witness_mask=12,
      failed_previous_grid_witness_leading_minor_size=6,
      six_source_inverse_width_upper_unchanged="743003/1000000",
      canonical_half_Gram_inverse_gate_passed=False,stage_I_closed=False,
      status="PASS: sharper six-source trial-action-error envelope; inverse gate remains open",
      next_cursor="transport this error envelope through the full RC203 variational and residual inverse bounds")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("rc203_certificate",type=Path)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--replay",action="store_true")
    a=p.parse_args()
    result=certify(a.rc203_certificate,a.replay)
    if a.replay:assert json.loads(a.output.read_text())==result
    else:a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("RC204 PASS: 128 signed controls, squared-error factor",result["selected_uniform_squared_error_factor"])

if __name__=="__main__":main()
