"""Exact integer Hankel products with outward moment radii."""

def convolution_window(a,b,start,count):
    """Nonnegative polynomial convolution via carry-free integer packing."""
    assert all(x>=0 for x in a) and all(x>=0 for x in b)
    maximum=min(len(a),len(b))*max(a,default=0)*max(b,default=0)
    if maximum==0:return [0]*count
    bits=maximum.bit_length()+1;mask=(1<<bits)-1
    def packed(values):
        out=0
        for x in reversed(values):out=(out<<bits)+x
        return out
    product=(packed(a)*packed(b))>>(bits*start)
    out=[]
    for _ in range(count):out.append(product&mask);product>>=bits
    return out


def hankel_apply(coefficients,moments,count):
    reverse=coefficients[::-1];start=len(coefficients)-1
    assert start+count<=len(moments)
    positive=convolution_window([max(x,0) for x in reverse],moments,start,count)
    negative=convolution_window([max(-x,0) for x in reverse],moments,start,count)
    return [x-y for x,y in zip(positive,negative)]


def moment_apply(coefficients,moments,count):
    center=[lo+hi for lo,hi in moments];radius=[hi-lo for lo,hi in moments]
    assert all(0<=lo<=hi for lo,hi in moments)
    return (hankel_apply(coefficients,center,count),
            hankel_apply([abs(x) for x in coefficients],radius,count))


def bilinear_bounds(coefficients,applied):
    center,radius=applied
    assert len(coefficients)<=len(center)
    mid=sum((x*y for x,y in zip(coefficients,center)),0)
    error=sum((abs(x)*y for x,y in zip(coefficients,radius)),0)
    return mid-error,mid+error
