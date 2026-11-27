// IV248: rigorous interval test of the trace-zero even near-null witness. Node standalone.
function audit(){
const S=10n**32n, fl=(n,d)=>{if(d<=0n)throw Error("den");return n>=0n?n/d:-((-n+d-1n)/d)},ce=(n,d)=>-fl(-n,d),I=(n,d=1n)=>[fl(n*S,d),ce(n*S,d)],add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[1],-a[0]],sub=(a,b)=>add(a,neg(b)),min=a=>a.reduce((x,y)=>x<y?x:y),max=a=>a.reduce((x,y)=>x>y?x:y),mul=(a,b)=>{let z=a.flatMap(x=>b.map(y=>x*y));return [fl(min(z),S),ce(max(z),S)]},div=(a,b)=>{if(b[1]<0n)return div(neg(a),neg(b));if(b[0]<=0n)throw Error("div");return [min(a.flatMap(x=>b.map(y=>fl(x*S,y)))),max(a.flatMap(x=>b.map(y=>ce(x*S,y))))]},pow=(x,n)=>{let y=I(1n);for(let k=0;k<n;k++)y=mul(y,x);return y},abs=a=>max([a[1],-a[0]]),fmt=a=>a.map(String);
function log(n,d=1n){let e=0n;while(n>=2n*d){d*=2n;e++}if(n<d)throw Error("log");function core(n,d){let u=n-d,v=n+d,L=0n,U=0n;for(let k=0;k<40;k++){let j=BigInt(2*k+1);L+=fl(2n*S*u**j,j*v**j);U+=ce(2n*S*u**j,j*v**j)}let j=81n;U+=ce(2n*S*u**j*v*v,j*v**j*(v*v-u*u));return [L,U]}let a=core(n,d),b=core(2n,1n);return add(a,mul(I(e),b))}
function atan(d){let a=I(0n);for(let k=0;k<30;k++){let j=BigInt(2*k+1);a=add(a,I(k%2?-1n:1n,j*d**j))}return add(a,[0n,ce(S,61n*d**61n)])}
const pi=sub(mul(I(16n),atan(5n)),mul(I(4n),atan(239n))),alpha=div(pi,I(4n)),lpi=[log(pi[0],S)[0],log(pi[1],S)[1]];
let e2=I(0n),fact=1n;for(let k=0n;k<=48n;k++){if(k)fact*=k;e2=add(e2,I(2n**k,fact))}e2=add(e2,[0n,ce(S*2n**49n*25n,fact*49n*24n)]);
let H=I(0n),N0=1000n;for(let n=1n;n<=N0;n++)H=add(H,I(1n,n));
let eg=add(sub(sub(H,log(N0)),I(1n,2n*N0)),add(I(1n,12n*N0**2n),add(I(-1n,120n*N0**4n),I(1n,252n*N0**6n))));
eg=add(eg,[-ce(2n*S,240n*N0**8n),ce(2n*S,240n*N0**8n)]);
const g0=neg(add(add(mul(I(3n),log(2n)),eg),add(div(pi,I(2n)),lpi)));
function isqrt(n){let l=0n,h=n+1n;while(h-l>1n){let m=(l+h)/2n;if(m*m<=n)l=m;else h=m}return l}
function trig(x){let period=mul(I(2n),pi),q=fl(x[0]+pi[0],period[0]),y=sub(x,mul(I(q),period));if(abs(y)>4n*S)throw Error("trig");let yy=mul(y,y);
let st=y,ct=I(1n),s=st,c=ct;for(let k=1n;k<32n;k++){st=neg(div(mul(st,yy),I(2n*k*(2n*k+1n))));ct=neg(div(mul(ct,yy),I((2n*k-1n)*2n*k)));s=add(s,st);c=add(c,ct)}let f=1n;for(let k=1n;k<=64n;k++)f*=k;let eps=ce(S*4n**64n,f);return [add(s,[-eps,eps]),add(c,[-eps,eps])]}
const v=[I(1n),I(-3n,2n),I(3n,5n),I(-1n,10n)],j=[0n,2n,4n,6n],r=j.map(k=>mul(I(k),alpha)),r2=r.map(x=>mul(x,x));
const K=128n,a0=4n*K+1n;
function zetaTail(p){let A=I(a0,4n),z=add(div(I(1n),mul(I(BigInt(p-1)),pow(A,p-1))),div(I(1n),mul(I(2n),pow(A,p))));let last;
const bs=[[1n,12n],[-1n,720n],[1n,30240n],[-1n,1209600n]];
for(let k=1;k<=4;k++){let rise=1n;for(let q=0;q<2*k-1;q++)rise*=BigInt(p+q);last=div(I(bs[k-1][0]*rise,bs[k-1][1]),pow(A,p+2*k-1));z=add(z,last)}
return add(z,[-abs(last),abs(last)])}
let arch=I(0n),norm=I(0n);
for(let i=0;i<4;i++){let nrm=mul(I(i?2n:4n),mul(v[i],v[i])),t=div(r2[i],I(4n)),g=g0;norm=add(norm,nrm);for(let n=0n;n<K;n++){let a=I(4n*n+1n,4n);g=add(g,div(t,mul(a,add(mul(a,a),t))))}let tail=I(0n);for(let l=1;l<=8;l++)tail=add(tail,mul(I(l%2?1n:-1n),mul(pow(t,l),zetaTail(2*l+1))));let err=mul(pow(t,9),zetaTail(19));g=add(g,add(tail,[0n,err[1]]));arch=add(arch,mul(nrm,g))}
const bank=[[2,2],[3,3],[4,2],[5,5],[7,7],[8,2],[9,3],[11,11],[13,13],[16,2],[17,17],[19,19],[23,23],[25,5],[27,3],[29,29],[31,31],[32,2],[37,37],[41,41],[43,43],[47,47],[49,7],[53,53]];
let P=I(0n),primeChannel=I(0n);
for(let [n,p] of bank){let s=log(BigInt(n)),z=isqrt(BigInt(n)*S*S),a=div(log(BigInt(p)),[z,z+1n]),tr=r.map(x=>trig(mul(x,s))),q=I(0n),ch=I(0n);for(let i=0;i<4;i++){ch=add(ch,mul(mul(v[i],I(j[i])),tr[i][0]));for(let k=i;k<4;k++){let T=i===k?(i===0?mul(I(2n),sub(I(4n),s)):sub(mul(sub(I(4n),s),tr[i][1]),div(tr[i][0],r[i]))):div(mul(I(2n),sub(mul(I(j[k]),tr[k][0]),mul(I(j[i]),tr[i][0]))),mul(alpha,I(j[i]*j[i]-j[k]*j[k])));q=add(q,mul(mul(mul(v[i],v[k]),I(i===k?1n:2n)),T))}}P=add(P,mul(a,q));primeChannel=add(primeChannel,mul(a,ch))}
const D=mul(mul(r2[1],r2[2]),r2[3]);let B=I(0n),Bch=I(0n),E=div(I(1n),e2),exp=E;
for(let n=0;n<128;n++){let k=I(BigInt(4*n+1),2n),kk=mul(k,k),U=div(D,mul(kk,mul(add(kk,r2[1]),mul(add(kk,r2[2]),add(kk,r2[3])))));let factor=n===0?div(sub(e2,I(1n)),I(2n)):mul(mul(I(2n),kk),sub(I(1n),exp));B=add(B,mul(factor,mul(U,U)));let fAgg=n<4?factor:mul(mul(I(2n),kk),pow(sub(I(1n),exp),2));Bch=add(Bch,mul(fAgg,U));exp=mul(exp,pow(E,4))}
let tailB=div(mul(D,D),mul(I(13n),pow(I(509n,2n),13))),tailCh=div(D,mul(I(5n),pow(I(509n,2n),5)));
B=add(B,[0n,tailB[1]]);Bch=add(Bch,[0n,tailCh[1]]);
const sqrt2=[isqrt(2n*S*S),isqrt(2n*S*S)+1n],beta=sub(div(Bch,mul(sqrt2,mul(alpha,alpha))),div(mul(sqrt2,primeChannel),alpha)),Q=add(sub(arch,P),B),delta=I(4n,232630513987206n),aggLower=sub(Q,mul(delta,norm));
if(Q[0]<=7n*S/10n**13n||Q[1]>=8n*S/10n**13n||aggLower[0]<=5n*S/10n**13n||abs(beta)>=S/10000n)throw Error("sign or channel");
const W2=I(96n,5n),W0=I(16n,5n),rem=add(mul(I(70n),W2),div(mul(I(16n),W0),I(32768n))),NN=32766n;
const pLead=div(I(20n,10000n**2n),I(6n*NN**3n)),pRem=div(mul(I(20n),mul(rem,rem)),I(10n*NN**5n));
const penalty=mul(I(2n),add(pLead,pRem)),receiver=sub(aggLower,penalty);
if(penalty[1]>=S/10n**15n||receiver[0]<=5n*S/10n**13n)throw Error("receiver");
return {scale:String(S),norm:fmt(norm),gamma0:fmt(g0),arch:fmt(arch),prime:fmt(P),boundary_pole:fmt(B),original_Q:fmt(Q),aggregate_lower:fmt(aggLower),second_channel:fmt(beta),prime_channel_scaled:fmt(neg(div(mul(sqrt2,primeChannel),alpha))),boundary_channel_scaled:fmt(div(Bch,mul(sqrt2,mul(alpha,alpha)))),penalty:fmt(penalty),receiver_lower:fmt(receiver)};
}
console.log(JSON.stringify(audit(),null,2));
