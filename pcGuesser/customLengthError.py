class Error(Exception):
   """Base class for other exceptions"""
   pass

class LengthTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class LengthTooLargeError(Error):
   """Raised when the input value is too large"""
   pass
