# EXCEPTIONS

class XYValueError(Exception):
    """ Custom error that is raised when x and y value is more than 100 """
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)