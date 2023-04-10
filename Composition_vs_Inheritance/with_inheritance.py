""" Very advanced Employee management system """

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Employee(ABC):
    """ Basic representation of an employee at the company """
    
    name: str
    id: int
    
    @abstractmethod
    def compute_pay(self) -> float:
        """ Compute how much the employee should be paid """
        

@dataclass
class HourlyEmployee(Employee):
    """ Employee that is paid based on number of hours worked """
    
    pay_rate: float
    hours_worked: int = 0 
    employer_cost: float = 1000
    
    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost
    
    
@dataclass
class SalariedEmployee(Employee):
    """ Employeer that is paid based on a fixed monthly salary """
    
    monthly_salary: float
    percentage: float = 1 
    
    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage
    

@dataclass
class Freelancer(Employee):
    """ Freelancer that is paid based on the number of hours worked """
    
    pay_rate: float 
    hours_worked: int = 0 
    vat_number: str = ""
    
    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked
    

@dataclass
class  SalariedEmployeeWithCommission(SalariedEmployee):
    """ Employee that is paid based on fixed monthly salary and that gets a commission """
    
    commission: float = 100
    contracts_landed: float = 0 
    
    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed
    

@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    """ Employee that is paid based on number of hours worked and gets a commisssion"""
    
    commission: float = 100
    contracts_landed: float = 0 
    
    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed
    

@dataclass
class FreelancerWithCommission(Freelancer):
    """ Freelancer that is paid based on number of hours worked and gets a commission """
    
    commission: float = 100 
    contracts_landed: float = 0
    
    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed
    

def main() -> None:
    """ Main Function """
    
    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()