from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IOTService


def main() -> None:
    # Create a IOT Service 
    service = IOTService()
    
    # Create and register a few devices 
    hue_light = HueLightDevice()
    speaker = SmartSpeakerDevice()
    toilet = SmartToiletDevice()
    hue_light_id = service.register_device(hue_light)
    speaker_id = service.register_device(speaker)
    toilet_id = service.register_device(toilet)
    
    # Create a few programs 
    wake_up_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(toilet_id, MessageType.PLAY_SONG)
    ]
    
    sleep_program = [
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
        Message(toilet_id, MessageType.FLUSH),
        Message(toilet_id, MessageType.CLEAN)
    ]
    
    # Run the programs 
    service.run_program(wake_up_program)
    service.run_program(sleep_program)
    
    
if __name__ == "__main__":
    main()