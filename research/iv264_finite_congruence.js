function audit(meta,rows){
const n=meta.n,S=BigInt(meta.Fscale),abs=x=>x<0n?-x:x,fl=(x,y)=>x>=0n?x/y:-((-x+y-1n)/y),ce=(x,y)=>-fl(-x,y);
function isqrt(x){if(x<0n)throw Error("sqrt");if(x<2n)return x;let a=1n<<BigInt(Math.ceil(x.toString(2).length/2));while(true){let b=(a+x/a)/2n;if(b>=a)return a;a=b}}
const F=rows.map(r=>r.F.map(BigInt)),E=rows.map(r=>r.Fr.map(BigInt)),A=F.map(r=>r.slice()),L=Array.from({length:n},()=>Array(n).fill(0n)),ord=Array.from({length:n},(_,i)=>i),piv=[];
for(let i=0;i<n;i++){let k=i;for(let j=i+1;j<n;j++)if(A[j][j]>A[k][k])k=j;
if(k!==i){[A[i],A[k]]=[A[k],A[i]];for(const r of A)[r[i],r[k]]=[r[k],r[i]];[L[i],L[k]]=[L[k],L[i]];[ord[i],ord[k]]=[ord[k],ord[i]]}
const d=A[i][i];piv.push(d);if(d<=0n)return {certified:false,stage:"center pivot",index:i,pivot:String(d),pivots:piv.map(String)};
L[i][i]=S;for(let j=i+1;j<n;j++)L[j][i]=fl(A[j][i]*S,d);
for(let j=i+1;j<n;j++)for(let k=j;k<n;k++){const z=A[k][j]-fl(L[k][i]*A[j][i],S);A[k][j]=A[j][k]=z}}
const W=[];for(let i=0;i<n;i++){const u=Array(n).fill(0n);u[i]=S;for(let j=i-1;j>=0;j--){let z=0n;for(let k=j+1;k<=i;k++)z+=u[k]*L[k][j];u[j]=-fl(z,S)}const a=isqrt(S**3n/piv[i]);const r=Array(n).fill(0n);for(let j=0;j<=i;j++)r[ord[j]]=fl(u[j]*a,S);if(r[ord[i]]<=0n)throw Error("invertible");W.push(r)}
const dot=(a,b)=>a.reduce((z,x,i)=>z+x*b[i],0n);
const Fc=F[0].map((_,j)=>F.map(r=>r[j])),Ec=E[0].map((_,j)=>E.map(r=>r[j]));
const WF=W.map(r=>Fc.map(c=>dot(r,c))),Wa=W.map(r=>r.map(abs)),WE=Wa.map(r=>Ec.map(c=>dot(r,c)));
let glo=null,cmin=null,radmax=0n;const details=[];
for(let i=0;i<n;i++){let g=0n,cg=0n,rr=0n;for(let j=0;j<n;j++){let m=dot(WF[i],W[j]),e=dot(WE[i],Wa[j]);rr+=e;cg+=i===j?m:-abs(m);g+=i===j?m-e:-abs(m)-e}if(glo===null||g<glo)glo=g;if(cmin===null||cg<cmin)cmin=cg;if(rr>radmax)radmax=rr;details.push({i,original_row:ord[i],pivot:String(piv[i]),row_lower:String(g),center_row_lower:String(cg),radius_row:String(rr)})}
return {certified:glo>0n,scale:String(S**3n),min_row:String(glo),min_center_row:String(cmin),max_radius_row:String(radmax),min_pivot:String(piv[n-1]),pivot_scale:String(S),details,basis_scale:String(S),basis:W.map(r=>r.map(String))};
}
