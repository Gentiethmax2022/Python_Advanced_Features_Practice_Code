
""" Basic video exporting example """

import pathlib 
from abc import ABC, abstractmethod

class VideoExporter(ABC):
    """ Basic representation of video exporting codec """
    
    @abstractmethod
    def prepare_export(self, video_data):
        """ Prepares video data for exporting """
        
        
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """ Exports the video data to a folder """
        

class LossLessVideoExporter(VideoExporter):
    """ Lossless Video Exporting codec """
    
    def prepare_export(self, video_data):
        print("Preparing video data for lossles export")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}")
        

class H264BPVideoexporter(VideoExporter):
    """ H.264 video exporting codec with Hi422P profile """
    
    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data for H.264 to {folder}")
        
class H455Videoexporter(VideoExporter):
    """ H455 video exporting codec """
    
    def prepare_export(self, video_data):
        print("Preparing video data for H455 ")
        
    def do_export(self, folder: pathlib.Path):
        print("Exporting video data for H455")
        

class AudioExporter(ABC):
    """ Basic representation of audio exporting codec """
    
    @abstractmethod
    def prepare_export(self, audio_data):
        """ Prepares audio data for exporting """
        
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """ Exports the audio data to a folder """
        
class AACAudioExporter(AudioExporter):
    """ AAC audio exporting codec """
    
    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export ")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in eAAC format in {folder}")
        
class WAVAudioExporter(AudioExporter):
    """ WAV (lossless) audio exporting codec"""
    
    def prepare_export(self, audio_data):
        print("Preparing audio data for export in WAV format")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Preparing audio data in WAV format in {folder}")
        

def main() -> None:
    
    # read the desired export quality 
    export_quality: str
    while True:
        export_quality = input("Please enter the desired output quality (low, high, master): ")
        if export_quality  in {"low", "high", "master"}:
            break
        
        print(f"Unknown output quality option: {export_quality}")
        
    # Create the video and audio exporters 
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    
    if export_quality == "low":
        video_exporter = H264BPVideoexporter()
        audio_exporter = AACAudioExporter()
    elif export_quality == "high":
        video_exporter = H455Videoexporter()
        audio_exporter = AACAudioExporter()
    else:
        # default: master quality
        video_exporter = LossLessVideoExporter()
        audio_exporter = WAVAudioExporter()
    
    # Prepare the export of data 
    video_exporter.prepare_export("placeholder for video data")
    audio_exporter.prepare_export("placeholder for audio data")
    
    # Do the export of data 
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)
    

if __name__ == "__main__":
    main()
        