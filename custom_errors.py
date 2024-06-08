class InvalidActionError(Exception):
    """Exception raised for invalid actions in the Tic-Tac-Toe game."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
