#import kivy
import os
os.environ["KIVY_NO_ARGS"] = "1"
os.environ['KIVY_IMAGE'] = "pil,sdl2" # use pil instead of SDL2 image if you get the libpng16 error
# you must add to the path the location of your SDL2 binaries
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\glew\\bin')
os.environ['PATH'] += ';' + os.path.expandvars('%AppData%\\Python\\share\\sdl2\\bin')

from kivy.app import App
from kivy.uix.label import Label

class Hogweed(App):
    def build(self):
    	return Label(text="hi")

    	
if __name__ == "__main__":
    Hogweed().run()