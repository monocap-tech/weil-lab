// IV240 exact rational multiplier and absorption checks; run from repository root.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
function audit(d,p){
const gcd=(a,b)=>b?gcd(b,a%b):a;const q=(n,d=1n)=>{let g=gcd(n<0n?-n:n,d);return {n:n/g,d:d/g}};const mul=(a,b)=>q(a.n*b.n,a.d*b.d);const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d);const lt=(a,b)=>a.n*b.d<b.n*a.d;const out=a=>({n:String(a.n),d:String(a.d)});const abs=x=>x<0n?-x:x;const ceil=(n,d)=>(n+d-1n)/d;
if(d.M!==16384||d.W!==1000000000||d.h.length!==d.M||d.shifts[0][0]!==2839||!d.h.every(x=>Number.isSafeInteger(x)&&x>0)||Math.max(...d.h)!==100000000)throw Error("frozen data");
let h=d.h.map(BigInt),B=100000000n,Q=1000000000n,sum=0n,min=h[0];for(let i=0;i<2840;i++){if(h[i]<min)min=h[i];if(i)sum+=ceil(Q*B*abs(h[i]-h[i-1]),h[i]*h[i-1]);}
const seam=ceil(Q*B,h[0])+ceil(Q*B,h[2839]);const v=q(sum,Q),j=q(sum+seam,Q),M=q(B,min);if(!lt(M,q(171n,100n))||!lt(j,q(63n,10n)))throw Error("multiplier constants");
const m=q(BigInt(Math.min(...d.h)),B),m2=mul(m,m),a2=q(9n,20n);if(!lt(q(15n),mul(q(225n),mul(m2,a2))))throw Error("chain bound");
const band=p.bands.find(b=>b.K===128);let b=q(BigInt(band.energy_coefficient.n),BigInt(band.energy_coefficient.d));if(!lt(q(6n),mul(q(4624n),b)))throw Error("mode bound");
let derivative=mul(q(399n,2000n),q(4n,128n)),jumpSq=mul(q(1029n,2000n),q(4n,128n));if(!lt(jumpSq,mul(q(127n,1000n),q(127n,1000n))))throw Error("jump");
let tail=mul(q(49n,20n),add(derivative,q(127n,1000n)));if(!lt(tail,q(1n,3n)))throw Error("absorption");if(!lt(mul(q(3n),mul(q(171n,100n),q(171n,100n))),q(9n)))throw Error("log coefficient");
return {base_cell_count:2840,base_minimum_weight:String(min),base_reciprocal_exact:out(M),internal_variation_upper:out(v),seam_upper:out(q(seam,Q)),jump_budget_upper:out(j),rounded_reciprocal_cap:out(q(171n,100n)),rounded_jump_cap:out(q(63n,10n)),iv239_band128_coefficient:out(b),chain_coefficient_upper:15,mode_coefficient_upper:68,derivative_tail_at_R4_K128:out(derivative),jump_tail_squared_at_R4_K128:out(jumpSq),sqrt6_tail_upper:out(tail),absorbed_distance_coefficient:out(q(2n,3n))};
}
const cell=readFileSync('custody/iv146-am/am_cells.json');
const modes=readFileSync('research/iv239_am_circle_modes.json');
if(createHash('sha256').update(cell).digest('hex')!=='2b149c79f469b594ce7c308e44c278da00e9e41fbd9da1436cad0b0dca9d294a')throw Error('cell digest');
if(createHash('sha1').update('blob '+modes.length+'\0').update(modes).digest('hex')!=='d2ce58d28af3a8ffdcc684cf89cebbef70e3cb25')throw Error('mode blob');
console.log(JSON.stringify(audit(JSON.parse(cell),JSON.parse(modes)),null,2));
