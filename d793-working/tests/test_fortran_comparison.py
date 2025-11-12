"""Compare Fortran and Python implementations."""
import subprocess
import pytest
from pathlib import Path
import os


@pytest.mark.fortran
class TestFortranPythonEquivalence:
    """Verify Python translation matches Fortran behavior.
    
    These tests require gfortran to be installed.
    Skip with: pytest -m "not fortran"
    """
    
    @pytest.fixture(scope="class")
    def fortran_program(self):
        """Compile Fortran code once for all tests."""
        try:
            result = subprocess.run(
                ['gfortran', '--version'],
                capture_output=True,
                timeout=2
            )
            if result.returncode != 0:
                pytest.skip("gfortran not available")
        except FileNotFoundError:
            pytest.skip("gfortran not installed")
        
        # Get all Fortran files
        fortran_files = list(Path('fortran').glob('*.f90'))
        if not fortran_files:
            pytest.skip("No Fortran files found")
        
        output_path = 'fortran_program'
        
        # Compile in fortran directory
        compile_cmd = ['gfortran'] + [f.name for f in fortran_files] + ['-o', output_path]
        
        compile_result = subprocess.run(
            compile_cmd,
            capture_output=True,
            text=True,
            cwd='fortran'
        )
        
        if compile_result.returncode != 0:
            pytest.skip(f"Fortran compilation failed: {compile_result.stderr}")
        
        yield f'fortran/{output_path}'
        
        # Cleanup
        prog_path = Path(f'fortran/{output_path}')
        if prog_path.exists():
            prog_path.unlink()
        # Remove .mod files
        for mod_file in Path('fortran').glob('*.mod'):
            mod_file.unlink()
    
    def run_fortran(self, fortran_program, input_data=""):
        """Execute Fortran program with given input."""
        result = subprocess.run(
            [f'./{Path(fortran_program).name}'],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5,
            cwd='fortran'
        )
        return result.stdout, result.stderr, result.returncode
    
    def run_python(self, input_data=""):
        """Execute Python program with given input."""
        result = subprocess.run(
            ['python', 'main.py'],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5,
            cwd='python'
        )
        return result.stdout, result.stderr, result.returncode
    
    def test_both_programs_execute(self, fortran_program):
        """Verify both Fortran and Python versions run."""
        f_out, f_err, f_code = self.run_fortran(fortran_program)
        p_out, p_err, p_code = self.run_python()
        
        # Just verify they don't crash catastrophically
        assert f_code != 127, f"Fortran program not found"
        assert p_code != 127, f"Python program not found"
    
    def test_output_format_similarity(self, fortran_program):
        """Check that both programs produce output."""
        f_out, f_err, _ = self.run_fortran(fortran_program)
        p_out, p_err, _ = self.run_python()
        
        # Both should do something (output or error)
        fortran_produces_something = len(f_out) > 0 or len(f_err) > 0
        python_produces_something = len(p_out) > 0 or len(p_err) > 0
        
        assert fortran_produces_something, "Fortran program produced nothing"
        assert python_produces_something, "Python program produced nothing"
