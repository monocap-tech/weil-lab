"""Exact signed convolution and outward batched Hankel moment action.

Carry-free packing is integer arithmetic. Optional GMP multiplication changes
speed only. Intervals remain on the historical 500-digit rational grid.
"""
import ctypes, subprocess, os
from pathlib import Path
import certify_native_next_shell_nf46_106 as historical
n=historical.n; I=n.I
_library=None; _attempted=False


def multiply(a,b):
    global _library,_attempted
    if not _attempted:
        _attempted=True
        root=Path(__file__).resolve().parents[1]
        target=root/'work/nf49/native_transport_integer.so'
        temporary=target.with_name('native_transport_integer_'+str(os.getpid())+'.so')
        target.parent.mkdir(parents=True,exist_ok=True)
        try:
            subprocess.run(['cc','-O2','-shared','-fPIC',str(Path(__file__).with_name('native_transport_nf49_integer.c')),
                            '-lgmp','-o',str(temporary)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            os.replace(temporary,target)
            _library=ctypes.CDLL(str(target))
            _library.nf49_multiply.argtypes=[ctypes.c_void_p,ctypes.c_size_t,ctypes.c_void_p,ctypes.c_size_t,ctypes.POINTER(ctypes.c_size_t)]
            _library.nf49_multiply.restype=ctypes.c_void_p
            _library.nf49_free.argtypes=[ctypes.c_void_p]
        except (OSError,subprocess.CalledProcessError):_library=None
    if _library is None:
        value=int.from_bytes(a,'little')*int.from_bytes(b,'little')
        return value.to_bytes((value.bit_length()+7)//8,'little')
    length=ctypes.c_size_t(0)
    pointer=_library.nf49_multiply(a,len(a),b,len(b),ctypes.byref(length))
    if not pointer:return b''
    try:return ctypes.string_at(pointer,length.value)
    finally:_library.nf49_free(pointer)


def convolution(a,b):
    assert a and b
    aa=max(0,-min(a));bb=max(0,-min(b))
    u=[v+aa for v in a];v=[z+bb for z in b]
    bound=max(u)*max(v)*min(len(a),len(b))
    bits=max(1,bound.bit_length()+1,max(u).bit_length(),max(v).bit_length())
    width=(bits+7)//8
    x=b''.join(z.to_bytes(width,'little') for z in u)
    y=b''.join(z.to_bytes(width,'little') for z in v)
    result=multiply(x,y)
    count=len(a)+len(b)-1
    assert len(result)<=count*width
    result=result.ljust(count*width,b'\0')
    pa=[0];pb=[0]
    for z in a:pa.append(pa[-1]+z)
    for z in b:pb.append(pb[-1]+z)
    out=[]
    for k in range(count):
        lo=max(0,k-len(b)+1);hi=min(len(a)-1,k)
        lo2=max(0,k-len(a)+1);hi2=min(len(b)-1,k)
        out.append(int.from_bytes(result[k*width:(k+1)*width],'little')
                   -bb*(pa[hi+1]-pa[lo])-aa*(pb[hi2+1]-pb[lo2])-aa*bb*(hi-lo+1))
    return out


def hankel(poly,moments,count):
    """Return sum_j poly_j moment_(i+j), with one outward grid rounding."""
    assert count>0 and len(moments)>=len(poly)+count-1
    p=list(reversed(poly));m=moments[:len(poly)+count-1]
    pc=[(z.l+z.h)//2 for z in p];mc=[(z.l+z.h)//2 for z in m]
    pr=[max(z.h-c,c-z.l) for z,c in zip(p,pc)]
    mr=[max(z.h-c,c-z.l) for z,c in zip(m,mc)]
    center=convolution(pc,mc)
    pieces=[convolution(list(map(abs,pc)),mr),convolution(pr,list(map(abs,mc))),convolution(pr,mr)]
    out=[]
    for i in range(count):
        k=len(poly)-1+i;r=sum(z[k] for z in pieces);c=center[k]
        out.append(I.raw((c-r)//n.SCALE,-((-(c+r))//n.SCALE)))
    return out


def coefficient_pair(a,b):
    return sum((x*y for x,y in zip(a,b)),I(0))


def adjoint(source,moments,bcount,lcount,ccount):
    _,b,l,cells=source
    vb=n.add(hankel(b,moments.M,bcount),hankel(l,moments.ML,bcount))
    vl=n.add(hankel(b,moments.ML,lcount),hankel(l,moments.ML2,lcount))
    vc=[]
    for cell,(mp,ml) in zip(cells,moments.cm):
        regular=hankel(n.add(b,cell),mp,bcount)
        logpart=hankel(l,ml,bcount)
        vb=n.add(vb,hankel(cell,mp,bcount))
        vl=n.add(vl,hankel(cell,ml,lcount))
        vc.append(n.add(regular[:ccount],logpart[:ccount]))
    return vb,vl,vc


def gram(source,adj):
    _,b,l,cells=source;vb,vl,vc=adj
    return coefficient_pair(b,vb)+coefficient_pair(l,vl)+sum(
        (coefficient_pair(c,v) for c,v in zip(cells,vc)),I(0))


def controls():
    global _library,_attempted
    import random
    rng=random.Random(490106)
    for size in [1,2,19,111,431]:
        a=[rng.randrange(-10**25,10**25) for _ in range(size)]
        b=[rng.randrange(-10**25,10**25) for _ in range(size//2+1)]
        direct=[sum(a[i]*b[k-i] for i in range(len(a)) if 0<=k-i<len(b)) for k in range(len(a)+len(b)-1)]
        assert convolution(a,b)==direct
    available=_library
    _library=None
    try:
        assert convolution([-9,0,12],[0,-7,2])==[0,63,-18,-84,24]
        assert convolution([10**1000],[0])==[0]
    finally:_library=available
    p=[I(-2,-1),I(0,1),I(3,4)];m=[I(i-1,i+1) for i in range(9)]
    for i,z in enumerate(hankel(p,m,7)):
        products=[[v.l*m[i+j].l,v.l*m[i+j].h,v.h*m[i+j].l,v.h*m[i+j].h] for j,v in enumerate(p)]
        lo=sum(min(v) for v in products);hi=sum(max(v) for v in products)
        assert z.l<=lo//n.SCALE and z.h>=-((-hi)//n.SCALE)
    return dict(exact_signed_convolution_controls='PASS',exact_python_fallback_controls='PASS',
                outward_hankel_controls='PASS',GMP_available=_library is not None)
