from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.uix.button import Button

Window.size = (720, 400)

class AnchorLayoutExample(App):
   def build(self):
      root = GridLayout(rows=3, cols=2, spacing=10)
      lo = AnchorLayout(
         anchor_x='left', anchor_y='bottom', size_hint=(0.1, 0.1)
      )
      lo1 = AnchorLayout(
         anchor_x='right', anchor_y='bottom', size_hint=(0.1, 0.1)
      )
      lo2 = AnchorLayout(
         anchor_x='left', anchor_y='top', size_hint=(0.1, 0.1)
      )
      lo3 = AnchorLayout(
         anchor_x='left', anchor_y='top', size_hint=(0.1, 0.1)
      )
      lo4 = AnchorLayout(
         anchor_x='left', anchor_y='center', size_hint=(0.1, 0.1)
      )
      btn1=Button(text='Button 1')
      btn2 = Button(text='Button 2')
      btn3 = Button(text='Button 3')
      btn4 = Button(text='Button 4')
      btn5 = Button(text='Button 5')


      lo.add_widget(btn1)
      lo1.add_widget(btn2)
      lo2.add_widget(btn3)
      lo3.add_widget(btn4)
      lo4.add_widget(btn5)

      for lo in (lo, lo1, lo2, lo3, lo4):
         root.add_widget(lo)
      return root

if __name__ == '__main__':
   AnchorLayoutExample().run()