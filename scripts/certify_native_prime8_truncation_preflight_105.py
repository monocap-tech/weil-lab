"""Fresh native highest-diagonal and analytic source-map budgets at 21/20."""
import json
from math import factorial
from certify_native_legendre_small_window import F,I,legendre,bernoulli,sqrt_rational
from certify_native_exact_polynomial import correlation
from certify_native_exact_logarithm import log_rational

def certificate():
 saved=I.grid;I.grid=10**140
 try:
  a=F(21,20);d=2*a;L=4*a;n=111;k=112
  assert log_rational(F(66),450).hi<L<log_rational(F(67),450).lo
  assert log_rational(F(8),450).hi<d<log_rational(F(9),450).lo
  assert L<6 and d<3 and d/4<log_rational(F(2),450).lo
  c=[a*x*2**j for j,x in enumerate(correlation(legendre(n)[n],legendre(n)[n]))]
  delta=2*a/F(2*n+1);assert c[0]==delta
  mass=sum(map(abs,c));abound=F(3,4)*L*delta+sum(map(abs,c[1:]))
  def width(N,K):
   e=67*L**(N+1)/factorial(N+1)*(delta+mass/F(4**(N+1)))
   b=4*(L/6)**(2*K+2)/(1-(L/6)**2)
   return 2*(5*a*e+abound*b)*F(2*n+1)/(2*a)
  native={str(N):str(width(N,N)) for N in [360,380,400,420]}
  ceiling=(1+d+d*d/3)/2;assert ceiling==F(457,200)<F(23,10)
  B=bernoulli(282);sources={}
  for N,K in [(90,114),(100,130),(100,140),(110,140)]:
   coefficients=[abs(B[2*j]*(2*d)**(2*j)/factorial(2*j)) for j in range(1,K+1)]
   assert all(y<x for x,y in zip(coefficients,coefficients[1:]))
   # The exponential remainder follows from Taylor's integral formula on x>=0;
   # no restriction x<=1 is needed for exp(-x).
   ce=F(23,10)*(d/2)**(N+1)/factorial(N+1)
   cb=4*(d/3)**(2*K+2)/(1-(d/3)**2)
   he=ce/(N+1)+cb/(2*K+2);ae=ce/(N+2)+cb/(2*K+3)
   ep=2*(d/4)**(N+1)/factorial(N+1)
   squared=sum(((2*j+1)*(2*he+2*j*(j+1)*ae+10*d*ep)**2 for j in range(k)),F(0))
   eta=sqrt_rational(squared).hi
   sources[f'{N}/{K}']={'squared_analytic_map_allowance':str(squared),'upper':str(eta),'display':float(eta)}
  return {'aperture':str(a),'retained_vectors':k,'exponential_guard':67,'kernel_guard':str(5*a),
   'source_polynomial_kernel_ceiling':str(ceiling),'source_kernel_ceiling_guard':'23/10',
   'native_diagonal_widths':native,'native_diagonal_width_displays':{s:float(F(t)) for s,t in native.items()},
   'source_analytic_allowances':sources,'inherited_native360_width_passes':F(native['360'])<F(1,10**35),
   'proposed_native_orders':[400,400],'proposed_native_diagonal_width_passes':F(native['400'])<F(1,10**35),
   'proposed_source_orders':[100,130],'proposed_source_analytic_allowance_passes':F(sources['100/130']['upper'])<F(1,10**35),
   'actual_source_error_complete':False,'all_native_entry_widths_checked':False,'whole_domain_positivity':False}
 finally:I.grid=saved
if __name__=='__main__':print(json.dumps(certificate(),indent=2))
