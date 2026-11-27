#!/usr/bin/env node
// Exact integer outward pilot; no native admissions or moment evaluations.
// Usage: node scripts/local_replay/NF618W02EndpointPower.cjs <repo-root>
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const b=fs.readFileSync(path.join(process.argv[2]||".","notes/provisional/NF618W02ResidualSupport.json"));
const id=crypto.createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex");
if(id!=="90b71e032264cf18d4febac3c11d804fb6a9f4ec")throw Error("pinned input mismatch");
function pilot(rows){
 const need=(b,m)=>{if(!b)throw Error(m)}, abs=x=>x<0n?-x:x, Q=10n**2600n,N=1200,M=2000;
 const floor=(a,b)=>{need(b>0n,"den");let d=a/b;return a%b<0n?d-1n:d},ceil=(a,b)=>-floor(-a,b);
 const exact=(a,b=1n)=>{let m=floor(a*Q,b);return [m,a*Q===m*b?0n:1n]};
 const add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[0],a[1]];
 const mul=(a,b)=>[floor(a[0]*b[0],Q),ceil(abs(a[0])*b[1]+abs(b[0])*a[1]+a[1]*b[1],Q)+1n];
 const div=(a,k)=>[floor(a[0],k),ceil(a[1],k)+1n];
 const zero=[0n,0n],one=[Q,0n],Z=[zero,zero],O=[one,zero];
 const za=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])],zm=(a,b)=>[add(mul(a[0],b[0]),neg(mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
 const cj=a=>[a[0],neg(a[1])],rot=a=>[neg(a[1]),a[0]],upper=a=>abs(a[0])+a[1];
 let fac=1n;for(let n=1;n<=N;n++)fac*=BigInt(n);need(2n*Q<=fac,"exp tail");
 function atan(p){let power=p,s=zero;for(let n=0;n<M;n++){s=add(s,exact(n%2?-1n:1n,power*BigInt(2*n+1)));power*=p*p}need(Q<=power*BigInt(2*M+1),"atan tail");return [s[0],s[1]+1n]}
 const pi=add(mul(exact(16n),atan(5n)),neg(mul(exact(4n),atan(239n))));
 function small(z){need(upper(z[0])+upper(z[1])<=Q,"small exp norm");let s=Z,t=O;for(let n=0;n<N;n++){s=za(s,t);if(n+1<N){const u=zm(t,z);t=u.map(a=>div(a,BigInt(n+1)))}}return s.map(a=>[a[0],a[1]+1n])}
 const root=small([zero,mul(pi,exact(1n,640n))]);
 const powers=[O,root];for(let r=2;r<=160;r++)powers.push(zm(powers[r-1],root));
 const mod=(n,m)=>(n%m+m)%m;
 function phase(p){p=mod(p,1280);let j=Math.floor((p+160)/320),r=p-320*j;let v=powers[Math.abs(r)];if(r<0)v=cj(v);for(let k=0;k<j%4;k++)v=rot(v);return v}
 const realpos=small([exact(11n,20n),zero]);
 const a=realpos[0],lo=a[0]-a[1],hi=a[0]+a[1];need(lo>0n,"positive exp");const L=floor(Q*Q,hi),U=ceil(Q*Q,lo);const c=floor(L+U,2n),r=U-c>c-L?U-c:c-L;
 const realneg=[[c,r],zero],realp=[a,zero];
 const real={"-2":zm(realneg,realneg),"-1":realneg,"0":O,"1":realp,"2":zm(realp,realp)};
 const raw=new Set([0]),rep=new Set([0]),hs=new Set(),endpoints=new Set();for(const row of rows)for(const s of [-1,1]){const p=mod(s*row[2],1280),h=s*row[1];raw.add(p);const q=mod(p,320);rep.add(Math.min(q,320-q));hs.add(h);endpoints.add(h+","+p)}
 const radiusExp=v=>Math.max(...v.map(a=>a[1]===0n?-Infinity:a[1].toString().length-2600));
 const overlap=(a,b)=>a.every((x,i)=>abs(x[0]-b[i][0])<=x[1]+b[i][1]);
 const samples=[0,1,159,160,161,319,320,639,640,641,959,1279];
 const checks=samples.map(p=>{let u=p>=640?p-1280:p;let t=small([zero,mul(pi,exact(BigInt(u),2560n))]);t=zm(t,t);t=zm(t,t);need(overlap(phase(p),t),"phase sample "+p);return {p,sharedRadiusExponent:Number.isFinite(radiusExp(phase(p)))?radiusExp(phase(p)):null,directRadiusExponent:radiusExp(t)}});
 const phaseMax=Math.max(...[...raw].map(p=>radiusExp(phase(p))));
 const endMax=Math.max(...[...endpoints].map(k=>{let [h,p]=k.split(",").map(Number);return radiusExp(zm(real[h],phase(p)))}));
 for(let n=0;n<=26;n++){let v=1n,cs=Array(n+1);for(let k=n;k>=0;k--){cs[k]=v;v=-v*BigInt(k)}for(let k=0;k<=n;k++)need(cs[k]+(k<n?BigInt(k+1)*cs[k+1]:0n)===(k===n?1n:0n),"primitive coefficient identity")}
 return {scale:"10^2600",N,M,phaseResidues:raw.size,octantRepresentatives:rep.size,realHalfExponentUnits:[...hs].sort((a,b)=>a-b),endpointPairs:endpoints.size,phaseTaylorSeeds:1,realTaylorSeeds:1,phasePowerMultiplications:159,phaseMaxRadiusExponent:phaseMax,endpointMaxRadiusExponent:endMax,independentTaylorComparisons:checks,primitiveDegreesChecked:27,scope:"external fixed-point outward enclosure; comparisons share pi; no moment rows or original frame evaluated"}
}
console.log(JSON.stringify(pilot(JSON.parse(b.toString("utf8")).ordinary.rows),null,2));
