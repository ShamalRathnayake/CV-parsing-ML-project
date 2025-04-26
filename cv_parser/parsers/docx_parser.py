from docx import Document
from .base_parser import BaseParser

class DocxParser(BaseParser):

    def extract_text(self, file_path: str) -> str:
        document = Document(file_path)
        return "\n".join([para.text for para in document.paragraphs])