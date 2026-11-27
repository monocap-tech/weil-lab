// IV257: replay the exact finite-prefix obstruction from the full even receipt.
import fs from "node:fs";
import crypto from "node:crypto";
const data=fs.readFileSync(new URL("./iv257_schur_even.json",import.meta.url));
const sha=crypto.createHash("sha1").update("blob "+data.length+"\0").update(data).digest("hex");
if(sha!=="e5d8d375dbc8d49e88f966ddd082522f0a4ffa31")throw Error("source receipt identity");
const a=JSON.parse(data.toString("utf8")),S=BigInt(a.scale);
if(a.stage!=="complete"||a.par!==0||a.retained!==256||a.diagonal_receipts.length!==256||S!==10n**400n)throw Error("scope");
const v=a.diagonal_receipts.map((r,i)=>({...r,row:i,upper:BigInt(r.F_center)+BigInt(r.F_radius),pen:500n*BigInt(r.prefix_residual_lower)})).sort((a,b)=>a.pen>b.pen?-1:1)[0];
const upper=v.upper*S-v.pen;
if(!(v.upper<2n*S&&BigInt(v.prefix_residual_lower)>5n*S*S&&upper< -2800n*S*S))throw Error("obstruction bound");
const bad=a.diagonal_receipts.filter(r=>(BigInt(r.F_center)+BigInt(r.F_radius))*S<500n*BigInt(r.prefix_residual_lower)).length;
if(bad!==117||v.row!==251||v.mode!==24)throw Error("census");
console.log(JSON.stringify({source_receipt_blob:sha,parity:0,trial_cutoff:a.J,residual_prefix_end:a.residual_prefix_end,scale:a.scale,congruence_row:v.row,pivot_mode:v.mode,F_upper_scaled:String(v.upper),partial_unnormalized_residual_square_lower_scaled_squared:v.prefix_residual_lower,uniform_inverse_penalty_lower_scaled_squared:String(v.pen),uniform_receiver_upper_scaled_squared:String(upper),negative_rows_from_prefix_only:bad,F_upper_lt:"2",partial_residual_square_gt:"5",uniform_receiver_upper_lt:"-2800",classification:"strict failure of the fixed finite trial with 1000 I inverse upper bound, even without far-tail loss; NOT a negative actual Schur direction"},null,2));
