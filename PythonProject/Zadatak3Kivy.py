from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import time


class GridLayoutExample(App):
    def build(self):
        self.last_click_time = 0
        self.click_index = 0

        layout = GridLayout(rows=6, cols=3, spacing=10)
        button1 = Button(text='1(, . ? !)')
        button2 = Button(text='2(abc)')
        button3 = Button(text='3(def)')
        button4 = Button(text='4(ghi)')
        button5 = Button(text='5(jkl)')
        button6 = Button(text='6(mno)')
        button7 = Button(text='7(pqrs)')
        button8 = Button(text='8(tuv)')
        button9 = Button(text='9(wxyz)')
        button10 = Button(text='*+')
        button11 = Button(text='0')
        button12 = Button(text='#')



        self.click_count2 = 0  # broj klikova
        self.char_list2 = ['a', 'b', 'c', '2']
        button2.bind(on_press=self.handle_click2)

        # button.bind(on_press=self.prikazi_text_input1)
        for btn in [button1, button2, button3, button4, button5, button6, button7]:
            layout.add_widget(btn)
        for btn in [button8, button9, button10, button11, button12]:
            layout.add_widget(btn)

        self.text_input1 = TextInput(multiline=False)
        layout.add_widget(self.text_input1)

        self.labela1 = Label(text='')
        layout.add_widget(self.labela1)

        button13 = Button(text='Posalji poruku')
        layout.add_widget(button13)
        button14 = Button(text='Izbrisi sve')
        layout.add_widget(button14)

        return layout

    def handle_click2(self, instance):
        current_time = time.time()
        if current_time - self.last_click_time <= 0.5:
            if self.click_index == 0:
                self.click_index = 1
            else:
                self.click_index = (self.click_index + 1) % len(self.char_list2)
            char_to_insert = self.char_list2[self.click_index]
            # Zameni poslednji karakter
            if len(self.text_input1.text) > 0:
                self.text_input1.text = self.text_input1.text[:-1] + char_to_insert
            else:
                self.text_input1.text += char_to_insert
        else:
            # Novi unos, dodaj novi karakter 'a' i resetuj brojač
            self.click_index = 0
            self.text_input1.text += self.char_list2[self.click_index]

        self.last_click_time = current_time
if __name__ == '__main__':
    GridLayoutExample().run()