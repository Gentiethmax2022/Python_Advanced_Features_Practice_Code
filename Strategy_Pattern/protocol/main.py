from support.app import CustomerSupport, RandomOrderingStrategy
from support.ticket import SupportTicket

class BlackHoleStrategy:
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return []
    

def main():
    app = CustomerSupport()
    
    # create a few tickets
    app.add_ticket(SupportTicket("John Smith", "My computer makes strange sounds!"))
    app.add_ticket(
        SupportTicket("Linus Sebastian", "I can't upload any videos, please help.")
    )
    app.add_ticket(
        SupportTicket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")
    )
    
    app.process_tickets(RandomOrderingStrategy(seed=9))
    

if __name__ == "__main__":
    main()