from dataclasses import dataclass
from enum import StrEnum, auto

FIXED_VACATION_DAYS_PAYOUT = 5


class Role(StrEnum):
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    ENGINEER = auto()
    INTERN = auto()
    

@dataclass
class Employee:
    name: str
    role: Role
    vacation_days: int = 25
    
    def take_a_holiday(self, payout: bool, nr_days: int = 1) -> None:
        if payout:
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(
                    """ You don't have  enough holidays left over to be considered
                        for a payout. """)
            self.vacation_days -= nr_days
            print("Happy Holiday. They we will be paid according to the company's policy")
            print(f"The total Holiday days you got left is : {self.vacation_days} days")
            
        else:
            if self.vacation_days < nr_days:
                raise ValueError("You don't have any holidays left")
            self.vacation_days -= nr_days
            print("Have fun on your holidays. Don't forget to check your emails")
            

def main() -> None:
    employee = Employee("Aleks Burgaj", Role.MANAGER)
    employee.take_a_holiday(False, 23)
    
    
if __name__ == "__main__":
    main()
    
    