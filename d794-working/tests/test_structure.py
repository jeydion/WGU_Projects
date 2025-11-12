"""Test D794 assignment structure and requirements."""
import pytest
from pathlib import Path


class TestD794Structure:
    """Verify D794 assignment files exist."""
    
    def test_outline_document_exists(self):
        """Check that PA1 outline exists."""
        assert Path('PA1_Outline.docx').exists(), \
            "PA1_Outline.docx not found"
    
    def test_outline_is_not_empty(self):
        """Verify outline document has content."""
        outline_path = Path('PA1_Outline.docx')
        if outline_path.exists():
            size = outline_path.stat().st_size
            assert size > 1000, \
                f"Outline seems too small ({size} bytes). Add more content?"


class TestD794Content:
    """Validate content requirements."""
    
    def test_outline_readable(self):
        """Ensure outline file is accessible."""
        outline_path = Path('PA1_Outline.docx')
        if outline_path.exists():
            # Basic check - can we read the file?
            try:
                with open(outline_path, 'rb') as f:
                    header = f.read(8)
                    # DOCX files start with PK (zip format)
                    assert header[:2] == b'PK', \
                        "File doesn't appear to be a valid DOCX"
            except Exception as e:
                pytest.fail(f"Cannot read outline file: {e}")
