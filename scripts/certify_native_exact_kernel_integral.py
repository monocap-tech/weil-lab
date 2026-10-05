"""Exact polynomial-kernel integration using one precomputed denominator."""
from math import lcm
from fractions import Fraction as F


def kernel_moment_weights(kernel,maximum_length):
    kernel_denominator=lcm(*(c.denominator for c in kernel))
    integers=[int(c*kernel_denominator) for c in kernel]
    integral_denominator=lcm(*range(1,len(kernel)+maximum_length))
    weights=[sum((c*(integral_denominator//(m+k+1)) for k,c in enumerate(integers) if c),0)
             for m in range(maximum_length)]
    denominator=kernel_denominator*integral_denominator
    return weights,denominator


def make_kernel_integrator(kernel,maximum_length):
    weights,denominator=kernel_moment_weights(kernel,maximum_length)
    def integrate(p):
        assert len(p)<=maximum_length
        polynomial_denominator=lcm(*(c.denominator for c in p))
        value=sum((int(c*polynomial_denominator)*w for c,w in zip(p,weights)),0)
        return F(value,polynomial_denominator*denominator)
    return integrate


def make_archimedean_integrator(kernel,exponential_coefficients,maximum_correlation_length):
    """Integrate (delta*exp(-Lt)-c(t)*exp(-Lt/4))/t exactly."""
    weights,moment_denominator=kernel_moment_weights(kernel,len(exponential_coefficients)+maximum_correlation_length-2)
    exp_denominator=lcm(*(x.denominator for x in exponential_coefficients))
    integers=[int(x*exp_denominator) for x in exponential_coefficients]
    shifted=[sum((x*weights[q+r-1] for q,x in enumerate(integers) if q+r>0),0)
             for r in range(maximum_correlation_length)]
    full=sum((4**q*x*weights[q-1] for q,x in enumerate(integers) if q>0),0)
    denominator=exp_denominator*moment_denominator
    def integrate(c,delta):
        assert len(c)<=maximum_correlation_length and c[0]==delta
        common=lcm(*(x.denominator for x in c))
        numbers=[int(x*common) for x in c]
        value=numbers[0]*full-sum((x*w for x,w in zip(numbers,shifted)),0)
        return F(value,common*denominator)
    return integrate
