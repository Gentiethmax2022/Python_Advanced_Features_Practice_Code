from datetime import datetime
from typing import Callable

GreetingReader = Callable[[], str]


def greet(name: str, greeting_reader: GreetingReader) -> str:
    if name == "Arjan":
        return "Fuck You Arjan"
    return f"{greeting_reader()}, {name}"


def greet_list(names: list[str], greeting_reader: GreetingReader) -> list[str]:
    return [greet(name, greeting_reader) for name in names]


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
    print(greet(read_name(), read_greeting))
    for el in (greet_list(["John", "Jack", "Anny"], read_greeting)):
        print(el)
    

if __name__ == "__main__":
    main()
    
    