// IV243: rational constant-mode signs, and non-certifying trigonometric formula smoke test.
// Run: node research/iv243_am_structured_receiver.mjs
function audit(){
const S=10n**15n, fl=(n,d)=>n/d, ce=(n,d)=>(n+d-1n)/d;
function logI(n,d=1n){let k=0n;while(n>=2n*d){d*=2n;k++}if(n<d)throw Error("log arg");function core(n,d){let u=n-d,v=n+d,L=0n,U=0n;for(let j=0;j<24;j++){let z=BigInt(2*j+1),a=2n*S*u**z,b=z*v**z;L+=fl(a,b);U+=ce(a,b)}let z=49n;U+=ce(2n*S*u**z*v*v,z*v**z*(v*v-u*u));return [L,U]}let l2=core(2n,1n),l=core(n,d);return [l[0]+k*l2[0],l[1]+k*l2[1]]}
function atanI(d){let L=0n,U=0n;for(let j=0;j<24;j++){let z=BigInt(2*j+1),a=fl(S,z*d**z),b=ce(S,z*d**z);if(j%2===0){L+=a;U+=b}else{L-=b;U-=a}}U+=ce(S,49n*d**49n);return [L,U]}
let a=atanI(5n),b=atanI(239n),pi=[16n*a[0]-4n*b[1],16n*a[1]-4n*b[0]],lp=[logI(pi[0],S)[0],logI(pi[1],S)[1]],l2=logI(2n);
let H=[0n,0n];for(let n=1n;n<=10000n;n++){H[0]+=fl(S,n);H[1]+=ce(S,n)}let eg=[H[0]-logI(10001n)[1],H[1]-logI(10000n)[0]];
let g=[-3n*l2[1]-eg[1]-ce(pi[1],2n)-lp[1],-3n*l2[0]-eg[0]-fl(pi[0],2n)-lp[0]];
let e2=[0n,0n],fact=1n;for(let j=0n;j<=32n;j++){if(j)fact*=j; e2[0]+=fl(S*2n**j,fact);e2[1]+=ce(S*2n**j,fact)}e2[1]+=ce(S*2n**33n*17n,fact*33n*16n);if(e2[0]*e2[0]<=54n*S*S||e2[1]*e2[1]>=55n*S*S||e2[0]<=7n*S)throw Error("census");
function isqrt(n){let l=0n,h=n+1n;while(h-l>1n){let m=(h+l)/2n;if(m*m<=n)l=m;else h=m}return l}
const primes=[];for(let p=2;p<=54;p++)if(!Array.from({length:p-2},(_,i)=>i+2).some(i=>p%i===0))primes.push(p);
let P=[0n,0n],count=0;const bank=[];for(let p of primes)for(let n=p;n<=54;n*=p){count++;bank.push(n);let l=logI(BigInt(p)),s=logI(BigInt(n)),r=isqrt(BigInt(n)*S*S);P[0]+=fl(l[0]*(4n*S-s[1]),2n*(r+1n));P[1]+=ce(l[1]*(4n*S-s[0]),2n*r)}
if(count!==24||bank.sort((a,b)=>a-b).join(",")!=="2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53")throw Error("count");
let first=[g[0]-P[1]+2n*e2[0]-2n*S,g[1]-P[0]+2n*e2[1]-2n*S],rows=[];
let low=first[0],high=first[1];for(let n=1n;n<32n;n++){let d=(4n*n+1n)**2n;low+=fl(S*2n*9999n,d*10000n);high+=ce(S*2n,d);if([2n,4n,8n,16n,32n].includes(n+1n))rows.push({terms:Number(n+1n),lower:String(low),upper:String(high)})}
let full=[low,high+ce(S,2n*125n)];
if(first[1]>=-S/10n||BigInt(rows.find(r=>r.terms===4).upper)>=0n||BigInt(rows.find(r=>r.terms===8).lower)<=0n||full[0]<=0n)throw Error("sign");
const N=32768n;
if(4n*4n**4n*10n**10n>=3n**5n*(N-1n)**3n)throw Error("pole tail");
return {scale:String(S),prime_count:count,pi:pi.map(String),euler:eg.map(String),gamma0:g.map(String),e2:e2.map(String),prime:P.map(String),one_boundary:first.map(String),truncations:rows,full:full.map(String),high_mode_negative_pole_norm_upper:"1/10000000000"};
}
function smoke(bank){
let worst=0,checks=0;const alpha=Math.PI/4,c=j=>j===0?.5:Math.SQRT1_2;
function direct(j,k,s){let L=4-s;function integ(q,p){return q===0?L*Math.cos(p):(Math.sin(q*L+p)-Math.sin(p))/q}return c(j)*c(k)*.5*(integ((j-k)*alpha,-k*alpha*s)+integ((j+k)*alpha,k*alpha*s)+integ((k-j)*alpha,-j*alpha*s)+integ((j+k)*alpha,j*alpha*s))}
function formula(j,k,s){if((j+k)%2)return 0;if(j===k)return j===0?(4-s)/2:((4-s)*Math.cos(j*alpha*s)-Math.sin(j*alpha*s)/(j*alpha))/2;return 2*c(j)*c(k)*(k*Math.sin(k*alpha*s)-j*Math.sin(j*alpha*s))/(alpha*(j*j-k*k))}
for(const n of bank)for(let j=0;j<32;j++)for(let k=0;k<32;k++){let s=Math.log(n);worst=Math.max(worst,Math.abs(direct(j,k,s)-formula(j,k,s)));checks++}
if(worst>1e-12)throw Error("formula smoke");return {checks,worst,classification:"floating smoke only"};
}
console.log(JSON.stringify({exact:audit(),smoke:smoke([2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,53])},null,2));
