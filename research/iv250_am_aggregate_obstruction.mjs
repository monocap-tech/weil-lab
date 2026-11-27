// IV250: exact directed integer sign certificate, self-contained Node replay.
function audit(){
const S=10n**65n,fl=(n,d)=>{if(d<=0n)throw Error("den");return n>=0n?n/d:-((-n+d-1n)/d)},ce=(n,d)=>-fl(-n,d),I=(n,d=1n)=>[fl(n*S,d),ce(n*S,d)],add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[1],-a[0]],sub=(a,b)=>add(a,neg(b)),min=a=>a.reduce((x,y)=>x<y?x:y),max=a=>a.reduce((x,y)=>x>y?x:y),mul=(a,b)=>{let z=a.flatMap(x=>b.map(y=>x*y));return [fl(min(z),S),ce(max(z),S)]},div=(a,b)=>{if(b[1]<0n)return div(neg(a),neg(b));if(b[0]<=0n)throw Error("div");return [min(a.flatMap(x=>b.map(y=>fl(x*S,y)))),max(a.flatMap(x=>b.map(y=>ce(x*S,y))))]},pow=(x,n)=>{let y=I(1n);for(let k=0;k<n;k++)y=mul(y,x);return y},abs=a=>max([a[1],-a[0]]),fmt=a=>a.map(String);
function log(n,d=1n){let e=0n;while(n>=2n*d){d*=2n;e++}if(n<d)throw Error("log");function core(n,d){let u=n-d,v=n+d,L=0n,U=0n;for(let k=0;k<80;k++){let j=BigInt(2*k+1);L+=fl(2n*S*u**j,j*v**j);U+=ce(2n*S*u**j,j*v**j)}let j=161n;U+=ce(2n*S*u**j*v*v,j*v**j*(v*v-u*u));return [L,U]}return add(core(n,d),mul(I(e),core(2n,1n)))}
function atan(d){let a=I(0n);for(let k=0;k<60;k++){let j=BigInt(2*k+1);a=add(a,I(k%2?-1n:1n,j*d**j))}return add(a,[0n,ce(S,121n*d**121n)])}
const pi=sub(mul(I(16n),atan(5n)),mul(I(4n),atan(239n))),alpha=div(pi,I(4n)),lpi=[log(pi[0],S)[0],log(pi[1],S)[1]];
let e2=I(0n),fact=1n;for(let k=0n;k<=100n;k++){if(k)fact*=k;e2=add(e2,I(2n**k,fact))}e2=add(e2,[0n,ce(S*2n**101n*51n,fact*101n*50n)]);
const bern=[[1n,6n],[-1n,30n],[1n,42n],[-1n,30n],[5n,66n],[-691n,2730n],[7n,6n],[-3617n,510n]];
let H=I(0n),NN=1000n;for(let n=1n;n<=NN;n++)H=add(H,I(1n,n));
let eg=sub(sub(H,log(NN)),I(1n,2n*NN)),last;for(let k=1;k<=8;k++){let [bn,bd]=bern[k-1];last=I(bn,bd*BigInt(2*k)*NN**BigInt(2*k));eg=add(eg,last)}eg=add(eg,[-abs(last),abs(last)]);
const g0=neg(add(add(mul(I(3n),log(2n)),eg),add(div(pi,I(2n)),lpi)));
function isqrt(n){let l=0n,h=n+1n;while(h-l>1n){let m=(h+l)/2n;if(m*m<=n)l=m;else h=m}return l}
function trig(x){let period=mul(I(2n),pi),q=fl(x[0]+pi[0],period[0]),y=sub(x,mul(I(q),period));if(abs(y)>4n*S)throw Error("trig");let yy=mul(y,y),st=y,ct=I(1n),s=st,c=ct;for(let k=1n;k<50n;k++){st=neg(div(mul(st,yy),I(2n*k*(2n*k+1n))));ct=neg(div(mul(ct,yy),I((2n*k-1n)*2n*k)));s=add(s,st);c=add(c,ct)}let f=1n;for(let k=1n;k<=100n;k++)f*=k;let eps=ce(S*4n**100n,f);return [add(s,[-eps,eps]),add(c,[-eps,eps])]}
const j=Array.from({length:9},(_,i)=>BigInt(2*i)),r=j.map(k=>mul(I(k),alpha)),r2=r.map(x=>mul(x,x));
const zs=[14134725n,21022040n,25010858n,30424876n].map(x=>I(x*x,10n**12n));
const prod=a=>a.reduce(mul,I(1n)),D=div(prod(r2.slice(1)),prod(zs)),v=j.map((k,i)=>i===0?I(1n):div(mul(D,prod(zs.map(z=>sub(z,r2[i])))),prod(r2.filter((_,l)=>l!==i).map(z=>sub(z,r2[i])))));
const K=512n,A=I(4n*K+1n,4n);function zetaTail(p){let z=add(div(I(1n),mul(I(BigInt(p-1)),pow(A,p-1))),div(I(1n),mul(I(2n),pow(A,p))));let term;for(let k=1;k<=8;k++){let rise=1n,fac=1n;for(let q=0;q<2*k-1;q++)rise*=BigInt(p+q);for(let q=1;q<=2*k;q++)fac*=BigInt(q);let [bn,bd]=bern[k-1];term=div(I(bn*rise,bd*fac),pow(A,p+2*k-1));z=add(z,term)}return add(z,[-abs(term),abs(term)])}
let arch=I(0n),norm=I(0n);for(let i=0;i<v.length;i++){let nrm=mul(I(i?2n:4n),mul(v[i],v[i])),t=div(r2[i],I(4n)),g=g0;norm=add(norm,nrm);for(let n=0n;n<K;n++){let a=I(4n*n+1n,4n);g=add(g,div(t,mul(a,add(mul(a,a),t))))}let tail=I(0n);for(let l=1;l<=16;l++)tail=add(tail,mul(I(l%2?1n:-1n),mul(pow(t,l),zetaTail(2*l+1))));let err=mul(pow(t,17),zetaTail(35));g=add(g,add(tail,[0n,err[1]]));arch=add(arch,mul(nrm,g))}
const bank=[[2,2],[3,3],[4,2],[5,5],[7,7],[8,2],[9,3],[11,11],[13,13],[16,2],[17,17],[19,19],[23,23],[25,5],[27,3],[29,29],[31,31],[32,2],[37,37],[41,41],[43,43],[47,47],[49,7],[53,53]];
let P=I(0n);for(let [n,p] of bank){let s=log(BigInt(n)),z=isqrt(BigInt(n)*S*S),a=div(log(BigInt(p)),[z,z+1n]),tr=r.map(x=>trig(mul(x,s))),q=I(0n);for(let i=0;i<v.length;i++)for(let k=i;k<v.length;k++){let T=i===k?(i===0?mul(I(2n),sub(I(4n),s)):sub(mul(sub(I(4n),s),tr[i][1]),div(tr[i][0],r[i]))):div(mul(I(2n),sub(mul(I(j[k]),tr[k][0]),mul(I(j[i]),tr[i][0]))),mul(alpha,I(j[i]*j[i]-j[k]*j[k])));q=add(q,mul(mul(mul(v[i],v[k]),I(i===k?1n:2n)),T))}P=add(P,mul(a,q))}
let B=I(0n),loss=I(0n),E=div(I(1n),e2),ex=E;
for(let n=0;n<512;n++){let k=I(BigInt(4*n+1),2n),kk=mul(k,k),U=div(mul(D,prod(zs.map(z=>add(kk,z)))),prod(r2.map(z=>add(kk,z))));let factor=n===0?div(sub(e2,I(1n)),I(2n)):mul(mul(I(2n),kk),sub(I(1n),ex));let b=mul(factor,mul(U,U));B=add(B,b);if(n===4)loss=mul(b,ex);ex=mul(ex,pow(E,4))}
const T=I(2045n,2n);if(zs.some(z=>z[1]>=1000n*S)||T[0]<=1000n*S||pow(add(I(1n),I(1n,1000n)),4)[1]>=2n*S)throw Error("tail bound");
const tail=div(mul(I(4n),mul(D,D)),mul(I(17n),pow(T,17)));B=add(B,[0n,tail[1]]);
const Q=add(sub(arch,P),B),upper=sub(Q,loss);
if(Q[0]<=0n||Q[1]>=S/10n**26n||loss[0]<=2n*S/10n**25n||upper[1]>=-19n*S/10n**26n)throw Error("sign");
return {scale:String(S),modes:j.map(String),zero_selection_rational_numerators:["14134725","21022040","25010858","30424876"],zero_selection_denominator:"1000000",coefficients:v.map(fmt),norm:fmt(norm),gamma0:fmt(g0),arch:fmt(arch),prime:fmt(P),boundary_pole:fmt(B),boundary_tail_upper:String(tail[1]),original_Q:fmt(Q),first_omitted_weight_loss:fmt(loss),aggregate_upper:String(upper[1])}
}
console.log(JSON.stringify(audit(),null,2));
