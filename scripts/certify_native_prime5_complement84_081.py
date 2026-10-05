"""Actual 84-moment complement at a=81/100, including joint prime-3/5 fibres."""
import json
from math import factorial
from certify_native_legendre_small_window import F,I,atan,log_rational,sqrt_rational
from certify_native_larger_aperture_complement import integrated_mass


def exact_positive_pivots(matrix):
    m=[row[:] for row in matrix];out=[]
    for k in range(len(m)):
        pivot=m[k][k]
        if pivot<=0:raise ArithmeticError('nonpositive exact pivot')
        out.append(pivot)
        for i in range(k+1,len(m)):
            for j in range(i,len(m)):
                m[i][j]-=m[i][k]*m[k][j]/pivot;m[j][i]=m[i][j]
    return out


def certificate():
    a=F(81,100);d=2*a;k=84;T=F(243,20);Tlog=F(19,2)
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    assert 3<pi.lo<pi.hi<F(22,7)
    s2,s3,s4,s5,s7=[log_rational(F(n)) for n in (2,3,4,5,7)]
    assert s5.hi<d<s7.lo and a<s3.lo and d<2*s3.lo
    assert s4.hi<d and s2.hi<a and d<3*s2.lo
    assert log_rational(F(8)).lo>d and log_rational(F(9)).lo>d
    delta_length=I(d)-s5
    gap1=s5-s3;gap2=2*s3-s5
    assert 0<delta_length.lo<delta_length.hi<min(gap1.lo,gap2.lo)
    A2=(s2/sqrt_rational(F(2))).hi;A4=s2.hi/2
    A3=s3/sqrt_rational(F(3));A5=s5/sqrt_rational(F(5))
    joint24=(A4+sqrt_rational(A4*A4+8*A2*A2).hi)/2
    joint35_formula=(A5.hi+sqrt_rational(A5.hi*A5.hi+4*A3.hi*A3.hi).hi)/2
    # A rational outward ceiling admits independent exact 4x4 PSD checks.
    grid=10**12;joint35=F(-(-joint35_formula*grid).__floor__(),grid)
    assert joint35>=joint35_formula
    B=[[F(0),A3.hi,F(0),F(0)],[A3.hi,F(0),A5.hi,F(0)],
       [F(0),A5.hi,F(0),A3.hi],[F(0),F(0),A3.hi,F(0)]]
    plus=exact_positive_pivots([[joint35*int(i==j)+B[i][j] for j in range(4)] for i in range(4)])
    minus=exact_positive_pivots([[joint35*int(i==j)-B[i][j] for j in range(4)] for i in range(4)])
    v=[A3.hi,joint35,joint35,A3.hi]
    norm=sum((x*x for x in v),F(0))
    actual_chain_quadratic_lower=4*A3.lo*v[0]*v[1]+2*A5.lo*v[1]*v[2]
    false_bound=joint35-F(1,10**6)
    negative_control_upper=false_bound*norm-actual_chain_quadratic_lower
    assert negative_control_upper<0 and joint35<A3.lo+A5.lo
    gamma_upper=sum((F(1,n) for n in range(1,101)),F(0))-log_rational(F(100)).lo
    assert gamma_upper<1
    arch_low=-gamma_upper-3*s2.hi-pi.hi/2-log_rational(pi.hi).hi
    assert arch_low>-F(27,5) and a/2<s2.lo
    loss=joint24+joint35
    rho=integrated_mass(a,k,T);pole=16*a*(a/2)**(2*k)/factorial(k)**2
    c=log_rational(T).lo-F(7,216)/T**2
    physical=c-(F(27,5)+c)*rho-pole-loss
    assert physical>F(51,100)
    rho_log=integrated_mass(a,k,Tlog)
    highgap=F(9,10)*log_rational(Tlog).lo-F(3,10)/Tlog-F(7,216)/Tlog**2-loss
    assert highgap>0
    logarithmic=F(1,10)-(F(27,5)+loss+F(3,10))*rho_log-pole
    assert logarithmic>F(9,100)
    return dict(status='certified uniform actual 84-moment complement through prime-5 activation',
        aperture_interval=['1/2','81/100'],physical_degrees=list(range(k)),prime_terms_at_upper_aperture=[2,3,4,5],
        physical_cutoff=str(T),logarithmic_cutoff=str(Tlog),physical_low_frequency_mass_upper=str(rho),
        logarithmic_low_frequency_mass_upper=str(rho_log),pole_absolute_upper=str(pole),
        archimedean_high_lower='log(abs(t))-7/(216t^2), abs(t)>=1',archimedean_global_lower=str(arch_low),
        archimedean_low_floor_used='-27/5',joint_prime24_operator_upper=str(joint24),
        joint_prime35_operator_upper=str(joint35),joint_prime35_formula='(A5+sqrt(A5^2+4*A3^2))/2',
        prime35_chain_vertex_offsets=['log(3)','0','log(5)','log(5)-log(3)'],
        prime35_chain_edge_amplitudes=['log(3)/sqrt(3)','log(5)/sqrt(5)','log(3)/sqrt(3)'],
        prime5_overlap_length_interval=[str(delta_length.lo),str(delta_length.hi)],
        positive_chain_bound_pivots=[str(x) for x in plus],negative_chain_bound_pivots=[str(x) for x in minus],
        too_small_chain_norm_control=str(false_bound),too_small_chain_norm_control_quadratic_upper=str(negative_control_upper),
        chain_norm_negative_control_rejected=True,independent_four_by_four_norm_check=True,
        physical_unrounded_lower=str(physical),physical_lower='51/100',complement_inverse_factor='100/51',
        logarithmic_high_symbol_gap_lower=str(highgap),logarithmic_unrounded_lower=str(logarithmic),logarithmic_lower='9/100',
        matching_finite_restriction_dimension_required=84,full_native_matrix_certified=False,
        full_actual_source_gram_certified=False,whole_domain_positivity=False,actual_negative_witness=False,
        global_endpoint_excluded=False,f4_entry_closed=False,full_transport_closed=False,lean_formalized=False)

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
