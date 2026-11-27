#!/usr/bin/env node
// Run: node scripts/local_replay/NF618W02ResidualEndpointDemand.cjs
// From the repository root at the W02-NF-09 commit.
const fs=require("node:fs"),crypto=require("node:crypto"),assert=require("node:assert/strict");
function read(p,sha){const b=fs.readFileSync(p),h=crypto.createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex");assert.equal(h,sha);return JSON.parse(b)}
const A=read("notes/provisional/NF618W02ResidualSupport.json","90b71e032264cf18d4febac3c11d804fb6a9f4ec");
const B=read("notes/provisional/NF618W02SourceDemand.json","1edda66274a2090af027011b1c264156a63c11aa");
const m=new Map(B.rows.map(x=>[x[0],x]));assert.equal(m.size,7835);
const mod=(x,n)=>x-n*Math.floor(x/n);
function cohort(rows){const p=new Set(),r=new Set(),e=new Set(),h=new Set();let n=0,max=0;for(const [id,H,F,d] of rows){n+=d+1;max=Math.max(max,d);for(const s of [-1,1]){const v=mod(s*F,1280),u=mod(v,320);p.add(v);r.add(Math.min(u,320-u));e.add(s*H+","+v);h.add(s*H)}}return {p,r,e,h,tables:rows.length,rows:n,max}}
const intersect=(a,b)=>[...a].filter(x=>b.has(x));
const describe=x=>({tables:x.tables,rows:x.rows,phaseResidues:x.p.size,rootPowers:x.r.size,endpointPairs:x.e.size,realExponents:[...x.h].sort((a,b)=>a-b),maxDegree:x.max});
const all=A.ordinary.rows;assert.equal(new Set(all.map(x=>x[0])).size,7835);
for(const [id,H,F,d,ds,first,g,b] of all){const y=m.get(id);assert.ok(y);assert.deepEqual([H,F,d,g,b],[y[1],y[2],Math.max(y[3],y[4]),y[9],y[10]]);assert.deepEqual(ds,Array.from({length:d+1},(_,i)=>i));if(g===null)assert.ok(b>=25&&b<=39)}
const a=cohort(all.filter(x=>x[6]!==null)),b=cohort(all.filter(x=>x[6]===null)),f=cohort(A.folded.rows.filter(x=>x[6]===null));
const out={matchedSlots:all.length,admitted:describe(a),outstanding:describe(b),foldedOutstanding:describe(f),sharedPhases:intersect(a.p,b.p).length,sharedEndpoints:intersect(a.e,b.e).length,sharedRoots:intersect(a.r,b.r).length,outstandingExclusiveRoots:[...b.r].filter(x=>!a.r.has(x)).sort((a,b)=>a-b)};
assert.equal(out.sharedPhases,0);assert.equal(out.sharedEndpoints,0);assert.deepEqual(out.outstandingExclusiveRoots,[72,152]);console.log(JSON.stringify(out,null,2));
