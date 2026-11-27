// IV257: exact finite-trial two-sided receiver in energy congruence coordinates.
// Uses the pinned IV253 fixed-point interval kernel, with extended scalar tails.
// Node: node research/iv257_schur_receiver.mjs 0 (or 1), from any directory.
function receiver(source,par,J=768,P=220,moments=192) {
  const anchor="function run(P=220,J=128){";
  const end="function cert(par){";
  if(!source.includes(anchor)||!source.includes(end)||!source.includes("const K=1024n,A=4n*K+1n,L=80,E=56")||!source.includes("const nodes=[];\nfor(let j=0;j<J;j++)"))throw Error("dependency anchors");
  const rotOld="s=Z,c=one;for(let j=0;j<J;j++){sn[j]=add(sn[j],mul(a,s));let diag=mul(sub(I(4n),l),c);if(j>0)diag=sub(diag,div(s,rat(alpha,BigInt(j),1n)));else diag=rat(diag,2n,1n);pd[j]=add(pd[j],mul(a,diag));[s,c]=[add(mul(s,ct),mul(c,st)),sub(mul(c,ct),mul(s,st))]}",rotNew="B0=fl(st[0]+st[1],2n),C0=fl(ct[0]+ct[1],2n),E0=max([B0-st[0],st[1]-B0,C0-ct[0],ct[1]-C0]);let u=0n,v=S;if(BigInt(J)*(4n*E0+2n)>=S)throw Error('rotation guard');for(let j=0;j<J;j++){let err=BigInt(j)*(4n*E0+2n),s=[u-err,u+err],c=[v-err,v+err];sn[j]=add(sn[j],mul(a,s));let diag=mul(sub(I(4n),l),c);if(j>0)diag=sub(diag,div(s,rat(alpha,BigInt(j),1n)));else diag=rat(diag,2n,1n);pd[j]=add(pd[j],mul(a,diag));[u,v]=[fl(u*C0+v*B0,S),fl(v*C0-u*B0,S)]}",prefixOld="for(let n=0;n<Number(K);n++){let x=I(BigInt(4*n+1),4n),xx=mul(x,x),den=add(xx,t);g=add(g,div(t,mul(x,den)));B=add(B,rat(div(one,den),1n,4n));D=add(D,rat(div(xx,mul(den,den)),1n,4n))}",prefixNew="if(t[0]<0n)throw Error('nonnegative node');const SS=S*S,SSS=SS*S;for(let n=0;n<Number(K);n++){const q=BigInt(4*n+1),q2=q*q,d0=q2*S+16n*t[0],d1=q2*S+16n*t[1];g=add(g,[fl(64n*S*t[0],q*d0),ce(64n*S*t[1],q*d1)]);B=add(B,[fl(4n*SS,d1),ce(4n*SS,d0)]);D=add(D,[fl(4n*q2*SSS,d1*d1),ce(4n*q2*SSS,d0*d0)])}";
  if(!source.includes(rotOld)||!source.includes(prefixOld))throw Error("extended kernel anchors");
  const kernel=source.slice(source.indexOf(anchor),source.indexOf(end))
    .replace(anchor,"function run(P,J,par){")
    .replace(rotOld,rotNew).replace(prefixOld,prefixNew)
    .replace("const K=1024n,A=4n*K+1n,L=80,E=56","const K=2048n,A=4n*K+1n,L=180,E=72")
    .replace("const nodes=[];\nfor(let j=0;j<J;j++)","const nodes=[];\nfor(let j=par;j<J;j+=2)")
    +"return {S,fl,ce,I,add,sub,mul,div,rat,abs,min,max,isqrt,alpha,e2,nodes,entry};\n}";
  const {S,fl,ce,I,add,sub,mul,div,rat,abs,min,max,isqrt,alpha,e2,nodes,entry}=new Function(kernel+"\nreturn run;")()(P,2*J,par);
  const n=256,t=J/2,h=t-n,N=J,absint=x=>x<0n?-x:x;
  if((par!==0&&par!==1)||J<=512||J%2||J>768||P!==220||moments<1)throw Error("scope");
  const order=[...Array.from({length:h},(_,i)=>n+i),...Array.from({length:n},(_,i)=>i)];
  let rad=0n;
  const M=Array.from({length:N},()=>Array(t));
  // Enclose symmetric finite block and rectangular mixed rows.
  for(let i=0;i<N;i++)for(let j=0;j<Math.min(i+1,t);j++){
    const a=entry(nodes[i],nodes[j]),mid=fl(a[0]+a[1],2n),err=max([mid-a[0],a[1]-mid]);
    if(err>rad)rad=err;M[i][j]=mid;if(i<t)M[j][i]=mid;
  }
  // Approximate integer LDL with high modes FIRST. This only proposes a trial and congruence.
  const A=order.map(i=>order.map(j=>M[i][j])),L=Array.from({length:t},()=>Array(t).fill(0n)),D=[];
  for(let i=0;i<t;i++){
    const d=A[i][i];D.push(d);
    if(d<=0n)return {par,J,P,certified:false,stage:"proposal LDL",index:i,pivot:String(d),rad:String(rad)};
    L[i][i]=S;
    for(let j=i+1;j<t;j++)L[j][i]=fl(A[j][i]*S,d);
    for(let j=i+1;j<t;j++)for(let k=j;k<t;k++){const x=A[k][j]-fl(L[k][i]*A[j][i],S);A[k][j]=A[j][k]=x}
  }
  // Only the last n rows of the inverse lower factor are needed.
  const W=[],wNorm=[],energyScales=[];
  for(let i=h;i<t;i++){
    const u=Array(t).fill(0n);u[i]=S;
    for(let j=i-1;j>=0;j--){let s=0n;for(let k=j+1;k<=i;k++)s+=u[k]*L[k][j];u[j]=-fl(s,S)}
    const scale=isqrt(S*S*S/D[i]);if(scale<=0n)throw Error("scale");
    const w=Array(t).fill(0n);for(let j=0;j<=i;j++)w[order[j]]=fl(u[j]*scale,S);
    if(w[i-h]<=0n||w.slice(i-h+1,n).some(x=>x!==0n))throw Error("noninvertible retained map");
    W.push(w);wNorm.push(w.reduce((s,x)=>s+absint(x),0n));energyScales.push(scale);
  }
  // W represents trial vectors in unnormalized cosine coordinates at scale S.
  // V[i][j] encloses <cos_j,Q w_i> with center and uniform per-column radius.
  const V=[],e=[];
  for(let i=0;i<n;i++){
    const w=W[i],v=[];
    for(let j=0;j<N;j++){let z=0n;for(let k=0;k<t;k++)z+=M[j][k]*w[k];v.push(fl(z,S))}
    V.push(v);e.push(ce(rad*wNorm[i],S)+1n);
  }
  const dot=(a,b)=>{let z=0n;for(let k=0;k<a.length;k++)z+=a[k]*b[k];return z};
  // Finite trial form F in congruence coordinates. Row-sum error bound around
  // exact symmetric rational centers; includes fixed-point rounding.
  let maxFdev=0n,minF=0n,maxF=0n,maxFerr=0n;
  const F0=Array.from({length:n},()=>Array(n)),Fr=Array.from({length:n},()=>Array(n));
  for(let i=0;i<n;i++)for(let j=0;j<=i;j++){
    let z=0n;for(let k=0;k<t;k++)z+=W[i][k]*V[j][k];
    const mid=fl(z,S),err=ce(wNorm[i]*e[j],S)+1n;
    F0[i][j]=F0[j][i]=mid;Fr[i][j]=Fr[j][i]=err;
  }
  for(let i=0;i<n;i++){
    let d=0n,r=0n;for(let j=0;j<n;j++){d+=absint(F0[i][j]-(i===j?S:0n));r+=Fr[i][j]}
    if(d+r>maxFdev)maxFdev=d+r;if(r>maxFerr)maxFerr=r;
    if(i===0||F0[i][i]-Fr[i][i]<minF)minF=F0[i][i]-Fr[i][i];if(i===0||F0[i][i]+Fr[i][i]>maxF)maxF=F0[i][i]+Fr[i][i];
  }
  // Far residual: exact combined divided difference a_j, with all weights.
  const alpha2=mul(alpha,alpha),a=nodes.slice(0,t).map(x=>add(rat(div(mul(x.z,x.B),alpha2),2n,1n),rat(div(x.sn,alpha),2n,1n)));
  const pole=nodes.slice(0,t).map(x=>div(I(1n),add(I(1n,4n),x.z)));
  const q=nodes.slice(0,t).map(x=>I(BigInt(x.j*x.j),BigInt(J*J)));
  const pp=Array(t).fill(I(1n)),ma=Array(n).fill(0n),mb=Array(n).fill(0n);
  const Wabs=W.map(w=>w.map(absint));
  function moment(weights) {
    const mid=weights.map(x=>fl(x[0]+x[1],2n)),rr=weights.map((x,k)=>max([mid[k]-x[0],x[1]-mid[k]]));
    return W.map((w,i)=>ce(absint(dot(w,mid))+dot(Wabs[i],rr),S)); // scaled upper absolute moment
  }
  let four=1n;
  for(let m=0;m<moments;m++){
    const x=moment(pp),y=moment(pp.map((v,k)=>mul(v,a[k])));
    for(let i=0;i<n;i++){ma[i]+=ce(x[i],four);mb[i]+=ce(y[i],four)}
    for(let k=0;k<t;k++)pp[k]=mul(pp[k],q[k]);four*=4n;
  }
  const upole=moment(pole),tail0=BigInt(2*J-2),far=[],pre=[],preLower=[];
  let allPre=0n,allFar=0n;
  let sumPrefixError=0n;
  for(let i=0;i<n;i++){
    const ai=40n*ma[i]+ce(80n*wNorm[i],four),bi=mb[i]+9n*upole[i];
    // Each far unnormalized row <= (ai/j+bi/j^2)/S.
    // Parity sum of squares, in units S^2.
    const fu=ce(ai*ai,tail0)+ce(bi*bi,3n*tail0**3n);
    far.push(fu);allFar+=fu;
    let pu=0n,pl=0n;for(let j=n;j<N;j++){const z=absint(V[i][j]);pu+=(z+e[i])**2n;pl+=(z>e[i]?z-e[i]:0n)**2n}
    pre.push(pu);preLower.push(pl);allPre+=pu;sumPrefixError+=BigInt(N-n)*e[i]**2n;
  }
  // Complete lower receiver: exact finite prefix Gram, bounded tail by trace.
  // R=V(prefix) plus errors. Young with epsilon=1/1000, then eta^-1/2
  // converts unnormalized residual rows into the physical L2 penalty 500.
  // All center matrices use denominator S^2, with exact symmetric row-sum.
  const Gram=Array.from({length:n},()=>Array(n));
  for(let i=0;i<n;i++)for(let j=0;j<=i;j++){let g=0n;for(let k=n;k<N;k++)g+=V[i][k]*V[j][k];Gram[i][j]=Gram[j][i]=g;}
  let lowerGersh=0n,maxPrefixDiag=0n,minUpper=0n,failDiag=0,maxPenIndex=0;
  const loss=500n*(1001n*sumPrefixError+allFar)+maxFerr*S;
  const diagRec=[];
  for(let i=0;i<n;i++){
    let radius=0n,diag=0n;
    for(let j=0;j<n;j++){
      const g=Gram[i][j];
      // 500*(1001/1000)=1001/2. Use doubled numerator throughout.
      const val=2n*F0[i][j]*S-1001n*g;
      if(j===i){diag=val-2n*loss;if(g>maxPrefixDiag){maxPrefixDiag=g;maxPenIndex=i}}else radius+=absint(val);
    }
    const lower=diag-radius;if(i===0||lower<lowerGersh)lowerGersh=lower;
    if(diag<0n)failDiag++;
    const u=(F0[i][i]+Fr[i][i])*S;if(i===0||u<minUpper)minUpper=u;
    diagRec.push({mode:nodes[i].j,F_center:String(F0[i][i]),F_radius:String(Fr[i][i]),prefix_residual_upper:String(pre[i]),prefix_residual_lower:String(preLower[i]),far_residual_upper:String(far[i]),lower_receiver_diagonal_doubled:String(diag),lower_gershgorin_doubled:String(lower)});
  }
  // Sign of the constructed *lower bound*, not of the exact Schur form if it fails.
  return {par,J,P,moments,retained:n,trial_high:h,residual_prefix_end:2*J,scale:String(S),matrix_entry_radius:String(rad),min_high_pivot_scaled:String(min(D.slice(0,h))),min_low_pivot_scaled:String(min(D.slice(h))),max_trial_l1_scaled:String(max(wNorm)),F_identity_deviation_scaled:String(maxFdev),F_error_row_max_scaled:String(maxFerr),F_diag_min_lower_scaled:String(minF),F_diag_max_upper_scaled:String(maxF),prefix_residual_trace_upper_scaled_squared:String(allPre),far_residual_trace_upper_scaled_squared:String(allFar),prefix_error_trace_scaled_squared:String(sumPrefixError),uniform_loss_scaled_squared:String(loss),max_prefix_gram_diagonal_scaled_squared:String(maxPrefixDiag),max_prefix_index:maxPenIndex,lower_receiver_min_gershgorin_doubled_scaled_squared:String(lowerGersh),lower_receiver_negative_diagonals:failDiag,certified:lowerGersh>0n,stage:"complete",diagonal_receipts:diagRec};
}

// Node CLI
import fs from "node:fs";
import crypto from "node:crypto";
const dep=fs.readFileSync(new URL("./iv253_am_exact_compression.mjs",import.meta.url));
const sha=crypto.createHash("sha1").update("blob "+dep.length+"\0").update(dep).digest("hex");
if(sha!=="b748429e9c9dff261014f9cb46f09bca9268c738")throw Error("IV253 source identity");
const par=Number(process.argv[2]);
if(par!==0&&par!==1)throw Error("parity argument 0 or 1");
const out=receiver(dep.toString("utf8"),par);
console.log(JSON.stringify(out,null,2));
