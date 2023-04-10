from support.app import CustomerSupport, TicketOrderingStrategy
from support.ticket import SupportTicket

class BlackHoleStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return []
    

def main():
    # Create the application 
    app = CustomerSupport()
    
    # Create a few tickets 
    app.add_ticket(SupportTicket("Alex Burgaj", "My SAP application is not working"))
    app.add_ticket(SupportTicket("Anna Martin", "My pc won't start"))
    
    # Process the tickets 
    app.process_tickets(BlackHoleStrategy())
    

if __name__ == "__main__":
    main()
    
    