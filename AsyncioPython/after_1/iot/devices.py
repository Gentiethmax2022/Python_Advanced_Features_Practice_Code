import asyncio
from iot.message import MessageType

class HueLightDevice:
    async def connect(self) -> None:
        print("Connecting Hue Light")
        await asyncio.sleep(1)
        print("Hue Light Connected")
        
    async def disconnect(self) -> None:
        print("Disconnecting the Hue Light")
        await asyncio.sleep(1)
        print("Hue Light disconnected")
        
    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(f"Hue Light handling message of type {message_type.name} with data [{data}]")
        await asyncio.sleep(1)               
        print("Hue Light received message")
        
        
class SmartSpeaker:
    async def connect(self) -> None:
        print("Connecting Smart Speaker")
        await asyncio.sleep(0.5)
        print("Smart Speaker Connected")
        
    async def disconnect(self) -> None:
        print("Disconnecting the Smart Speaker")
        await asyncio.sleep(0.5)
        print("Smart Speaker disconnected")
        
    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(f"Smart Speaker handling message of type {message_type.name} with data [{data}]")
        await asyncio.sleep(0.5)               
        print("Smart Speaker received message")
        
class SmartToiletDevice:
    async def connect(self) -> None:
        print("Connecting Smart Toilet")
        await asyncio.sleep(0.5)
        print("Smart Toilet Connected")
        
    async def disconnect(self) -> None:
        print("Disconnecting the Smart Speaker")
        await asyncio.sleep(0.5)
        print("Smart Toilet disconnected")
        
    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(f"Smart Toilet handling message of type {message_type.name} with data [{data}]")
        await asyncio.sleep(0.5)               
        print("Smart Toilet received message")
        
        