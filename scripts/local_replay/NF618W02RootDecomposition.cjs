#!/usr/bin/env node
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const b=fs.readFileSync(path.join(process.argv[2]||".","notes/provisional/NF618W02ResidualSupport.json"));
if(crypto.createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex")!=="90b71e032264cf18d4febac3c11d804fb6a9f4ec")throw Error("input blob");
function decompose(rows){
 const out=[],residues=new Set([0]),octants=new Set([0]);let signed=0;
 for(const row of rows){const [slot,h,F,maxDegree]=row;if(!Number.isSafeInteger(F)||!Number.isSafeInteger(h))throw Error("key");
 for(const sign of [1,-1]){const v=sign*F,t0=Math.floor(v/1280),p=v-1280*t0,j=Math.floor((p+160)/320),r=p-320*j,q=j%4,t=t0+Math.floor(j/4);
 if(v!==1280*t+320*q+r||q<0||q>3||Math.abs(r)>160)throw Error("decomposition");
 residues.add(p);octants.add(Math.abs(r));signed++;
 if(sign===1)out.push([slot,h,F,maxDegree,t,q,r,row[6],row[7]]);
 }}
 if(out.length!==7835||residues.size!==1276||octants.size!==161)throw Error("census");
 return {columns:["slot","2h","1408f","max_degree","turns","quarter_turns","signed_root_power","ledger_group","scheduled_batch"],slots:out.length,signed_checks:signed,phase_residues:residues.size,representatives:octants.size,rows:out};
}
console.log(JSON.stringify(decompose(JSON.parse(b.toString("utf8")).ordinary.rows)));
