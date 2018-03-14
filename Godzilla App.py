# Logan Czernel : First Kivy App 

from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation
from time import sleep
from random import randrange

# Credits to the following files in README.txt
main_sound = SoundLoader.load('godzilla_sound.wav')
main_icon = 'godzilla_icon.ico'
main_button = 'godzilla_img.png'

class MyButton(ButtonBehavior, Image):
    """
    The main feature; displays Godzilla and shakes.
    """
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = main_button
    def shake(self):
        sleep(0.05)
        anim = Animation()
        for i in range(100):
            new_x = randrange(-2, 2)
            new_y = randrange(-2, 2)
            anim += Animation(x=new_x, y=new_y, duration=0.04)
        anim.start(self)
    def on_touch_down(self, touch):
        main_sound.play()
        self.shake()

class MyLayout(AnchorLayout):
    """
    The layout (anchor in order to keep the button centered)
    """
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.add_widget(MyButton())

class MyGodzillaApp(App):
    """
    Main class: builds app, changes colour to white + updates that rectangle.
    """
    def build(self):
        self.title = 'Roar'
        self.icon = main_icon
        self.root = root = MyLayout()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MyGodzillaApp().run()
