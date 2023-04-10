import logging

from stream.dslr_camera import dslr_camera
from stream.twitch_stream import TwitchStreamingService
from stream.webcam import webcam
from stream.youtube_stream import YoutubeStreamingService


def main() -> None:
    # Setup logging 
    logging.basicConfig(level=logging.INFO)
    
    # Create a device and a streaming service 
    service = YoutubeStreamingService()
    service.add_device(webcam)
    
    # Start streaming 
    reference = service.start_stream()
    service.fill_buffer(reference)
    service.stop_stream(reference)
    
    # Create another device and streaming service 
    service2 = TwitchStreamingService()
    service2.add_device(dslr_camera)
    service2.add_device(webcam)
    
    # Start streaming there as well 
    reference2 = service2.start_stream()
    service2.fill_buffer(reference2)
    service2.stop_stream(reference2)
    
    
if __name__ == "__main__":
    main()
    
    