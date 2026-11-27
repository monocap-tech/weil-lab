// IV249 exact near-cutoff negative receiver witness. Run from repo root; optional argv[2] is pinned original Lean file.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
function audit(prior,rows){
const S=10n**25n, fl=(n,d)=>{if(d<=0n)throw Error("den");return n>=0n?n/d:-((-n+d-1n)/d)},ce=(n,d)=>-fl(-n,d),I=(n,d=1n)=>[fl(n*S,d),ce(n*S,d)],add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[1],-a[0]],sub=(a,b)=>add(a,neg(b)),min=a=>a.reduce((x,y)=>x<y?x:y),max=a=>a.reduce((x,y)=>x>y?x:y),mul=(a,b)=>{let z=a.flatMap(x=>b.map(y=>x*y));return [fl(min(z),S),ce(max(z),S)]},div=(a,b)=>{if(b[1]<0n)return div(neg(a),neg(b));if(b[0]<=0n)throw Error("div");return [min(a.flatMap(x=>b.map(y=>fl(x*S,y)))),max(a.flatMap(x=>b.map(y=>ce(x*S,y))))]},abs=a=>max([a[1],-a[0]]),fmt=a=>a.map(String);
function log(n,d=1n){let e=0n;while(n>=2n*d){d*=2n;e++}if(n<d)throw Error("log");function core(n,d){let u=n-d,v=n+d,L=0n,U=0n;for(let k=0;k<40;k++){let j=BigInt(2*k+1);L+=fl(2n*S*u**j,j*v**j);U+=ce(2n*S*u**j,j*v**j)}let j=81n;U+=ce(2n*S*u**j*v*v,j*v**j*(v*v-u*u));return [L,U]}return add(core(n,d),mul(I(e),core(2n,1n)))}
function atan(d){let a=I(0n);for(let k=0;k<30;k++){let j=BigInt(2*k+1);a=add(a,I(k%2?-1n:1n,j*d**j))}return add(a,[0n,ce(S,61n*d**61n)])}
const pi=sub(mul(I(16n),atan(5n)),mul(I(4n),atan(239n))),alpha=div(pi,I(4n));
function sqrt(n){let l=0n,h=n+1n;while(h-l>1n){let m=(l+h)/2n;if(m*m<=n)l=m;else h=m}return l}
function trig(x){let period=mul(I(2n),pi),q=fl(x[0]+pi[0],period[0]),y=sub(x,mul(I(q),period));if(abs(y)>4n*S)throw Error("range");let yy=mul(y,y),st=y,ct=I(1n),s=st,c=ct;for(let k=1n;k<32n;k++){st=neg(div(mul(st,yy),I(2n*k*(2n*k+1n))));ct=neg(div(mul(ct,yy),I((2n*k-1n)*2n*k)));s=add(s,st);c=add(c,ct)}let f=1n;for(let k=1n;k<=64n;k++)f*=k;let eps=ce(S*4n**64n,f);return [add(s,[-eps,eps]),add(c,[-eps,eps])]}
if(prior.scale!=="1000000000000000"||BigInt(prior.gamma0[1])>=-5370000000000000n||BigInt(prior.e2[1])>=9n*10n**15n||rows.length!==24)throw Error("inputs");
const ns=rows.map(r=>Number(r[0]));if(ns.join(",")!=="2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53")throw Error("bank");
let A=rows.reduce((s,r)=>s+BigInt(r[2]),0n);if(A>=12192000000n)throw Error("cap");
let prefix=I(0n);for(let n=0n;n<64n;n++)prefix=add(prefix,I(4n,4n*n+1n));
let gammaUpper=add(I(-537n,100n),add(prefix,add(I(4n,257n),mul(I(17n,2n),log(2n)))));
if(pi[0]<=3n*S||pi[1]>=4n*S||gammaUpper[1]>=9n*S)throw Error("gamma");
const k=32766n,N=32768n,bank=ns.map(n=>{let p=2;while(n%p!==0)p++;const z=sqrt(BigInt(n)*S*S),s=log(BigInt(n)),theta=mul(alpha,s);return {n,s,theta,a:div(log(BigInt(p)),[z,z+1n]),tr:trig(mul(I(k),theta))}});
let diag=I(0n);for(const b of bank){let t=div(sub(mul(sub(I(4n),b.s),b.tr[1]),div(b.tr[0],mul(I(k),alpha))),I(2n));diag=add(diag,mul(b.a,t))}
function err(j){return add(I(2n,j),I(43n,j*j))}
const diagBound=err(k),Qupper=add(sub([gammaUpper[1],gammaUpper[1]],diag),[0n,diagBound[1]])[1];
let pen=I(0n),cross=[];
for(let j=N;j<=N+16n;j+=2n){let p=I(0n);for(const b of bank){let t=trig(mul(I(j),b.theta))[0],q=div(sub(mul(I(k),b.tr[0]),mul(I(j),t)),mul(alpha,I(j*j-k*k)));p=add(p,mul(b.a,q))}let al=p[0]>0n?p[0]:p[1]<0n?-p[1]:0n;let loss=err(j)[1];let lo=al>loss?al-loss:0n;let term=fl(20n*lo*lo,S);pen[0]+=term;pen[1]+=term;cross.push({j:String(j),prime:fmt(p),boundary_pole_abs_upper:String(loss),K_abs_lower:String(lo),penalty_lower:String(term)})}
const receiver=Qupper-pen[0];if(diag[0]<=198n*S/100n||Qupper>=71n*S/10n||pen[0]<=75n*S/10n||receiver>=-4n*S/10n)throw Error("receiver sign");
return {scale:String(S),low_mode:String(k),high_modes:cross,gamma_upper:String(gammaUpper[1]),prime_diagonal:fmt(diag),boundary_pole_diagonal_abs_upper:String(diagBound[1]),aggregate_Q_upper:String(Qupper),partial_penalty_lower:String(pen[0]),receiver_upper:String(receiver)};
}
const paths=["research/iv243_am_structured_receiver.json","WeilDefect/Arithmetic/ActualZetaIV152AMPhysicalEnvelope.lean"],pins=["f83acc6c0e2caf3e05815c3dea219c8ad1774ddb","d27bf0b67f80fb8797a948ce2928f5a3f39edcf5"];if(process.argv[2])paths[1]=process.argv[2];const a=paths.map((p,i)=>{const b=readFileSync(p);if(createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex')!==pins[i])throw Error('blob '+p);return b.toString('utf8')});const rows=[...a[1].matchAll(/^\s*\((\d+), (\d+), (\d+)\),?$/gm)].map(m=>m.slice(1));console.log(JSON.stringify(audit(JSON.parse(a[0]).exact,rows),null,2));
