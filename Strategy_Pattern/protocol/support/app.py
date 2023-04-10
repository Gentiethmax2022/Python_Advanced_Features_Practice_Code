import random 
from dataclasses import dataclass
from typing import Optional, Protocol

from support.ticket import SupportTicket

class TicketOrderingStrategy(Protocol):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        """ Returns  an ordered list of tickets """
        ...
        
class FifoOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return tickets.copy()
    
class LifoOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return list(reversed(tickets))
    

@dataclass
class RandomOrderingStrategy:
    seed: Optional[int] = None
    
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        tickets_copy = tickets.copy()
        random.seed(self.seed)
        random.shuffle(tickets_copy)
        return tickets_copy
    
    
class CustomerSupport:
    def __init__(self):
        self.tickets: list[SupportTicket] = []
        
    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)
        
    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        ticket_list = processing_strategy.create_ordering(self.tickets)
        
        if len(self.tickets) == 0:
            print("There are no tickets to process")
            return 
        
        for ticket in ticket_list:
            ticket.process()
            
            