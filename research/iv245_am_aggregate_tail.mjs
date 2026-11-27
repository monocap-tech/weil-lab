// IV245 exact error and inherited-witness transfer audit. Run from repository root.
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
function audit(prior,witness){
 const S=10n**15n;if(prior.scale!==String(S)||witness.scale!==String(S)||BigInt(prior.e2[0])<=7n*S)throw Error("input");
 const d=7n**17n,ceil=(a,b)=>(a+b-1n)/b;
 if(4n*10n**13n>=d-1n)throw Error("operator error");
 const norm=BigInt(witness.norm[1]),q64=BigInt(witness.rows.find(r=>r.m===64).lower);
 const loss=ceil(4n*norm,d-1n),bound=q64-loss;
 if(bound<=509558000000n)throw Error("witness");
 return {scale:String(S),retained_explicit_boundary_terms:4,epsilon_upper:{n:"1",d:String(d)},operator_error_upper:{n:"4",d:String(d-1n)},coarse_error_upper:"1/10000000000000",witness_norm_squared_upper:String(norm),witness_Q64_lower:String(q64),witness_loss_upper:String(loss),aggregate_witness_lower:String(bound)};
}
const paths=["research/iv243_am_structured_receiver.json","research/iv244_am_mixed_witness.json"], pins=["f83acc6c0e2caf3e05815c3dea219c8ad1774ddb","3906416100c3b468066607c92eb5ac99f858e657"];
const inputs=paths.map((p,i)=>{const b=readFileSync(p);if(createHash('sha1').update('blob '+b.length+'\0').update(b).digest('hex')!==pins[i])throw Error('input identity');return JSON.parse(b);});
console.log(JSON.stringify(audit(inputs[0].exact,inputs[1]),null,2));
