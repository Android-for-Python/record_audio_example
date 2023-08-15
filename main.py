#
# Derived from
# https://developer.android.com/guide/topics/media/platform/mediarecorder
#

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior

from android import mActivity
from android_permissions import AndroidPermissions
from android_media_recorder import AndroidMediaRecorder
from android_media_player import AndroidMediaPlayer

from os.path import join


class ToggleButton(ToggleButtonBehavior, Button):
    
    def __init__(self, action, **kwargs):
        super().__init__(**kwargs)
        self.action = action  
        self.disabled = True

    def on_state(self, widget, value):
        if self.action:
            self.action(value)


class MyApp(App):

    ##################
    # Layout
    ##################

    def build(self, **args):
        self.record = ToggleButton(self.record_action, text = 'Record')
        self.play = ToggleButton(self.play_action, text = 'Play')
        l = BoxLayout(orientation='vertical')
        l.add_widget(self.record)
        l.add_widget(self.play)
        return l
         
    ##################
    # State Machine
    ##################

    def record_action(self, state):
        if state == 'down':
            self.record.text = 'Stop'
            self.play.disabled = True
            self.amr = AndroidMediaRecorder(self.file_name)
            self.amr.start()
        else:
            self.record.text = 'Record'
            self.play.disabled = False
            self.amr.stop()
            self.amr = None

    def play_action(self, state):
        if state == 'down':
            self.play.text = 'Stop'
            self.record.disabled = True
            self.amp = AndroidMediaPlayer(self.file_name)
            self.amp.start()
        else:
            self.play.text = 'Play'
            self.record.disabled = False
            self.amp.stop()
            self.amp = None

    ##################
    # Lifecycle events
    ##################

    def on_start(self):
        self.dont_gc = AndroidPermissions(self.start_app)

    def start_app(self):
        self.dont_gc = None        
        cache = mActivity.getApplicationContext().getExternalCacheDir()
        if cache:
            self.file_name = join(str(cache.toString()), 'whatever.3gp')
            self.record.disabled = False

    def on_pause(self):
        self.record.state = 'normal'
        self.play.state = 'normal'
        return True
        
MyApp().run()



                         
