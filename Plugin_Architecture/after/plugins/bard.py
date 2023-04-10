""" Game extension that adds a bard character """

from dataclasses import dataclass
from game import factory


@dataclass
class Bard:
    
    name: str
    instrument: str = "flute"
    
    def make_a_noise(self) -> None:
        print(f"I am {self.name} and i play the {self.instrument} instrument. Toss a coin to your witcher")
        

def register() -> None:
    factory.register("bard", Bard)
    
    