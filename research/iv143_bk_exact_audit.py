"""Independent exact integer tests of the authenticated BK comparison data.

Checks finite matrix inequalities and the stored beta fractions only.
The physical Gram error and inverse comparator bounds are inherited
from BK and are not analytically rederived here.
"""
from fractions import Fraction as Q
import hashlib, io, json, pathlib, zipfile
import numpy as np
from iv142_generate_bk import ROOT, OUT, ARCHIVE, raw, require, sha

def pd(A):
    """Fraction-free symmetric Bareiss; positive leading minors."""
    prev=1
    n=len(A)
    for i in range(n):
        pivot=A[i][i]
        require(pivot>0,f"nonpositive pivot {i+1}")
        for j in range(i+1,n):
            for k in range(j,n):
                num=A[j][k]*pivot-A[i][j]*A[i][k]
                q,r=divmod(num,prev)
                require(r==0,"nonexact Bareiss division")
                A[j][k]=q
        prev=pivot
    return {"pivots":n,"last_minor_digits":len(str(prev))}
def ceil(q):
    return -(-q.numerator//q.denominator)
def main():
    idx=json.loads((ROOT/"index.json").read_text())
    data=raw(idx["archive"])
    require(len(data)==2992441 and sha(data)==ARCHIVE,"ZIP identity")
    out={}
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        require(z.testzip() is None,"ZIP CRC")
        for p,n,lower,margin in (("even",121,177,Q(17,10000)),("odd",119,187,Q(53,10000))):
            with np.load(io.BytesIO(z.read(p+"/exceptional.npz")),allow_pickle=False) as a:
                beta=Q(str(a["beta"].item()))
            with np.load(io.BytesIO(z.read(p+"/physical_gram.npz")),allow_pickle=False) as a:
                K=a["K"]; scale=int(a["scale"].item()); err=Q(str(a["error"].item()))
                require(K.shape==(n,n) and K.dtype.kind in "iu","Gram shape/dtype")
                A=[[int(x) for x in row] for row in K]
            require(scale==2**26 and err>=0,"Gram scale and error")
            require(all(A[i][j]==A[j][i] for i in range(n) for j in range(n)),"symmetry")
            shift=ceil(err*scale)
            require(beta<1-2*margin,"stored beta margin")
            L=[[100*A[i][j]-(lower*scale+100*shift if i==j else 0)
                for j in range(n)] for i in range(n)]
            U=[[-100*A[i][j]+(1200*scale-100*shift if i==j else 0)
                for j in range(n)] for i in range(n)]
            out[p]={"beta":str(beta),"margin":str(margin),"error":str(err),
                "scale":scale,"error_shift":shift,"lower":str(Q(lower,100)),
                "upper":"12","lower_test":pd(L),"upper_test":pd(U)}
            print(p,json.dumps(out[p],sort_keys=True),flush=True)
        # The actual archived scripts, not paraphrased substitutes.
        for member in ("even/bk_basis.py","odd/bk_basis.py","physical_gram.py","bk_check.py",
                       "even/basis.log","odd/basis.log","even/physical.log","odd/physical.log"):
            b=z.read(member)
            rec=next(x for x in idx["members"] if x["name"]==member)
            require(sha(b)==rec["sha256"],"script identity "+member)
            (OUT/("BK-"+member.replace("/","-"))).write_bytes(b)
    (OUT/"bk-exact-audit.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("BK FINITE MATRIX AND STORED BETA AUDIT PASS (conditional source enclosure)")
if __name__=="__main__": main()
