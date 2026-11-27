// E19U exact integer directional contraction. Node.js 22+.
// Conditional on the E19Q/E19R Fourier, tail and Parseval attachments.
// Replays the original coarse alias bounds and the tightened common sinc² bounds.
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
function certify(c,j) {
  const Q=16384,M=128,N=665,E=64,S=1048576n,B=1n<<60n,H=1n<<30n,D=10n**12n;
  const ceil=(a,b)=>{if(a<0n||b<=0n)throw Error("ceil domain");return (a+b-1n)/b};
  const floor=(a,b)=>a>=0n?a/b:-ceil(-a,b);
  const abs=a=>a<0n?-a:a, max=(a,b)=>a>b?a:b, min=(a,b)=>a<b?a:b;
  const assert=(x,msg)=>{if(!x)throw Error(msg)};
  const fac=n=>{let v=1n;for(let i=2;i<=n;i++)v*=BigInt(i);return v};
  const frac=s=>{const [a,b="1"]=s.split("/");return [BigInt(a),BigInt(b)]};
  const scale=s=>{let [a,b]=frac(s);assert((a*D)%b===0n,"coefficient scale");return a*D/b};
  const rat=(a,b)=>a+"/"+b, approx=(a,b)=>Number(a)/Number(b);
  const x=c.dedicated_pole_interior.map(scale),g=c.dedicated_pole_exterior.map(scale),p=c.pole_coefficients.map(scale);
  assert(x.length===N&&p.length===N&&g.length===2*E,"shapes");
  const q=[...g.slice(0,E).map(a=>-a),...p,...g.slice(E).map(a=>-a)];
  // Machin: 30 alternating terms, plus one positive term; fixed-scale outward rounding.
  const PS=10n**25n, pn=314159265358979323846n,pd=10n**20n;
  function atanBounds(k){let a=0n;for(let n=0;n<30;n++){const den=BigInt(2*n+1)*k**BigInt(2*n+1);a+=floor((n%2?-PS:PS),den)}return [a,a+30n+ceil(PS,61n*k**61n)]}
  const [al,au]=atanBounds(5n),[bl,bu]=atanBounds(239n);
  assert((16n*al-4n*bu)*pd>pn*PS&&(16n*au-4n*bl)*pd<(pn+1n)*PS,"pi bounds");
  // e bounds inherited from E19P, recheck via partial sum through degree 11.
  const ef=fac(12);let es=0n;for(let i=0;i<=11;i++)es+=ef/fac(i);
  assert(271828n*ef<100000n*es&&100000n*(es+2n)<271829n*ef,"e bounds");
  const HL=1n<<40n;
  assert(18n*HL<200n*3n**25n,"log tail");
  function logsmall(a,b){let z=a-b,d=a+b;assert(z>=0n&&3n*z<=d,"logsmall");let v=0n;for(let i=0;i<12;i++){const k=BigInt(2*i+1);v+=2n*HL*z**k/(k*d**k)}return v}
  const l2=logsmall(2n,1n);
  function logbounds(a,b){let k=0n;while(a>=2n*b){b*=2n;k++}let l=k*l2+logsmall(a,b);return [l,l+13n*(k+1n)]}
  const hnum=11n,hden=3325n;
  function wbin(m,i,bins){const den=2n*BigInt(bins),a=BigInt(2*m*bins-bins+2*i),b=a+2n;
    const l=a<=0n&&b>=0n?0n:min(abs(a),abs(b)),u=max(abs(a),abs(b));
    const d=100000n*den*hnum;
    const lo=logbounds(271828n*den*hnum+100000n*l*hden,d)[0];
    const hi=logbounds(271829n*den*hnum+100000n*u*hden,d)[1];
    return [max(S,S*lo/HL),ceil(S*hi,HL)]}
  const old=[Array(Q).fill(0n),Array(Q).fill(0n),Array(Q).fill(0n)];
  const fresh=[Array(Q).fill(0n),Array(Q).fill(0n),Array(Q).fill(0n)];
  const qu=BigInt(2*Q),central=[],upper=[];
  for(let i=0;i<Q;i++){const a=BigInt(2*i-Q),b=a+2n;const l=a<=0n&&b>=0n?0n:min(abs(a),abs(b));upper.push(max(abs(a),abs(b)));
    // P(t)=1-t²/6+t⁴/120 is decreasing on [0,pi/2]; lower pi and lower |u| give upper P.
    const z=pn*l,d=pd*qu,z2=z*z,d2=d*d;const num=120n*d2*d2-20n*z2*d2+z2*z2,den=120n*d2*d2;
    assert(num>0n&&num<=den,"central range");central.push(ceil(S*num*num,den*den))}
  function add(A,i,s,L,U){A[0][i]+=ceil(s*U,S);A[1][i]+=ceil(s*S,L);A[2][i]+=s}
  for(let m=0;m<=M;m++){const bins=m===0?2048:16,ws=Array.from({length:bins},(_,i)=>wbin(m,i,bins));
    for(let i=0;i<Q;i++){const [L,U]=ws[Math.floor(i*bins/Q)];const a=BigInt(2*m*Q+2*i-Q),b=a+2n;let so=S,sn=central[i];
      if(m){let den=min(abs(a),abs(b));assert(den>0n,"alias");so=ceil(S*upper[i]**2n,den**2n);sn=ceil(central[i]*upper[i]**2n,den**2n)}
      add(old,i,so,L,U);add(fresh,i,sn,L,U);if(m){add(old,Q-1-i,so,L,U);add(fresh,Q-1-i,sn,L,U)}}}
  for(const A of [old,fresh])for(let k=0;k<3;k++)for(let i=0;i<Q;i++){assert(A[k][i]===A[k][Q-1-i],"symmetry");assert(A[k][i]<(k===0?20n:4n)*S,"weight range")}
  // High fixed point Taylor evaluation: each floored term loses <1/(1024 B).
  const BB=B*1024n;
  function trig(a,b,kind){let s=0n;for(let i=0;i<=5;i++){const n=kind==="cos"?2*i:2*i+1;
      const pow=kind==="sinc"?2*i:n;
      s+=floor((i%2?-BB:BB)*a**BigInt(pow),b**BigInt(pow)*fac(n))}
    return floor(s,1024n)}
  const root=[trig(pn,pd*BigInt(Q),"cos"),-trig(pn,pd*BigInt(Q),"sin")];
  const mul=(a,b)=>[floor(a[0]*b[0]-a[1]*b[1],B),floor(a[0]*b[1]+a[1]*b[0],B)];
  const roots=[[B,0n]];for(let i=1;i<=Q;i++)roots.push(mul(roots[i-1],root));
  // Root error <4/B; accumulated twiddle error <12Q/B. FFT bound in B-scaled units.
  const R=12n*BigInt(Q);assert(8n*BigInt(Q)<B,"root bound");
  let err=1n;for(let i=1;i<Q;i*=2)err=ceil((2n*B+R)*err,B)+20n*R+2n;
  err=ceil((B+R)*err,B)+20n*R+2n;
  // sinc Taylor remainder t^12/13! for t<= (pi*792/Q); pi input error negligible.
  const a=(pn+1n)*BigInt(N+2*E-1),b=pd*BigInt(Q);
  assert(B*a**12n<b**12n*fac(13),"sinc remainder");
  const errH=ceil((err+100n)*H,B)+2n;assert(errH<=128n,"gram error");
  const sinc=Array.from({length:N+2*E},(_,i)=>trig(pn*BigInt(i),pd*BigInt(Q),"sinc"));
  function gram(weights){const a=weights.map(w=>[w*B/(S*BigInt(Q)),0n]);let j=0;
    for(let i=1;i<Q;i++){let bit=Q>>1;while(j&bit){j^=bit;bit>>=1}j^=bit;if(i<j)[a[i],a[j]]=[a[j],a[i]]}
    for(let m=2;m<=Q;m*=2){const half=m>>1,step=2*Q/m;for(let i=0;i<Q;i+=m)for(let j=0;j<half;j++){const x=a[i+j],y=mul(a[i+j+half],roots[j*step]);a[i+j]=[x[0]+y[0],x[1]+y[1]];a[i+j+half]=[x[0]-y[0],x[1]-y[1]]}}
    return sinc.map((s,n)=>floor((n%2?-1n:1n)*mul(a[n],roots[n])[0]*s*H,B*B))}
  function bilinear(a,b,w,offset){let v=0n;for(let i=0;i<a.length;i++)for(let k=0;k<b.length;k++)v+=a[i]*b[k]*w[Math.abs(i-k+offset)];return v}
  const l1=a=>a.reduce((s,v)=>s+abs(v),0n);const l=l1(x)+l1(q);
  function run(A){const [wa,wv,wc]=A.map(gram);
    const contraction=bilinear(x,x,wa,0)+bilinear(q,q,wv,0)-2n*bilinear(x,q,wc,E);
    const er=errH*l*l,num=hnum*(contraction+er),den=hden*H*D*D;assert(num>=0n,"finite nonnegative");
    const [tn,td]=frac(c.dedicated_tail_upper),[pn0,pd0]=frac(c.physical_approximation_norm);
    const sumN=num*td+tn*den,sumD=den*td;
    function isqrt(v){if(v===0n)return 0n;let x=1n<<BigInt(Math.ceil(v.toString(2).length/2));while(true){let y=(x+v/x)/2n;if(y>=x)return x;x=y}}
    const K=10n**12n,v=ceil(sumN*K*K,sumD),s=isqrt(v);const sq=s+(s*s<v?1n:0n);
    const poleN=sq*pd0+pn0*K,poleD=K*pd0;
    const [jn,jd]=frac(j.total_upper),[kn,kd]=frac(c.packed_zero_squared);
    const combinedN=poleN*poleN*jd*kd+jn*poleD*poleD*kd+kn*poleD*poleD*jd,combinedD=poleD*poleD*jd*kd;
    return {finite_upper:rat(num,den),finite_display:approx(num,den),gram_reserve:rat(hnum*er,den),pole_norm_upper:rat(poleN,poleD),pole_display:approx(poleN,poleD),combined_squared_upper:rat(combinedN,combinedD),combined_display:Math.sqrt(approx(combinedN,combinedD))}}
  return {status:"conditional arithmetic; same frozen E19R coefficients; no native or analytic attachment",Q,M,N,E,gram_error_units:Number(errH),central_edge_upper:String(central[0]),old:run(old),sharpened:run(fresh),inherited_finite:c.dedicated_finite_upper,inherited_pole:c.dedicated_pole_norm_upper};
}
const dir=path.dirname(fileURLToPath(import.meta.url));
function read(f,sha){const b=fs.readFileSync(path.join(dir,'..',f));if(crypto.createHash('sha256').update(b).digest('hex')!==sha)throw Error('input hash mismatch');return JSON.parse(b);}
const c=read('iv106_e19r/remaining_certificate.json','59fe6feb3dc0e39d7c21c719bea36f0d124a7b9c2941da391077a62fd5f46a72');
const j=read('iv106_e19q/joint_certificate.json','d61da378760ca11e21c7e828b46a717d810116d35dfc03d5ec325f1f6ddbb8c9');
console.log(JSON.stringify(certify(c,j),null,2));
