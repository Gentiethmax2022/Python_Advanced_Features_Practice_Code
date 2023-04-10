""" Basic video exporting example"""

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
    """ Lossless video exporting codec """
    
    def prepare_export(self, video_data):
        print("Preparing video data for lossless export ")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}")
        
class H264VideoExporter(VideoExporter):
    """ H264 video exporting codec """
    
    def prepare_export(self, video_data):
        print("Preparing video data in H264 format")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting H264 video format data in {folder}")
        
class H466VideoExporter(VideoExporter):
    """ H466 video exporting codec """
    
    def prepare_export(self, video_data):
        print("Preparing video data in H466 format ")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H466 format in {folder}")
        

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
        print("Preparing audio data for AAC export")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Doing export for AAC audio data in {folder}")
        
class WAVAudioExporter(AudioExporter):
    """ WAV audio exporter codec """
    
    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV format ")
        
    def do_export(self, folder: pathlib.Path):
        print(f"Doing export in WAV format in {folder}")
        

class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codecs
    The factory doesn't maintain any of the instances that it creates 
    
    """
    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """ Returns a new video exporter instance belonging to this factory """
      
    @abstractmethod  
    def get_audio_exporter(self) -> AudioExporter:
        """ Returns a new audio exporter instance belonging to this factory """
        
class FastExporter(ExporterFactory):
    """ Factory aimed at providing a high speed, low quality export """
    
    def get_video_exporter(self) -> VideoExporter:
        return H264VideoExporter()
    
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()
    
class HighQualityExporter(ExporterFactory):
    """ Factory aimed at providing lower speed but high quality export """
    
    def get_video_exporter(self) -> VideoExporter:
        return H466VideoExporter()
    
    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()
    
class MasterQualityExporter(ExporterFactory):
    """ Factory aimed at providing low speed, master quality export """
    
    def get_video_exporter(self) -> VideoExporter:
        return LossLessVideoExporter()
    
    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()
    

def read_factory() -> ExporterFactory:
    """ Construct an exporter factory based on the user preferences """
    
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter(),
    }
    while True:
        export_quality = input("Please enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}")
    
def main(factory: ExporterFactory) -> None:
    
    # retrieve the exporters 
    video_exporter = factory.get_video_exporter()
    audio_exporter = factory.get_audio_exporter()
    
    # prepare the export 
    video_exporter.prepare_export("placeholder for video data ")
    audio_exporter.prepare_export("placeholder for audio data")
    
    # do the export 
    folder = pathlib.Path("/usr/temp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)
    
if __name__ == "__main__":
    # create the factory 
    factory = read_factory()
    
    # perform the exporting job
    main(factory)
    
    
    