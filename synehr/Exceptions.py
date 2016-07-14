class SizeValueError(Exception):
    def __init__(self):
        Exception.__init__(self,"Size  value out of range. Please choose between 100 and 1 million.")

class GenderValueError(Exception):
    def __init__(self):
        Exception.__init__(self,"Gender value out of range. Please use percentage between 0% and 100% or select None")
