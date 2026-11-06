class AfroPinError(Exception):
    """
    A request the API refused, or one that couldn't be made. Branch on code (for example pin_balance_low or
    duplicate_external_reference); the message is for people and may change. fields has per-field messages for input
    problems. status is the HTTP status, or 0 when the API wasn't reached.
    """

    def __init__(self, code, message, fields=None, status=0):
        super().__init__(message)
        self.code = code
        self.message = message
        self.fields = fields
        self.status = status
