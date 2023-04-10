""" Basic example showing how to create objects from data using a dynamic factory
      with register/unregister methods """
      
      
import json 
from dataclasses import dataclass
from game import factory, loader


@dataclass
class Sorcerer:
    
    name: str
    
    def make_a_noise(self) -> None:
        print("Arrrrggggooooonnnnn")
        
        
@dataclass
class Wizard:
    
    name: str 
    
    def make_a_noise(self) -> None:
        print("Boooaaaahhhhh")
        

@dataclass
class Witcher:
    
    name: str 
    
    def make_a_noise(self) -> None:
        print("I am wiitchy wiitchy")
        
        
def main() -> None:
    """ Create Game Characters from a file containing a level definition """
    
    # register a couple of character types 
    factory.register("sorcerer", Sorcerer)
    factory.register("wizard", Wizard)
    factory.register("witcher", Witcher)
    
    # read data from a json file 
    with open("C:\\Users\\genti\\OneDrive\\Desktop\\ArjanCodes\\Plugin_Architecture\\after\\level.json") as j_file:
        data = json.load(j_file)
        
        # load the plugins 
        loader.load_plugins(data["plugins"])
        
        # create the characters 
        characters = [factory.create(item) for item in data["characters"]]
        
        # do sth with the characters 
        for character in characters:
            character.make_a_noise()
            

if __name__ == "__main__":
    main()
    
    
    