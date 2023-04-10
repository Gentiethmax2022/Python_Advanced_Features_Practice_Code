import random 
from typing import Callable, Optional

from support.ticket import SupportTicket

TicketOrderingStrategy = Callable[[list[SupportTicket]], list[SupportTicket]]

def fifo_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return tickets.copy()

def lifo_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return list(reversed(tickets))

def random_strategy_generator(seed: Optional[int] = None) -> TicketOrderingStrategy:
    """ This function takes an optional seed argument and returns an inner function (which returns the random list with or without the seed)"""
    use_seed = False
    
    def random_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
        if use_seed:
            random.seed(seed)
        return random.sample(tickets, len(tickets))
    
    return random_strategy

class CustomerSupport:
    def __init__(self) -> None:
        self.tickets: list[SupportTicket] = []
        
    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)
    
    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        # Create the ordered list 
        ticket_list = processing_strategy(self.tickets)
        
        if len(self.tickets) == 0:
            print("There are no tickets to process")
            return 
        
        for ticket in ticket_list:
            ticket.process()
            
    
    