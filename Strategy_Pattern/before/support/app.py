import random 
from support.ticket import SupportTicket

class CustomerSupport:
    def __init__(self):
        self.tickets: list[SupportTicket] = []
        
    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)
        
    def process_tickets(self, processing_strategy: str = "fifo"):
        # if the it's empty don't do anything 
        if len(self.tickets) == 0:
            print("There are no Tickets to process")
            return
        
        if processing_strategy == "fifo":
            for ticket in self.tickets:
                ticket.process()
        elif processing_strategy == "lifo":
            for ticket in reversed(self.tickets):
                ticket.process()
        elif processing_strategy == "random":
            random_list = random.sample(self.tickets, len(self.tickets))
            for ticket in random_list:
                ticket.process()
        