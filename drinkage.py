###
### Great video on explaining this.


import time
from typing import Literal
from datetime import datetime, timedelta

def timer_decorator(base_function):
    """
    # Timer decorator is an example on how to create a decorator in python
    :param base_function:
    :return: Timer function to tally up the time it takes to execute a function.
    """
    def enhanced_function(*args, **kwargs):
        start_time = time.time()
        result = base_function(*args, **kwargs)
        end_time = time.time()
        print(f"Task time: {end_time - start_time} seconds")
        return result
    return enhanced_function

@timer_decorator
def brew_tea(tea_type: str, steep_time: int) -> None:
    """
    # Brewing Tea: Example of using Type Hinting
    :param tea_type: Type of tea
    :param steep_time: time it takes to steep the tea
    :return: None
    """
    print(f'\nBrewing {tea_type} Tea...')
    time.sleep(steep_time)
    print("Tea is ready!")

@timer_decorator
def brew_coffee(mode: Literal["light", "dark", "regular"]) -> None:
    print(f"\nBrewing {mode} Coffee...")
    time.sleep(2)
    print("Coffee is ready!")


@timer_decorator
def brew_matcha() -> None:
    print('\nBrewing Matcha...')
    time.sleep(2)
    print("Matcha is ready!")
    return f"Drink Matcha by {datetime.now() + timedelta(minutes=30)}"

def calculate_length(text: str) -> int:
    """
    # Shown an Example of SUPER strinct Validation in Python
    :param text:
    :return:
    """
    if not isinstance(text, str):
        raise TypeError("The text argument must be a string!")
    return len(text)


if __name__ == '__main__':
    print(brew_matcha())
    brew_tea("light", 1)
    brew_coffee("regular")
