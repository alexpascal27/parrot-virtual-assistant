###KIVY
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.switch import Switch
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.config import Config
from kivy.uix.image import Image
from kivy.core.window import Window
###
import threading
import webbrowser
import time
###INTERNAL
from scripts.VA import assistant,speak,myCommand

#window settings
#############Config.set('graphics', 'resizable', '0')##############
Window.size = (400, 700)
#background colour
Window.clearcolor = (93.9, 94.3, 94.7, 1)

class IconButton(ButtonBehavior, Image):
    pass

class UI(App):

    def build(self):
        #layout
        self.layout = FloatLayout()
        # main screen widgets
        self.listen_b = Button(text = "Listen", font_size=30, pos=(130,180), size_hint=(.375,.115))
        self.listen_b.bind(on_release = self.function)
        self.quit_b = Button(text = "Quit", font_size=30, pos=(130,50), size_hint=(.375,.115))
        self.quit_b.bind(on_press = lambda b: stop())
        self.standby_gif = Image(source = 'media/parrot_sleeping.gif', size_hint=(.75, .429), pos = (50, 320), anim_delay = 0.05, anim_loop = 0)
        self.settings_b = IconButton(source="media/settings.png", pos=(330,630), size_hint=(0.12,0.0686),on_press = self.to_settings_screen)
        self.info_b = IconButton(source = "media/info.png", size_hint=(0.12,0.0686),pos=(20,630),on_press = self.to_info_screen)
        #settings screen widgets
        self.settings_title = Label(text = "[color=413b49]Settings[/color]", markup=True, font_size=45, pos=(150,615), size_hint=(.375,.115))
        self.news_source = Spinner(text='Google News', values=('Google News','BBC News', 'Buzzfeed', 'Al Jazeera', 'NY Times', 'CNN'), size_hint=(.9, .1), font_size=38, pos=(20,450))
        self.settings = Label(text = "[color=413b49]News Sources:\n\n\n\n\n\n\n\n\n\n\n\nDark Theme:[/color]", markup=True, halign = "left", font_size=30, pos=(-60,270), size_hint=(.9,.2))
        self.theme_switch = Switch(active=False, pos=(190, 55), size_hint=(.5, .2))
        #info screen widgets
        self.info_title = Label(text = "[color=413b49]Information[/color]", markup=True, font_size=45, pos=(150,615), size_hint=(.375,.115))
        self.title_separator = Label(text = "[color=413b49]_________________[/color]", markup=True,font_size=45, pos=(125,580), size_hint=(.375,.115))
        self.back_b = IconButton(source = "media/back.png", size_hint=(0.12,0.0686),pos=(20,630),on_press = self.to_main_screen)
        self.information = Label(text = "[color=413b49] Refer to the [color=000000]README file[/color] \n for  information about \n content used in making[/color]\n\n\n[color=413b49]Build: [/color][color=000000]1.0[/color]\n\n\n[color=413b49]About maker:[/color]\n [color=000000]Alex Zamurca \n Aspiring Developerr[/color]", halign="center", markup = True,font_size=30, pos=(20,280), size_hint=(.9,.2))
        self.github = IconButton(source = "media/github.png", size_hint=(.16,.0914),pos=(80,50), on_press= self.open_github)
        self.stack = IconButton(source = "media/stack.png", size_hint=(.16,.0914),pos=(260,50) , on_press=self.open_stack)
        #pop-up
        self.popup_layout = FloatLayout()
        self.popup_info = Label(text="Be sure to \nhave your \nMICROPHONE \nat a MEDIUM \nINPUT LEVEL \n(between 30-60%)\n and AVOID\n being TOO CLOSE\n to the \nMICROPHONE", halign="center", pos=(110,170),font_size=30, size_hint=(.6, .8))
        self.close_popup_b = Button(text="Close Pop-Up", halign="center",font_size=30,pos=(65,100), size_hint=(.9,.1))
        self.close_popup_b.bind(on_press = self.popup_close)
        self.popup_layout.add_widget(self.close_popup_b)
        self.popup_layout.add_widget(self.popup_info)
        self.popup = Popup(title = "     FOR A MORE RESPONSIVE EXPERIENCE",content = self.popup_layout, size_hint=(.8,.8), auto_dismiss=False)
        self.popup.open()

        #show layout in window
        return self.layout

    def popup_close(self, instance, *args):
        self.popup.dismiss()
        #adding widgets main screen by default
        self.layout.add_widget(self.listen_b)
        self.layout.add_widget(self.quit_b)
        self.layout.add_widget(self.standby_gif)
        self.layout.add_widget(self.info_b)
        self.layout.add_widget(self.settings_b)

    def open_stack(self, instance, *args):
        webbrowser.open('alexzamurca.github.io/')

    def open_github(self, instance, *args):
        webbrowser.open('https://github.com/alexzamurca')

    def to_info_screen(self, instance, *args):
        self.layout.remove_widget(self.listen_b)
        self.layout.remove_widget(self.quit_b)
        self.layout.remove_widget(self.standby_gif)
        self.layout.remove_widget(self.info_b)
        self.layout.remove_widget(self.settings_b)
        #animation
        time.sleep(.5)
        #adding
        self.layout.add_widget(self.info_title)
        self.layout.add_widget(self.information)
        self.layout.add_widget(self.back_b)
        self.layout.add_widget(self.title_separator)
        self.layout.add_widget(self.github)
        self.layout.add_widget(self.stack)

    def to_main_screen(self, instance, *args):
        self.layout.remove_widget(self.information)
        self.layout.remove_widget(self.back_b)
        self.layout.remove_widget(self.info_title)
        self.layout.remove_widget(self.title_separator)
        self.layout.remove_widget(self.settings_title)
        self.layout.remove_widget(self.github)
        self.layout.remove_widget(self.stack)
        self.layout.remove_widget(self.news_source)
        self.layout.remove_widget(self.settings)
        self.layout.remove_widget(self.theme_switch)
        #animation
        time.sleep(.5)
        #adding
        self.layout.add_widget(self.listen_b)
        self.layout.add_widget(self.quit_b)
        self.layout.add_widget(self.standby_gif)
        self.layout.add_widget(self.info_b)
        self.layout.add_widget(self.settings_b)

    def to_settings_screen(self, instance, *args):
        self.layout.remove_widget(self.listen_b)
        self.layout.remove_widget(self.quit_b)
        self.layout.remove_widget(self.standby_gif)
        self.layout.remove_widget(self.info_b)
        self.layout.remove_widget(self.settings_b)
        #animation
        time.sleep(.5)
        #adding
        self.layout.add_widget(self.back_b)
        self.layout.add_widget(self.settings_title)
        self.layout.add_widget(self.title_separator)
        self.layout.add_widget(self.news_source)
        self.layout.add_widget(self.settings)
        self.layout.add_widget(self.theme_switch)

    def open_va_script(self, instance, *args):
        #disable listen button
        self.listen_b.disabled = True
        #Virtual assitant
        speak('Hi, Alex, what can I do for you? ')
        assistant(myCommand())
        #re-enable listen button
        self.listen_b.disabled = False

    def function(self, instance, *args):
        #threading GUI and va_script (running them simultaneously)
        threading.Thread(target=self.open_va_script, args=(1,)).start()

#Run the app
if __name__ == '__main__':
	UI().run()
