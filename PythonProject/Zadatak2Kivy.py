from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button


class ScrollApp(App):
    def build(self):
        scroll = ScrollView()

        layout = GridLayout( cols=2, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        labela1 = Label(text='Item',size_hint_y=None, height=40)
        self.text_input1 = TextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(labela1)
        layout.add_widget(self.text_input1)

        self.labela4 = Label(text='', size_hint_y=None, height=40)

        button = Button(text='Submit', size_hint_y=None, height=40)
        button.bind(on_press=self.prikazi_unos)
        layout.add_widget(button)
        layout.add_widget(self.labela4)

        for i in range(30):
            lbl1 = Label(text=f'Label lijevo {i + 1}', size_hint_y=None, height=40)
            lbl2 = Label(text=f'Label desno {i + 1}', size_hint_y=None, height=40)
            layout.add_widget(lbl1)
            layout.add_widget(lbl2)

        scroll.add_widget(layout)
        return scroll


    def prikazi_unos(self, instance):
        tekst= self.text_input1.text
        if len(tekst)>5:
            tekst=tekst[:5]
        self.labela4.text = f"Labela: {tekst}"

if __name__ == '__main__':
    ScrollApp().run()