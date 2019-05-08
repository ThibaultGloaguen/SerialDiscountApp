class NoMoreDiscountException(Exception):
    def __init__(self, message):
        super(NoMoreDiscountException, self).__init__(message)
