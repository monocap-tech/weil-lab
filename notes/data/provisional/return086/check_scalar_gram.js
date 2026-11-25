'use strict';
// Usage: node check_scalar_gram.js direct_sums.json
// All JSON integer tokens are parsed losslessly, including the interval endpoints.
const fs=require('fs');
function verify(s) {
 const d=JSON.parse(s.replace(/"(?:\\.|[^"\\])*"|-?\d+/g,m=>m[0]==='"'?m:'"'+m+'"'));
 const bands=d.bands.map(b=>({name:b.name,count:BigInt(b.count),scale:BigInt(b.scale),sums:b.sums.map(row=>row.map(pair=>pair.map(BigInt)))}));
 if(bands.length!==2||bands[0].name!=='full'||bands[1].name!=='restricted'||bands[0].count!==114688n||bands[1].count!==98304n||bands[0].scale!==bands[1].scale||bands[0].scale<=0n)throw Error('unexpected bands');
 for(const [i,b] of bands.entries()){
  if(d.bands[i].p.join(',')!==Array.from({length:45},(_,i)=>String(i+2)).join(',')||b.sums.length!==45||b.sums.some(row=>row.length!==10||row.some(a=>a.length!==2||a[0]>a[1])))throw Error('unexpected scalar data');
 }
 const sub=(a,b)=>[a[0]-b[1],a[1]-b[0]], mul=(a,n)=>n>=0n?[a[0]*n,a[1]*n]:[a[1]*n,a[0]*n];
 bands.push({name:'lower_difference',count:bands[0].count-bands[1].count,scale:bands[0].scale,sums:bands[0].sums.map((row,i)=>row.map((a,j)=>sub(a,bands[1].sums[i][j])))});
 const col=[[0,1,3,4],[1,2,5,6],[3,5,7,8],[4,6,8,9]];
 function gram(b,p,n=4){return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>b.sums[p-2+Math.floor(i/4)+Math.floor(j/4)][col[i%4][j%4]]));}
 // Doubled midpoint minus row-sum radius diagonal is a Loewner lower bound.
 // Bareiss fraction-free elimination tests the leading principal minors exactly.
 function pd(m){let n=m.length;let A=m.map((row,i)=>{let rad=row.reduce((s,a)=>s+a[1]-a[0],0n);return row.map((a,j)=>a[0]+a[1]-(i===j?rad:0n))});let prev=1n;for(let k=0;k<n;k++){let piv=A[k][k];if(piv<=0n)return false;for(let i=k+1;i<n;i++)for(let j=k+1;j<n;j++){let num=A[i][j]*piv-A[i][k]*A[k][j];if(num%prev!==0n)throw Error('nonexact');A[i][j]=num/prev;}prev=piv;}return true;}
 const out=[];
 for(const b of bands){let res={name:b.name,count:String(b.count),gram4:[0,0],hankel8:[0,0],localizing:[0,0],fails:[]};const check=(key,m,desc)=>{let pass=pd(m);res[key][pass?0:1]++;if(!pass)res.fails.push(desc);};for(let p=2;p<=32;p++)check('gram4',gram(b,p),`gram p=${p}`);for(let p=2;p<=30;p++)check('hankel8',gram(b,p,8),`hankel p=${p}`);const [ln,ld,un,ud]=b.name==='full'?[1n,8n,1n,1n]:b.name==='restricted'?[1n,8n,1n,2n]:[1n,2n,1n,1n];for(let p=2;p<=31;p++){let g=gram(b,p),h=gram(b,p+1);check('localizing',h.map((row,i)=>row.map((a,j)=>sub(mul(a,ld),mul(g[i][j],ln)))),`lower p=${p}`);check('localizing',g.map((row,i)=>row.map((a,j)=>sub(mul(a,un),mul(h[i][j],ud)))),`upper p=${p}`);}out.push(res);}
 return out;
}
if(require.main===module){if(process.argv.length!==3)throw Error('usage: node check_scalar_gram.js direct_sums.json');const result=verify(fs.readFileSync(process.argv[2],'utf8'));console.log(JSON.stringify(result,null,2));if(result.some(b=>b.fails.length))process.exitCode=1;}
module.exports={verify};
