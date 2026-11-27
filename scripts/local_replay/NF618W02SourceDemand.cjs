#!/usr/bin/env node
// W02-NF-02 source-demand replay. No numeric moment evaluation or Lean execution.
// Usage: node scripts/local_replay/NF618W02SourceDemand.cjs <repo-root> > demand.json
const fs=require("node:fs"), path=require("node:path"), crypto=require("node:crypto");
const inputs=["WeilDefect/Arithmetic/ActualZetaOriginalJ242ExponentialSignature.lean","WeilDefect/Arithmetic/ActualZetaOriginalNF407FrozenData.lean","notes/provisional/NF618CertifiedSlotLedgerBatch24R1.json"];
const blobs=["b56b2dc6c482ca79e8f023d556bd52edf5e24f48","86ca70c8a2a8ba24ce4204081fef74d4ac543646","5931d3ef251562f71c8871a9ad20707781071428"];
const root=process.argv[2]||".";
const read=(p,i)=>{const b=fs.readFileSync(path.join(root,p));const id=crypto.createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex");if(id!==blobs[i])throw Error("pinned input mismatch: "+p);return b.toString("utf8")};
function audit(sig,data,ledger){
 const need=(b,m)=>{if(!b)throw Error(m)};
 const F=x=>{const [a,b="1"]=x.split("/").map(Number);return a*1408/b};
 const G=[...sig.matchAll(/\(\((\d+(?:\/\d+)?)\s*:\s*ℚ\),\s*(\d+)\)/g)].map(m=>[F(m[1]),Number(m[2])]);
 const C=[...data.split("def neutralNF587CriticalFrequencies")[1].split("]")[0].matchAll(/\((\d+(?:\/\d+)?)\)/g)].map(m=>F(m[1]));
 need(G.length===67&&G.reduce((a,g)=>a+g[1],0)===241&&C.length===32,"source census");
 need([...G.map(x=>x[0]),...C].every(Number.isSafeInteger),"exact rational units");
 const S=G.flatMap(([f,m])=>Array.from({length:m},(_,n)=>[[0,f,n],[0,-f,n]]));S.push([[1,0,0],[-1,0,0]]);
 const T=C.map(f=>[[0,f,0],[0,-f,0]]);T.push([[1,0,0],[-1,0,0]]);
 const map=new Map();let zeroH=0,zeroV=0,nh=0,nv=0;
 function add(a,b,kind,owner){let h=a[0]+b[0],f=a[1]+b[1],n=a[2]+b[2];if(f<0||(f===0&&h<0)){h=-h;f=-f}if(h===0&&f===0){if(kind==="H")zeroH++;else zeroV+=4;return}const k=h+","+f;let r=map.get(k);if(!r){r={h,f,H:-1,V:-1,Hrequests:0,Vrequests:0,Hfirst:null,Vfirst:null};map.set(k,r)}r[kind]=Math.max(r[kind],n);r[kind+"requests"]+=kind==="V"?4:1;if(!r[kind+"first"])r[kind+"first"]=owner}
 for(let i=0;i<S.length;i++)for(let j=0;j<S.length;j++)for(let s=0;s<2;s++)for(let t=0;t<2;t++){nh++;add(S[i][s],S[j][t],"H",[i,j,s,t])}
 for(let i=0;i<S.length;i++)for(let k=0;k<T.length;k++)for(let s=0;s<2;s++)for(let t=0;t<2;t++){nv+=4;add(S[i][s],T[k][t],"V",[i,0,k,s,t])}
 const rows=[...map.values()].sort((a,b)=>a.h-b.h||a.f-b.f).map((r,i)=>({...r,i,rows:Math.max(r.H,r.V)+1,group:ledger.slots[i]?.certified_group,batch:ledger.slots[i]?.scheduled_batch}));
 need(rows.length===7835&&ledger.slots.length===rows.length,"slot count");need(rows.every((r,i)=>ledger.slots[i].index===i&&ledger.slots[i].rows===r.rows),"row shapes");
 const summary={};for(const r of rows){const k=(r.H>=0?(r.V>=0?"H_and_V":"H_only"):"V_only");const z=summary[k]??={tables:0,rows:0,certified_tables:0,certified_rows:0,residual_tables:0,residual_rows:0,H_prefix_rows:0,V_prefix_rows:0,residual_H_prefix_rows:0,residual_V_prefix_rows:0};z.tables++;z.rows+=r.rows;z.H_prefix_rows+=r.H+1;z.V_prefix_rows+=r.V+1;if(r.group){z.certified_tables++;z.certified_rows+=r.rows}else{z.residual_tables++;z.residual_rows+=r.rows;z.residual_H_prefix_rows+=r.H+1;z.residual_V_prefix_rows+=r.V+1}}
 need(nh===242*242*4&&nv===242*4*33*4,"request census");need(rows.reduce((a,r)=>a+r.rows,0)===37994,"moment rows");
 return {summary,requests:{H:nh,V:nv,zeroH,zeroV,nonzeroH:nh-zeroH,nonzeroV:nv-zeroV},columns:["slot","2h","1408f","H_max_degree","V_max_degree","H_requests","V_requests","H_first","V_first","ledger_group","scheduled_batch"],rows:rows.map(r=>[r.i,r.h,r.f,r.H,r.V,r.Hrequests,r.Vrequests,r.Hfirst,r.Vfirst,r.group,r.batch])}
}
const [s,c,l]=inputs.map(read);
console.log(JSON.stringify(audit(s,c,JSON.parse(l))));
