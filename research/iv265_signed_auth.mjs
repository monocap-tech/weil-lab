// Authenticate local regeneration before relying on the historical signed and trial certificate.
import fs from 'node:fs';
import crypto from 'node:crypto';
const git=b=>crypto.createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const expected=['54dbb6a5c99c2e96cdcaf25db7dacb79ffb7c3f4','b15f1c141d72ac3e2204ff99691c9b7b72b8e5a1','ab9fe221d6e1f19be3fe34f9cf41e45affbd198f','1a705a2e2969c351256c72312ed57d9bf19e6fe7','f26075cc71432e09e0fcc29c82e91b7a51543d2f','6c94f4cb35878974da998518a3b390839ed87c64','5458e2244dadac410c24102ccde38b43145f54a1','28d296e665b8d2dbe784f2890934104616cbffdc'];
const read=p=>fs.readFileSync(new URL(p,import.meta.url));
const start=Date.now();const raw=read('signed_replay.json');const {meta,rows}=JSON.parse(raw.toString('utf8'));
if(rows.length!==256||meta.par!==1||meta.active!==456||meta.terms!==640||meta.K!==1536||meta.P!==400||rows.some((r,i)=>r.i!==i))throw Error('scope');
const parts=expected.map((h,i)=>{const first=32*i,last_exclusive=first+32,b=Buffer.from(JSON.stringify({first,last_exclusive,rows:rows.slice(first,last_exclusive)})+'\n');const actual=git(b);if(actual!==h)throw Error('signed segment '+i+' mismatch: '+actual+' != '+h);return {part:i,bytes:b.length,git_blob:actual,sha256:sha(b)}});
console.log('all signed segments byte-identical');
const s=read('iv264_finite_congruence.js');if(git(s)!=='1b010d7fb1eab5a563021f04714338fd7c1b87e8')throw Error('congruence source');
const fn=new Function(s.toString('utf8')+'\nreturn audit;')();const cert=fn(meta,rows);
const c=Buffer.from(JSON.stringify(cert,null,2)+'\n');if(git(c)!=='97928a1ce7b3a7752301146b25c92f1b23b78861')throw Error('basis mismatch: '+git(c));
if(!cert.certified||10000n*BigInt(cert.min_row)<=6276n*BigInt(cert.scale))throw Error('sign');
fs.writeFileSync(new URL('iv265_finite_congruence.json',import.meta.url),c);
const receipt={scope:'full odd signed data and exact finite trial replay; no actual Schur claim',rows:256,terms:640,active:456,parts,source_git_blobs:{kernel:git(read('iv253_am_exact_compression.mjs')),signed_export:git(read('iv264_signed_export.mjs')),finite_congruence:git(s)},signed_replay_sha256:sha(raw),signed_replay_bytes:raw.length,finite_congruence_git_blob:git(c),finite_congruence_sha256:sha(c),finite_congruence_bytes:c.length,min_row:cert.min_row,scale:cert.scale,elapsed_seconds:(Date.now()-start)/1000};
fs.writeFileSync(new URL('iv265_signed_auth.json',import.meta.url),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt,null,2));
