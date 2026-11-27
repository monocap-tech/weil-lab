#!/usr/bin/env node
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const root=process.argv[2]||".";
function read(p,sha){const b=fs.readFileSync(path.join(root,p));if(crypto.createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex")!==sha)throw Error("blob mismatch "+p);return JSON.parse(b);}
const a=read("notes/provisional/NF618W02ResidualSupport.json","90b71e032264cf18d4febac3c11d804fb6a9f4ec");
const b=read("notes/provisional/NF618W02RootAttachment/FrequencyDecomposition.json","1558a62fe99f3a10e34eb75106cab6028b3997ad");
const keys=a.ordinary.rows;let errs=[],res=new Set([0]),abs=new Set([0]),signed=0,quarters=[0,0,0,0],tie=0,zero=0;
for(let i=0;i<keys.length;i++){let k=keys[i],row=b.rows[i];if(!row||row[0]!==k[0]||row[1]!==k[1]||row[2]!==k[2]||row[3]!==k[3]||row[7]!==k[6]||row[8]!==k[7])errs.push([i,"binding"]);
if(!Number.isSafeInteger(k[2]))throw Error("noninteger frequency");
for(let sign of [1,-1]){let F=BigInt(sign*k[2]),p=((F%1280n)+1280n)%1280n;let j=(p+160n)/320n,r=p-j*320n,q=j%4n,t=(F-p)/1280n+j/4n;if(F!==1280n*t+320n*q+r||r< -160n||r>160n||q<0n||q>3n)errs.push([i,sign]);if(sign===1&&(row[4]!==Number(t)||row[5]!==Number(q)||row[6]!==Number(r)))errs.push([i,"stored"]);res.add(Number(p));abs.add(Number(r<0n?-r:r));quarters[Number(q)]++;if(r===-160n||r===160n)tie++;if(r===0n)zero++;signed++;}}
const result={keys:keys.length,stored:b.rows.length,signed,errorCount:errs.length,residues:res.size,abs:abs.size,quarters,tie,zero};
console.log(JSON.stringify(result,null,2));
if(JSON.stringify(result)!==JSON.stringify({keys:7835,stored:7835,signed:15670,errorCount:0,residues:1276,abs:161,quarters:[4208,3937,3590,3935],tie:156,zero:148}))process.exitCode=1;
