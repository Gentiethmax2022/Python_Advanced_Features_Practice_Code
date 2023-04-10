from datetime import datetime
from functools import partial
from typing import Callable


GreetingReader = Callable[[], str]
GreetingFunction = Callable[[str], str]


def greet(name: str, greeting_reader: GreetingReader) -> str:
    if name == "Arjan":
        return "Fuck you Arjan"
    return f"{greeting_reader()}, {name}"


def greet_list(names: list[str], greet_fn: GreetingFunction) -> list[str]:
    return [greet_fn(name) for name in names]


def read_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good Morning"
    elif 12 <= current_time.hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"
    

def read_name() -> str:
    return input("Please enter your name: ")


def main() -> None:
    greet_function = partial(greet, greeting_reader=read_greeting)
    print(greet_function(read_name()))
    print("\n".join(greet_list(["John", "Jack", "Anny"], greet_function)))
    

if __name__ == "__main__":
    main()
    
    