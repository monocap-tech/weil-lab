// IV246 exact constant audit; run from repo root.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
function audit(p,g){
const N=32768n,C=7979648000n,scale=1000000000n;
if(p.scale!==String(scale)||p.mode_cutoff!==Number(N)||BigInt(p.gamma_lower)!==8036029850n||g.epsilon_upper.d!=="232630513987207")throw Error("input");
const R=24576n,a=257n;
if(a*a*100000n>=4n*R*R*3n)throw Error("tail loss");
const margin=BigInt(p.gamma_lower)-C-15000n-1n;
if(margin<=50000000n)throw Error("base");
if(12191645931n*8n>=33n*3n*scale||43n>=65536n)throw Error("cross");
const bands=[];for(let b=0;b<=8;b++){let J=N*2n**BigInt(b),d=3n+40n*BigInt(b);bands.push({b,start:String(J),weight:{n:"60",d:String(d)},improvement:{n:String(d),d:"3"}})}
return {N:String(N),gamma_tail_loss_upper:"3/200000",pole_loss_upper:"1/10000000000",base_margin_lower_scaled:String(margin),denominator_scale:String(scale),dyadic_bands:bands,entry_tail_constant:36};
}
const paths=["research/iv242_am_neumann_complement.json","research/iv245_am_aggregate_tail.json"],pins=["4507b04b760fc1652c63766bc762e21cfc96ae04","8c07b1db73dd2307016a41654bb573d2f4829066"];
const x=paths.map((p,i)=>{let b=readFileSync(p);if(createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex')!==pins[i])throw Error('blob');return JSON.parse(b);});
console.log(JSON.stringify(audit(...x),null,2));
