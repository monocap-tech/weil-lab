// IV258: exact prefix Galerkin correction in inherited energy congruence coordinates.
// Uses the pinned IV253 fixed-point interval kernel, with extended scalar tails.
// Node: node research/iv261_null_tail_test.mjs 0 (or 1), from any directory.
function receiver(source,audit,par,J=768,P=400,moments=320) {
  const anchor="function run(P=220,J=128){";
  const end="function cert(par){";
  if(!source.includes(anchor)||!source.includes(end)||!source.includes("const K=1024n,A=4n*K+1n,L=80,E=56")||!source.includes("const nodes=[];\nfor(let j=0;j<J;j++)"))throw Error("dependency anchors");
  const rotOld="s=Z,c=one;for(let j=0;j<J;j++){sn[j]=add(sn[j],mul(a,s));let diag=mul(sub(I(4n),l),c);if(j>0)diag=sub(diag,div(s,rat(alpha,BigInt(j),1n)));else diag=rat(diag,2n,1n);pd[j]=add(pd[j],mul(a,diag));[s,c]=[add(mul(s,ct),mul(c,st)),sub(mul(c,ct),mul(s,st))]}",rotNew="B0=fl(st[0]+st[1],2n),C0=fl(ct[0]+ct[1],2n),E0=max([B0-st[0],st[1]-B0,C0-ct[0],ct[1]-C0]);let u=0n,v=S;if(BigInt(J)*(4n*E0+2n)>=S)throw Error('rotation guard');for(let j=0;j<J;j++){let err=BigInt(j)*(4n*E0+2n),s=[u-err,u+err],c=[v-err,v+err];sn[j]=add(sn[j],mul(a,s));let diag=mul(sub(I(4n),l),c);if(j>0)diag=sub(diag,div(s,rat(alpha,BigInt(j),1n)));else diag=rat(diag,2n,1n);pd[j]=add(pd[j],mul(a,diag));[u,v]=[fl(u*C0+v*B0,S),fl(v*C0-u*B0,S)]}",prefixOld="for(let n=0;n<Number(K);n++){let x=I(BigInt(4*n+1),4n),xx=mul(x,x),den=add(xx,t);g=add(g,div(t,mul(x,den)));B=add(B,rat(div(one,den),1n,4n));D=add(D,rat(div(xx,mul(den,den)),1n,4n))}",prefixNew="if(t[0]<0n)throw Error('nonnegative node');const SS=S*S,SSS=SS*S;for(let n=0;n<Number(K);n++){const q=BigInt(4*n+1),q2=q*q,d0=q2*S+16n*t[0],d1=q2*S+16n*t[1];g=add(g,[fl(64n*S*t[0],q*d0),ce(64n*S*t[1],q*d1)]);B=add(B,[fl(4n*SS,d1),ce(4n*SS,d0)]);D=add(D,[fl(4n*q2*SSS,d1*d1),ce(4n*q2*SSS,d0*d0)])}";
  if(!source.includes(rotOld)||!source.includes(prefixOld))throw Error("extended kernel anchors");
  const kernel=source.slice(source.indexOf(anchor),source.indexOf(end))
    .replace(anchor,"function run(P,J,par){")
    .replace(rotOld,rotNew).replace(prefixOld,prefixNew)
    .replace("const K=1024n,A=4n*K+1n,L=80,E=56","const K=2048n,A=4n*K+1n,L=400,E=160")
    .replace("k<=500;k++","k<=1000;k++")
    .replace("k<260;k++","k<460;k++").replace("let j=521n;","let j=921n;")
    .replace("k<180;k++","k<320;k++").replace("361n*d**361n","641n*d**641n")
    .replace("k<=250;k++","k<=350;k++").replace("S*2n**251n*126n,fac[251]*125n","S*2n**351n*176n,fac[351]*175n")
    .replace("k<110n;k++","k<160n;k++").replace("S*4n**220n,fac[220]","S*4n**320n,fac[320]")
    .replaceAll("n<80;n++","n<140;n++").replace("2400n*7n**321n","2400n*7n**561n")
    .replace("const nodes=[];\nfor(let j=0;j<J;j++)","const nodes=[];\nfor(let j=par;j<J;j+=2)")
    +"return {S,fl,ce,I,add,sub,mul,div,rat,abs,min,max,isqrt,alpha,e2,nodes,entry,log,trig,bank};\n}";
  const {S,fl,ce,I,add,sub,mul,div,rat,abs,min,max,isqrt,alpha,e2,nodes,entry,log,trig,bank}=new Function(kernel+"\nreturn run;")()(P,2*J,par);
  const n=256,t=J/2,h=t-n,N=J,absint=x=>x<0n?-x:x;
  if((par!==0&&par!==1)||J<=512||J%2||J>768||P!==400||moments<1)throw Error("scope");
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
    // Diagonal pivoting, within the high and low blocks separately.
    let kmax=i,last=i<h?h:t;
    for(let k=i+1;k<last;k++)if(A[k][k]>A[kmax][kmax])kmax=k;
    if(kmax!==i){
      [A[i],A[kmax]]=[A[kmax],A[i]];
      for(let k=0;k<t;k++)[A[k][i],A[k][kmax]]=[A[k][kmax],A[k][i]];
      [L[i],L[kmax]]=[L[kmax],L[i]];
      [order[i],order[kmax]]=[order[kmax],order[i]];
    }
    const d=A[i][i];D.push(d);
    if(d<=0n){
      const u=Array(t).fill(0n);u[i]=S;
      for(let j=i-1;j>=0;j--){let z=0n;for(let k=j+1;k<=i;k++)z+=u[k]*L[k][j];u[j]=-fl(z,S)}
      const w=Array(t).fill(0n);for(let k=0;k<=i;k++)w[order[k]]=u[k];
      let val=0n;for(let k=0;k<t;k++){let z=0n;for(let l=0;l<t;l++)z+=M[k][l]*w[l];val+=w[k]*z}
      const wn=w.reduce((s,x)=>s+absint(x),0n),err=rad*wn*wn;
      return {par,J,P,certified:false,stage:"pivoted proposal LDL",index:i,mode:nodes[order[i]].j,pivot:String(d),rad:String(rad),min_previous_pivot:String(min(D.slice(0,-1))),witness_norm_l1_scaled:String(wn),witness_Q_numerator_lower:String(val-err),witness_Q_numerator_upper:String(val+err),witness_Q_scale:String(S*S*S),witness_sign:val+err<0n?"negative":val-err>0n?"positive":"unresolved",pivot_order:order.map(k=>nodes[k].j),witness_coefficients_scaled:w.map(String)};
    }
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
    if(w[order[i]]<=0n||order.slice(i+1).some(k=>w[k]!==0n))throw Error("noninvertible retained map");
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

  // IV258: use all prefix high rows as a single Galerkin correction.
  // The low projection W is unchanged. The high solve is only a proposal.
  const T=10n**12n,hh=N-n;
  const H=Array.from({length:hh},()=>Array(hh)),Y=Array.from({length:n},()=>Array(hh));
  let hrad=0n,yrad=0n;
  function quant(a){let mid=fl((a[0]+a[1])*T,2n*S);return [mid,max([mid-fl(a[0]*T,S),ce(a[1]*T,S)-mid])];}
  for(let i=0;i<hh;i++)for(let j=0;j<=i;j++){
    const [x,err]=quant(entry(nodes[n+i],nodes[n+j]));H[i][j]=H[j][i]=x;if(err>hrad)hrad=err;
  }
  for(let i=0;i<n;i++)for(let j=0;j<hh;j++){
    const [x,err]=quant([V[i][n+j]-e[i],V[i][n+j]+e[i]]);
    Y[i][j]=x;if(err>yrad)yrad=err;
  }
  if(hrad>2n||yrad>2n)throw Error("coarse correction enclosure");
  const ld=Array.from({length:hh},()=>new Float64Array(hh));
  for(let i=0;i<hh;i++)for(let j=0;j<=i;j++){
    let x=Number(H[i][j])/Number(T);for(let k=0;k<j;k++)x-=ld[i][k]*ld[j][k];
    if(i===j){if(!(x>0))throw Error("high proposal");ld[i][i]=Math.sqrt(x);}else ld[i][j]=x/ld[j][j];
  }
  const Z=[],zn=[];
  for(let i=0;i<n;i++){
    const y=new Float64Array(hh),z=new Float64Array(hh);
    for(let j=0;j<hh;j++){let a=-Number(Y[i][j])/Number(T);for(let k=0;k<j;k++)a-=ld[j][k]*y[k];y[j]=a/ld[j][j];}
    for(let j=hh-1;j>=0;j--){let a=y[j];for(let k=j+1;k<hh;k++)a-=ld[k][j]*z[k];z[j]=a/ld[j][j];}
    const zz=Array.from(z,v=>{const q=Math.round(v*Number(T));if(!Number.isSafeInteger(q))throw Error("proposal quantization");return BigInt(q);});
    Z.push(zz);zn.push(zz.reduce((s,x)=>s+absint(x),0n));
  }
  // Exact prefix residual centers with denominator T^2.
  const R=[],er=[];let pre=0n,newPre=0n,maxPre=0n,maxZ=0n;
  const prediag=[],postdiag=[];
  for(let i=0;i<n;i++){
    const u=Y[i],z=Z[i],v=Array(hh),err=yrad*T+hrad*zn[i];er.push(err);if(zn[i]>maxZ)maxZ=zn[i];
    let p=0n,q=0n;
    for(let j=0;j<hh;j++){
      v[j]=u[j]*T+dot(H[j],z);q+=(absint(v[j])+err)**2n;
      const x=absint(u[j]);p+=(x>yrad?x-yrad:0n)**2n;
    }
    R.push(v);prediag.push(p);postdiag.push(q);pre+=p;newPre+=q;if(q>maxPre)maxPre=q;
  }
  // Exact symmetric enclosure for corrected trial F':
  // F'ij=Fij+<Y_i,Z_j>+<Z_i,R_j>, where residual R_j=Y_j+H Z_j.
  // Convert F to units T^3 with directed bounds, then use exact products.
  const F1=Array.from({length:n},()=>Array(n)),F1r=Array.from({length:n},()=>Array(n)),T3=T**3n;
  let dmin=0n,dmax=0n,trLo=0n,trHi=0n,ferr=0n,gersh=0n;
  const diag=[];
  for(let i=0;i<n;i++)for(let j=0;j<=i;j++){
    const f=fl(F0[i][j]*T3,S),ferr0=ce(Fr[i][j]*T3,S)+1n;
    const v=f+T*dot(Y[i],Z[j])+dot(Z[i],R[j]);
    const rr=ferr0+yrad*zn[j]*T+zn[i]*er[j];
    F1[i][j]=F1[j][i]=v;F1r[i][j]=F1r[j][i]=rr;
  }
  for(let i=0;i<n;i++){
    const lo=F1[i][i]-F1r[i][i],hi=F1[i][i]+F1r[i][i];
    let r=0n,rs=0n;for(let j=0;j<n;j++){rs+=F1r[i][j];if(i!==j)r+=absint(F1[i][j])+F1r[i][j];}
    const g=lo-r;if(i===0||g<gersh)gersh=g;if(rs>ferr)ferr=rs;
    if(i===0||lo<dmin)dmin=lo;if(i===0||hi>dmax)dmax=hi;trLo+=lo;trHi+=hi;
    diag.push({row:i,mode:nodes[order[h+i]].j,old_prefix_square_lower:String(prediag[i]),corrected_prefix_square_upper:String(postdiag[i]),corrected_trial_lower:String(lo),corrected_trial_upper:String(hi),corrected_trial_gershgorin:String(g)});
  }
  // Full corrected trial coefficients, unchanged low projection, exact grid T.
  const ratio=S/T;if(ratio*T!==S)throw Error("scale ratio");
  const W1=W.map((w,i)=>Array.from({length:N},(_,j)=>(j<t?w[j]:0n)+(j>=n?Z[i][j-n]*ratio:0n)));
  if(W1.some((w,i)=>w.slice(0,n).some((x,j)=>x!==W[i][j])))throw Error("changed low projection");
  // Evaluate first signed moments using the pole-absorbed divided difference.
  // For j!=k: Q_jk=(a'_j-a'_k)/(j^2-k^2).
  const alpha2=mul(alpha,alpha),sig=par===0?1n:-1n,pc=rat(sub(rat(e2,sig,1n),I(2n)),1n,2n);
  const a=nodes.map(x=>sub(add(rat(div(mul(x.z,x.B),alpha2),2n,1n),rat(div(x.sn,alpha),2n,1n)),div(pc,mul(alpha2,add(I(1n,4n),x.z)))));
  const A0=a.map(x=>fl(x[0]+x[1],2n)),Ar=a.map((x,k)=>max([A0[k]-x[0],x[1]-A0[k]]));
  let m0max=0n,n0max=0n,n0err=0n,wmax=0n;
  const moment0=W1.map((w,i)=>{
    const m=w.reduce((s,x)=>s+x,0n),wa=w.map(absint),wn=wa.reduce((s,x)=>s+x,0n);
    const nn=dot(w,A0),ne=dot(wa,Ar);
    const mu=absint(m),nu=ce(absint(nn)+ne,S);if(mu>m0max)m0max=mu;if(nu>n0max)n0max=nu;if(ce(ne,S)>n0err)n0err=ce(ne,S);if(wn>wmax)wmax=wn;
    return {row:i,moment0_scaled:String(m),absorbed_moment0_center_scaled_squared:String(nn),absorbed_moment0_radius_scaled_squared:String(ne)};
  });

  {
  // IV261: necessary test for the fixed lifted IV256 inverse receiver.
  // Exact nullspace of the rational IV260 four-channel correction map.
  if(par!==0||audit.all4.detail.length!==n)throw Error("scope");
  const C=audit.all4.detail.map(x=>x.coefficient_scaled.map(BigInt)),kdim=4;
  const Cfloat=C[0].map((_,b)=>C.map(r=>Number(r[b])/1e20));
  const piv=[];
  for(let b=0;b<4;b++){
    let k=-1,mx=0;
    for(let i=0;i<n;i++)if(!piv.includes(i)&&Math.abs(Cfloat[b][i])>mx){mx=Math.abs(Cfloat[b][i]);k=i}
    if(k<0||mx<1e-10)throw Error("rank");
    piv.push(k);
    for(let c=b+1;c<4;c++){let z=Cfloat[c][k]/Cfloat[b][k];for(let i=0;i<n;i++)Cfloat[c][i]-=z*Cfloat[b][i]}
  }
  const free=Array.from({length:n},(_,i)=>i).filter(i=>!piv.includes(i)),nf=free.length;
  const Piv=Array.from({length:4},(_,b)=>piv.map(i=>C[i][b]));
  function det(A){if(!A.length)return 1n;return A[0].reduce((s,x,i)=>s+(i%2?-1n:1n)*x*det(A.slice(1).map(r=>r.filter((_,k)=>k!==i))),0n)}
  function adj(A){return A.map((r,i)=>r.map((_,j)=>((i+j)%2?-1n:1n)*det(A.filter((_,k)=>k!==j).map(r=>r.filter((_,k)=>k!==i)))))}
  const de=det(Piv),ad=adj(Piv);if(de===0n)throw Error("singular nullspace");
  const pv=free.map(i=>ad.map(r=>-dot(r,C[i])));
  const mat=free.map((i,k)=>{let u=new Float64Array(n);u[i]=1;for(let b=0;b<4;b++)u[piv[b]]=Number(pv[k][b])/Number(de);return u});
  const ff=F1.map(r=>r.map(x=>Number(x)/Number(T3)));
  const A=Array.from({length:nf},()=>new Float64Array(nf));
  const FF=mat.map(u=>ff.map(r=>r.reduce((s,x,i)=>s+x*u[i],0)));
  for(let i=0;i<nf;i++)for(let j=0;j<=i;j++)A[i][j]=A[j][i]=mat[i].reduce((s,x,k)=>s+x*FF[j][k],0);
  // Jacobi eigensolver only proposes directions. All final signs exact.
  const E=Array.from({length:nf},(_,i)=>Float64Array.from({length:nf},(_,j)=>i===j?1:0));
  for(let sweep=0;sweep<18;sweep++){
    let mx=0;
    for(let i=0;i<nf;i++)for(let j=i+1;j<nf;j++){
      const x=A[i][j];mx=Math.max(mx,Math.abs(x));if(Math.abs(x)<1e-17)continue;
      const tau=(A[j][j]-A[i][i])/(2*x),t0=(tau>=0?1:-1)/(Math.abs(tau)+Math.hypot(1,tau)),c=1/Math.hypot(1,t0),s=t0*c;
      const ai=A[i][i],aj=A[j][j];A[i][i]=ai-t0*x;A[j][j]=aj+t0*x;A[i][j]=A[j][i]=0;
      for(let k=0;k<nf;k++)if(k!==i&&k!==j){let u=A[k][i],v=A[k][j];A[k][i]=A[i][k]=c*u-s*v;A[k][j]=A[j][k]=s*u+c*v}
      for(let k=0;k<nf;k++){let u=E[k][i],v=E[k][j];E[k][i]=c*u-s*v;E[k][j]=s*u+c*v}
    }
    if(mx<1e-15)break;
  }
  const idx=Array.from({length:nf},(_,i)=>i).sort((i,j)=>A[i][i]-A[j][j]).slice(0,24);
  const cs=10n**14n,den=absint(de)*cs,sgn=de<0n?-1n:1n;
  const cand=idx.map(k=>{
    const u=E.map(r=>BigInt(Math.round(r[k]*Number(cs)))),v=Array(n).fill(0n);
    for(let i=0;i<nf;i++)v[free[i]]=u[i]*absint(de);
    for(let b=0;b<4;b++)v[piv[b]]=sgn*pv.reduce((s,r,i)=>s+r[b]*u[i],0n);
    for(let b=0;b<4;b++)if(v.reduce((s,x,i)=>s+x*C[i][b],0n)!==0n)throw Error("nullspace check");
    const vnorm=v.reduce((s,x)=>s+x*x,0n);
    let q=0n,qr=0n;
    for(let i=0;i<n;i++)for(let j=0;j<n;j++){let z=v[i]*v[j];q+=z*F1[i][j];qr+=absint(z)*F1r[i][j]}
    // Trial column combination in original finite cosine coefficients.
    const w=Array.from({length:N},(_,j)=>v.reduce((s,x,i)=>s+x*W1[i][j],0n));
    // Quantize this rational vector at 10^200; its errors are accounted in each channel.
    const BB=10n**200n,wt=w.map(x=>fl(x*BB,den*S));
    return {k,proposal:A[k][k],v,vnorm,q,qr,wt,wa:wt.map(absint),BB,pen:0n,resmax:0n,rows:[]};
  });
  // For j>=28672, exact lower bound of diagonal tail penalty in lifted majorant:
  // D_T(j)=1/5+log(j/28672) <= 1/5+(j-28672)/28672.
  // Each actual unnormalized row contributes |t_j|^2/(2D_T(j)).
  // Evaluate a complete 1024-row initial tail block using signed rational moments.
  const split=28672,last=split+2048,BB=cand[0].BB;
  const alpha2b=mul(alpha,alpha),lam=div(I(2n),alpha),a0=div(I(1n),rat(alpha2b,2n,1n));
  const aM=a.map(x=>fl(x[0]+x[1],2n)),aR=a.map((x,i)=>max([aM[i]-x[0],x[1]-aM[i]]));
  const sn=Array((last-split)/2).fill(I(0n));
  for(const [nn,p] of bank){
    const l=log(BigInt(nn)),sq=isqrt(BigInt(nn)*S*S),aa=div(log(BigInt(p)),[sq,sq+1n]),theta=mul(alpha,l);
    const [si,co]=trig(rat(theta,BigInt(split),1n)),[ss,cc]=trig(rat(theta,2n,1n));
    const x0=fl(si[0]+si[1],2n),y0=fl(co[0]+co[1],2n),a1=fl(ss[0]+ss[1],2n),b1=fl(cc[0]+cc[1],2n);
    const E0=max([x0-si[0],si[1]-x0,y0-co[0],co[1]-y0]),Er=max([a1-ss[0],ss[1]-a1,b1-cc[0],cc[1]-b1]);
    let x=x0,y=y0;
    if(2n*E0+BigInt(sn.length)*(4n*Er+2n)>=S)throw Error("rotation");
    for(let k=0;k<sn.length;k++){const e=2n*E0+BigInt(k)*(4n*Er+2n);sn[k]=add(sn[k],mul(aa,[x-e,x+e]));[x,y]=[fl(x*b1+y*a1,S),fl(y*b1-x*a1,S)]}
  }
  const Vscale=10n**40n;
  for(let j=split;j<last;j+=2){
    const jj=BigInt(j),jj2=jj*jj,aj=add(add(rat(add(I(2n),mul(lam,sn[(j-split)/2])),jj,1n),a0),[-ce(16n*S,jj)-ce(S,1000n),ce(16n*S,jj)+ce(S,1000n)]);
    const am=fl(aj[0]+aj[1],2n),ae=max([am-aj[0],aj[1]-am]);
    // Exact directed features 1/(j^2-k^2) and A'_k/(j^2-k^2), coarsened to BB.
    const fm=[],fr=[],gm=[],gr=[];
    for(let k=0;k<N;k++){
      const d=jj2-BigInt(nodes[k].j)**2n,lo=fl(BB,d),hi=ce(BB,d);
      fm.push(lo);fr.push(hi-lo);
      const gl=fl((aM[k]-aR[k])*BB,S*d),gu=ce((aM[k]+aR[k])*BB,S*d);
      gm.push(fl(gl+gu,2n));gr.push(max([gm[k]-gl,gu-gm[k]]));
    }
    const ef=fm.reduce((s,x,k)=>s+absint(x)+fr[k],0n),eg=gm.reduce((s,x,k)=>s+absint(x)+gr[k],0n);
    for(const o of cand){
      const mc=dot(o.wt,fm),me=dot(o.wa,fr)+ef,nc=dot(o.wt,gm),ne=dot(o.wa,gr)+eg;
      // t= A'_j M - N; signed cancellation kept in exact intervals.
      const v=am*mc-S*nc,er=absint(am)*me+ae*(absint(mc)+me)+S*ne;
      const lo=fl(max([0n,absint(v)-er])*Vscale,S*BB*BB),hi=ce((absint(v)+er)*Vscale,S*BB*BB);
      const dnum=BigInt(split)+5n*BigInt(j-split),dd=5n*BigInt(split);
      // Vscale^2 units, actual penalty lower, 1/(2 D_T).
      o.pen+=fl(lo*lo*dd,2n*dnum);if(hi>o.resmax)o.resmax=hi;
      if(j===split||j===last-2)o.rows.push({j,abs_lower_scaled:String(lo),abs_upper_scaled:String(hi)});
    }
  }
  const out=cand.map(o=>{
    const fup=ce((o.q+o.qr)*Vscale*Vscale,T3*den*den),flo=fl((o.q-o.qr)*Vscale*Vscale,T3*den*den);
    return {proposal_index:o.k,proposal_eigenvalue:o.proposal,norm_squared_numerator:String(o.vnorm),trial_lower_scaled_squared:String(flo),trial_upper_scaled_squared:String(fup),partial_tail_penalty_lower_scaled_squared:String(o.pen),receiver_upper_scaled_squared:String(fup-o.pen),negative:fup-o.pen<0n,residual_max_upper_scaled:String(o.resmax),sample_rows:o.rows,vector_numerators:o.v.map(String)};
  });
  return {par,J,P,retained:n,correction_null_rank:4,null_dimension:nf,pivot_rows:piv,vector_denominator:String(den),trial_cutoff:2*J,tail_first:split,tail_last_exclusive:last,tail_rows:(last-split)/2,scale:String(Vscale),candidate_count:out.length,negative_receiver_count:out.filter(x=>x.negative).length,records:out,classification:"Necessary test on exact correction-null subspace: negative receiver upper rejects fixed IV256 lifted inverse majorant, not actual Schur positivity."};
  }
}
// Node CLI
import fs from "node:fs";
import crypto from "node:crypto";
const dep=fs.readFileSync(new URL("./iv253_am_exact_compression.mjs",import.meta.url));
const sha=crypto.createHash("sha1").update("blob "+dep.length+"\0").update(dep).digest("hex");
if(sha!=="b748429e9c9dff261014f9cb46f09bca9268c738")throw Error("IV253 source identity");
const par=Number(process.argv[2]);
if(par!==0&&par!==1)throw Error("parity argument 0 or 1");
const raw=fs.readFileSync(new URL("./iv260_all_direction_audit.json",import.meta.url));
if(crypto.createHash("sha1").update("blob "+raw.length+"\0").update(raw).digest("hex")!=="8b51ae5eb9a4be2ed8e0bbc4cb05a87c275e3dec")throw Error("audit identity");
const out=receiver(dep.toString("utf8"),JSON.parse(raw.toString("utf8")),par);
console.log(JSON.stringify(out,null,2));
