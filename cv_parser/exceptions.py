class CVParserError(Exception):
    """Base class for CV parser exceptions."""
    pass

class UnsupportedFileTypeError(CVParserError):
    """Raised when the file type is not supported."""
    def __init__(self, file_extension):
        super().__init__(f"Unsupported file type: {file_extension}")