// IV247 exact witness-level penalty bounds + separate floating leading-term diagnostic.
// Run from repo root. Third input must be the pinned original source file.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
function audit(w,g,rows){
 const S=10n**15n, U=10n**9n, N=32768n, ce=(n,d)=>(n+d-1n)/d, abs=n=>n<0n?-n:n, fl=(n,d)=>n>=0n?n/d:-ce(-n,d);
 const v=w.coefficients.map(BigInt), ks=w.modes.map(BigInt);
 if(w.scale!==String(S)||g.scale!==String(S)||v.length!==20||ks.some((k,i)=>k!==2n*BigInt(i))||rows.length!==24)throw Error("inputs");
 const sum=v.reduce((a,b)=>a+b,0n),l1=v.reduce((a,b)=>a+abs(b),0n),w1=v.reduce((a,b,i)=>a+abs(b)*ks[i],0n),w2=v.reduce((a,b,i)=>a+abs(b)*ks[i]**2n,0n);
 if(sum!==1944n||l1!==96596n||w1>=1860000n||w2>=50360000n)throw Error("witness");
 const bank=rows.map(([n,j,u])=>[BigInt(n),BigInt(j),BigInt(u)]),A=bank.reduce((s,r)=>s+r[2],0n),A2=bank.reduce((s,r)=>s+r[2]**2n,0n);
 if(A>=12192000000n||A2*800n>629n*9n*U*U)throw Error("mean");
 function dist(l,u){let q=fl(l,16384n);if(fl(u,16384n)!==q)throw Error("phase meets integer");let a=l-q*16384n,b=(q+1n)*16384n-u,d=a<b?a:b;if(d<=0n)throw Error("phase zero");return d}
 let lin=0n,quad=0n,min=16384n;
 function phase(l,u){let d=dist(l,u);if(d<min)min=d;return d}
 for(let i=0;i<bank.length;i++){let [,k,a]=bank[i];lin+=ce(S*a*8192n,U*phase(k,k+1n));for(let j=0;j<bank.length;j++){let [,l,b]=bank[j];quad+=ce(S*a*b*4096n,U*U*phase(k+l,k+l+2n));if(i!==j)quad+=ce(S*a*b*4096n,U*U*phase(k-l-1n,k-l+1n));}}
 const osc=ce(8n*lin,3n)+ce(16n*quad,9n);
 if(osc>=1600n*S)throw Error("osc");
 if(8n*12192n*(186n*N+5036n)*N>=6100n*3n*1000n*(N*N-38n*38n)||2n*(186n*9n+8n*10n*16n)>=660n*9n||6100n+660n+860n>=10000n)throw Error("remainder");
 let lead=0n;const bands=[];
 for(let b=0;b<16;b++){let J=N*2n**BigInt(b),d=3n+40n*BigInt(b);
 let mass=ce(S*J,2n*(J-2n)*(2n*J-2n));let shell=ce(729n*mass,100n)+ce(1600n*S,J*J);
 let z=ce(2n*sum*sum*60n*shell,10000n**2n*d);lead+=z;if(b<8)bands.push({b,upper_scaled:String(z)})}
 let J=N*2n**16n;
 if(2n*sum*sum*(3n*1000n+4n*12192n)**2n>=24n*10000n**2n*(3n*1000n)**2n)throw Error("pointwise");
 lead+=ce(24n*60n*S,2n*(J-2n)*(3n+40n*16n));
 const rem=ce(20n*10000n**2n*S,6n*(N-2n)**3n);
 if(lead*100000n>=91n*S/10n||rem*10000000n>=95n*S)throw Error("penalty budgets");
 if(lead*100000n**2n>=954n**2n*S||rem*100000n**2n>=309n**2n*S||(954n+309n)**2n*100000n>=16n*100000n**2n)throw Error("combined");
 const q=BigInt(g.aggregate_witness_lower),pen=160000000000n;
 if(q<=pen)throw Error("witness failed");
 let diag=[];const coeff=rows.map(([n,j,u])=>{let p=2;while(n%p!==0)p++;return [Math.log(p)/Math.sqrt(n),Math.PI*Math.log(n)/4]});
 for(let b=0;b<4;b++){let J=Number(N)*2**b,d=.05+2*b/3,s=0;for(let j=J;j<2*J;j+=2){let x=1+coeff.reduce((s,[a,t])=>s+a*Math.sin(j*t)/(Math.PI/4),0);s+=2*.1944**2*x*x/(j*j*d)}diag.push({b,leading_penalty:s})}
 return {scale:String(S),coefficient_sum:String(sum),coefficient_l1:String(l1),weighted_l1:String(w1),weighted_l2_index_l1:String(w2),phase_min_numerator:String(min),oscillation_bound_scaled:String(osc),lead_upper_scaled:String(lead),remainder_upper_scaled:String(rem),combined_penalty_upper_scaled:String(pen),aggregate_lower_scaled:String(q),receiver_lower_scaled:String(q-pen),bands,diagnostic:diag};
}
const paths=["research/iv244_am_mixed_witness.json","research/iv245_am_aggregate_tail.json","WeilDefect/Arithmetic/ActualZetaIV152AMPhysicalEnvelope.lean"],pins=["3906416100c3b468066607c92eb5ac99f858e657","8c07b1db73dd2307016a41654bb573d2f4829066","d27bf0b67f80fb8797a948ce2928f5a3f39edcf5"];
if(process.argv[2])paths[2]=process.argv[2];
const a=paths.map((p,i)=>{const b=readFileSync(p);if(createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex')!==pins[i])throw Error('blob: '+p);return b.toString('utf8');});
const rows=[...a[2].matchAll(/^\s*\((\d+), (\d+), (\d+)\),?$/gm)].map(m=>m.slice(1).map(Number));
console.log(JSON.stringify(audit(JSON.parse(a[0]),JSON.parse(a[1]),rows),null,2));
