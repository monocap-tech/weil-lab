// IV253: exact directed-interval finite compression and rational congruence audit.
// Run node research/iv253_am_exact_compression.mjs from any directory.
// Original prime bank and normalization inherited from pinned IV251 / IV252; source census checked during delivery.
function run(P=220,J=128){
const S=10n**BigInt(P),fl=(n,d)=>{if(d<0n)return fl(-n,-d);if(!d)throw Error("zero");return n>=0n?n/d:-((-n+d-1n)/d)},ce=(n,d)=>-fl(-n,d),I=(n,d=1n)=>[fl(n*S,d),ce(n*S,d)],add=(a,b)=>[a[0]+b[0],a[1]+b[1]],neg=a=>[-a[1],-a[0]],sub=(a,b)=>add(a,neg(b)),min=a=>a.reduce((x,y)=>x<y?x:y),max=a=>a.reduce((x,y)=>x>y?x:y),mul=(a,b)=>{let z=a.flatMap(x=>b.map(y=>x*y));return [fl(min(z),S),ce(max(z),S)]},div=(a,b)=>{if(b[1]<0n)return div(neg(a),neg(b));if(b[0]<=0n)throw Error("div");return [min(a.flatMap(x=>b.map(y=>fl(x*S,y)))),max(a.flatMap(x=>b.map(y=>ce(x*S,y))))]},abs=a=>max([a[1],-a[0]]),fmt=a=>a.map(String),rat=(a,n,d)=>n<0n?neg(rat(a,-n,d)):[fl(a[0]*n,d),ce(a[1]*n,d)],Z=I(0n),one=I(1n);
const fac=[1n];for(let k=1;k<=500;k++)fac.push(fac[k-1]*BigInt(k));
function log(n,d=1n){let e=0n;while(n>=2n*d){d*=2n;e++}if(n<d)throw Error("log");function core(n,d){let u=n-d,v=n+d,L=0n,U=0n,up=u,vp=v;for(let k=0;k<260;k++){let j=BigInt(2*k+1);L+=fl(2n*S*up,j*vp);U+=ce(2n*S*up,j*vp);up*=u*u;vp*=v*v}let j=521n;U+=ce(2n*S*up*v*v,j*vp*(v*v-u*u));return [L,U]}return add(core(n,d),rat(core(2n,1n),e,1n))}
function atan(d){let a=Z;for(let k=0;k<180;k++){let j=BigInt(2*k+1);a=add(a,I(k%2?-1n:1n,j*d**j))}return add(a,[0n,ce(S,361n*d**361n)])}
const pi=sub(rat(atan(5n),16n,1n),rat(atan(239n),4n,1n)),alpha=rat(pi,1n,4n),lpi=[log(pi[0],S)[0],log(pi[1],S)[1]];
let e2=Z;for(let k=0;k<=250;k++)e2=add(e2,I(2n**BigInt(k),fac[k]));e2=add(e2,[0n,ce(S*2n**251n*126n,fac[251]*125n)]);
if(e2[0]<=7n*S||pi[0]<=3n*S||pi[1]>=4n*S)throw Error("elementary bounds");
const K=1024n,A=4n*K+1n,L=80,E=56,bc=[one,I(-1n,2n)];for(let k=2;k<=2*E;k++){if(k%2){bc.push(Z);continue}let z=Z;for(let l=0;l<k;l++)z=add(z,rat(bc[l],1n,fac[k+1-l]));bc.push(neg(z))}
let H=Z;for(let n=1n;n<=K;n++)H=add(H,I(1n,n));let eg=sub(sub(H,log(K)),I(1n,2n*K)),term;for(let k=1;k<=E;k++){term=rat(bc[2*k],fac[2*k-1],K**BigInt(2*k));eg=add(eg,term)}eg=add(eg,[-abs(term),abs(term)]);
const g0=neg(add(add(rat(log(2n),3n,1n),eg),add(rat(pi,1n,2n),lpi)));
let em=[null,null];for(let p=2;p<=2*L+3;p++){let v=add(I(A,4n*BigInt(p-1)),I(1n,2n)),rise=1n,ap=1n,fp=1n;for(let k=1;k<=E;k++){let q=2*k-1;if(k===1){rise=BigInt(p);ap=A;fp=4n}else{rise*=BigInt(p+q-2)*BigInt(p+q-1);ap*=A*A;fp*=16n}term=rat(bc[2*k],rise*fp,ap);v=add(v,term)}em[p]=add(v,[-abs(term),abs(term)])}
function isqrt(n){if(n<0n)throw Error("sqrt");if(n<2n)return n;let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));while(true){let y=(x+n/x)/2n;if(y>=x)return x;x=y}}
function trig(x){let period=rat(pi,2n,1n),q=fl(x[0]+pi[0],period[0]),y=sub(x,rat(period,q,1n));if(abs(y)>4n*S)throw Error("trig");let yy=mul(y,y),st=y,ct=one,s=st,c=ct;for(let k=1n;k<110n;k++){st=neg(rat(mul(st,yy),1n,2n*k*(2n*k+1n)));ct=neg(rat(mul(ct,yy),1n,(2n*k-1n)*2n*k));s=add(s,st);c=add(c,ct)}let eps=ce(S*4n**220n,fac[220]);return [add(s,[-eps,eps]),add(c,[-eps,eps])]}
const bank=[[2,2],[3,3],[4,2],[5,5],[7,7],[8,2],[9,3],[11,11],[13,13],[16,2],[17,17],[19,19],[23,23],[25,5],[27,3],[29,29],[31,31],[32,2],[37,37],[41,41],[43,43],[47,47],[49,7],[53,53]];
const pd=Array(J).fill(Z),sn=Array(J).fill(Z);
for(let [n,p] of bank){let l=log(BigInt(n)),sq=isqrt(BigInt(n)*S*S),a=div(log(BigInt(p)),[sq,sq+1n]),[st,ct]=trig(mul(alpha,l)),s=Z,c=one;for(let j=0;j<J;j++){sn[j]=add(sn[j],mul(a,s));let diag=mul(sub(I(4n),l),c);if(j>0)diag=sub(diag,div(s,rat(alpha,BigInt(j),1n)));else diag=rat(diag,2n,1n);pd[j]=add(pd[j],mul(a,diag));[s,c]=[add(mul(s,ct),mul(c,st)),sub(mul(c,ct),mul(s,st))]}}
let ex=div(one,e2),exstep=mul(mul(ex,ex),mul(ex,ex)),weights=[ex];for(let n=1;n<80;n++)weights.push(mul(weights[n-1],exstep));
const remExp=I(2401n,2400n*7n**321n);
const nodes=[];
for(let j=0;j<J;j++){let r=rat(alpha,BigInt(j),1n),z=mul(r,r),t=rat(z,1n,4n),q=rat(t,16n,A*A),g=g0,B=Z,D=Z;
for(let n=0;n<Number(K);n++){let x=I(BigInt(4*n+1),4n),xx=mul(x,x),den=add(xx,t);g=add(g,div(t,mul(x,den)));B=add(B,rat(div(one,den),1n,4n));D=add(D,rat(div(xx,mul(den,den)),1n,4n))}
let power=one,gt=Z,bt=Z,dt=Z;for(let l=0;l<L;l++){let sign=l%2?-1n:1n;bt=add(bt,rat(mul(power,em[2*l+2]),sign,1n));dt=add(dt,rat(mul(power,em[2*l+2]),sign*BigInt(l+1),1n));power=mul(power,q);gt=add(gt,rat(mul(power,em[2*l+3]),sign,1n))}
let berr=mul(power,em[2*L+2]),derr=rat(berr,BigInt(L+1),1n),gerr=mul(mul(power,q),em[2*L+3]);
g=add(g,rat(add(gt,[0n,gerr[1]]),4n,A));B=add(B,rat(add(bt,[0n,berr[1]]),4n,A*A));D=add(D,rat(add(dt,[0n,derr[1]]),4n,A*A));
let be=Z,de=Z;for(let n=1;n<80;n++){let kk=I(BigInt(4*n+1)**2n,4n),den=add(kk,z);be=add(be,div(weights[n],den));de=add(de,div(mul(weights[n],kk),mul(den,den)))}be=add(be,[0n,remExp[1]]);de=add(de,[0n,remExp[1]]);let sig=j%2?-1n:1n;nodes.push({j,z,g,B:sub(B,rat(be,sig,1n)),D:sub(D,rat(de,sig,1n)),sn:rat(sn[j],BigInt(j),1n),p:pd[j]})}
function entry(x,y){let j=x.j,k=y.j,sig=j%2?-1n:1n;if(j%2!==k%2)return Z;let b=j===k?rat(x.D,2n,1n):rat(div(sub(mul(x.z,x.B),mul(y.z,y.B)),sub(x.z,y.z)),2n,1n);let corr=rat(sub(rat(e2,sig,1n),I(2n)),1n,2n);b=add(b,div(corr,mul(add(I(1n,4n),x.z),add(I(1n,4n),y.z))));let p=j===k?x.p:div(rat(sub(y.sn,x.sn),2n,1n),rat(alpha,BigInt(j*j-k*k),1n));return add(sub(b,p),j===k?rat(x.g,j===0?4n:2n,1n):Z)}
function cert(par){let nd=nodes.filter(x=>x.j%2===par),n=nd.length,m=Array.from({length:n},()=>Array(n)),rad=0n;for(let i=0;i<n;i++)for(let j=0;j<=i;j++){let a=entry(nd[i],nd[j]),mid=fl(a[0]+a[1],2n),err=max([mid-a[0],a[1]-mid]);if(err>rad)rad=err;m[i][j]=m[j][i]=mid}let A=m.map(r=>r.slice()),LL=Array.from({length:n},()=>Array(n).fill(0n)),R=Array.from({length:n},()=>Array(n).fill(0n)),piv=[];for(let i=0;i<n;i++){let d=A[i][i];piv.push(String(d));if(d<=0n)return {par,n,certified:false,reason:"midpoint pivot",index:i,pivot:String(d),rad:String(rad)};LL[i][i]=S;for(let j=i+1;j<n;j++)LL[j][i]=fl(A[j][i]*S,d);for(let j=i+1;j<n;j++)for(let k=j;k<n;k++){let z=A[k][j]-fl(LL[k][i]*A[j][i],S);A[k][j]=A[j][k]=z}}
for(let i=0;i<n;i++){R[i][i]=S;for(let j=i-1;j>=0;j--){let t=0n;for(let k=j+1;k<=i;k++)t+=R[i][k]*LL[k][j];R[i][j]=-fl(t,S)}}
let row=R.map(r=>r.reduce((s,x)=>s+(x<0n?-x:x),0n)),RM=R.map((r,i)=>m.map((_,j)=>{let z=0n;for(let k=0;k<=i;k++)z+=r[k]*m[k][j];return z})),dlo=[],off=[];
for(let i=0;i<n;i++){off.push([]);for(let j=0;j<=i;j++){let z=0n;for(let k=0;k<=j;k++)z+=RM[i][k]*R[j][k];let er=rad*row[i]*row[j];if(i===j)dlo[i]=z-er;else off[i][j]=(z<0n?-z:z)+er}}
let minD=min(dlo),bad=0,maxRow=max(row),factor=1n;for(let i=0;i<n;i++)for(let j=0;j<i;j++)if(dlo[i]<=0n||dlo[j]<=0n||BigInt(2*n)**2n*off[i][j]**2n>=dlo[i]*dlo[j])bad++;
// Bound relative defect by 10^-e/(2n), with exact squared comparison.
let e=0;if(bad===0&&minD>0n){for(let k=1;k<=220;k++){let test=10n**BigInt(2*k)*BigInt(2*n)**2n;if(off.some((r,i)=>r.some((v,j)=>j<i&&test*v*v>=dlo[i]*dlo[j])))break;e=k;}}
let expLower=0,den=8n*BigInt(n)*S*maxRow*maxRow;if(minD>0n){while(minD*10n**BigInt(expLower)<=den)expLower++}
return {par,n,certified:bad===0&&minD>0n,bad,rad:String(rad),min_midpoint_pivot_scaled:String(min(piv.map(BigInt))),min_congruence_diagonal_scaled:String(minD),max_R_row_scaled:String(maxRow),relative_defect_exponent:e,physical_L2_margin_lower_exponent:expLower,margin_numerator:String(minD),margin_denominator:String(den),pivots:piv}}
return {scale:String(S),precision:P,cutoff:J,results:[cert(0),cert(1)]}
}
const result=run();if(result.results.some(x=>!x.certified))throw Error("cert");console.log(JSON.stringify(result,null,2));
