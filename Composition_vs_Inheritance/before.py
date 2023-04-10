""" Very advanced employee management system """

from dataclasses import dataclass

@dataclass
class HourlyEmployee:
    """ Employees that are paid based on numbers of hour worked """
    
    name: str 
    id: int
    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000
    
    def compute_pay(self) -> float:
        """ Compute how much the employee should be paid """
        return (self.pay_rate * self.hours_worked + self.employer_cost + self.commission * self.contracts_landed)
    
    

@dataclass
class SalariedEmployee:
    """ Employee that is paid on a fixed monthly salary """
    
    name: str
    id: int
    commission: float = 100
    contracts_landed: float = 0
    monthly_salary: float = 0
    percentage: float = 1
    
    def compute_pay(self) -> float:
        """ Compute how much the employee should be paid """
        
        return (self.monthly_salary * self.percentage + self.commission * self.contracts_landed)
    

@dataclass
class Freelancer:
    """ Freelancer that is paid based on numbers of hours worked """
    
    name: str 
    id: int
    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0 
    vat_number: str = ""
    
    def compute_pay(self) -> float:
        """ Compute how much the employee should be paid """
        
        return (self.pay_rate * self.hours_worked + self.commission * self.contracts_landed)
    
    
def main() -> None:
    """ Main function """
    
    henry = HourlyEmployee(name="Henry", id=389238, pay_rate=45, hours_worked=123)
    print(f"{henry.name} worked for {henry.hours_worked} and earned ${henry.compute_pay()}")
    
    sarah = SalariedEmployee(name="Sarah", id=80789, commission=345, contracts_landed=4, monthly_salary=3400, percentage=1.1)
    print(f"{sarah.name} landed {sarah.contracts_landed} and earned ${sarah.compute_pay()}")
    
    
if __name__ == "__main__":
    main()
    
    
    