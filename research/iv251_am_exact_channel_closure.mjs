// IV251: exact rational buffer coercivity and preconditioner checks.
// Inherited IV242 gamma lower at r=24576: 8036029850/10^9, blob 4507b04b760fc1652c63766bc762e21cfc96ae04.
function audit(){
 const S=1000000000n, r=24000n,N=64,t=r/2n;
 let gains=0n;for(let k=0;k<N;k++){let a=BigInt(4*k+1);gains+=S*64n*t*t/(a*(a*a+16n*t*t));}
 let n=BigInt(4*N+1)**2n+16n*t*t,d=BigInt(4*N+1)**2n,e=0n;while(n>=2n*d){d*=2n;e++;}
 function logLower(n,d){let u=n-d,v=n+d,s=0n;for(let k=0;k<12;k++){let j=BigInt(2*k+1);s+=2n*S*u**j/(j*v**j);}return s;}
 let tail=(e*logLower(2n,1n)+logLower(n,d))/2n;
 let gamma=-5600000000n+gains+tail, margin=gamma-7979648000n-1n;
 if(margin<=30000000n||4n*4n**4n*S>=3n**5n*31999n**3n)throw Error("buffer margin");
 let g=8036029850n;
 if(1000n*(g-7979648000n-1n)<=g+32n*S)throw Error("preconditioner");
 return {scale:String(S),gamma_lower:String(gamma),prefix_gain_lower:String(gains),half_tail_log_lower:String(tail),margin_lower:String(margin),buffer_start:32000,cutoff:32768,buffer_dimension:768,buffer_eta:"3/100",preconditioned_lower:"1/1000",preconditioned_upper:"1",K_norm_upper:"32"};
}
console.log(JSON.stringify(audit(),null,2));
