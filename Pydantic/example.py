""" Basic example showing how to read and validate data from a file using 
    Pydantic   """
    
    
import json 
from typing import List, Optional
import pydantic 

class ISBNMissingerror(Exception):
    """ Custom error which is raised when both ISBN10 and ISBN13 are missing """
    
    def __init__(self, title: str, message: str) -> None:
        self.title = title 
        self.message = message
        super().__init__(message)
        

class ISBN10FormatError(Exception):
    """ Custom error that is raised when ISBN10 doesn't have the right format """
    
    def __init__(self, value: str, message: str) -> None:
        self.value = value 
        self.message = message
        super().__init__(message)
        
        
class Author(pydantic.BaseModel):
    name: str
    verified: bool 
    

class Book(pydantic.BaseModel):
    """ Represents a book that you can read from a JSON file """
    
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    author2: Optional[Author]
    
    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn_10_or_13(cls, values):
        """ Make sure there is either an isbn_10 or an isbn_13 defined"""
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingerror(title=values["title"], message="""The document should have either 
                                   an isbn_10 or an isbn_13""")
        return values 
    
    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) -> None:
        """ Validator to check if ISBN10 is valid """
        
        chars = [c for c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 shuld be exactly 10 digits long")
        
        # here we define a helper function in local scope     
        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)
        
        if sum((10 - i) * char_to_int(x) for i, x in enumerate(chars)) % 11 != 0:
            raise ISBN10FormatError(value=value, message="ISBN10 digit sum should be divisible by 11")
        
        return value
    
class Config:
    """ Pydantic config class """
    
    allow_mutation = False
    anystr_lower = True 
    
    
def main() -> None:
    
    # Read data from a json file 
    with open("C:\\Users\\genti\\OneDrive\\Desktop\\ArjanCodes\\Pydantic\\data.json") as j_file:
        data = json.load(j_file)                
        books: list[Book] = [Book(**item) for item in data]
        
        print(books)
        
        
if __name__ == "__main__":
    main()