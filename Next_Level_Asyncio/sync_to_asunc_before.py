import asyncio 
import time 
import requests


async def counter(until: int = 10) -> None:
    now = time.perf_counter()
    print("Started counter")
    for i in range (0, until):
        last = now 
        await asyncio.sleep(0.1)
        now = time.perf_counter()
        print(f"{i}: was asleep for {now - last} seconds")
        

def send_request(url: str) -> int:
    print("Sending HTTP requests")
    response = requests.get(url)
    return response.status_code


async def main() -> None:
    
    status_code = send_request("https://arjancodes.com")
    print(f"Got HTTP response with status {status_code}")
    
    await counter()
    
    
asyncio.run(main())

