// IV260 exact all-direction audit.
function audit(d,a){
 const S=BigInt(d.scale),U=BigInt(a.scale),R=10n**20n,N=a.retained,abs=x=>x<0n?-x:x,fl=(n,d)=>{if(d<=0n)throw Error("den");return n>=0n?n/d:-((-n+d-1n)/d)},ce=(n,d)=>-fl(-n,d),max=a=>a.reduce((x,y)=>x>y?x:y);
 const y=a.tail_rows.map(r=>r.correlation_centers.map(BigInt)),er=a.tail_rows.map(r=>r.correlation_radii.map((v,b)=>BigInt(v)+ce(BigInt(d.extra_correlation_radius[b])*U,S)));
 const D0=a.bands.map(x=>BigInt(x.energy_upper_scaled)),prod=D0.reduce((x,y)=>x*y,1n),old=y.map(v=>v.map((z,b)=>z*(prod/D0[b])));
 const G0=d.prefix_gram.map(r=>r.map(z=>z.map(BigInt))),Gp=d.projected_prefix_gram.map(r=>r.map(z=>z.map(BigInt))),D=d.projected_energy_upper.map(r=>r.map(BigInt)),E=d.projected_factor_inverse_upper.map(r=>r.map(BigInt));
 const quad=(v,M)=>v.reduce((s,x,i)=>s+v.reduce((z,w,j)=>z+x*w*M[i][j],0n),0n);
 function qiv(v,M){let lo=0n,hi=0n;for(let i=0;i<v.length;i++)for(let j=0;j<v.length;j++){const p=v[i]*v[j],q=M[i][j];lo+=p*(p>=0n?q[0]:q[1]);hi+=p*(p>=0n?q[1]:q[0]);}return [lo,hi]}
 let oldlo=0n,oldhi=0n;for(const v of old){const z=qiv(v,G0);oldlo+=z[0];oldhi+=z[1];}
 const oldScaledLo=fl(oldlo,prod*prod),oldScaledHi=ce(oldhi,prod*prod);
 // Frobenius squared residual: >= injection/2 - old residual square.
 const prefixBefore=ce(437n*S,10n**20n);
 const oldAfterLo=fl(oldScaledLo,2n)-prefixBefore;
 function det(A){if(!A.length)return 1n;return A[0].reduce((z,v,k)=>z+(k%2?-1n:1n)*v*det(A.slice(1).map(r=>r.filter((_,i)=>i!==k))),0n)}
 function adj(A){return A.map((r,i)=>r.map((_,j)=>((i+j)%2?-1n:1n)*det(A.filter((_,k)=>k!==j).map(r=>r.filter((_,k)=>k!==i)))))}
 function inertia(A){let pos=0,neg=0;A=A.map(r=>r.slice());while(A.length){let k=A.findIndex((r,i)=>r[i]!==0n);if(k<0)throw Error("zero pivot");if(k!==0){[A[0],A[k]]=[A[k],A[0]];for(const r of A)[r[0],r[k]]=[r[k],r[0]];}const p=A[0][0];if(p>0n)pos++;else neg++;A=A.slice(1).map((r,i)=>r.slice(1).map((v,j)=>p*p*v-p*A[i+1][0]*A[0][j+1]));}return {pos,neg}}
 function isqrt(n){if(n<0n)throw Error("sqrt");if(n<2n)return n;let x=1n<<BigInt(Math.ceil(n.toString(2).length/2));while(true){const y=(x+n/x)/2n;if(y>=x)return x;x=y}}
 function pass(k){
   const A=D.slice(0,k).map(r=>r.slice(0,k)),dd=det(A),aa=adj(A);if(dd<=0n||inertia(A).pos!==k)throw Error("upper Gram");
   const C=y.map(v=>aa.map(row=>fl(row.reduce((z,w,b)=>z+w*v[b],0n)*S*R,U*dd)));
   let gain=0n,inj=0n,projEnergy=0n,errsq=0n,diagNeg=0;
   const den=U*S*R*R,detail=[];
   for(let i=0;i<N;i++){
     const c=C[i],ys=y[i],es=er[i];
     const lo=2n*S*R*c.reduce((s,x,b)=>s+ys[b]*x-es[b]*abs(x),0n)-U*quad(c,A);
     gain+=lo;
     const p=qiv(c,Gp)[1];inj+=p;
     const q=quad(c,E);projEnergy+=q;
     const rr=A.map((row,b)=>abs(ys[b]*S*R-U*row.reduce((z,x,j)=>z+x*c[j],0n))+es[b]*S*R);
     errsq+=rr.reduce((s,x)=>s+x*x,0n);
     const trialUp=BigInt(a.tail_rows[i].corrected_trial_upper_before_tail_scaled);
     if(trialUp*S*R*R-lo<0n)diagNeg++;
     detail.push({row:i,coefficient_scaled:c.map(String),energy_decrement_lower_numerator:String(lo),prefix_injection_upper_numerator:String(p),projected_inverse_energy_upper_numerator:String(q)});
   }
   const normInvNum=S*max(aa.map(row=>row.reduce((s,x)=>s+abs(x),0n)));
   const lossScaled=ce(10n*S*normInvNum*errsq,dd*(U*S*R)**2n);
   const Gc=A.map((r,i)=>r.map((_,j)=>C.reduce((z,c)=>z+c[i]*c[j],0n)));
   const thresholds=[S/1000n,S/100n,S/20n,S/10n,S/5n];
   const certs=thresholds.map(t=>({threshold_scaled:String(t),directions:inertia(Gc.map((r,i)=>r.map((v,j)=>9n*dd*v-10n*R*R*(lossScaled+t)*aa[i][j]))).pos}));
   const gainScaled=fl(gain*S,den),injScaled=ce(inj,R*R),projScaled=ce(projEnergy,2n*R*R);
   // Full tail projection of correction: bound low contribution below J/2 and high remainder of h3.
   const K=1536n,J=28672n,B0=J/2n;
   const l1=Array.from({length:k},(_,b)=>{const l=K*2n**BigInt(b),sq=BigInt(d.prefix_projection_column_square_upper[b]);return ce(S*K*K*(2n+l),64n*l*l)+isqrt(512n*sq*S)+1n});
   // High part of h3: gamma <=9+j/B0; use gamma^2 <=2(81+(j/B0)^2), ||K_orig||<32.
   // normalized action square <=4 sum h_j^2 (gamma_j^2+1024).
   const s4den=6n*B0**4n,s4num=6n+B0;
   const s2den=2n*B0**2n,s2num=2n+B0;
   const highScaled=ce(S*4n*K**4n*((1186n*s4num*s2den*B0**2n)+(2n*s2num*s4den)),1024n*s4den*s2den*B0**2n);
   let fullEnergyTrace=0n,maxFull=0n;
   for(let i=0;i<N;i++){
     const c=C[i],row=a.tail_rows[i],mu=BigInt(row.M_polynomial_abs_sum_scaled)+BigInt(row.M_model_error_scaled),nu=BigInt(row.N_polynomial_abs_sum_scaled)+BigInt(row.N_model_error_scaled);
     function oldTail(j){return ce(S*41n**2n*mu*mu,2n*(j-2n)*U*U)+ce(S*nu*nu,6n*(j-2n)**3n*U*U)}
     const oldI=oldTail(K)+prefixBefore,oldT=oldTail(J);
     const l=c.reduce((z,x,b)=>z+abs(x)*l1[b],0n);
     const lowCorr=ce(82n**2n*l*l,4n*(J-2n)*R*R*S);
     const highCorr=k===4?ce(highScaled*c[3]**2n,R*R):0n;
     const postT=2n*oldT+4n*(lowCorr+highCorr);
     const p=ce(quad(c,E),2n*R*R);
     const upper=5n*postT+3n*(125n*oldI+p+125n*40n**2n*postT);
     fullEnergyTrace+=upper;if(upper>maxFull)maxFull=upper;
   }
   return {channels:k,coefficient_scale:String(R),decrement_trace_lower_scaled:String(gainScaled),post_prefix_trace_upper_scaled:String(2n*(injScaled+prefixBefore)),prefix_injection_upper_scaled:String(injScaled),projected_inverse_action_trace_upper_scaled:String(projScaled),rank_lower_uniform_loss_scaled:String(lossScaled),rank_checks:certs,negative_trial_upper_diagonal_count:diagNeg,full_conservative_inverse_trace_upper_scaled:String(fullEnergyTrace),full_conservative_inverse_max_diagonal_upper_scaled:String(maxFull),full_bound_classification:"mixed argument bounded by operator norm, not signed numerical factorized solve on full residual; no sign clearance",detail};
 }
 const first=pass(3),all=pass(4);
 return {scale:String(S),old_iv259_prefix_injection_lower_scaled:String(oldScaledLo),old_iv259_prefix_injection_upper_scaled:String(oldScaledHi),old_iv259_post_prefix_lower_scaled:String(oldAfterLo),prefix_before_upper_scaled:String(prefixBefore),first3:first,all4:all,scope:"all 256 even directions; corrected channel action and conservative full majorant; actual full mixed inverse not sharply evaluated"};
}
import fs from "node:fs";
import crypto from "node:crypto";
function get(path,h){const b=fs.readFileSync(new URL(path,import.meta.url));if(crypto.createHash("sha1").update("blob "+b.length+"\0").update(b).digest("hex")!==h)throw Error("identity");return JSON.parse(b.toString("utf8"));}
console.log(JSON.stringify(audit(get("./iv260_digest.json","ec811065bb376e7f7fe3ceeaa4077f95e6be1a5c"),get("./iv259_analytic_tail_even.json","c74fbae341b8a129a1ac6102302cc5a8c8a7e77c")),null,2));
