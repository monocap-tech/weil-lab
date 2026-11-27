// IV259: actual analytic tail correction in inherited congruence coordinates.
// Uses the pinned IV253 fixed-point interval kernel, with extended scalar tails.
// Node: node research/iv259_analytic_tail_correction.mjs 0 (or 1), from any directory.
function receiver(source,par,J=768,P=400,moments=320) {
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

  // IV259: correlated analytic tail correction over the ENTIRE residual j>=K.
  // W has enormous coefficients only on k<K/2; Z/T has bounded l1 on k<K.
  const K=2*J,terms=512,B=10n**200n,U=10n**30n,us=U*U;
  const floorU=x=>fl(x*U,S), ceilU=x=>ce(x*U,S);
  const wc=W1.map(w=>w.map(x=>fl(x*B,S))),wa=wc.map(w=>w.map(absint));
  const qcoeff=Array.from({length:n},()=>[]),ncoeff=Array.from({length:n},()=>[]),Merr=Array(n).fill(0n),Nerr=Array(n).fill(0n);
  const Mnorm=Array(n).fill(0n),Nnorm=Array(n).fill(0n);
  const pp=[],rr=[];
  for(let k=0;k<N;k++){
    const q=I(BigInt(nodes[k].j)**2n,BigInt(K)**2n),d=sub(I(1n),q);
    if(d[0]<=0n)throw Error("tail support");
    const Dv=[isqrt(d[0]*S),isqrt(d[1]*S)+1n],rv=div(sub(I(1n),Dv),add(I(1n),Dv));
    if(Dv[0]*20n<=S||abs(rv)*21n>=19n*S)throw Error("full-tail ratio");
    if(k<t&&(Dv[0]*2n<=S||abs(rv)*13n>=S))throw Error("old support ratio");
    pp.push(div(I(1n),Dv));rr.push(rv);
  }
  const aMax=max(a.map(abs));
  function coeff(weights,out,errs,norms,m){
    const cv=weights.map(v=>{const x=fl((v[0]+v[1])*B,2n*S);return [x,max([x-fl(v[0]*B,S),ce(v[1]*B,S)-x])];});
    const mid=cv.map(x=>x[0]),rad=cv.map(x=>x[1]),extra=mid.reduce((s,x,k)=>s+absint(x)+rad[k],0n),factor=m===0?1n:2n;
    for(let i=0;i<n;i++){
      const center=dot(wc[i],mid)*factor,err=(dot(wa[i],rad)+extra)*factor;
      const val=fl(center*U,B*B),er=ce(err*U,B*B)+1n;
      out[i].push(val);errs[i]+=er;norms[i]+=absint(val);
    }
  }
  for(let m=0;m<terms;m++){
    coeff(pp,qcoeff,Merr,Mnorm,m);
    coeff(pp.map((x,k)=>mul(x,a[k])),ncoeff,Nerr,Nnorm,m);
    for(let k=0;k<N;k++)pp[k]=mul(pp[k],rr[k]);
  }
  // Exact uniform omitted-series bounds, separate original W and correction Z.
  // Original: 2/D<=4, 1/(1-r)<=13/12. Correction: 2/D<=40, 1/(1-r)<=21/2.
  const geomOld=3n*13n**BigInt(terms),pow19=19n**BigInt(terms),pow21=21n**BigInt(terms);
  let maxMerr=0n,maxNerr=0n,maxMnorm=0n,maxNnorm=0n;
  for(let i=0;i<n;i++){
    const oldRem=ce(13n*wNorm[i]*U,geomOld*S),newRem=ce(420n*zn[i]*pow19*U,T*pow21);
    Merr[i]+=oldRem+newRem;Nerr[i]+=ce((oldRem+newRem)*aMax,S);
    if(Merr[i]>maxMerr)maxMerr=Merr[i];if(Nerr[i]>maxNerr)maxNerr=Nerr[i];
    if(Mnorm[i]>maxMnorm)maxMnorm=Mnorm[i];if(Nnorm[i]>maxNnorm)maxNnorm=Nnorm[i];
  }
  // Compress only negligible signed coefficients, charging every omitted term.
  let active=terms;
  const mdrop=Array(n).fill(0n),ndrop=Array(n).fill(0n);
  while(active>1){
    let ok=true;for(let i=0;i<n;i++)if(mdrop[i]+absint(qcoeff[i][active-1])>U/10n**12n||ndrop[i]+absint(ncoeff[i][active-1])>U/10n**9n){ok=false;break}
    if(!ok)break;
    for(let i=0;i<n;i++){mdrop[i]+=absint(qcoeff[i][active-1]);ndrop[i]+=absint(ncoeff[i][active-1]);}active--;
  }
  for(let i=0;i<n;i++){
    qcoeff[i].length=active;ncoeff[i].length=active;Merr[i]+=mdrop[i];Nerr[i]+=ndrop[i];
    Mnorm[i]-=mdrop[i];Nnorm[i]-=ndrop[i];
  }
  // Small-scale directed operations (U=10^30). Intervals [center +/- radius]
  // for exact scalar sums; no cancellation is discarded in their contraction.
  const IU=(p,d=1n)=>[fl(p*U,d),ce(p*U,d)],AU=(x,y)=>[x[0]+y[0],x[1]+y[1]];
  const NU=x=>[-x[1],-x[0]],SU=(x,y)=>AU(x,NU(y));
  const MU=(x,y)=>{const t=x.flatMap(a=>y.map(b=>a*b));return [fl(min(t),U),ce(max(t),U)]};
  const RU=(x,p,d=1n)=>p<0n?NU(RU(x,-p,d)):[fl(x[0]*p,d),ce(x[1]*p,d)];
  const cU=x=>fl((x[0]+x[1])*U,2n*S),eU=(x,c)=>max([c-fl(x[0]*U,S),ce(x[1]*U,S)-c]);
  const fromS=x=>[floorU(x[0]),ceilU(x[1])];
  const al2=mul(alpha,alpha),lambda=fromS(div(I(2n),alpha)),a0=fromS(div(I(1n),rat(al2,2n,1n)));
  if(lambda[1]*3n>=8n*U||a0[1]>=U)throw Error("asymptotic constants");
  // Exact literal bank and norm-controlled trig centers through 8K.
  const last=8*K,ds=Array(last).fill(0n);let be=0n,osc=0n;
  for(const [nn,prime] of bank){
    const l=log(BigInt(nn)),sq=isqrt(BigInt(nn)*S*S),aa=div(log(BigInt(prime)),[sq,sq+1n]),[si,co]=trig(mul(alpha,l));
    if(si[0]<=0n||aa[0]<=0n||aa[1]>=S)throw Error("bank angle");
    const av=cU(aa),as=eU(aa,av),sv=cU(si),cv=cU(co),E=max([eU(si,sv),eU(co,cv)]);
    if(BigInt(last)*(4n*E+2n)>=U)throw Error("rotation guard");
    let x=0n,y=U;
    for(let j=0;j<last;j++){
      if(j>=K&&j%2===par)ds[j]+=fl(av*x,U);
      [x,y]=[fl(x*cv+y*sv,U),fl(y*cv-x*sv,U)];
    }
    be+=BigInt(last)*(4n*E+2n)+as+1n;
    osc+=ceilU(div(aa,[si[0],si[0]])[1]);
  }
  if(osc>1000n*U||be>U/10n**15n)throw Error("oscillation audit");
  // Bands: [K,2K), [2K,4K), [4K,8K), [8K,infinity).
  // S_qm=sum v^q T_m(2v^2-1), O_3m=sum b_j v^3 T_m.
  const bands=[];
  for(let b=0;b<3;b++){
    const L=K*(1<<b),R=L*2,c3=Array(active).fill(0n),c4=Array(active).fill(0n),o3=Array(active).fill(0n);
    let count=0;
    for(let j=L+par;j<R;j+=2){
      const jj=BigInt(j),kk=BigInt(K),tc=fl((2n*kk*kk-jj*jj)*U,jj*jj),v3=fl(kk**3n*U,jj**3n),v4=fl(kk**4n*U,jj**4n);
      let prev=0n,cur=U;const b0=ds[j];
      if(absint(b0)>14n*U)throw Error("prime sine center");
      for(let m=0;m<active;m++){
        if(absint(cur)>2n*U)throw Error("Cheb recurrence center");
        const f3=fl(v3*cur,U),f4=fl(v4*cur,U);
        c3[m]+=f3;c4[m]+=f4;o3[m]+=fl(b0*f3,U);
        const next=m===0?tc:fl(2n*tc*cur,U)-prev;prev=cur;cur=next;
      }
      count++;
    }
    const r3=[],r4=[],ro=[];
    for(let m=0;m<active;m++){
      const ef=4n*BigInt(m)**2n+4n;
      r3.push(BigInt(count)*ef);r4.push(BigInt(count)*ef);
      ro.push(BigInt(count)*(14n*ef+2n*be+1n));
    }
    bands.push({b,L,R,count,c3,c4,o3,r3,r4,ro});
  }
  // Infinite final band: exact polynomial integral + bounded variation.
  // T_m(2v^2-1) polynomials in v^2, at endpoint v=1/8.
  let prev=[],poly=[1n];
  const c3=[],c4=[],o3=[],r3=[],r4=[],ro=[],khalf=BigInt(K/2);
  function integ(poly,q){
    let lo=0n,hi=0n;
    for(let s=0;s<poly.length;s++){
      const p=BigInt(q-1+2*s),den=p*8n**p,num=poly[s]*U*khalf;
      lo+=fl(num,den);hi+=ce(num,den);
    }
    return [lo,hi];
  }
  for(let m=0;m<active;m++){
    const i3=integ(poly,3),i4=integ(poly,4),c=fl(i3[0]+i3[1],2n),d=fl(i4[0]+i4[1],2n);
    c3.push(c);c4.push(d);o3.push(0n);
    // Integral comparison error <= total variation (even start; odd also <=2 variation).
    const v=1n+2n*BigInt(m);
    r3.push(max([c-i3[0],i3[1]-c])+ce(2n*v*U,8n**3n));
    r4.push(max([d-i4[0],i4[1]-d])+ce(2n*v*U,8n**4n));
    ro.push(ce(osc*(2n+2n*BigInt(m)),8n**3n));
    const next=Array(poly.length+1).fill(0n);
    if(m===0){next[0]=-1n;next[1]=2n;}else{
      for(let s=0;s<poly.length;s++){next[s]-=2n*poly[s];next[s+1]+=4n*poly[s];}
      for(let s=0;s<prev.length;s++)next[s]-=prev[s];
    }
    prev=poly;poly=next;
  }
  bands.push({b:3,L:8*K,R:null,count:null,c3,c4,o3,r3,r4,ro});
  function contract(coeff,c,r){let mid=0n,er=0n;for(let m=0;m<active;m++){mid+=coeff[m]*c[m];er+=absint(coeff[m])*r[m];}
    return [fl(mid-er,U),ce(mid+er,U)];
  }
  // h_b(j)=v^2/32 on band b, zero elsewhere. In unnormalized cosine coefficients.
  // Q(h) <= sum (80/v)|h_j|^2, so the four-band upper Gram D is diagonal.
  const db=[],yc=Array.from({length:n},()=>[]),ye=Array.from({length:n},()=>[]),bandInfo=[];
  for(const band of bands){
    const {b,L,R,c3,c4,o3,r3,r4,ro}=band,den=1n<<BigInt(b),end=R===null?0n:1n;
    // upper sum v^q via decreasing integral + initial term.
    function sumUp(q){
      const p=BigInt(q-1),dp=den**p,ep=R===null?1n:2n**p;
      const z=R===null?IU(BigInt(K),2n*p*dp):IU(BigInt(K)*(ep-1n),2n*p*dp*ep);
      return z[1]+ce(U,den**BigInt(q));
    }
    const d=ce(80n*sumUp(3),1024n);db.push(d);
    const e3=sumUp(3),e4=sumUp(4),errA=ce(16n*U,BigInt(L))+ce(U,1000n);
    let maxY=0n,maxEr=0n;
    for(let i=0;i<n;i++){
      const m3=contract(qcoeff[i],c3,r3),m4=contract(qcoeff[i],c4,r4),mo=contract(qcoeff[i],o3,ro),n4=contract(ncoeff[i],c4,r4);
      const z1=RU(AU(RU(m3,2n),MU(lambda,mo)),1n,32n*BigInt(K));
      const z2=RU(SU(MU(a0,m4),n4),1n,32n*BigInt(K)**2n);
      const y=AU(z1,z2),center=fl(y[0]+y[1],2n);
      // Polynomial model errors and high A'_j asymptotic error.
      const e=ce(37n*Merr[i]*e3,32n*BigInt(K)*U)+ce((Merr[i]+Nerr[i])*e4,32n*BigInt(K)**2n*U)+ce(errA*(Mnorm[i]+Merr[i])*e4,32n*BigInt(K)**2n*U*U);
      const er=max([center-y[0],y[1]-center])+e;
      yc[i].push(center);ye[i].push(er);if(absint(center)>maxY)maxY=absint(center);if(er>maxEr)maxEr=er;
    }
    bandInfo.push({band:b,first:L+par,last_exclusive:R,rows:band.count,energy_upper_scaled:String(d),max_correlation_center_scaled:String(maxY),max_correlation_radius_scaled:String(maxEr)});
  }
  // Exact analytic correction z_i=sum_b (Y_ib/D_b)h_b.
  // Rational candidate uses center yc. Matrix decrement >=
  // .9 Y0 D^-1 Y0^T - 10 * sum_b ||error_b||^2/D_b I.
  // Report direct diagonal/trace bound too, preserving rank-four factors.
  let uniform=0n;
  for(let b=0;b<4;b++)uniform+=ce(10n*ye.reduce((s,x)=>s+x[b]**2n,0n),db[b]);
  let traceLo=0n,traceHi=0n,maxLo=0n,maxIndex=-1,negUpper=0;
  const tailRows=[];
  for(let i=0;i<n;i++){
    let lo=0n,hi=0n,centerGain=0n;
    for(let b=0;b<4;b++){
      const y=yc[i][b],e=ye[i][b],d=db[b];
      lo+=fl(y*y-2n*absint(y)*e,d);hi+=ce(y*y+2n*absint(y)*e,d);centerGain+=fl(y*y,d);
    }
    traceLo+=lo;traceHi+=hi;if(lo>maxLo){maxLo=lo;maxIndex=i;}
    const oldUpper=ce((F1[i][i]+F1r[i][i])*U,T3);if(oldUpper-lo<0n)negUpper++;
    tailRows.push({row:i,mode:nodes[order[h+i]].j,correlation_centers:yc[i].map(String),correlation_radii:ye[i].map(String),rational_gain_lower_scaled:String(lo),rational_gain_upper_scaled:String(hi),center_gain_scaled:String(centerGain),corrected_trial_upper_before_tail_scaled:String(oldUpper),M_polynomial_abs_sum_scaled:String(Mnorm[i]),N_polynomial_abs_sum_scaled:String(Nnorm[i]),M_model_error_scaled:String(Merr[i]),N_model_error_scaled:String(Nerr[i])});
  }
  return {par,J,P,retained:n,initial_trial_high:h,corrected_trial_high:hh,tail_start:K,terms,active,scale:String(U),prefix_scale:String(T),old_prefix_trace_lower_scaled_squared:String(pre),corrected_prefix_trace_upper_scaled_fourth:String(newPre),corrected_trial_error_row_scaled_cubed:String(ferr),bands:bandInfo,prime_sine_center_radius_scaled:String(be),prime_oscillation_bound_scaled:String(osc),max_M_model_error_before_drop_scaled:String(maxMerr),max_N_model_error_before_drop_scaled:String(maxNerr),max_M_abs_sum_before_drop_scaled:String(maxMnorm),max_N_abs_sum_before_drop_scaled:String(maxNnorm),rank4_uniform_loss_scaled:String(uniform),rational_gain_trace_lower_scaled:String(traceLo),rational_gain_trace_upper_scaled:String(traceHi),max_rational_gain_lower_scaled:String(maxLo),max_gain_row:maxIndex,negative_trial_upper_count:negUpper,tail_rows:tailRows,classification:"correlated analytic infinite-tail trial correction; not full Schur sign"};
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
