
from services.extraction_service import ExtractionService
from parsers.pdf_parser import PDFParser

def main():
    parser = PDFParser()
    service = ExtractionService(parser)

    path = 'cv2.pdf'  # Change this
    candidate_profile = service.extract_candidate_profile(path)

    print(candidate_profile)

if __name__ == "__main__":
    main()