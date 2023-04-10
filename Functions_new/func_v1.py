from datetime import datetime

def greet(name: str, greeting_intro: str) -> str:
    return f"{greeting_intro}, {name}"


def greet_list(names: list[str], greeting_intro: str) -> list[str]:   #type: ignore
    return [greet(name, greeting_intro) for name in names]
      

def reed_greeting() -> str:
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
    print(greet(read_name(), reed_greeting()))
    print(greet_list(["John", "Jack", "Anny"], reed_greeting()))
    
    
if __name__ == "__main__":
    main()
    
