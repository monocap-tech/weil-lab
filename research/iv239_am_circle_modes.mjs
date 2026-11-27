// IV239 exact finite-mode interval bounds; run from repository root with Node.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
function audit(d){
const gcd=(a,b)=>b?gcd(b,a%b):a;const q=(n,d=1n)=>{let g=gcd(n<0n?-n:n,d);return {n:n/g,d:d/g}};
const add=(a,b)=>q(a.n*b.d+b.n*a.d,a.d*b.d),mul=(a,b)=>q(a.n*b.n,a.d*b.d),lt=(a,b)=>a.n*b.d<b.n*a.d;
const out=x=>({n:String(x.n),d:String(x.d),approx:Number(x.n)/Number(x.d)});
if(d.M!==16384||d.W!==1000000000||d.h.length!==d.M||d.shifts.length!==48||!d.h.every(x=>Number.isSafeInteger(x)&&x>0)||Math.max(...d.h)!==100000000)throw Error("input");
const rows=[{p:3,j:4499,u:634284101,lo:q(3n,5n),K:2},{p:5,j:6592,u:719762516,lo:q(7n,10n),K:3},{p:7,j:7970,u:735484905,lo:q(7n,10n),K:3}];if(d.shifts[0][0]!==2839||d.shifts[0][1]!==490129072)throw Error("a");
for(const r of rows){if(!d.shifts.some(([j,u])=>j===r.j&&u===r.u))throw Error("row"); if(BigInt(r.j+1)>=BigInt(r.K)*2839n)throw Error("K");if(r.j+1+2840>=16384)throw Error("overlap");}
let m=q(BigInt(Math.min(...d.h)),100000000n);let S=q(0n);for(const r of rows)S=add(S,q(BigInt(r.u)*BigInt(r.K),1000000000n));
let factor=add(q(1n),mul(S,q(20n,9n)));let coeff=mul(mul(m,m),q(factor.d,factor.n));
function dist(k,j){let L=BigInt(k*j),U=BigInt(k*(j+1)),a=2840n,b=2839n;let fl=L/a,fu=U/b;if(fl!==fu)return q(0n);let x=q(L-fl*a,a),y=q((fl+1n)*b-U,b);return lt(x,y)?x:y;}
let record=[],modes=[];let min=null;for(let k=1;k<=256;k++){let parts=rows.map(r=>{let z=dist(k,r.j);return {p:r.p,dist:out(z),value:mul(q(16n),mul(r.lo,mul(z,z)))}});let total=parts.reduce((a,b)=>add(a,b.value),q(0n));modes.push({k,distances:parts.map(({p,dist})=>({p,dist})),lambda:out(total)});if(!min||lt(total,min.v))min={k,v:total};if([8,16,32,64,128,256].includes(k))record.push({K:k,worst_mode:min.k,lambda:out(min.v),energy_coefficient:out(mul(coeff,min.v))});}
return {m:out(m),S:out(S),factor:out(factor),coefficient:out(coeff),bands:record,modes};
}
const bytes=readFileSync(process.argv[2]||'custody/iv146-am/am_cells.json');
if(createHash('sha256').update(bytes).digest('hex')!=='2b149c79f469b594ce7c308e44c278da00e9e41fbd9da1436cad0b0dca9d294a')throw Error('input digest');
console.log(JSON.stringify(audit(JSON.parse(bytes)),null,2));
