class invalidInput(Exception):
    def __str__(self):
        return "Invalid Input"

class positionAlreadyFilled(Exception):
    def __str__(self):
        return "position Already Filled"