import random 
from typing import Callable
from support.ticket import SupportTicket

TicketOrderingStrategy = Callable[[list[SupportTicket]], list[SupportTicket]]


def fifo_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return tickets.copy()

def lifo_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return list(reversed(tickets))

def random_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return random.sample(tickets, len(tickets))


class CustomerSupport:
    def __init__(self):
        self.tickets: list[SupportTicket] = []
        
    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)
        
    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        # Create the ordered list 
        ticket_list = processing_strategy(self.tickets)
        
        # if its empty dont do anything 
        if len(self.tickets) == 0:
            print("There are no tickets to process")
            return 
        
        # Go through the tickets in the list 
        for ticket in ticket_list:
            ticket.process()
            
    