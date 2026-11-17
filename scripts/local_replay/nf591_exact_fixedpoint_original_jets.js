/* NF591: exact BigInt fixed-point balls, no floating point or Arb.
 * Every multiplication rounds its center down and widens its radius.
 * Machin arctan alternating remainder; complex exp small-disc factorial tail.
 * The Lean checker/analytic remainder proofs are separate obligations. */
function replay(j,table) {
  const Q=10n**250n, N=400, T=220, A=200;
  const abs=x=>x<0n?-x:x;
  const floor=(a,b)=>{if(b<=0n)throw Error("denominator");const r=a/b;return a<0n&&a%b!==0n?r-1n:r};
  const ceil=(a,b)=>-floor(-a,b);
  const check=(h,m)=>{if(!h)throw Error(m)};
  const exact=(n,d=1n)=>[floor(n*Q,d),n*Q%d===0n?0n:1n];
  const add=(a,b)=>[a[0]+b[0],a[1]+b[1]];
  const neg=a=>[-a[0],a[1]];
  const mul=(a,b)=>[floor(a[0]*b[0],Q),ceil(abs(a[0])*b[1]+abs(b[0])*a[1]+a[1]*b[1],Q)+1n];
  const div=(a,d)=>[floor(a[0],d),ceil(a[1],d)+1n];
  const enlarge=(a,r)=>[a[0],a[1]+r];
  const mag=a=>abs(a[0])+a[1];
  const zero=[0n,0n],one=[Q,0n],C0=[zero,zero],C1=[one,zero];
  const ca=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
  const cn=a=>[neg(a[0]),neg(a[1])];
  const cm=(a,b)=>[add(mul(a[0],b[0]),neg(mul(a[1],b[1]))),add(mul(a[0],b[1]),mul(a[1],b[0]))];
  const cd=(a,n)=>[div(a[0],n),div(a[1],n)];
  const cr=(a,b)=>[mul(a[0],b),mul(a[1],b)];
  const expSmall=z=>{
    check(mag(z[0])+mag(z[1])<=Q,"exp norm <=1 enclosure");
    let s=C1,e=C1,f=1n;
    for(let n=1;n<T;n++){e=cd(cm(e,z),BigInt(n));s=ca(s,e);f*=BigInt(n)}
    f*=BigInt(T);check(2n*Q<=f,"exp tail");
    return [enlarge(s[0],1n),enlarge(s[1],1n)];
  };
  const atanInv=p=>{
    let s=zero;
    for(let n=0;n<A;n++){let d=BigInt(2*n+1)*p**BigInt(2*n+1);s=add(s,exact(n%2===0?1n:-1n,d))}
    check(Q<=p**BigInt(2*A+1)*BigInt(2*A+1),"atan tail");
    return enlarge(s,1n);
  };
  const pi=add(mul(exact(16n),atanInv(5n)),neg(mul(exact(4n),atanInv(239n))));
  check(pi[0]-pi[1]>3n*Q&&pi[0]+pi[1]<4n*Q,"pi range");
  const rat=s=>{let [n,d]=String(s).split("/").map(BigInt);return [n,d??1n]};
  const rf=s=>exact(...rat(s));
  const dy=p=>{let n=BigInt(p[0]),e=BigInt(p[1]);return e>=0n?exact(n<<e):exact(n,1n<<(-e))};
  const box=row=>{let a=dy(row[0]),r=dy(row[1]);return enlarge(a,mag(r))};
  const jets=z=>{let e=[C1];for(let n=1;n<N;n++)e.push(cd(cm(e[n-1],z),BigInt(n)));return e};
  const ch=(k,m)=>{let c=1n;for(let i=1;i<=m;i++)c=c*BigInt(k-i+1)/BigInt(i);return c};
  const cache=new Map();
  function oscillator(f,k){
    const key=f+":"+k;if(cache.has(key))return cache.get(key);
    let [p,q]=rat(f);
    // Exact reduction of f*B to [-1/2,1/2) turns.
    let u=p*11n,v=q*10n,j=floor(2n*u+v,2n*v),r=u-j*v;
    check(2n*abs(r)<=v,"phase reduce");
    let z=[zero,mul(pi,exact(r,2n*v))];
    let phase=expSmall(z);phase=cm(phase,phase);phase=cm(phase,phase);
    if(k%2===0)phase=[phase[1],neg(phase[0])];
    const lambda=[zero,neg(mul(pi,exact(2n*p,500n*q)))];
    const e=jets(lambda);
    const poly=Array.from({length:k+1},(_,m)=>exact(ch(k,m)*11n**BigInt(k-m)*(m%2===0?1n:-1n),10n**BigInt(k-m)*500n**BigInt(m)));
    let out=[];
    for(let n=0;n<N;n++){
      let s=C0;
      for(let m=0;m<=Math.min(k,n);m++)s=ca(s,cr(e[n-m],poly[m]));
      out.push(cm(phase,s)[0]);
    }
    cache.set(key,out);return out;
  }
  const ep=expSmall([exact(11n,20n),zero]),en=expSmall([exact(-11n,20n),zero]);
  const jp=jets([exact(-1n,1000n),zero]),jn=jets([exact(1n,1000n),zero]);
  const pole=Array.from({length:N},(_,n)=>div(add(cm(ep,jp[n])[0],neg(cm(en,jn[n])[0])),2n));
  const out=Array.from({length:N},()=>zero);
  let count=0;function accumulate(c,v){count++;for(let n=0;n<N;n++)out[n]=add(out[n],mul(c,v[n]))}
  j.original_selected_generator_node_orders.forEach(([f,k],i)=>accumulate(box(j.original_exact_native_raw_selected_coefficients_mid_radius[i]),f==="pole"?pole:oscillator(f,k)));
  j.original_source_critical_sines_and_pole_coefficients.forEach((s,i)=>{
    let c=box(j.original_exact_native_original_four_critical_coefficients_mid_radius[i]);
    s.sine_coefficients.forEach((v,k)=>accumulate(mul(c,rf(v)),oscillator(j.original_source_critical_sine_frequencies[k],0)));
    accumulate(mul(c,rf(s.sinh_coefficient)),pole)
  });
  check(count===374&&cache.size===273,"mode counts");
  const prefix=table.split("def neutralNF588U400CeilPrefix")[1].split(":=")[1].split("]")[0].match(/\d+/g).map(BigInt);
  const ceilings=[...prefix,...Array(N-prefix.length).fill(1n)];
  const computed=out.map(a=>ceil(mag(a),Q/10n**40n));
  const misses=computed.map((a,i)=>a>ceilings[i]?i:-1).filter(i=>i>=0);
  check(misses.length===0,"ceiling mismatch: "+misses);
  check(out[0][0]+out[0][1]<-Q/10n**11n,"endpoint negative");
  return {pass:"NF591-exact-fixedpoint-full-box",scale_digits:250,atan_terms:A,exp_terms:T,primitive_summands:count,modes:cache.size,all_400_ceilings_dominate:true,all_400_ceilings_equal:computed.every((a,i)=>a===ceilings[i]),max_radius_scaled:out.reduce((a,b)=>a>b[1]?a:b[1],0n).toString(),endpoint_upper_scaled:(out[0][0]+out[0][1]).toString(),intervals:out.map(([m,r])=>[(m-r).toString(),(m+r).toString()]),ceilings:computed.map(String)};
}
const fs=require("node:fs"),crypto=require("node:crypto"),path=require("node:path");
const root=path.resolve(__dirname,"../..");
const raw=fs.readFileSync(path.join(root,"notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json"));
if(crypto.createHash("sha256").update(raw).digest("hex")!=="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce")throw Error("source hash");
const tab=fs.readFileSync(path.join(root,"WeilDefect/Arithmetic/ActualZetaOriginalU400NormalizedBudget.lean"),"utf8");
const r=replay(JSON.parse(raw),tab);
fs.writeFileSync(process.argv[2]||"nf591-fixedpoint.json",JSON.stringify(r,null,2)+"\n");
console.log(r.pass, r.primitive_summands,r.modes,r.all_400_ceilings_equal);
