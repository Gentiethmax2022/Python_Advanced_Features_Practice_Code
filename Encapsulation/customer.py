from dataclasses import dataclass

def send_mail(to: str, subject: str, body: str) -> None:
    print(f"Sending email to: {to}")
    print(f"Subject: {subject}")
    print("Body")
    print(body)
    
    
@dataclass
class Customer:
    id: str 
    name: str
    email_address: str
    
    def __post_init__(self):
        self.send_welcome_email()
        
    def send_welcome_email(self):
        subject = "Welcome to our Platform"
        body = (
            f"Hi, {self.name}, we are so glad you joined our platform"
            f"Here is a tutorial to help you get started: https://..... Hope you find this helpful"
        )
        send_mail(self.email_address, subject, body)
        
        