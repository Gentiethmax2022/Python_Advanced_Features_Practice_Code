""" Factory for creating a game character """

from typing import Any, Callable
from game.character import GameCharacter

character_creation_functions: dict[str, Callable[..., GameCharacter]] = {}


def register(character_type: str, creator_function: Callable[..., GameCharacter]) -> None:
    """ Register a new game character type """
    character_creation_functions[character_type] = creator_function
    

def unregister(character_type: str) -> None:
    """ Unregister a game character type """
    character_creation_functions.pop(character_type, None)
    

def create(arguments: dict[str, Any]) -> GameCharacter:
    """ Create a game character of a specific type, given json data """
    args_copy = arguments.copy()
    character_type = args_copy.pop("type")
    try:
        creator_function = character_creation_functions[character_type]
    except KeyError:
        raise ValueError(f"Unknown character type {character_type!r}")
    
    return creator_function(**args_copy)



    
    
    