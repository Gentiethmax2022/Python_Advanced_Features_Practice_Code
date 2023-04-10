import random 
from abc import ABC, abstractmethod

from support.ticket import SupportTicket

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        """ Returns an ordered list of tickets """
        

class FifoStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return tickets.copy()
    
class LifoOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return list(reversed(tickets))
    
class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return list(random.sample(tickets, len(tickets)))
    

class CustomerSupport:
    def __init__(self):
        self.tickets: list[SupportTicket] = []
        
    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)
        
    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        # Create the ordered list
        ticket_list = processing_strategy.create_ordering(self.tickets)
        
        # if its empty don't do anything 
        if len(ticket_list) == 0:
            print("There are no tickets to process")
            return 
        
        # Go through the tickets to process
        for ticket in ticket_list:
            ticket.process()
            
