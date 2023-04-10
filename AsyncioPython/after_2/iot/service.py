import asyncio
import random 
import string 
from typing import Any, Awaitable, Protocol

from iot.message import MessageType, Message


def generate_id(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=length))


class Device(Protocol):
    async def connect(self) -> None:
        ...
        
    async def disconnect(self) -> None:
        ...
        
    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        ...
        
        
class IOTService:
    def __init__(self):
        self.devices: dict[str, Device] = {}
        
    async def register_device(self, device: Device) -> str:
        await device.connect()
        device_id = generate_id()
        self.devices[device_id] = device 
        return device_id 
    
    async def unregister_device(self, device_id: str) -> None:
        await self.devices[device_id].disconnect()
        del self.devices[device_id]
        
    def get_device(self, device_id: str) -> Device:
        return self.devices[device_id]
    
    async def run_program(self, program: list[Message]) -> None:
        print("========= RUNNING THE PROGRAM ============")
        await asyncio.gather(*[self.send_msg(msg) for msg in program])
        print("============= END OF THE PROGRAM ==========")
        
    async def send_msg(self, message: Message) -> None:
        await self.devices[message.device_id].send_message(message.msg_type, message.data)
        
        
        