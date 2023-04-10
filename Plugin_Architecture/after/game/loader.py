""" A simple plug-in loader """

import importlib

class ModuleInterface:
    """ Represents a plug-in Interface. A plug-in has a single register function """
    
    @staticmethod
    def register() -> None:
        """ Register the necessary items in the game character factory """
        

def import_module(name: str) -> ModuleInterface:
    """ Imports a module given a name """
    return importlib.import_module(name)  # type: ignore 


def load_plugins(plugins: list[str]) -> None:
    """ Loads the plug-ins defined in the plugins list """
    for plugin_file in plugins:
        plugin = import_module(plugin_file)
        plugin.register()
        
        