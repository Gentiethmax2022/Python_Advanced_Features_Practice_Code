from support.app import CustomerSupport, RandomOrderingStrategy
from support.ticket import SupportTicket

class BlackHoleStrategy:
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return []
    

def main():
    # Create the application 
    app = CustomerSupport()
    
    # Create a few tickets 
    app.add_ticket(SupportTicket("Alex Burgaj", "My SAP application is not working"))
    app.add_ticket(SupportTicket("Anna Martin", "My monitor doesnt work"))
    
    # Process the tickets 
    app.process_tickets(RandomOrderingStrategy())
    
if __name__ == "__main__":
    main()