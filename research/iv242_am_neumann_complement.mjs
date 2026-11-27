// IV242 exact rational lower bound from the literal Gamma gain expansion.
// Run: node research/iv242_am_neumann_complement.mjs
function audit(){
 const Q=1000000000n, r=24576n,N=64, t=r/2n;
 const floor=(n,d)=>n/d;
 let gains=0n; for(let k=0;k<N;k++){let a=BigInt(4*k+1);gains+=floor(Q*64n*t*t,a*(a*a+16n*t*t));}
 let num=BigInt(4*N+1)**2n+16n*t*t,den=BigInt(4*N+1)**2n,e=0;
 while(num>=2n*den){den*=2n;e++;}
 if(num<den)throw Error("log normalization");
 function logLower(n,d){let u=n-d,v=n+d,s=0n;for(let k=0;k<12;k++){let j=BigInt(2*k+1);s+=floor(2n*Q*u**j,j*v**j);}return s;}
 let l2=logLower(2n,1n),lm=logLower(num,den),log=BigInt(e)*l2+lm;
 let gamma=-5600000000n+gains+log/2n;
 let margin=gamma-7979648000n;
 if(gamma<=8030000000n||margin<=50000000n||3n*32768n!==4n*r)throw Error("margin");
 return {scale:String(Q),r:Number(r),prefix_terms:N,log_power_of_two:e,log2_lower:String(l2),normalized_log_lower:String(lm),prefix_gain_lower:String(gains),half_tail_log_lower:String(log/2n),gamma_lower:String(gamma),margin_lower:String(margin),mode_cutoff:32768,complement_dimension_upper:32769,eta:"1/20"};
}
console.log(JSON.stringify(audit(),null,2));
