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
    
    def payout_holiday(self) -> None:
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise ValueError(f"You don't have enough holidays left for a payout.\
                                Remaining holidays: {self.vacation_days}")
            
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Vacation days lef: {self.vacation_days}")
        
        
    def take_holiday(self, nr_days: int = 1) -> None:
        if self.vacation_days < nr_days:
            raise ValueError("You don't have that much holiday days left")
        self.vacation_days -= nr_days
        print("Have fun on your holidays. Don't forget to check your email")
        

def main() -> None:
    employee = Employee("Aleks Burgaj", role=Role.MANAGER)
    employee.payout_holiday()
    
if __name__ == "__main__":
    main()
    
    