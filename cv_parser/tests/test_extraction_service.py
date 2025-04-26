import pytest
from services.extraction_service import ExtractionService
from exceptions import UnsupportedFileTypeError

def test_extract_valid_pdf():
    service = ExtractionService()
    text = service.extract('tests/data/sample_resume.pdf')
    assert len(text) > 0

def test_extract_invalid_file_type():
    service = ExtractionService()
    with pytest.raises(UnsupportedFileTypeError):
        service.extract('tests/data/sample_resume.txt')