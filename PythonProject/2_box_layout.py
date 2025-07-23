from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        button1 = Button(text='Button 1')
        layout.add_widget(button1)
        layout.add_widget(Button(text='Button 2'))
        layout.add_widget(Button(text='Button 3'))
        layout.add_widget(Button(text='Button 4'))
        layout.add_widget(Button(text='Button 5'))
        return layout

if __name__ == '__main__':
    BoxLayoutExample().run()
