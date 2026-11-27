// Exact BigInt replay of the frozen AM row envelope. Run from repo root: node research/iv238_am_ground_state.mjs
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
function replay(d) {
  if(d.M!==16384||d.W!==1000000000||d.h.length!==d.M||d.shifts.length!==48||!d.h.every(x=>Number.isSafeInteger(x)&&x>0)||!d.shifts.every(([j,u])=>Number.isSafeInteger(j)&&Number.isSafeInteger(u)&&u>0))throw Error("input");
  for(let k=0;k<48;k+=2){let [j,u]=d.shifts[k],[m,v]=d.shifts[k+1];if(j<0||m!==-j-1||u!==v)throw Error("signed pair");}
  const h=d.h.map(BigInt),W=BigInt(d.W),N=7979648n,D=1000000n;
  const get=i=>i<0||i>=h.length?0n:h[i];
  const gcd=(a,b)=>b?gcd(b,a%b):a;
  const lt=(a,b)=>a.n*b.d<b.n*a.d;
  const fmt=x=>{const g=gcd(x.n,x.d);return {numerator:String(x.n/g),denominator:String(x.d/g),cell:x.i}};
  let min=null,max=null,peak=null,slack=null,slackIndex=-1,minH=h[0],maxH=h[0],bands=Array(16).fill(null);
  for(let i=0;i<h.length;i++){
    if(h[i]<minH)minH=h[i];if(h[i]>maxH)maxH=h[i];
    let R=0n;
    for(const [j,u] of d.shifts){const x=get(i+j),y=get(i+j+1);R+=BigInt(u)*(x>y?x:y);}
    const den=W*h[i],z=N*den-D*R;
    if(z<=0n)throw Error("nonpositive row slack "+i);
    const q={n:z,d:D*den,i},r={n:R,d:den,i},k=Math.floor(i/1024);
    if(!min||lt(q,min))min=q;if(!max||lt(max,q))max=q;
    if(!peak||lt(peak,r))peak=r;
    if(slack===null||z<slack){slack=z;slackIndex=i;}
    if(!bands[k]||lt(q,bands[k]))bands[k]=q;
  }
  return {M:d.M,shift_count:d.shifts.length,minimum_weight:String(minH),maximum_weight:String(maxH),minimum_integer_slack:String(slack),minimum_integer_slack_cell:slackIndex,maximum_row_ratio:fmt(peak),minimum_envelope_residual:fmt(min),maximum_envelope_residual:fmt(max),band_minima:bands.map((v,k)=>({start_cell:1024*k,end_cell_exclusive:1024*(k+1),...fmt(v)}))};
}
const bytes=readFileSync(process.argv[2] || 'custody/iv146-am/am_cells.json');
if(createHash('sha256').update(bytes).digest('hex')!=='2b149c79f469b594ce7c308e44c278da00e9e41fbd9da1436cad0b0dca9d294a')throw Error('frozen input digest');
console.log(JSON.stringify(replay(JSON.parse(bytes.toString('utf8'))),null,2));
