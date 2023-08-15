#
# Derived from
# https://developer.android.com/guide/topics/media/platform/mediarecorder
#
from kivy.logger import Logger
from jnius import autoclass

MediaPlayer = autoclass('android.media.MediaPlayer')

class AndroidMediaPlayer():

    def __init__(self, file_name, **kwargs):
        super().__init__(**kwargs)
        self.file_name = file_name

    def start(self):
        self.player = MediaPlayer()
        try:
            self.player.setDataSource(self.file_name)
            self.player.prepare()
            self.player.start()
        except Exception as e:
            Logger.warning('Android Media Player prepare() failed.\n' +\
                           str(e))
    
    def stop(self):
        self.player.release()
        self.player = None        
