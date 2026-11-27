// IV244: exact directed integer intervals for a rational mixed even-mode witness.
// Run from repository root: node research/iv244_am_mixed_witness.mjs
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
function audit(prev){
 const S=10n**15n, floor=(n,d)=>{if(d<=0n)throw Error("den");return n>=0n?n/d:-((-n+d-1n)/d)},ceil=(n,d)=>-floor(-n,d);
 const I=(n,d=1n)=>[floor(n*S,d),ceil(n*S,d)], add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[1],-a[0]],sub=(a,b)=>add(a,neg(b));
 const lo=a=>a.reduce((x,y)=>x<y?x:y),hi=a=>a.reduce((x,y)=>x>y?x:y);
 const mul=(a,b)=>{let z=a.flatMap(x=>b.map(y=>x*y));return [floor(lo(z),S),ceil(hi(z),S)]},div=(a,b)=>{if(b[1]<0n)return div(neg(a),neg(b));if(b[0]<=0n)throw Error("division by zero interval");let l=a.flatMap(x=>b.map(y=>floor(x*S,y))),u=a.flatMap(x=>b.map(y=>ceil(x*S,y)));return [lo(l),hi(u)]};
 const sq=a=>{let l=a[0]*a[0],u=a[1]*a[1];return [a[0]<=0n&&a[1]>=0n?0n:floor(l<u?l:u,S),ceil(l>u?l:u,S)]};
 const isqrt=n=>{let l=0n,h=n+1n;while(h-l>1n){let m=(l+h)/2n;if(m*m<=n)l=m;else h=m}return l};
 function logI(n,d=1n){let k=0n;while(n>=2n*d){d*=2n;k++}if(n<d)throw Error("log arg");function core(n,d){let u=n-d,v=n+d,L=0n,U=0n;for(let j=0;j<24;j++){let z=BigInt(2*j+1),a=2n*S*u**z,b=z*v**z;L+=floor(a,b);U+=ceil(a,b)}let z=49n;U+=ceil(2n*S*u**z*v*v,z*v**z*(v*v-u*u));return [L,U]}let l2=core(2n,1n),l=core(n,d);return [l[0]+k*l2[0],l[1]+k*l2[1]]}
 const pi=prev.pi.map(BigInt),e2=prev.e2.map(BigInt);if(prev.scale!==String(S)||pi[0]<=3n*S||pi[1]>=4n*S||e2[0]<=7n*S)throw Error("input");
 const alpha=div(pi,I(4n)),l2=logI(2n),lp=[logI(pi[0],S)[0],logI(pi[1],S)[1]];
 let H=I(0n),N=10000n;for(let n=1n;n<=N;n++)H=add(H,I(1n,n));
 let eg=sub(sub(H,logI(N)),[I(1n,2n*(N+1n))[0],I(1n,2n*N)[1]]);
 let g0=neg(add(add(mul(I(3n),l2),eg),add(div(pi,I(2n)),lp)));
 const v=[7272,7078,6501,5563,4297,2752,992,-900,-2821,29,-6167,-7219,-7355,-3904,-9933,-5497,-1765,4786,10000,-1765].map(x=>I(BigInt(x),10000n));const j=v.map((_,i)=>BigInt(2*i)),r=j.map(k=>mul(I(k),alpha)),r2=r.map(sq);
 let norm=I(0n),arch=I(0n);const K=4096n;
 for(let i=0;i<v.length;i++){let nrm=mul(I(i?2n:4n),sq(v[i]));norm=add(norm,nrm);let t=div(r2[i],I(4n));let g=g0;for(let n=0n;n<K;n++){let a=I(4n*n+1n,4n);g=add(g,div(t,mul(a,add(sq(a),t))))}let tail=div(t,mul(I(2n),sq(I(4n*K-3n,4n))));g=add(g,[0n,tail[1]]);arch=add(arch,mul(nrm,g))}
 function trig(x){let period=mul(I(2n),pi);let q=floor(x[0]+pi[0],period[0]);let y=sub(x,mul(I(q),period));if(y[0]<-4n*S||y[1]>4n*S)throw Error("range reduction");let yy=sq(y),st=y,ct=I(1n),s=st,c=ct;for(let k=1n;k<24n;k++){st=neg(div(mul(st,yy),I(2n*k*(2n*k+1n))));ct=neg(div(mul(ct,yy),I((2n*k-1n)*2n*k)));s=add(s,st);c=add(c,ct)}let fact=1n;for(let k=1n;k<=48n;k++)fact*=k;let eps=ceil(S*4n**48n,fact);return [add(s,[-eps,eps]),add(c,[-eps,eps])]}
 const bank=[[2,2],[3,3],[4,2],[5,5],[7,7],[8,2],[9,3],[11,11],[13,13],[16,2],[17,17],[19,19],[23,23],[25,5],[27,3],[29,29],[31,31],[32,2],[37,37],[41,41],[43,43],[47,47],[49,7],[53,53]];
 let P=I(0n);for(let [n,p] of bank){let s=logI(BigInt(n)),l=logI(BigInt(p)),z=isqrt(BigInt(n)*S*S),a=div(l,[z,z+1n]),tr=r.map(x=>trig(mul(x,s)));let q=I(0n);for(let u=0;u<v.length;u++)for(let k=u;k<v.length;k++){let T;if(u===k)T=u===0?mul(I(2n),sub(I(4n),s)):sub(mul(sub(I(4n),s),tr[u][1]),div(tr[u][0],r[u]));else T=div(mul(I(2n),sub(mul(I(j[k]),tr[k][0]),mul(I(j[u]),tr[u][0]))),mul(alpha,I(j[u]*j[u]-j[k]*j[k])));q=add(q,mul(mul(mul(v[u],v[k]),I(u===k?1n:2n)),T))}P=add(P,mul(a,q))}
 let b=I(0n),pow=I(1n),inv=div(I(1n),e2);const rows=[];
 for(let n=0;n<128;n++){let k=I(BigInt(4*n+1),2n),kk=sq(k),moment=I(0n);for(let i=0;i<v.length;i++)moment=add(moment,div(v[i],add(kk,r2[i])));let factor;if(n===0){factor=div(sub(e2,I(1n)),I(2n));pow=inv;}else{for(let t=0;t<4;t++)pow=mul(pow,inv);factor=mul(mul(I(2n),kk),sub(I(1n),pow))}b=add(b,mul(factor,sq(moment)));if([8,16,32,64,128].includes(n+1))rows.push({m:n+1,upper:String(add(sub(arch,P),b)[1]),lower:String(add(sub(arch,P),b)[0])})}
 if(BigInt(rows.find(x=>x.m===32).upper)>=0n)throw Error("Q32 not certified");
 return {scale:String(S),coefficients:v.map(x=>String(x[0]/(S/10000n))),modes:j.map(Number),norm:norm.map(String),gamma0:g0.map(String),arch:arch.map(String),prime:P.map(String),rows};
}
const bytes=readFileSync('research/iv243_am_structured_receiver.json');
if(createHash('sha1').update('blob '+bytes.length+'\0').update(bytes).digest('hex')!=='f83acc6c0e2caf3e05815c3dea219c8ad1774ddb')throw Error('input blob');
console.log(JSON.stringify(audit(JSON.parse(bytes).exact),null,2));
