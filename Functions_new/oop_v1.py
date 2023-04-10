from datetime import datetime

class Greeting:
    
    def __init__(self) -> None:
        current_time = datetime.now()
        if current_time.hour < 12:
            self.greeting_intro = "Good Morning"
        elif 12 <= current_time.hour < 18:
            self.greeting_intro = "Good Afternoon"
        else:
            self.greeting_intro = "Good Evening"
        
    def greet(self, name: str) -> None:
        print(f"{self.greeting_intro}, {name}")
        
        
    def greet_list(self, names: list[str]) -> None:
        for name in names:
            self.greet(name)
            

def main() -> None:
    name = input("Pleas enter your name: ")
    
    greeting = Greeting()
    greeting.greet(name)
    

if __name__ == "__main__":
    main()