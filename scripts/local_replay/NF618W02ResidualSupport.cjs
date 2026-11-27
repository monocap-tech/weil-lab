#!/usr/bin/env node
// W02-NF-05: exact coefficient support, not moment or integral evaluation.
// Usage: node scripts/local_replay/NF618W02ResidualSupport.cjs <repository root>
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const inputs=["WeilDefect/Arithmetic/ActualZetaOriginalNF407FrozenData.lean","WeilDefect/Arithmetic/ActualZetaOriginalNF407DyadicChunk0.lean","WeilDefect/Arithmetic/ActualZetaOriginalNF407DyadicChunk1.lean","WeilDefect/Arithmetic/ActualZetaOriginalNF407DyadicChunk2.lean","WeilDefect/Arithmetic/ActualZetaOriginalNF407DyadicChunk3.lean","WeilDefect/Arithmetic/ActualZetaOriginalCriticalSolveCustody.lean","WeilDefect/Arithmetic/ActualZetaOriginalJ242ExponentialSignature.lean","notes/provisional/NF618W02SourceDemand.json"];
const blobs=["86ca70c8a2a8ba24ce4204081fef74d4ac543646","c5241e94c17936a593d4d5f2a2e3f42ee54916c8","e47a5c2cf7b262ef1bc7ccac71912fa9b5a26e40","bf4d0f2dcdafcc073a904848115858caf123dcf4","386b5b81d372c31b566aa91e574d26c0d2961c33","9994253e400a84d78728ea3f12eb1ac9ca9b900c","b56b2dc6c482ca79e8f023d556bd52edf5e24f48","1edda66274a2090af027011b1c264156a63c11aa"];
const root=process.argv[2]||".";
const read=(p,i)=>{const b=fs.readFileSync(path.join(root,p));const id=crypto.createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex");if(id!==blobs[i])throw Error("pinned input mismatch "+p);return b.toString("utf8")};
function analyze(inputs){
 const [data,...rest]=inputs;const chunks=rest.slice(0,4),crit=rest[4],sig=rest[5],map=JSON.parse(rest[6]);
 const need=(x,m)=>{if(!x)throw Error(m)};
 const dyads=s=>[...s.matchAll(/\(\((-?\d+),\s*(-?\d+)\),\s*\((-?\d+),\s*(-?\d+)\)\)/g)].map(m=>[BigInt(m[1]),+m[2],BigInt(m[3]),+m[4]]);
 const sel=chunks.flatMap(dyads),cb=dyads(data.split("def neutralNF587CriticalDyads")[1].split("def neutralNF587FrozenNodes")[0]);
 need(sel.length===242&&cb.length===4&&cb.every(r=>r[2]===0n),"dyads");
 const E=Math.max(20,...sel.map(r=>-r[1]),...cb.map(r=>-r[1]));const S=1n<<BigInt(E),Q=1000000000000n;
 const dy=(m,e)=>{need(E+e>=0,"dyadic scale");return m*(1n<<BigInt(E+e))};
 const mids=sel.map(r=>dy(r[0],r[1]));const T=[...crit.split("def neutralNF604OriginalT4Numerators")[1].split("]")[0].matchAll(/-?\d+/g)].map(m=>BigInt(m[0]));need(T.length===4,"T");
 const Y=[...crit.split("def neutralNF604OriginalY0")[1].split("def neutralNF604OriginalT4Numerators")[0].matchAll(/\((-?\d+),\s*(-?\d+)\)/g)].map(m=>[BigInt(m[1]),+m[2]]);
 need(Y.length===16,"Y");
 for(let j=0;j<4;j++){let v=0n;for(let k=0;k<4;k++)v-=dy(Y[4*j+k][0],Y[4*j+k][1]-20)*T[k];need(v===dy(cb[j][0],cb[j][1]),"critical coefficient identity "+j)}
 const w=cb.map((r,j)=>dy(T[j],-20)-dy(r[0],r[1]));
 const parseq=s=>[...s.matchAll(/\((-?\d+(?:\/\d+)?)\)/g)].map(m=>m[1]);
 const freq=s=>{let [a,b="1"]=s.split("/").map(Number);need(Number.isSafeInteger(a*1408/b),"freq");return a*1408/b};
 const rat=s=>{let [a,b="1"]=s.split("/").map(BigInt);need(Q%b===0n,"coefficient denominator");return a*(Q/b)};
 const groups=[...sig.matchAll(/\(\((\d+(?:\/\d+)?)\s*:\s*ℚ\),\s*(\d+)\)/g)].map(m=>[freq(m[1]),+m[2]]);
 const cf=parseq(data.split("def neutralNF587CriticalFrequencies")[1].split("]")[0]).map(freq);
 const cs=[...data.split("def neutralNF587CriticalSines")[1].split("def neutralNF587CriticalPoles")[0].matchAll(/#\[([^\[\]]+)\]/g)].map(m=>parseq(m[1]).map(rat));
 const cp=parseq(data.split("def neutralNF587CriticalPoles")[1].split("]")[0]).map(rat);
 need(groups.length===67&&cf.length===32&&cs.length===4&&cs.every(r=>r.length===32)&&cp.length===4,"source shapes");
 const nodes=groups.flatMap(([f,m])=>Array.from({length:m},(_,n)=>[f,n]));need(nodes.length===241,"nodes");
 const frozen=[...data.split("def neutralNF587FrozenNodes")[1].split("def neutralNF587CriticalFrequencies")[0].matchAll(/\(\((\d+(?:\/\d+)?)\),\s*(\d+)\)/g)].map(m=>[freq(m[1]),+m[2]]);need(JSON.stringify(frozen)===JSON.stringify(nodes),"frozen node identity");
 // exp(h*x+2*pi*i*f*x)*x^n, coefficients scaled by 2 (test) and 2*S*Q (residual).
 const osc=(f,n,c)=>n%2?[[0,f,n,c,0n],[0,-f,n,c,0n]]:[[0,f,n,0n,-c],[0,-f,n,0n,c]];
 const pole=c=>[[1,0,0,c,0n],[-1,0,0,-c,0n]];
 const tests=nodes.map(([f,n])=>osc(f,n,1n)).concat([pole(1n)]);
 const C=cf.map((f,k)=>w.reduce((a,x,j)=>a+x*cs[j][k],0n));
 const P=w.reduce((a,x,j)=>a+x*cp[j],0n)-mids[241]*Q;
 const source=nodes.flatMap(([f,n],i)=>osc(f,n,-mids[i]*Q)).concat(cf.flatMap((f,k)=>osc(f,0,C[k])),pole(P));
 function accumulate(fold){
  const union=new Map(),rowstats=[];let pairs=0,terms=0,raw=0,zeroRows=0;
  for(let i=0;i<242;i++){
   const acc=new Map();
   for(const a of tests[i])for(const b of source){pairs++;let h=a[0]+b[0],f=a[1]+b[1],n=a[2]+b[2],re=a[3]*b[3]-a[4]*b[4],im=a[3]*b[4]+a[4]*b[3];
    if(f<0||(f===0&&h<0)){h=-h;f=-f;if(n%2){re=-re;im=-im}}
    if(fold&&h<0){h=-h;if(n%2)re=-re;else im=-im}
    if(f===0)im=0n;
    if(h===0){if(n%2)re=0n;else im=0n}
    const k=h+","+f+","+n;const p=acc.get(k)||[0n,0n];p[0]+=re;p[1]+=im;acc.set(k,p);
   }
   raw+=acc.size;let ct=0;for(const [k,[re,im]] of acc){if(re===0n&&im===0n)continue;const [h,f,n]=k.split(",").map(Number);if(h===0&&f===0){need(n%2===0,"zero parity");zeroRows++;continue}
    ct++;terms++;const key=h+","+f;let o=union.get(key);if(!o){o={h,f,max:-1,degrees:new Set(),first:i};union.set(key,o)}o.max=Math.max(o.max,n);o.degrees.add(n);
   }rowstats.push(ct)
  }
  const idx=new Map(map.rows.map(r=>[r[1]+","+r[2],r]));
  const rows=[...union.values()].sort((a,b)=>a.h-b.h||a.f-b.f).map(x=>{let r=idx.get(x.h+","+x.f);need(r&&x.max<=Math.max(r[3],r[4]),"map match");return [r[0],x.h,x.f,x.max,[...x.degrees].sort((a,b)=>a-b),x.first,r[9],r[10]]});
  return {pairs,raw,terms,zeroRows,rowstats,summary:{tables:rows.length,prefixRows:rows.reduce((a,r)=>a+r[3]+1,0),distinctDegrees:rows.reduce((a,r)=>a+r[4].length,0),residualTables:rows.filter(r=>!r[6]).length,residualPrefix:rows.filter(r=>!r[6]).reduce((a,r)=>a+r[3]+1,0)},rows};
 }
 const ordinary=accumulate(false),folded=accumulate(true);
 const fi=new Map(folded.rows.map(r=>[r[1]+","+r[2],r]));
 const omitted=ordinary.rows.filter(r=>!fi.has(r[1]+","+r[2])).map(r=>{const p=fi.get(-r[1]+","+r[2]);need(r[1]<0&&p&&r[4].every(n=>p[4].includes(n)),"fold representative");return {omitted:r[0],representative:p[0],degrees:r[4],omittedGroup:r[6],representativeGroup:p[6]}});
 need(ordinary.rows.length===map.rows.length&&ordinary.rows.every((r,i)=>r[0]===i&&r[3]===Math.max(map.rows[i][3],map.rows[i][4])),"original full demand");
 return {E,criticalIdentity:4,selectedNonzero:mids.filter(x=>x!==0n).length,criticalCombinedNonzero:C.filter(x=>x!==0n).length,combinedPoleNonzero:P!==0n,selectedRadiusBitExponentRange:[Math.min(...sel.map(r=>r[3]+(r[2]<0n?-r[2]:r[2]).toString(2).length-1)),Math.max(...sel.map(r=>r[3]+(r[2]<0n?-r[2]:r[2]).toString(2).length-1))],columns:["slot","2h","1408f","max_degree","actual_degrees","first_residual_row","ledger_group","scheduled_batch"],ordinary,folded,omitted};
}
console.log(JSON.stringify(analyze(inputs.map(read))));
