from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.label = Label(text='Hello world', font_size=50)
        return self.label
    

if __name__ == '__main__':
    MyApp().run()
