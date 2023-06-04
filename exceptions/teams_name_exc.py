

class SameTeamsNameException(Exception):
    """
    Raised when the input same teams name

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Names of away and home teams cannot be the same"):
        self.message = message
        super().__init__(self.message)