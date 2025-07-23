from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class GridLayoutExample(App):
    def build(self):
        layout = GridLayout(rows=4, cols=2, spacing=10)

        labela1=Label(text='Ime')
        self.text_input1 = TextInput(multiline=False)
        layout.add_widget(labela1)
        layout.add_widget(self.text_input1)

        labela2=Label(text='Prezime')
        self.text_input2 = TextInput(multiline=False)
        layout.add_widget(labela2)
        layout.add_widget(self.text_input2)

        labela3 = Label(text='Godine')
        self.text_input3 = TextInput(multiline=False, input_filter='int')  # samo brojevi
        layout.add_widget(labela3)
        layout.add_widget(self.text_input3)

        self.labela4=Label(text='')
        button = Button(text='Prikazi unos')
        button.bind(on_press=self.prikazi_unos)
        layout.add_widget(button)
        layout.add_widget(self.labela4)


        return layout

    def prikazi_unos(self,instance):
        ime = self.text_input1.text
        prezime = self.text_input2.text
        godine = self.text_input3.text
        self.labela4.text = f"Ime: {ime}, Prezime: {prezime}, Godine: {godine}"
if __name__ == '__main__':
    GridLayoutExample().run()