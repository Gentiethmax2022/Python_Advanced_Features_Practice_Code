from support.app import CustomerSupport
from support.ticket import SupportTicket

class BlackHoleStrategy:
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return []
    

# same thing but using a function 
def black_hole_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    print("Everything is going in the black hole")
    return []


def main():
    # Create the application 
    app = CustomerSupport()
    
    # Create a few tickets 
    app.add_ticket(SupportTicket("John Smith", "My computer makes strange sounds!"))
    app.add_ticket(
        SupportTicket("Linus Sebastian", "I can't upload any videos, please help.")
    )
    app.add_ticket(
        SupportTicket("Arjan Codes", "VSCode doesn't automatically solve my bugs.")
    )

    app.process_tickets(black_hole_strategy)
    
if __name__ == "__main__":
    main()