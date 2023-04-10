class HueLightDevice:
    def connect(self) -> None:
        print("Connecting to Hue light ")
        
    def disconnect(self) -> None:
        print("Disconnecting the Hue Light")
        
    def status_update(self) -> str:
        return "Hue Light status ok"
    
    def connection_info(self) -> tuple[str, int]:
        return "192.168.1.100", 1234
    

class SmartSpeakerDevice:
    def connect(self) -> None:
        print("Connecting to smart speaker")
        
    def disconnect(self) -> None:
        print("Disconnecting the smart speaker")
        
    def status_update(self) -> str:
        return "smart_speaker_status_is_ok"
        
    def connection_info(self) -> tuple[str, int]:
        return "193.168.1.101", 2368
    

class CurtainDevice:
    def connect(self) -> None:
        print("Connecting to curtains ")
        
    def disconnect(self) -> None:
        print("Disconnecting curtains ")
        
    def status_update(self) -> str:
        return "status of curtains is ok"
    
    def connection_info(self) -> tuple[str, int]:
        return "192.168.1.101", 2369