from dataclasses import dataclass
from enum import Enum
from typing import Any


class PaymentStatus(Enum):
    CANCELLED = "cancelled"
    PENDING = "pending"
    PAID = "paid"
    

class PaymentStatusError(Exception):
    pass 


@dataclass
class OrderNoEncapsulationNoInformatonHiding:
    """ Anyone can get the payment status directly via the instance variable.
    There are no boundaries whatsoever"""
    
    payment_status: PaymentStatus = PaymentStatus.PENDING
    
@dataclass
class OrderEncapsulationNoInformationHiding:
    """ There is an interface now that you should use that provides encapsulation.
    Users of this class still need to know that the status is represented by an enum type"""
    
    _payment_status: PaymentStatus = PaymentStatus.PENDING
    
    def get_payment_status(self) -> PaymentStatus:
        return self._payment_status
    
    def set_payment_status(self, status: PaymentStatus) -> None:
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError(
                "You cannot change the status of an already paid order"
            )
        self._payment_status = status
        

@dataclass
class OrderEncapsulationAndInformationHiding:
    """ The status variable is set to 'private'. The only thing you are supposed to use 
    is the is_paid method, you need no knowledge of how status is represented (the info is 'hidden')"""
    
    _payment_status: PaymentStatus = PaymentStatus.PENDING
    
    def is_paid(self) -> bool:
        return self._payment_status == PaymentStatus.PAID
    
    def is_cancelled(self) -> bool:
        return self._payment_status == PaymentStatus.CANCELLED
    
    def cancel(self) -> None:
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("You cannot cancel an already paid order")
        self._payment_status = PaymentStatus.CANCELLED
        
    def pay(self) -> None:
        if self._payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("Order is already paid")
        
        self._payment_status = PaymentStatus.PAID
        
        
@dataclass
class OrderInfromationHidingWithoutEncapsulation:
    """ The status variable is public again (so there is no boundary), 
    but we don't know what the type is - that info is hidden. I know, it's a bit
    of a contrived example - you wouldn't ever do this.
    But it shows that it is possible"""
    
    payment_status: Any = None
    
    def is_paid(self) -> bool:
        return self.payment_status == PaymentStatus.PAID
    
    def is_cancelled(self) -> bool:
        return self.payment_status == PaymentStatus.CANCELLED
    
    def cancel(self) -> None:
        if self.payment_status == PaymentStatus.PAID:
            raise PaymentStatusError("You cannot cancel an already paid order")
        self.payment_status = PaymentStatus.CANCELLED
        
    def pay(self) -> None:
        if self.payment_status == PaymentStatus.PAID:
            raise PaymentStatusError()
    
    
    
def main() -> None:
    test = OrderInfromationHidingWithoutEncapsulation()
    test.pay()
    print(f"Is paid: {test.is_paid()}")
    

if __name__ == "__main__":
    main()
    
    
    