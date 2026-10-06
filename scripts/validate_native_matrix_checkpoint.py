"""Independent raw row-codec controls; synthetic fixtures are never native certificates."""
import gzip,json,tempfile
from pathlib import Path
from certify_native_legendre_small_window import F,I,certificate as native
from certify_native_matrix_checkpoint import save,load

def certificate():
    old=I.grid;I.grid=10**400
    try:
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'control.gz';bindings={'aperture':'23/25','order':240,'control_only':True}
            matrix=[[I(0) for _ in range(84)] for _ in range(84)]
            for j in range(0,84,2):
                matrix[0][j]=matrix[j][0]=I(F(j+1,7),F(j+2,7))
            save(path,bindings,1,matrix);original=path.read_bytes();n,recovered=load(path,bindings)
            assert n==1 and all((matrix[i][j].lo,matrix[i][j].hi)==(recovered[i][j].lo,recovered[i][j].hi) for i in range(84) for j in range(84))
            controls=0
            try:load(path,{**bindings,'aperture':'91/100'})
            except ValueError:controls+=1
            else:raise AssertionError('Stale aperture accepted')
            data=json.loads(gzip.decompress(original))
            mutations=[lambda d:d.update(grid_digits=80),lambda d:d.update(completed_rows=85),
                       lambda d:d['lower_triangle'].__setitem__(1,['1','1']),
                       lambda d:d['lower_triangle'].__setitem__(2,['1','1']),
                       lambda d:d['lower_triangle'].__setitem__(0,['2','1']),
                       lambda d:d['lower_triangle'].pop()]
            for mutation in mutations:
                d=json.loads(gzip.decompress(original));mutation(d)
                path.write_bytes(gzip.compress(json.dumps(d).encode(),mtime=0))
                try:load(path,bindings)
                except ValueError:controls+=1
                else:raise AssertionError('Invalid native checkpoint accepted')
            path.write_bytes(original)
            try:native(F(91,100),return_matrix=True,degree=83,matrix_resume=(1,matrix))
            except ValueError:controls+=1
            else:raise AssertionError('Historical native recovery mode accepted')
            return dict(exact_fixed_grid_endpoints_preserved=7056,codec_controls_rejected=controls,
                        synthetic_fixture_only=True,actual_native_checkpoint_certified=False,
                        whole_domain_positivity=False,f4_entry_closed=False)
    finally:I.grid=old

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
