"""Test file structure and basic requirements."""
import os
import pytest
from pathlib import Path


class TestFileStructure:
    """Verify required files exist."""
    
    def test_required_python_files_exist(self):
        """Check that main Python files are present."""
        required_files = [
            'python/main.py',
            'python/weather.py',
        ]
        
        for file in required_files:
            assert Path(file).exists(), f"Missing required file: {file}"
    
    def test_required_fortran_files_exist(self):
        """Check that original Fortran files are present."""
        required_files = [
            'fortran/main.f90',
            'fortran/weather.f90',
        ]
        
        for file in required_files:
            assert Path(file).exists(), f"Missing required file: {file}"
    
    def test_documentation_exists(self):
        """Check that documentation files exist."""
        doc_files = [
            'docs/PA_Task1.docx',
            'docs/PA_Task2.docx',
        ]
        
        for file in doc_files:
            assert Path(file).exists(), f"Missing documentation: {file}"


class TestCodeQuality:
    """Verify code quality standards."""
    
    def test_python_files_have_docstrings(self):
        """Ensure Python modules have docstrings."""
        python_files = ['python/main.py', 'python/weather.py']
        
        for file in python_files:
            with open(file, 'r') as f:
                content = f.read()
                assert '"""' in content or "'''" in content, \
                    f"{file} missing module docstring"
    
    def test_python_files_parse_correctly(self):
        """Verify Python files have valid syntax."""
        import ast
        python_files = ['python/main.py', 'python/weather.py']
        
        for file in python_files:
            with open(file, 'r') as f:
                try:
                    ast.parse(f.read())
                except SyntaxError as e:
                    pytest.fail(f"Syntax error in {file}: {e}")
