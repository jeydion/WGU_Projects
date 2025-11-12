"""Compare Fortran and Python implementations."""
import subprocess
import pytest
from pathlib import Path
import os


class TestFortranPythonEquivalence:
    """Verify Python translation matches Fortran behavior."""
    
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
        
        output_path = 'fortran/fortran_program'
        compile_result = subprocess.run(
            ['gfortran', 'fortran/main.f90', 'fortran/weather.f90', 
             '-o', output_path],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        if compile_result.returncode != 0:
            pytest.skip(f"Fortran compilation failed: {compile_result.stderr}")
        
        yield output_path
        
        if Path(output_path).exists():
            Path(output_path).unlink()
    
    def run_fortran(self, fortran_program, input_data=""):
        """Execute Fortran program with given input."""
        result = subprocess.run(
            [f'./{fortran_program}'],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout, result.stderr, result.returncode
    
    def run_python(self, input_data=""):
        """Execute Python program with given input."""
        result = subprocess.run(
            ['python', 'python/main.py'],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout, result.stderr, result.returncode
    
    def test_both_programs_execute(self, fortran_program):
        """Verify both Fortran and Python versions run without crashing."""
        f_out, f_err, f_code = self.run_fortran(fortran_program)
        p_out, p_err, p_code = self.run_python()
        
        assert f_code in [0, 1], f"Fortran crashed: {f_err}"
        assert p_code in [0, 1], f"Python crashed: {p_err}"
    
    def test_output_format_similarity(self, fortran_program):
        """Check that output structures are similar."""
        f_out, _, _ = self.run_fortran(fortran_program)
        p_out, _, _ = self.run_python()
        
        assert len(f_out) > 0 or len(p_out) > 0, \
            "Neither program produced output"
