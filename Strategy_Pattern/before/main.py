from support.app import CustomerSupport
from support.ticket import SupportTicket


def main() -> None:
    # Create the application 
    app = CustomerSupport()
    
    # Register a few tickets 
    app.add_ticket(SupportTicket("Alex Burgaj", "Cannot access my SAP application. It crashes"))
    app.add_ticket(SupportTicket("Anita Biba", "My monitor shows a black screen"))
    app.add_ticket(SupportTicket("Enny Bratwole", "I don't want to work today. I am broken"))
    
    # Process the tickets 
    app.process_tickets("fifo")
    
    
if __name__ == "__main__":
    main()
    
    
    