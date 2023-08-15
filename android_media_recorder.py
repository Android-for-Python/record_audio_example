#
# Derived from
# https://developer.android.com/guide/topics/media/platform/mediarecorder
#
from kivy.logger import Logger
from jnius import autoclass

MediaRecorder = autoclass('android.media.MediaRecorder')
AudioSource = autoclass('android.media.MediaRecorder$AudioSource')
OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')
AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')

class AndroidMediaRecorder():

    def __init__(self, file_name, **kwargs):
        super().__init__(**kwargs)
        self.file_name = file_name

    def start(self):
        self.recorder = MediaRecorder()
        self.recorder.setAudioSource(AudioSource.MIC)
        self.recorder.setOutputFormat(OutputFormat.THREE_GPP)
        self.recorder.setOutputFile(self.file_name)
        self.recorder.setAudioEncoder(AudioEncoder.AMR_NB)
        try:
            self.recorder.prepare()
        except Exception as e:
            Logger.warning('Android Media Recorder prepare() failed.\n' +\
                           str(e))
        else:
            self.recorder.start()
    
    def stop(self):
        self.recorder.release()
        self.recorder = None        
