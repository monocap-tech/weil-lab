// Replay the executed IV264 congruence audit from committed signed rows.
import fs from "node:fs";
import crypto from "node:crypto";
const read=(p,sha)=>{const b=fs.readFileSync(new URL(p,import.meta.url));if(crypto.createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex")!==sha)throw Error(p+" identity");return b.toString("utf8")};
const m=JSON.parse(read("./iv264_signed_manifest.json","2e474178d131f872f648eca22e1b712f89a9b806"));
const rows=m.parts.flatMap((p,i)=>JSON.parse(read("./iv264_signed_part"+String(i).padStart(2,"0")+".json",p.sha)).rows);
if(rows.length!==256||rows.some((r,i)=>r.i!==i))throw Error("rows");
const fn=new Function(read("./iv264_finite_congruence.js","1b010d7fb1eab5a563021f04714338fd7c1b87e8")+"\nreturn audit;")();
const out=fn(m,rows);
if(!out.certified||10000n*BigInt(out.min_row)<=6276n*BigInt(out.scale))throw Error("sign");
console.log(JSON.stringify(out,null,2));
