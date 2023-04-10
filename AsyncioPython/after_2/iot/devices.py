import asyncio
from iot.message import MessageType


class HueLightDevice:
    async def connect(self) -> None:
        print("Connecting Hue Light")
        await asyncio.sleep(2)
        print("Hue Light connected")
        
    async def disconnect(self) -> None:
        print("Disconnecting Hue Light")
        await asyncio.sleep(2)
        print("Disconnecting Hue Light")
        
    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(f"Hue Light handling message of type {message_type.name} with data [{data}]")
        
class SmartSpeakerDevice:
    async def connect(self) -> None:
        print("Connecting Smart Speaker")
        await asyncio.sleep(2)
        print("Smart Speaker connected")
        
    async def disconnect(self) -> None:
        print("Disconnecting Smart Speaker")
        await asyncio.sleep(2)
        print("Disconnecting Smart speaker")
        
    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(f"Smart Speaker handling message of type {message_type.name} with data [{data}]")
        
        
class SmartToiletDevice:
    async def connect(self) -> None:
        print("Connecting Smart Toilet")
        await asyncio.sleep(2)
        print("Smart Toilet connected")
        
    async def disconnect(self) -> None:
        print("Disconnecting Smart Toilet")
        await asyncio.sleep(2)
        print("Disconnecting Smart Toilet")
        
    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(f"Smart Toilet handling message of type {message_type.name} with data [{data}]")
        
        
