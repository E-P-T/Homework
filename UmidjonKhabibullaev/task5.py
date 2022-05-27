class CustomException(BaseException):
    def __init__(self) -> None:
        self.error_message = "Some unknown error has occured."
    
    def __str__(self) -> str:
        return f"Error: {self.error_message}"


class NotEvenException(CustomException):
    def __init__(self, *args, **krargs):
        self.error_message = "The provided number is not even"
    

class LessThanThreeException(CustomException):
    def __init__(self) -> None:
        self.error_message = "The provided number is not greater than three"


class NonIntegerException(CustomException):
    def __init__(self) -> None:
        self.error_message = "The provided argument is not an integer"
        


def is_even(number):
    try:
        if not isinstance(number, int):
            raise NonIntegerException

        elif number < 3:
            raise LessThanThreeException

        elif number % 2 != 0:
            raise NotEvenException
        
        try:
            if number > 3 and number % 2 == 0:
                true_flag = True
        except:
            raise CustomException
    
    except (CustomException, NonIntegerException, NotEvenException, NotEvenException) as exc:
        print(exc)
        return False
    
    else:
        return true_flag


if __name__ == "__main__":
    print(is_even(1))