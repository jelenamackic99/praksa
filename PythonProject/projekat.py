import threading
import time
import serial
import random

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton

class RelativelayoutExample(App):
    def build(self):
        self.ser = serial.Serial('/dev/serial0', 9600, timeout=1)

        self.trenutna_slika_index = 0
        self.slike = ["Kivy_logo.png",
                      "Python.png"]
        self.flag = False
        self.running = False
        self.our_time = 0
        self.layout = RelativeLayout()

        self.human_button = ToggleButton(text='HUMAN',group='mode', state='down',size_hint=(0.2, 0.1), pos_hint={'x': 0.05, 'top': 0.9})
        self.layout.add_widget(self.human_button)

        self.ai_button = ToggleButton(text='AI',group='mode', size_hint=(0.2, 0.1), pos_hint={'x': 0.3, 'top': 0.9})
        self.layout.add_widget(self.ai_button)



        self.label = Label(text='', size_hint=(0.2, 0.4), pos_hint={'right': 0.95, 'top': 1})
        self.layout.add_widget(self.label)

        self.button = Button(text='START', size_hint=(0.3, 0.1), pos_hint={'right': 0.95, 'y': 0.5})
        self.button.bind(on_press=self.pokreni)
        self.layout.add_widget(self.button)

        self.image = Image(source=self.slike[self.trenutna_slika_index],
                           size_hint=(0.4, 0.5),
                           pos_hint={'right': 0.5, 'y': 0.2},
                           keep_ratio=True)
        self.layout.add_widget(self.image)

        self.rx_thread = threading.Thread(target=self.receive, daemon=True)
        self.rx_thread.start()

        return self.layout

    def pokreni(self, instance):
        if not self.running:
            self.our_time = 0
            self.event = Clock.schedule_interval(self.azuriraj_vrijeme, 0.02)
            self.event2=Clock.schedule_interval(self.promijeni_sliku, 5)
            self.flag=True
            self.button.text = 'STOP'
            self.running = True
            tx_thread = threading.Thread(target=self.send)
            tx_thread.start()
        else:
            self.event.cancel()
            self.event2.cancel()
            self.flag=False
            self.button.text = 'START'
            self.running = False

    def azuriraj_vrijeme(self,dt):
        self.our_time += dt
        self.label.text = f'Timer: {self.our_time:.2f}'

    def promijeni_sliku(self, dt):
        if self.flag:
            self.trenutna_slika_index = (self.trenutna_slika_index + 1) % 2
            self.image.source = self.slike[self.trenutna_slika_index]
            self.image.reload()

    def send(self):
        mode = 'HUMAN' if self.human_button.state == 'down' else 'AI'
        message = f"MODE: {mode}, CMD: start\n"
        print(f"[TX] Sent: {message.strip()}")
        self.ser.write(message.encode())

    def receive(self):
        while True:
            if self.ser.in_waiting > 0:
                data = self.ser.readline()
                if data:
                    received = data.decode().strip()
                    print(f"[RX] Received: {received}")

                    sleep_time = random.randint(2, 10)
                    print(f"[RX] Simulating work for {sleep_time} second(s)")
                    time.sleep(sleep_time)

                    Clock.schedule_once(lambda dt: self.zaustavi_tajmer(), 0)

    def on_stop(self):
        self.ser.close()

    def zaustavi_tajmer(self):
        if self.running:
            self.event.cancel()
            self.event2.cancel()
            self.flag = False
            self.button.text = 'START'
            self.running = False

if __name__ == '__main__':
    RelativelayoutExample().run()