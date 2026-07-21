from types import ModuleType


def error_message_detail(error, error_detail: ModuleType):
    """
    Returns a detailed error message including file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error occurred in Python script [{file_name}] "
        f"at line [{line_number}] : {str(error)}"
    )


class CustomException(Exception):
    """
    Custom exception class for the project.
    """

    def __init__(self, error_message, error_detail: ModuleType):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
