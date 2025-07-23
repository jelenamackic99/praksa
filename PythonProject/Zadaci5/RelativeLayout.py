from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

class RelativeLayoutExample(App):
    def build(self):
        layout = RelativeLayout()
        btn1=Button(text='Button 1', size_hint=(0.2, 0.1), pos_hint={'right': 0.5, 'y': 0.0})
        btn2 = Button(text='Button 2', size_hint=(0.2, 0.1), pos_hint={'right': 0.5, 'y': 0.25})
        btn3 = Button(text='Button 3', size_hint=(0.2, 0.1), pos_hint={'right': 1, 'y': 0.0})
        btn4 = Button(text='Button 4', size_hint=(0.2, 0.1), pos_hint={'right': 1, 'y': 0.25})
        btn5 = Button(text='Button 5', size_hint=(0.2, 0.1), pos_hint={'right': 1, 'y': 0.5})
        for btn in [btn1, btn2, btn3, btn4, btn5]:
            layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    RelativeLayoutExample().run()