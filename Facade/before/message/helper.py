import base64
from dataclasses import dataclass

@dataclass
class Message:
    sender: str
    receiver: str
    content: str
    b64: str = ""
    
    def __post_init__(self) -> None:
        self.b64 = self._to_base64__()
        
    def _to_base64__(self) -> str:
        message_bytes = f"{self.sender}{self.receiver}{self.content}".encode("ascii")
        base64_bytes = base64.b64encode(message_bytes)
        return base64_bytes.decode("ascii")
    
    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}: {self.content}"
    
    